---
tags: [medicine, davidson, hematology, essential-thrombocythaemia, et, mpn, myeloproliferative-neoplasm, fcps, mrcp]
davidson_chapter: Chapter 25: Haematology and Transfusion Medicine
status: full-fcps-mrcp-note
priority: high
exam_relevance: "FCPS: Essential | MRCP: Core | JAK2/CALR/MPL, IPSET-thrombosis, hydroxyurea, anagrelide, interferon, pregnancy, acquired VWS"
see_also: "[[Polycythaemia Vera]], [[Primary Myelofibrosis]], [[MPN]], [[JAK2 Mutations]], [[Acquired von Willebrand Syndrome]]"
created: 2025-06-16
modified: 2025-06-16
---

# Essential Thrombocythaemia (ET)

> [!info] **Davidson Ch 25 Alignment**: Haematological Malignancies → Myeloproliferative Neoplasms → Essential Thrombocythaemia
> **FCPS/MRCP Focus**: JAK2/CALR/MPL mutations, IPSET-thrombosis risk stratification, hydroxyurea, anagrelide, interferon-α, acquired VWS, pregnancy management

---

## 🎯 Learning Objectives

- [ ] Define ET: **Clonal MPN** with **sustained thrombocytosis (Plt >450×10⁹/L)** + megakaryocytic hyperplasia
- [ ] Apply **WHO 2022 Criteria**: Platelet count, BM megakaryocytes, **JAK2/CALR/MPL mutation**, exclusion of PV/PMF/secondary
- [ ] Apply **IPSET-Thrombosis Risk Stratification**: Age >60, prior thrombosis, JAK2 V617F, CV risk factors
- [ ] Manage **Low-risk**: **Aspirin 75-100 mg daily** (if no bleeding risk)
- [ ] Manage **High-risk**: **Hydroxyurea** first-line; **Anagrelide** (platelet-specific); **Interferon-α** (young/pregnancy)
- [ ] Recognise **Acquired von Willebrand Syndrome (AVWS)**: Plt >1000-1500 → bleeding despite thrombosis risk
- [ ] Manage **Pregnancy in ET**: **Interferon-α** (safe); **Aspirin**; **Avoid HU/Anagrelide**

---

## 📖 Definition & WHO 2022 Criteria

| **Major Criteria** | |
|---------------------|---|
| 1. **Platelet count ≥450×10⁹/L** | |
| 2. **BM biopsy**: **Megakaryocytic hyperplasia** (large, mature, hyperlobated nuclei) – **NO significant erythroid/granulocytic proliferation** | |
| 3. **JAK2 V617F, CALR, or MPL mutation** | |
| 4. **Exclusion** of PV, PMF, CML, secondary thrombocytosis, other myeloid neoplasms | |

**Diagnosis**: **All 4 Major Criteria** met

> [!tip] **FCPS/MRCP**: **ET = Thrombocytosis ≥450 + Megakaryocyte hyperplasia + Driver mutation (JAK2 50-60%, CALR 25-30%, MPL 3-5%)**. **CALR = better prognosis, lower thrombosis risk**. **"Triple-negative" (10-15%) = worse prognosis**.

---

## ⚙️ Pathophysiology

```mermaid
flowchart TD
    A[Driver Mutation] --> B[Constitutive JAK-STAT / MPL Signaling]
    B --> C[Megakaryocyte Hyperplasia]
    C --> D[↑ Platelet Production]
    D --> E[Thrombocytosis]
    E --> F1[Thrombosis Risk: Platelet activation + JAK2 V617F ↑ vWF + ↑ vWF-platelet interaction]
    E --> F2[Bleeding Risk (Plt >1000): **Acquired von Willebrand Syndrome** – vWF adsorption on platelets]
    
    A -.->|JAK2 V617F (50-60%)| G1[Higher Thrombosis Risk]
    A -.->|CALR Type 1/2 (25-30%)| G2[Lower Thrombosis Risk, Better OS]
    A -.->|MPL W515L/K (3-5%)| G3[Intermediate]
    A -.->|Triple-Negative (10-15%)| G4[Worse Prognosis, Higher MF Transformation]
```

---

## 🔬 Diagnostic Workup

```mermaid
flowchart TD
    A[Thrombocytosis: Plt ≥450×10⁹/L] --> B[Exclude Reactive/Secondary Causes]
    B --> C{**Iron Deficiency, Infection, Inflammation, Splenectomy, Malignancy, Tissue Damage**}
    C -->|Excluded| D[**Driver Mutation Testing**]
    D --> E1[**JAK2 V617F**]
    D --> E2[**CALR Exon 9 (Type 1/2)**]
    D --> E3[**MPL W515L/K**]
    E1 & E2 & E3 --> F[**BM Biopsy** if mutation +ve or uncertain]
    F --> G{Megakaryocyte Hyperplasia? Large, Mature, Hyperlobated?}
    G -->|Yes| H[**ET Diagnosis**]
    G -->|No / Fibrosis| I[Consider PMF / PV]
```

### Key Investigations

| Test | ET Finding |
|------|------------|
| **CBC** | **Plt ≥450×10⁹/L** (often >1000); Hb/WBC normal |
| **Blood Film** | **Large platelets**, **platelet clumps**, **no dysplasia** |
| **JAK2 V617F** | **50-60%** |
| **CALR Exon 9** | **25-30%** (Type 1 = 52bp del; Type 2 = 5bp ins) |
| **MPL W515L/K** | **3-5%** |
| **Triple-Negative** | **10-15%** |
| **BM Biopsy** | **Megakaryocytic hyperplasia**; large, mature, hyperlobulated; **NO trilineage** |
| **Iron Studies** | Exclude iron deficiency (reactive thrombocytosis) |
| **Inflammatory Markers** | Exclude reactive (CRP, ESR) |

---

## 🩺 Clinical Features

| Feature | Details |
|---------|---------|
| **Asymptomatic** | Many diagnosed incidentally |
| **Microvascular Disturbances** | **Erythromelalgia** (burning hands/feet, relieved by aspirin/cooling), **TIAs**, **visual disturbances**, **headache**, **paresthesiae** |
| **Thrombosis** | **Arterial (MI, stroke, TIA) + Venous (DVT, PE, Budd-Chiari, portal vein)** |
| **Bleeding** | **Acquired von Willebrand Syndrome (AVWS)** if Plt >1000-1500: epistaxis, gum bleeding, GI bleed |
| **Splenomegaly** | Mild (~20-30%) |
| **Constitutional** | Fatigue, night sweats, weight loss (less than PV) |

---

## 📊 Risk Stratification (IPSET-Thrombosis)

| Risk Factor | Points |
|-------------|--------|
| **Age >60** | 2 |
| **Prior Thrombosis** | 1 |
| **JAK2 V617F Mutation** | 1 |
| **CV Risk Factors** (HTN, DM, Smoking) | 1 |

| Score | Risk Category | Annual Thrombosis Rate | Management |
|-------|---------------|------------------------|------------|
| **0-1** | **Low** | ~1% | **Aspirin 75-100 mg daily** (if no bleeding risk) |
| **2** | **Intermediate** | ~2-3% | **Aspirin**; Consider cytoreduction if other factors |
| **≥3** | **High** | ~4-5%+ | **Aspirin + Cytoreduction (Hydroxyurea)** |

> [!tip] **CALR mutation = protective (lower thrombosis risk)**. **IPSET-thrombosis validated in >1000 patients**.

---

## 💊 Management

### Low-Risk (IPSET 0-1)

| Intervention | Details |
|--------------|---------|
| **Aspirin** | **75-100 mg daily** (if Plt <1000, no bleeding diathesis) |
| **Observation** | Regular CBC (q3-6mo), symptom review |
| **CV Risk Factor Control** | HTN, lipids, diabetes, smoking cessation |

### High-Risk (IPSET ≥3) + Intermediate with Indications

| Agent | Indication | Starting Dose | Target/Monitoring |
|-------|------------|---------------|-------------------|
| **Hydroxyurea (HU)** | **First-line cytoreduction** | 15 mg/kg/day (round to 500mg) | **Plt <400**, WBC >3, Hb >10; CBC q2-4wk titrate → q3mo stable |
| **Anagrelide** | **Platelet-specific**; HU-intolerant; **High Plt >1000** | 0.5 mg BD → titrate (max 10 mg/day) | **Plt <400**; **Avoid if CVD** (arrhythmias, HF); Monitor ECG, echo |
| **Interferon-α (Peg-IFN-α)** | **Young (<40)**, **Pregnancy**, HU-intolerant | 45-90 µg SC weekly | **Plt <400**, Molecular (CALR/JAK2) response; Safe in pregnancy |
| **Busulfan** | Elderly, short life expectancy | 2-4 mg/day | **Avoid if possible** (leukaemogenic) |

> [!tip] **Anagrelide = Platelet-specific (no effect on WBC/Hb)**; **Cardiac monitoring required**. **Interferon-α = Only safe cytoreductive in pregnancy**.

---

## ⚠️ Acquired von Willebrand Syndrome (AVWS)

| Feature | Details |
|---------|---------|
| **Mechanism** | **Plt >1000-1500** → adsorption of **vWF** on platelet surface → **loss of HMW multimers** |
| **Presentation** | **Bleeding** (epistaxis, GI, post-procedure) **despite thrombocytosis** |
| **Diagnosis** | **vWF:Ag ↓, vWF:RCo ↓↓, vWF:Ag/vWF:RCo ratio >2**, **HMW multimers absent** |
| **Management** | **Platelet apheresis** (rapid ↓ Plt), **Desmopressin (DDAVP)**, **Avoid aspirin if active bleed**, **Hydroxyurea/Anagrelide** to lower Plt |

---

## 🤰 Pregnancy in ET

| Drug | Safety | Recommendation |
|------|--------|----------------|
| **Aspirin** | **Safe** (low dose) | **Continue 75-100 mg daily** throughout |
| **Hydroxyurea** | **Teratogenic (Category D)** | **CONTRAINDICATED** – stop before conception |
| **Anagrelide** | **Contraindicated** | Stop before conception |
| **Interferon-α (Peg-IFN-α)** | **Safe** | **Preferred cytoreductive in pregnancy** |
| **Heparin (LMWH)** | **Safe** | Prophylactic if high-risk (prior thrombosis, JAK2) |

**Pregnancy Risk**: **Miscarriage rate ↑** (especially JAK2); **Thrombosis risk ↑** postpartum; **Aspirin + LMWH prophylaxis** if high-risk

---

## 🔄 Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **Reactive/Secondary Thrombocytosis** | **No driver mutation**, Iron deficiency, infection, inflammation, splenectomy, malignancy – **resolves with treatment** |
| **Polycythaemia Vera (PV)** | **Hb/Hct ↑** (erythrocytosis dominant); JAK2+; trilineage BM |
| **Primary Myelofibrosis (PMF)** | **Fibrosis**, teardrops, leukoerythroblastic film, splenomegaly; JAK2/CALR/MPL |
| **CML** | **BCR::ABL1+**, WBC ↑↑, basophilia, splenomegaly |
| **MPL-Mutant ET vs PMF** | **MPL in ET = lower transformation**; **MPL in PMF = worse prognosis** |

---

## 💡 FCPS/MRCP High-Yield Summary

| Topic | Key Point |
|-------|-----------|
| **Diagnosis** | **Plt ≥450 + Megakaryocyte hyperplasia + JAK2/CALR/MPL** |
| **Driver Mutations** | **JAK2 V617F (50-60%)**, **CALR Type 1/2 (25-30%)**, **MPL (3-5%)**, **Triple-neg (10-15%)** |
| **CALR vs JAK2** | **CALR = Lower thrombosis risk, better OS**; **JAK2 = Higher risk** |
| **Risk Stratification** | **IPSET-Thrombosis**: Age>60 (2pts), Prior thrombosis (1), JAK2 (1), CV risk (1) |
| **Low Risk** | **Aspirin 75-100 mg daily** |
| **High Risk** | **Aspirin + Hydroxyurea** (1st line) |
| **Anagrelide** | **Platelet-specific**; **Avoid if CVD** (arrhythmia); HU-intolerant |
| **Interferon-α** | **Young/Pregnancy**; **Safe in pregnancy**; Molecular remission |
| **AVWS** | **Plt >1000-1500** → vWF adsorption → **Bleeding**; **Apheresis + DDAVP** |
| **Pregnancy** | **Aspirin + Interferon-α; Avoid HU/Anagrelide** |

---

## ❓ Viva Questions

1. **What are the WHO 2022 diagnostic criteria for Essential Thrombocythaemia?**
   - **Plt ≥450**, **BM megakaryocytic hyperplasia**, **JAK2/CALR/MPL mutation**, **Exclusion of PV/PMF/secondary**

2. **What are the driver mutations in ET and their frequencies?**
   - **JAK2 V617F (50-60%)**, **CALR exon 9 (25-30%)**, **MPL W515L/K (3-5%)**, **Triple-negative (10-15%)**

3. **How does CALR mutation differ from JAK2 V617F in prognosis?**
   - **CALR = Lower thrombosis risk, better overall survival**; **JAK2 = Higher thrombosis risk**

4. **What is the IPSET-Thrombosis risk stratification?**
   - Age >60 (2pts), Prior thrombosis (1), JAK2 mutation (1), CV risk factors (1); **≥3 = High risk**

5. **What is the first-line cytoreductive therapy for high-risk ET?**
   - **Hydroxyurea** (15 mg/kg/day; target Plt <400)

6. **How does Anagrelide differ from Hydroxyurea?**
   - **Anagrelide = Platelet-specific** (no effect on WBC/Hb); **Cardiac monitoring required** (arrhythmia); **HU = Pan-myelosuppression**

7. **What is Acquired von Willebrand Syndrome and when does it occur?**
   - **Plt >1000-1500** → vWF adsorption on platelets → **loss of HMW multimers** → **bleeding risk**

8. **How is AVWS managed?**
   - **Platelet apheresis** (rapid Plt reduction), **Desmopressin (DDAVP)**, **Hold aspirin if bleeding**, **Cytoreduction (HU/Anagrelide)**

9. **What is the safe cytoreductive therapy in pregnancy for ET?**
   - **Interferon-α (Peg-IFN-α)** – **Safe in pregnancy**; **Avoid Hydroxyurea (teratogenic)** and **Anagrelide**

10. **Differentiate ET from Reactive Thrombocytosis.**
    - **ET = Driver mutation+, BM megakaryocyte hyperplasia, sustained**; **Reactive = No mutation, resolves with treatment of cause**

---

## 🧠 Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **ET vs Reactive Thrombocytosis** | **ET = Mutation+ (JAK2/CALR/MPL), sustained**; **Reactive = Mutation-, resolves** |
| **ET vs PV** | **ET = Thrombocytosis dominant, Plt ≥450, Hb normal**; **PV = Erythrocytosis dominant, Hb/Hct ↑** |
| **ET vs PMF** | **PMF = Fibrosis, teardrops, leukoerythroblastic, splenomegaly**; **ET = No fibrosis** |
| **CALR Type 1 vs Type 2** | **Type 1 = 52bp del (better)**; **Type 2 = 5bp ins** |
| **Anagrelide Cardiac Risk** | **Avoid in CVD**; Monitor ECG/echo |
| **IPSET Points** | **Age>60 = 2pts**; others = 1pt |

| Mnemonic | Meaning |
|----------|---------|
| **"ET = Plt ≥450 + Mega Hyperplasia + Mutation"** | Diagnosis |
| **"JAK2 = Thrombosis Risk; CALR = Better OS"** | Mutation prognosis |
| **"IPSET: Age>60 = 2pts"** | Risk scoring |
| **"HU = 1st Line Cyto"** | Hydroxyurea first |
| **"Anagrelide = Platelet Only"** | Platelet-specific |
| **"IFN = Pregnancy Safe"** | Interferon in pregnancy |
| **"AVWS = Plt >1000 = Bleeding"** | Acquired VWS |

---

## 🗺️ Mind Map

```mermaid
mindmap
  root((Essential Thrombocythaemia))
    Diagnosis
      Plt ≥450
      BM: Megakaryocyte Hyperplasia
      Mutation: JAK2/CALR/MPL
    Mutations
      JAK2 V617F: 50-60% (High Thrombosis)
      CALR Type 1/2: 25-30% (Better OS)
      MPL: 3-5%
      Triple-Neg: 10-15% (Worse)
    Risk Stratification (IPSET)
      Low (0-1): Aspirin
      Intermediate (2): Aspirin ± Cyto
      High (≥3): Aspirin + HU
    Management
      Aspirin 75-100mg (All)
      Low Risk: Observe
      High Risk: HU 1st line
      HU Fail: Anagrelide / IFN-α
    Special
      AVWS: Plt >1000 → Bleeding
      Pregnancy: Aspirin + IFN-α (Safe)
      HU/Anagrelide: Contraindicated
```

---

## 📋 One-Page Revision Card

| **ESSENTIAL THROMBOCYTHAEMIA – FCPS/MRCP REVISION CARD** |
|-----------------------------------------------------------|
| **Diagnosis**: **Plt ≥450 + Megakaryocyte Hyperplasia + JAK2/CALR/MPL** |
| **Mutations**: **JAK2 50-60%** (↑ thrombosis); **CALR 25-30%** (↓ thrombosis, better OS) |
| **IPSET-Thrombosis**: Age>60 (2pts), Prior clot (1), JAK2 (1), CV risk (1) |
| **Low Risk (0-1)**: **Aspirin 75-100mg** |
| **High Risk (≥3)**: **Aspirin + Hydroxyurea** (target Plt <400) |
| **Anagrelide**: **Platelet-specific**; **Avoid CVD** (arrhythmia) |
| **Interferon-α**: **Young/Pregnancy**; **Safe in pregnancy**; Molecular remission |
| **AVWS**: **Plt >1000-1500** → vWF adsorption → **Bleeding** → Apheresis + DDAVP |
| **Pregnancy**: **Aspirin + IFN-α** (Safe); **NO HU / NO Anagrelide** |

---

## 📅 Spaced Repetition Tracker

| Review | Date | Score (1-5) | Next Review |
|--------|------|-------------|-------------|
| Day 1 | 2025-06-16 | | 2025-06-17 |
| Day 3 | | | |
| Day 7 | | | |
| Day 15 | | | |
| Day 30 | | | |

---

## 🎯 Must Know / Should Know / Nice to Know

| Level | Content |
|-------|---------|
| **Must Know** | WHO criteria, mutations (JAK2/CALR/MPL), CALR vs JAK2 prognosis, IPSET-thrombosis scoring, aspirin + HU for high-risk, anagrelide platelet-specific/cardiac risk, interferon for pregnancy/young, AVWS at Plt>1000, pregnancy management |
| **Should Know** | CALR Type 1 vs Type 2, IPSET-thrombosis validation studies, HU dosing/monitoring, anagrelide trials (PT-1, EXELS), interferon molecular remission rates, busulfan historical use, acquired VWS lab diagnosis (vWF:Ag, vWF:RCo, multimers), platelet apheresis technique |
| **Nice to Know** | CALR frameshift mechanism (C-terminal neoepitope), MPL W515 clustering, triple-negative ET prognosis, ropeginterferon approval, momelotinib (ACVR1) in ET, givinostat, thrombosis risk in JAK2 VAF >50%, ET to MF transformation biology, platelet activation markers (PF4, β-TG, sP-selectin) |

---

## ✅ Self-Test Scorecard

| Section | Score (0-10) | Notes |
|---------|--------------|-------|
| WHO Criteria & Mutations | | |
| IPSET-Thrombosis Stratification | | |
| Cytoreductive Therapy Selection | | |
| AVWS & Bleeding Management | | |
| Pregnancy Management | | |
| Viva Questions | | |

---

## 🔗 Local Navigation

- **Previous**: [[Renal Anaemia]]
- **Next**: [[Primary Myelofibrosis]]
- **Section Hub**: [[Haematological Malignancies]]
- **MOC**: [[Hematology MOC]]
- **Template**: [[../Templates/Hematology Topic Template]]

---

*Generated for FCPS/MRCP exam preparation. Based on Davidson Medicine 24th Ed Chapter 25.*
---

> Auto-generated study sections for "Hematology" — Ch 24: Haematology & Transfusion Medicine.

## Flashcards (19 generated)

- Q: What is the definition of Hematology?
  A: [!info] Davidson Ch 25 Alignment: Haematological Malignancies → Myeloproliferative Neoplasms → Essential Thrombocythaemia
- Q: What is the mechanism of Hematology?
  A: Plt >1000-1500 → adsorption of vWF on platelet surface → loss of HMW multimers
- Q: What are the clinical features of Hematology?
  A: Bleeding (epistaxis, GI, post-procedure) despite thrombocytosis
- Q: What is the investigation of choice for Hematology?
  A: vWF:Ag ↓, vWF:RCo ↓↓, vWF:Ag/vWF:RCo ratio >2, HMW multimers absent
- Q: How is Hematology managed?
  A: Platelet apheresis (rapid ↓ Plt), Desmopressin (DDAVP), Avoid aspirin if active bleed, Hydroxyurea/Anagrelide to lower Plt
- Q: What is the mechanism of Hematology?
  A: Plt >1000-1500 → adsorption of vWF on platelet surface → loss of HMW multimers
- Q: What are the clinical features of Hematology?
  A: Bleeding (epistaxis, GI, post-procedure) despite thrombocytosis
- Q: What is the investigation of choice for Hematology?
  A: vWF:Ag ↓, vWF:RCo ↓↓, vWF:Ag/vWF:RCo ratio >2, HMW multimers absent
- Q: How is Hematology managed?
  A: Platelet apheresis (rapid ↓ Plt), Desmopressin (DDAVP), Avoid aspirin if active bleed, Hydroxyurea/Anagrelide to lower Plt
- Q: What is the investigation of choice for Hematology?
  A: Plt ≥450 + Megakaryocyte hyperplasia + JAK2/CALR/MPL
- Q: What is Driver Mutations of Hematology?
  A: JAK2 V617F (50-60%), CALR Type 1/2 (25-30%), MPL (3-5%), Triple-neg (10-15%)
- Q: What is CALR vs JAK2 of Hematology?
  A: CALR = Lower thrombosis risk, better OS; JAK2 = Higher risk
- Q: What is Risk Stratification of Hematology?
  A: IPSET-Thrombosis: Age>60 (2pts), Prior thrombosis (1), JAK2 (1), CV risk (1)
- Q: What is Low Risk of Hematology?
  A: Aspirin 75-100 mg daily
- Q: What is High Risk of Hematology?
  A: Aspirin + Hydroxyurea (1st line)
- Q: What is Anagrelide of Hematology?
  A: Platelet-specific; Avoid if CVD (arrhythmia); HU-intolerant
- Q: What is Interferon-α of Hematology?
  A: Young/Pregnancy; Safe in pregnancy; Molecular remission
- Q: What is AVWS of Hematology?
  A: Plt >1000-1500 → vWF adsorption → Bleeding; Apheresis + DDAVP
- Q: What is Pregnancy of Hematology?
  A: Aspirin + Interferon-α; Avoid HU/Anagrelide

## MCQs (1 generated)

1. **Which of the following best describes Hematology?**
   A. **[!info] Davidson Ch 25 Alignment: Haematological Malignancies → Myeloproliferative Neoplasms → Essential Thrombocythaemia**
   B. An unrelated condition not matching the clinical picture of Hematology
   C. A complication seen late in the disease course of Hematology
   D. A condition that mimics Hematology but has a different underlying cause

## SBA Questions (1 generated)

1. A patient with suspected Hematology presents with: 1. Platelet count ≥450×10⁹/L — ; Diagnosis: All 4 Major Criteria met; [!tip] FCPS/MRCP: ET = Thrombocytosis ≥450 + Megakaryocyte hyperplasia + Driver mutation (JAK2 50-60%, CALR 25-30%, MPL 3-5%). CALR = better prognosis, lower thrombosis risk. "Triple-negative" (10-15%) = worse prognosis.. What is the most likely diagnosis?
   A. **Hematology**
   B. A condition that mimics Hematology but is not the same entity
   C. A complication of Hematology rather than the primary diagnosis
   D. An unrelated condition in the same clinical category as Hematology

## PasTest Scenario SBAs (Clinical Vignettes)

> **Auto-generated PasTest/Mediscope-style scenario SBAs** grounded in the authored source. Each scenario tests a real clinical fact (triad, specific sign, contraindication, trial, first-line Rx) extracted from the topic. *Source: Ch 24: Haematology — Essential Thrombocythaemia*

**Q1.** Which of the following features is most specific or characteristic of Essential Thrombocythaemia?

  - **A.** "Anagrelide = Platelet Only"
  - **B.** A feature common to many acute inflammatory conditions
  - **C.** A non-specific sign that does not localise the diagnosis
  - **D.** An investigation finding rather than a clinical feature

  > **Answer: A** — "Anagrelide = Platelet Only"
  >
  > *Source:* |
| **"IPSET: Age>60 = 2pts"** | Risk scoring |
| **"HU = 1st Line Cyto"** | Hydroxyurea first |
| **"Anagrelide = Platelet Only"** | Platelet-specific |
| **"IFN = Pregnancy Safe"** | Interferon in p

**Q2.** What is the most appropriate first-line therapy for Essential Thrombocythaemia?

  - **A.** Hydroxyurea + First-line cytoreduction + Plt <400
  - **B.** An advanced/surgical therapy reserved for refractory disease
  - **C.** Symptomatic treatment only, no disease-modifying therapy
  - **D.** Empiric broad-spectrum therapy without specific indication

  > **Answer: A** — Hydroxyurea + First-line cytoreduction + Plt <400
  >
  > *Source:* **Hydroxyurea (HU)**   **First-line cytoreduction**   15 mg/kg/day (round to 500mg)   **Plt <400**, WBC >3, Hb >10; CBC q2-4wk titrate → q3mo stable

