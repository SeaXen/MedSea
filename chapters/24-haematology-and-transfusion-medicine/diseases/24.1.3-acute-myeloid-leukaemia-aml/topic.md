---
tags: [medicine, davidson, hematology, aml, acute-leukaemia, fcps, mrcp]
davidson_chapter: Chapter 25: Haematology and Transfusion Medicine
status: full-fcps-mrcp-note
priority: high
exam_relevance: "FCPS: Essential | MRCP: Core | High-yield for vivas, cytogenetics, management algorithms"
see_also: "[[Acute Promyelocytic Leukaemia (APML)]], [[Acute Lymphoblastic Leukaemia (ALL)]], [[MDS]], [[Stem Cell Transplantation]], [[Mixed Lineage Leukaemia]]"
created: 2025-06-15
modified: 2025-06-15
---

# Acute Myeloid Leukaemia (AML)

> [!info] **Davidson Ch 25 Alignment**: Haematological Malignancies → Acute Leukaemias → AML
> **FCPS/MRCP Focus**: WHO 2022/ICC classification, cytogenetic/molecular risk stratification, "7+3" induction, consolidation, HSCT indications, APML specific protocol

---

## 🎯 Learning Objectives

- [ ] Define AML: ≥20% blasts in BM/PB (or defining genetic abnormalities)
- [ ] Classify per WHO 2022 / ICC: AML with defining genetic abnormalities, AML with myelodysplasia-related changes, therapy-related AML, AML NOS
- [ ] Apply **ELN 2022 risk stratification** (Favourable/Intermediate/Adverse) using cytogenetics + molecular markers
- [ ] Diagnose: CBC, BM aspirate/biopsy, flow cytometry (CD34, CD117, MPO, CD13, CD33, lineage markers), cytogenetics, NGS panel
- [ ] Manage **induction**: "7+3" (Cytarabine + Anthracycline) ± Midostaurin (FLT3mut), ± Gemtuzumab (CD33+), ± Venetoclax (unfit)
- [ ] Manage **APML separately**: ATRA + Arsenic trioxide (+ anthracycline)
- [ ] Define **consolidation**: HiDAC vs HSCT based on risk/response
- [ ] Monitor **MRD**: Multiparameter flow, NGS, RT-qPCR (e.g., NPM1, CBF fusions)
- [ ] Manage complications: TLS, differentiation syndrome (APML), infections, bleeding
- [ ] Understand salvage/relapsed therapy: FLAG-IDA, CPX-351, Venetoclax combinations, targeted agents

---

## 📖 Definition & Classification

### WHO 2022 / ICC Classification – Key Categories

| Category | Defining Features | Examples |
|----------|-------------------|----------|
| **AML with defining genetic abnormalities** | Specific recurrent translocations/mutations | t(8;21), inv(16), t(15;17), t(9;11), NPM1mut, CEBPAmut, FLT3-ITD, KMT2Ar |
| **AML with myelodysplasia-related changes (AML-MRC)** | Prior MDS, MDS cytogenetics, multilineage dysplasia | Complex karyotype, -5/del5q, -7/del7q |
| **Therapy-related AML (t-AML)** | Prior chemo/radiotherapy | Alkylator-related (-5/-7, 5-7y), Topo II inhibitor-related (11q23/KMT2Ar, 1-3y) |
| **AML, not otherwise specified (AML-NOS)** | No defining features, ≥20% blasts | AML with minimal differentiation, without maturation, with maturation, myelomonocytic, monoblastic, erythroid, megakaryoblastic |

> [!tip] **FCPS/MRCP**: **AML diagnosis = ≥20% blasts** EXCEPT: t(8;21), inv(16), t(15;17), t(9;11), NPM1mut, CEBPAbiallelic, RBM15::MKL1 – these diagnose AML **regardless of blast %**

---

## ⚙️ Pathophysiology

```mermaid
flowchart TD
    A[HSC/Progenitor Mutations] --> B[Class I: Proliferation/Survival]
    A --> C[Class II: Differentiation Block]
    B & C --> D[Leukaemic Stem Cell (LSC)]
    D --> E[Clonal Expansion]
    E --> F[Blast Accumulation ≥20%]
    F --> G[Marrow Failure: Anaemia, Neutropenia, Thrombocytopenia]
    F --> H[Extramedullary: Gingival hypertrophy, Skin, CNS, Chloroma]
```

| Mutation Class | Examples | Effect |
|----------------|----------|--------|
| **Class I (Proliferation)** | FLT3-ITD/TKD, KIT, RAS, JAK2, FGFR | Constitutive signalling → survival/proliferation |
| **Class II (Differentiation Block)** | RUNX1::RUNX1T1 (t(8;21)), CBFB::MYH11 (inv16), PML::RARA (t(15;17)), NPM1, CEBPA, KMT2A-fusions | Block myeloid differentiation |
| **Epigenetic/Other** | DNMT3A, TET2, ASXL1, IDH1/2, TP53, WT1, SRSF2, U2AF1, Cohesin (STAG2, RAD21) | Age-related clonal haematopoiesis (CHIP), prognosis |

---

## 🔬 Diagnostic Workup

```mermaid
flowchart TD
    A[Suspected AML: Blasts on PB or Pancytopenia] --> B[CBC + Film: Blasts, Auer rods?]
    B --> C[BM Aspirate + Biopsy]
    C --> D[Flow Cytometry: CD34, CD117, MPO, CD13, CD33, CD14, CD64, CD11b, CD41, CD61, Glycophorin A, CD19, CD7, TdT]
    C --> E[Cytogenetics: Karyotype + FISH panel]
    C --> F[Molecular: NGS Panel (FLT3, NPM1, CEBPA, IDH1/2, DNMT3A, TP53, etc.)]
    C --> G[Immunophenotype: MPO+, CD117+, CD34+, HLA-DR+ (except APML)]
    D & E & F --> G[WHO/ICC Classification + ELN 2022 Risk]
    G --> H[CNS Assessment: LP if WBC>50 or neuro symptoms]
    G --> I[Baseline: Echo, LFT, Renal, Coagulation, Viral Screen, HLA Typing]
```

### Essential Diagnostic Panel

| Test | Purpose |
|------|---------|
| **BM Aspirate** | Blast %, morphology, Auer rods, flow cytometry |
| **BM Biopsy** | Cellularity, fibrosis, infiltration pattern |
| **Flow Cytometry** | Lineage assignment (MPO for myeloid), CD34, CD117, aberrant markers |
| **Cytogenetics (Karyotype)** | **Mandatory**: t(8;21), inv(16), t(15;17), -5, -7, complex, monosomal |
| **NGS Molecular Panel** | **Mandatory**: FLT3-ITD/TKD (allelic ratio), NPM1, CEBPA, IDH1/2, DNMT3A, TP53, KIT, WT1, RAS, splicing factors |
| **FISH** | Rapid detection of CBF fusions, PML::RARA, KMT2A |
| **LP + CSF Flow** | If WBC >50×10⁹/L or neurological symptoms |

---

## 📊 ELN 2022 Risk Stratification (Standard for Treatment Decisions)

| Risk | Genetic Features | CR Rate | 5-yr OS | Post-Remission |
|------|------------------|---------|---------|----------------|
| **Favourable** | t(8;21)(RUNX1::RUNX1T1), inv(16)(CBFB::MYH11), **NPM1mut without FLT3-ITD** (or low AR <0.5), **CEBPAbiallelic** | 80-90% | 60-70% | **Consolidation: HiDAC × 3-4 cycles** (HSCT in CR1 controversial) |
| **Intermediate** | NPM1mut with FLT3-ITDhigh (AR ≥0.5), WT1mut, DNMT3Amut, IDH1/2mut, t(9;11), other KMT2A-r, normal karyotype | 60-70% | 40-50% | **HSCT in CR1 preferred** (if donor, fit); HiDAC if no donor |
| **Adverse** | **TP53mut**, **complex karyotype (≥3 abn)**, **monosomal karyotype**, -5/del5q, -7/del7q, inv3/t(3;3), KMT2A-r (non-t(9;11)), FLT3-ITDhigh with adverse cytogenetics, ASXL1mut, RUNX1mut, U2AF1mut | 30-40% | <20% | **Allo-HSCT in CR1 mandatory** (if fit); Clinical trial; CPX-351, Venetoclax+Aza |

> [!warning] **Key ELN 2022 Changes**: NPM1mut/FLT3-ITDlow = Favourable; TP53mut = Adverse regardless of karyotype; complex karyotype = Adverse; monosomal karyotype = Adverse

---

## 💊 Management

### Induction Therapy ("7+3" Backbone)

| Regimen | Components | Indication |
|---------|------------|------------|
| **Standard "7+3"** | **Cytarabine 100-200 mg/m²/day CI × 7 days + Daunorubicin 60-90 mg/m²/day × 3 days** (or Idarubicin 12 mg/m² × 3) | **Fit patients <60-65y** (90mg dauno if <60) |
| **"7+3" + Midostaurin** | Add **Midostaurin 50 mg BD days 8-21** | **FLT3mut (ITD or TKD)** – RATIFY trial |
| **"7+3" + Gemtuzumab Ozogamicin** | Add **GO 3 mg/m² day 1, 4, 7** (fractionated) | **CD33+ AML** (AML-19, ALFA-0701) – favourable/intermediate |
| **CPX-351 (Liposomal Cytarabine:Daunorubicin 5:1)** | Fixed 5:1 molar ratio, days 1,3,5 + 8,10 | **t-AML, AML-MRC, age 60-75** – better CR/OS vs 7+3 |
| **Venetoclax + Azacitidine/Decitabine** | Ven 400mg days 1-28 + Aza 75mg/m² days 1-7 (28d cycle) | **Unfit/≥75y, comorbidities** – VIALE-A trial |
| **Venetoclax + Low-dose Cytarabine** | Ven 600mg days 1-28 + LDAC 20mg SC days 1-10 | **Unfit** – alternative to Ven+Aza |

> [!tip] **FCPS/MRCP**: **"7+3" = Cytarabine 7 days + Anthracycline 3 days**. **Daunorubicin 90 mg/m²** if <60y (better than 60). **Midostaurin for FLT3mut**. **GO fractionated for CD33+**. **CPX-351 for t-AML/AML-MRC**. **Venetoclax+HMA for unfit**.

### APML (t(15;17)) – Separate Protocol
| Phase | Regimen | Key Points |
|-------|---------|------------|
| **Induction** | **ATRA 45 mg/m²/day + Arsenic Trioxide (ATO) 0.15 mg/kg/day** (or + Idarubicin) | **ATRA syndrome prophylaxis: Dex 10mg BD if WBC>10 or rising**; monitor coagulation |
| **Consolidation** | ATRA + ATO (or ATRA + Chemo) | 4 cycles total |
| **Maintenance** | ATRA (2yr) ± 6-MP/Methotrexate | Low relapse risk |

### Consolidation (Post-CR1)

| Risk | Preferred | Alternative |
|------|-----------|-------------|
| **Favourable** | **HiDAC 3-4 g/m² q12h × 3-4 cycles** | HSCT if molecular persistence |
| **Intermediate** | **Allo-HSCT in CR1** (if donor, fit) | HiDAC × 3-4 cycles if no donor |
| **Adverse** | **Allo-HSCT in CR1** (mandatory if fit) | Clinical trial / CPX-351 / Ven+Aza |

**HiDAC Regimen**: Cytarabine 3 g/m² q12h IV × 3 days (days 1,3,5) = 1 cycle; repeat q3-4wk × 3-4 cycles. **Neurotoxicity risk** (cerebellar) – dose reduce if age >60 or renal impairment.

---

## 🔬 Monitoring: MRD & Response Assessment

| Timepoint | Assessment | MRD Methods |
|-----------|------------|-------------|
| **Day 14-21** | Early blast clearance (morphology) | Flow if persistent blasts |
| **End of Induction (Day 28-35)** | **CR/CRi/MLFS/PR/NR** | **Flow MRD (sensitivity 10⁻⁴), NGS (10⁻⁴-10⁻⁵), RT-qPCR** (NPM1, CBF fusions) |
| **Post-Consolidation** | CR + MRD status | MRD-guided HSCT decision |
| **Post-HSCT** | q3mo × 2yr, then q6mo | Flow + NGS; pre-emptive intervention if molecular relapse |

### Response Criteria (ELN/IWG)

| Category | Definition |
|----------|------------|
| **CR** | BM blasts <5%, ANC≥1.0, Plt≥100, no extramedullary disease |
| **CRi** | CR + incomplete count recovery (ANC<1 or Plt<100) |
| **MLFS** | BM blasts 5-19% or <5% with cytopenia |
| **PR** | ≥50% blast reduction but >5% blasts |
| **NR** | Failure to achieve PR |

---

## ⚠️ Complications & Supportive Care

| Complication | Prevention / Management |
|--------------|--------------------------|
| **Tumour Lysis Syndrome (TLS)** | **Allopurinol** (prophylaxis), **Rasburicase** (high risk: WBC>50, high LDH, renal impairment); Hydration 3L/day, monitor K/PO₄/UA/Ca |
| **Febrile Neutropenia** | **Piperacillin-tazobactam** or **Meropenem** empirical; add **Vancomycin** if catheter/skin/hemodynamic instability; **Posaconazole** prophylaxis (mould) |
| **Bleeding** | Platelet threshold **<10** prophylactic; **<20** if fever/sepsis; **<50** for procedures; **Irradiated, HLA-matched if refractory** |
| **DIC** | Common in APML; treat underlying + replace fibrinogen/cryo/platelets |
| **ATRA Syndrome** (APML) | **Dex 10mg BD** if WBC>10 or rising; pulmonary infiltrates, fever, weight gain, hypotension |
| **Differentiation Syndrome** (IDH inhibitors, Venetoclax) | Similar to ATRA syndrome; steroids |
| **CNS Leukaemia** | Prophylaxis: Intrathecal MTX/Ara-C (induction/consolidation); High-dose systemic (HiDAC) |

---

## 🌱 Relapsed/Refractory AML

| Setting | Options |
|---------|---------|
| **Early Relapse (<6mo) / Primary Refractory** | **FLAG-IDA** (Fludarabine + Cytarabine + G-CSF + Idarubicin), **CPX-351**, **Venetoclax + Aza/LDAC**, Clinical trial |
| **Late Relapse (>6mo)** | Re-induction with original regimen if favourable risk; otherwise as above |
| **Targeted Therapy** | **Midostaurin/Gilteritinib** (FLT3mut), **Ivosidenib** (IDH1mut), **Enasidenib** (IDH2mut), **Gemtuzumab** (CD33+), **CPX-351** |
| **Bridge to HSCT** | Achieve CR/CRi → proceed to Allo-HSCT (RIC if older/comorbidities) |

---

## 🔄 Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **ALL** | **TdT+, CD19+, CD10+ (B-ALL) or CD7+, CD3+ (T-ALL)**; MPO negative; different cytogenetics |
| **APML (AML-M3)** | **Promyelocytes with Auer rods**, t(15;17), PML::RARA, **DIC**, **ATRA syndrome risk** |
| **MDS with Excess Blasts (MDS-EB2)** | **Blasts 10-19%**, dysplasia, cytopenias, MDS cytogenetics |
| **Blastic Plasmacytoid DC Neoplasm** | **CD123+, CD56+, CD4+, MPO-, TCL1+**; skin involvement common |
| **Myeloid Sarcoma (Chloroma)** | Extramedullary mass, MPO+, CD117+, no systemic blasts initially |

---

## 💡 FCPS/MRCP High-Yield Summary

| Topic | Key Point |
|-------|-----------|
| **AML Definition** | **≥20% blasts** (except defining genetic abnormalities: t(8;21), inv16, t(15;17), t(9;11), NPM1mut, CEBPAbiallelic) |
| **Induction** | **"7+3": Ara-C 100-200 mg/m² CI ×7d + Dauno 90 mg/m² ×3d** (if <60y) |
| **FLT3mut** | Add **Midostaurin** days 8-21 (RATIFY) |
| **CD33+** | Add **Gemtuzumab** fractionated days 1,4,7 |
| **Unfit/≥75y** | **Venetoclax + Azacitidine** (VIALE-A) |
| **t-AML/AML-MRC** | **CPX-351** (liposomal 5:1) |
| **APML** | **ATRA + ATO** (not 7+3); **Dex if WBC>10**; monitor DIC |
| **Risk Stratification** | **ELN 2022**: Favourable (t(8;21), inv16, NPM1mut/FLT3-ITDlow, CEBPAbiallelic), Adverse (TP53, complex/monosomy, -5/-7) |
| **Consolidation** | Favourable: **HiDAC ×3-4**; Intermediate/Adverse: **Allo-HSCT in CR1** |
| **MRD** | **Flow (10⁻⁴), NGS (10⁻⁵), RT-qPCR (NPM1, CBF)** |
| **TLS Prophylaxis** | **Allopurinol** (all); **Rasburicase** if high risk (WBC>50, high LDH) |
| **Febrile Neutropenia** | **Pip-Tazo or Meropenem** empirical; **Posaconazole** mould prophylaxis |

---

## ❓ Viva Questions

1. **What is the blast threshold for AML diagnosis and what are the exceptions?**
   - ≥20% blasts in BM/PB; exceptions: t(8;21), inv(16), t(15;17), t(9;11), NPM1mut, CEBPAbiallelic, RBM15::MKL1 – diagnose AML regardless of blast count

2. **Describe the "7+3" induction regimen for AML.**
   - Cytarabine 100-200 mg/m²/day continuous infusion ×7 days + Daunorubicin 90 mg/m²/day ×3 days (or Idarubicin 12 mg/m² ×3)

3. **When do you add Midostaurin to induction?**
   - **FLT3 mutation (ITD or TKD)** – given days 8-21 with 7+3 (RATIFY trial)

4. **What is the ELN 2022 favourable risk group?**
   - t(8;21), inv(16), **NPM1mut without FLT3-ITD (or AR<0.5)**, **CEBPAbiallelic**

5. **What is the consolidation strategy for favourable risk AML?**
   - **HiDAC 3-4 g/m² q12h × 3-4 cycles** (HSCT in CR1 not routinely recommended)

6. **How is APML (t(15;17)) managed differently?**
   - **ATRA + Arsenic Trioxide** (not 7+3); **Dexamethasone prophylaxis if WBC>10**; monitor/treat DIC

7. **What are the indications for Allo-HSCT in CR1?**
   - **Intermediate/Adverse risk** (ELN 2022); **MRD-positive CR1**; Refractory/relapsed disease

8. **How do you monitor MRD in AML?**
   - **Multiparameter flow (10⁻⁴), NGS panel (10⁻⁴-10⁻⁵), RT-qPCR for NPM1/CBF fusions**

9. **What is the management of Tumour Lysis Syndrome prophylaxis?**
   - **Allopurinol** for all; **Rasburicase** if high risk (WBC>50×10⁹/L, LDH>2xULN, renal impairment, bulky disease)

10. **Differentiate AML from ALL on flow cytometry.**
    - **AML: MPO+, CD117+, CD34+, CD13, CD33, HLA-DR+**; **ALL: TdT+, CD19/CD10 (B-ALL) or CD7/CD3 (T-ALL), MPO-**

---

## 🧠 Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **AML vs ALL flow** | **AML = MPO+ (myeloid)**; **ALL = TdT+ (lymphoid)** |
| **NPM1mut + FLT3-ITD low AR** | **Favourable** (ELN 2022: AR<0.5 = favourable) |
| **NPM1mut + FLT3-ITD high AR** | **Intermediate** (AR≥0.5) |
| **t-AML vs AML-MRC** | t-AML: **prior chemo/radiotherapy**; AML-MRC: **prior MDS/MDS cytogenetics/dysplasia** |
| **CPX-351 vs 7+3** | CPX-351 = **liposomal fixed 5:1 ratio**; for t-AML/AML-MRC/age 60-75 |
| **Venetoclax combinations** | **Ven+Aza** (standard unfit); **Ven+LDAC** (alternative) |

| Mnemonic | Meaning |
|----------|---------|
| **"7+3 = 7 days Ara-C, 3 days Dauno"** | Induction backbone |
| **"FLT3mut = Midostaurin add-on"** | RATIFY trial |
| **"ELN Fav = t(8;21), inv16, NPM1/FLT3low, CEBPAbi"** | Favourable risk |
| **"ELN Adv = TP53, Complex, Mono, -5/-7"** | Adverse risk |
| **"APML = ATRA + ATO, NO 7+3"** | Unique protocol |
| **"HiDAC = 3g/m² q12h × 3d × 3-4 cycles"** | Favourable consolidation |
| **"TLS: Allo for all, Rasburi for high"** | Tumour lysis prophylaxis |

---

## 🗺️ Mind Map

```mermaid
mindmap
  root((Acute Myeloid Leukaemia))
    Definition
      ≥20% blasts
      Exceptions: Genetic AML
    Classification (WHO/ICC)
      Defining Genetic Abnormalities
      AML-MRC
      Therapy-related
      NOS
    Diagnosis
      BM: Morphology + Flow (MPO+)
      Cytogenetics (Karyotype + FISH)
      NGS Panel (FLT3, NPM1, CEBPA, TP53...)
    Risk (ELN 2022)
      Favourable: t(8;21), inv16, NPM1/FLT3low, CEBPAbi
      Intermediate: NPM1/FLT3high, normal karyotype
      Adverse: TP53, Complex, Mono, -5/-7
    Induction
      7+3 (Ara-C + Dauno 90)
      + Midostaurin (FLT3mut)
      + GO (CD33+)
      Unfit: Ven+Aza / CPX-351
    APML (Separate)
      ATRA + ATO
      Dex if WBC>10
    Consolidation
      Favourable: HiDAC ×3-4
      Int/Adv: Allo-HSCT CR1
    MRD
      Flow, NGS, RT-qPCR
    Complications
      TLS, Febrile Neutropenia, Bleeding, DIC
    Relapse
      FLAG-IDA, CPX-351, Targeted, Bridge to HSCT
```

---

## 📋 One-Page Revision Card

| **AML – FCPS/MRCP REVISION CARD** |
|-----------------------------------|
| **Diagnosis**: ≥20% blasts (except t(8;21), inv16, t(15;17), t(9;11), NPM1mut, CEBPAbiallelic) |
| **Induction**: **7+3** = Ara-C 100-200 CI ×7d + **Dauno 90 ×3d** (<60y) |
| **FLT3mut**: Add **Midostaurin** days 8-21 |
| **CD33+**: Add **Gemtuzumab** fractionated |
| **Unfit/≥75y**: **Venetoclax + Azacitidine** |
| **t-AML/AML-MRC**: **CPX-351** |
| **APML**: **ATRA + ATO** (NO 7+3); **Dex if WBC>10** |
| **Risk (ELN 2022)**: Fav (t8;21, inv16, NPM1/FLT3low, CEBPAbi); Adv (TP53, Complex, Mono, -5/-7) |
| **Consolidation**: Fav → **HiDAC ×3-4**; Int/Adv → **Allo-HSCT CR1** |
| **MRD**: Flow (10⁻⁴), NGS (10⁻⁵), qPCR (NPM1, CBF) |
| **TLS**: Allopurinol all; Rasburicase if WBC>50/high LDH |
| **Febrile Neutropenia**: Pip-Tazo/Meropenem + Posaconazole |

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
| **Must Know** | AML definition/exceptions, 7+3 regimen (doses), FLT3/Midostaurin, APML protocol, ELN 2022 risk groups, consolidation strategy, MRD methods, TLS prophylaxis, febrile neutropenia management |
| **Should Know** | CPX-351 indication, Venetoclax combinations, ELN 2022 specifics (NPM1/FLT3 AR), GO fractionated dosing, HiDAC neurotoxicity, FLAG-IDA salvage, differentiation syndrome |
| **Nice to Know** | Detailed NGS mutation prognostic impact (DNMT3A, IDH1/2, ASXL1, RUNX1, splicing factors), specific clinical trial data (RATIFY, VIALE-A, AML-19), CAR-T/immunotherapy in AML, measurable residual disease kinetics |

---

## ✅ Self-Test Scorecard

| Section | Score (0-10) | Notes |
|---------|--------------|-------|
| Definition & Classification | | |
| Diagnostic Workup | | |
| ELN 2022 Risk Stratification | | |
| Induction Regimens | | |
| APML Specific Protocol | | |
| Consolidation Strategy | | |
| MRD Monitoring | | |
| Complications & Supportive Care | | |
| Relapsed/Refractory Management | | |
| Viva Questions | | |

---

## 🔗 Local Navigation

- **Previous**: [[Aplastic Anaemia]]
- **Next**: [[Acute Lymphoblastic Leukaemia (ALL)]]
- **Section Hub**: [[Haematological Malignancies]]
- **MOC**: [[Hematology MOC]]
- **Template**: [[../Templates/Hematology Topic Template]]

---

*Generated for FCPS/MRCP exam preparation. Based on Davidson Medicine 24th Ed Chapter 25.*
---

> Auto-generated study sections for "Hematology" — Ch 24: Haematology & Transfusion Medicine.

## Flashcards (40 generated)

- Q: What is BM Aspirate of Hematology?
  A: Blast %, morphology, Auer rods, flow cytometry
- Q: What is BM Biopsy of Hematology?
  A: Cellularity, fibrosis, infiltration pattern
- Q: What is Flow Cytometry of Hematology?
  A: Lineage assignment (MPO for myeloid), CD34, CD117, aberrant markers
- Q: How is Hematology classified?
  A: Mandatory: t(8;21), inv(16), t(15;17), -5, -7, complex, monosomal
- Q: What is NGS Molecular Panel of Hematology?
  A: Mandatory: FLT3-ITD/TKD (allelic ratio), NPM1, CEBPA, IDH1/2, DNMT3A, TP53, KIT, WT1, RAS, splicing factors
- Q: What is FISH of Hematology?
  A: Rapid detection of CBF fusions, PML::RARA, KMT2A
- Q: What is LP + CSF Flow of Hematology?
  A: If WBC >50×10⁹/L or neurological symptoms
- Q: What is Tumour Lysis Syndrome (TLS) of Hematology?
  A: Allopurinol (prophylaxis), Rasburicase (high risk: WBC>50, high LDH, renal impairment); Hydration 3L/day, monitor K/PO₄/UA/Ca
- Q: What is Febrile Neutropenia of Hematology?
  A: Piperacillin-tazobactam or Meropenem empirical; add Vancomycin if catheter/skin/hemodynamic instability; Posaconazole prophylaxis (mould)
- Q: What is Bleeding of Hematology?
  A: Platelet threshold <10 prophylactic; <20 if fever/sepsis; <50 for procedures; Irradiated, HLA-matched if refractory
- Q: What is DIC of Hematology?
  A: Common in APML; treat underlying + replace fibrinogen/cryo/platelets
- Q: What is ATRA Syndrome (APML) of Hematology?
  A: Dex 10mg BD if WBC>10 or rising; pulmonary infiltrates, fever, weight gain, hypotension
- Q: What is Differentiation Syndrome (IDH inhibitors, Venetoclax) of Hematology?
  A: Similar to ATRA syndrome; steroids
- Q: What is CNS Leukaemia of Hematology?
  A: Prophylaxis: Intrathecal MTX/Ara-C (induction/consolidation); High-dose systemic (HiDAC)
- Q: What is BM Aspirate of Hematology?
  A: Blast %, morphology, Auer rods, flow cytometry
- Q: What is BM Biopsy of Hematology?
  A: Cellularity, fibrosis, infiltration pattern
- Q: What is Flow Cytometry of Hematology?
  A: Lineage assignment (MPO for myeloid), CD34, CD117, aberrant markers
- Q: How is Hematology classified?
  A: Mandatory: t(8;21), inv(16), t(15;17), -5, -7, complex, monosomal
- Q: What is NGS Molecular Panel of Hematology?
  A: Mandatory: FLT3-ITD/TKD (allelic ratio), NPM1, CEBPA, IDH1/2, DNMT3A, TP53, KIT, WT1, RAS, splicing factors
- Q: What is FISH of Hematology?
  A: Rapid detection of CBF fusions, PML::RARA, KMT2A
- Q: What is LP + CSF Flow of Hematology?
  A: If WBC >50×10⁹/L or neurological symptoms
- Q: What is Tumour Lysis Syndrome (TLS) of Hematology?
  A: Allopurinol (prophylaxis), Rasburicase (high risk: WBC>50, high LDH, renal impairment); Hydration 3L/day, monitor K/PO₄/UA/Ca
- Q: What is Febrile Neutropenia of Hematology?
  A: Piperacillin-tazobactam or Meropenem empirical; add Vancomycin if catheter/skin/hemodynamic instability; Posaconazole prophylaxis (mould)
- Q: What is Bleeding of Hematology?
  A: Platelet threshold <10 prophylactic; <20 if fever/sepsis; <50 for procedures; Irradiated, HLA-matched if refractory
- Q: What is DIC of Hematology?
  A: Common in APML; treat underlying + replace fibrinogen/cryo/platelets
- Q: What is ATRA Syndrome (APML) of Hematology?
  A: Dex 10mg BD if WBC>10 or rising; pulmonary infiltrates, fever, weight gain, hypotension
- Q: What is Differentiation Syndrome (IDH inhibitors, Venetoclax) of Hematology?
  A: Similar to ATRA syndrome; steroids
- Q: What is CNS Leukaemia of Hematology?
  A: Prophylaxis: Intrathecal MTX/Ara-C (induction/consolidation); High-dose systemic (HiDAC)
- Q: What is the definition of Hematology?
  A: ≥20% blasts (except defining genetic abnormalities: t(8;21), inv16, t(15;17), t(9;11), NPM1mut, CEBPAbiallelic)
- Q: What is Induction of Hematology?
  A: "7+3": Ara-C 100-200 mg/m² CI ×7d + Dauno 90 mg/m² ×3d (if <60y)
- Q: What is FLT3mut of Hematology?
  A: Add Midostaurin days 8-21 (RATIFY)
- Q: What is CD33+ of Hematology?
  A: Add Gemtuzumab fractionated days 1,4,7
- Q: What is Unfit/≥75y of Hematology?
  A: Venetoclax + Azacitidine (VIALE-A)
- Q: What is t-AML/AML-MRC of Hematology?
  A: CPX-351 (liposomal 5:1)
- Q: What is APML of Hematology?
  A: ATRA + ATO (not 7+3); Dex if WBC>10; monitor DIC
- Q: What is Risk Stratification of Hematology?
  A: ELN 2022: Favourable (t(8;21), inv16, NPM1mut/FLT3-ITDlow, CEBPAbiallelic), Adverse (TP53, complex/monosomy, -5/-7)
- Q: What is Consolidation of Hematology?
  A: Favourable: HiDAC ×3-4; Intermediate/Adverse: Allo-HSCT in CR1
- Q: What is MRD of Hematology?
  A: Flow (10⁻⁴), NGS (10⁻⁵), RT-qPCR (NPM1, CBF)
- Q: What is TLS Prophylaxis of Hematology?
  A: Allopurinol (all); Rasburicase if high risk (WBC>50, high LDH)
- Q: What is Febrile Neutropenia of Hematology?
  A: Pip-Tazo or Meropenem empirical; Posaconazole mould prophylaxis

## MCQs (1 generated)

1. **Which of the following best describes Hematology?**
   A. **[!info] Davidson Ch 25 Alignment: Haematological Malignancies → Acute Leukaemias → AML**
   B. An unrelated condition not matching the clinical picture of Hematology
   C. A complication seen late in the disease course of Hematology
   D. A condition that mimics Hematology but has a different underlying cause

## SBA Questions (1 generated)

1. A patient with suspected Hematology presents with: Category — Defining Features; AML with defining genetic abnormalities — Specific recurrent translocations/mutations; AML with myelodysplasia-related changes (AML-MRC) — Prior MDS, MDS cytogenetics, multilineage dysplasia. What is the most likely diagnosis?
   A. **Hematology**
   B. A condition that mimics Hematology but is not the same entity
   C. A complication of Hematology rather than the primary diagnosis
   D. An unrelated condition in the same clinical category as Hematology

