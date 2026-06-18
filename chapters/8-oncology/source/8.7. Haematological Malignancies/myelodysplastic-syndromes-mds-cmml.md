# Myelodysplastic Syndromes (MDS) & CMML

> [!tip] **FCPS/MRCP Priority: HIGH**
> **MDS = Clonal haematopoietic stem cell disorder**; **Dysplasia + Cytopenias + Risk of AML transformation**. **WHO 2022 / ICC 2022** classification. **IPSS-R / IPSS-M** for risk stratification. **Lower-risk**: ESA (Epoetin), **Luspatercept** (RS+), **Lenalidomide** (del(5q)), **Imetelstat** (RS+ transfusion-dep). **Higher-risk**: **HMA (Azacitidine/Decitabine)** ± **Venetoclax**; **Allo-HSCT** curative. **CMML** = MDS/MPN overlap; **Monocytosis ≥1×10⁹/L**; **ASXL1, TET2, SRSF2, RUNX1**; **CPSS-Mol** for risk.

---

## 1. Learning Objectives
By the end of this note you should be able to:
- [ ] Apply **WHO 2022 / ICC 2022** MDS classification
- [ ] Calculate **IPSS-R** and **IPSS-M** (molecular) risk scores
- [ ] Manage **Lower-risk MDS**: ESA → Luspatercept (RS+, ESA-refractory) → Lenalidomide (del(5q)) → Imetelstat (RS+, TD)
- [ ] Manage **Higher-risk MDS**: **HMA (Aza/Decitabine)** ± **Venetoclax** (TP53, unfit for HSCT) → **Allo-HSCT** (curative)
- [ ] Diagnose **CMML**: Monocytosis ≥1×10⁹/L, No BCR-ABL1, No PCM1-JAK2, No PDGFRA/B/FGFR1 rearrangement
- [ ] Stratify **CMML** with **CPSS / CPSS-Mol** (ASXL1, SRSF2, RUNX1)
- [ ] Select patients for **Allo-HSCT** (Age, Comorbidity, Donor, Disease risk, Molecular)

---

## 2. Definition & Epidemiology

| Feature | Detail |
|---------|--------|
| **MDS Definition** | Clonal haematopoietic stem cell disorder; **Ineffective haematopoiesis** → **Cytopenias** + **Morphological dysplasia** (≥10% in ≥1 lineage) + **AML transformation risk** |
| **MDS Incidence** | UK: ~2,500/year; Median age 70-75; M:F = 1.5:1 |
| **CMML Definition** | **MDS/MPN Overlap**; **Persistent Monocytosis ≥1×10⁹/L** + Dysplasia + No BCR-ABL1/PCM1-JAK2/PDGFRA/B/FGFR1 rearrangement |
| **CMML Incidence** | Rare: 0.5-1/100,000; Median age 70; M:F = 2:1 |
| **Risk Factors** | **Age**, **Prior chemo/RT (t-MDS)**, **Benzene**, **Smoking**, **Genetic predisposition** (GATA2, RUNX1, CEBPA, DDX41, ETV6, ANKRD26, SAMD9/9L) |

---

## 3. Aetiology & Pathophysiology

```mermaid
flowchart LR
    A[HSC Mutation] --> B[Clonal Expansion]
    B --> C[Ineffective Haematopoiesis]
    C --> D[Dysplasia + Cytopenias]
    D --> E[Microenvironment Changes]
    E --> F[Inflammatory Cytokines (TGF-β, TNF-α, IFN-γ)]
    F --> G[Apoptosis of Progenitors]
    G --> H[AML Transformation]
    A --> I[Key Driver Mutations]
    I --> I1[SF3B1 (Splicing) — MDS-RS]
    I --> I2[TP53 (Genome Guardian) — High Risk]
    I --> I3[ASXL1, TET2, DNMT3A — Epigenetic]
    I --> I4[SRSF2, U2AF1, ZRSR2 — Splicing]
    I --> I5[RUNX1, GATA2 — Transcription]
    I --> I6[RAS Pathway (NRAS, KRAS, PTPN11) — CMML]
```

### Key Mutations & Prognostic Impact

| Gene | Pathway | MDS Subtype | Prognosis |
|------|---------|-------------|-----------|
| **SF3B1** | Splicing | **MDS-RS** (Ring sideroblasts) | **Favourable** (if isolated) |
| **TP53** | DNA Repair | **t-MDS, Complex karyotype, MDS-AML** | **Very Poor** (resistant to HMA) |
| **ASXL1** | Epigenetic | MDS, CMML | Poor |
| **TET2** | Epigenetic | MDS, CMML | Intermediate |
| **DNMT3A** | Epigenetic | MDS, CMML, CHIP | Intermediate |
| **SRSF2** | Splicing | MDS, **CMML** | Poor (in CMML) |
| **U2AF1 / ZRSR2** | Splicing | MDS | Poor (ZRSR2) |
| **RUNX1** | Transcription | MDS, CMML | Poor |
| **RAS (NRAS/KRAS/PTPN11)** | Signal Transduction | **CMML**, MDS | Intermediate |

---

## 4. Clinical Features

| Feature | MDS | CMML |
|---------|-----|------|
| **Presentation** | Asymptomatic (routine bloods), Fatigue (anaemia), Infections (neutropenia), Bleeding (thrombocytopenia) | Splenomegaly (50%), Fatigue, Weight loss, Infections, Skin lesions, Monocytosis |
| **Cytopenias** | **Anaemia** (most common), Neutropenia, Thrombocytopenia (single or multi-lineage) | Anaemia, Thrombocytopenia, **Monocytosis ≥1×10⁹/L** |
| **Splenomegaly** | Uncommon (unless CMML/MPN overlap) | **Common (50%)** |
| **Skin** | Rare | **Leukaemia cutis**, Vasculitis, Pyoderma gangrenosum |
| **Autoimmune** | **Associated**: AIHA, ITP, Pure red cell aplasia, Vasculitis | Similar |

---

## 5. Classification (WHO 2022 / ICC 2022)

### MDS WHO 2022

| Category | Defining Features |
|----------|-------------------|
| **MDS with defining genetic abnormalities** | **MDS with del(5q)**; **MDS with SF3B1 mutation** (RS not required); **MDS with TP53 mutation** (VAF≥10%) |
| **MDS, morphologically defined** | **MDS with low blasts (MDS-LB)**: <5% BM blasts, <2% PB blasts<br/>**MDS, hypoplastic (MDS-h)**: Hypocellular BM (<25% cellularity)<br/>**MDS with increased blasts (MDS-IB)**: **MDS-IB1** (5-9% BM or 2-4% PB); **MDS-IB2** (10-19% BM or 5-19% PB) |
| **MDS with ring sideroblasts (MDS-RS)** | **SF3B1 mut** + **RS ≥15%** (or ≥5% if SF3B1 mut); **MDS-RS-SLD** (single lineage dysplasia) / **MDS-RS-MLD** (multilineage) |

### ICC 2022 (Similar but nuanced)
- **MDS with defining genetic abnormalities**: del(5q), SF3B1, TP53
- **MDS, morphologically defined**: SLD, MLD, IB1, IB2, h

### CMML (WHO 2022)
- **CMML-0**: <2% PB blasts, <5% BM blasts
- **CMML-1**: 2-4% PB blasts, 5-9% BM blasts
- **CMML-2**: 5-19% PB blasts, 10-19% BM blasts
- **CMML-BP**: ≥20% blasts (= AML)

---

## 6. Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|-------------------------|
| **Nutritional Deficiencies** | B12/Folate/Copper deficiency → Macro-ovalocytes, Hypersegmented neutrophils; **No clonal cytogenetics** |
| **AA (Aplastic Anaemia)** | Pancytopenia, **Hypocellular BM** (<25%), **No dysplasia**; PNH clone possible |
| **MDS-h vs AA** | MDS-h: Dysplasia + Clonal cytogenetics; AA: No dysplasia, no clonal markers |
| **MPN (ET, PV, PMF)** | Thrombocytosis / Erythrocytosis / Splenomegaly; **JAK2/CALR/MPL mut**; **No significant dysplasia** |
| **CMML vs MDS** | **Monocytosis ≥1×10⁹/L** (persistent); **CMML** |
| **CMML vs CML** | **No BCR-ABL1**; No basophilia; Monocytosis |
| **CHIP/CCUS** | **Clonal mutation (VAF≥2%) + Cytopenias (CCUS)** but **<10% dysplasia** → Not MDS |

---

## 7. Risk Stratification

### IPSS-R (Revised International Prognostic Scoring System)

| Variable | Categories & Points |
|----------|---------------------|
| **Cytogenetics** | Very Good (0): -Y, del(11q)<br>Good (1): Normal, del(5q), del(12p), del(20q), double incl. del(5q)<br>Intermediate (2): del(7q), +8, +19, i(17q), other<br>Poor (3): -7, inv(3)/t(3q)/del(3q), double incl. -7/del(7q), complex (3 abn)<br>Very Poor (4): Complex (>3 abn) |
| **BM Blasts** | ≤2% (0); >2-<5% (1); 5-10% (2); >10% (3) |
| **Hb** | ≥100 (0); 80-<100 (1); <80 (1.5) |
| **Platelets** | ≥100 (0); 50-<100 (0.5); <50 (1) |
| **ANC** | ≥0.8 (0); <0.8 (0.5) |

| Risk Group | Score | Median OS | AML Risk |
|------------|-------|-----------|----------|
| **Very Low** | ≤1.5 | 8.8 yr | 3% |
| **Low** | >1.5-3 | 5.3 yr | 14% |
| **Intermediate** | >3-4.5 | 3.0 yr | 33% |
| **High** | >4.5-6 | 1.6 yr | 54% |
| **Very High** | >6 | 0.8 yr | 84% |

### IPSS-M (Molecular IPSS) — **Adds Mutations**
- Incorporates **TP53 (VAF), SF3B1, ASXL1, RUNX1, EZH2, etc.** + **VAF weighting**
- **Superior discrimination**, especially for TP53, SF3B1

---

## 8. Management

### Lower-Risk MDS (IPSS-R Very Low/Low/Intermediate)

```mermaid
flowchart TD
    A[Lower-Risk MDS] --> B{Transfusion Dependent?}
    B -->|**Anaemia, Non-transfusion dep**| C[**ESA (Epoetin alfa/beta, Darbepoetin)**<br/>**Predictors of Response**: Serum EPO <200-500 mU/mL, No/low transfusion burden, Non-del(5q)<br/>**Dose**: Epoetin 40-60k IU SC q1-2wk; Darbepoetin 500mcg q3-4wk<br/>**Response**: Hb ↑≥1.5g/dL or ↓transfusion by ≥4 units/8wk]
    B -->|**Transfusion Dependent Anaemia**| D{SF3B1 mut / Ring Sideroblasts?}
    D -->|**Yes (MDS-RS)**| E[**Luspatercept** (MEDALIST)<br/>Activin Receptor Ligand Trap → ↓SMAD2/3 → ↑Erythropoiesis<br/>**1.0-1.75mg/kg SC q3wk**<br/>**TI response (≥8wk transfusion independence) ~38-45%**<br/>**Preferred over ESA if RS+ & ESA-refractory**]
    D -->|**No (or ESA failure)**| F[**Imetelstat** (IMerge) — **Telomerase Inhibitor**<br/>**MDS-RS, Transfusion-dependent, ESA-refractory**<br/>9.4mg/kg IV q4wk<br/>**TI response ~40%**]
    B -->|**Isolated del(5q)**| G[**Lenalidomide**<br/>**10mg/day (21/28 days)**<br/>**Transfusion Independence ~67%**<br/>**Contraindicated if TP53 mut**]
    B -->|**Thrombocytopenia**| H[**Romiplostim / Eltrombopag** (TPO-RA)<br/>If severe/refractory; Monitor BM blasts]
```

### Higher-Risk MDS (IPSS-R High/Very High / IPSS-M High/Very High)

```mermaid
flowchart TD
    A[Higher-Risk MDS] --> B{Transplant Candidate?<br/>(Age <70-75, HCT-CI ≤3, Donor)}
    B -->|**Yes**| C[**HMA Bridging → Allo-HSCT**<br/>**Azacitidine 75mg/m² SC/IV d1-7 q4wk** (or Decitabine 20mg/m² IV d1-5)<br/>**4-6 cycles** before HSCT<br/>**TP53 mut: Aza + Venetoclax** (Phase 2/3) preferred bridge]
    B -->|**No / Unfit**| D[**HMA Monotherapy**<br/>**Azacitidine** (AZA-001: OS benefit vs BSC)<br/>**Decitabine** (alternative, IV only)<br/>**Response**: CR/PR/mCR/HI (IWG criteria)<br/>**Median cycles to response: 4-6**]
    D --> D1[**TP53 mut MDS**<br/>**Azacitidine + Venetoclax**<br/>**CR rate ~50-60%** (vs ~20% Aza alone)<br/>**Pending regulatory approval**]
    D --> D2[**Maintenance**: Continue HMA until progression/toxicity<br/>**Dose reduction**: 50mg/d1-5 if cytopenias]
```

### CMML Management

```mermaid
flowchart TD
    A[CMML Diagnosis] --> B{Risk (CPSS / CPSS-Mol)}
    B -->|**Low Risk**<br/>CPSS Low/Int-1| C[**Watch & Wait** / Supportive Care<br/>Transfusions, Growth factors, Hydroxyurea if WBC>20-50×10⁹/L]
    B -->|**High Risk**<br/>CPSS Int-2/High| D[**Higher-Risk MDS Approach**]
    D --> D1[**Azacitidine** (preferred over Decitabine)<br/>**Efficacy similar to MDS**]
    D1 --> D2[**Transplant Candidate?**]
    D2 -->|Yes| E[**Allo-HSCT** (Curative)<br/>**Reduced Intensity Conditioning (RIC)**<br/>FLU/MEL or FLU/BU2]
    D2 -->|No| F[**Continue HMA**<br/>Clinical Trials (JAK2, BET, etc.)]
```

### Allo-HSCT in MDS/CMML

| Indication | Details |
|------------|---------|
| **Higher-Risk MDS** (IPSS-R Int/High/Very High) | **Curative**; Best if **CR/PR** pre-HSCT |
| **Lower-Risk with adverse features** | TP53 mut, Complex karyotype, Transfusion dependence refractory to therapy |
| **CMML** | CPSS Int-2/High; **CPSS-Mol High** (ASXL1/SRSF2 mut) |
| **Donor** | Matched Sibling > MUD > Haploidentical > Cord |
| **Conditioning** | **RIC (FLU/MEL, FLU/BU2)** preferred for age >55-60 / HCT-CI >3; **MAC** for young, fit, high-risk |
| **TP53 mut** | **Allo-HSCT only potentially curative**; High relapse risk post-HSCT; Consider **Post-HSCT maintenance (Aza/Venetoclax)** |

### Supportive Care

| Issue | Management |
|-------|------------|
| **Transfusion** | Leukodepleted, Irradiated (if potential HSCT); **Iron Chelation** (Deferasirox) if ferritin >1000-2500, TD >1yr |
| **Infections** | **Febrile Neutropenia**: Piperacillin-tazobactam / Meropenem; **Prophylaxis**: PJP (Co-trimoxazole), HSV (Acyclovir), Fungal (Posaconazole if prolonged neutropenia) |
| **Growth Factors** | **G-CSF** (Filgrastim/Pegfilgrastim) if recurrent infections / FN; **EPO** for anaemia |
| **Vaccinations** | **Inactivated** safe; **Live** avoided; **COVID/Influenza/Pneumococcal** recommended |

---

## 9. FCPS/MRCP High-Yield Summary

| Topic | Key Points |
|-------|------------|
| **MDS Definition** | **Dysplasia ≥10% in ≥1 lineage** + **Cytopenia(s)** + **Clonal** (cytogenetics/mutation) + **Exclude other causes** |
| **WHO 2022 Key Categories** | **MDS with defining genetic abn**: del(5q), **SF3B1**, **TP53**; **MDS-LB** (<5% blasts); **MDS-IB1/IB2** (5-19% blasts); **MDS-h** |
| **MDS-RS** | **SF3B1 mut + RS ≥15%** (or ≥5% if SF3B1 mut); **Favourable** if isolated |
| **del(5q) MDS** | **Isolated del(5q)** → **Lenalidomide 10mg** (TI ~67%); **Contraindicated if TP53 mut** |
| **TP53 MDS** | **Very Poor**; Complex karyotype; **Aza + Venetoclax** preferred; **Allo-HSCT only cure** |
| **IPSS-R vs IPSS-M** | **IPSS-M adds mutations (TP53, SF3B1, ASXL1, RUNX1, VAF)** → Better risk discrimination |
| **Lower-Risk Rx** | **ESA (sEPO<200-500)** → **Luspatercept** (RS+, ESA-refractory) → **Lenalidomide** (del(5q)) → **Imetelstat** (RS+, TD) |
| **Higher-Risk Rx** | **HMA (Aza/Decitabine)** → **Allo-HSCT** (curative); **TP53: Aza + Ven** |
| **CMML** | **Monocytosis ≥1×10⁹/L** persistent; **No BCR-ABL1/PDGFR/JAK2**; **ASXL1, TET2, SRSF2, RUNX1**; **CPSS-Mol** for risk |
| **Luspatercept** | **Activin receptor trap** → ↓SMAD2/3 → ↑Erythropoiesis; **MEDALIST**: MDS-RS, TD, ESA-refractory |
| **Imetelstat** | **Telomerase inhibitor**; **IMERGE**: MDS-RS, TD, ESA-refractory |
| **Allo-HSCT** | **Curative for Higher-Risk**; RIC preferred; **TP53 = high relapse post-HSCT** |

---

## 10. Viva Questions (MRCP PACES / FCPS)

| Question | Expected Answer |
|----------|-----------------|
| **70M, Hb 85, Plt 80, Neut 0.9. BM: 6% blasts, multilineage dysplasia. Karyotype: del(5q) isolated. Diagnosis?** | **MDS with isolated del(5q)** (WHO 2022: MDS with defining genetic abnormality). **IPSS-R: Good cytogenetics=1pt, Blasts 1pt, Hb 1pt, Plt 0.5, ANC 0.5 = 4 → Intermediate**. |
| **Same patient — treatment?** | **Lenalidomide 10mg/day (21/28 days)** — **TI rate ~67%**. Monitor for VTE, TLS, neutropenia. Contraindicated if TP53 mut. |
| **75M, transfusion-dependent anaemia, SF3B1 mut, RS 25%, failed ESA. Next?** | **Luspatercept 1.0-1.75mg/kg SC q3wk** (MEDALIST). **TI response ~38-45%**. |
| **65M, MDS, IPSS-R High, TP53 mut, VAF 40%, fit. Management?** | **Azacitidine + Venetoclax** (preferred for TP53) → **Allo-HSCT** if response (CR/PR). **TP53 MDS = Very Poor prognosis, Aza alone CR ~20%**. |
| **IPSS-R cytogenetic categories — which is Very Poor?** | **Complex >3 abnormalities**. **Complex 3 abn = Poor (3pts)**; **>3 abn = Very Poor (4pts)**. |
| **CMML diagnostic criteria?** | **Persistent Monocytosis ≥1×10⁹/L** + **Dysplasia** + **No BCR-ABL1** + **No PCM1-JAK2** + **No PDGFRA/B/FGFR1 rearrangement** + **Blasts <20%**. |
| **CMML risk stratification — CPSS-Mol?** | **Clinical**: Hb<100, WBC>10, Plt<100, PB blasts≥2% + **Molecular**: **ASXL1, SRSF2, RUNX1 mutations** (each adverse). |
| **Luspatercept vs Imetelstat — both for MDS-RS?** | **Luspatercept**: Activin receptor trap; **Imetelstat**: Telomerase inhibitor; Both for **MDS-RS, TD, ESA-refractory**; Imetelstat newer (IMerge). |
| **Higher-risk MDS — when refer for Allo-HSCT?** | **IPSS-R ≥Intermediate (or IPSS-M High/VHigh)**, Age <70-75, HCT-CI ≤3, Donor available, **Preferable in CR/PR after HMA**. |
| **t-MDS — typical cytogenetics?** | **Complex karyotype**, **TP53 mut**, **-5/del(5q), -7/del(7q), -17/del(17p)** — **Very Poor prognosis**. |

---

## 11. Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **MDS vs CCUS** | **CCUS**: Clonal mutation (VAF≥2%) + Cytopenias + **<10% dysplasia** → Not MDS; **Progression risk to MDS/AML** |
| **MDS-RS vs MDS-SF3B1** | **WHO 2022**: **MDS with SF3B1 mutation** (RS not required if SF3B1 mut); **ICC**: Requires RS ≥15% (or ≥5% if SF3B1 mut) |
| **del(5q) MDS vs 5q- Syndrome** | **5q- Syndrome** = Old term for **MDS with isolated del(5q)**, macrocytic anaemia, normal/increased platelets, female predominance; Now **MDS with isolated del(5q)** |
| **IPSS-R vs IPSS-M** | **IPSS-R**: Clinical + Cytogenetics + Blasts + Cytopenias; **IPSS-M**: Adds **Molecular (TP53, SF3B1, ASXL1, RUNX1, VAF)** — **New standard** |
| **Aza vs Decitabine** | **Aza**: SC/IV, d1-7 q4wk; **Decitabine**: IV only, d1-5 q4wk; **Aza has OS benefit (AZA-001)**; Decitabine alternative |
| **CMML vs aCML** | **aCML**: **No monocytosis**, WBC>13, Neutrophilia, Dysgranulopoiesis, **CSF3R mut**; **CMML**: **Monocytosis ≥1×10⁹/L** |

**Mnemonic: MDS-CMML**
- **M**orphology: **Dysplasia ≥10%** in ≥1 lineage
- **D**efining Genetics: **del(5q), SF3B1, TP53** (WHO 2022)
- **S**core: **IPSS-R** (Cytogen, Blasts, Hb, Plt, ANC) → **IPSS-M** (+ Mutations)
- **C**MML: **Monocytosis ≥1×10⁹/L** + No BCR-ABL1/PDGFR/JAK2
- **M**olecular CMML: **ASXL1, TET2, SRSF2, RUNX1** → CPSS-Mol
- **M**anagement Low: ESA → **Luspatercept (RS+)** / **Lenalidomide (5q-)** / Imetelstat
- **L**ow-risk: ESA if sEPO<200-500
- **H**igh-risk: **Aza ± Ven** → **Allo-HSCT** (Curative)

---

## 12. Mind Map

```mermaid
mindmap
  root((MDS & CMML))
    MDS WHO 2022
      Defining Genetic Abnormalities
        del(5q) → Lenalidomide
        SF3B1 mut → MDS-RS → Luspatercept/Imetelstat
        TP53 mut → Poor → Aza+Ven / Allo-HSCT
      Morphologically Defined
        MDS-LB (<5% blasts)
        MDS-h (Hypocellular)
        MDS-IB1 (5-9% BM)
        MDS-IB2 (10-19% BM)
    Risk Stratification
      IPSS-R (Cytogen, Blasts, Hb, Plt, ANC)
      IPSS-M (+ TP53, SF3B1, ASXL1, RUNX1, VAF)
    Lower-Risk Rx
      ESA (sEPO<200-500)
      Luspatercept (RS+, ESA-refractory)
      Lenalidomide (del(5q))
      Imetelstat (RS+, TD, ESA-ref)
    Higher-Risk Rx
      HMA: Aza (SC/IV d1-7) / Decitabine (IV d1-5)
      TP53: Aza + Venetoclax
      Allo-HSCT (Curative)
    CMML
      Monocytosis ≥1×10⁹/L
      Mut: ASXL1, TET2, SRSF2, RUNX1
      CPSS / CPSS-Mol
      Rx: Aza → Allo-HSCT (High risk)
```

---

## 13. One-Page Revision Card

| Domain | Key Points |
|--------|------------|
| **MDS Definition** | Dysplasia ≥10% + Cytopenia(s) + Clonal + Exclude other causes |
| **WHO 2022 Key** | MDS-del(5q), MDS-SF3B1, MDS-TP53, MDS-LB, MDS-h, MDS-IB1/IB2 |
| **MDS-RS** | SF3B1 mut + RS ≥15% (or ≥5% if SF3B1) — Favourable |
| **del(5q)** | Isolated → **Lenalidomide 10mg** (21/28d); Contra: TP53 mut |
| **TP53 MDS** | Complex karyotype, Very Poor; **Aza + Venetoclax** → Allo-HSCT |
| **IPSS-R** | Cytogen (0-4), Blasts (0-3), Hb (0-1.5), Plt (0-1), ANC (0-0.5) → 5 Risk Groups |
| **IPSS-M** | Adds TP53, SF3B1, ASXL1, RUNX1, VAF — Better discrimination |
| **Lower-Risk** | ESA → Luspatercept (RS+) → Lenalidomide (5q) → Imetelstat (RS+) |
| **Higher-Risk** | **Aza ± Ven** → **Allo-HSCT** (RIC) |
| **CMML** | Monocytosis ≥1×10⁹/L persistent; ASXL1/TET2/SRSF2/RUNX1; CPSS-Mol |
| **Luspatercept** | Activin receptor trap, MEDALIST, MDS-RS TD ESA-ref |
| **Allo-HSCT** | Curative Higher-Risk; RIC preferred; TP53 = high relapse |

---

## 14. Spaced Repetition Trackers

| Review Interval | Date Completed | Confidence (1-5) | Notes |
|-----------------|----------------|------------------|-------|
| 24 hours | | | |
| 7 days | | | |
| 15 days | | | |
| 30 days | | | |
| 90 days | | | |

---

## 15. Self-Test Scorecard

| Section | Score /5 | Last Attempt |
|---------|----------|--------------|
| WHO 2022 MDS classification | | |
| IPSS-R calculation | | |
| IPSS-M vs IPSS-R | | |
| Lower-risk management algorithm | | |
| del(5q) / SF3B1 specific Rx | | |
| TP53 MDS management | | |
| CMML diagnosis & risk | | |
| Allo-HSCT indications | | |

---

## 16. Local Navigation
- **Parent Heading**: [[../Oncology|Oncology]]
- **Chapter Map**: [[../Davidson Chapter 7 - Oncology Hierarchy|Oncology Hierarchy]]
- **Chapter MOC**: [[../Oncology MOC|Oncology MOC]]
- **Drug Reference**: [[../../Clinical Therapeutics and Good Prescribing|Drugs]]
- **Related**: [[AML]], [[Lenalidomide]], [[Luspatercept]], [[Azacitidine]], [[Allo-HSCT]], [[TP53 MDS]], [[SF3B1]]

---

# FCPS/MRCP Exam Extras

## 17. MCQs (10)


**1.** Regarding Myelodysplastic Syndromes (MDS) & CMML (MDS Definition), which statement is correct?
   A. **Dysplasia ≥10% in ≥1 lineage** + **Cytopenia(s)** + **Clonal** (cytogenetics/mutation) + **Exclude
   B. **Dysplasia - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **Dysplasia ≥10% in ≥1 lineage** + **Cytopenia(s)** + **Clonal** (cytogenetics/mutation) + **Exclude other causes**


**2.** Regarding Myelodysplastic Syndromes (MDS) & CMML (WHO 2022 Key Categories), which statement is correct?
   A. **MDS with defining genetic abn**: del(5q), **SF3B1**, **TP53**
   B. **MDS - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **MDS with defining genetic abn**: del(5q), **SF3B1**, **TP53**; **MDS-LB** (<5% blasts); **MDS-IB1/IB2** (5-19% blasts)...


**3.** Regarding Myelodysplastic Syndromes (MDS) & CMML (MDS-RS), which statement is correct?
   A. **SF3B1 mut + RS ≥15%** (or ≥5% if SF3B1 mut)
   B. **SF3B1 - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **SF3B1 mut + RS ≥15%** (or ≥5% if SF3B1 mut); **Favourable** if isolated


**4.** Regarding Myelodysplastic Syndromes (MDS) & CMML (del(5q) MDS), which statement is correct?
   A. **Isolated del(5q)** → **Lenalidomide 10mg** (TI ~67%)
   B. **Isolated - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **Isolated del(5q)** → **Lenalidomide 10mg** (TI ~67%); **Contraindicated if TP53 mut**


**5.** Regarding Myelodysplastic Syndromes (MDS) & CMML (TP53 MDS), which statement is correct?
   A. **Very Poor**
   B. **Very - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **Very Poor**; Complex karyotype; **Aza + Venetoclax** preferred; **Allo-HSCT only cure**


**6.** Regarding Myelodysplastic Syndromes (MDS) & CMML (IPSS-R vs IPSS-M), which statement is correct?
   A. **IPSS-M adds mutations (TP53, SF3B1, ASXL1, RUNX1, VAF)** → Better risk discrimination
   B. **IPSS-M - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **IPSS-M adds mutations (TP53, SF3B1, ASXL1, RUNX1, VAF)** → Better risk discrimination


**7.** Regarding Myelodysplastic Syndromes (MDS) & CMML (Lower-Risk Rx), which statement is correct?
   A. **ESA (sEPO<200-500)** → **Luspatercept** (RS+, ESA-refractory) → **Lenalidomide** (del(5q)) → **Ime
   B. **ESA - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **ESA (sEPO<200-500)** → **Luspatercept** (RS+, ESA-refractory) → **Lenalidomide** (del(5q)) → **Imetelstat** (RS+, TD)


**8.** Regarding Myelodysplastic Syndromes (MDS) & CMML (Higher-Risk Rx), which statement is correct?
   A. **HMA (Aza/Decitabine)** → **Allo-HSCT** (curative)
   B. **HMA - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **HMA (Aza/Decitabine)** → **Allo-HSCT** (curative); **TP53: Aza + Ven**


**9.** Regarding Myelodysplastic Syndromes (MDS) & CMML (CMML), which statement is correct?
   A. **Monocytosis ≥1×10⁹/L** persistent
   B. **Monocytosis - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **Monocytosis ≥1×10⁹/L** persistent; **No BCR-ABL1/PDGFR/JAK2**; **ASXL1, TET2, SRSF2, RUNX1**; **CPSS-Mol** for risk


**10.** Regarding Myelodysplastic Syndromes (MDS) & CMML (Luspatercept), which statement is correct?
   A. **Activin receptor trap** → ↓SMAD2/3 → ↑Erythropoiesis
   B. **Activin - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **Activin receptor trap** → ↓SMAD2/3 → ↑Erythropoiesis; **MEDALIST**: MDS-RS, TD, ESA-refractory


## 18. SBA Questions (10)


**1.** A 55-year-old presents with classic features. MDT discussion recommends:
   - A. **Dysplasia ≥10% in ≥1 lineage** + **Cytopenia(s)** + **Clonal** (cytogenetics/mutation) + **Exclude
   - B. **Dysplasia (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — first-line: **Dysplasia ≥10% in ≥1 lineage** + **Cytopenia(s)** + **Clonal** (cytogenetics/mutation) + **Exclude other causes**


**2.** On staging workup, the patient is found to be [Stage X]. Best management is:
   - A. **MDS with defining genetic abn**: del(5q), **SF3B1**, **TP53**
   - B. **MDS (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — stage-specific: **MDS with defining genetic abn**: del(5q), **SF3B1**, **TP53**; **MDS-LB** (<5% blasts); **MDS-IB1/IB2** (5-19% blasts)...


**3.** Following first-line treatment, the patient develops [complication]. Best next step:
   - A. **SF3B1 mut + RS ≥15%** (or ≥5% if SF3B1 mut)
   - B. **SF3B1 (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — complication: **SF3B1 mut + RS ≥15%** (or ≥5% if SF3B1 mut); **Favourable** if isolated


**4.** The patient asks about prognosis. Most appropriate response based on:
   - A. **Isolated del(5q)** → **Lenalidomide 10mg** (TI ~67%)
   - B. **Isolated (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — prognosis: **Isolated del(5q)** → **Lenalidomide 10mg** (TI ~67%); **Contraindicated if TP53 mut**


**5.** A 65-year-old with relevant risk factors should be screened with:
   - A. **Very Poor**
   - B. **Very (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — screening: **Very Poor**; Complex karyotype; **Aza + Venetoclax** preferred; **Allo-HSCT only cure**


**6.** The most clinically important biomarker/molecular test is:
   - A. **IPSS-M adds mutations (TP53, SF3B1, ASXL1, RUNX1, VAF)** → Better risk discrimination
   - B. **IPSS-M (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — biomarker: **IPSS-M adds mutations (TP53, SF3B1, ASXL1, RUNX1, VAF)** → Better risk discrimination


**7.** The standard chemotherapy/regimen of choice is:
   - A. **ESA (sEPO<200-500)** → **Luspatercept** (RS+, ESA-refractory) → **Lenalidomide** (del(5q)) → **Ime
   - B. **ESA (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — chemo: **ESA (sEPO<200-500)** → **Luspatercept** (RS+, ESA-refractory) → **Lenalidomide** (del(5q)) → **Imetelstat** (RS+, TD)


**8.** The role of surgery in this case is:
   - A. **HMA (Aza/Decitabine)** → **Allo-HSCT** (curative)
   - B. **HMA (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — surgery: **HMA (Aza/Decitabine)** → **Allo-HSCT** (curative); **TP53: Aza + Ven**


**9.** The recommended surveillance/follow-up protocol is:
   - A. **Monocytosis ≥1×10⁹/L** persistent
   - B. **Monocytosis (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — follow-up: **Monocytosis ≥1×10⁹/L** persistent; **No BCR-ABL1/PDGFR/JAK2**; **ASXL1, TET2, SRSF2, RUNX1**; **CPSS-Mol** for risk


**10.** Palliative care referral is most appropriate when:
   - A. **Activin receptor trap** → ↓SMAD2/3 → ↑Erythropoiesis
   - B. **Activin (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — palliative: **Activin receptor trap** → ↓SMAD2/3 → ↑Erythropoiesis; **MEDALIST**: MDS-RS, TD, ESA-refractory


## 19. Flashcards

**Q1:** MDS Definition?
**A1:** Dysplasia ≥10% in ≥1 lineage + Cytopenia(s) + Clonal (cytogenetics/mutation) + Exclude other causes

**Q2:** WHO 2022 Key Categories?
**A2:** MDS with defining genetic abn: del(5q), SF3B1, TP53; MDS-LB (<5% blasts); MDS-IB1/IB2 (5-19% blasts); MDS-h

**Q3:** MDS-RS?
**A3:** SF3B1 mut + RS ≥15% (or ≥5% if SF3B1 mut); Favourable if isolated

**Q4:** del(5q) MDS?
**A4:** Isolated del(5q) → Lenalidomide 10mg (TI ~67%); Contraindicated if TP53 mut

**Q5:** TP53 MDS?
**A5:** Very Poor; Complex karyotype; Aza + Venetoclax preferred; Allo-HSCT only cure

**Q6:** IPSS-R vs IPSS-M?
**A6:** IPSS-M adds mutations (TP53, SF3B1, ASXL1, RUNX1, VAF) → Better risk discrimination

**Q7:** Lower-Risk Rx?
**A7:** ESA (sEPO<200-500) → Luspatercept (RS+, ESA-refractory) → Lenalidomide (del(5q)) → Imetelstat (RS+, TD)

**Q8:** Higher-Risk Rx?
**A8:** HMA (Aza/Decitabine) → Allo-HSCT (curative); TP53: Aza + Ven

## 20. Answer Key with Explanations

| # | MCQ | Topic | Explanation |
|---|-----|-------|-------------|
| 1 | A | MDS Definition | Dysplasia ≥10% in ≥1 lineage + Cytopenia(s) + Clonal (cytogenetics/mutation) + Exclude other causes |
| 2 | A | WHO 2022 Key Categories | MDS with defining genetic abn: del(5q), SF3B1, TP53; MDS-LB (<5% blasts); MDS-IB1/IB2 (5-19% blasts); MDS-h |
| 3 | A | MDS-RS | SF3B1 mut + RS ≥15% (or ≥5% if SF3B1 mut); Favourable if isolated |
| 4 | A | del(5q) MDS | Isolated del(5q) → Lenalidomide 10mg (TI ~67%); Contraindicated if TP53 mut |
| 5 | A | TP53 MDS | Very Poor; Complex karyotype; Aza + Venetoclax preferred; Allo-HSCT only cure |
| 6 | A | IPSS-R vs IPSS-M | IPSS-M adds mutations (TP53, SF3B1, ASXL1, RUNX1, VAF) → Better risk discrimination |
| 7 | A | Lower-Risk Rx | ESA (sEPO<200-500) → Luspatercept (RS+, ESA-refractory) → Lenalidomide (del(5q)) → Imetelstat (RS+, TD) |
| 8 | A | Higher-Risk Rx | HMA (Aza/Decitabine) → Allo-HSCT (curative); TP53: Aza + Ven |
| 9 | A | CMML | Monocytosis ≥1×10⁹/L persistent; No BCR-ABL1/PDGFR/JAK2; ASXL1, TET2, SRSF2, RUNX1; CPSS-Mol for risk |
| 10 | A | Luspatercept | Activin receptor trap → ↓SMAD2/3 → ↑Erythropoiesis; MEDALIST: MDS-RS, TD, ESA-refractory |

| # | SBA | Topic | Explanation |
|---|-----|-------|-------------|
| 1 | A | MDS Definition | Dysplasia ≥10% in ≥1 lineage + Cytopenia(s) + Clonal (cytogenetics/mutation) + Exclude other causes |
| 2 | A | WHO 2022 Key Categories | MDS with defining genetic abn: del(5q), SF3B1, TP53; MDS-LB (<5% blasts); MDS-IB1/IB2 (5-19% blasts); MDS-h |
| 3 | A | MDS-RS | SF3B1 mut + RS ≥15% (or ≥5% if SF3B1 mut); Favourable if isolated |
| 4 | A | del(5q) MDS | Isolated del(5q) → Lenalidomide 10mg (TI ~67%); Contraindicated if TP53 mut |
| 5 | A | TP53 MDS | Very Poor; Complex karyotype; Aza + Venetoclax preferred; Allo-HSCT only cure |
| 6 | A | IPSS-R vs IPSS-M | IPSS-M adds mutations (TP53, SF3B1, ASXL1, RUNX1, VAF) → Better risk discrimination |
| 7 | A | Lower-Risk Rx | ESA (sEPO<200-500) → Luspatercept (RS+, ESA-refractory) → Lenalidomide (del(5q)) → Imetelstat (RS+, TD) |
| 8 | A | Higher-Risk Rx | HMA (Aza/Decitabine) → Allo-HSCT (curative); TP53: Aza + Ven |
| 9 | A | CMML | Monocytosis ≥1×10⁹/L persistent; No BCR-ABL1/PDGFR/JAK2; ASXL1, TET2, SRSF2, RUNX1; CPSS-Mol for risk |
| 10 | A | Luspatercept | Activin receptor trap → ↓SMAD2/3 → ↑Erythropoiesis; MEDALIST: MDS-RS, TD, ESA-refractory |

## 21. Local Navigation


- **Parent Heading Hub**: [[../../Haematological Malignancies|Haematological Malignancies]]
- **Chapter Map**: [[../../Davidson Chapter 7 - Oncology Hierarchy|Oncology Hierarchy]]
- **Chapter MOC**: [[../../Oncology MOC|Oncology MOC]]
- **Drug Reference**: [[../../../Clinical Therapeutics and Good Prescribing|Drugs]]

