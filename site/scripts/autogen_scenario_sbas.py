#!/usr/bin/env python3
"""Generate PasTest/Mediscope-style clinical scenario SBAs from authored source.

For each source topic in /mnt/tb/Medicine/<chapter>/.../topic.md, reads
real authored clinical content and generates 2-5 clinical scenario SBAs
that test real clinical knowledge.

Each scenario follows the PasTest/Mediscope format:

    "A 65-year-old man presents with 3-day history of productive cough,
     fever 39°C, and right pleuritic chest pain. On examination: RR 28,
     SpO2 92% on room air, bronchial breathing right lower zone.
     What is the most appropriate initial severity assessment?"

SBA types generated (only when the underlying fact is found in the source):
  1. TRIAD_RECOGNITION  — "Which condition is characterised by: [triad]?"
  2. SPECIFIC_FEATURE   — "Which of the following is specific to [disease]?"
  3. SCORE_INTERPRET    — "What does [score] of N indicate?"
  4. FIRST_LINE_RX      — "First-line therapy for [disease]?"
  5. AVOID_PITFALL      — "Which is contraindicated in [condition]?"
  6. TRIAL_RECALL       — "Which trial showed [finding] in [condition]?"
  7. NUMERIC_THRESHOLD  — "What value of [parameter] indicates [severity]?"

Each scenario is built from real authored text. The answer is the
ground-truth from the source. Distractors are drawn from a curated pool
of common alternative conditions/tests/options.

Output is APPENDED to the published tree at:
    chapters/<chapter>/diseases/<topic>/topic.md

A new section is added:
    ## PasTest Scenario SBAs (Clinical Vignettes)

It does NOT pollute the existing MCQ/SBA/Flashcard sections. Re-runnable
(skips topics that already have the section).
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from collections import defaultdict

MED = Path('/mnt/tb/Medicine')
ROOT = Path('/mnt/tb/Sea-knowledge/#MedSea')
CHAPTERS = ROOT / 'chapters'

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SRC_TO_PUB = {
    'Acute Medicine and Critical Illness':     '10-acute-medicine',
    'Adolescent and Transition Medicine':     '31-adolescence-transition-and-young-adult-m',
    'Ageing and Disease':                     '32-older-adult-medicine-and-frailty',
    'Cardiology':                             '16-cardiology',
    'Chapter 7 - Poisoning':                  '11-poisoning',
    'Clinical Biochemistry and Metabolic Medicine': '19-clinical-biochemistry-and-metabolic-medi',
    'Clinical Decision-Making':               '1-clinical-decision-making',
    'Clinical Genetics':                      '3-clinical-genetics',
    'Clinical Immunology':                    '4-clinical-immunology',
    'Clinical Therapeutics and Good Prescribing': '2-clinical-therapeutics',
    'Dermatology':                            '26-dermatology',
    'Diabetes':                              '21-diabetes-mellitus',
    'Endocrinology':                          '20-endocrinology',
    'Envenomation':                           '12-envenomation',
    'Environmental medicine':                 '13-austere-medicine',
    'Gastroenterology':                       '22-gastroenterology',
    'Hematology':                             '24-haematology-and-transfusion-medicine',
    'Hepatology':                             '23-hepatology',
    'HIV Infection and AIDS':                  '7-principles-of-infection',
    'Infectious Disease':                     '14-infectious-disease',
    'Maternal Medicine':                      '30-maternal-medicine',
    'Medical Ophthalmology':                  '28-medical-ophthalmology',
    'Medical Psychiatry':                     '29-medical-psychiatry',
    'Nephrology and Urology':                 '18-nephrology-urology',
    'Nephrology and Urology 15':              '15-nephrology-urology',  # legacy
    'Neurology':                              '27-neurology-and-stroke-medicine',
    'Nutritional Factors in Disease':         '5-nutritional-factors',
    'Oncology':                               '8-oncology',
    'Pain and Palliative Care':               '9-palliative-care',
    'Population Health and Epidemiology':     '6-population-health',
    'Principles of Infectious Disease':       '7-principles-of-infection',
    'Respiratory':                            '17-respiratory-medicine',
    'Rheumatology':                           '25-rheumatology-and-bone-disease',
    'Sexually Transmitted Infections':        '15-sexually-transmitted-infections',
    'Stroke Medicine':                        '27-neurology-and-stroke-medicine',
}

CH_LABELS = {
    '10-acute-medicine':                      'Ch 10: Acute Medicine',
    '11-poisoning':                           'Ch 11: Poisoning',
    '12-envenomation':                        'Ch 12: Envenomation',
    '13-austere-medicine':                    'Ch 13: Austere Medicine',
    '14-infectious-disease':                  'Ch 14: Infectious Disease',
    '15-nephrology-urology':                  'Ch 15: Nephrology & Urology',
    '15-sexually-transmitted-infections':     'Ch 15b: STI',
    '16-cardiology':                          'Ch 16: Cardiology',
    '17-respiratory-medicine':                'Ch 17: Respiratory Medicine',
    '18-nephrology-urology':                  'Ch 18: Nephrology & Urology',
    '19-clinical-biochemistry-and-metabolic-medi': 'Ch 19: Clinical Biochemistry',
    '1-clinical-decision-making':             'Ch 1: Clinical Decision-Making',
    '20-endocrinology':                       'Ch 20: Endocrinology',
    '21-diabetes-mellitus':                   'Ch 21: Diabetes',
    '22-gastroenterology':                    'Ch 22: Gastroenterology',
    '23-hepatology':                          'Ch 23: Hepatology',
    '24-haematology-and-transfusion-medicine':'Ch 24: Haematology',
    '25-rheumatology-and-bone-disease':       'Ch 25: Rheumatology',
    '26-dermatology':                         'Ch 26: Dermatology',
    '27-neurology-and-stroke-medicine':       'Ch 27: Neurology & Stroke',
    '28-medical-ophthalmology':               'Ch 28: Medical Ophthalmology',
    '29-medical-psychiatry':                  'Ch 29: Medical Psychiatry',
    '2-clinical-therapeutics':                'Ch 2: Clinical Therapeutics',
    '30-maternal-medicine':                   'Ch 30: Maternal Medicine',
    '31-adolescence-transition-and-young-adult-m': 'Ch 31: Adolescent Medicine',
    '32-older-adult-medicine-and-frailty':    'Ch 32: Ageing & Disease',
    '3-clinical-genetics':                    'Ch 3: Clinical Genetics',
    '4-clinical-immunology':                  'Ch 4: Clinical Immunology',
    '5-nutritional-factors':                  'Ch 5: Nutritional Factors',
    '6-population-health':                    'Ch 6: Population Health',
    '7-principles-of-infection':              'Ch 7: Principles of Infection',
    '8-oncology':                             'Ch 8: Oncology',
    '9-palliative-care':                      'Ch 9: Palliative Care',
}

# Curated distractor pools per chapter area. These are *real* alternative
# conditions/treatments that are common in exam questions for the same
# clinical area. They are NOT fabricated per-question — they come from a
# hand-curated list of MRCP/FCPS-relevant alternatives.
DISTRACTOR_POOLS = {
    # Cardiology
    '16-cardiology': {
        'tamponade':     ['Constrictive pericarditis', 'Tension pneumothorax',
                          'Pulmonary embolism', 'Aortic dissection',
                          'Right ventricular infarct', 'Massive PE'],
        'acs':           ['Stable angina', 'Aortic dissection', 'Pericarditis',
                          'Pulmonary embolism', 'Oesophageal spasm',
                          'Musculoskeletal chest pain', 'Costochondritis'],
        'stemi':         ['NSTEMI', 'Pericarditis', 'Aortic dissection',
                          'Pulmonary embolism', 'Early repolarisation',
                          'LBBB (pre-existing)'],
        'heart_failure': ['COPD exacerbation', 'Pulmonary embolism',
                          'Cardiac tamponade', 'Constrictive pericarditis',
                          'ARDS', 'Severe anaemia'],
        'hfref':         ['ARVC', 'Hypertrophic cardiomyopathy', 'Restrictive cardiomyopathy',
                          'Pericardial constriction', 'Tachycardia-induced cardiomyopathy',
                          'Peripartum cardiomyopathy'],
        'hfpef':         ['HFrEF', 'Constrictive pericarditis',
                          'Restrictive cardiomyopathy', 'Amyloidosis',
                          'Hypertensive heart disease'],
        'af':            ['Atrial flutter', 'AVNRT', 'Atrial tachycardia',
                          'Frequent atrial ectopy', 'Multifocal atrial tachycardia',
                          'Atrial fibrillation with aberrancy'],
        'af_management': ['Atrial flutter', 'AVNRT', 'SVT', 'Ventricular tachycardia',
                          'AF with pre-excitation', 'Focal atrial tachycardia'],
        'htn':           ['White-coat hypertension', 'Pheochromocytoma',
                          'Renal artery stenosis', 'Hyperaldosteronism',
                          'Coarctation of the aorta', 'Cushing syndrome'],
        'as':            ['Aortic sclerosis', 'Subaortic membrane',
                          'HCM with LVOT obstruction', 'Mitral regurgitation',
                          'Supravalvular aortic stenosis'],
        'ms':            ['Mitral regurgitation', 'Atrial myxoma',
                          'Ball-valve thrombus', 'Cor triatriatum',
                          'Pulmonary vein stenosis'],
        'mr':            ['Mitral stenosis', 'VSD', 'HCM', 'Aortic stenosis',
                          'Tricuspid regurgitation'],
        'ie':            ['Infectious endocarditis', 'Non-bacterial thrombotic endocarditis',
                          'Marantic endocarditis', 'Rheumatic carditis',
                          'Libman-Sacks endocarditis'],
        'dcm':           ['Ischaemic cardiomyopathy', 'Tachycardia-induced cardiomyopathy',
                          'Peripartum cardiomyopathy', 'Infiltrative cardiomyopathy',
                          'Toxic cardiomyopathy (alcohol)', 'Chagas cardiomyopathy'],
        'hcm':           ['Athletic heart', 'Hypertensive heart disease',
                          'Aortic stenosis', 'Amyloidosis',
                          'Danon disease', 'Friedreich ataxia cardiomyopathy'],
        'icard':         ['Hypertensive heart disease', 'HCM', 'Dilated cardiomyopathy',
                          'Constrictive pericarditis', 'Sarcoidosis (cardiac)'],
        'pe':            ['Pneumonia', 'ACS', 'Aortic dissection',
                          'Pneumothorax', 'Pericarditis', 'Musculoskeletal pain'],
        'aaa':           ['Aortic dissection', 'Inflammatory AAA', 'RAAA',
                          'Aortitis', 'Renal colic', 'Pancreatitis'],
        'pad':           ['Venous insufficiency', 'Lumbar spinal stenosis',
                          'Diabetic neuropathy', 'Raynaud phenomenon',
                          'Thromboangiitis obliterans', 'Vasculitis'],
        'svt':           ['Sinus tachycardia', 'AF', 'Atrial flutter',
                          'Ventricular tachycardia', 'Anxiety-related palpitations'],
        'vt':            ['SVT with aberrancy', 'AF with pre-excitation',
                          'Torsades de pointes', 'Idioventricular rhythm',
                          'Hyperkalaemic ECG changes'],
        'arrhythmogenic':['HCM', 'Dilated cardiomyopathy', 'Myocarditis',
                          'Sarcoidosis (cardiac)', 'Brugada syndrome'],
        'default':       ['Hypertensive heart disease', 'Ischaemic heart disease',
                          'Valvular heart disease', 'Cardiomyopathy',
                          'Pericardial disease', 'Pulmonary embolism'],
    },
    # Respiratory
    '17-respiratory-medicine': {
        'pneumonia':     ['COPD exacerbation', 'Pulmonary embolism',
                          'Heart failure (pulmonary oedema)', 'Atelectasis',
                          'Lung abscess', 'Aspiration pneumonitis'],
        'cap':           ['HAP', 'Aspiration pneumonia', 'VAP', 'Lung abscess',
                         'TB', 'Fungal pneumonia'],
        'copd':          ['Asthma', 'Bronchiectasis', 'ILD', 'CHF',
                         'Bronchiolitis obliterans', 'Cystic fibrosis'],
        'asthma':        ['COPD', 'Vocal cord dysfunction', 'Bronchiectasis',
                          'Hyperventilation', 'GERD-related cough',
                          'Eosinophilic bronchitis'],
        'bronchiectasis':['COPD', 'Cystic fibrosis', 'TB', 'Lung abscess',
                          'ABPA', 'Sarcoidosis'],
        'tb':            ['Sarcoidosis', 'Lung cancer', 'Pneumonia',
                          'Fungal infection (histoplasmosis)',
                          'Atypical mycobacterial infection', 'Lung abscess'],
        'pe':            ['Pneumonia', 'Pneumothorax', 'ACS', 'Aortic dissection',
                         'Musculoskeletal chest pain', 'Pericarditis'],
        'pl_effusion':   ['Empyema', 'Haemothorax', 'Chylothorax', 'Transudate (CHF)',
                          'Malignant pleural effusion', 'TB pleural effusion'],
        'empyema':       ['Simple parapneumonic effusion', 'Lung abscess',
                          'Pneumonia', 'TB pleural effusion', 'Malignant effusion'],
        'ild':           ['Pulmonary oedema', 'Pneumonia', 'Sarcoidosis',
                          'Hypersensitivity pneumonitis', 'Drug-induced ILD',
                          'Connective tissue disease-ILD'],
        'ipf':           ['NSIP', 'Sarcoidosis', 'HP', 'Drug-induced ILD',
                         'Asbestosis', 'Connective tissue disease-ILD'],
        'lung_cancer':   ['Pneumonia', 'TB', 'Pulmonary nodule (benign)',
                          'Lymphoma', 'Mesothelioma', 'Lung abscess'],
        'osa':           ['Central sleep apnoea', 'Obesity hypoventilation',
                          'COPD', 'CHF (central apnoea)'],
        'occupational':  ['Asbestosis', 'Silicosis', 'Coal workers pneumoconiosis',
                          'Berylliosis', 'Hypersensitivity pneumonitis',
                          'Sarcoidosis'],
        'default':       ['Asthma', 'COPD', 'Pneumonia', 'Pulmonary embolism',
                          'Bronchiectasis', 'ILD'],
    },
    # Gastroenterology
    '22-gastroenterology': {
        'gerd':          ['Eosinophilic oesophagitis', 'Achalasia', 'Functional heartburn',
                          'Cardiac chest pain', 'Diffuse oesophageal spasm',
                          'Oesophageal web', 'Schatzki ring'],
        'peptic_ulcer':  ['GERD', 'Gastric cancer', 'Pancreatitis',
                          'Functional dyspepsia', 'Gastritis', 'Duodenitis',
                          'Biliary colic'],
        'ibs':           ['IBD', 'Coeliac disease', 'Microscopic colitis',
                          'Colorectal cancer', 'Bile acid diarrhoea',
                          'Lactose intolerance', 'Hyperthyroidism'],
        'ibd':           ['IBS', 'Infectious colitis', 'Ischaemic colitis',
                          'Colorectal cancer', 'Diverticulitis', 'Drug-induced colitis',
                          'Microscopic colitis'],
        'uc':            ['Crohn disease', 'Infectious colitis', 'Ischaemic colitis',
                          'Diverticulitis', 'Behçet colitis', 'Radiation colitis'],
        'crohn':         ['Ulcerative colitis', 'TB ileitis', 'Yersinia ileitis',
                          'Lymphoma', 'Sarcoidosis', 'NSAID enteropathy'],
        'cirrhosis':     ['Budd-Chiari', 'Veno-occlusive disease',
                          'Cardiac cirrhosis', 'Primary sclerosing cholangitis',
                          'Alcohol-related liver disease', 'NAFLD', 'Haemochromatosis'],
        'pancreatitis':  ['Biliary colic', 'Perforated peptic ulcer',
                          'Mesenteric ischaemia', 'AAA', 'Acute cholecystitis',
                          'Choledocholithiasis', 'Duodenal perforation'],
        # Pancreatic mass / tumour differential — for the Ch 22 pancreatic
        # cancer / adenocarcinoma / IPMN / cystic-fibrosis topics where the
        # rotator previously reached for "Hemorrhoids / IBS / UC" from the
        # default pool because there was no specific entry.
        'pancreatic_mass':['Cholangiocarcinoma', 'Duodenal adenocarcinoma',
                           'Ampullary carcinoma', 'Gastric cancer',
                           'Lymphoma', 'Autoimmune pancreatitis',
                           'Chronic pancreatitis'],
        'pancreatic_cyst':['Pseudocyst', 'IPMN', 'MCN', 'SPN',
                           'Serous cystadenoma', 'Mucinous cystadenoma',
                           'Solid pseudopapillary neoplasm'],
        'pancreatic_diabetes':['Type 1 DM', 'Type 2 DM', 'MODY', 'LADA',
                               'Steroid-induced hyperglycaemia',
                               'Chronic pancreatitis-related DM'],
        'pancreatic_exocrine':['Coeliac disease', 'IBS-D', 'Small bowel bacterial overgrowth',
                               'Microscopic colitis', 'Bile acid malabsorption',
                               'Short bowel syndrome'],
        'peptic_ulcer_complication':['Acute cholecystitis', 'Pancreatitis',
                                     'Mesenteric ischaemia', 'Small bowel obstruction',
                                     'Aortic dissection'],
        'upper_gi_bleed':['Variceal haemorrhage', 'Mallory-Weiss tear',
                          'Gastric angiodysplasia', 'Dieulafoy lesion',
                          'Gastric cancer', 'Erosive gastritis'],
        'lower_gi_bleed':['Angiodysplasia', 'Haemorrhoids', 'Anal fissure',
                          'Ischaemic colitis', 'Infectious colitis',
                          'Colorectal polyp'],
        'jaundice':       ['Hepatitis A', 'Hepatitis B', 'Hepatitis C',
                           'Alcoholic hepatitis', 'Primary biliary cholangitis',
                           'Gilbert syndrome', 'Drug-induced cholestasis'],
        'dysphagia':      ['Achalasia', 'Oesophageal web', 'Schatzki ring',
                           'Diffuse oesophageal spasm', 'Oesophageal cancer',
                           'Eosinophilic oesophagitis', 'Functional dysphagia'],
        'default':        ['GERD', 'IBS', 'IBD', 'Pancreatitis',
                           'Peptic ulcer', 'Gallstones', 'Coeliac disease'],
    },
    # Neurology
    '27-neurology-and-stroke-medicine': {
        'stroke':        ['TIA', 'Migraine with aura', 'Seizure (Todd paresis)',
                          'Hypoglycaemia'],
        'ischaemic':     ['Haemorrhagic stroke', 'TIA', 'Subdural haematoma',
                          'Brain tumour'],
        'haemorrhagic':  ['Ischaemic stroke', 'Subarachnoid haemorrhage',
                          'Subdural haematoma', 'Brain tumour'],
        'sah':           ['Ischaemic stroke', 'Migraine', 'Meningitis',
                          'Vertebral artery dissection'],
        'tia':           ['Stroke', 'Migraine with aura', 'Focal seizure',
                          'Hypoglycaemia'],
        'epilepsy':      ['PNES', 'Syncope', 'TIA', 'Migraine'],
        'ms':            ['ADEM', 'NMOSD', 'Small-vessel disease',
                          'Spinocerebellar ataxia'],
        'parkinsons':    ['Essential tremor', 'Drug-induced parkinsonism',
                          'Multiple system atrophy', 'Progressive supranuclear palsy'],
        'migraine':      ['Tension headache', 'Cluster headache', 'SAH',
                          'Trigeminal neuralgia'],
        'gbs':           ['CIDP', 'Myasthenic crisis', 'Botulism', 'Transverse myelitis'],
        'mnd':           ['Kennedy disease', 'Spinal muscular atrophy',
                          'CIDP', 'Inclusion body myositis'],
        'myasthenia':    ['Lambert-Eaton', 'Botulism', 'GBS', 'Polymyositis'],
        'default':       ['Stroke', 'TIA', 'Migraine', 'Seizure'],
    },
    # Endocrinology
    '20-endocrinology': {
        'diabetes':      ['Pre-diabetes', 'MODY', 'LADA', 'Type 1 DM'],
        'dka':           ['HHS', 'Euglycaemic DKA', 'Lactic acidosis',
                          'Starvation ketoacidosis'],
        'hhs':           ['DKA', 'Stroke', 'Hyperosmolar non-ketotic state',
                          'Sepsis'],
        'thyrotoxicosis':['Anxiety disorder', 'Phaeochromocytoma', 'Alcohol withdrawal',
                          'Sepsis'],
        'hypothyroid':   ['Depression', 'CFS', 'Fibromyalgia', 'Iron deficiency'],
        'addisons':      ['Secondary adrenal insufficiency', 'Hypopituitarism',
                          'Sepsis', 'Hypovolaemia'],
        'cushings':      ['PCOS', 'Metabolic syndrome', 'Obesity (exogenous)',
                          'Alcohol-related pseudo-Cushing'],
        'pheo':          ['Hyperthyroidism', 'Anxiety', 'Panic disorder',
                          'Carcinoid'],
        'default':       ['Type 2 diabetes', 'Hypothyroidism', 'Hypertension',
                          'Obesity'],
    },
    # Nephrology
    '15-nephrology-urology': {
        'aki':           ['Pre-renal AKI', 'Post-renal AKI', 'CKD',
                          'ATN'],
        'ckd':           ['AKI', 'Diabetic nephropathy', 'Hypertensive nephropathy',
                          'Polycystic kidney disease'],
        'gn':            ['Minimal change disease', 'FSGS', 'Membranous nephropathy',
                          'IgA nephropathy'],
        'rsa':           ['Fibromuscular dysplasia', 'Atherosclerotic RAS',
                          'Phaeochromocytoma', 'Coarctation'],
        'default':       ['AKI', 'CKD', 'UTI', 'Nephrolithiasis'],
    },
    '18-nephrology-urology': {
        'aki':           ['Pre-renal AKI', 'Post-renal AKI', 'CKD',
                          'ATN'],
        'ckd':           ['AKI', 'Diabetic nephropathy', 'Hypertensive nephropathy',
                          'Polycystic kidney disease'],
        'gn':            ['Minimal change disease', 'FSGS', 'Membranous nephropathy',
                          'IgA nephropathy'],
        'rsa':           ['Fibromuscular dysplasia', 'Atherosclerotic RAS',
                          'Phaeochromocytoma', 'Coarctation'],
        'stone':         ['Calcium oxalate stone', 'Uric acid stone',
                          'Struvite stone', 'Cystine stone'],
        'uti':           ['Cystitis', 'Pyelonephritis', 'Urethritis',
                          'Asymptomatic bacteriuria'],
        'default':       ['AKI', 'CKD', 'UTI', 'Nephrolithiasis'],
    },
    # Hepatology
    '23-hepatology': {
        'hepatitis_b':   ['Hepatitis C', 'Hepatitis A', 'Hepatitis D',
                          'Autoimmune hepatitis'],
        'hepatitis_c':   ['Hepatitis B', 'NAFLD', 'Autoimmune hepatitis',
                          'Primary biliary cholangitis'],
        'cirrhosis':     ['Budd-Chiari', 'Cardiac cirrhosis', 'PSC',
                          'Haemochromatosis'],
        'pbc':           ['PSC', 'Autoimmune hepatitis', 'Viral hepatitis',
                          'Sarcoidosis of liver'],
        'psc':           ['PBC', 'Choledocholithiasis', 'Cholangiocarcinoma',
                          'IgG4 disease'],
        'ai_hep':        ['Viral hepatitis', 'PBC', 'PSC', 'Drug-induced hepatitis'],
        'nafld':         ['ALD', 'Viral hepatitis', 'Haemochromatosis',
                          'Autoimmune hepatitis'],
        'wilson':        ['Haemochromatosis', 'Autoimmune hepatitis',
                          'Viral hepatitis', 'Alpha-1 antitrypsin deficiency'],
        'hemochrom':     ['Wilson disease', 'Sideroblastic anaemia',
                          'Thalassaemia', 'Secondary iron overload'],
        'hcc':           ['Cholangiocarcinoma', 'Metastatic liver disease',
                          'Hepatic adenoma', 'FNH'],
        'default':       ['NAFLD', 'ALD', 'Viral hepatitis', 'Autoimmune hepatitis'],
    },
    # Infectious disease
    '14-infectious-disease': {
        'sepsis':        ['SIRS', 'Septic shock', 'Severe sepsis',
                          'Multi-organ dysfunction'],
        'meningitis':    ['Encephalitis', 'Brain abscess', 'Subarachnoid haemorrhage',
                          'Migraine'],
        'endocarditis':  ['Rheumatic fever', 'SLE', 'Antiphospholipid syndrome',
                          'Atrial myxoma'],
        'tb':            ['Sarcoidosis', 'Lung cancer', 'Atypical mycobacteria',
                          'Fungal infection'],
        'malaria':       ['Typhoid', 'Dengue', 'Viral hepatitis', 'Sepsis'],
        'hiv':           ['Acute retroviral syndrome', 'EBV', 'CMV',
                          'Lymphoma'],
        'default':       ['Sepsis', 'Pneumonia', 'UTI', 'Meningitis'],
    },
    # Haematology
    '24-haematology-and-transfusion-medicine': {
        'anaemia':       ['Iron deficiency', 'B12 deficiency', 'Folate deficiency',
                          'Anaemia of chronic disease'],
        'itp':           ['TTP', 'HIT', 'DIC', 'Aplastic anaemia'],
        'ttp':           ['ITP', 'HUS', 'DIC', 'Evans syndrome'],
        'dic':           ['TTP', 'HUS', 'Liver failure', 'Massive transfusion'],
        'leukaemia':     ['Lymphoma', 'Myeloma', 'MDS', 'Aplastic anaemia'],
        'lymphoma':      ['Leukaemia', 'Metastatic carcinoma', 'Sarcoidosis',
                          'Infectious mononucleosis'],
        'myeloma':       ['MGUS', 'Waldenström', 'Lymphoma', 'Metastatic disease'],
        'default':       ['Iron deficiency anaemia', 'B12 deficiency',
                          'Anaemia of chronic disease', 'Haemolytic anaemia'],
    },
    # Rheumatology
    '25-rheumatology-and-bone-disease': {
        'ra':            ['Psoriatic arthritis', 'SLE', 'Polymyalgia rheumatica',
                          'Reactive arthritis'],
        'sle':           ['RA', 'Mixed connective tissue disease', 'Sjögren',
                          'Dermatomyositis'],
        'scleroderma':   ['SLE', 'MCTD', 'Eosinophilic fasciitis',
                          'Scleroedema'],
        'polymyalgia':   ['RA', 'Statin-induced myopathy', 'Hypothyroidism',
                          'Fibromyalgia'],
        'gca':           ['Takayasu arteritis', 'PAN', 'ANCA vasculitis',
                          'Polyarteritis nodosa'],
        'anca':          ['SLE', 'IgA vasculitis', 'Cryoglobulinaemia',
                          'Anti-GBM disease'],
        'osteoporosis':  ['Osteomalacia', 'Paget disease', 'Metastatic bone disease',
                          'Multiple myeloma'],
        'default':       ['RA', 'SLE', 'Polymyalgia', 'Gout'],
    },
    # Dermatology
    '26-dermatology': {
        'default':       ['Eczema', 'Psoriasis', 'Drug eruption', 'Cellulitis'],
    },
    # Oncology
    '8-oncology': {
        'default':       ['Chemotherapy', 'Radiotherapy', 'Surgery',
                          'Targeted/biological therapy'],
    },
    # Maternal Medicine
    '30-maternal-medicine': {
        'preeclampsia':  ['Chronic hypertension', 'Gestational hypertension',
                          'Renal disease', 'Essential HTN'],
        'hellp':         ['AFLP', 'Severe preeclampsia', 'ITP', 'Dengue'],
        'aflp':          ['HELLP', 'Severe preeclampsia', 'Hepatitis',
                          'Cholecystitis'],
        'default':       ['Pre-eclampsia', 'Gestational diabetes',
                          'Anaemia', 'VTE'],
    },
    # Acute Medicine
    '10-acute-medicine': {
        'sepsis':        ['SIRS', 'Septic shock', 'Severe sepsis',
                          'MODS'],
        'anaphylaxis':   ['Asthma exacerbation', 'Vasovagal episode',
                          'Panic attack', 'MI'],
        'default':       ['Sepsis', 'DKA', 'PE', 'MI'],
    },
    # Poisoning
    '11-poisoning': {
        'paracetamol':   ['Salicylate poisoning', 'Methanol poisoning',
                          'Ethylene glycol poisoning', 'Iron poisoning'],
        'opioid':        ['Benzodiazepine overdose', 'TCA overdose',
                          'Alcohol intoxication', 'CO poisoning'],
        'tca':           ['Sodium-channel blockade from antiarrhythmic',
                          'Beta-blocker toxicity', 'Calcium-channel blocker toxicity',
                          'Digoxin toxicity'],
        'default':       ['Paracetamol overdose', 'Salicylate overdose',
                          'Opioid overdose', 'Organophosphate poisoning'],
    },
    # Diabetes Mellitus
    '21-diabetes-mellitus': {
        'dka':           ['HHS', 'Euglycaemic DKA', 'Lactic acidosis',
                          'Starvation ketoacidosis'],
        'hhs':           ['DKA', 'Stroke', 'Hyperosmolar non-ketotic state',
                          'Sepsis'],
        't1dm':          ['T2DM', 'MODY', 'LADA', 'Pancreatic diabetes'],
        't2dm':          ['T1DM', 'MODY', 'LADA', 'Steroid-induced diabetes'],
        'dkd':           ['Hypertensive nephropathy', 'IgA nephropathy',
                          'Polycystic kidney disease', 'Interstitial nephritis'],
        'default':       ['T1DM', 'T2DM', 'DKA', 'HHS', 'Hypoglycaemia'],
    },
    # Medical Ophthalmology
    '28-medical-ophthalmology': {
        'amaurosis':     ['Retinal vein occlusion', 'Ischaemic optic neuropathy',
                          'Vitreous haemorrhage', 'Retinal detachment'],
        'gca':           ['Takayasu arteritis', 'Polyarteritis nodosa',
                          'Granulomatosis with polyangiitis', 'Behçet disease'],
        'glaucoma':      ['Acute angle-closure glaucoma', 'Open-angle glaucoma',
                          'Neovascular glaucoma', 'Secondary glaucoma'],
        'default':       ['Anterior uveitis', 'Optic neuritis', 'GCA',
                          'Central retinal artery occlusion'],
    },
    # Clinical Decision-Making
    '1-clinical-decision-making': {
        'diagnostic':    ['Sensitivity', 'Specificity',
                          'Positive predictive value',
                          'Negative predictive value'],
        'screening':     ['Sensitivity', 'Specificity',
                          'Lead-time bias', 'Length-time bias'],
        'evidence':      ['Randomised controlled trial',
                          'Meta-analysis', 'Cohort study', 'Case-control study'],
        'default':       ['Sensitivity', 'Specificity',
                          'Number needed to treat',
                          'Number needed to harm'],
    },
    # Clinical Therapeutics
    '2-clinical-therapeutics': {
        'prescribing':   ['ACE inhibitor', 'Beta-blocker',
                          'Calcium channel blocker', 'Thiazide diuretic'],
        'prescription':  ['Antibiotic course', 'Analgesic ladder step',
                          'Antihypertensive titration',
                          'Insulin sliding scale'],
        'adverse':       ['Allergic reaction', 'Idiosyncratic reaction',
                          'Type A adverse drug reaction',
                          'Type B adverse drug reaction'],
        'default':       ['ACE inhibitor', 'Beta-blocker', 'Statin',
                          'Metformin'],
    },
    # Clinical Genetics
    '3-clinical-genetics': {
        'inheritance':   ['Autosomal dominant', 'Autosomal recessive',
                          'X-linked recessive', 'Mitochondrial'],
        'mutation':      ['Point mutation', 'Frameshift mutation',
                          'Splice-site mutation', 'Trinucleotide repeat'],
        'screening':     ['Carrier testing', 'Predictive testing',
                          'Prenatal testing', 'Newborn screening'],
        'default':       ['Autosomal dominant', 'Autosomal recessive',
                          'X-linked recessive', 'Mitochondrial'],
    },
    # Clinical Immunology
    '4-clinical-immunology': {
        'autoimmune':    ['Systemic lupus erythematosus',
                          'Rheumatoid arthritis', 'Sjögren syndrome',
                          'Systemic sclerosis'],
        'immunodeficiency': ['Common variable immunodeficiency',
                            'X-linked agammaglobulinaemia',
                            'Severe combined immunodeficiency',
                            'Chronic granulomatous disease'],
        'allergy':       ['Type I hypersensitivity', 'Type II hypersensitivity',
                          'Type III hypersensitivity',
                          'Type IV hypersensitivity'],
        'default':       ['SLE', 'RA', 'Sjögren', 'Systemic sclerosis'],
    },
    # Nutritional Factors
    '5-nutritional-factors': {
        'vitamin':       ['Vitamin A deficiency', 'Vitamin B12 deficiency',
                          'Vitamin C deficiency', 'Vitamin D deficiency'],
        'mineral':       ['Iron deficiency', 'Zinc deficiency',
                          'Selenium deficiency', 'Copper deficiency'],
        'refeeding':     ['Hypophosphataemia', 'Hypokalaemia',
                          'Hypomagnesaemia', 'Thiamine deficiency'],
        'default':       ['Iron-deficiency anaemia', 'Vitamin D deficiency',
                          'Vitamin B12 deficiency', 'Folate deficiency'],
    },
    # Population Health
    '6-population-health': {
        'study':         ['Randomised controlled trial', 'Cohort study',
                          'Case-control study', 'Cross-sectional study'],
        'bias':          ['Selection bias', 'Recall bias', 'Observer bias',
                          'Confounding'],
        'screening':     ['Sensitivity', 'Specificity',
                          'Positive predictive value',
                          'Wilson-Jungner criteria'],
        'default':       ['Randomised controlled trial', 'Cohort study',
                          'Case-control study', 'Meta-analysis'],
    },
    # Principles of Infection
    '7-principles-of-infection': {
        'antibiotic':    ['Beta-lactam', 'Aminoglycoside', 'Macrolide',
                          'Fluoroquinolone'],
        'resistance':    ['MRSA', 'VRE', 'ESBL-producing organism',
                          'Carbapenem-resistant Enterobacteriaceae'],
        'vaccine':       ['Live attenuated', 'Inactivated', 'Subunit',
                          'Toxoid'],
        'default':       ['Gram-positive cocci', 'Gram-negative bacilli',
                          'Anaerobes', 'Atypical organisms'],
    },
    # Palliative Care
    '9-palliative-care': {
        'pain':          ['WHO analgesic ladder step 1', 'Step 2',
                          'Step 3', 'Adjuvant analgesic'],
        'symptom':       ['Dyspnoea', 'Nausea and vomiting', 'Agitation',
                          'Constipation'],
        'communication': ['Breaking bad news (SPIKES)',
                          'Advance care planning',
                          'End-of-life care discussion',
                          'Family meeting'],
        'default':       ['Morphine', 'Oxycodone', 'Gabapentin',
                          'Hyoscine butylbromide'],
    },
    # Envenomation
    '12-envenomation': {
        'snake':         ['Viper bite', 'Elapid bite',
                          'Colubrid bite', 'Sea snake bite'],
        'scorpion':      ['Centruroides', 'Tityus', 'Mesobuthus',
                          'Androctonus'],
        'spider':        ['Latrodectus (widow)', 'Loxosceles (recluse)',
                          'Phoneutria (banana)', 'Atrax (Sydney funnel-web)'],
        'default':       ['Snake bite', 'Scorpion sting', 'Spider bite',
                          'Bee/wasp sting'],
    },
    # Austere Medicine
    '13-austere-medicine': {
        'environmental': ['Heat stroke', 'Hypothermia', 'Frostbite',
                          'Acute mountain sickness'],
        'water':         ['Cholera', 'Typhoid', 'Hepatitis A',
                          'Bacillary dysentery'],
        'disaster':      ['Mass-casualty triage', 'Tetanus',
                          'Communicable disease outbreak',
                          'Malnutrition'],
        'default':       ['Heat illness', 'Hypothermia', 'Drowning',
                          'High-altitude pulmonary oedema'],
    },
    # STI
    '15-sexually-transmitted-infections': {
        'ulcer':         ['Syphilis', 'Chancroid', 'Lymphogranuloma venereum',
                          'Granuloma inguinale'],
        'discharge':     ['Gonorrhoea', 'Chlamydia', 'Trichomoniasis',
                          'Bacterial vaginosis'],
        'systemic':      ['HIV', 'Syphilis (secondary)',
                          'Hepatitis B', 'Disseminated gonococcal infection'],
        'default':       ['Gonorrhoea', 'Chlamydia', 'Syphilis', 'HIV'],
    },
    # Biochemistry
    '19-clinical-biochemistry-and-metabolic-medi': {
        'acidbase':      ['Respiratory acidosis', 'Respiratory alkalosis',
                          'Metabolic acidosis', 'Metabolic alkalosis'],
        'electrolyte':   ['Hyponatraemia', 'Hypernatraemia',
                          'Hypokalaemia', 'Hyperkalaemia'],
        'endocrine':     ['Primary hyperparathyroidism',
                          'Secondary hyperparathyroidism',
                          'Hypoparathyroidism',
                          'Pseudohypoparathyroidism'],
        'default':       ['Hyponatraemia', 'Hypokalaemia',
                          'Hypercalcaemia', 'Metabolic acidosis'],
    },
    # Medical Psychiatry
    '29-medical-psychiatry': {
        'mood':          ['Major depressive disorder', 'Bipolar disorder',
                          'Persistent depressive disorder',
                          'Postpartum depression'],
        'anxiety':       ['Generalised anxiety disorder',
                          'Panic disorder', 'PTSD', 'OCD'],
        'substance':     ['Alcohol use disorder', 'Opioid use disorder',
                          'Benzodiazepine dependence',
                          'Stimulant use disorder'],
        'somatic':        ['Somatic symptom disorder',
                          'Illness anxiety disorder',
                          'Conversion disorder', 'Factitious disorder'],
        'default':       ['Major depressive disorder', 'Anxiety disorder',
                          'Substance use disorder', 'Dementia'],
    },
    # Adolescence
    '31-adolescence-transition-and-young-adult-m': {
        'developmental': ['Delayed puberty', 'Precocious puberty',
                          'Turner syndrome', 'Klinefelter syndrome'],
        'eating':        ['Anorexia nervosa', 'Bulimia nervosa',
                          'Binge eating disorder', 'ARFID'],
        'mental_health': ['Depression', 'Anxiety disorder',
                          'Self-harm / suicide attempt',
                          'Eating disorder'],
        'default':       ['Depression in adolescents', 'Eating disorder',
                          'Substance misuse', 'Acne vulgaris'],
    },
    # Older Adult
    '32-older-adult-medicine-and-frailty': {
        'cognitive':     ['Alzheimer disease', 'Vascular dementia',
                          'Dementia with Lewy bodies',
                          'Frontotemporal dementia'],
        'falls':         ['Syncope', 'Vestibular dysfunction',
                          'Orthostatic hypotension', 'Polypharmacy'],
        'frailty':       ['Frailty syndrome', 'Sarcopenia',
                          'Cachexia', 'Multimorbidity'],
        'default':       ['Dementia', 'Delirium', 'Falls', 'Frailty'],
    },
}

# Generic distractor pool (when no chapter-specific)
GENERIC_DISTRACTORS = {
    'condition': [
        'A related condition in the same clinical area',
        'A common mimicker with overlapping features',
        'A complication rather than the underlying disease',
        'A less common alternative diagnosis',
    ],
    'investigation': [
        'An advanced imaging modality (e.g., MRI/CT)',
        'Invasive testing as first-line',
        'Empirical treatment without further investigation',
        'Watchful waiting with serial review',
    ],
    'treatment': [
        'Conservative management only',
        'Most aggressive advanced therapy as first-line',
        'Surgical intervention',
        'Targeted/biological therapy',
    ],
}


# ---------------------------------------------------------------------------
# Section extraction
# ---------------------------------------------------------------------------

H2_RE = re.compile(r'^##\s+([^\n]+)', re.M)


def get_h2_sections(text: str) -> list[tuple[str, str]]:
    """Return list of (header, body) for every H2 section."""
    matches = list(H2_RE.finditer(text))
    out = []
    for i, m in enumerate(matches):
        header = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        out.append((header, body))
    return out


def find_section(sections: list[tuple[str, str]], *needles: str) -> str | None:
    needles_lc = [n.lower() for n in needles]
    for header, body in sections:
        h = header.lower()
        for n in needles_lc:
            if n in h:
                return body
    return None


def topic_title_from_path(path: Path) -> str:
    name = path.stem
    name = re.sub(r'^[\d.]+\s+', '', name)
    name = name.replace('_', ' ').strip()
    if not name:
        name = path.parent.name
    # If still very long, try to take a short title from the first phrase
    if len(name) > 60:
        # Take up to first comma or first 50 chars
        short = re.split(r'[,;]| — | - ', name)[0]
        name = short.strip()[:50]
    return name


def topic_keyword(title: str) -> str:
    """Derive a single keyword for distractor lookup from topic title."""
    t = title.lower()
    # Cardiac-specific mappings
    if 'tamponade' in t or 'pericardial' in t: return 'tamponade'
    if 'acute coronary' in t or 'stemi' in t or 'nstemi' in t or 'acs' in t: return 'acs'
    if 'heart failure' in t or 'hf' in t and 'hfpef' in t: return 'hfpef'
    if 'hfr' in t or 'systolic heart' in t: return 'hfref'
    if 'atrial fibril' in t or 'af ' in t: return 'af'
    if 'aortic steno' in t or t.endswith('as'): return 'as'
    if 'mitral steno' in t or t.endswith('ms'): return 'ms'
    if 'mitral regurg' in t or t.endswith('mr'): return 'mr'
    if 'aortic regurg' in t: return 'mr'
    if 'endocard' in t: return 'ie'
    if 'dilated' in t or 'dcm' in t: return 'dcm'
    if 'hypertrophic' in t or 'hcm' in t: return 'hcm'
    if 'restrictive' in t or 'infiltrative' in t: return 'icard'
    if 'pulm embolism' in t or 'pe ' in t or t.endswith('pe'): return 'pe'
    if 'aaa' in t or 'aortic aneurysm' in t: return 'aaa'
    if 'pad' in t or 'peripheral' in t: return 'pad'
    if 'hyperten' in t or 'htn' in t: return 'htn'
    if 'ischaemic' in t and 'heart' in t: return 'acs'
    if 'cardiomyopathy' in t: return 'dcm'
    # Respiratory
    if 'pneumonia' in t: return 'pneumonia'
    if 'cap' in t: return 'cap'
    if 'copd' in t or 'chronic obstruct' in t: return 'copd'
    if 'asthma' in t: return 'asthma'
    if 'bronchiect' in t: return 'bronchiectasis'
    if t.startswith('tb') or 'tuberculosis' in t: return 'tb'
    if 'pleural eff' in t: return 'pl_effusion'
    if 'empyema' in t: return 'empyema'
    if 'interstitial' in t or 'ild' in t: return 'ild'
    if 'ipf' in t or 'pulm fibrosis' in t: return 'ipf'
    if 'lung cancer' in t: return 'lung_cancer'
    if 'sleep apn' in t: return 'osa'
    # GI
    if 'gerd' in t or 'reflux' in t: return 'gerd'
    if 'peptic ulcer' in t: return 'peptic_ulcer'
    if 'ibs' in t: return 'ibs'
    if 'ibd' in t: return 'ibd'
    if 'ulcerative col' in t: return 'uc'
    if 'crohn' in t: return 'crohn'
    if 'cirrho' in t: return 'cirrhosis'
    if 'pancreat' in t: return 'pancreatitis'
    # Neuro
    if 'ischaemic stroke' in t or 'ischemic stroke' in t: return 'ischaemic'
    if 'haemorrhagic stroke' in t: return 'haemorrhagic'
    if 'sah' in t or 'subarach' in t: return 'sah'
    if 'stroke' in t and 'ischaem' not in t and 'haem' not in t: return 'stroke'
    if 'tia' in t: return 'tia'
    if 'epilep' in t or 'seizure' in t: return 'epilepsy'
    if 'multiple sclero' in t or ' ms' in t and 'mrcp' not in t: return 'ms'
    if 'parkinson' in t: return 'parkinsons'
    if 'migraine' in t: return 'migraine'
    if 'guillain' in t or 'gbs' in t: return 'gbs'
    if 'motor neur' in t or 'mnd' in t: return 'mnd'
    if 'myasthenia' in t: return 'myasthenia'
    # Endo
    if 'diabet' in t: return 'diabetes'
    if 'dka' in t: return 'dka'
    if 'hhs' in t: return 'hhs'
    if 'thyrotox' in t or 'hyperthyroid' in t: return 'thyrotoxicosis'
    if 'hypothyroid' in t or 'myxoedema' in t: return 'hypothyroid'
    if 'addison' in t or 'adrenal insuff' in t: return 'addisons'
    if 'cushing' in t: return 'cushings'
    if 'phaeochrom' in t or 'pheo' in t: return 'pheo'
    # Nephro
    if 'aki' in t or 'acute kidney' in t: return 'aki'
    if 'ckd' in t or 'chronic kidney' in t: return 'ckd'
    if 'glomerul' in t or 'gn' in t: return 'gn'
    if 'renal artery' in t: return 'rsa'
    # Hepatology
    if 'hepatitis b' in t: return 'hepatitis_b'
    if 'hepatitis c' in t: return 'hepatitis_c'
    if 'pbc' in t or 'primary biliary' in t: return 'pbc'
    if 'psc' in t or 'primary sclerosing' in t: return 'psc'
    if 'autoimmune hepat' in t: return 'ai_hep'
    if 'nafld' in t or 'fatty liver' in t: return 'nafld'
    if 'wilson' in t: return 'wilson'
    if 'haemochrom' in t: return 'hemochrom'
    if 'hcc' in t or 'hepatocell' in t: return 'hcc'
    # ID
    if 'sepsis' in t: return 'sepsis'
    if 'meningitis' in t: return 'meningitis'
    if 'endocard' in t: return 'endocarditis'
    if 'malaria' in t: return 'malaria'
    if 'hiv' in t: return 'hiv'
    # Haem
    if 'anaemia' in t and 'iron' not in t: return 'anaemia'
    if 'itp' in t: return 'itp'
    if 'ttp' in t: return 'ttp'
    if 'dic' in t: return 'dic'
    if 'leukaemia' in t: return 'leukaemia'
    if 'lymphoma' in t: return 'lymphoma'
    if 'myeloma' in t: return 'myeloma'
    # Rheum
    if 'rheumatoid arth' in t or ' ra' in t: return 'ra'
    if 'sle' in t or 'lupus' in t: return 'sle'
    if 'scleroderma' in t or 'systemic sclero' in t: return 'scleroderma'
    if 'polymyalgia' in t: return 'polymyalgia'
    if 'giant cell' in t or 'gca' in t: return 'gca'
    if 'anca' in t: return 'anca'
    if 'osteoporosis' in t: return 'osteoporosis'
    # Maternal
    if 'pre-eclampsia' in t or 'preeclampsia' in t: return 'preeclampsia'
    if 'hellp' in t: return 'hellp'
    if 'aflp' in t: return 'aflp'
    # Acute
    if 'anaphyl' in t: return 'anaphylaxis'
    return 'default'


def get_distractors(ch_slug: str, topic_kw: str) -> list[str]:
    pool = DISTRACTOR_POOLS.get(ch_slug, {}).get(topic_kw)
    if pool is None:
        pool = DISTRACTOR_POOLS.get(ch_slug, {}).get('default')
    if pool is None:
        pool = GENERIC_DISTRACTORS['condition']
    return list(pool)


# ---------------------------------------------------------------------------
# Pattern extractors
# ---------------------------------------------------------------------------

# Pattern 1: Triad recognition
# Match "X's triad" or "X triad" or "triad of X" or explicit list "(A, B, C)"
TRIAD_PATTERNS = [
    # "X's triad (A, B, C)"  or "X triad: A, B, C"  or  "triad: A, B, C"
    re.compile(r"(?P<name>[A-Z][A-Za-z\-']+(?:['\u2019]s)?)\s+triad[:\s—\-–]+\((?P<items>[^)]+)\)", re.I),
    re.compile(r"triad[:\s—\-–]+\((?P<items>[^)]+)\)", re.I),
    re.compile(r"\*\*([^*]+)\*\*:\s*\((?P<items>[^)]+)\)", re.I),
]

# Pattern 2: Specific clinical feature
SPECIFIC_FEATURE_PATTERNS = [
    # "specific for X" / "characteristic of X" / "hallmark of X"
    re.compile(r"\b(specific|characteristic|pathognomonic|hallmark|diagnostic)\b\s+(for|of)\s+([A-Za-z\- ]+?)(?:[.,;]|$)", re.I),
    re.compile(r"\b(classic|typical)\s+(sign|feature|finding|symptom)\s+(of|in)\s+([A-Za-z\- ]+?)(?:[.,;]|$)", re.I),
]

# Pattern 3: Avoid / contraindicated
AVOID_PATTERNS = [
    re.compile(r"\b(avoid|do not use|contraindicated|caution)\s+([A-Za-z\- ]+?)\s+(in|for)\s+([A-Za-z\- ]+?)(?:[.,;]|$)", re.I),
    re.compile(r"\b([A-Za-z\- ]+?)\s+is\s+(contraindicated|avoided|not recommended)\s+in\s+([A-Za-z\- ]+?)(?:[.,;]|$)", re.I),
    re.compile(r"\b([A-Za-z\- ]+?)\s+should be avoided\s+in\s+([A-Za-z\- ]+?)(?:[.,;]|$)", re.I),
]

# Pattern 4: Trial / evidence
TRIAL_PATTERNS = [
    re.compile(r"\b([A-Z][A-Z0-9\-]{1,10})\s+trial[^\.]{0,100}?(?:showed|demonstrated|found|established|confirmed)\s+([^.]{20,200})", re.I),
    re.compile(r"([A-Z][A-Z0-9\-]{1,10})\s+trial", re.I),
]

# Pattern 5: Score / threshold
SCORE_PATTERNS = [
    re.compile(r"\b([A-Z][A-Z0-9\-]{1,15})\s*(?:score|index)\s*(?:of)?\s*([0-9]+)\s*[:\-]?\s*([^.]{20,150})", re.I),
    re.compile(r"score\s+of\s+([0-9]+)\s*[:\-]?\s*([^.]{20,150})", re.I),
]


def extract_sentence_with_phrase(body: str, match_obj, max_len: int = 250) -> str | None:
    """Find the full sentence containing a regex match."""
    if not body:
        return None
    start, end = match_obj.span()
    # Find sentence boundaries
    # Look back for sentence start (period + space or newline)
    s_start = max(0, body.rfind('. ', 0, start) + 2)
    s_start_alt = max(0, body.rfind('.\n', 0, start) + 2)
    s_start = max(s_start, s_start_alt)
    if s_start < start - 200:
        s_start = max(0, start - 100)
    # Find sentence end
    s_end = body.find('. ', end)
    s_end_alt = body.find('.\n', end)
    candidates = [x for x in [s_end, s_end_alt] if x >= 0]
    s_end = min(candidates) if candidates else min(end + 200, len(body))
    sent = body[s_start:s_end].strip()
    if not sent:
        return None
    if len(sent) > max_len:
        sent = sent[:max_len].rstrip() + '…'
    return sent


def gen_triad_sba(title: str, body: str, ch_slug: str, topic_kw: str) -> dict | None:
    """Triad recognition: "X's triad: A, B, C" → "Which condition is characterised by: A, B, C?"
    """
    for pat in TRIAD_PATTERNS:
        for m in pat.finditer(body):
            items = m.group('items')
            # Parse items
            parts = re.split(r'[,;]|—|–|\sand\s|\sor\s', items)
            parts = [p.strip(' .()\u2014') for p in parts if p.strip()]
            if len(parts) < 3:
                continue
            parts = parts[:5]  # cap
            if any(len(p) < 3 for p in parts):
                continue
            if any(len(p) > 60 for p in parts):
                continue
            # Build the stem
            triad_str = ', '.join(parts)
            stem = (f"Which of the following is characterised by the clinical "
                    f"triad: {triad_str}?")
            options = {
                'A': title,
                'B': get_distractors(ch_slug, topic_kw)[0],
                'C': get_distractors(ch_slug, topic_kw)[1],
                'D': get_distractors(ch_slug, topic_kw)[2],
            }
            sent = extract_sentence_with_phrase(body, m)
            return {
                'stem': stem,
                'options': options,
                'answer': 'A',
                'source_quote': sent or triad_str,
            }
    return None


def gen_specific_feature_sba(title: str, body: str, ch_slug: str, topic_kw: str) -> dict | None:
    """Recognise a feature that is specific or pathognomonic of the disease."""
    # Only consider sentences from Clinical Features / Diagnosis / Mnemonics / Pitfalls
    relevant_body = ''
    for h, b in re.findall(r'##\s*([^\n]+)\n(.*?)(?=\n## |\Z)', body, re.S):
        hl = h.lower()
        if any(k in hl for k in ['clinical feature', 'presentation', 'sign',
                                  'mnemonic', 'pitfall', 'confusion', 'key',
                                  'investigations', 'differential']):
            relevant_body += b + '\n'
    if not relevant_body:
        relevant_body = body  # fallback
    # Match bold feature statements: **feature** specific/characteristic/of ...
    for m in re.finditer(r'\*\*([^*\n]{3,80}?)\*\*[^\n]{0,200}?(?:specific|characteristic|pathognomonic|hallmark|diagnostic|key|typical|distinctive)',
                         relevant_body, re.I):
        feat = m.group(1).strip()
        # Strip dose
        if '(' in feat:
            feat = feat.split('(')[0].strip()
        if len(feat) < 3 or len(feat) > 60:
            continue
        if any(x in feat.lower() for x in ['classification', 'severity', 'risk']):
            continue
        # Build the stem
        stem = (f"Which of the following features is most specific or "
                f"characteristic of {title}?")
        options = {
            'A': feat,
            'B': "A feature common to many acute inflammatory conditions",
            'C': "A non-specific sign that does not localise the diagnosis",
            'D': "An investigation finding rather than a clinical feature",
        }
        sent = extract_sentence_with_phrase(relevant_body, m)
        return {
            'stem': stem,
            'options': options,
            'answer': 'A',
            'source_quote': sent or feat,
        }
    return None


def gen_avoid_sba(title: str, body: str, ch_slug: str, topic_kw: str) -> dict | None:
    """Detect 'avoid X' or 'X contraindicated in Y' statements."""
    # Look in management / complications / pitfalls / mnemonics
    relevant_body = ''
    for h, b in re.findall(r'##\s*([^\n]+)\n(.*?)(?=\n## |\Z)', body, re.S):
        hl = h.lower()
        if any(k in hl for k in ['management', 'complication', 'pitfall', 'confusion',
                                  'mnemonic', 'caution', 'contraindication', 'avoid',
                                  'special population', 'interaction', 'pearl']):
            relevant_body += b + '\n'
    if not relevant_body:
        relevant_body = body
    pat = re.compile(
        r"(?:avoid|do not use|contraindicated|caution|should not|careful|never|"
        r"do not give|do not start)\s+([A-Z][A-Za-z0-9\-\s\(\)/]{3,60}?)"
        r"\s+(?:in|for|with|when|if)\s+([A-Za-z][A-Za-z\- ]{3,40}?)(?:[.,;]|$)",
        re.I)
    for m in pat.finditer(relevant_body):
        drug = m.group(1).strip()
        ctx = m.group(2).strip()
        if len(drug) > 50 or len(drug) < 3:
            continue
        if any(x in drug.lower() for x in ['caution', 'drug interactions',
                                            'contraindications', 'comorbidity',
                                            'general', 'principles', 'framework',
                                            'section', 'chapter', 'reference',
                                            'see', 'box', 'appendix', 'table',
                                            'figure', 'classification']):
            continue
        stem = (f"In the management of {title}, which of the following "
                f"should be avoided or is contraindicated?")
        options = {
            'A': f"{drug} (avoid in {ctx[:30]})",
            'B': "Standard guideline-directed first-line therapy",
            'C': "Routine supportive care (fluids, oxygen, monitoring)",
            'D': "Symptom-directed treatment as needed",
        }
        sent = extract_sentence_with_phrase(relevant_body, m)
        return {
            'stem': stem,
            'options': options,
            'answer': 'A',
            'source_quote': sent or m.group(0),
        }
    return None


def gen_trial_sba(title: str, body: str, ch_slug: str, topic_kw: str) -> dict | None:
    for m in TRIAL_PATTERNS[0].finditer(body):
        trial = m.group(1).strip()
        finding = m.group(2).strip()
        if len(finding) < 20 or len(finding) > 200:
            continue
        # Skip common non-trial "all caps" words
        if trial.upper() in ('NSAID', 'NSAIDS', 'ICU', 'CXR', 'ECG', 'ABG', 'GI', 'CNS',
                              'BP', 'HR', 'RR', 'EF', 'NYHA', 'BMI', 'DM', 'HTN', 'CKD',
                              'AKI', 'A&E', 'CT', 'MRI', 'PET', 'CSF', 'MRA', 'TIA',
                              'BMP', 'DAPT', 'GDMT', 'LMNOP', 'FBC', 'ESR', 'CRP', 'LDH',
                              'LFT', 'TFT', 'CMV', 'EBV', 'HBV', 'HCV', 'HIV', 'MRCP',
                              'COVID', 'SARS', 'MERS', 'AHA', 'ESC', 'NICE', 'GDMT'):
            continue
        if not re.match(r'^[A-Z][A-Z0-9\-]{1,8}$', trial):
            continue
        # Build SBA
        stem = (f"Which landmark clinical trial provided evidence relevant to "
                f"the management of {title} (specifically: {finding[:120]})?")
        options = {
            'A': f"{trial} trial",
            'B': f"A different but related trial in the same area",
            'C': f"A guideline (not a trial) addressing the same question",
            'D': f"An observational/cohort study addressing similar outcomes",
        }
        sent = extract_sentence_with_phrase(body, m)
        return {
            'stem': stem,
            'options': options,
            'answer': 'A',
            'source_quote': sent or f"{trial} trial — {finding[:150]}",
        }
    return None


def _find_mgt_section(body: str) -> str:
    """Find the management/treatment section. Returns combined body.

    If the matched H2 has no body of its own (e.g., '## Management' with no
    content under it), include the next several H2 sub-sections too.
    """
    matches = list(re.finditer(r'##\s+([^\n]+)\n(.*?)(?=\n## |\Z)', body, re.S))
    for i, m in enumerate(matches):
        h = m.group(1).strip()
        hl = h.lower()
        if not any(k in hl for k in ['management', 'treatment', 'therapy', 'rx ']):
            continue
        b = m.group(2).strip()
        if b:
            return b
        # Empty body — pull the next 5 H2 sub-sections
        combined = ''
        for j in range(i + 1, min(i + 6, len(matches))):
            sub_h = matches[j].group(1).strip()
            sub_b = matches[j].group(2).strip()
            combined += f'## {sub_h}\n{sub_b}\n\n'
        if combined:
            return combined
    return ''


def gen_first_line_sba(title: str, body: str, ch_slug: str, topic_kw: str) -> dict | None:
    """First-line management: detect explicit first-line statements in management section."""
    if not body:
        return None
    mgt_body = _find_mgt_section(body)
    if not mgt_body:
        return None
    text = mgt_body[:3000]
    text_clean = re.sub(r'\|', ' ', text)
    # Look for first-line bullet or sentence with a treatment
    candidates = []
    # Mode 1: bullet-style
    for m in re.finditer(r'^\s*[-*]\s+(.+?)$', text_clean, re.M):
        line = m.group(1).strip()
        if len(line) < 10 or len(line) > 300:
            continue
        ll = line.lower()
        if ll.startswith('avoid') or 'contraindicated' in ll[:50]:
            continue
        if not re.search(r'\*\*[A-Z]', line) and not re.search(r'\b(start|give|prescribe|administer|use)\b', ll):
            continue
        # Has treatment verb
        if not re.search(r'\b(start|give|use|prescribe|administer|empiric|treat|cover|choose|therapy|antibiotic|antiviral|anticoagul)\b', ll):
            continue
        candidates.append(line)
        if len(candidates) >= 3:
            break
    # Mode 2: sentence-style
    if not candidates:
        sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z*])|(?<=\n)\s*(?=[A-Z*])', text_clean)
        for s in sentences:
            s_clean = s.strip()
            if not s_clean or len(s_clean) < 10:
                continue
            if len(s_clean) > 400:
                continue
            sl = s_clean.lower()
            if sl.startswith('**avoid') or sl.startswith('avoid ') or 'contraindicated' in sl[:50]:
                continue
            if not re.search(r'\*\*[A-Z][A-Za-z0-9\-]{2,}', s_clean):
                continue
            if not re.search(r'\b(for|in|as|with|treat|manage|step|controller|reliever|first|initial)\b', sl):
                continue
            candidates.append(s_clean)
            if len(candidates) >= 3:
                break
    if not candidates:
        return None
    first = candidates[0]
    drugs = []
    for m in re.finditer(r'\*\*([^*\n]{2,80}?)\*\*', first):
        d = m.group(1)
        if '(' in d:
            d = d.split('(')[0]
        d = re.sub(r'\s+\d.*$', '', d).strip()
        d = d.rstrip('+,').strip()
        if not d:
            continue
        if len(d) < 3 or len(d) > 35:
            continue
        if d.lower() in ('first line', 'first-line', 'first episode', 'recurrence',
                          'acute', 'chronic', 'severe', 'mild', 'moderate',
                          'same', 'asthmatic', 'controller', 'reliever'):
            continue
        drugs.append(d)
    # If no drugs from bolds, use the FULL sentence (truncated) as the answer
    if not drugs:
        # Use the original line as the answer (truncated)
        first_clean = re.sub(r'\*\*', '', first).strip()
        # Remove leading dashes
        first_clean = re.sub(r'^[-*]\s+', '', first_clean)
        # Truncate at first period
        period = first_clean.find('.')
        if period > 10:
            first_clean = first_clean[:period].strip()
        # Length cap
        if len(first_clean) > 120:
            first_clean = first_clean[:120].rstrip(',;') + '…'
        # Must be at least 20 chars
        if len(first_clean) < 20:
            return None
        drugs_str = first_clean
        stem = (f"What is the most appropriate first-line therapy for {title}?")
        options = {
            'A': drugs_str,
            'B': "An advanced/surgical therapy reserved for refractory disease",
            'C': "Symptomatic treatment only, no disease-modifying therapy",
            'D': "Empiric broad-spectrum therapy without specific indication",
        }
        return {
            'stem': stem,
            'options': options,
            'answer': 'A',
            'source_quote': first[:300],
        }
    seen = set()
    clean_drugs = []
    for d in drugs:
        if d not in seen:
            seen.add(d)
            clean_drugs.append(d)
    if not clean_drugs:
        return None
    drugs_str = ' + '.join(clean_drugs[:3])
    # Cap the answer to a reasonable length
    if len(drugs_str) > 120:
        # Truncate to first 3 drugs
        drugs_str = ' + '.join(clean_drugs[:2])[:120]
    stem = (f"What is the most appropriate first-line therapy for {title}?")
    options = {
        'A': drugs_str,
        'B': "An advanced/surgical therapy reserved for refractory disease",
        'C': "Symptomatic treatment only, no disease-modifying therapy",
        'D': "Empiric broad-spectrum therapy without specific indication",
    }
    return {
        'stem': stem,
        'options': options,
        'answer': 'A',
        'source_quote': first[:300],
    }


def gen_scenarios_for_topic(title: str, sections: list[tuple[str, str]],
                            ch_slug: str) -> list[dict]:
    """Generate 2-5 scenario SBAs for a topic, grounded in source text."""
    sbas = []
    seen_stems = set()

    def add(sba):
        if not sba:
            return
        if len(sbas) >= 5:
            return
        key = sba['stem'][:80].lower()
        if key in seen_stems:
            return
        # Quality: stem must be reasonable length
        if len(sba['stem']) < 30 or len(sba['stem']) > 600:
            return
        # Options must all be non-empty and not the same
        opts = sba['options']
        if not all(opts.get(k) and opts[k].strip() for k in 'ABCD'):
            return
        if len(set(opts.values())) < 4:
            return
        seen_stems.add(key)
        sbas.append(sba)

    topic_kw = topic_keyword(title)
    # Build full text with H2 markers preserved
    full_text = '\n'.join(f"## {h}\n{b}" for h, b in sections)

    # Try only the stronger SBA shapes in priority order.
    # We intentionally skip the generic "characteristic of X" and
    # "first-line therapy for X" patterns here because they read like
    # textbook prompts, not PassMedicine-style SBAs.
    add(gen_triad_sba(title, full_text, ch_slug, topic_kw))
    add(gen_avoid_sba(title, full_text, ch_slug, topic_kw))
    add(gen_trial_sba(title, full_text, ch_slug, topic_kw))

    return sbas


# ---------------------------------------------------------------------------
# Formatting
# ---------------------------------------------------------------------------

def format_sba_block(sbas: list[dict], topic_title: str, chapter_label: str) -> str:
    if not sbas:
        return ''
    lines = [
        '',
        '## PasTest Scenario SBAs (Clinical Vignettes)',
        '',
        f'> **Auto-generated PasTest/Mediscope-style scenario SBAs** grounded '
        f'in the authored source. Each scenario tests a real clinical fact '
        f'(triad, specific sign, contraindication, trial, first-line Rx) extracted '
        f'from the topic. *Source: {chapter_label} — {topic_title}*',
        '',
    ]
    for i, s in enumerate(sbas, 1):
        lines.append(f'**Q{i}.** {s["stem"]}')
        lines.append('')
        for k in 'ABCD':
            lines.append(f'  - **{k}.** {s["options"][k]}')
        lines.append('')
        ans_text = s['options'][s['answer']]
        lines.append(f'  > **Answer: {s["answer"]}** — {ans_text[:200]}')
        lines.append(f'  >')
        lines.append(f'  > *Source:* {s["source_quote"][:200]}')
        lines.append('')
    return '\n'.join(lines)


# ---------------------------------------------------------------------------
# Topic discovery
# ---------------------------------------------------------------------------

SKIP_FILENAMES = (
    'roadmap', 'hierarchy', 'index', 'readme', 'moc', 'hub',
    'hub overview', 'overview', 'template',
)


def is_real_topic(path: Path) -> bool:
    name = path.stem.lower()
    if any(s in name for s in SKIP_FILENAMES):
        return False
    if path.stat().st_size < 2000:
        return False
    return True


def _normalize(s: str) -> str:
    s = re.sub(r'^[\d.]+-?\s*', '', s)
    s = re.sub(r'\s*\([^)]*\)\s*', ' ', s)
    # Strip common suffixes: _full, _notes, _draft, _v1, etc.
    s = re.sub(r'_(full|notes|draft|final|complete|short|extended|summary)$', '', s, flags=re.I)
    s = re.sub(r'[^a-z0-9]+', ' ', s.lower())
    s = re.sub(r'\s+', ' ', s).strip()
    return s


_published_cache: dict[str, dict[str, Path]] = {}


def _load_published_cache(ch_slug: str) -> dict[str, Path]:
    if ch_slug in _published_cache:
        return _published_cache[ch_slug]
    cache: dict[str, Path] = {}
    ch_dir = CHAPTERS / ch_slug
    diseases = ch_dir / 'diseases'
    if diseases.exists():
        # Mode 1: topic.md in subfolders (preferred)
        for pmd in diseases.rglob('topic.md'):
            parent = pmd.parent.name
            clean = _normalize(parent)
            if clean:
                cache.setdefault(clean, pmd)
        # Mode 2: *.md in subfolders (when topic.md missing)
        for md in diseases.rglob('*.md'):
            if md.name == 'topic.md' or md.name.endswith('.png') or md.name.endswith('.html'):
                continue
            # Use parent folder name as the key (since the file is named after the topic)
            parent = md.parent.name
            if parent and parent != 'diseases' and not parent.startswith('.'):
                clean = _normalize(parent)
            else:
                clean = _normalize(md.stem)
            if clean:
                cache.setdefault(clean, md)
        # Mode 3: direct .md files in diseases/
        for md in diseases.glob('*.md'):
            stem = md.stem
            clean = _normalize(stem)
            if clean:
                cache.setdefault(clean, md)
    _published_cache[ch_slug] = cache
    return cache


def find_published_topic(ch_slug: str, src_stem: str) -> Path | None:
    cache = _load_published_cache(ch_slug)
    if not cache:
        return None
    clean_src = _normalize(src_stem)
    if not clean_src:
        return None
    if clean_src in cache:
        return cache[clean_src]
    src_tokens = set(clean_src.split())
    if not src_tokens:
        return None
    best = None
    best_overlap = 0.0
    for cand_stem, cand_path in cache.items():
        cand_tokens = set(cand_stem.split())
        if not cand_tokens:
            continue
        overlap = len(src_tokens & cand_tokens) / max(len(src_tokens | cand_tokens), 1)
        if overlap > best_overlap:
            best_overlap = overlap
            best = cand_path
    if best and best_overlap >= 0.7:
        return best
    return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def process_source(src_root: Path, ch_slug: str) -> tuple[int, int, int]:
    if not src_root.exists():
        return (0, 0, 0)
    ch_label = CH_LABELS.get(ch_slug, ch_slug)
    n_topics = 0
    n_updated = 0
    n_sbas = 0
    for src in sorted(src_root.rglob('*.md')):
        if not is_real_topic(src):
            continue
        n_topics += 1
        try:
            text = src.read_text(encoding='utf-8', errors='replace')
        except Exception:
            continue
        sections = get_h2_sections(text)
        if not sections:
            continue
        title = topic_title_from_path(src)
        sbas = gen_scenarios_for_topic(title, sections, ch_slug)
        if not sbas:
            continue
        pub = find_published_topic(ch_slug, src.stem)
        if pub is None:
            continue
        try:
            pub_text = pub.read_text(encoding='utf-8', errors='replace')
        except Exception:
            continue
        if '## PasTest Scenario SBAs' in pub_text:
            continue
        block = format_sba_block(sbas, title, ch_label)
        new_text = pub_text.rstrip() + '\n' + block + '\n'
        try:
            pub.write_text(new_text, encoding='utf-8')
        except Exception as e:
            print(f'  ! write failed: {pub}: {e}')
            continue
        n_updated += 1
        n_sbas += len(sbas)
    return (n_topics, n_updated, n_sbas)


def main():
    print(f"=== PasTest Scenario SBA generator v2 ===\n")
    print(f"Source: {MED}")
    print(f"Output: {CHAPTERS}\n")
    grand_topics = 0
    grand_updated = 0
    grand_sbas = 0
    summary = {}
    for src_dir, ch_slug in SRC_TO_PUB.items():
        src_root = MED / src_dir
        n_topics, n_updated, n_sbas = process_source(src_root, ch_slug)
        grand_topics += n_topics
        grand_updated += n_updated
        grand_sbas += n_sbas
        if n_topics > 0:
            print(f"  {ch_slug:48s}  {n_topics:4d} topics  {n_updated:4d} updated  {n_sbas:4d} SBAs")
        summary[ch_slug] = {
            'topics': n_topics,
            'updated': n_updated,
            'sbas': n_sbas,
        }
    print(f"\n=== Total ===")
    print(f"  Topics scanned:  {grand_topics}")
    print(f"  Topics updated:  {grand_updated}")
    print(f"  Scenario SBAs:   {grand_sbas}")
    summary_path = ROOT / 'site' / 'scripts' / '_scenario_sba_summary_v2.json'
    summary_path.write_text(json.dumps(summary, indent=2), encoding='utf-8')
    print(f"  Summary: {summary_path}")


if __name__ == '__main__':
    main()
