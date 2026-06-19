---
tags: [medicine, davidson, hematology, cml, chronic-leukaemia, fcps, mrcp]
davidson_chapter: Chapter 25: Haematology and Transfusion Medicine
status: full-fcps-mrcp-note
priority: high
exam_relevance: "FCPS: Essential | MRCP: Core | High-yield for vivas, TKI sequencing, response milestones, blast crisis"
see_also: "[[Chronic Lymphocytic Leukaemia (CLL)]], [[Acute Myeloid Leukaemia (AML)]], [[Stem Cell Transplantation]], [[Myeloproliferative Neoplasms]]"
created: 2025-06-15
modified: 2025-06-15
---

# Chronic Myeloid Leukaemia (CML)

> [!info] **Davidson Ch 25 Alignment**: Haematological Malignancies → Chronic Leukaemias → CML
> **FCPS/MRCP Focus**: Ph+ (BCR::ABL1), TKI sequencing (Imatinib → 2G/3G), response milestones (ELN 2020), blast crisis management, treatment-free remission (TFR)

---

## 🎯 Learning Objectives

- [ ] Define CML: Clonal myeloproliferative neoplasm driven by **BCR::ABL1** (t(9;22))
- [ ] Classify phases: **Chronic**, **Accelerated**, **Blast Crisis** (myeloid/lymphoid)
- [ ] Diagnose: CBC, blood film, BM, **RT-qPCR BCR::ABL1 (IS)**, FISH, Karyotype
- [ ] Apply **ELN 2020 / NCCN response milestones** at 3, 6, 12, 18 months
- [ ] Select **first-line TKI**: Imatinib vs 2G (Nilotinib, Dasatinib, Bosutinib) based on risk/Sokal/ELTS
- [ ] Manage **TKI failure/intolerance**: Switch to next-generation TKI (2G/3G Ponatinib)
- [ ] Define **Treatment-Free Remission (TFR)** criteria: Deep molecular response (DMR) ≥2 years
- [ ] Manage **Blast Crisis**: Induction (TKI + AML-type/ALL-type chemo) → HSCT
- [ ] Monitor **BCR::ABL1 kinase domain mutations** for resistance (T315I = Ponatinib)
- [ ] Counsel on **pregnancy**: Stop TKI (except interferon-α), breastfeeding considerations

---

## 📖 Definition & Classification

| Feature | Details |
|---------|---------|
| **Driver** | **t(9;22)(q34;q11) → BCR::ABL1 fusion** (Philadelphia chromosome) |
| **Isoforms** | **p210 (b2a2, b3a2)** – classic CML; **p190 (e1a2)** – Ph+ ALL-like, more aggressive |
| **WHO Classification** | CML, BCR::ABL1-positive |
| **Phases** | Chronic Phase (CP), Accelerated Phase (AP), Blast Crisis (BC) |

### Phase Definitions (WHO / MD Anderson / ELN)

| Phase | Criteria |
|-------|----------|
| **Chronic Phase (CP)** | Blasts <10% (BM/PB), Basophils <20%, Platelets ≥100×10⁹/L, No splenomegaly >10cm (palpable) |
| **Accelerated Phase (AP)** | Blasts 10-19% (BM/PB), **Basophils ≥20%**, Platelets <100 (unrelated to therapy), **Additional cytogenetic abnormalities (ACA)**, Spleen >10cm, **Increasing WBC unresponsive to TKI** |
| **Blast Crisis (BC)** | Blasts ≥20% (BM/PB) or **Extramedullary proliferation** of blasts; Myeloid (~70%) or Lymphoid (~20-30%) |

> [!tip] **FCPS/MRCP**: **CML = t(9;22) = BCR::ABL1 p210**. **Phases: CP (<10% blasts), AP (10-19% blasts + basophilia/ACA), BC (≥20% blasts)**.

---

## ⚙️ Pathophysiology

```mermaid
flowchart TD
    A[t(9;22) Translocation] --> B[BCR::ABL1 Fusion Gene]
    B --> C[Constitutively Active Tyrosine Kinase]
    C --> D[Downstream Signalling: PI3K/AKT, RAS/MAPK, JAK/STAT, MYC]
    D --> E[Genomic Instability → Additional Mutations]
    D --> F[Uncontrolled Proliferation]
    D --> G[Impaired Apoptosis]
    D --> H[Adhesion Defects → Premature Release]
    E & F & G & H --> I[Phase Progression: CP → AP → BC]
```

---

## 🔬 Diagnostic Workup

```mermaid
flowchart TD
    A[Suspected CML: Leukocytosis + Splenomegaly + Basophilia] --> B[CBC + Film: Left shift, myelocytes, metamyelocytes, basophils, <10% blasts]
    B --> C[BM Aspirate: Hypercellular, myeloid hyperplasia, <10% blasts]
    C --> D[**RT-qPCR BCR::ABL1 (International Scale - IS)**]
    C --> E[FISH: BCR::ABL1 dual-fusion probe]
    C --> F[Karyotype: t(9;22) + ACA?]
    D & E & F --> G[Phase Determination: CP / AP / BC]
    G --> H[Risk Score: Sokal / Hasford / ELTS]
    H --> I[TKI Selection]
    G --> J[Baseline: BCR::ABL1 KD Mutations if AP/BC, HLA Typing, Echo, LFT, Renal, Lipids, Glucose]
```

### Essential Baseline Investigations

| Test | Purpose |
|------|---------|
| **RT-qPCR BCR::ABL1 (IS)** | **Gold standard for diagnosis & monitoring** (quantitative, IS calibrated) |
| **FISH** | Rapid confirmation, detects cryptic translocations |
| **Karyotype** | Detect **Additional Chromosomal Abnormalities (ACA)** – major route ACA, minor route ACA |
| **BCR::ABL1 Kinase Domain Sequencing** | If AP/BC, TKI failure, or suboptimal response |
| **Risk Scores** | **Sokal** (age, spleen, platelets, blasts), **Hasford** (adds eosinophils, basophils), **ELTS** (simplified: age, spleen, platelets) |

---

## 📊 Response Milestones (ELN 2020 / NCCN)

| Timepoint | Optimal Response | Warning | Failure |
|-----------|------------------|---------|---------|
| **3 months** | **BCR::ABL1 ≤10% (IS)** | >10% | No CHR, No CyR |
| **6 months** | **BCR::ABL1 <1% (CCyR)** | 1-10% (PCyR) | **No PCyR** (>10%) |
| **12 months** | **BCR::ABL1 ≤0.1% (MMR)** | >0.1% to 1% | **No MMR** (>1%) |
| **18 months** | **BCR::ABL1 ≤0.01% (MR4)** | 0.01-0.1% (MMR) | **No MMR** (>0.1%) |
| **≥24 months** | **MR4.5 (≤0.0032%)** for TFR consideration | | |

**Definitions:**
- **CHR**: Complete Haematological Response (normal CBC, no splenomegaly)
- **CyR**: Cytogenetic Response (CCyR = 0% Ph+; PCyR = 1-35%)
- **MMR**: Major Molecular Response (BCR::ABL1 ≤0.1% IS)
- **MR4**: BCR::ABL1 ≤0.01% IS
- **MR4.5**: BCR::ABL1 ≤0.0032% IS (DMR for TFR)

> [!tip] **FCPS/MRCP**: **3mo: ≤10%; 6mo: <1% (CCyR); 12mo: ≤0.1% (MMR)**. **MMR at 12mo = key milestone**. **Failure at any timepoint = switch TKI**.

---

## 💊 TKI Selection & Sequencing

### First-Line TKI Options

| TKI | Generation | Dose | Key Features | Preferred For |
|-----|------------|------|--------------|---------------|
| **Imatinib** | 1G | 400 mg OD | Gold standard, long safety data, cheap | Low risk (Sokal/ELTS), cost-sensitive, elderly |
| **Nilotinib** | 2G | 300 mg BD (fasting) | Deeper/faster response, **CV risk (QTc, PAD, hyperglycaemia)** | High risk, young patients desiring TFR |
| **Dasatinib** | 2G | 100 mg OD | **CNS penetration**, **pleural effusion risk**, rapid response | High risk, CNS disease, pulmonary HTN (caution) |
| **Bosutinib** | 2G | 400 mg OD (with food) | GI toxicity (diarrhoea), minimal CV/pleural, **no T315I activity** | Intolerance to other 2G TKIs |
| **Ponatinib** | 3G | 45 mg OD (↓ to 15mg after response) | **Only TKI for T315I**, pan-BCR::ABL1 inhibitor, **high CV/thrombotic risk** | **T315I mutation**, failure of 2G TKIs |

### TKI Selection Algorithm

```mermaid
flowchart TD
    A[Newly Diagnosed CP-CML] --> B{Risk Score (ELTS/Sokal)}
    B -->|Low| C[**Imatinib 400mg** or **Nilotinib/Dasatinib** if TFR goal]
    B -->|Intermediate/High| D[**2G TKI: Nilotinib or Dasatinib**]
    C & D --> E[Monitor BCR::ABL1 at 3, 6, 12, 18mo]
    E --> F{Response per ELN 2020?}
    F -->|Optimal| G[Continue same TKI]
    F -->|Warning| H[Optimise adherence, check mutations, consider switch]
    F -->|Failure| I[**Switch TKI**]
    I --> J[**Mutation Analysis**]
    J -->|T315I| K[**Ponatinib**]
    J -->|Other Mutation| L[Select TKI per mutation profile]
    J -->|No Mutation| M[Switch to **2G/3G TKI**]
```

### Mutation-Guided TKI Selection

| Mutation | Sensitive TKI | Resistant TKI |
|----------|---------------|---------------|
| **T315I** | **Ponatinib** | All others |
| **Y253H, E255K/V, F359V/C** | Nilotinib, Dasatinib, Bosutinib, Ponatinib | Imatinib |
| **F317L/V** | Nilotinib, Bosutinib, Ponatinib | Dasatinib |
| **V299L, T315A** | Dasatinib, Ponatinib | Nilotinib |
| **Compound Mutations** | **Ponatinib** | Usually all |

> [!warning] **T315I = Ponatinib ONLY**. **Ponatinib 45mg OD** (reduce to 15mg after response due to vascular toxicity).

---

## ⚠️ Key TKI Toxicities & Management

| TKI | Major Toxicities | Management |
|-----|------------------|------------|
| **Imatinib** | **Periorbital oedema**, fluid retention, muscle cramps, nausea, rash, cytopenias | Diuretics, calcium/magnesium, dose hold/reduction |
| **Nilotinib** | **QTc prolongation**, **peripheral arterial disease (PAD)**, hyperglycaemia, pancreatitis, lipase↑ | **ECG baseline/q3mo**, lipid/glucose control, avoid if CVD/PAD |
| **Dasatinib** | **Pleural effusion** (20-30%), pulmonary HTN (rare), cytopenias, bleeding | Diuretics, thoracentesis, dose reduce, hold if severe |
| **Bosutinib** | **Diarrhoea** (70%), hepatotoxicity, rash | Loperamide, dose with food, LFT monitoring |
| **Ponatinib** | **Arterial/venous thrombosis** (20-30%), heart failure, pancreatitis, hypertension | **CV risk assessment**, aspirin, aggressive risk factor control |

---

## 🌱 Treatment-Free Remission (TFR)

### Criteria for TFR Attempt (ELN/ENESTfreedom/STIM)

| Criterion | Requirement |
|-----------|-------------|
| **Deep Molecular Response (DMR)** | **MR4.5 (BCR::ABL1 ≤0.0032% IS) sustained ≥2 years** (some protocols ≥3 years) |
| **Prior TKI Duration** | ≥3 years on current TKI |
| **Monitoring Capacity** | **Monthly RT-qPCR for 6mo, then q3mo** (mandatory for early detection) |
| **Patient Factors** | Motivated, adherent, understands risk of molecular relapse (~40-50%) |

### TFR Relapse Management

| Scenario | Action |
|----------|--------|
| **Molecular Relapse** (Loss of MMR: BCR::ABL1 >0.1%) | **Restart SAME TKI** – regain MMR in >90% |
| **Loss of DMR but maintain MMR** | Increase monitoring frequency (monthly) |
| **Clinical Progression** | Restart TKI, assess mutations |

> [!tip] **FCPS/MRCP**: **TFR = MR4.5 sustained ≥2-3 years + monthly monitoring for 6mo**. **Relapse = restart same TKI**. **~50% remain TFR at 3 years**.

---

## 💥 Blast Crisis Management

| BC Type | Features | Induction | Consolidation |
|---------|----------|-----------|---------------|
| **Myeloid BC** (~70%) | Blasts MPO+, CD117+, CD34+ | **TKI (Dasatinib/Ponatinib) + "7+3" AML-type** | **Allo-HSCT in CR1** |
| **Lymphoid BC** (~20-30%) | Blasts TdT+, CD19+, CD10+ | **TKI (Dasatinib/Ponatinib) + ALL-type chemo** (Hyper-CVAD, UKALL) | **Allo-HSCT in CR1** |
| **Mixed/Undefined** | | TKI + intensive chemo per lineage | Allo-HSCT |

> [!warning] **Blast Crisis = Allo-HSCT mandatory if remission achieved**. **Dasatinib/Ponatinib preferred** (CNS penetration, potency). **Ponatinib if T315I**.

---

## 🤰 Pregnancy in CML

| Trimester | Recommendation |
|-----------|----------------|
| **Pre-conception** | **Switch to Interferon-α** (safe in pregnancy) OR stop TKI with close monitoring if DMR |
| **1st Trimester** | **Stop all TKIs** (teratogenic); **Interferon-α** if needed |
| **2nd/3rd Trimester** | Interferon-α safe; TKIs contraindicated |
| **Delivery** | Normal vaginal delivery preferred |
| **Breastfeeding** | **Contraindicated on TKIs** (excreted in milk); Interferon-α compatible |

> [!warning] **All TKIs teratogenic (Category D)**. **Imatinib: skeletal malformations**. **Stop TKI immediately on confirmed pregnancy**.

---

## 🔄 Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **Leukemoid Reaction** | **No Ph chromosome, no BCR::ABL1**, reactive maturation, **LAP score HIGH** (CML = LOW) |
| **Other MPNs (PV, ET, PMF)** | JAK2/CALR/MPL mutations, no BCR::ABL1, different clinical features |
| **aCML (Atypical CML)** | No BCR::ABL1, dysgranulopoiesis, SETBP1/ASXL1 mutations |
| **CNL (Chronic Neutrophilic Leukaemia)** | CSF3R mutation, no BCR::ABL1, mature neutrophilia |
| **Ph+ ALL** | **p190 isoform**, ≥20% lymphoblasts, TdT+ |

---

## 💡 FCPS/MRCP High-Yield Summary

| Topic | Key Point |
|-------|-----------|
| **Diagnosis** | **t(9;22) → BCR::ABL1 p210**; RT-qPCR (IS) quantitative |
| **Phases** | CP (<10% blasts), AP (10-19% blasts/basophilia≥20%/ACA), BC (≥20% blasts) |
| **Risk Scores** | **Sokal, Hasford, ELTS** (age, spleen, platelets, blasts ± basophils/eosinophils) |
| **First-line TKI** | Low risk: **Imatinib**; High risk: **Nilotinib/Dasatinib** (2G) |
| **Response Milestones (ELN 2020)** | **3mo: ≤10%; 6mo: <1% (CCyR); 12mo: ≤0.1% (MMR); 18mo: ≤0.01% (MR4)** |
| **Failure Definition** | **3mo: >10%; 6mo: >10%; 12mo: >0.1%; 18mo: >0.1%** → Switch TKI |
| **T315I Mutation** | **Ponatinib ONLY** |
| **TFR Criteria** | **MR4.5 (≤0.0032%) sustained ≥2-3 years** + monthly monitoring |
| **Blast Crisis** | **TKI (Dasatinib/Ponatinib) + AML/ALL-type chemo → Allo-HSCT CR1** |
| **Pregnancy** | **Stop TKI → Interferon-α** (all TKIs teratogenic) |
| **LAP Score** | **CML = LOW**; Leukemoid reaction = HIGH |

---

## ❓ Viva Questions

1. **What is the diagnostic genetic hallmark of CML?**
   - **t(9;22)(q34;q11) → BCR::ABL1 fusion (p210 isoform)**

2. **How do you diagnose CML and what is the gold standard for monitoring?**
   - CBC, film, BM, FISH/karyotype; **RT-qPCR BCR::ABL1 (International Scale) is gold standard for monitoring**

3. **What are the ELN 2020 response milestones at 3, 6, 12, 18 months?**
   - 3mo: ≤10%; 6mo: <1% (CCyR); 12mo: ≤0.1% (MMR); 18mo: ≤0.01% (MR4)

4. **When do you consider a TKI failure requiring switch?**
   - **3mo: >10%; 6mo: >10%; 12mo: >0.1%; 18mo: >0.1%** (Loss of MMR at any time)

5. **Which TKI is effective against T315I mutation?**
   - **Ponatinib** (3G TKI) – only TKI with activity against T315I

6. **What are the criteria for Treatment-Free Remission (TFR)?**
   - **MR4.5 (BCR::ABL1 ≤0.0032% IS) sustained ≥2-3 years** + monthly PCR monitoring for 6mo

7. **How is blast crisis managed?**
   - **Dasatinib/Ponatinib + intensive chemo (AML-type or ALL-type) → Allo-HSCT in CR1**

8. **What is the management of CML in pregnancy?**
   - **Stop TKI immediately** (teratogenic); switch to **Interferon-α** if treatment needed

9. **Differentiate CML from leukemoid reaction.**
   - **CML: Ph+, BCR::ABL1+, LAP LOW**; Leukemoid: **Ph-, BCR::ABL1-, LAP HIGH**

10. **What are the major toxicities of Nilotinib and Dasatinib?**
    - Nilotinib: **QTc prolongation, PAD, hyperglycaemia**; Dasatinib: **Pleural effusion, pulmonary HTN**

---

## 🧠 Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **CML vs Leukemoid Reaction** | CML: Ph+, BCR::ABL1+, **LAP LOW**; Leukemoid: **Ph-, LAP HIGH** |
| **Imatinib vs 2G TKI first-line** | Low risk (ELTS): Imatinib OK; High risk: **2G preferred for deeper/faster response** |
| **TFR vs Stopping TKI** | TFR = **structured attempt with criteria + monthly monitoring**; not just stopping |
| **T315I** | **Ponatinib ONLY** (gatekeeper mutation) |
| **MMR vs MR4.5** | MMR = ≤0.1% (milestone); MR4.5 = ≤0.0032% (TFR threshold) |
| **Accelerated Phase Criteria** | Blasts 10-19%, **Basophils ≥20%**, Platelets <100, **ACA** |

| Mnemonic | Meaning |
|----------|---------|
| **"CML = Ph+ = BCR-ABL"** | Diagnostic triad |
| **"3-6-12-18: 10, 1, 0.1, 0.01"** | ELN 2020 milestones |
| **"MMR = 0.1%, MR4.5 = 0.0032%"** | Molecular response thresholds |
| **"T315I = Pono (Ponatinib)"** | Gatekeeper mutation |
| **"TFR = MR4.5 × 2y + Monthly PCR"** | TFR criteria |
| **"LAP Low = CML; LAP High = Leukemoid"** | LAP score distinction |
| **"BC = TKI + Chemo → HSCT"** | Blast crisis algorithm |

---

## 🗺️ Mind Map

```mermaid
mindmap
  root((Chronic Myeloid Leukaemia))
    Genetics
      t(9;22) → BCR::ABL1 p210
      p190 = Ph+ ALL
    Phases
      CP: <10% blasts
      AP: 10-19% blasts, Baso≥20%, ACA
      BC: ≥20% blasts (Myeloid/Lymphoid)
    Diagnosis
      CBC, Film, BM
      RT-qPCR BCR::ABL1 (IS) - Gold Standard
      FISH, Karyotype (ACA)
    Risk Scores
      Sokal, Hasford, ELTS
    TKI Selection
      Low Risk: Imatinib
      High Risk: Nilotinib/Dasatinib
      T315I: Ponatinib
    Response Milestones (ELN 2020)
      3mo: ≤10%
      6mo: <1% (CCyR)
      12mo: ≤0.1% (MMR)
      18mo: ≤0.01% (MR4)
    Failure → Switch TKI + Mutation Analysis
    TFR
      MR4.5 (≥2-3y) + Monthly PCR
    Blast Crisis
      Dasatinib/Ponatinib + Chemo → HSCT
    Pregnancy
      Stop TKI → Interferon-α
```

---

## 📋 One-Page Revision Card

| **CML – FCPS/MRCP REVISION CARD** |
|-----------------------------------|
| **Genetics**: **t(9;22) → BCR::ABL1 p210** |
| **Phases**: CP (<10% blasts), AP (10-19% + baso≥20%/ACA), BC (≥20%) |
| **Gold Standard Monitoring**: **RT-qPCR BCR::ABL1 (IS)** |
| **Risk**: Sokal/Hasford/ELTS (age, spleen, plt, blasts ± baso/eos) |
| **1st Line TKI**: Low risk → **Imatinib**; High risk → **Nilotinib/Dasatinib** |
| **Milestones (ELN 2020)**: 3mo ≤10%; 6mo <1% (CCyR); 12mo ≤0.1% (MMR); 18mo ≤0.01% (MR4) |
| **Failure**: >10% (3/6mo), >0.1% (12/18mo) → **Switch TKI + Mutations** |
| **T315I**: **Ponatinib ONLY** |
| **TFR**: **MR4.5 (≤0.0032%) × ≥2-3y** + monthly PCR × 6mo |
| **Blast Crisis**: **Dasatinib/Ponatinib + AML/ALL chemo → Allo-HSCT CR1** |
| **Pregnancy**: **Stop TKI → Interferon-α** |
| **Toxicities**: Nilo=QTc/PAD; Dasat=Pleural effusion; Ponat=Thrombosis; Bosi=Diarrhoea |
| **LAP Score**: **CML = LOW**; Leukemoid = HIGH |

---

## 📅 Spaced Repetition Tracker

| Review | Date | Score (1-5) | Next Review |
|--------|------|-------------|-------------|
| Day 1 | 2025-06-15 | | 2025-06-16 |
| Day 3 | | | |
| Day 7 | | | |
| Day 15 | | | |
| Day 30 | | | |

---

## 🎯 Must Know / Should Know / Nice to Know

| Level | Content |
|-------|---------|
| **Must Know** | BCR::ABL1 p210, phases, RT-qPCR IS monitoring, ELN 2020 milestones, TKI selection by risk, failure definitions, T315I = Ponatinib, TFR criteria, blast crisis management, pregnancy: stop TKI → IFN-α, LAP score |
| **Should Know** | Detailed mutation profiles for 2G TKI selection, Sokal vs Hasford vs ELTS formulas, MR4.5 vs MMR vs MR4, nilotinib fasting requirement, dasatinib pleural effusion management, ponatinib vascular toxicity, interferon-α in pregnancy, ACA significance |
| **Nice to Know** | Specific kinase domain mutations and TKI sensitivity profiles, STIM/ENESTfreedom/EURO-SKI trial data for TFR, 4th generation TKIs (asciminib - ABL myristoyl pocket inhibitor), CML in children, cost-effectiveness analyses, discontinuation syndromes |

---

## ✅ Self-Test Scorecard

| Section | Score (0-10) | Notes |
|---------|--------------|-------|
| Diagnosis & Phases | | |
| Response Milestones (ELN 2020) | | |
| TKI Selection & Sequencing | | |
| Mutation Analysis (T315I) | | |
| TFR Criteria & Monitoring | | |
| Blast Crisis Management | | |
| Pregnancy Management | | |
| Toxicities & Toxicity Management | | |
| Viva Questions | | |

---

## 🔗 Local Navigation

- **Previous**: [[Acute Promyelocytic Leukaemia (APML)]]
- **Next**: [[Chronic Lymphocytic Leukaemia (CLL)]]
- **Section Hub**: [[Haematological Malignancies]]
- **MOC**: [[Hematology MOC]]
- **Template**: [[../Templates/Hematology Topic Template]]

---

*Generated for FCPS/MRCP exam preparation. Based on Davidson Medicine 24th Ed Chapter 25.*