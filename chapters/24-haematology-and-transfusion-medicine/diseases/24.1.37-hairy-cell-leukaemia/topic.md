---
tags: [medicine, davidson, hematology, hcl, hairy-cell-leukaemia, fcps, mrcp]
davidson_chapter: Chapter 25: Haematology and Transfusion Medicine
status: full-fcps-mrcp-note
priority: high
exam_relevance: "FCPS: Essential | MRCP: Core | BRAF V600E, TRAP+, CD25/CD103/CD123, splenomegaly, pancytopenia, cladribine/pentostatin, vemurafenib"
see_also: "[[CLL]], [[Splenic Marginal Zone Lymphoma]], [[Prolymphocytic Leukaemia]], [[Splenectomy]]"
created: 2025-06-16
modified: 2025-06-16
---

# Hairy Cell Leukaemia (HCL)

> [!info] **Davidson Ch 25 Alignment**: Haematological Malignancies → Hairy Cell Leukaemia
> **FCPS/MRCP Focus**: BRAF V600E, TRAP+, CD25/CD103/CD123/CD11c, massive splenomegaly, pancytopenia, dry tap, cladribine/pentostatin, vemurafenib (BRAF inhibition)

---

## 🎯 Learning Objectives

- [ ] Define HCL: **Mature B-cell neoplasm** with **hairy projections**, **splenomegaly**, **pancytopenia**, **dry tap**
- [ ] Diagnose: **BRAF V600E mutation** (>95%), **TRAP+**, **Immunophenotype: CD20+, CD25+, CD103+, CD123+, CD11c+, CD5-, CD10-, CD23-**
- [ ] Recognise **HCL-variant (HCL-v)**: **BRAF WT**, **MAP2K1 mutations**, **CD25-**, less responsive to purine analogues
- [ ] Manage **Treatment Indications**: Symptomatic cytopenias, massive splenomegaly, recurrent infections, constitutional symptoms
- [ ] First-line: **Cladribine (2-CdA)** or **Pentostatin** (purine analogues) – **High CR rates**
- [ ] Relapsed/Refractory: **Vemurafenib** (BRAF inhibitor), **Rituximab + Vemurafenib**, **Ibrutinib**, **Moxetumomab pasudotox** (anti-CD22 ADC)
- [ ] Manage **Splenectomy**: Historically curative; now reserved for purine analogue failure
- [ ] Monitor **Infections**: Encapsulated organisms (splenectomy/functional hyposplenism) – vaccinate, penicillin prophylaxis

---

## 📖 Definition & Diagnostic Criteria

| Feature | Classic HCL | HCL-Variant (HCL-v) |
|---------|-------------|---------------------|
| **BRAF V600E** | **>95% Positive** | **Negative (WT)** |
| **MAP2K1 Mutation** | Rare | **Common** |
| **CD25** | **Positive** | **Negative** |
| **CD103** | Positive | Positive |
| **CD123** | Positive | Variable |
| **TRAP (Tartrate-Resistant Acid Phosphatase)** | **Strongly Positive** | Weak/Negative |
| **Response to Purine Analogues** | **Excellent (CR >85%)** | **Poor/Lower** |

> [!tip] **FCPS/MRCP**: **HCL = BRAF V600E + TRAP+ + CD25+/CD103+/CD123+**. **HCL-v = BRAF WT, CD25-, MAP2K1 mut, purine analogue resistant**. **Cladribine/Pentostatin = First-line**. **Vemurafenib = BRAF inhibitor for relapsed**.

---

## ⚙️ Pathophysiology

```mermaid
flowchart TD
    A[BRAF V600E Mutation] --> B[Constitutive MAPK/ERK Pathway Activation]
    B --> C[Cell Survival & Proliferation]
    C --> D[Hairy Projections (CD103/Integrins)]
    D --> E[Splenic Red Pulp Infiltration]
    E --> F1[Massive Splenomegaly]
    E --> F2[Pancytopenia (Sequestration + Marrow Infiltration)]
    E --> F3[Dry Tap (Fibrosis/Infiltration)]
    C --> G[Impaired Immunoglobulin Production] --> H[Hypogammaglobulinaemia → Infections]
```

---

## 🔬 Diagnostic Workup

```mermaid
flowchart TD
    A[Pancytopenia + Massive Splenomegaly + Dry Tap] --> B[**CBC + Film**]
    B --> C{**Hairy Cells** (spindle-shaped projections)}
    C --> D[**Flow Cytometry Immunophenotype**]
    D --> E{**CD20+, CD25+, CD103+, CD123+, CD11c+, CD5-, CD10-, CD23-**}
    E -->|Yes| F[**BRAF V600E PCR/NGS** (>95%)]
    F -->|Positive| G[**Classic HCL**]
    F -->|Negative| H[**HCL-v: Check MAP2K1 Mut, CD25-**]
    G & H --> I[**BM Biopsy: Dry Tap, Reticulin Fibrosis, Hairy Cells in Red Pulp**]
    I --> J[**Staging: CBC, LDH, β2M, Ig Levels, Viscosity**]
```

### Key Investigations

| Test | Classic HCL Finding |
|------|---------------------|
| **Blood Film** | **"Hairy Cells"** – spindle-shaped cytoplasmic projections |
| **Flow Cytometry** | **CD20+, CD25+, CD103+, CD123+, CD11c+, CD5-, CD10-, CD23-, FMC7+** |
| **TRAP Stain** | **Strongly Positive** (histochemical) |
| **BRAF V600E** | **>95% Positive** (PCR/NGS) |
| **BM Aspirate** | **Dry Tap** (common due to fibrosis/infiltration) |
| **BM Biopsy** | **Reticulin Fibrosis**, Hairy cells in **Splenic Red Pulp** pattern |
| **CD25 (IL-2R)** | **Positive** (Classic); **Negative (HCL-v)** |

---

## 🩺 Clinical Features

| Feature | Details |
|---------|---------|
| **Splenomegaly** | **Massive** (often >20 cm), **Most common presentation** |
| **Pancytopenia** | Anaemia, Neutropenia, Thrombocytopenia (sequestration + marrow infiltration) |
| **Infections** | Recurrent (encapsulated organisms) – **Hypogammaglobulinaemia**, Neutropenia, Splenic dysfunction |
| **Fatigue** | Anaemia-related |
| **Constitutional** | Weight loss, night sweats (less common) |
| **Lymphadenopathy** | **Rare** (unlike CLL/FL) |

---

## 💊 Management

### Treatment Indications
- **Symptomatic cytopenias**: Hb <10, ANC <1.0, Plt <100
- **Massive splenomegaly** causing symptoms
- **Recurrent infections**
- **Constitutional symptoms**
- **Autoimmune complications** (AIHA, ITP)

### First-Line Therapy

| Agent | Regimen | CR Rate | Key Points |
|-------|---------|---------|------------|
| **Cladribine (2-CdA)** | **0.14 mg/kg/day IV × 5-7 days** (continuous infusion) OR **SC × 5 days** | **>85-90%** | **Single course**; **Profound immunosuppression** (CD4+ T-cell depletion); **Prophylaxis: ACV + PJP** |
| **Pentostatin** | **4 mg/m² IV q2wk × 3-6 months** | **>85-90%** | **Less myelotoxic**; **Renal toxicity**; **IV only** |

> [!tip] **Cladribine = Preferred** (shorter course, SC option, similar efficacy). **Both cause prolonged CD4+ lymphopenia** → **ACV + Co-trimoxazole prophylaxis for 12 months**.

### Relapsed/Refractory HCL

| Agent | Setting | Key Points |
|-------|---------|------------|
| **Vemurafenib** | **BRAF V600E+ Relapsed** | **BRAF Inhibitor**; 960 mg BD; **Rapid response**; **Skin toxicity** (cuSCC), **Arthralgia**; **Add Rituximab** for deeper remission |
| **Rituximab + Vemurafenib** | Relapsed | **Synergistic**; Deeper MRD-negative remissions |
| **Ibrutinib** | Relapsed/Refractory | **BTK Inhibitor**; Active in HCL & HCL-v; **AFib, bleeding** |
| **Moxetumomab Pasudotox** | Relapsed (≥2 prior) | **Anti-CD22 ADC**; **CR ~30-40%**; **Capillary leak syndrome**, **Haemolytic uraemic syndrome** |
| **Rituximab** | Relapsed (mild) | **375 mg/m² weekly × 4**; Lower CR rate alone |

### HCL-Variant (HCL-v) Management
- **Purine analogues LESS effective**
- **Rituximab + Vemurafenib** (if BRAF WT → vemurafenib not effective; consider **Ibrutinib**, **Rituximab + Ibrutinib**, **Moxetumomab**, Clinical trials)
- **MAP2K1 mutations** → **MEK inhibitors** (Trametinib) investigational

### Splenectomy
- **Historically** curative
- **Now**: Reserved for **Purine analogue failure** or **Massive splenomegaly with mechanical complications**
- **Vaccines + Penicillin prophylaxis post-splenectomy**

---

## 🔄 Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **HCL-variant** | **BRAF WT, CD25-, MAP2K1 mut**, **TRAP weak/neg**, **Purine analogue resistant** |
| **Splenic MZL (SMZL)** | **CD25-, CD103+/-**, **BRAF WT**, **IgM paraprotein** possible, **DBA44+** |
| **CLL** | **CD5+, CD23+, CD20 dim, sIg dim**, **No hairy projections**, **No massive splenomegaly** |
| **Prolymphocytic Leukaemia (B-PLL)** | **>55% Prolymphocytes**, **CD5-, CD23-**, **No hairy cells** |
| **HCL-v vs SMZL** | **HCL-v: CD103+ (usually), CD25-, MAP2K1**; **SMZL: CD103 variable, CD25-, DBA44+** |

---

## 💡 FCPS/MRCP High-Yield Summary

| Topic | Key Point |
|-------|-----------|
| **Diagnosis** | **BRAF V600E (>95%)**, **TRAP+**, **CD25+, CD103+, CD123+, CD11c+, CD5-, CD10-, CD23-** |
| **Clinical** | **Massive Splenomegaly**, **Pancytopenia**, **Dry Tap**, **Infections** |
| **HCL-v** | **BRAF WT, CD25-, MAP2K1 mut**, **TRAP weak**, **Purine analogue resistant** |
| **First-line** | **Cladribine (2-CdA) 0.14mg/kg × 5-7d** OR **Pentostatin 4mg/m² q2wk** |
| **CR Rate** | **>85-90%** with purine analogues |
| **Immunosuppression** | **Prolonged CD4+ depletion** → **ACV + PJP Prophylaxis × 12 months** |
| **Relapsed** | **Vemurafenib (BRAF inhibitor) + Rituximab**; **Ibrutinib**; **Moxetumomab** |
| **HCL-v** | **BRAF WT, CD25-, MAP2K1 mut** → **Purine analogue resistant** → **Ibrutinib/Vemurafenib+Rituximab** |
| **Splenectomy** | **Reserved for purine analogue failure** |
| **Infections** | **Encapsulated organisms** – Vaccinate, Penicillin prophylaxis post-splenectomy |

---

## ❓ Viva Questions

1. **What is the diagnostic immunophenotype of classic Hairy Cell Leukaemia?**
   - **CD20+, CD25+, CD103+, CD123+, CD11c+, CD5-, CD10-, CD23-, FMC7+**

2. **What is the BRAF V600E mutation frequency in HCL?**
   - **>95%** of classic HCL cases

3. **How does HCL-variant differ from classic HCL?**
   - **BRAF WT, CD25-, MAP2K1 mutation, TRAP weak/negative, Purine analogue resistant**

4. **What is the first-line treatment for classic HCL and what are the response rates?**
   - **Cladribine (2-CdA) 0.14 mg/kg/day × 5-7 days** or **Pentostatin 4mg/m² q2wk**; **CR >85-90%**

5. **What prophylactic measures are required after cladribine therapy?**
   - **Acyclovir + Co-trimoxazole (PCP) for 12 months** (prolonged CD4+ T-cell depletion)

6. **What is the role of Vemurafenib in relapsed HCL?**
   - **BRAF Inhibitor** (960mg BD) for **BRAF V600E+ relapsed**; **Combined with Rituximab for deeper remission**; **Skin squamous cell carcinoma risk**

7. **How is HCL-variant managed differently from classic HCL?**
   - **Purine analogues ineffective**; **BRAF WT → Vemurafenib ineffective**; Use **Ibrutinib, Rituximab + Vemurafenib (if MAP2K1), Moxetumomab**, Clinical trials

8. **What is the significance of a "dry tap" on bone marrow aspiration in HCL?**
   - **Fibrosis/Infiltration of marrow by hairy cells** – common in HCL; **Biopsy required**

9. **What is the immunophenotype difference between HCL and CLL?**
   - **HCL: CD25+, CD103+, CD123+, CD5-, CD23-**; **CLL: CD5+, CD23+, CD20 dim, sIg dim, CD25-, CD103-**

10. **What vaccines are required pre-splenectomy in HCL?**
    - **PCV13, PPSV23 (2mo later), MenACWY, Hib, Hep B, Annual Flu, COVID**

---

## 🧠 Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **HCL vs HCL-v** | **HCL = BRAF V600E+, CD25+, TRAP+**; **HCL-v = BRAF WT, CD25-, MAP2K1, TRAP-** |
| **HCL vs SMZL** | **HCL = CD25+, CD103+, BRAF V600E**; **SMZL = CD25-, DBA44+, BRAF WT** |
| **HCL vs CLL** | **HCL = CD25+, CD103+, CD123+, CD5-, CD23-**; **CLL = CD5+, CD23+, CD20dim, sIg dim** |
| **Cladribine vs Pentostatin** | **Cladribine = Shorter course (5-7d), SC option**; **Pentostatin = Longer (3-6mo), IV only, Renal toxicity** |
| **Vemurafenib** | **Only for BRAF V600E+**; **Combined with Rituximab**; **Skin cancer risk** |

| Mnemonic | Meaning |
|----------|---------|
| **"HCL = Hairy = CD25, CD103, CD123, CD11c"** | Immunophenotype |
| **"BRAF V600E = Classic HCL (95%)"** | Mutation |
| **"Dry Tap = Fibrosis/Infiltration"** | BM finding |
| **"Cladribine = 5-7 Days = CR 90%"** | First-line |
| **"ACV + PJP Prophylaxis × 12mo"** | Post-cladribine |
| **"Vemurafenib = BRAF Inhibitor = Relapsed HCL"** | Relapse treatment |
| **"HCL-v = BRAF WT + CD25- + MAP2K1"** | Variant |

---

## 🗺️ Mind Map

```mermaid
mindmap
  root((Hairy Cell Leukaemia))
    Classic HCL
      BRAF V600E (>95%)
      TRAP Strongly Positive
      CD25+, CD103+, CD123+, CD11c+
      CD5-, CD10-, CD23-
    HCL-Variant
      BRAF WT
      CD25-
      MAP2K1 Mutation
      TRAP Weak/Negative
      Purine Analogue Resistant
    Clinical
      Massive Splenomegaly
      Pancytopenia
      Dry Tap
      Infections (Hyposplenism, Hypogammaglobulinaemia)
    First-Line
      Cladribine (2-CdA) 0.14mg/kg × 5-7d
      Pentostatin 4mg/m² q2wk
      CR >85-90%
    Relapsed
      Vemurafenib (BRAF Inhibitor) + Rituximab
      Ibrutinib
      Moxetumomab Pasudotox
      HCL-v: Ibrutinib, Clinical Trials
    Complications
      Infections (Encapsulated)
      Secondary Malignancies
      Richter Transformation (Rare)
```

---

## 📋 One-Page Revision Card

| **HAIRY CELL LEUKAEMIA – FCPS/MRCP REVISION CARD** |
|-----------------------------------------------------|
| **Diagnosis**: **BRAF V600E (>95%), TRAP+, CD25+/CD103+/CD123+/CD11c+, CD5-/CD10-/CD23-** |
| **Clinical**: **Massive Splenomegaly, Pancytopenia, Dry Tap, Infections** |
| **HCL-v**: **BRAF WT, CD25-, MAP2K1 mut, TRAP-, Purine Analogue Resistant** |
| **First-Line**: **Cladribine 0.14mg/kg × 5-7d** or **Pentostatin 4mg/m² q2wk** |
| **CR Rate**: **>85-90%** |
| **Post-Cladribine**: **ACV + Co-trimoxazole × 12mo** (CD4 depletion) |
| **Relapsed**: **Vemurafenib (BRAFi) + Rituximab**, **Ibrutinib**, **Moxetumomab** |
| **HCL-v Rx**: **Ibrutinib, Vemurafenib+Rituximab (if MAP2K1), Clinical Trials** |
| **Splenectomy**: **Failure of purine analogues only** |
| **Vaccines Post-Splenectomy**: PCV13, PPSV23, MenACWY, Hib |

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
| **Must Know** | Immunophenotype (CD25/103/123), BRAF V600E >95%, TRAP+, massive splenomegaly, pancytopenia, dry tap, cladribine/pentostatin first-line, CR >85%, post-cladribine prophylaxis (ACV+PJP), vemurafenib for relapsed, HCL-v = BRAF WT/CD25-/MAP2K1, HCL-v resistant to purine analogues |
| **Should Know** | Cladribine vs pentostatin details, rituximab + vemurafenib synergy, moxetumomab pasudotox (anti-CD22 ADC), ibrutinib in HCL-v, splenectomy indications, BRAF inhibitor skin toxicity (cuSCC), MEK inhibitors for MAP2K1, minimal residual disease monitoring, familial HCL, HCL in paediatrics |
| **Nice to Know** | BRAF V600E structural biology, MAPK pathway in HCL, TRAP biochemistry (tartrate resistance), CD25/IL-2R biology, cladribine pharmacokinetics (intracellular triphosphate), pentostatin adenosine deaminase inhibition, vemurafenib resistance mechanisms (NRAS, MEK), anti-CD22 ADC mechanism, HCL-v MAP2K1 clonal architecture, cost-effectiveness, quality of life |

---

## ✅ Self-Test Scorecard

| Section | Score (0-10) | Notes |
|---------|--------------|-------|
| Diagnosis & Immunophenotype | | |
| Classic vs Variant HCL | | |
| First-Line Treatment (Cladribine/Pentostatin) | | |
| Relapsed Management | | |
| HCL-v Management | | |
| Infections & Prophylaxis | | |
| Viva Questions | | |

---

## 🔗 Local Navigation

- **Previous**: [[Waldenström Macroglobulinaemia]]
- **Next**: [[Prolymphocytic Leukaemia]]
- **Section Hub**: [[Haematological Malignancies]]
- **MOC**: [[Hematology MOC]]
- **Template**: [[../Templates/Hematology Topic Template]]

---

*Generated for FCPS/MRCP exam preparation. Based on Davidson Medicine 24th Ed Chapter 25.*
---

> Auto-generated study sections for "Hematology" — Ch 24: Haematology & Transfusion Medicine.

## Flashcards (24 generated)

- Q: What is the definition of Hematology?
  A: [!info] Davidson Ch 25 Alignment: Haematological Malignancies → Hairy Cell Leukaemia
- Q: What is Blood Film of Hematology?
  A: "Hairy Cells" – spindle-shaped cytoplasmic projections
- Q: What is Flow Cytometry of Hematology?
  A: CD20+, CD25+, CD103+, CD123+, CD11c+, CD5-, CD10-, CD23-, FMC7+
- Q: What is TRAP Stain of Hematology?
  A: Strongly Positive (histochemical)
- Q: What is BRAF V600E of Hematology?
  A: >95% Positive (PCR/NGS)
- Q: What is BM Aspirate of Hematology?
  A: Dry Tap (common due to fibrosis/infiltration)
- Q: What is BM Biopsy of Hematology?
  A: Reticulin Fibrosis, Hairy cells in Splenic Red Pulp pattern
- Q: What is CD25 (IL-2R) of Hematology?
  A: Positive (Classic); Negative (HCL-v)
- Q: What is Blood Film of Hematology?
  A: "Hairy Cells" – spindle-shaped cytoplasmic projections
- Q: What is Flow Cytometry of Hematology?
  A: CD20+, CD25+, CD103+, CD123+, CD11c+, CD5-, CD10-, CD23-, FMC7+
- Q: What is TRAP Stain of Hematology?
  A: Strongly Positive (histochemical)
- Q: What is BRAF V600E of Hematology?
  A: >95% Positive (PCR/NGS)
- Q: What is BM Aspirate of Hematology?
  A: Dry Tap (common due to fibrosis/infiltration)
- Q: What is BM Biopsy of Hematology?
  A: Reticulin Fibrosis, Hairy cells in Splenic Red Pulp pattern
- Q: What is CD25 (IL-2R) of Hematology?
  A: Positive (Classic); Negative (HCL-v)
- Q: What is the investigation of choice for Hematology?
  A: BRAF V600E (>95%), TRAP+, CD25+, CD103+, CD123+, CD11c+, CD5-, CD10-, CD23-
- Q: What is Clinical of Hematology?
  A: Massive Splenomegaly, Pancytopenia, Dry Tap, Infections
- Q: What is HCL-v of Hematology?
  A: BRAF WT, CD25-, MAP2K1 mut, TRAP weak, Purine analogue resistant
- Q: What is the first-line treatment for Hematology?
  A: Cladribine (2-CdA) 0.14mg/kg × 5-7d OR Pentostatin 4mg/m² q2wk
- Q: What is CR Rate of Hematology?
  A: >85-90% with purine analogues
- Q: What is Immunosuppression of Hematology?
  A: Prolonged CD4+ depletion → ACV + PJP Prophylaxis × 12 months
- Q: What is Relapsed of Hematology?
  A: Vemurafenib (BRAF inhibitor) + Rituximab; Ibrutinib; Moxetumomab
- Q: What is Splenectomy of Hematology?
  A: Reserved for purine analogue failure
- Q: What is Infections of Hematology?
  A: Encapsulated organisms – Vaccinate, Penicillin prophylaxis post-splenectomy

## MCQs (1 generated)

1. **Which of the following best describes Hematology?**
   A. **[!info] Davidson Ch 25 Alignment: Haematological Malignancies → Hairy Cell Leukaemia**
   B. An unrelated condition not matching the clinical picture of Hematology
   C. A complication seen late in the disease course of Hematology
   D. A condition that mimics Hematology but has a different underlying cause

## SBA Questions (1 generated)

1. A patient with suspected Hematology presents with: Feature — Classic HCL; BRAF V600E — >95% Positive; MAP2K1 Mutation — Rare. What is the most likely diagnosis?
   A. **Hematology**
   B. A condition that mimics Hematology but is not the same entity
   C. A complication of Hematology rather than the primary diagnosis
   D. An unrelated condition in the same clinical category as Hematology

## PasTest Scenario SBAs (Clinical Vignettes)

> **Auto-generated PasTest/Mediscope-style scenario SBAs** grounded in the authored source. Each scenario tests a real clinical fact (triad, specific sign, contraindication, trial, first-line Rx) extracted from the topic. *Source: Ch 24: Haematology — Hairy Cell Leukaemia*

**Q1.** What is the most appropriate first-line therapy for Hairy Cell Leukaemia?

  - **A.** Symptomatic cytopenias + Massive splenomegaly + Recurrent infections
  - **B.** An advanced/surgical therapy reserved for refractory disease
  - **C.** Symptomatic treatment only, no disease-modifying therapy
  - **D.** Empiric broad-spectrum therapy without specific indication

  > **Answer: A** — Symptomatic cytopenias + Massive splenomegaly + Recurrent infections
  >
  > *Source:* ### Treatment Indications
- **Symptomatic cytopenias**: Hb <10, ANC <1.0, Plt <100
- **Massive splenomegaly** causing symptoms
- **Recurrent infections**
- **Constitutional symptoms**
- **Autoimmune c

