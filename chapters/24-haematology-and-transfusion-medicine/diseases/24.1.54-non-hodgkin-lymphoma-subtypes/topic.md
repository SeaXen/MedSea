---
tags: [medicine, davidson, hematology, lymphoma, nhl, fcps, mrcp]
davidson_chapter: Chapter 25: Haematology and Transfusion Medicine
status: full-fcps-mrcp-note
priority: high
exam_relevance: "FCPS: Essential | MRCP: Core | High-yield for vivas, DLBCL/FL/MCL/MZL/Burkitt, R-CHOP, R-Benda, CAR-T"
see_also: "[[Hodgkin Lymphoma]], [[CLL]], [[Mantle Cell Lymphoma]], [[Follicular Lymphoma]], [[Diffuse Large B-cell Lymphoma]], [[Burkitt Lymphoma]]"
created: 2025-06-15
modified: 2025-06-15
---

# Non-Hodgkin Lymphoma (NHL) Subtypes

> [!info] **Davidson Ch 25 Alignment**: Haematological Malignancies → Lymphomas → Non-Hodgkin Lymphoma
> **FCPS/MRCP Focus**: WHO classification, DLBCL/FL/MCL/MZL/Burkitt, IPI/FLIPI/MANTLE-IPI, R-CHOP/R-Benda/R-CVP, CAR-T, bispecifics

---

## 🎯 Learning Objectives

- [ ] Classify NHL per WHO 2022: **B-cell (85-90%)** vs **T/NK-cell (10-15%)**
- [ ] Diagnose: **Excisional node biopsy** (gold standard), immunophenotype, FISH/cytogenetics, PET-CT staging (Ann Arbor/Lugano)
- [ ] Apply **prognostic indices**: **IPI (DLBCL)**, **FLIPI/FLIPI2 (FL)**, **MANTLE-IPI (MCL)**, **MIPI (MZL)**
- [ ] Manage **DLBCL**: **R-CHOP ×6** (standard); **Polatuzumab-R-CHP (Pola-R-CHP)** for high-intermediate/high IPI; CNS prophylaxis
- [ ] Manage **FL**: **R-Benda / R-CVP / Obinutuzumab-chemo**; **Tazemetostat (EZH2mut)**; **Radioimmunotherapy**
- [ ] Manage **MCL**: **R-CHOP / R-Benda** induction → **Auto-HSCT consolidation** (young/fit); **BTKi (Ibrutinib/Acalabrutinib/Zanubrutinib)** relapsed
- [ ] Manage **MZL**: **Rituximab ± chemo**; **Splenic MZL = Splenectomy/Rituximab**; **Gastric MALT = H. pylori eradication first**
- [ ] Manage **Burkitt**: **Intensive chemo (CODOX-M/IVAC, Hyper-CVAD, LMB) + Rituximab** ± CNS prophylaxis
- [ ] Recognise **Double/Triple Hit Lymphoma**: MYC + BCL2/BCL6 → **DA-EPOCH-R**
- [ ] Apply **CAR-T (Axicabtagene, Tisagenlecleucel, Lisocabtagene)** for R/R DLBCL/FL/MCL
- [ ] Apply **Bispecific Antibodies (Glofitamab, Epcoritamab)** for R/R DLBCL/FL

---

## 📖 WHO 2022 Classification – Key Subtypes

| Category | Subtypes | Frequency |
|----------|----------|-----------|
| **Mature B-cell Neoplasms** | | **~85-90%** |
| | **DLBCL** (Diffuse Large B-cell Lymphoma) | **~30-35%** (most common) |
| | **Follicular Lymphoma (FL)** | **~20-25%** |
| | **Mantle Cell Lymphoma (MCL)** | **~5-7%** |
| | **Marginal Zone Lymphoma (MZL)** | **~8-10%** (Extranodal/MALT, Nodal, Splenic) |
| | **Burkitt Lymphoma (BL)** | **~1-2%** |
| | **Lymphoplasmacytic Lymphoma / WM** | **~1-2%** |
| | **CLL/SLL** | **~25-30%** (see separate note) |
| **Mature T/NK-cell Neoplasms** | | **~10-15%** |
| | **Peripheral T-cell Lymphoma NOS (PTCL-NOS)** | Most common T-cell |
| | **Angioimmunoblastic T-cell Lymphoma (AITL)** | |
| | **Anaplastic Large Cell Lymphoma (ALCL, ALK+/-)** | |
| | **NK/T-cell Lymphoma (EBV+)** | |
| | **Adult T-cell Leukaemia/Lymphoma (HTLV-1)** | |

> [!tip] **FCPS/MRCP**: **DLBCL = most common aggressive B-NHL**; **FL = most common indolent B-NHL**; **MCL = t(11;14) Cyclin D1+**; **MZL = CD5-, CD23-, DBA44+**; **Burkitt = MYC translocation, Ki-67 100%**.

---

## 🔬 Diagnostic Workup (All Subtypes)

```mermaid
flowchart TD
    A[Lymphadenopathy / Extranodal Mass / B-symptoms] --> B[**Excisional Node Biopsy** (Gold Standard)]
    B --> C[Histology + Immunohistochemistry Panel]
    C --> D[Flow Cytometry (if fresh tissue)]
    D --> E[FISH / Cytogenetics / Molecular]
    E --> F[PET-CT Staging (Lugano Classification)]
    F --> G[Bone Marrow Biopsy (if stage III/IV or indicated)]
    G --> H[Baseline: LDH, HIV, Hepatitis B/C, Echo (anthracycline), Fertility, Pregnancy Test]
```

### Essential IHC Panel per Subtype

| Subtype | Positive Markers | Negative/Key Markers |
|---------|------------------|----------------------|
| **DLBCL** | **CD20+, CD79a+, BCL6+, PAX5+, MUM1/IRF4+ (variable)** | CD10+ (GCB), CD10- MUM1+ (ABC); BCL2+ (50%) |
| **FL** | **CD20+, CD10+, BCL6+, BCL2+ (t(14;18))**, CD23+ | CD5-, Cyclin D1- |
| **MCL** | **CD20+, CD5+, Cyclin D1+, SOX11+, CD23-, FMC7+** | CD10-, CD23- |
| **MZL** | **CD20+, CD5-, CD10-, CD23-, DBA44+, BCL2+** | Cyclin D1-, CD10- |
| **Burkitt** | **CD20+, CD10+, BCL6+, BCL2-, Ki-67 ~100%, MYC+** | BCL2-, MUM1- |
| **PTCL-NOS** | **CD3+, CD4+ (usually), CD5+, CD7+, TIA-1+, Granzyme B+** | CD20-, ALK- |
| **ALCL (ALK+)** | **CD30+, ALK+, EMA+, CD4+** | ALK- |
| **AITL** | **CD3+, CD4+, CD10+, CXCL13+, PD-1+, BCL6+, TET2/RHOA/IDH2 mut** | |
| **NK/T-cell** | **CD2+, CD56+, CD3ε+ (cytoplasmic), EBV+ (EBER+)** | CD3 surface-, CD20- |

---

## 📊 Prognostic Indices

### IPI (International Prognostic Index) – **DLBCL**

| Risk Factor | Points |
|-------------|--------|
| Age >60 | 1 |
| Stage III/IV | 1 |
| LDH >ULN | 1 |
| ECOG PS ≥2 | 1 |
| Extranodal sites >1 | 1 |

| Score | Risk Group | 5-yr OS (pre-Rituximab) | 5-yr OS (R-CHOP era) |
|-------|------------|-------------------------|----------------------|
| 0-1 | Low | 73% | ~90% |
| 2 | Low-Intermediate | 51% | ~80% |
| 3 | High-Intermediate | 43% | ~65% |
| 4-5 | High | 26% | ~55% |

> **R-IPI** (Rituximab era): 3 groups (Very Good 0, Good 1-2, Poor 3-5)

### FLIPI / FLIPI-2 – **Follicular Lymphoma**

| FLIPI (Pre-treatment) | FLIPI-2 (Post-induction) |
|-----------------------|--------------------------|
| Age >60 | β2M >ULN |
| Stage III/IV | Longest diameter >6cm |
| Hb <120 g/L | Hb <120 g/L |
| Nodal sites ≥5 | Age >60 |
| LDH >ULN | |

### MANTLE-IPI – **Mantle Cell Lymphoma** (Simplified MIPI)

| Factor | Points |
|--------|--------|
| Age ≥65 | 1 |
| ECOG PS 1-2 | 1 |
| WBC ≥6.7×10⁹/L | 1 |
| Ki-67 ≥30% | 1 |
| Blastoid morphology | 1 |

| Score | Risk | Median OS |
|-------|------|-----------|
| 0-1 | Low | Not reached |
| 2-3 | Intermediate | ~5-7 years |
| 4-5 | High | ~2-3 years |

---

## 💊 Subtype-Specific Management

### 1. Diffuse Large B-cell Lymphoma (DLBCL) – **Most Common Aggressive NHL**

#### Frontline
| Risk | Regimen | Key Trials |
|------|---------|------------|
| **Standard (IPI 0-2)** | **R-CHOP × 6 cycles** | Standard of care >20 years |
| **High-Intermediate/High (IPI 3-5)** | **Pola-R-CHP** (Polatuzumab vedotin + R-CHP) | **POLARIX trial** – improved PFS |
| **Double/Triple Hit (MYC+BCL2/BCL6)** | **DA-EPOCH-R** (Dose-adjusted EPOCH-R) | Dose-intensive, CNS prophylaxis |
| **Elderly/Frail** | **R-mini-CHOP** (dose-reduced) | | R-GemOx |

#### CNS Prophylaxis (DLBCL)
- **Indicated if**: **High-risk sites** (testicular, breast, adrenal, kidney, epidural, paranasal sinus, bone marrow involvement) OR **≥2 CNS-IPI risk factors** (Age>60, Stage III/IV, LDH>ULN, ECOG≥2, Extranodal>1, Kidney/Adrenal involvement)
- **Method**: **Intrathecal MTX (4-6 doses)** during/after R-CHOP; **High-dose MTX (3.5 g/m²) × 2-4 cycles** alternative

#### Relapsed/Refractory DLBCL
| Line | Options |
|------|---------|
| **2nd Line (Transplant-eligible)** | **R-DHAP / R-ICE / R-GDP** → **Auto-HSCT** if chemosensitive |
| **2nd Line (Transplant-ineligible)** | **Polatuzumab + BR / Tafasitamab + Len** |
| **3rd Line+ / R/R Post-ASCT** | **CAR-T**: Axicabtagene (ZUMA-1), Tisagenlecleucel (JULIET), **Lisocabtagene (TRANSCEND)** |
| | **Bispecifics**: **Glofitamab (CD20×CD3)**, **Epcoritamab (CD20×CD3)** |
| | **BCL2 inhibitor**: Venetoclax (if t(14;18)) + R / + Pola |
| | **Antibody-Drug Conjugate**: Loncastuximab tesirine (CD19) |

---

### 2. Follicular Lymphoma (FL) – **Most Common Indolent NHL**

| Stage / Risk | Frontline | Key Points |
|--------------|-----------|------------|
| **Stage I-II (Localised)** | **Radiotherapy 24-30 Gy** (curative intent) |  |
| **Stage III-IV Asymptomatic (GELF criteria not met)** | **Watch & Wait** (observation) | No OS benefit to early Rx |
| **Stage III-IV Symptomatic / Bulky** | **R-Benda (Rituximab + Bendamustine)** or **R-CVP** or **G-chemo (Obinutuzumab + Bendamustine/CHOP/CVP)** | **GALLIUM: G-chemo > R-chemo PFS** |
| **Relapsed** | **BTKi (Zanubrutinib)** + Obinutuzumab, **Tazemetostat (EZH2mut)**, **CAR-T (Axi/Liso)**, **Bispecifics (Mosunetuzumab, Epcoritamab)**, **Radioimmunotherapy (Ibritumomab)** | **EZH2mut ~20-25%** |

> [!tip] **Transformation to DLBCL**: ~2-3%/yr; **Excisional biopsy + PET-CT** → Treat as DLBCL (R-CHOP/Pola-R-CHP) → **Auto-HSCT if remission**

---

### 3. Mantle Cell Lymphoma (MCL) – **t(11;14) Cyclin D1+**

| Setting | Regimen |
|---------|---------|
| **Young/Fit (≤65-70, eligible for HSCT)** | **R-CHOP / R-Benda** induction (4-6 cycles) → **Auto-HSCT (BEAM/BEAC) consolidation** → **Rituximab maintenance** |
| **Elderly/Unfit** | **R-Benda** (preferred) or **R-CHOP** or **VR-CAP** (Bortezomib + R-CHOP) |
| **Relapsed/Refractory** | **BTKi: Ibrutinib / Acalabrutinib / Zanubrutinib** (high response rates, continuous) |
| | **Venetoclax** (BCL2+), **CAR-T (Brexucabtagene)**, **Bortexizumab** |

> [!warning] **MCL = Auto-HSCT in CR1 is standard for fit patients**. **BTKi = Game-changer for R/R**.

---

### 4. Marginal Zone Lymphoma (MZL)

| Subtype | Management |
|---------|------------|
| **Gastric MALT** | **H. pylori eradication (triple therapy)** first → remission in 70-80% if localised; **Radiotherapy** if H. pylori -ve or persistent |
| **Non-gastric MALT** | **Radiotherapy** (localised); **Rituximab ± Chemo** (advanced) |
| **Nodal MZL** | **Watch & Wait** if asymptomatic; **R-Benda / R-CHOP / R-CVP** if treatment needed |
| **Splenic MZL (SMZL)** | **Splenectomy** (historical); **Rituximab monotherapy** (current standard); **BTKi** if relapsed |

---

### 5. Burkitt Lymphoma (BL) – **MYC translocation, Ki-67 100%**

| Feature | Details |
|---------|---------|
| **Genetics** | **t(8;14) MYC::IGH** (80%), t(8;22) MYC::IGL, t(2;8) MYC::IGK |
| **Immunophenotype** | **CD20+, CD10+, BCL6+, BCL2-, Ki-67 ~100%**, MYC protein+ |
| **Treatment** | **Intensive chemo + Rituximab**: **CODOX-M/IVAC**, **Hyper-CVAD**, **LMB (pediatric)** |
| **CNS Prophylaxis** | **Mandatory**: Intrathecal MTX/Ara-C + **High-dose MTX (3-4 g/m²)** during systemic chemo |
| **TLS Risk** | **EXTREME** – Rasburicase, aggressive hydration, allopurinol, monitor q6h |

> [!warning] **Burkitt = Medical Emergency**. **Ki-67 100%, MYC+, BCL2-**; **Start chemo within 24h of diagnosis**.

---

### 6. Double/Triple Hit Lymphoma (DH/TH-L)

| Definition | MYC rearrangement + **BCL2 and/or BCL6 rearrangement** (by FISH) |
|------------|------------------------------------------------------------------|
| **DH**: MYC + BCL2 (most common) | |
| **TH**: MYC + BCL2 + BCL6 | |
| **Treatment** | **DA-EPOCH-R** (Dose-adjusted EPOCH-R) preferred over R-CHOP |
| **CNS Prophylaxis** | **Mandatory** (High CNS risk) |
| **Outcomes** | Better with DA-EPOCH-R but still inferior to standard DLBCL |

---

### 7. T-cell Lymphomas (Key Subtypes)

| Subtype | Key Features | Treatment |
|---------|--------------|-----------|
| **PTCL-NOS** | CD4+, heterogeneous | **CHOP / CHOEP** → Auto-HSCT in CR1; **Pralatrexate / Belinostat / Brentuximab (if CD30+)** relapsed |
| **AITL** | CD4+, CD10+, CXCL13+, PD-1+, **TET2/RHOA/IDH2 mut** | Same as PTCL; **Anti-PD-1 (Pembrolizumab)** emerging |
| **ALCL (ALK+)** | CD30+, ALK+, young, good prognosis | **CHOP** → excellent cure rate; **Brentuximab vedotin** relapsed |
| **ALCL (ALK-)** | CD30+, ALK-, older, worse prognosis | **CHOP** → Auto-HSCT in CR1; **Brentuximab** |
| **NK/T-cell (EBV+)** | Nasal/extranodal, EBV+, CD56+, CD3ε+, **Asparaginase-sensitive** | **SMILE / DeVIC / AspaMetDex** (Asparaginase-based) → CRT; **PD-1 inhibitors** |

---

## 🌱 CAR-T & Bispecific Antibodies (R/R Aggressive B-NHL)

| Agent | Target | Indication | Key Trial |
|-------|--------|------------|-----------|
| **Axicabtagene Ciloleucel (Axi-cel)** | CD19 CAR-T | R/R DLBCL, PMBCL, FL (after ≥2 lines) | ZUMA-1, ZUMA-5 |
| **Tisagenlecleucel (Tisa-cel)** | CD19 CAR-T | R/R DLBCL, FL (after ≥2 lines) | JULIET, ELARA |
| **Lisocabtagene Maraleucel (Liso-cel)** | CD19 CAR-T | R/R DLBCL (after ≥2 lines) | TRANSCEND |
| **Brexucabtagene (Brexu-cel)** | CD19 CAR-T | **R/R MCL** | ZUMA-2 |
| **Glofitamab** | CD20×CD3 BiTE | R/R DLBCL (after ≥2 lines) | NP30179 |
| **Epcoritamab** | CD20×CD3 BiTE | R/R DLBCL, FL | EPCORE |
| **Mosunetuzumab** | CD20×CD3 BiTE | R/R FL (after ≥2 lines) | GO29781 |

> [!tip] **FCPS/MRCP**: **CAR-T = CD19 CAR-T for R/R DLBCL/FL/MCL after ≥2 lines**. **Bispecifics = CD20×CD3 (Glofitamab, Epcoritamab, Mosunetuzumab) – off-the-shelf, step-up dosing, CRS/ICANS risk**.

---

## 🔄 Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **DLBCL vs Burkitt** | **Burkitt: Ki-67 100%, BCL2-, MYC+, starry-sky**; DLBCL: Ki-67 variable, BCL2+ (50%) |
| **FL vs MZL** | **FL: CD10+, BCL2+, t(14;18)**; **MZL: CD10-, CD5-, DBA44+, no t(14;18)** |
| **MCL vs CLL** | **MCL: Cyclin D1+, SOX11+, CD23-, FMC7+**; **CLL: CD23+, CD5+, Cyclin D1-, CD20 dim, sIg dim** |
| **PTCL vs AITL** | **AITL: CD10+, PD-1+, CXCL13+, TET2/RHOA/IDH2 mut**; PTCL: usually CD10- |
| **ALCL vs DLBCL** | **ALCL: CD30+, ALK+/- (T-cell markers)**; DLBCL: CD20+, B-cell markers |
| **NK/T-cell vs PTCL** | **NK/T: EBV+ (EBER+), CD56+, CD3ε+ cytoplasmic, nasal/extranodal** |

---

## 💡 FCPS/MRCP High-Yield Summary

| Topic | Key Point |
|-------|-----------|
| **NHL Classification** | **B-cell 85-90%** (DLBCL 30-35%, FL 20-25%, MCL 5-7%, MZL 8-10%, Burkitt 1-2%) |
| **Diagnosis** | **Excisional node biopsy** (core/incisional inadequate); IHC, Flow, FISH, PET-CT |
| **DLBCL Frontline** | **R-CHOP ×6 (IPI 0-2)**; **Pola-R-CHP (IPI 3-5, POLARIX)**; **DA-EPOCH-R (DH/TH)** |
| **DLBCL CNS Prophylaxis** | High-risk sites OR CNS-IPI ≥2 → **IT MTX or HD-MTX** |
| **FL Indolent** | **Stage I-II = RT (curative)**; **Stage III-IV asymptomatic = Watch & Wait**; Symptomatic = **R-Benda / G-chemo** |
| **FL Transformation** | **Excisional biopsy → Treat as DLBCL** |
| **MCL** | **t(11;14) Cyclin D1+** → Fit young = **R-CHOP/R-Benda → Auto-HSCT** → Ritux maint; R/R = **BTKi** |
| **MZL (Gastric MALT)** | **H. pylori eradication FIRST** |
| **Burkitt** | **MYC translocation, Ki-67 100%, BCL2-** → **CODOX-M/IVAC/Hyper-CVAD + RTX + CNS prophylaxis** |
| **DH/TH Lymphoma** | **MYC + BCL2/BCL6** → **DA-EPOCH-R + CNS prophylaxis** |
| **CAR-T** | CD19 CAR-T for **R/R DLBCL/FL/MCL after ≥2 lines** (Axi, Tisa, Liso, Brexu) |
| **Bispecifics** | **Glofitamab, Epcoritamab (CD20×CD3)** – step-up dosing, CRS/ICANS |

---

## ❓ Viva Questions

1. **What is the gold standard for NHL diagnosis?**
   - **Excisional lymph node biopsy** (adequate tissue for histology, IHC, flow, FISH)

2. **What are the IPI risk factors for DLBCL?**
   - Age >60, Stage III/IV, LDH >ULN, ECOG PS ≥2, Extranodal sites >1

3. **What is the first-line treatment for DLBCL with IPI 0-2 vs IPI 3-5?**
   - **IPI 0-2: R-CHOP ×6**; **IPI 3-5: Pola-R-CHP (POLARIX trial)** or R-CHOP

4. **How does FL management differ by stage?**
   - **Stage I-II = Radiotherapy (curative)**; **Stage III-IV asymptomatic = Watch & Wait**; **Symptomatic = R-Benda or G-chemo**

5. **What is the genetic hallmark of MCL and how does it affect treatment?**
   - **t(11;14) → Cyclin D1 overexpression**; Fit young → **R-CHOP/R-Benda → Auto-HSCT consolidation → Rituximab maintenance**

6. **What is the first step in gastric MALT lymphoma?**
   - **H. pylori eradication therapy** (triple therapy) – remission in 70-80% if localised

7. **Describe Burkitt lymphoma immunophenotype and treatment.**
   - **CD20+, CD10+, BCL6+, BCL2-, Ki-67 ~100%, MYC+**; **Intensive chemo (CODOX-M/IVAC/Hyper-CVAD) + Rituximab + CNS prophylaxis**

8. **What defines Double Hit Lymphoma and how is it treated?**
   - **MYC + BCL2 rearrangement (FISH)**; Treated with **DA-EPOCH-R + CNS prophylaxis**

9. **When is CNS prophylaxis indicated in DLBCL?**
   - **High-risk sites** (testicular, breast, adrenal, kidney, epidural, sinus, BM) OR **CNS-IPI ≥2 factors** (Age>60, Stage III/IV, LDH>ULN, ECOG≥2, Extranodal>1, Kidney/Adrenal)

10. **What are the CAR-T options for R/R DLBCL?**
    - **Axicabtagene (ZUMA-1)**, **Tisagenlecleucel (JULIET)**, **Lisocabtagene (TRANSCEND)** – all CD19 CAR-T, after ≥2 lines

---

## 🧠 Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **DLBCL vs Burkitt** | **Burkitt = Ki-67 100%, BCL2-, MYC+**; DLBCL = Ki-67 variable, BCL2+ common |
| **FL vs MZL** | **FL = CD10+, BCL2+, t(14;18)**; **MZL = CD10-, CD5-, DBA44+** |
| **MCL vs CLL** | **MCL = Cyclin D1+, SOX11+, CD23-, FMC7+**; **CLL = CD23+, CD5+, CD20 dim, sIg dim, Cyclin D1-** |
| **R-CHOP vs Pola-R-CHP** | **Pola-R-CHP = R-CHP + Polatuzumab (anti-CD79b ADC)**; For IPI 3-5 |
| **DA-EPOCH-R vs R-CHOP** | **DA-EPOCH-R = Dose-adjusted EPOCH-R (infusional)**; For DH/TH lymphoma |
| **CAR-T vs Bispecifics** | **CAR-T = Autologous, manufacturing time, hospitalisation**; **Bispecifics = Off-the-shelf, step-up dosing** |

| Mnemonic | Meaning |
|----------|---------|
| **"R-CHOP = Standard DLBCL"** | Rituximab, Cyclophosphamide, Hydroxydaunorubicin, Oncovin, Prednisone |
| **"Pola-R-CHP = POLARIX for High IPI"** | Polatuzumab vedotin + R-CHP |
| **"FL = CD10, BCL2, t(14;18)"** | Follicular lymphoma markers |
| **"MCL = Cyclin D1, t(11;14)"** | Mantle cell lymphoma |
| **"MALT = H. pylori First"** | Gastric MALT management |
| **"Burkitt = 100% Ki-67, MYC+, BCL2-"** | Burkitt lymphoma |
| **"DH = MYC + BCL2 = DA-EPOCH-R"** | Double hit lymphoma |
| **"CAR-T = Autologous, Bispecific = Off-shelf"** | Cellular vs off-shelf immunotherapy |

---

## 🗺️ Mind Map

```mermaid
mindmap
  root((Non-Hodgkin Lymphoma))
    B-cell (85-90%)
      DLBCL (30-35%)
        R-CHOP (IPI 0-2)
        Pola-R-CHP (IPI 3-5)
        DA-EPOCH-R (DH/TH)
        CNS Prophylaxis
        R/R: CAR-T, Bispecifics
      FL (20-25%)
        Stage I-II: RT
        Stage III-IV Asx: Watch & Wait
        Symptomatic: R-Benda / G-chemo
        Transformation: Treat as DLBCL
        Relapse: BTKi, Tazemetostat, CAR-T, Bispecifics
      MCL (5-7%)
        t(11;14) Cyclin D1+
        Young/Fit: R-CHOP → Auto-HSCT → Ritux maint
        R/R: BTKi (Ibru/Acal/Zanu)
      MZL (8-10%)
        Gastric MALT: H. pylori eradication
        Nodal/Splenic: Ritux ± Chemo / Splenectomy
      Burkitt (1-2%)
        MYC+, Ki-67 100%, BCL2-
        CODOX-M/IVAC/Hyper-CVAD + RTX
        Mandatory CNS prophylaxis
      DH/TH
        MYC + BCL2/BCL6
        DA-EPOCH-R + CNS prophylaxis
      WM/LPL
        IgM, MYD88 L265P
        BTKi, Rituximab-based
    T/NK-cell (10-15%)
      PTCL-NOS: CHOP/CHOEP → HSCT
      AITL: TET2/RHOA/IDH2, PD-1 inhibitors
      ALCL ALK+: CHOP (excellent prognosis)
      ALCL ALK-: CHOP → HSCT, Brentuximab
      NK/T: EBV+, Asp-based (SMILE), PD-1 inhibitors
    Novel Immunotherapy
      CAR-T: Axi, Tisa, Liso (CD19), Brexu (MCL)
      Bispecifics: Glofitamab, Epcoritamab (CD20×CD3), Mosunetuzumab
```

---

## 📋 One-Page Revision Card

| **NHL SUBTYPES – FCPS/MRCP REVISION CARD** |
|--------------------------------------------|
| **Diagnosis**: **Excisional biopsy** + IHC/Flow/FISH + PET-CT (Lugano) |
| **DLBCL (30-35%)**: R-CHOP (IPI 0-2); **Pola-R-CHP (IPI 3-5)**; DA-EPOCH-R (DH/TH); CNS prophylaxis if high-risk |
| **FL (20-25%)**: I-II = **RT**; III-IV Asx = **Watch & Wait**; Sx = **R-Benda / G-chemo**; Transform = DLBCL Rx |
| **MCL (5-7%)**: **t(11;14) Cyclin D1+**; Young/Fit = **R-CHOP → Auto-HSCT → Ritux maint**; R/R = **BTKi** |
| **MZL**: **Gastric MALT = H. pylori eradication first**; Nodal/Splenic = Ritux ± Chemo |
| **Burkitt (1-2%)**: **MYC+, Ki-67 100%, BCL2-**; **CODOX-M/IVAC/Hyper-CVAD + RTX + CNS prophylaxis** |
| **DH/TH**: **MYC + BCL2/BCL6** → **DA-EPOCH-R + CNS prophylaxis** |
| **T-cell**: PTCL (CHOP→HSCT), AITL (TET2/RHOA/IDH2), ALK+ ALCL (CHOP, great prognosis), NK/T (EBV+, Asparaginase-based) |
| **CAR-T**: Axi/Tisa/Liso (CD19, R/R DLBCL/FL), Brexu (MCL) – after ≥2 lines |
| **Bispecifics**: Glofitamab/Epcoritamab (CD20×CD3) – off-shelf, step-up, CRS/ICANS |

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
| **Must Know** | Excisional biopsy gold standard, IPI/FLIPI/MANTLE-IPI, DLBCL R-CHOP vs Pola-R-CHP vs DA-EPOCH-R, FL watch & wait vs RT vs chemo, MCL Auto-HSCT consolidation, MCL BTKi for R/R, Gastric MALT H. pylori, Burkitt intensive chemo + CNS prophylaxis, DH/TH DA-EPOCH-R, CAR-T indications (R/R ≥2 lines), Bispecifics mechanism |
| **Should Know** | CNS-IPI for DLBCL, GALLIUM trial (G-chemo), Polatuzumab mechanism, CAR-T CRS/ICANS management, Bispecific step-up dosing, Tazemetostat (EZH2mut FL), Radioimmunotherapy (Ibritumomab), WM (MYD88 L265P, BTKi), ALCL ALK+ vs ALK-, NK/T asparaginase-based, Double expressor (MYC/BCL2 protein, not FISH) |
| **Nice to Know** | Detailed POLARIX/GALLIUM/MAIA/ZUMA-1/JULIET/TRANSCEND/NP30179/EPCORE trial data, NCCN/ESMO/EHA guideline updates, CAR-T manufacturing failures, bridging therapy, bispecific subcutaneous formulations, T-cell lymphoma genomic landscape, post-CAR-T monitoring, lymphoma in immunocompromised (PTLD, HIV), paediatric vs adult Burkitt protocols |

---

## ✅ Self-Test Scorecard

| Section | Score (0-10) | Notes |
|---------|--------------|-------|
| WHO Classification & Diagnosis | | |
| DLBCL Management (IPI-based) | | |
| FL Management (Stage-based) | | |
| MCL Management | | |
| MZL Subtypes | | |
| Burkitt Lymphoma | | |
| DH/TH Lymphoma | | |
| T-cell Lymphomas | | |
| CAR-T & Bispecifics | | |
| Viva Questions | | |

---

## 🔗 Local Navigation

- **Previous**: [[Multiple Myeloma]]
- **Next**: [[Hodgkin Lymphoma]]
- **Section Hub**: [[Haematological Malignancies]]
- **MOC**: [[Hematology MOC]]
- **Template**: [[../Templates/Hematology Topic Template]]

---

*Generated for FCPS/MRCP exam preparation. Based on Davidson Medicine 24th Ed Chapter 25.*
---

> Auto-generated study sections for "Hematology" — Ch 24: Haematology & Transfusion Medicine.

## Flashcards (23 generated)

- Q: What is the definition of Hematology?
  A: [!info] Davidson Ch 25 Alignment: Haematological Malignancies → Lymphomas → Non-Hodgkin Lymphoma
- Q: What is Genetics of Hematology?
  A: t(8;14) MYC::IGH (80%), t(8;22) MYC::IGL, t(2;8) MYC::IGK
- Q: How is Hematology classified?
  A: CD20+, CD10+, BCL6+, BCL2-, Ki-67 ~100%, MYC protein+
- Q: How is Hematology managed?
  A: Intensive chemo + Rituximab: CODOX-M/IVAC, Hyper-CVAD, LMB (pediatric)
- Q: What is CNS Prophylaxis of Hematology?
  A: Mandatory: Intrathecal MTX/Ara-C + High-dose MTX (3-4 g/m²) during systemic chemo
- Q: What is TLS Risk of Hematology?
  A: EXTREME – Rasburicase, aggressive hydration, allopurinol, monitor q6h
- Q: What is Genetics of Hematology?
  A: t(8;14) MYC::IGH (80%), t(8;22) MYC::IGL, t(2;8) MYC::IGK
- Q: How is Hematology classified?
  A: CD20+, CD10+, BCL6+, BCL2-, Ki-67 ~100%, MYC protein+
- Q: How is Hematology managed?
  A: Intensive chemo + Rituximab: CODOX-M/IVAC, Hyper-CVAD, LMB (pediatric)
- Q: What is CNS Prophylaxis of Hematology?
  A: Mandatory: Intrathecal MTX/Ara-C + High-dose MTX (3-4 g/m²) during systemic chemo
- Q: What is TLS Risk of Hematology?
  A: EXTREME – Rasburicase, aggressive hydration, allopurinol, monitor q6h
- Q: How is Hematology classified?
  A: B-cell 85-90% (DLBCL 30-35%, FL 20-25%, MCL 5-7%, MZL 8-10%, Burkitt 1-2%)
- Q: What is the investigation of choice for Hematology?
  A: Excisional node biopsy (core/incisional inadequate); IHC, Flow, FISH, PET-CT
- Q: What is DLBCL Frontline of Hematology?
  A: R-CHOP ×6 (IPI 0-2); Pola-R-CHP (IPI 3-5, POLARIX); DA-EPOCH-R (DH/TH)
- Q: What is DLBCL CNS Prophylaxis of Hematology?
  A: High-risk sites OR CNS-IPI ≥2 → IT MTX or HD-MTX
- Q: What is FL Indolent of Hematology?
  A: Stage I-II = RT (curative); Stage III-IV asymptomatic = Watch & Wait; Symptomatic = R-Benda / G-chemo
- Q: What is FL Transformation of Hematology?
  A: Excisional biopsy → Treat as DLBCL
- Q: What is MCL of Hematology?
  A: t(11;14) Cyclin D1+ → Fit young = R-CHOP/R-Benda → Auto-HSCT → Ritux maint; R/R = BTKi
- Q: What is MZL (Gastric MALT) of Hematology?
  A: H. pylori eradication FIRST
- Q: What is Burkitt of Hematology?
  A: MYC translocation, Ki-67 100%, BCL2- → CODOX-M/IVAC/Hyper-CVAD + RTX + CNS prophylaxis
- Q: What is DH/TH Lymphoma of Hematology?
  A: MYC + BCL2/BCL6 → DA-EPOCH-R + CNS prophylaxis
- Q: What is CAR-T of Hematology?
  A: CD19 CAR-T for R/R DLBCL/FL/MCL after ≥2 lines (Axi, Tisa, Liso, Brexu)
- Q: What is Bispecifics of Hematology?
  A: Glofitamab, Epcoritamab (CD20×CD3) – step-up dosing, CRS/ICANS

## MCQs (1 generated)

1. **Which of the following best describes Hematology?**
   A. **[!info] Davidson Ch 25 Alignment: Haematological Malignancies → Lymphomas → Non-Hodgkin Lymphoma**
   B. An unrelated condition not matching the clinical picture of Hematology
   C. A complication seen late in the disease course of Hematology
   D. A condition that mimics Hematology but has a different underlying cause

## SBA Questions (1 generated)

1. A patient with suspected Hematology presents with: Mature B-cell Neoplasms — ;  — DLBCL (Diffuse Large B-cell Lymphoma);  — Follicular Lymphoma (FL). What is the most likely diagnosis?
   A. **Hematology**
   B. A condition that mimics Hematology but is not the same entity
   C. A complication of Hematology rather than the primary diagnosis
   D. An unrelated condition in the same clinical category as Hematology

