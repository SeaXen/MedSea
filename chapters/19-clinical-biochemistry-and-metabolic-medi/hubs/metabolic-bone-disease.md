---
tags: [medicine, davidson, clinical-biochemistry, metabolic-bone, osteoporosis, osteomalacia, paget, renal-osteodystrophy, fcps, mrcp]
davidson_part: Part 3: Clinical Medicine
davidson_chapter: Chapter 10: Clinical Biochemistry and Metabolic Medicine
status: scaffold-hub
---

# Metabolic Bone Disease
> **Chapter 10 Theme Group Hub | Metabolic Bone Disease**
> Covers osteoporosis, osteomalacia, Paget disease of bone, and renal osteodystrophy.

---

## Disease-Level Topics in this Group

| # | Topic | File | Status |
|---|-------|------|--------|
| 1 | **Osteoporosis** (DEXA, FRAX, Bisphosphonates, Denosumab, Anabolics) | `Osteoporosis.md` | scaffold |
| 2 | **Osteomalacia** (Rickets, Vitamin D Deficiency, Causes) | `Osteomalacia.md` | scaffold |
| 3 | **Paget Disease of Bone** (Diagnosis, Bisphosphonates) | `Paget Disease of Bone.md` | scaffold |
| 4 | **Renal Osteodystrophy** (CKD-MBD, SHPT, FGF23) | `Renal Osteodystrophy.md` | scaffold |

---

## Clinical Algorithms

### Osteoporosis

```
OSTEOPOROSIS MANAGEMENT
         │
         ├── DIAGNOSIS
         │       ├── **DEXA T-Score**
         │       │       ├── ≥-1.0 SD → Normal
         │       │       ├── -1.0 to -2.5 SD → Osteopenia
         │       │       ├── ≤-2.5 SD → **Osteoporosis**
         │       │       └── ≤-2.5 + Fragility Fracture → Severe/Established
         │       │
         │       ├── **FRAX** (10-Year Major Osteoporotic / Hip Fracture Risk)
         │       │       ├── With/Without BMD
         │       │       ├── Thresholds (NOGG): Age-Dependent (e.g., ≥7.5% at 50, ≥15% at 70)
         │       │       └── Major OP Fx ≥7.5-15% / Hip Fx ≥3-4.5% → Treat
         │       │
         │       └── Secondary Causes Screen
         │               ├── TSH, Calcium, ALP, 25-OH Vit D, Coeliac (TTG), FSH/LH/Testosterone
         │               └── Exclude: Hyperthyroidism, Hyperparathyroidism, Cushing's, Coeliac, MMM
         │
         ├── LIFESTYLE (All Patients)
         │       ├── Weight-Bearing Exercise (30 min/d, 3-5x/wk)
         │       ├── Calcium 1000-1200 mg/d (Diet + Supplement)
         │       ├── Vitamin D 800-2000 IU/d (Target 25-OH D >50 nmol/L)
         │       ├── Smoking Cessation, Alcohol <14 Units/wk
         │       └── Falls Prevention (Home Hazards, Vision, Balance)
         │
         └── PHARMACOTHERAPY
                 ├── INDICATIONS (Any):
                 │       ├── T-Score ≤-2.5
                 │       ├── T-Score -1.0 to -2.5 + FRAX >Threshold
                 │       ├── Fragility Fracture (Hip, Vertebra, Wrist, Humerus)
                 │       └── Glucocorticoid-Induced (≥7.5mg Pred >3mo + T ≤-1.5)
                 │
                 ├── FIRST-LINE
                 │       ├── **Oral Bisphosphonate** (Alendronate 70mg Weekly / Risedronate 35mg Weekly)
                 │       └── **Denosumab 60mg SC q6mo** (If Bisphosphonate Contraindicated/Intolerant)
                 │
                 ├── SECOND-LINE / SPECIALIST
                 │       ├── **Zoledronic Acid 5mg IV Annual** (If Oral Contraindicated)
                 │       ├── **Teriparatide 20µg SC Daily × 24mo Max** (Anabolic; Severe: T ≤-3.0, Fracture)
                 │       ├── **Romosozumab 210mg SC Monthly × 12mo** (Anabolic+Antiresorptive; Severe)
                 │       └── **Raloxifene 60mg OD** (Postmenopausal; Breast Ca Risk Reduction)
                 │
                 ├── MONITORING
                 │       ├── DEXA at 2-3 Years (Then q2-3yr)
                 │       ├── Height Annual (Vertebral Fracture Screen)
                 │       ├── Adherence / Adverse Effects (GI, ONJ, Atypical Femoral Fracture)
                 │       └── **Drug Holiday**: Oral BP after 3-5yr if Low Risk (T >-2.5, No Fx); Zol after 3yr
                 │
                 └── GLUCOCORTICOID-INDUCED OSTEOPOROSIS (GIOP)
                         ├── ≥7.5mg Pred >3mo + T ≤-1.5 → Treat
                         ├── **Teriparatide Preferred** (Anabolic Superior in GIOP)
                         └── Alendronate / Zoledronic / Denosumab Alternatives
```

---

### Osteomalacia / Rickets

```
OSTEOMALACIA / RICKETS
         │
         ├── PATHOPHYSIOLOGY
         │       ├── **Defective Mineralisation** of Osteoid (Vitamin D / Calcium / Phosphate Deficiency)
         │       ├── Adults = Osteomalacia; Children = Rickets (Growth Plate Involvement)
         │
         ├── CAUSES
         │       ├── **Vitamin D Deficiency** (Most Common): Low Sunlight, Malabsorption, CKD, AEDs, Dark Skin
         │       ├── **Calcium Deficiency**: Low Intake, Malabsorption
         │       ├── **Phosphate Deficiency**: Fanconi, Oncogenic Osteomalacia, X-Linked Hypophosphataemic Rickets
         │       ├── **Renal Disease**: CKD → ↓ 1α-Hydroxylase → ↓ 1,25-(OH)₂D
         │       └── **Drug-Induced**: AEDs (Enzyme Induction), Antiretrovirals (TDF)
         │
         ├── CLINICAL
         │       ├── **Adults**: Bone Pain (Pelvis, Lower Back, Thighs), Proximal Myopathy, Waddling Gait
         │       ├── **Children**: Bow Legs/Genu Valgum, Wrist/Ankle Widening, Rachitic Rosary, Craniotabes
         │       └── **Biochemical**: ↓ Ca²⁺/Normal, ↓ Phosphate, **↑ ALP**, ↓ 25-OH D, ↑ PTH (Secondary HPT)
         │
         └── MANAGEMENT
                 ├── **Vitamin D Replacement**: Cholecalciferol 50,000 IU Weekly × 6-8wk → 800-2000 IU/d Maintenance
                 ├── **Calcium Supplementation** 1-2g/d (If Dietary Inadequate)
                 ├── **Phosphate Replacement** (If Hypophosphataemic)
                 ├── **Treat Underlying Cause** (Malabsorption, CKD, Drug Review)
                 └── **Monitor**: Ca²⁺, Phosphate, ALP, 25-OH D, PTH q3-6mo
```

---

### Paget Disease of Bone

```
PAGET DISEASE OF BONE (Osteitis Deformans)
         │
         ├── EPIDEMIOLOGY
         │       ├── Age >55; Male > Female; UK/Northern Europe Highest Prevalence
         │       ├── Genetic (SQSTM1 Mutation ~30%), Viral (Paramyxovirus Hypothesis)
         │
         ├── PATHOPHYSIOLOGY
         │       ├── **Excessive Osteoclastic Resorption** → Compensatory Disorganised Osteoblastic Formation
         │       ├── 3 Phases: **Lytic (Early)** → **Mixed** → **Sclerotic (Late/Burnt-Out)**
         │
         ├── CLINICAL
         │       ├── **Asymptomatic** (Incidental ALP ↑, X-Ray Findings)
         │       ├── **Bone Pain** (Deep, Aching, Night), **Deformity** (Bowing, Skull Enlargement)
         │       ├── **Complications**: Osteoarthritis, Fractures, Nerve Compression (CN VIII → Deafness), High-Output Heart Failure, Osteosarcoma (<1%)
         │       ├── **Biochemical**: **↑ ALP** (Disproportionate to Other LFTs), Normal Ca²⁺/Phosphate/PTH
         │       └── **Imaging**: X-Ray (Lytic → Mixed → Sclerotic), Bone Scan (Polyostotic, Intense Uptake)
         │
         ├── INDICATIONS FOR TREATMENT
         │       ├── Symptomatic (Bone Pain, Neurological, Cardiac)
         │       ├── Impending Fracture / Impending Complication
         │       ├── Pre-Operative (If Surgery on Pagetic Bone)
         │       └── Serum ALP >2x ULN (Asymptomatic but High Turnover)
         │
         └── MANAGEMENT
                 ├── **Bisphosphonates** (1st Line)
                 │       ├── **Zoledronic Acid 5mg IV Single Infusion** (Preferred; Potent, Long Duration)
                 │       ├── **Risedronate 30mg OD × 2mo** (Oral Alternative)
                 │       └── **Pamidronate** (IV, If Zoledronic Unavailable)
                 │
                 ├── **Monitoring**: ALP q3-6mo (Target Normalisation → Remission)
                 ├── **Analgesia** (NSAIDs, Opioids for Bone Pain)
                 └── **Surgery**: Joint Replacement (Osteoarthritis), Fixation (Fractures), Decompression (Nerve)
```

---

### Renal Osteodystrophy (CKD-MBD)

```
RENAL OSTEODYSTROPHY (CKD-MBD)
         │
         ├── PATHOPHYSIOLOGY (CKD-MBD Cascade)
         │       ├── **CKD → ↓ Phosphate Excretion → ↑ FGF23 → ↓ 1α-Hydroxylase → ↓ 1,25-(OH)₂D**
         │       ├── **↓ 1,25-(OH)₂D → ↓ Ca²⁺ Absorption → Hypocalcaemia → ↑ PTH (2° HPT)**
         │       ├── **↑ PTH → ↑ Bone Resorption (High Turnover) ↔ Adynamic Bone (Over-Suppressed PTH)**
         │       └── **Vascular Calcification** (Ca×PO₄ >4.5, High Phosphate, High PTH)
         │
         ├── BONE TURNOVER TYPES (KDIGO)
         │       ├── **High Turnover** (2° HPT): ALP ↑, PTH ↑↑, Bone Pain, Fractures
         │       ├── **Low Turnover (Adynamic)**: ALP Normal/Low, PTH Low, Fracture Risk High
         │       ├── **Mixed**: Features of Both
         │       └── **Osteomalacia**: Low Ca²⁺/Phosphate, Low ALP, Low 25-OH D
         │
         ├── KDIGO TARGETS (CKD G3-5D)
         │       ├── **PTH**: 2-9x ULN (Avoid <2x = Adynamic; Avoid >9x = High Turnover)
         │       ├── **Calcium**: 2.1-2.5 mmol/L (Corrected)
         │       ├── **Phosphate**: 0.8-1.5 mmol/L (G3-4) / 1.1-1.5 mmol/L (Dialysis)
         │       ├── **Ca × Phosphate**: <4.5 mmol²/L²
         │       └── **25-OH Vit D**: ≥30 ng/mL (75 nmol/L)
         │
         └── MANAGEMENT
                 ├── **Phosphate Binders** (With Meals)
                 │       ├── Ca-Based (CaCO₃/Acetate) if Ca²⁺ Normal/Low
                 │       └── Non-Ca (Sevelamer/Lanthanum/Sucroferric/Ferric Citrate) if Ca²⁺ High/Calcification
                 │
                 ├── **Vitamin D Analogues** (CKD G4-5D)
                 │       ├── Alfacalcidol/Calcitriol 0.25-1µg/d (or 1µg Alt Days)
                 │       └── **Paricalcitol** (Selective VDR; Less Hypercalcaemia/Phosphataemia)
                 │
                 ├── **Calcimimetics**
                 │       └── **Cinacalcet** (CaSR Agonist): 30-180mg/d PO (HD: Etelcalcetide IV Post-HD)
                 │
                 └── **Parathyroidectomy** (Refractory 2°/3° HPT)
                         ├── PTH >800-1000 pg/mL Despite Max Medical Rx
                         ├── Ca²⁺ >2.75 / Phosphate >1.8
                         ├── Subtotal (3.5-Gland) PTX ± Autotransplant
                         └── IOPTH >50% Drop at 10min (Miami Criterion)
```

---

## Key Formulae & Cut-offs

| Parameter | Target / Value |
|-----------|----------------|
| **DEXA T-Score** | Normal ≥-1.0; Osteopenia -1.0 to -2.5; Osteoporosis ≤-2.5 |
| **FRAX Threshold (UK/NOGG)** | Major OP Fx: ≥7.5% (Age 50) → ≥15% (Age 70+); Hip Fx: ≥3% → ≥4.5% |
| **Alendronate** | 70mg Weekly PO (1st Line); Upright 30min, Water 200mL |
| **Zoledronic Acid** | 5mg IV Annual (eGFR ≥35); 3 Years Treatment → Holiday |
| **Denosumab** | 60mg SC q6mo (No Holiday; → Rapid Bone Loss if Stopped) |
| **Teriparatide** | 20µg SC Daily × 24mo Max (Anabolic; Severe Osteoporosis) |
| **Romosozumab** | 210mg SC Monthly × 12mo (Anabolic + Antiresorptive) |
| **Osteomalacia Biochem** | ↓ Phosphate, ↑ ALP, ↑ PTH, ↓ 25-OH D, Normal Ionised Ca²⁺ |
| **Paget ALP** | Disproportionately ↑ (vs Other LFTs); Target Normalisation |
| **Zoledronic (Paget)** | 5mg IV Single Dose (Preferred); Monitor ALP q3-6mo |
| **CKD-MBD PTH Target** | 2-9x ULN (Avoid <2x = Adynamic; >9x = High Turnover) |
| **CKD Phosphate Target** | 0.8-1.5 (G3-4) / 1.1-1.5 (Dialysis) |
| **Ca × Phosphate** | <4.5 mmol²/L² (Vascular Calcification Risk) |
| **Cinacalcet** | CaSR Agonist; ↓ PTH, ↓ Ca²⁺, ↓ Phosphate; Monitor Hypocalcaemia |

---

## Local Navigation

> **Parent**: [Davidson Chapter 10 Hierarchy](./Davidson Chapter 10 - Clinical Biochemistry and Metabolic Medicine Hierarchy.md)  
> **Template**: `../../Templates/Clinical Biochemistry Topic Template.md`  
> **See also**: [Calcium Magnesium Phosphate](./Calcium Magnesium Phosphate.md) | [Acid-Base Disorders](../Acid-Base Disorders.md)