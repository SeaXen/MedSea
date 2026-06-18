# 3. Chromosomal Disorders

**Parent Topic:** [Clinical Genetics MOC](../Clinical%20Genetics%20MOC.md) → [Chapter 3 Hierarchy](../Davidson%20Chapter%203%20-%20Clinical%20Genetics%20Hierarchy.md)  
**Status:** `full-fcps-mrcp-note`  
**Priority:** ⭐⭐⭐ HIGHEST (FCPS/MRCP — Aneuploidy, Translocations, Microdeletions, Instability syndromes)  
**Source:** Davidson 24th Ed Ch 3; Gardner & Sutherland; FCPS/MRCP syllabus; Unique (rarechromo.org)

---

## 1. 🎯 Learning Objectives
- [ ] Identify **aneuploidy ultrasound features** and **recurrence risks**
- [ ] Interpret **balanced vs unbalanced translocations** (Robertsonian, Reciprocal) and recurrence risks
- [ ] Recognise **microdeletion/duplication syndromes** (22q11, 1p36, 5p, 7q11, 15q, 17p, 17q)
- [ ] Recognise **chromosomal instability syndromes** (Fanconi, Bloom, AT, NBS)
- [ ] Calculate **recurrence risks** for translocation carriers
- [ ] Answer viva: "Robertsonian translocation 14;21 recurrence risk" and "Microdeletion 22q11.2 features"

---

## 2. 🧠 Core Concept: Chromosomal Architecture

```mermaid
flowchart TD
    A[Chromosomal Disorders] --> B[Aneuploidy<br/>Numerical]
    A --> B2[Structural Rearrangements<br/>Balanced/Unbalanced]
    A --> B3[Microdeletion/Duplication<br/>Submicroscopic]
    A --> B4[Instability Syndromes<br/>DNA Repair Defects]
    
    B --> C1[Trisomy 21 (Down)]
    B --> C2[Trisomy 18 (Edwards)]
    B --> C3[Trisomy 13 (Patau)]
    B --> C4[Sex Chromosome (45,X; 47,XXY; 47,XXX; 47,XYY)]
    
    B2 --> D1[Robertsonian Translocation]
    B2 --> D2[Reciprocal Translocation]
    B2 --> D3[Inversions]
    B2 --> D4[Insertions/Rings/Dicentrics]
    
    B3 --> E1[22q11.2 (DiGeorge/VCFS)]
    B3 --> E2[1p36, 5p (Cri-du-chat), 7q11 (Williams)]
    B3 --> E3[15q11-13 (PWS/AS), 17p13 (Miller-Dieker)]
    B3 --> E4[17q12 (HNF1B), 16p11.2, 1q21.1]
    
    B4 --> F1[Fanconi Anaemia (FA pathway)]
    B2 --> F2[Bloom Syndrome (BLM)]
    B2 --> F3[AT (ATM)]
    B2 --> F4[NBS (NBN)]
```

---

## 3. ️⃣ Autosomal Aneuploidies

### Trisomy 21 — Down Syndrome
| Feature | Detail |
|---------|--------|
| **Incidence** | 1/700-1/1000 live births; ↑ with maternal age |
| **Karyotype** | **47,XX,+21** / **47,XY,+21** (95% free trisomy) |
| **Mosaicism** | 46,XX/47,XX,+21 (2-3%) — Milder phenotype |
| **Robertsonian Translocation** | **46,XX,der(14;21)(q10;q10)** — 3-4% of cases |
| **Prenatal Features** | Increased NT (>3.5mm), Absent nasal bone, Echogenic bowel, Short femur, AVSD, Duodenal atresia |
| **Neonatal Features** | Hypotonia, Flat face, Epicanthic folds, Upward slanting palpebral fissures, Single palmar crease, Sandal gap |
| **Medical Issues** | **AVSD (40-50%)**, Gastrointestinal (Duodenal atresia, Hirschsprung), Leukaemia risk (ALL/AMKL), Hypothyroidism, Atlantoaxial instability, Early-onset Alzheimer's (>40y) |
| **Life Expectancy** | ~60 years (improved with cardiac surgery) |

### Trisomy 18 — Edwards Syndrome
| Feature | Detail |
|---------|--------|
| **Incidence** | 1/5000-1/7000 |
| **Karyotype** | 47,XX,+18 / 47,XY,+18 (90% free trisomy) |
| **Prenatal** | IUGR, Polyhydramnios, Clenched hands (index over middle), Rocker-bottom feet, Omphalocele, CHD (VSD, ASD), Cystic hygroma |
| **Survival** | Median 3-14 days; 5-10% survive >1 year |

### Trisomy 13 — Patau Syndrome
| Feature | Detail |
|---------|--------|
| **Incidence** | 1/10,000-1/20,000 |
| **Karyotype** | 47,XX,+13 / 47,XY,+13 |
| **Prenatal** | Holoprosencephaly, Facial clefts, Polydactyly (postaxial), Cardiac defects, Renal cysts, Rocker-bottom feet |
| **Survival** | Median 3-7 days; >90% die by 1 year |

### Prenatal Screening for Aneuploidy
| Test | Timing | Detection Rate (T21) | False Positive |
|------|--------|---------------------|----------------|
| **Combined Test** | 11-14w | 85-90% | 3-5% |
| **NIPT (cfDNA)** | 10w+ | >99% | <0.1% |
| **Quadruple Test** | 15-20w | 80% | 5% |
| **Diagnostic** | CVS (11-14w) / Amnio (15-20w) | >99.9% | — |

---

## 4. ️⃣ Sex Chromosome Aneuploidies

| Syndrome | Karyotype | Incidence | Key Features |
|----------|-----------|-----------|--------------|
| **Turner Syndrome** | **45,X** (50% mosaic 45,X/46,XX) | 1/2500 females | **Short stature**, Webbed neck, Lymphoedema (neonatal), Coarctation, Bicuspid aortic valve, Streak ovaries (POI), Horseshoe kidney, Autoimmune thyroiditis |
| **Klinefelter Syndrome** | **47,XXY** (80%); Variants: 48,XXXY, 49,XXXXY | 1/600 males | **Tall stature**, Small firm testes, **Azoospermia**, Gynaecomastia, Low testosterone, Learning difficulties, Language delay |
| **Triple X Syndrome** | **47,XXX** | 1/1000 females | Tall stature, Learning difficulties, Seizures, Premature ovarian insufficiency (10-15%) |
| **XYY Syndrome** | **47,XYY** | 1/1000 males | Tall stature, Learning difficulties, Behavioural issues, Normal fertility |
| **Tetrasomy X** | 48,XXXX | Rare | Severe ID, Facial dysmorphism, Cardiac/renal anomalies |
| **48,XXXY / 49,XXXXY** | Variants of Klinefelter | Rare | More severe phenotype, Severe ID, Radioulnar synostosis |

---

## 5. ️⃣ Structural Chromosomal Rearrangements

### Balanced vs Unbalanced
| Type | Definition | Phenotype | Recurrence Risk |
|------|------------|-----------|-----------------|
| **Balanced** | No net gain/loss | Usually normal (unless breakpoint disrupts gene) | See below |
| **Unbalanced** | Net gain/loss | Abnormal (DD/CA) | Depends on rearrangement type |

### 3.1 Robertsonian Translocations
- **Involves**: Acrocentric chromosomes (13, 14, 15, 21, 22) — fusion at centromeres
- **Karyotype**: 45,XX,rob(14;21)(q10;q10) — 45 chromosomes
- **Formation**: Centric fusion of long arms; Short arms lost (acrocentric p arms = rDNA, non-essential)

| Translocation | Carrier Karyotype | Gametes | Offspring Risk |
|---------------|-------------------|---------|----------------|
| **rob(14;21)** | 45,XX,rob(14;21) | 6 types | **Down syndrome risk ~10-15%** if mother carrier; ~1-2% if father carrier |
| **rob(13;14)** | 45,XX,rob(13;14) | 6 types | **No viable unbalanced** (Trisomy 13/14 lethal); Carrier risk 50% |
| **rob(21;21)** | 45,XX,rob(21;21) | 100% unbalanced | **100% Down syndrome** if carrier parent; **Do not reproduce without PGT** |
| **rob(13;15), 14;15, 15;21, 15;22, 13;21, 13;22, 22;21** | Various | Various | Trisomy risk for larger chromosome (13, 15, 21, 22) |

> **Key:** **rob(21;21) = 100% Down syndrome** if carrier parent. **rob(14;21)** risk depends on parent of origin (maternal > paternal).

### 3.2 Reciprocal Translocations
- **Exchange** of segments between non-homologous chromosomes
- **Karyotype**: e.g., 46,XX,t(2;5)(q31;q14)
- **Segregation Patterns**:
  - **Alternate** → Balanced (Normal or Carrier) — **Viable**
  - **Adjacent-1** → Unbalanced (Duplication + Deletion) — **Non-viable/Abnormal**
  - **Adjacent-2** → Unbalanced — **Non-viable/Abnormal**
  - **3:1 Segregation** → Highly unbalanced — Usually non-viable

| Parameter | Value |
|-----------|-------|
| **Liveborn Unbalanced Risk** | ~5-10% (depends on segment size) |
| **Carrier Risk (balanced)** | ~30-40% |
| **Pregnancy Loss** | High (30-50%) |

### 3.3 Inversions
| Type | Description | Recombinant Risk |
|------|-------------|------------------|
| **Paracentric** | Inversion within arm (no centromere) | Acentric/Dicentric recombinants → Non-viable |
| **Pericentric** | Includes centromere | **Recombinant viable** → Partial dup/del |

### 3.4 Other Structural Variants
| Variant | Description |
|---------|-------------|
| **Ring Chromosome** | Deletion both ends + fusion → Ring; Mitotic instability → Variegated phenotype |
| **Dicentric** | Two centromeres → Mitotic instability, Breakage |
| **Insertion** | Segment inserted into non-homologous chromosome |
| **Isochromosome** | Mirror-image arms (e.g., i(Xq) in Turner) |

---

## 6. ️⃣ Microdeletion / Microduplication Syndromes (Genomic Disorders)

### Recurrent Microdeletion Syndromes (Recurrent = NAHR between LCRs)

| Syndrome | Locus | Size | Key Features |
|----------|-------|------|--------------|
| **22q11.2 Deletion (DiGeorge/VCFS)** | 22q11.2 | ~3 Mb (LCR22 A-D) | **CATCH-22**: Cardiac (conotruncal), Abnormal facies, Thymic hypoplasia/aplasia, Cleft palate, Hypocalcaemia (hypoparathyroidism); **1/4000** |
| **1p36 Deletion** | 1p36.3 | ~2-10 Mb | **Severe ID**, Microcephaly, Seizures, Cardiomyopathy, Facial dysmorphism, Hearing loss, Delayed growth |
| **5p Deletion (Cri-du-chat)** | 5p15.2 | Variable | **High-pitched cat-like cry**, Microcephaly, Round face, Hypertelorism, ID, Developmental delay |
| **7q11.23 Deletion (Williams)** | 7q11.23 | ~1.5-1.8 Mb | **Elfin facies**, Supravalvular aortic stenosis, **Hypercalcaemia**, **Elfin facies**, Outgoing personality, **Hyperacusis**, ID (mild-moderate) |
| **15q11-q13 Deletion** | 15q11-q13 | ~4-6 Mb | **Prader-Willi (paternal)** / **Angelman (maternal)** — Imprinting |
| **17p13.3 Deletion (Miller-Dieker)** | 17p13.3 | ~1 Mb | **Lissencephaly** (smooth brain), Severe epilepsy, Profound ID, Characteristic face |
| **17p12 Deletion (Smith-Magenis)** | 17p11.2 | ~3.7 Mb | **Sleep disturbance**, Self-hugging, Brachydactyly, Hoarse voice, Behavioural issues, ID |
| **16p11.2 Deletion** | 16p11.2 | ~600 kb | **Autism, ID, Obesity, Macrocephaly**, Seizures, Schizophrenia risk |
| **1q21.1 Deletion/Duplication** | 1q21.1 | ~1.35 Mb | Variable: ID, Microcephaly/Macrocephaly, Cardiac, Psychiatric |
| **3q29 Deletion** | 3q29 | ~1.6 Mb | ID, Autism, Schizophrenia risk, Microcephaly |
| **15q13.3 Deletion** | 15q13.3 | ~2 Mb | Epilepsy, ID, Autism, Schizophrenia risk |
| **Xp22.3 Deletion (STS)** | Xp22.3 | Various | X-linked ichthyosis (STS), Kallmann (ANOS1), Chondrodysplasia punctata |

### Non-Recurrent (Unique) CNVs
- **De novo**, Random breakpoints
- Variable phenotype depending on genes involved
- **DGV (Database of Genomic Variants)** for population frequency

### Recurrent Microduplication Syndromes
| Syndrome | Locus | Key Features |
|----------|-------|--------------|
| **22q11.2 Duplication** | 22q11.2 | Variable: ID, Autism, Schizophrenia risk, Normal |
| **16p11.2 Duplication** | 16p11.2 | **Low BMI**, ID, Autism, SCZ risk, Microcephaly |
| **17p12 Duplication (CMT1A)** | 17p12 | **PMP22 duplication** → Charcot-Marie-Tooth Type 1A |
| **Xp22.3 Duplication (MECP2)** | Xq28 | **MECP2 duplication syndrome** (Males) — Severe ID, Epilepsy, Spasticity |
| **7q11.23 Duplication** | 7q11.23 | **Reciprocal of Williams** — Severe speech delay, Autism, Anxiety |
| **15q11-13 Duplication (maternal)** | 15q11-q13 | **Autism, ID, Epilepsy** (maternal dup) |

---

## 7. ️⃣ Chromosomal Instability Syndromes (DNA Repair Defects)

| Syndrome | Gene | Pathway | Key Features | Cancer Risk |
|----------|------|---------|--------------|-------------|
| **Fanconi Anaemia (FA)** | FANCA-FANCW (22 genes) | FA/BRCA pathway (ICL repair) | **Thumb/Radius anomalies**, Skin hyperpigmentation, **BM failure (median 7y)**, Microcephaly, Renal/Heart anomalies | **AML (5-10%)**, HNSCC, Gynae, GI |
| **Bloom Syndrome** | BLM | RecQ Helicase (HR) | **Photosensitivity**, Facial telangiectasia, **Short stature**, Immunodeficiency, **Sister chromatid exchanges (SCE ↑)** | **All cancers** (early onset, multiple) |
| **Ataxia-Telangiectasia (AT)** | ATM | PIKK (DSB response, HR/NHEJ) | **Cerebellar ataxia**, Oculocutaneous telangiectasia, **Immunodeficiency** (IgA/IgG2), **Radiosensitivity**, **Chromosomal breakage (7;14 translocations)** | **Lymphoma, Leukaemia** (10-30%) |
| **Nijmegen Breakage Syndrome (NBS)** | NBN (NBS1) | MRN Complex (DSB sensing) | **Microcephaly**, **Bird-like face**, Immunodeficiency, **Radiosensitivity**, **Chromosomal breakage** | **Lymphoma** (50% by 20y) |
| **LIG4 Syndrome** | LIG4 | NHEJ (Ligation) | Microcephaly, Growth retardation, Immunodeficiency, Radiosensitivity | Lymphoma |
| **DNA Ligase IV** | LIG4 | NHEJ | Similar to NBS |
| **Cernunnos/XLF** | NHEJ1 | NHEJ | Microcephaly, Growth failure, Immunodeficiency |
| **RAD50 Deficiency** | RAD50 | MRN Complex | NBS-like, Radiosensitivity |

> **All:** **Radiosensitivity** (avoid X-rays), **Chromosomal breakage** (DEB/MMC test for FA, **SCE for Bloom**), **Cancer predisposition**.

---

## 8. ⚡ FCPS/MRCP High-Yield Summary

| Topic | Key Points |
|-------|------------|
| **Down Syndrome** | Trisomy 21 (95%), Robertsonian rob(14;21) 3-4%, Mosaic 2-3%; AVSD 40-50%, AVSD, Leukaemia, Alzheimer's >40 |
| **Edwards (T18)** | 1/5000, Clenched hands, Rocker-bottom feet, Lethal by 1yr |
| **Patau (T13)** | 1/10-20K, Holoprosencephaly, Polydactyly, Cleft lip/palate, Lethal |
| **Turner (45,X)** | Short, Webbed neck, Coarctation, Streak ovaries, Bicuspid AV |
| **Klinefelter (47,XXY)** | Tall, Small testes, Azoospermia, Gynaecomastia |
| **Robertsonian Translocation** | rob(14;21) → Down risk: **Mother ~10-15%, Father ~1-2%**; rob(21;21) = 100% DS |
| **Reciprocal Translocation** | Alternate = Balanced; Adjacent = Unbalanced; Liveborn unbalanced ~5-10% |
| **22q11.2 Del (DiGeorge)** | CATCH-22: Cardiac, Abnormal facies, Thymic hypoplasia, Cleft palate, Hypocalcaemia |
| **Williams (7q11.23 del)** | Elfin facies, SVAS, Hypercalcaemia, Outgoing personality |
| **Cri-du-chat (5p-)** | Cat-like cry, Microcephaly, ID |
| **Smith-Magenis (17p11.2)** | Self-hug, Sleep disorder, Hoarse voice |
| **FA/Bloom/AT/NBS** | **Radiosensitivity**, Chromosomal breakage, **Cancer predisposition** |
| **FA** | Thumb/Radius, BM failure, DEB/MMC test |
| **Bloom** | SCE ↑, Short stature, Photosensitivity |
| **AT** | Ataxia, Telangiectasia, Radiosensitivity, 7;14 translocations, Lymphoma |
| **NBS** | Microcephaly, Bird-like face, Radiosensitivity, Lymphoma |

---

## 9. 🎤 Viva Questions (Expected Answers)

| # | Question | Expected Answer |
|---|----------|-----------------|
| 1 | Robertsonian translocation 14;21 — Down syndrome risk if mother carrier? | **~10-15%** (if father carrier ~1-2%). 6 gamete types: 1 normal, 1 balanced carrier, 1 trisomy 21, 1 monosomy 21 (lethal), 2 unbalanced other. |
| 2 | Robertsonian 21;21 — recurrence risk? | **100% Down syndrome** — All gametes carry extra 21. Carrier should not reproduce without PGT. |
| 3 | Reciprocal translocation — viable unbalanced risk? | **5-10%** (alternate segregation = balanced; adjacent-1/2 = unbalanced; 3:1 usually lethal). |
| 4 | 22q11.2 deletion — CATCH-22 mnemonic? | **C**ardiac (conotruncal), **A**bnormal facies, **T**hymic hypoplasia, **C**left palate, **H**ypocalcaemia (hypoparathyroidism). |
| 5 | Williams syndrome — cardiovascular hallmark? | **Supravalvular aortic stenosis** (SVAS); Hypercalcaemia, Elfin facies, Outgoing personality. |
| 6 | Cri-du-chat — characteristic cry? | **High-pitched, cat-like cry** (laryngeal anomaly); Microcephaly, ID. |
| 6 | Fanconi anaemia — diagnostic test? | **DEB (Diepoxybutane) or MMC (Mitomycin C) chromosome breakage test** — ↑ Chromosomal breakage. |
| 7 | Bloom syndrome — characteristic cytogenetic finding? | **Sister Chromatid Exchanges (SCE) markedly increased** (10x normal). |
| 8 | Ataxia-Telangiectasia — characteristic chromosomal abnormality? | **Reciprocal translocations involving chromosomes 7 and 14** (TCR/IG loci). |
| 9 | Reciprocal translocation carrier — recurrence risk for unbalanced liveborn? | **~5-10%** (Alternate segregation = balanced/viable; Adjacent = unbalanced). |
| 10 | Cri-du-chat — origin of name? | **High-pitched cat-like cry** (laryngeal/hypoplastic epiglottis) in infancy. |

---

## 10. 🧩 Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **"All translocations cause disease"** | **NO.** **Balanced** carriers usually phenotypically normal unless breakpoint disrupts gene. |
| **"Robertsonian 14;21 = 50% Down risk"** | **NO.** Risk depends on **parent of origin** (Mother ~15%, Father ~1-2%) due to oogenesis vs spermatogenesis selection. |
| **"All Robertsonian = 1/3 risk"** | **NO.** rob(21;21) = **100% DS**. rob(13;14) = no viable unbalanced. |
| **"Reciprocal translocation = 50% unbalanced"** | **NO.** Most unbalanced gametes non-viable → **Liveborn unbalanced risk ~5-10%**. |
| **"All 22q11.2 deletions = DiGeorge"** | **Variable** — VCFS (no cardiac), Conotruncal Anomaly Face Syndrome (CAFS) — same deletion, variable expressivity. |
| **"Mosaicism = Always milder"** | **Not always** — Can be severe if high % abnormal cells in critical tissues. |
| **"All acrocentric can form Robertsonian"** | **Only specific pairs** form Robertsonian in practice (13;14, 14;21, 21;22 most common). |
| **"Ring chromosome = Always mosaic"** | **No. Ring can be non-mosaic** but often unstable → Mosaicism in later cells. |
| **"AT = Always immunodeficiency"** | **Variable** — IgA/IgG2 deficiency common, but some have normal immunoglobulins. |
| **"FA = Only thumb anomalies"** | **NO.** Thumb/radius most visible, but **BM failure** is major cause of mortality. |

> **Mnemonic: CHROMOSOMAL DISORDERS**  
> **C**hr 21: **Down (T21)**, Rob(14;21) — M=15%, F=1%  
> **H**r 18: **Edwards** — Clenched hand, Rocker bottom, Lethal  
> **R**hr 13: **Patau** — Holoprosencephaly, Polydactyly, Lethal  
> **O**ptic Sex: **Turner (45,X) — Short/Coarctation/Streak; Klinefelter (47,XXY) — Tall/Azoospermia**  
> **M**icrodeletions: **22q11 (CATCH-22), 7q11 (Williams), 5p (Cri-du-chat), 1p36, 17p11 (SMS)**  
> **S**mith-Magenis: **Self-hug, Sleep disorder, Hoarse voice**  
> **O**ther: **16p11.2 (Autism/Obesity), 1q21.1 (Variable), 15q13 (Epilepsy)**  
> **M**osaicism: **Level matters** — Blood vs Tissue; Recurrence risk if Gonadal  
> **A**neuploidy: **T21 (95%), T18, T13, 45,X, 47,XXY/XXX/XYY**  
> **A**crocentric Robertsonian: **13/14/15/21/22** — Centric fusion  
> **L**oss: **Balanced vs Unbalanced** — Alternate viable, Adjacent lethal  
> **D**uplications: **CMT1A (17p12 PMP22 dup), MECP2 dup (Xq28), 22q11 dup**  
> **I**nstability: **FA/Bloom/AT/NBS** — **Radiosensitive, Breakage, Cancer**  
> **I**SCN: **t(2;5), rob(14;21), der(14;21)**  
> **S**creening: **Combined (NT+PAPP-A), NIPT (>99%), CFTS, Quad**  
> **O**ther: **Inversions (Pari/Peri), Rings, Dicentrics, Insertions**  
> **R**eciprocal: **Alternate (Balanced) vs Adjacent (Unbalanced)**  
> **D**iagnosis: **Karyotype + FISH + Microarray (1st tier DD/ID)**  
> **E**nd: **Genetic Counselling** — Recurrence risk, Prenatal options, PGT  
> **R**ecurrence: **Rob(14;21) Mat 15%/Pat 1%; Rob(21;21)=100%; Reciprocal ~5-10%**  
> **D**Eletion: **22q11 CATCH-22, 7q11 Williams, 5p Cri-du-chat, 1p36, 17p11 SMS**  
> **S**yndromes: **FA=DEB test, Bloom=SCE, AT=7;14 transloc, NBS=Microcephaly**  

---

## 11. 🗺️ Mind Map

```mermaid
mindmap
  root((Chromosomal Disorders))
    Aneuploidy
      Trisomy 21 (Down)
      Trisomy 18 (Edwards)
      Trisomy 13 (Patau)
      Sex Chr (45,X / 47,XXY / 47,XXX / 47,XYY)
    Structural
      Robertsonian (Acrocentric)
        rob(14;21) Mat 15% Pat 1%
        rob(21;21) = 100% DS
      Reciprocal
        Alternate vs Adjacent
        Unbalanced ~5-10%
      Inversions (Pari/Peri)
      Rings/Dicentrics/Insertions
    Microdeletions
      22q11 (CATCH-22)
      7q11 (Williams)
      5p (Cri-du-chat)
      1p36, 17p11 (SMS), 17p13 (Miller-Dieker)
      16p11.2, 1q21.1, 3q29, 15q13
    Microduplications
      22q11 dup, 16p11.2 dup (Low BMI)
      17p12 (CMT1A)
      MECP2 dup (Xq28)
    Instability Syndromes
      FA (DEB test, BM failure)
      Bloom (SCE↑)
      AT (7;14 transloc, radiosensitive)
      NBS (Microcephaly, Bird face)
```

---

## 12. 📅 Spaced Repetition Tracker

| Review | Date | Score (0–5) | Notes |
|--------|------|-------------|-------|
| Day 1 | | | |
| Day 3 | | | |
| Day 7 | | | |
| Day 14 | | | |
| Day 30 | | | |
| Day 90 | | | |

---

## 13. 📝 Self-Test Scorecard

| Section | Max | Score | % |
|---------|-----|-------|---|
| Aneuploidies (T21/18/13, Sex Chr) | 4 | | |
| Robertsonian Translocations | 3 | | |
| Reciprocal Translocations | 3 | | |
| Microdeletion Syndromes | 4 | | |
| Microduplication Syndromes | 2 | | |
| Instability Syndromes (FA/Bloom/AT/NBS) | 4 | | |
| **Total** | **20** | | |

---

## 14. 💬 Exam Answer Modes

| Format | Prompt | Key Points |
|--------|--------|------------|
| **Long Essay** | "Classify chromosomal disorders with recurrence risks." | Aneuploidy (T21/18/13, Sex), Structural (Rob/Recip/Inv/Ring), Microdeletions (22q11, 7q11, 5p, 1p36), Microduplications, Instability (FA/Bloom/AT/NBS) |
| **Short Note** | "Robertsonian translocation 14;21 — recurrence risk." | Mother carrier ~15%, Father ~1%; rob(21;21)=100%; Mechanism: centric fusion of acrocentrics. |
| **Viva** | "Newborn with cat-like cry, microcephalia, hypertelorism. Diagnosis? Genetic test?" | **Cri-du-chat (5p-)**. Test: Microarray (detects 5p del) + FISH for 5p. |
| **Ward Round** | "Couple with recurrent miscarriages. Karyotype shows balanced t(11;22). Counselling?" | Balanced reciprocal translocation. Liveborn unbalanced risk ~5-10%. Offer PGT-M. Prenatal: CVS/Amnio. |
| **Last-Night** | "T21: Trisomy (95%), Rob(14;21) M15% F1%, Rob(21;21)=100%. T18: Clench/Rocker. T13: Holo/Poly. Turner 45,X: Short/Coarct/Streak. Klinefelter 47,XXY: Tall/Azoosperm. Rob(14;21): Mat 15% F 1%. Recip: Alt bal, Adj unb ~5-10%. 22q11 CATCH-22. Williams 7q11: SVAS/HyperCa/Elfin. FA: DEB, Bloom: SCE, AT: 7;14/radiosense, NBS: Micro/Bird." | Compressed. |

---

## 15. 📌 Summary
- **Aneuploidies**: T21 (Down) 1/700, T18 (Edwards) 1/5000, T13 (Patau) 1/10-20K. Sex: Turner 45,X (1/2500 ♀), Klinefelter 47,XXY (1/600 ♂), Triple X (1/1000 ♀), XYY (1/1000 ♂).
- **Robertsonian**: Acrocentric fusion (13,14,15,21,22). **rob(14;21)** → DS risk: Mother ~15%, Father ~1-2%. **rob(21;21) = 100% DS**. Carrier karyotype 45,XX,rob(14;21).
- **Reciprocal Translocation**: Balanced exchange. **Alternate segregation = Balanced; Adjacent = Unbalanced**. Liveborn unbalanced risk ~5-10%.
- **Microdeletions**: **22q11.2 (DiGeorge/VCFS) — CATCH-22**, 7q11.23 (Williams: SVAS, HyperCa, Elfin), 5p- (Cri-du-chat), 1p36, 17p11.2 (SMS), 17p13.3 (Miller-Dieker).
- **Microduplications**: 17p12 (CMT1A), 16p11.2 dup (Low BMI/Autism), 22q11.2 dup (Variable), MECP2 dup (Xq28), 7q11.23 dup.
- **Instability Syndromes**: **FA** (DEB/MMC test, BM failure), **Bloom** (SCE↑, short stature), **AT** (7;14 transloc, radiosensitivity, lymphoma), **NBS** (Microcephaly, bird face, lymphoma). All = **Radiosensitive, Chromosomal breakage, Cancer predisposition**.
- **Recurrence Risks**: Rob(14;21) Mother ~15% / Father ~1-2%; Rob(21;21) = 100%; Reciprocal ~5-10% live unbalanced; FA/Bloom/AT/NBS = AR (25% sib recurrence).

---

## 16. ❓ MCQs (10)

1. **Robertsonian translocation 14;21 — Down syndrome risk if mother carrier?**  
   A. 1-2%  B. 25%  C. **10-15%**  D. 50%  
   *Answer: C. Maternal carrier risk ~10-15%; Paternal ~1-2%.*

2. **Reciprocal translocation — viable unbalanced offspring risk?**  
   A. 25%  B. **5-10%**  C. 50%  D. 75%  
   *Answer: B. Alternate segregation = balanced; Adjacent = unbalanced (mostly non-viable). Liveborn unbalanced ~5-10%.*

3. **22q11.2 deletion — CATCH-22 mnemonic?**  
   A. Cardiac, Abnormal facies, Thymic hypoplasia, Cleft palate, Hypocalcaemia  
   B. Cardiac, Arthritis, Thrombocytopenia, Cataracts, Hepatitis, Alkalosis  
   C. Cleft, Atresia, Tracheoesophageal, Cardiac, Hypospadias, Hypocalcaemia  
   D. Coarctation, Aneurysm, Torsion, Cystic, Hydrocephalus, Atresia  
   *Answer: A. **C**ardiac, **A**bnormal facies, **T**hymic hypoplasia, **C**left palate, **H**ypocalcaemia (parathyroid).*

4. **Williams syndrome — hallmark CV defect?**  
   A. TOF  B. VSD  C. **Supravalvular Aortic Stenosis**  D. Coarctation  
   *Answer: C. SVAS is hallmark; Also peripheral pulmonary stenosis, Hypercalcaemia, Elfin facies.*

5. **Cri-du-chat syndrome — deletion locus?**  
   A. 22q11  B. 7q11  C. **5p15**  D. 1p36  
   *Answer: C. 5p15.2 deletion (Cri-du-chat).*

5. **Fanconi anaemia — diagnostic test?**  
   A. Karyotype  B. **DEB/MMC chromosome breakage test**  C. SNP Array  D. FISH  
   *Answer: B. DEB (Diepoxybutane) or MMC (Mitomycin C) induces chromosomal breakage in FA cells.*

6. **Bloom syndrome — characteristic cytogenetic finding?**  
   A. Translocations  B. **Sister Chromatid Exchanges (SCE) ↑**  C. Dicentrics  D. Acentric fragments  
   *Answer: B. SCE markedly increased (10-100x normal) due to BLM helicase defect.*

7. **Ataxia-Telangiectasia — characteristic translocations?**  
   A. 8;14  B. 9;22  C. **7;14**  D. 11;14  
   *Answer: C. Reciprocal translocations involving TCR (14) and IGH (14) loci; also 7;14.*

8. **Robertsonian 21;21 — Down syndrome risk?**  
   A. 25%  B. **100%**  C. 50%  D. 1%  
   *Answer: B. All gametes carry extra 21 → 100% DS if carrier parent.*

9. **Nijmegen Breakage Syndrome — facial appearance?**  
   A. Elfin facies  B. **Bird-like face**  C. Coarse features  D. Coarse with hirsutism  
   *Answer: B. Microcephaly, Bird-like face (prominent midface, receding forehead).*

10. **Ataxia-Telangiectasia — deficient protein?**  
    A. FANCA  B. BLM  C. **ATM**  D. NBN  
    *Answer: C. ATM (Ataxia-Telangiectasia Mutated) — PIKK, DSB response.*

---

## 17. 📋 SBAs (10)

1. **Couple with recurrent miscarriages. Karyotype: 46,XX,t(11;22)(q23;q11). Recurrence risk for liveborn unbalanced?**  
   A. 25%  B. 50%  C. **5-10%**  D. 1%  
   *Answer: C. Reciprocal translocation carrier → Liveborn unbalanced risk ~5-10%.*

2. **Newborn: Cat-like cry, microcephaly, hypertelorism, low-set ears. Likely diagnosis?**  
   A. 22q11 del  B. **5p- (Cri-du-chat)**  C. 1p36 del  D. 17p11 del  
   *Answer: B. High-pitched cat-like cry = Cri-du-chat (5p15.2 deletion).*

3. **22q11.2 deletion — which feature is NOT part of CATCH-22?**  
   A. Cardiac (conotruncal)  B. Hypocalcaemia  C. **Renal agenesis**  D. Cleft palate  
   *Answer: C. Renal agenesis not typical for 22q11.2 del (C = Cardiac, A = Abnormal facies, T = Thymic, C = Cleft, H = Hypocalcaemia).*

4. **Couple with Down syndrome child. Karyotype: 46,XX,der(14;21)(q10;q10). Mother carrier. Recurrence risk?**  
   A. 1%  B. **10-15%**  C. 25%  D. 50%  
   *Answer: B. Maternal carrier of rob(14;21) → ~10-15% DS risk.*

5. **Child with microcephaly, bird-like face, immunodeficiency, chromosomal breakage. Gene?**  
   A. FANCA  B. BLM  C. ATM  D. **NBN**  
   *Answer: D. NBS (NBN/NBS1): Microcephaly, Bird-like face, Immunodeficiency, Radiosensitivity.*

---

## 18. 🔑 Answer Keys
| MCQs | SBAs |
|------|------|
| 1-C, 2-B, 3-A, 4-C, 5-C, 6-B, 6-B, 7-C, 8-B, 9-B, 10-C | 1-C, 2-B, 3-C, 4-B, 5-D |

---

## 19. 🔗 Cross-Links
- [[1. Fundamentals of Medical Genetics]] — Chromosome structure, ISCN, Mutation types (CNV)
- [[2.1 Mendelian Inheritance]] — Translocation carriers → Mendelian segregation risks
- [[2.2 Non-Mendelian Inheritance]] — UPD from trisomy rescue, Mosaicism
- [[4.5 Imprinting & UPD]] — 15q11-13 del (PWS/AS), 11p15 (BWS/SRS)
- [[5.1-5.4 Genetic Testing Technologies]] — Karyotype, FISH, Microarray, NGS for detection
- [[5.5 Genetic Counselling]] — Recurrence risk counselling for translocation carriers
- [[4.5 Imprinting & UPD]] — 15q11-13 (PWS/AS), 11p15 (BWS/SRS) overlap
- [[5.4 Prenatal & Preimplantation Testing]] — PND for aneuploidy/translocations, PGT for carriers
- [[6.1 Hereditary Cancer Syndromes]] — Instability syndromes (FA, Bloom, AT, NBS) → Cancer predisposition
- [[9. ELSI]] — Prenatal diagnosis ethics, PGT ethics, Discrimination

---

**Last Updated:** 2026-06-14  
**Next:** Build `4.1 Autosomal Dominant Disorders.md`, `4.2 Autosomal Recessive Disorders.md`, `4.3 X-Linked Disorders.md`
