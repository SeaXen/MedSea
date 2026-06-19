---
tags: [medicine, davidson, hematology, myeloma, plasma-cell-disorder, fcps, mrcp]
davidson_chapter: Chapter 25: Haematology and Transfusion Medicine
status: full-fcps-mrcp-note
priority: high
exam_relevance: "FCPS: Essential | MRCP: Core | High-yield for vivas, CRAB/SLiM, R-ISS, triplet induction, transplant eligibility, MRD"
see_also: "[[MGUS]], [[Amyloidosis]], [[Waldenström Macroglobulinaemia]], [[Smouldering Myeloma]], [[Stem Cell Transplantation]]"
created: 2025-06-15
modified: 2025-06-15
---

# Multiple Myeloma (MM)

> [!info] **Davidson Ch 25 Alignment**: Haematological Malignancies → Plasma Cell Disorders → Multiple Myeloma
> **FCPS/MRCP Focus**: CRAB/SLiM criteria, R-ISS staging, triplet induction (VRd/Dara-VRd), transplant eligibility, maintenance, MRD, renal management

---

## 🎯 Learning Objectives

- [ ] Diagnose MM using **SLiM-CRAB criteria**: Clonal BM plasma cells ≥10% (or biopsy-proven plasmacytoma) + **Myeloma-Defining Events (MDE)**
- [ ] Differentiate **MGUS, Smouldering Myeloma (SMM), Active Myeloma** by M-protein, BMPC%, CRAB/SLiM
- [ ] Apply **R-ISS (Revised ISS) Staging**: ISS + FISH (del17p, t(4;14), t(14;16)) + LDH
- [ ] Select **induction**: **VRd (Bortezomib + Lenalidomide + Dex)** or **Dara-VRd (Daratumumab + VRd)** for transplant-eligible; **VRd-lite / Rd / Dara-Rd** for transplant-ineligible
- [ ] Determine **transplant eligibility**: Age <70-75, fit, CGA, no major comorbidities → **Autologous HSCT** (melphalan 200)
- [ ] Apply **maintenance**: **Lenalidomide** post-transplant (until progression); **Dara-Rd** maintenance emerging
- [ ] Monitor **Response (IMWG)**: sCR, CR, VGPR, PR, MR, SD, PD; **MRD** (NGS 10⁻⁵-10⁻⁶, Flow 10⁻⁵)
- [ ] Manage **renal failure**: **Bortezomib-based** (no dose adjust), hydration, avoid NSAIDs, bisphosphonates, early dialysis if needed
- [ ] Manage **bone disease**: **Zoledronic acid / Denosumab** (monthly × 1-2yr, then q3mo), **Dental exam** pre-treatment
- [ ] Recognise **Relapse categories**: Biochemical, Clinical; select next-line based on prior exposure, refractoriness, TP53 status

---

## 📖 Definition & Diagnostic Criteria (IMWG 2014/2022)

### SLiM-CRAB Criteria for Active Myeloma

**Require BOTH:**
1. **Clonal BM plasma cells ≥10%** (or biopsy-proven plasmacytoma)
2. **≥1 Myeloma-Defining Event (MDE)**:

| Category | MDE (SLiM) |
|----------|-------------|
| **S** | **Bone lesions**: ≥1 lytic lesion on CT/PET-CT (not plain X-ray) |
| **L** | **Clonal BM plasma cells ≥60%** |
| **iM** | **Involved/Uninvolved FLC ratio ≥100** (absolute involved FLC ≥100 mg/L) |
| **C** | **Hypercalcaemia**: Corrected Ca >2.75 mmol/L (>11 mg/dL) |
| **R** | **Renal insufficiency**: Creatinine >177 µmol/L (>2 mg/dL) or eGFR <40 |
| **A** | **Anaemia**: Hb <10 g/dL or >2 g/dL below LLN |
| **B** | **Bone lesions**: ≥1 lytic lesion (plain X-ray/CT/PET-CT) |

> [!tip] **FCPS/MRCP**: **SLiM = biomarkers (no CRAB symptoms); CRAB = end-organ damage**. **≥10% BMPC + 1 MDE = Active Myeloma**. **SMM = ≥10% BMPC or M-spike ≥30g/L but NO MDE**.

### Differential Spectrum

| Entity | BM Plasma Cells | M-Protein | CRAB/SLiM | Management |
|--------|-----------------|-----------|-----------|------------|
| **MGUS** | <10% | <30 g/L | None | Observe (1%/yr progression) |
| **Smouldering Myeloma (SMM)** | **≥10% OR M-spike ≥30g/L** | Any | **None** | Observe (high-risk SMM → consider early Rx trials) |
| **Active Myeloma** | **≥10%** (usually) | Usually present | **≥1 MDE (SLiM/CRAB)** | **TREAT** |
| **Solitary Plasmacytoma** | <10% (marrow) | None/Minimal | Single bone/soft tissue lesion | **Radiotherapy ± observation** |

---

## ⚙️ Pathophysiology

```mermaid
flowchart TD
    A[Genetic Insult: Translocations / Hyperdiploidy] --> B[Plasma Cell Transformation]
    B --> C[Clonal Expansion in Marrow]
    C --> D[Monoclonal Protein Secretion]
    D --> E1[CRAB: End-Organ Damage]
    D --> E2[SLiM: Biomarkers]
    C --> F[Microenvironment Interaction: IL-6, APRIL, BAFF, VEGF]
    F --> G[Angiogenesis, Osteoclast Activation (RANKL↑/OPG↓)]
    G --> H[Lytic Lesions, Bone Pain, Fractures, Hypercalcaemia]
    E1 & E2 --> I[Organ Dysfunction]
```

**Key Driver Mutations:**
- **IgH Translocations (40%)**: t(11;14) CCND1, t(4;14) FGFR3/MMSET, t(14;16) MAF, t(14;20) MAFB
- **Hyperdiploidy (50%)**: Trisomies of odd chromosomes (3,5,7,9,11,15,19,21)
- **Secondary**: TP53, RAS, MYC, NF-κB pathway mutations

---

## 🔬 Diagnostic Workup

```mermaid
flowchart TD
    A[Suspected Myeloma: Bone Pain, Anaemia, Renal, High ESR, HyperCa] --> B[CBC, U&E, LFT, Ca, Albumin, LDH, β2M]
    B --> C[Serum Protein Electrophoresis (SPEP) + Immunofixation]
    B --> D[24h Urine Protein Electrophoresis (UPEP) + Immunofixation]
    B --> E[Serum Free Light Chains (sFLC) κ/λ Ratio]
    C & D & E --> F{Monoclonal Protein?}
    F -->|Yes| G[BM Aspirate + Biopsy: BMPC%, Flow Cytometry (CD38+, CD138+, CD19-, CD56+, CD45-)]
    G --> H[Cytogenetics: FISH Panel + Karyotype]
    H --> I[Imaging: **Whole-Body Low-Dose CT (WBLD-CT) or PET-CT** (not skeletal survey)]
    I --> J[Staging: **R-ISS**]
    J --> K[Baseline: Echo, Dental, Vaccines, Viral Screen, HLA Typing]
```

### Essential Investigations

| Test | Purpose |
|------|---------|
| **SPEP + Immunofixation** | Identify & quantify M-spike (IgG, IgA, IgD, IgE, IgM, light chain only) |
| **UPEP + Immunofixation** | Bence Jones protein (light chain only disease) |
| **sFLC (κ/λ ratio)** | **Light chain myeloma**, oligosecretory, non-secretory; **ratio ≥100 = SLiM** |
| **BM Aspirate/Biopsy** | **BMPC% (clonality by κ/λ restriction)**, flow cytometry |
| **FISH Panel** | **Mandatory**: del17p, t(4;14), t(14;16), t(14;20), 1q gain, del1p, del13q |
| **Karyotype** | Hyperdiploidy, complex karyotype |
| **Imaging** | **WBLD-CT or PET-CT** (standard; skeletal survey obsolete) |
| **β2-Microglobulin, Albumin, LDH** | **R-ISS Staging** |

---

## 📊 R-ISS Staging (Revised International Staging System)

| Stage | Criteria | Median OS | 5-yr OS |
|-------|----------|-----------|---------|
| **I** | **ISS I (β2M <3.5, Alb ≥35) + No high-risk FISH + Normal LDH** | Not reached | ~80% |
| **II** | Not I or III | ~8-10 years | ~60% |
| **III** | **ISS III (β2M >5.5) + High-risk FISH (del17p, t(4;14), t(14;16)) OR High LDH** | ~4-5 years | ~40% |

> [!tip] **FCPS/MRCP**: **R-ISS = ISS + FISH (del17p, t(4;14), t(14;16)) + LDH**. **High-risk FISH = del17p, t(4;14), t(14;16)**.

---

## 💊 Treatment Algorithm

### Transplant-Eligible (TE) – Age <70-75, Fit

```mermaid
flowchart TD
    A[Newly Diagnosed TE MM] --> B[Induction: **Dara-VRd (4 cycles)** preferred<br/>or **VRd (4 cycles)**]
    B --> C[Stem Cell Mobilisation: G-CSF ± Plerixafor]
    C --> D[**High-Dose Melphalan 200 mg/m² (HDM) + Auto-HSCT**]
    D --> E[Consolidation: **Dara-VRd × 2 cycles** (optional)]
    E --> F[Maintenance: **Lenalidomide 10-15 mg days 1-21** until progression]
```

### Transplant-Ineligible (TIE) – Age >75 or Unfit

| Regimen | Components | Key Trials | Notes |
|---------|------------|------------|-------|
| **Dara-Rd** | Daratumumab + Lenalidomide + Dex | MAIA | **Preferred** for fit TIE |
| **VRd-lite** | Bortezomib 1.3mg/m² d1,4,8,11 + Len 25mg d1-21 + Dex | SWOG S0777 | Reduced bortezomib dose |
| **Rd** | Lenalidomide + Dex | FIRST | Frail/elderly |
| **VMP** | Bortezomib + Melphalan + Prednisone | VISTA | Non-lenalidomide option |

> [!tip] **FCPS/MRCP**: **TE = Dara-VRd → Auto-HSCT (Mel 200) → Len maintenance**. **TIE = Dara-Rd (preferred) or VRd-lite**. **Dara-VRd now standard for TE (GRIFFIN, PERSEUS)**.

---

## 💊 Induction Regimens Detail

### Dara-VRd (Daratumumab + Bortezomib + Lenalidomide + Dexamethasone)

| Drug | Dose | Schedule |
|------|------|----------|
| **Daratumumab (SC preferred)** | 1800 mg SC | Cycles 1-2: weekly; Cycles 3-4: q2wk; Maintenance: q4wk |
| **Bortezomib (SC)** | 1.3 mg/m² | Days 1, 4, 8, 11 (21-day cycles) |
| **Lenalidomide** | 25 mg PO | Days 1-21 |
| **Dexamethasone** | 20 mg (40 mg if >75) | Days 1, 2, 8, 9, 15, 16 (or 40mg weekly) |

### VRd (Standard for TE if Dara unavailable)

| Drug | Dose | Schedule |
|------|------|----------|
| **Bortezomib (SC)** | 1.3 mg/m² | Days 1, 4, 8, 11 |
| **Lenalidomide** | 25 mg PO | Days 1-21 |
| **Dexamethasone** | 40 mg PO | Days 1, 8, 15, 22 |

> [!warning] **Lenalidomide = Teratogenic (Category X)**. **Pregnancy prevention programme mandatory**. **Dose adjust for renal impairment** (eGFR <30: 15mg; <15: 5mg; dialysis: 5mg post-dialysis).

---

## 🌱 Autologous HSCT

| Aspect | Details |
|--------|---------|
| **Mobilisation** | **G-CSF 10 µg/kg/day** ± **Plerixafor 240 µg/kg** (if poor mobiliser) |
| **Conditioning** | **Melphalan 200 mg/m² (Mel 200)** single dose |
| **Timing** | After 4 cycles induction (deeper response → better PFS) |
| **Tandem Transplant** | **Not routinely recommended** (STaMINA, EMN02/HO95: no OS benefit) |
| **Post-HSCT Assessment** | Day 100: Response, MRD (NGS/Flow) |

---

## 💊 Maintenance Therapy

| Agent | Dose | Duration | Key Points |
|-------|------|----------|------------|
| **Lenalidomide** | 10-15 mg days 1-28 (adjust for renal) | **Until progression** | **Standard post-ASCT** (CALGB 100104, IFM 2005-02); **SPM risk ↑** (monitor) |
| **Dara-R / Dara-VRd** | Emerging | Clinical trials | PERSEUS: Dara-VRd maintenance improved PFS |

---

## 🔬 Response Assessment (IMWG Criteria)

| Response | Criteria |
|----------|----------|
| **sCR (Stringent CR)** | CR + **Normal FLC ratio** + **BM BMPC <5%** + **Normal imaging** |
| **CR** | Negative immunofixation (serum/urine) + **BM <5% BMPC** |
| **VGPR** | **M-protein ↓≥90%** + urine M-protein <100 mg/24h |
| **PR** | **Serum M-protein ↓≥50%** + urine M-protein ↓≥90% or <200 mg/24h |
| **MR (Minimal Response)** | ↓25-49% |
| **SD (Stable Disease)** | Not PR/PD |
| **PD (Progressive Disease)** | ↑25% from nadir (M-protein, FLC, BMPC) + absolute increase |

### MRD Assessment (Critical for Prognosis)

| Method | Sensitivity | Standard |
|--------|-------------|----------|
| **NGS (Clonotypic)** | **10⁻⁵ - 10⁻⁶** | **Preferred** (requires baseline diagnostic sample) |
| **Multiparameter Flow (MFC)** | **10⁻⁵** | Alternative (CD38, CD138, CD19, CD45, CD56, CD27, CD81) |
| **Imaging (PET-CT)** | Spatial | For extramedullary disease |

> [!tip] **MRD-negative (10⁻⁵ or 10⁻⁶) = Superior PFS/OS regardless of therapy**. **Sustained MRD-neg → consider treatment discontinuation trials**.

---

## ⚠️ Key Complications & Management

### Renal Impairment (eGFR <40 or Cr >177)
| Aspect | Management |
|--------|------------|
| **Drug Choice** | **Bortezomib-based (no dose adjust)**; **Avoid Lenalidomide** if eGFR <30 (dose adjust); **Carfilzomib** (no dose adjust) |
| **Hydration** | 3L/day IV/oral if possible |
| **Avoid** | NSAIDs, IV contrast (if possible), aminoglycosides, high-dose bisphosphonates |
| **Dialysis** | **Early if indicated**; High-cutoff dialysis for FLC removal (e.g., Myers cocktail) |
| **Plasma Exchange** | **Not routinely recommended** (MYRE trial: no benefit) |

### Bone Disease
| Agent | Dose | Monitoring |
|-------|------|------------|
| **Zoledronic Acid** | 4 mg IV monthly × 12-24mo, then q3mo | **Renal function pre-dose**; Dental exam (ONJ risk) |
| **Denosumab** | 120 mg SC monthly × 12-24mo, then q3mo | **Hypocalcaemia risk** (supplement Ca/VitD); **ONJ risk**; **No renal adjust** |

> [!warning] **ONJ (Osteonecrosis of Jaw)**: Dental exam pre-treatment; hold bisphosphonate/denosumab for dental surgery.

### Infection Prophylaxis
| Prophylaxis | Indication |
|-------------|------------|
| **Aciclovir 400mg BD** | All on bortezomib/carfilzomib/daratumumab (VZV reactivation) |
| **Co-trimoxazole** | If on high-dose steroids (≥20mg pred >4wks) or post-HSCT |
| **IVIG** | IgG <4 g/L + recurrent infections |
| **Vaccines** | **Inactivated only**: Flu, COVID, PCV20/PPSV23, HepB, **Shingrix (recombinant)** – **NO LIVE** |

### Peripheral Neuropathy (Bortezomib)
- **SC administration** (less than IV)
- **Dose reduce** (1.3 → 1.0 → 0.7 mg/m²) or **hold** for Grade ≥2
- **Switch to carfilzomib/ixazomib** if persistent

---

## 💥 Relapsed/Refractory Myeloma

| Setting | Preferred Regimens |
|---------|-------------------|
| **1st Relapse (Len-naïve)** | **Dara-VRd**, **KRd**, **Isa-VRd**, **Dara-Kd** |
| **Len-refractory** | **Dara-Kd**, **Isa-Kd**, **Dara-Pd**, **Elo-Pd** |
| **PI-refractory (Bortezomib)** | **Dara-Kd**, **Isa-Kd**, **Venetoclax (if t(11;14))** |
| **Double-refractory (PI + IMiD)** | **Dara-Pd**, **Isa-Pd**, **Belantamab (BCMA-ADC)**, **CAR-T (Idecabtagene, Ciltacabtagene)**, **Teclistamab (BCMA×CD3 BiTE)** |
| **Triple-refractory (PI + IMiD + anti-CD38)** | **CAR-T**, **BiTE**, **BCMA-ADC**, Clinical trials |

> [!tip] **TP53/del17p = High-risk = Consider CAR-T early**. **Venetoclax ONLY if t(11;14) (BCL-2 dependent)** – BELLINI trial showed harm in non-t(11;14).

---

## 🔄 Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **MGUS** | **<10% BMPC, M-spike <30g/L, NO CRAB/SLiM** |
| **Smouldering Myeloma** | **≥10% BMPC OR M-spike ≥30g/L, NO CRAB/SLiM** |
| **Waldenström Macroglobulinaemia** | **IgM κ/λ paraprotein**, **MYD88 L265P**, lymphoplasmacytic infiltrate, hyperviscosity |
| **AL Amyloidosis** | **Low BMPC** (<10%), **Organ involvement (heart, kidney, liver, nerve)**, **FLC elevation**, Congo red +ve |
| **POEMS Syndrome** | **Polyneuropathy, Organomegaly, Endocrinopathy, M-protein (λ), Castleman-like**; **VEGF ↑** |
| **Solitary Plasmacytoma** | Single lesion, **<10% BMPC**, no CRAB |
| **Monoclonal Gammopathy of Renal Significance (MGRS)** | Low tumour burden, **renal lesion from M-protein** (cast nephropathy, amyloidosis, MIDD) |

---

## 💡 FCPS/MRCP High-Yield Summary

| Topic | Key Point |
|-------|-----------|
| **Diagnosis** | **≥10% Clonal BMPC + ≥1 MDE (SLiM/CRAB)** |
| **SLiM** | **≥60% BMPC, FLC ratio ≥100, Lytic lesion (CT/PET)** |
| **CRAB** | **Ca >2.75, Renal Cr>177, Anaemia Hb<10, Bone lytic lesions** |
| **R-ISS** | **ISS + FISH (del17p, t(4;14), t(14;16)) + LDH** |
| **Imaging** | **WBLD-CT or PET-CT** (not skeletal survey) |
| **TE Induction** | **Dara-VRd (4 cycles) → Auto-HSCT (Mel 200) → Len maintenance** |
| **TIE Induction** | **Dara-Rd (preferred) or VRd-lite** |
| **Renal Failure** | **Bortezomib-based (no dose adjust)**; Avoid lenalidomide/NSAIDs |
| **Bone Disease** | **Zoledronic acid 4mg monthly × 1-2yr** or **Denosumab 120mg SC qmo** |
| **Maintenance** | **Lenalidomide until progression** post-ASCT |
| **MRD** | **NGS 10⁻⁵-10⁻⁶ (gold standard)**; MRD-neg = best prognosis |
| **Venetoclax** | **Only if t(11;14)** |
| **Relapse** | Dara-VRd, Dara-Kd, CAR-T, BiTE, BCMA-ADC per refractoriness |

---

## ❓ Viva Questions

1. **What are the SLiM criteria for myeloma diagnosis?**
   - **S**: ≥1 lytic lesion on CT/PET; **L**: BM plasma cells ≥60%; **iM**: Involved FLC/uninvolved FLC ratio ≥100 (absolute involved FLC ≥100 mg/L)

2. **How does R-ISS differ from ISS?**
   - **R-ISS = ISS + High-risk FISH (del17p, t(4;14), t(14;16)) + LDH**

3. **What is the standard induction for transplant-eligible myeloma?**
   - **Dara-VRd (Daratumumab + Bortezomib + Lenalidomide + Dex) × 4 cycles** → Auto-HSCT (Mel 200) → Len maintenance

4. **How do you manage myeloma with renal failure?**
   - **Bortezomib-based regimen (no dose adjust)**, avoid lenalidomide/NSAIDs/contrast, hydration, early dialysis if needed, **NO routine plasma exchange**

5. **What bisphosphonate regimen is used for myeloma bone disease?**
   - **Zoledronic acid 4 mg IV monthly × 12-24 months, then q3mo** (dental exam, renal check pre-dose); **Denosumab 120 mg SC monthly** alternative

6. **What is the response criteria for VGPR?**
   - **Serum M-protein ↓≥90%** + **Urine M-protein <100 mg/24h**

7. **When can you stop Lenalidomide maintenance?**
   - **Until progression** (standard); **Sustained MRD-neg for ≥2 years → trial discontinuation**

8. **What is the role of Venetoclax in myeloma?**
   - **Only for t(11;14) (BCL-2 dependent)** – BELLINI showed harm in non-t(11;14)

9. **How do you monitor MRD in myeloma?**
   - **NGS (clonotypic, 10⁻⁵-10⁻⁶) preferred**; **Multiparameter Flow (10⁻⁵)** alternative; requires baseline sample

10. **Differentiate MGUS, Smouldering Myeloma, and Active Myeloma.**
    - **MGUS**: <10% BMPC, M-spike <30g/L, NO CRAB/SLiM
    - **SMM**: ≥10% BMPC OR M-spike ≥30g/L, NO CRAB/SLiM
    - **Active Myeloma**: ≥10% BMPC + ≥1 MDE (SLiM/CRAB)

---

## 🧠 Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **SLiM vs CRAB** | **SLiM = biomarkers (asymptomatic)**; **CRAB = end-organ damage (symptomatic)** |
| **SMM vs Active Myeloma** | **SMM = NO MDE**; **Active = ≥1 MDE** |
| **ISS vs R-ISS** | **R-ISS = ISS + FISH + LDH** |
| **VRd vs Dara-VRd** | **Dara-VRd = Superior (GRIFFIN, PERSEUS); now standard for TE** |
| **Venetoclax in MM** | **Only t(11;14)**; contraindicated otherwise |
| **MRD 10⁻⁵ vs 10⁻⁶** | **10⁻⁵ = Flow standard**; **10⁻⁶ = NGS deep** |

| Mnemonic | Meaning |
|----------|---------|
| **"SLiM = Silent (biomarkers), CRAB = Clinical damage"** | MDE categories |
| **"R-ISS = ISS + FISH + LDH"** | Staging components |
| **"High-risk FISH = 17p, 4;14, 14;16"** | Adverse cytogenetics |
| **"Renal = Bortezomib (No adjust)"** | Drug choice in renal failure |
| **"Bone = Zol 4mg monthly → q3mo"** | Bisphosphonate schedule |
| **"t(11;14) = Venetoclax (Ven)"** | Venetoclax indication |
| **"Len = Maintenance till progression"** | Post-ASCT maintenance |

---

## 🗺️ Mind Map

```mermaid
mindmap
  root((Multiple Myeloma))
    Diagnosis
      ≥10% Clonal BMPC
      + 1 MDE (SLiM/CRAB)
    MDE
      SLiM: ≥60% BMPC, FLC≥100, Lytic lesion
      CRAB: Ca, Renal, Anaemia, Bone
    Staging
      R-ISS = ISS + FISH + LDH
      High-risk FISH: del17p, t(4;14), t(14;16)
    Imaging
      WBLD-CT / PET-CT
    TE Induction
      Dara-VRd × 4
      → Auto-HSCT (Mel 200)
      → Len maintenance
    TIE Induction
      Dara-Rd (preferred)
      VRd-lite / Rd
    Renal Failure
      Bortezomib-based
      No len/NSAIDs
    Bone Disease
      Zol 4mg monthly ×1-2y → q3mo
      Denosumab 120mg SC qmo
    Maintenance
      Lenalidomide till progression
    MRD
      NGS 10⁻⁵-10⁻⁶ (preferred)
      Flow 10⁻⁵
    Relapse
      1st: Dara-VRd, KRd
      Len-ref: Dara-Kd
      PI-ref: Dara-Kd
      Double: Dara-Pd, CAR-T, BiTE
    Venetoclax
      ONLY t(11;14)
```

---

## 📋 One-Page Revision Card

| **MULTIPLE MYELOMA – FCPS/MRCP REVISION CARD** |
|------------------------------------------------|
| **Diagnosis**: **≥10% clonal BMPC + ≥1 MDE (SLiM/CRAB)** |
| **SLiM**: BMPC≥60%, FLC ratio≥100, Lytic lesion (CT/PET) |
| **CRAB**: Ca>2.75, Renal Cr>177, Anaemia Hb<10, Bone lytic |
| **R-ISS**: ISS + **High-risk FISH (del17p, t(4;14), t(14;16))** + LDH |
| **Imaging**: **WBLD-CT or PET-CT** (no skeletal survey) |
| **TE**: **Dara-VRd ×4 → Auto-HSCT (Mel 200) → Len maint** |
| **TIE**: **Dara-Rd preferred** or VRd-lite |
| **Renal**: **Bortezomib-based (no dose adjust)** |
| **Bone**: **Zol 4mg monthly ×1-2y → q3mo** (dental, renal check) |
| **Maintenance**: **Lenalidomide till progression** |
| **MRD**: **NGS 10⁻⁵-10⁻⁶ (gold)**; MRD-neg = best prognosis |
| **Venetoclax**: **ONLY t(11;14)** |
| **Relapse**: Dara-Kd, Dara-Pd, CAR-T, BiTE, BCMA-ADC |

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
| **Must Know** | SLiM/CRAB criteria, R-ISS staging, Dara-VRd induction for TE, Dara-Rd for TIE, Auto-HSCT (Mel 200), Len maintenance, renal management (bortezomib), bisphosphonate schedule, MRD methods (NGS/Flow), venetoclax only t(11;14), relapse algorithm |
| **Should Know** | ISS vs R-ISS details, high-risk FISH specifics, lenalidomide renal dosing, daratumumab SC vs IV, carfilzomib vs bortezomib, denosumab vs zoledronic acid, MRD-guided discontinuation trials, SPM risk with len maintenance, Plerixafor mobilisation, melphalan dose reduction for elderly/renal |
| **Nice to Know** | Detailed IMWG response criteria (sCR/CR/VGPR/PR/MR/SD/PD), specific clinical trial data (GRIFFIN, PERSEUS, MAIA, SWOG S0777, CALGB 100104, IFM 2005-02, BELLINI, CARTITUDE, KarMMa), bispecific antibodies (teclistamab, talquetamab), BCMA CAR-T (ide-cel, cilta-cel), ADC (belantamab), quad induction (Dara-VRd, Isa-VRd), MGRS (monoclonal gammopathy of renal significance) |

---

## ✅ Self-Test Scorecard

| Section | Score (0-10) | Notes |
|---------|--------------|-------|
| Diagnostic Criteria (SLiM/CRAB) | | |
| Staging (R-ISS) | | |
| TE Induction & Transplant | | |
| TIE Induction | | |
| Renal Management | | |
| Bone Disease & Bisphosphonates | | |
| Maintenance Therapy | | |
| MRD Monitoring | | |
| Relapsed/Refractory Algorithm | | |
| Viva Questions | | |

---

## 🔗 Local Navigation

- **Previous**: [[Chronic Lymphocytic Leukaemia (CLL)]]
- **Next**: [[Non-Hodgkin Lymphoma Subtypes]]
- **Section Hub**: [[Haematological Malignancies]]
- **MOC**: [[Hematology MOC]]
- **Template**: [[../Templates/Hematology Topic Template]]

---

*Generated for FCPS/MRCP exam preparation. Based on Davidson Medicine 24th Ed Chapter 25.*