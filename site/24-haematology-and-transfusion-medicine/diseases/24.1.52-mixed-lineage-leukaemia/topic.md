---
tags: [medicine, davidson, hematology, mixed-lineage-leukaemia, mll, fcps, mrcp]
davidson_chapter: Chapter 25: Haematology and Transfusion Medicine
status: full-fcps-mrcp-note
priority: high
exam_relevance: "FCPS: High-yield | MRCP: Core | KMT2A (MLL) rearrangements, infant ALL/AML, poor prognosis, KMT2A-r classification, therapy (FLT3 inhibitors, menin inhibitors)"
see_also: "[[Acute Myeloid Leukaemia (AML)]], [[Acute Lymphoblastic Leukaemia (ALL)]], [[Acute Promyelocytic Leukaemia (APML)]]"
created: 2025-06-17
modified: 2025-06-17
---

# Mixed Lineage Leukaemia (MLL)

> [!info] **Davidson Ch 25 Alignment**: Haematological Malignancies → Acute Leukaemias → Mixed Lineage Leukaemia
> **FCPS/MRCP Focus**: KMT2A (MLL) rearrangements, 11q23 abnormalities, infant leukaemia, biphenotypic features, poor prognosis, KMT2A-r classification, emerging therapies

---

## 🎯 Learning Objectives

- [ ] Define **Mixed Lineage Leukaemia (MLL)**: Acute leukaemia with **KMT2A (MLL) gene rearrangement** at **11q23**, showing **biphenotypic** (myeloid + lymphoid) features
- [ ] Classify per **WHO/ICC**: **Acute leukaemia with KMT2A rearrangement** (regardless of lineage)
- [ ] Identify **Epidemiology**: **Infants** (<1 year) ~70-80% of infant ALL/AML; **Secondary** post-topoisomerase II inhibitors
- [ ] Diagnose: **KMT2A rearrangement** (FISH/PCR/NGS), **Immunophenotype**: **Biphenotypic** (CD19, CD10, CD33, CD13, CD117, MPO)
- [ ] Apply **Prognosis**: **High-risk** in infants; **Intermediate** in adults; **ELN 2022: Adverse** if KMT2A-r
- [ ] Manage: **Intensive chemotherapy** (ALL-type or AML-type per dominant lineage), **FLT3 inhibitors** (if FLT3mut), **Menin inhibitors** (emerging), **HSCT in CR1**
- [ ] Differentiate from: **B-ALL, AML, MPAL, BPDCN**

---

## 📖 Definition & Classification

| Feature | Details |
|---------|---------|
| **Defining Genetic Abnormality** | **KMT2A (MLL) rearrangement at 11q23** |
| **Partner Genes** | **>100 partners**; Common: **AF4 (AFF1), AF9 (MLLT3), ENL (MLLT1), AF10 (MLLT10), ELL, AF6, SEPTIN6** |
| **WHO/ICC Classification** | **Acute leukaemia with KMT2A rearrangement** (Myeloid, Lymphoid, or Mixed phenotype) |
| **Lineage** | **Biphenotypic** (co-expression of myeloid + lymphoid markers) |

| WHO Category | Description |
|--------------|-------------|
| **B-ALL with KMT2A-r** | CD19+, CD10+, CD33+, CD13+, MPO- |
| **AML with KMT2A-r** | MPO+, CD13+, CD33+, CD19+/CD10+ |
| **Mixed Phenotype Acute Leukaemia (MPAL) with KMT2A-r** | **Both myeloid (MPO) AND lymphoid (CD19/CD22/cCD79a) criteria met** |

> [!tip] **FCPS/MRCP**: **KMT2A-r = Defining genetic abnormality = AML diagnosis regardless of blast %**. **Infants <1yr = >70% of infant ALL/AML**. **MPO+ = Myeloid; CD19+CD10+ = Lymphoid; Both = MPAL**.

---

## ⚙️ Pathophysiology

```mermaid
flowchart TD
    A[KMT2A (MLL) Gene at 11q23] --> B[Chromosomal Translocation]
    B --> C[KMT2A::Partner Fusion Protein]
    C --> D[Loss of Normal KMT2A Function (H3K4 Methylation)]
    C --> E[Gain of Aberrant Transcriptional Activation]
    D & E --> F[Dysregulation of HOX Genes]
    F --> G[Block in Differentiation + Self-Renewal]
    G --> H[Leukaemic Stem Cell Expansion]
    H --> I[Biphenotypic Leukaemia]
```

| Normal KMT2A | KMT2A::Partner Fusion |
|--------------|----------------------|
| Histone methyltransferase (H3K4) | Loss of H3K4 methylation |
| Regulates HOX genes | Constitutive HOX activation |
| Tumour suppressor | Oncogenic fusion |

---

## 🔬 Diagnostic Workup

```mermaid
flowchart TD
    A[Infant/Young Adult: Leukaemia with Biphenotypic Features] --> B[**CBC + Film: Blasts**]
    B --> C[**Flow Cytometry**]
    C --> D{**Biphenotypic: Myeloid + Lymphoid Markers**}
    D -->|Yes| E[**KMT2A FISH/PCR/NGS**]
    E --> F{**KMT2A Rearrangement?**}
    F -->|Yes| G[**MLL / KMT2A-r Diagnosis**]
    F -->|No| H[Consider Other MPAL / B-ALL / AML]
    G --> I[**Partner Gene Identification** (AF4, AF9, ENL, etc.)]
    I --> J[**Risk Stratification & Treatment Selection**]
```

### Essential Investigations

| Test | Finding in KMT2A-r |
|------|-------------------|
| **Flow Cytometry** | **Biphenotypic**: **CD19+, CD10+** (B-lymphoid) + **CD13+, CD33+, CD117+, MPO+** (Myeloid) |
| **KMT2A FISH** | **Positive** (Break-apart probe) |
| **KMT2A PCR/NGS** | **Partner gene identified** (AF4, AF9, ENL, AF10, ELL, etc.) |
| **Cytogenetics** | **t(4;11), t(9;11), t(11;19), t(10;11), etc.** |
| **Cytochemistry** | **MPO+** (Myeloid), **TdT+** (Lymphoid) - may be both |
| **Cytogenetics** | **Complex karyotype** often associated |

### Key Immunophenotype

| Marker | Myeloid | Lymphoid |
|--------|---------|----------|
| **CD13** | + | - |
| **CD33** | + | - |
| **CD117** | + | - |
| **MPO** | + | - |
| **CD19** | - | + |
| **CD10** | - | + |
| **CD22** | - | + |
| **cCD79a** | - | + |
| **TdT** | - | + |

---

## 🩺 Clinical Features

| Feature | Infant KMT2A-r (<1 yr) | Adult KMT2A-r |
|---------|----------------------|---------------|
| **Age** | **<1 year** (70-80% of infant ALL/AML) | Adults (20-30% of AML with KMT2A-r) |
| **Presentation** | High WBC, Hepatosplenomegaly, Skin infiltrates, CNS involvement | Similar to de novo AML/ALL |
| **CNS Involvement** | **High** (15-25%) | Variable |
| **Skin Infiltration** | Common | Less common |
| **Coagulopathy** | DIC-like (especially t(9;11)) | Variable |

---

## 📊 Prognosis & Risk Stratification

| Factor | Impact |
|--------|--------|
| **Age <1 year** | **Poor prognosis** (but some protocols improved) |
| **KMT2A-r Partner** | **t(4;11)/AF4 = Worst**; **t(9;11) = Intermediate**; **t(11;19)/ELL = Better** |
| **WBC >300×10⁹/L** | **Poor** (leukostasis risk) |
| **CNS Involvement** | **Adverse** |
| **MPAL vs Pure Lineage** | **MPAL = Intermediate** |

> [!tip] **ELN 2022: KMT2A-r = Adverse Risk** (regardless of lineage). **t(4;11) = Worst partner gene**.

---

## 💊 Management

### Treatment by Lineage Dominance

| Dominant Lineage | Regimen |
|------------------|---------|
| **Lymphoid-dominant (B-ALL type)** | **ALL-type protocol** (UKALL, COG, AIEOP): Vincristine, Prednisolone, Daunorubicin, L-Asparaginase, Cyclophosphamide, Cytarabine, Methotrexate, 6-MP |
| **Myeloid-dominant (AML type)** | **AML-type protocol** (7+3: Cytarabine + Anthracycline) ± Midostaurin (if FLT3mut) |
| **MPAL (True biphenotypic)** | **ALL-type backbone** + **Anthracycline** + **Cytarabine** (Hybrid); **HSCT in CR1** |

### Infant Protocols (KMT2A-r <1 yr)

| Protocol | Key Features |
|----------|--------------|
| **Interfant-06 / Interfant-10** | **ALL-type backbone** + **High-dose Cytarabine** + **Etoposide** + **HSCT in CR1** |
| **Risk Stratification** | **Age <6mo, WBC >300, t(4;11) = Highest risk** → **HSCT in CR1** |
| **Outcomes** | **5-yr OS ~40-50%** (improved from historical <20%) |

### Emerging Targeted Therapies

| Target | Agent | Status |
|--------|-------|--------|
| **Menin-MLL Interaction** | **Menin Inhibitors** (Revumenib, Ziftomenib) | **Phase 1/2: Promising CR rates** |
| **FLT3** | **Midostaurin, Gilteritinib** | **If FLT3mut co-occurring** |
| **DOT1L** | **Pinometostat** | **Early phase** |
| **BCL-2** | **Venetoclax** | **Combination trials** |

---

## 🔄 Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **B-ALL** | **CD19+, CD10+, CD34+, TdT+, MPO-**; No KMT2A-r |
| **AML** | **MPO+, CD13+, CD33+, CD117+**; No lymphoid markers |
| **MPAL (B/Myeloid)** | **Both lineages ≥20% blasts each**; **KMT2A-r common** |
| **BPDCN (Blastic Plasmacytoid DC Neoplasm)** | **CD123+, CD56+, CD4+, CD303+, TCL1+**; MPO-, CD19- |
| **ETP-ALL (Early T-cell Precursor ALL)** | **CD7+, CD2+, CD5+, CD1a-, CD8-, CD117+, TdT+** |
| **t-AML with KMT2A-r** | **Post-topoisomerase II inhibitor** (Etoposide, Anthracycline) latency 1-3y |

---

## 💡 FCPS/MRCP High-Yield Summary

| Topic | Key Point |
|-------|-----------|
| **Defining Feature** | **KMT2A (MLL) rearrangement at 11q23** |
| **Common Partners** | **AF4 (t(4;11)), AF9 (t(9;11)), ENL (t(11;19)), AF10 (t(10;11)), ELL** |
| **Epidemiology** | **Infants <1yr: 70-80% of infant ALL/AML**; **Secondary post-topo II inhibitors** |
| **Immunophenotype** | **Biphenotypic**: **CD19+/CD10+ + CD13+/CD33+/MPO+** |
| **Lineage** | **MPAL (mixed phenotype) common**; Can be B-ALL type or AML type |
| **Prognosis** | **Infants = Poor**; **t(4;11) = Worst partner**; **Adults = Adverse (ELN 2022)** |
| **Treatment** | **Lineage-directed**: ALL-type vs AML-type backbone; **HSCT in CR1** |
| **Emerging** | **Menin inhibitors** (Revumenib) - **Target Menin-MLL interaction** |
| **ELN 2022** | **KMT2A-r = Adverse risk** (regardless of blast % or lineage) |

---

## ❓ Viva Questions

1. **What is the defining genetic abnormality in Mixed Lineage Leukaemia?**
   - **KMT2A (MLL) rearrangement at 11q23** (translocation with partner genes like AF4, AF9, ENL)

2. **What is the typical immunophenotype of KMT2A-rearranged leukaemia?**
   - **Biphenotypic**: **CD19+, CD10+ (B-lymphoid)** + **CD13+, CD33+, CD117+, MPO+ (Myeloid)**

3. **Which age group has the highest incidence of KMT2A-rearranged leukaemia?**
   - **Infants <1 year** (70-80% of infant ALL/AML have KMT2A rearrangement)

4. **What are the common KMT2A partner genes and their translocations?**
   - **AF4/AFF1: t(4;11)**; **AF9/MLLT3: t(9;11)**; **ENL/MLLT1: t(11;19)**; **AF10/MLLT10: t(10;11)**; **ELL: t(11;19)**

5. **Which KMT2A partner gene carries the worst prognosis?**
   - **AF4/AFF1 (t(4;11))** = **Worst prognosis**; **t(9;11) = Intermediate**; **t(11;19)/ELL = Better**

6. **How does ELN 2022 classify KMT2A-rearranged AML?**
   - **Adverse risk** (regardless of blast percentage or lineage)

7. **What is the treatment approach for KMT2A-rearranged leukaemia?**
   - **Lineage-directed**: **ALL-type protocol** (Lymphoid-dominant) OR **AML-type (7+3)** (Myeloid-dominant); **HSCT in CR1** for high-risk

8. **What are the emerging targeted therapies for KMT2A-r leukaemia?**
   - **Menin inhibitors** (Revumenib, Ziftomenib) - disrupt Menin-MLL interaction; **DOT1L inhibitors**; **FLT3 inhibitors** if co-mutated

9. **How does KMT2A-r leukaemia differ from MPAL without KMT2A-r?**
   - **KMT2A-r = Defining genetic lesion**; **MPAL without KMT2A = Diagnosis by immunophenotype only**; **KMT2A-r has specific biology (HOX dysregulation)**

10. **What is the significance of t(9;11) in KMT2A-r leukaemia?**
    - **Most common KMT2A translocation** (~50%); **Associated with myelomonocytic features, DIC-like coagulopathy; Intermediate prognosis**

---

## 🧠 Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **KMT2A vs MLL** | **Same gene**; **MLL = Mixed Lineage Leukaemia (old name)**; **KMT2A = Lysine Methyltransferase 2A (current name)** |
| **KMT2A-r vs MPAL** | **KMT2A-r = Specific genetic subtype**; **MPAL = Immunophenotypic category**; KMT2A-r often presents as MPAL |
| **t(4;11) vs t(9;11)** | **t(4;11) = AF4, Worst prognosis**; **t(9;11) = AF9, DIC-like, Intermediate** |
| **Infant vs Adult KMT2A-r** | **Infant = <1yr, B-ALL type dominant, Worse**; **Adult = AML type dominant, Adverse (ELN 2022)** |
| **KMT2A-r vs B-ALL** | **KMT2A-r = Biphenotypic (Myeloid+Lymphoid markers)**; **B-ALL = Pure lymphoid** |

| Mnemonic | Meaning |
|----------|---------|
| **"KMT2A = 11q23 = MLL"** | Gene location |
| **"t(4;11) = AF4 = Worst"** | Partner gene prognosis |
| **"Biphenotypic = CD19+CD10+ + CD13+CD33+MPO+"** | Immunophenotype |
| **"Infants <1yr = 70-80% KMT2A-r"** | Age distribution |
| **"Menin Inhibitors = Target Menin-MLL"** | Emerging therapy |

---

## 🗺️ Mind Map

```mermaid
mindmap
  root((Mixed Lineage Leukaemia))
    Genetics
      KMT2A (MLL) at 11q23
      Partners: AF4, AF9, ENL, AF10, ELL
      t(4;11), t(9;11), t(11;19), t(10;11)
    Epidemiology
      Infants <1yr: 70-80%
      Post-Topo II Inhibitors
    Immunophenotype
      Biphenotypic
      B-lineage: CD19, CD10, CD22
      Myeloid: CD13, CD33, CD117, MPO
    Classification
      B-ALL with KMT2A-r
      AML with KMT2A-r
      MPAL with KMT2A-r
    Prognosis
      t(4;11) = Worst
      t(9;11) = Intermediate + DIC
      ELN 2022: Adverse
    Treatment
      Lineage-directed (ALL vs AML)
      Interfant Protocol (Infants)
      HSCT in CR1 (High Risk)
    Emerging
      Menin Inhibitors (Revumenib)
      DOT1L Inhibitors
```

---

## 📋 One-Page Revision Card

| **MIXED LINEAGE LEUKAEMIA (KMT2A-r) – FCPS/MRCP REVISION CARD** |
|------------------------------------------------------------------|
| **Definition**: **KMT2A (MLL) rearrangement at 11q23** |
| **Partners**: **AF4 (t(4;11) - Worst)**, AF9 (t(9;11) - DIC-like), ENL, AF10, ELL |
| **Epidemiology**: **Infants <1yr = 70-80% of infant ALL/AML** |
| **Immunophenotype**: **Biphenotypic** = **CD19+/CD10+ + CD13+/CD33+/MPO+** |
| **Classification**: B-ALL with KMT2A-r / AML with KMT2A-r / MPAL with KMT2A-r |
| **Prognosis**: **Infants poor, t(4;11) worst, ELN 2022 = Adverse** |
| **Treatment**: **Lineage-directed** (ALL-type vs AML-type); **HSCT in CR1** (High risk) |
| **Emerging**: **Menin Inhibitors** (Revumenib) - Target Menin-MLL interaction |
| **ELN 2022**: **KMT2A-r = Adverse Risk** (regardless of lineage) |

---

## 📅 Spaced Repetition Tracker

| Review | Date | Score (1-5) | Next Review |
|--------|------|-------------|-------------|
| Day 1 | 2025-06-17 | | 2025-06-18 |
| Day 3 | | | |
| Day 7 | | | |
| Day 15 | | | |
| Day 30 | | | |

---

## 🎯 Must Know / Should Know / Nice to Know

| Level | Content |
|-------|---------|
| **Must Know** | KMT2A/MLL at 11q23, Partner genes (AF4, AF9, ENL), Infant incidence, Biphenotypic immunophenotype, Lineage classification, t(4;11) worst prognosis, ELN 2022 adverse risk, HSCT in CR1, Menin inhibitors emerging |
| **Should Know** | Interfant protocol details, Partner gene specific features (t(9;11) DIC, t(11;19) better), MPAL vs KMT2A-r distinction, t-AML with KMT2A-r (topo II inhibitors), Menin inhibitor trials, DOT1L inhibitors, FLT3 co-mutation, CNS prophylaxis importance |
| **Nice to Know** | KMT2A normal function (H3K4 methylation, HOX regulation), Leukaemic stem cell biology in KMT2A-r, Specific partner gene fusion transcripts, KMT2A-r in therapy-related AML, Epigenetic dysregulation, CAR-T in KMT2A-r, Venous vs arterial thrombosis risk, Quality of life in infant leukaemia survivors, Global incidence variations |

---

## ✅ Self-Test Scorecard

| Section | Score (0-10) | Notes |
|---------|--------------|-------|
| Genetics & Partner Genes | | |
| Immunophenotype | | |
| Classification (WHO/ICC) | | |
| Prognosis & Risk Stratification | | |
| Treatment by Lineage | | |
| Emerging Therapies | | |
| Viva Questions | | |

---

## 🔗 Local Navigation

- **Previous**: [[Hyperhomocysteinaemia]]
- **Next**: [[Plasmacytoma]]
- **Section Hub**: [[Haematological Malignancies]]
- **MOC**: [[Hematology MOC]]
- **Template**: [[../Templates/Hematology Topic Template]]

---

*Generated for FCPS/MRCP exam preparation. Based on Davidson Medicine 24th Ed Chapter 25.*