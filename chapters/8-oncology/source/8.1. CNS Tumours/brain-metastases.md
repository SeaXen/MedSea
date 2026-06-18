# Brain Metastases

> [!tip] **FCPS/MRCP Priority: HIGH**
> **Brain Metastases = Most Common CNS Malignancy (10x Primary)**; **Sources: Lung (50%), Breast (15-20%), Melanoma (10%), RCC, GI**; **1-3 Mets: SRS Standard (JROSG, NCCTG); >3 Mets: WBRT OR SRS (JROSG-99); Surgery for Solitary/Symptomatic/Accessible**; **Molecular-Driven Systemic Therapy**: **Lung EGFR/ALK (Osimertinib, Lorlatinib)**; **Breast HER2+ (T-DXd, Tucatinib+Capecitabine+Trastuzumab)**; **Melanoma (Ipi+Nivo, Pembro)**; **RT Oedema: Dexamethasone**; **VTE: LMWH**; **Prognosis: RPA/GPA Classes**.

---

## 1. Learning Objectives
By the end of this note you should be able to:
- [ ] Apply **SRS vs WBRT** Decision (Number, Size, Location, Histology, Performance Status)
- [ ] Indicate **Surgery** for Solitary, Symptomatic, Accessible, Diagnostic Uncertainty
- [ ] Select **Molecular-Driven Systemic Therapy** for Lung (EGFR/ALK), Breast (HER2), Melanoma
- [ ] Use **RPA/GPA/DS-GPA** Prognostic Classes for Treatment Decisions
- [ ] Manage **RT Oedema** with **Dexamethasone** (Taper)
- [ ] Prescribe **VTE Prophylaxis** (LMWH) — High Risk
- [ ] Recognise **Radionecrosis vs Progression** (PET, Perfusion, Spectroscopy)

---

## 2. Definition & Epidemiology

| Feature | Detail |
|---------|--------|
| **Definition** | Secondary malignant deposits in brain parenchyma; **Haematogenous Spread** (Grey-White Junction) |
| **Incidence** | **10x Primary Brain Tumours**; ~100,000-170,000/year US; **20-40% of Cancer Patients** |
| **Sources** | **Lung (50%)**, **Breast (15-20%)**, **Melanoma (10%)**, **RCC (5%)**, **GI (5%)**, **Unknown Primary (5%)** |
| **Prevalence** | Rising (Better Systemic Therapy, Better Imaging) |
| **Peak Age** | 60-70 years |
| **Location** | **Supratentorial (80%)**, **Grey-White Junction**, **Watershed Areas** |

---

## 3. Clinical Features

| Feature | Description |
|---------|-------------|
| **Headache** | **Most Common (50%)**; Morning, Valsalva-Aggravated (Raised ICP) |
| **Seizures** | **15-25%** (Focal > Generalised) |
| **Focal Neurological Deficits** | Hemiparesis, Aphasia, Visual Field, Ataxia, Cranial Nerve Palsies |
| **Cognitive/Behavioural** | Personality Change, Memory, Executive Dysfunction |
| **Asymptomatic** | **Incidental on Staging Imaging (10-20%)** |

---

## 4. Diagnosis & Investigations

| Investigation | Role | Key Details |
|---------------|------|-------------|
| **MRI Brain with Contrast (Gold Standard)** | **Diagnosis, Number, Size, Location, Oedema, Haemorrhage** | **T1 Post-Contrast: Ring/Solid Enhancement**, **T2/FLAIR: Perilesional Oedema**, **DWI: Restricted Diffusion (High Cellularity)**, **SWI: Haemorrhage (Melanoma, RCC, Choriocarcinoma)** |
| **CT Brain** | Emergency, Surgical Planning | Less Sensitive for Small Mets |
| **PET-CT** | Systemic Staging, Primary Detection | If Primary Unknown |
| **CSF Analysis** | Leptomeningeal Disease (If Suspected) | Cytology, ctDNA |
| **Molecular Testing (Primary/Metastasis)** | **EGFR, ALK, ROS1, HER2, PD-L1, BRAF** | Guides Targeted Therapy |

---

## 5. Prognostic Indices

### RPA (Recursive Partitioning Analysis) — Gastrin 1997

| Class | Criteria | Median OS |
|-------|----------|-----------|
| **Class 1** | **KPS ≥70, Age <65, Controlled Primary, No Extracranial Mets** | **7.1 months** |
| **Class 2** | **Not Class 1 or 3** | **4.2 months** |
| **Class 3** | **KPS <70** | **2.3 months** |

### GPA (Graded Prognostic Assessment) — Sperduto 2008

| Factor | Score |
|--------|-------|
| **KPS** | 0: <70; 1: 70-80; 2: 90-100 |
| **Age** | 0: >65; 1: 50-65; 2: <50 |
| **Extracranial Mets** | 0: Yes; 1: No |
| **Number of Brain Mets** | 0: >3; 1: 2-3; 2: 1 |

| GPA Score | Median OS |
|-----------|-----------|
| **0-1.0** | **2.6 months** |
| **1.5-2.0** | **4.7 months** |
| **2.5-3.0** | **9.2 months** |
| **3.5-4.0** | **13.9 months** |

### Disease-Specific GPA (DS-GPA) — Sperduto 2017
- **Lung, Breast, Melanoma, RCC** — **Adds Molecular Markers** (EGFR, ALK, HER2, etc.)

---

## 6. Management

### Local Therapy Decision Algorithm

```mermaid
flowchart TD
    A[Brain Metastases] --> B{Number / Size / Location / KPS}
    B -->|**1-3 Mets, ≤3cm, KPS ≥70**| C[**SRS (Stereotactic Radiosurgery)** — **Standard**<br/>**JROSG/NCCTG: SRS Alone Non-Inferior to SRS+WBRT**<br/>**Less Neurocognitive Decline**]
    B -->|**>3 Mets OR >3cm OR Critical Location**| D[**WBRT (Whole Brain RT)**<br/>**30Gy/10fx OR 20Gy/5fx**<br/>**Hippocampal Avoidance (HA-WBRT) + Memantine**]
    B -->|**Solitary, >3cm, Symptomatic, Accessible, Diagnostic Uncertainty**| E[**Surgery + SRS to Cavity**<br/>**Patchell: Surgery+WBRT > WBRT Alone**<br/>**Modern: Surgery + Cavity SRS (No WBRT)**]
    C --> F[**Surveillance MRI q3mo ×1yr, q6mo ×2yr**]
    D --> F
    E --> F
```

### SRS vs WBRT — Key Trials

| Trial | Comparison | Result |
|-------|------------|--------|
| **JROSG (1-4 Mets)** | **SRS Alone vs SRS + WBRT** | **OS Equivalent**; **WBRT: ↑Local Control, ↓Neurocognition** |
| **NCCTG N0574 (1-3 Mets)** | **SRS Alone vs SRS + WBRT** | **OS Equivalent**; **WBRT: ↓Cognitive Function (3mo)** |
| **JROSG-99 (5-10 Mets)** | **SRS vs WBRT** | **OS Equivalent**; **SRS: Less Cognitive Decline** |
| **QUARTZ (NSCLC, Unfit)** | **WBRT + Dex vs Dex Alone** | **No OS/QOL Benefit for WBRT** |

### Hippocampal-Avoidance WBRT + Memantine

| Trial | Result |
|-------|--------|
| **NRG CC001** | **HA-WBRT + Memantine** → **Less Memory Decline** vs Standard WBRT |
| **Standard WBRT Dose** | **30Gy/10fx** OR **20Gy/5fx** (Poor Prognosis) |

---

## 7. Surgery Indications

| Indication | Details |
|------------|---------|
| **Solitary Metastasis** | **Accessible, Symptomatic, KPS ≥70** |
| **Diagnostic Uncertainty** | **Biopsy/Resection** |
| **Symptomatic (Mass Effect, Herniation Risk)** | **Urgent Decompression** |
| **Large (>3-4cm)** | **SRS Less Effective for Large Lesions** |
| **Post-Surgery** | **Cavity SRS (15-18Gy Single Fraction)** — **Standard** |

---

## 8. Molecular-Driven Systemic Therapy (Blood-Brain Barrier Penetration)

### NSCLC with Brain Mets

| Target | Agent | CNS Penetration | Key Trial |
|--------|-------|----------------|-----------|
| **EGFR** | **Osimertinib** | **High** (CNS ORR 60-70%) | **FLAURA, BLOOM, AURA3** |
| **EGFR Ex20ins** | **Amivantamab** | Moderate | **CHRYSALIS** |
| **ALK** | **Lorlatinib** | **Very High** (CNS ORR 60-70%) | **CROWN** |
| | **Alectinib** | High | **ALEX, J-ALEX** |
| | **Brigatinib** | High | **ALTA-1L** |
| **ROS1** | **Entrectinib** | High | **TRIDENT-1** |
| **KRAS G12C** | **Sotorasib/Adagrasib** | Moderate | **CodeBreaK/KRYSTAL** |
| **No Driver** | **ICI + Chemo** | Variable | **KEYNOTE-189, IMpower150** |

### Breast Cancer Brain Mets

| Subtype | Preferred Systemic |
|---------|-------------------|
| **HER2+** | **Tucatinib + Capecitabine + Trastuzumab** (HER2CLIMB: **CNS ORR 47%, OS HR 0.58**) |
| | **T-DXd (Trastuzumab Deruxtecan)** (DESTINY-Breast03: **CNS Activity**) |
| **HR+/HER2-** | **CDK4/6i (Abemaciclib: CNS Penetration)** + Endocrine |
| **TNBC** | **ICI (Pembro) + Chemo** (KEYNOTE-355/522) |

### Melanoma Brain Mets

| Agent | CNS Activity |
|-------|--------------|
| **Ipilimumab + Nivolumab** | **CheckMate 204: Intracranial ORR 46-57%**, Durable |
| **Pembrolizumab** | **KEYNOTE-022: Intracranial ORR 22%** |
| **Dabrafenib + Trametinib** (BRAF V600E) | **COMBI-MB: Intracranial ORR 58%** |

---

## 9. Supportive Care

| Issue | Management |
|-------|------------|
| **Vasogenic Oedema** | **Dexamethasone 4-16mg/day** (IV/PO) — **Taper Over 1-2 Weeks** once RT Started/Stable |
| **Seizures** | **Levetiracetam** (Prophylaxis if Supratentorial); **No Routine Prophylaxis for Infratentorial** |
| **VTE Prophylaxis** | **LMWH (Enoxaparin 40mg daily)** — **High Risk (Cancer + Immobility + Brain)**; **DOACs if No Active Bleeding** |
| **Anticoagulation (Therapeutic)** | **LMWH Preferred** (DOACs: Intracranial Haemorrhage Risk) |

---

## 10. Radionecrosis vs Progression

| Feature | **Radionecrosis** | **Tumour Progression** |
|---------|-------------------|------------------------|
| **Timing** | **>6-12 Months Post-RT** | **Variable, Often <6mo** |
| **MRI** | **Ring Enhancement, Perilesional Oedema**, **Stable/Slow Growth** | **Progressive Enhancement, New Lesions** |
| **Clinical** | **Stable/Slow Worsening** | **Progressive Deficits** |
| **Advanced Imaging** | **PET: Hypometabolic**; **Perfusion: Low rCBV**; **Spectroscopy: Lipids/Lactate, Low Cho/NAA** | **PET: Hypermetabolic**; **Perfusion: High rCBV**; **Spectroscopy: High Cho/NAA** |
| **Management** | **Bevacizumab, Hyperbaric O2, Surgery** | **SRS, Systemic, Surgery** |

---

## 11. FCPS/MRCP High-Yield Summary

| Topic | Key Points |
|-------|------------|
| **Epidemiology** | **Most Common CNS Malignancy**; **Lung 50%, Breast 15-20%, Melanoma 10%, RCC, GI** |
| **SRS vs WBRT** | **1-3 Mets: SRS Standard** (Equiv OS, Less Cognitive Decline); **>3 Mets: WBRT or SRS** (JROSG-99) |
| **Surgery** | **Solitary, Symptomatic, Accessible, >3cm, Diagnostic Uncertainty** → **Cavity SRS Post-Op** |
| **WBRT** | **30Gy/10fx or 20Gy/5fx**; **HA-WBRT + Memantine Preserves Memory** |
| **Lung EGFR/ALK** | **Osimertinib, Lorlatinib, Alectinib, Brigatinib** — **High CNS Penetration** |
| **Breast HER2+** | **Tucatinib + Cape + Tras (HER2CLIMB)**, **T-DXd** |
| **Melanoma** | **Ipi+Nivo (CheckMate 204)**, **Pembro**, **Dab/Tram (BRAF)** |
| **Dexamethasone** | **Vasogenic Oedema**; **Taper Over 1-2wk** |
| **VTE Prophylaxis** | **LMWH** (High Risk) |
| **Prognosis** | **RPA/GPA/DS-GPA**; **Lung EGFR/ALK Best**; **Melanoma ICI Best** |

---

## 12. Viva Questions (MRCP PACES / FCPS)

| Question | Expected Answer |
|----------|-----------------|
| **60M, NSCLC, 2 Brain Mets (1.5cm, 2cm), KPS 80, EGFR Ex19del. Management?** | **SRS to Both Mets** → **Osimertinib (CNS Penetration)** — **Avoid WBRT** (Neurocognitive Preservation). |
| **55F, Breast Cancer, 4 Brain Mets, HER2+. Management?** | **SRS to All 4 (JROSG-99: SRS Non-Inferior for 5-10 Mets)** + **Tucatinib + Capecitabine + Trastuzumab (HER2CLIMB)**. |
| **SRS vs WBRT for 1-3 Mets — Key Trial?** | **JROSG / NCCTG N0574**: **SRS Alone Non-Inferior OS to SRS+WBRT**; **Less Neurocognitive Decline with SRS**. |
| **When to Operate on Brain Met?** | **Solitary, Symptomatic (Mass Effect), Accessible, >3cm, Diagnostic Uncertainty** → **Resection + Cavity SRS**. |
| **Hippocampal-Avoidance WBRT — Trial?** | **NRG CC001**: **HA-WBRT + Memantine → Less Memory Decline** vs Standard WBRT. |
| **NSCLC EGFR Ex19del Brain Mets — Best TKI?** | **Osimertinib** — **High CNS Penetration, CNS ORR 60-70%** (BLOOM, AURA3). |
| **Dexamethasone for Brain Mets — Dose, Taper?** | **4-16mg/day** (IV/PO); **Taper Over 1-2 Weeks** Once RT Started/Oedema Controlled. |
| **Radionecrosis vs Progression — MRI Differentiation?** | **PET: Radionecrosis = Hypometabolic; Progression = Hypermetabolic**; **Perfusion: Radionecrosis = Low rCBV; Progression = High rCBV**. |
| **VTE Prophylaxis in Brain Mets?** | **LMWH (Enoxaparin 40mg daily)** — **High Risk (Cancer + Immobility + Brain)**; **DOACs Caution (ICH Risk)**. |
| **Quartz Trial — NSCLC Brain Mets, WBRT?** | **QUARTZ**: **WBRT + Dex vs Dex Alone** → **No OS/QOL Benefit** for WBRT in Unfit NSCLC. |

---

## 13. Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **SRS for >3 Mets** | **JROSG-99**: **SRS for 5-10 Mets Non-Inferior to WBRT**; **Up to 10-15 Mets Feasible with Modern SRS** |
| **WBRT Dose** | **30Gy/10fx (Standard)**; **20Gy/5fx (Poor Prognosis/KPS<70)**; **HA-WBRT + Memantine Preferred** |
| **Osimertinib vs 1/2G EGFR TKIs** | **Osimertinib: High CNS Penetration, T790M, 1L Standard**; **Gefitinib/Erlotinib/Afatinib: Poor CNS Penetration** |
| **SRS + WBRT vs SRS Alone** | **SRS Alone = Standard for 1-3 Mets**; **WBRT Adds Local Control BUT ↑Neurocognitive Decline** |
| **Cavity SRS Post-Surgery** | **Single Fraction 15-18Gy to Resection Cavity** — **Standard of Care** |
| **DS-GPA Lung** | **Adds EGFR, ALK to GPA** — **Better Prognostication** |

**Mnemonic: BRAIN-METS**
- **B**rain Mets: **Most Common CNS Malignancy** (10x Primary)
- **R**PA/GPA/DS-GPA: **Prognostic Classes** (KPS, Age, Extracranial, #Mets, Molecular)
- **A**ccess: **Surgery for Solitary/Symptomatic/Accessible** → Cavity SRS
- **I**mmunotherapy: **Melanoma (Ipi+Nivo), NSCLC (ICI+Chemo), TNBC (Pembro)**
- **N**SCLC Drivers: **EGFR (Osimertinib), ALK (Lorlatinib/Alectinib), ROS1 (Entrectinib)**
- **G**lioblastoma vs Mets: **Mets = Multiple, Junction, Haemorrhage (Melanoma/RCC)**
- **M**olecular-Driven: **Lung EGFR/ALK, Breast HER2 (Tucatinib/T-DXd), Melanoma ICI**
- **E**dema: **Dexamethasone 4-16mg/d, Taper 1-2wk**
- **T**argeted: **HER2CLIMB (Tucatinib), DESTINY (T-DXd), HER2CLIMB-BM**
- **S**RS vs WBRT: **1-3 Mets = SRS**; **>3 = WBRT/SRS**; **HA-WBRT + Memantine**

---

## 14. Mind Map

```mermaid
mindmap
  root((Brain Metastases))
    Sources
      Lung (50%)
      Breast (15-20%)
      Melanoma (10%)
      RCC, GI
    Prognosis
      RPA (KPS, Age, Primary, Extracranial)
      GPA (KPS, Age, Extracranial, #Mets)
      DS-GPA (Adds Molecular: EGFR, ALK, HER2)
    Local Therapy
      1-3 Mets: SRS (Standard)
      >3 Mets: WBRT / SRS (JROSG-99)
      Surgery: Solitary/Symptomatic/Accessible → Cavity SRS
      WBRT: 30Gy/10fx (HA-WBRT + Memantine)
    Molecular Systemic
      Lung: EGFR (Osimertinib), ALK (Lorlatinib/Alectinib)
      Breast: HER2 (Tucatinib, T-DXd)
      Melanoma: Ipi+Nivo, Pembro, Dab/Tram
    Supportive
      Dexamethasone (Oedema)
      Levetiracetam (Seizures)
      LMWH (VTE)
    Radionecrosis vs Progression
      PET/Perfusion/Spectroscopy
```

---

## 15. One-Page Revision Card

| Domain | Key Points |
|--------|------------|
| **Sources** | Lung 50%, Breast 15-20%, Melanoma 10% |
| **SRS vs WBRT** | 1-3 Mets: SRS (≥4: WBRT/SRS); JROSG-99: SRS 5-10 Mets OK |
| **Surgery** | Solitary/Symptomatic/Accessible → Cavity SRS |
| **WBRT** | 30Gy/10fx; HA-WBRT + Memantine |
| **Lung EGFR/ALK** | Osimertinib / Lorlatinib / Alectinib / Brigatinib |
| **Breast HER2+** | Tucatinib + Cape + Tras (HER2CLIMB), T-DXd |
| **Melanoma** | Ipi+Nivo (CheckMate 204), Pembro, Dab/Tram (BRAF) |
| **Dexamethasone** | 4-16mg/d, Taper 1-2wk |
| **VTE** | LMWH (High Risk) |
| **Radionecrosis** | PET Hypometabolic, Low rCBV; vs Progression Hypermetabolic, High rCBV |

---

## 16. Spaced Repetition Trackers

| Review Interval | Date Completed | Confidence (1-5) | Notes |
|-----------------|----------------|------------------|-------|
| 24 hours | | | |
| 7 days | | | |
| 15 days | | | |
| 30 days | | | |
| 90 days | | | |

---

## 17. Self-Test Scorecard

| Section | Score /5 | Last Attempt |
|---------|----------|--------------|
| SRS vs WBRT Indications | | |
| Surgery Criteria | | |
| Molecular Systemic Therapy | | |
| RPA/GPA/DS-GPA | | |
| Radionecrosis vs Progression | | |
| Dexamethasone Taper | | |
| VTE Prophylaxis | | |
| Hippocampal-Avoidance WBRT | | |

---

## 18. Local Navigation
- **Parent Heading**: [[../Oncology|Oncology]]
- **Chapter Map": [[../Davidson Chapter 7 - Oncology Hierarchy|Oncology Hierarchy]]
- **Chapter MOC": [[../Oncology MOC|Oncology MOC]]
- **Drug Reference": [[../../Clinical Therapeutics and Good Prescribing|Drugs]]
- **Related": [[Glioblastoma]], [[Meningioma]], [[Primary CNS Lymphoma]], [[NSCLC]], [[Breast Cancer]], [[Melanoma]], [[SRS vs WBRT]], [[EGFR TKIs CNS]], [[ALK TKIs CNS]]

---

# FCPS/MRCP Exam Extras

## 19. MCQs (10)


**1.** Regarding Brain Metastases (Epidemiology), which statement is correct?
   A. **Most Common CNS Malignancy**
   B. **Most - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **Most Common CNS Malignancy**; **Lung 50%, Breast 15-20%, Melanoma 10%, RCC, GI**


**2.** Regarding Brain Metastases (SRS vs WBRT), which statement is correct?
   A. **1-3 Mets: SRS Standard** (Equiv OS, Less Cognitive Decline)
   B. **1-3 - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **1-3 Mets: SRS Standard** (Equiv OS, Less Cognitive Decline); **>3 Mets: WBRT or SRS** (JROSG-99)


**3.** Regarding Brain Metastases (Surgery), which statement is correct?
   A. **Solitary, Symptomatic, Accessible, >3cm, Diagnostic Uncertainty** → **Cavity SRS Post-Op**
   B. **Solitary, - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **Solitary, Symptomatic, Accessible, >3cm, Diagnostic Uncertainty** → **Cavity SRS Post-Op**


**4.** Regarding Brain Metastases (WBRT), which statement is correct?
   A. **30Gy/10fx or 20Gy/5fx**
   B. **30Gy/10fx - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **30Gy/10fx or 20Gy/5fx**; **HA-WBRT + Memantine Preserves Memory**


**5.** Regarding Brain Metastases (Lung EGFR/ALK), which statement is correct?
   A. **Osimertinib, Lorlatinib, Alectinib, Brigatinib**
   B. **Osimertinib, - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **Osimertinib, Lorlatinib, Alectinib, Brigatinib** — **High CNS Penetration**


**6.** Regarding Brain Metastases (Breast HER2+), which statement is correct?
   A. **Tucatinib + Cape + Tras (HER2CLIMB)**, **T-DXd**
   B. **Tucatinib - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **Tucatinib + Cape + Tras (HER2CLIMB)**, **T-DXd**


**7.** Regarding Brain Metastases (Melanoma), which statement is correct?
   A. **Ipi+Nivo (CheckMate 204)**, **Pembro**, **Dab/Tram (BRAF)**
   B. **Ipi+Nivo - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **Ipi+Nivo (CheckMate 204)**, **Pembro**, **Dab/Tram (BRAF)**


**8.** Regarding Brain Metastases (Dexamethasone), which statement is correct?
   A. **Vasogenic Oedema**
   B. **Vasogenic - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **Vasogenic Oedema**; **Taper Over 1-2wk**


**9.** Regarding Brain Metastases (VTE Prophylaxis), which statement is correct?
   A. **LMWH** (High Risk)
   B. **LMWH** - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **LMWH** (High Risk)


**10.** Regarding Brain Metastases (Prognosis), which statement is correct?
   A. **RPA/GPA/DS-GPA**
   B. **RPA/GPA/DS-GPA** - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **RPA/GPA/DS-GPA**; **Lung EGFR/ALK Best**; **Melanoma ICI Best**


## 20. SBA Questions (10)


**1.** A 55-year-old presents with classic features. MDT discussion recommends:
   - A. **Most Common CNS Malignancy**
   - B. **Most (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — first-line: **Most Common CNS Malignancy**; **Lung 50%, Breast 15-20%, Melanoma 10%, RCC, GI**


**2.** On staging workup, the patient is found to be [Stage X]. Best management is:
   - A. **1-3 Mets: SRS Standard** (Equiv OS, Less Cognitive Decline)
   - B. **1-3 (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — stage-specific: **1-3 Mets: SRS Standard** (Equiv OS, Less Cognitive Decline); **>3 Mets: WBRT or SRS** (JROSG-99)


**3.** Following first-line treatment, the patient develops [complication]. Best next step:
   - A. **Solitary, Symptomatic, Accessible, >3cm, Diagnostic Uncertainty** → **Cavity SRS Post-Op**
   - B. **Solitary, (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — complication: **Solitary, Symptomatic, Accessible, >3cm, Diagnostic Uncertainty** → **Cavity SRS Post-Op**


**4.** The patient asks about prognosis. Most appropriate response based on:
   - A. **30Gy/10fx or 20Gy/5fx**
   - B. **30Gy/10fx (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — prognosis: **30Gy/10fx or 20Gy/5fx**; **HA-WBRT + Memantine Preserves Memory**


**5.** A 65-year-old with relevant risk factors should be screened with:
   - A. **Osimertinib, Lorlatinib, Alectinib, Brigatinib**
   - B. **Osimertinib, (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — screening: **Osimertinib, Lorlatinib, Alectinib, Brigatinib** — **High CNS Penetration**


**6.** The most clinically important biomarker/molecular test is:
   - A. **Tucatinib + Cape + Tras (HER2CLIMB)**, **T-DXd**
   - B. **Tucatinib (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — biomarker: **Tucatinib + Cape + Tras (HER2CLIMB)**, **T-DXd**


**7.** The standard chemotherapy/regimen of choice is:
   - A. **Ipi+Nivo (CheckMate 204)**, **Pembro**, **Dab/Tram (BRAF)**
   - B. **Ipi+Nivo (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — chemo: **Ipi+Nivo (CheckMate 204)**, **Pembro**, **Dab/Tram (BRAF)**


**8.** The role of surgery in this case is:
   - A. **Vasogenic Oedema**
   - B. **Vasogenic (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — surgery: **Vasogenic Oedema**; **Taper Over 1-2wk**


**9.** The recommended surveillance/follow-up protocol is:
   - A. **LMWH** (High Risk)
   - B. **LMWH** (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — follow-up: **LMWH** (High Risk)


**10.** Palliative care referral is most appropriate when:
   - A. **RPA/GPA/DS-GPA**
   - B. **RPA/GPA/DS-GPA** (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — palliative: **RPA/GPA/DS-GPA**; **Lung EGFR/ALK Best**; **Melanoma ICI Best**


## 21. Flashcards

**Q1:** Epidemiology?
**A1:** Most Common CNS Malignancy; Lung 50%, Breast 15-20%, Melanoma 10%, RCC, GI

**Q2:** SRS vs WBRT?
**A2:** 1-3 Mets: SRS Standard (Equiv OS, Less Cognitive Decline); >3 Mets: WBRT or SRS (JROSG-99)

**Q3:** Surgery?
**A3:** Solitary, Symptomatic, Accessible, >3cm, Diagnostic Uncertainty → Cavity SRS Post-Op

**Q4:** WBRT?
**A4:** 30Gy/10fx or 20Gy/5fx; HA-WBRT + Memantine Preserves Memory

**Q5:** Lung EGFR/ALK?
**A5:** Osimertinib, Lorlatinib, Alectinib, Brigatinib — High CNS Penetration

**Q6:** Breast HER2+?
**A6:** Tucatinib + Cape + Tras (HER2CLIMB), T-DXd

**Q7:** Melanoma?
**A7:** Ipi+Nivo (CheckMate 204), Pembro, Dab/Tram (BRAF)

**Q8:** Dexamethasone?
**A8:** Vasogenic Oedema; Taper Over 1-2wk

## 22. Answer Key with Explanations

| # | MCQ | Topic | Explanation |
|---|-----|-------|-------------|
| 1 | A | Epidemiology | Most Common CNS Malignancy; Lung 50%, Breast 15-20%, Melanoma 10%, RCC, GI |
| 2 | A | SRS vs WBRT | 1-3 Mets: SRS Standard (Equiv OS, Less Cognitive Decline); >3 Mets: WBRT or SRS (JROSG-99) |
| 3 | A | Surgery | Solitary, Symptomatic, Accessible, >3cm, Diagnostic Uncertainty → Cavity SRS Post-Op |
| 4 | A | WBRT | 30Gy/10fx or 20Gy/5fx; HA-WBRT + Memantine Preserves Memory |
| 5 | A | Lung EGFR/ALK | Osimertinib, Lorlatinib, Alectinib, Brigatinib — High CNS Penetration |
| 6 | A | Breast HER2+ | Tucatinib + Cape + Tras (HER2CLIMB), T-DXd |
| 7 | A | Melanoma | Ipi+Nivo (CheckMate 204), Pembro, Dab/Tram (BRAF) |
| 8 | A | Dexamethasone | Vasogenic Oedema; Taper Over 1-2wk |
| 9 | A | VTE Prophylaxis | LMWH (High Risk) |
| 10 | A | Prognosis | RPA/GPA/DS-GPA; Lung EGFR/ALK Best; Melanoma ICI Best |

| # | SBA | Topic | Explanation |
|---|-----|-------|-------------|
| 1 | A | Epidemiology | Most Common CNS Malignancy; Lung 50%, Breast 15-20%, Melanoma 10%, RCC, GI |
| 2 | A | SRS vs WBRT | 1-3 Mets: SRS Standard (Equiv OS, Less Cognitive Decline); >3 Mets: WBRT or SRS (JROSG-99) |
| 3 | A | Surgery | Solitary, Symptomatic, Accessible, >3cm, Diagnostic Uncertainty → Cavity SRS Post-Op |
| 4 | A | WBRT | 30Gy/10fx or 20Gy/5fx; HA-WBRT + Memantine Preserves Memory |
| 5 | A | Lung EGFR/ALK | Osimertinib, Lorlatinib, Alectinib, Brigatinib — High CNS Penetration |
| 6 | A | Breast HER2+ | Tucatinib + Cape + Tras (HER2CLIMB), T-DXd |
| 7 | A | Melanoma | Ipi+Nivo (CheckMate 204), Pembro, Dab/Tram (BRAF) |
| 8 | A | Dexamethasone | Vasogenic Oedema; Taper Over 1-2wk |
| 9 | A | VTE Prophylaxis | LMWH (High Risk) |
| 10 | A | Prognosis | RPA/GPA/DS-GPA; Lung EGFR/ALK Best; Melanoma ICI Best |

## 23. Local Navigation


- **Parent Heading Hub**: [[../../CNS Tumours|CNS Tumours]]
- **Chapter Map**: [[../../Davidson Chapter 7 - Oncology Hierarchy|Oncology Hierarchy]]
- **Chapter MOC**: [[../../Oncology MOC|Oncology MOC]]
- **Drug Reference**: [[../../../Clinical Therapeutics and Good Prescribing|Drugs]]

