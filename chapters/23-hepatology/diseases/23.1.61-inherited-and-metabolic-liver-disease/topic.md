> [!tip] **FCPS/MRCP Priority: HIGH**
> **Inherited & Metabolic Liver Disease** — **Wilson** (ceruloplasmin, 24h urinary copper, ATP7B, penicillamine/trientine/zinc), **Haemochromatosis** (HFE C282Y/H63D, ferritin/TSAT, venesection), **Alpha-1 AT deficiency** (PiZZ, serum level <11 µmol/L, augmentation), **Gilbert/Crigler-Najjar/Dubin-Johnson/Rotor**, **Porphyrias** (AIP, VP, HCP, PCT).

---

## 1. Learning Objectives
By the end of this note you should be able to:
- [ ] Diagnose **Wilson disease**: ceruloplasmin <20 mg/dL, 24h urinary copper >100 µg, ATP7B mutations, Kayser-Fleischer rings
- [ ] Manage **Wilson** with **chelators (penicillamine/trientine)** and **zinc** maintenance
- [ ] Diagnose **Haemochromatosis**: **HFE C282Y/H63D**, ferritin >1000, TSAT >45%, **venesection** therapy
- [ ] Recognise **Alpha-1 Antitrypsin Deficiency**: PiZZ phenotype, serum level <11 µmol/L, **augmentation therapy**
- [ ] Distinguish **inherited hyperbilirubinaemias**: Gilbert, Crigler-Najjar (I/II), Dubin-Johnson, Rotor
- [ ] Classify **Porphyrias**: Acute (AIP, VP, HCP) vs Cutaneous (PCT, EPP, CEP); diagnose with PBG/urinary porphyrins

---

## 1. Wilson Disease

### Genetics & Pathophysiology
- **Gene**: **ATP7B** (chromosome 13) — copper-transporting ATPase
- **Inheritance**: **Autosomal recessive**
- **Defect**: Impaired copper excretion into bile → copper accumulation in liver → brain, cornea, kidneys, joints

### Diagnostic Criteria (Leipzig Score)

| Parameter | Normal | Wilson Disease |
|-----------|--------|----------------|
| **Ceruloplasmin** | 20-40 mg/dL | **<20 mg/dL** (low in 85-95%) |
| **24h Urinary Copper** | <40 µg/24h | **>100 µg/24h** (100-2000) |
| **Kayser-Fleischer Rings** | Absent | **Present** (95% neuro, 50% hepatic) |
| **Hepatic Copper** | <50 µg/g dry weight | **>250 µg/g** dry weight |
| **ATP7B Mutations** | None detected | **Two pathogenic mutations** |

**Leipzig Score ≥4 = Wilson Disease**

### Clinical Presentations
| Type | Age | Features |
|------|-----|----------|
| **Hepatic** | 5-35 yrs | Acute hepatitis, acute liver failure, chronic hepatitis, cirrhosis |
| **Neurological** | 15-45 yrs | Tremor (wing-beating), dystonia, dysarthria, psychiatric, parkinsonism |
| **Mixed** | 10-30 yrs | Both hepatic + neurological |
| **Acute Liver Failure** | <18 yrs | **Fulminant** with Coombs-negative haemolytic anaemia, low ALP:bilirubin ratio (<2) |

### Treatment

| Drug | Dose | Indication | Monitoring |
|------|------|------------|------------|
| **Penicillamine** | 500-1500 mg/day (divided) | **First-line chelator** | FBC, U&E, LFT, proteinuria q3mo |
| **Trientine** | 750-1500 mg/day (divided) | **If penicillamine intolerant** | FBC, U&E, LFT q3mo |
| **Zinc (Acetate/Sulfate)** | **50 mg elemental Zn TDS** (150 mg/day) | **Maintenance** (after decoppering) OR **Initial if mild/presymptomatic** | 24h urinary copper, zinc level q6mo |

> **Decoppering phase**: Chelator until 24h urinary copper <100 µg/24h + normal LFTs (6-18 months)
> **Maintenance**: Zinc lifelong (or low-dose chelator if zinc intolerance)
> **Pregnancy**: Continue zinc; reduce penicillamine/trientine dose; avoid teratogenicity

### Neurological Wilson — Special Considerations
- **Penicillamine** can **worsen** neurological symptoms initially (in 20-50%) → start **low dose (250mg) + pyridoxine 25mg**
- **Trientine** preferred if neurological presentation
- **Zinc** as adjunct

---

## 2. Haemochromatosis

### Classification
| Type | Gene | Inheritance | Features |
|------|------|-------------|----------|
| **Type 1 (Classic)** | **HFE** (C282Y, H63D) | **Autosomal recessive** | **Most common**; Northern European |
| **Type 2A (Juvenile)** | **HJV** (hemojuvelin) | AR | Severe, onset <30, cardiomyopathy, hypogonadism |
| **Type 2B (Juvenile)** | **HAMP** (hepcidin) | AR | Similar to 2A |
| **Type 3** | **TFR2** | AR | Similar to Type 1 but earlier |
| **Type 4 (Ferroportin Disease)** | **SLC40A1** | **Autosomal dominant** | High ferritin, low/normal TSAT, macrophage iron loading |

### HFE Haemochromatosis (Type 1) — Diagnostic Criteria

| Test | Normal | Haemochromatosis |
|------|--------|------------------|
| **Transferrin Saturation (TSAT)** | 20-45% | **>45%** (often >80%) |
| **Serum Ferritin** | M: 30-300 µg/L; F: 15-200 µg/L | **>1000 µg/L** (if >1000 + TSAT>45% = 95% PPV) |
| **HFE Genotype** | Wild type | **C282Y Homozygous** (90%); **C282Y/H63D Compound Het** (5%); C282Y Het (carrier) |

### Diagnostic Algorithm

```mermaid
flowchart TD
    A[Suspected Haemochromatosis] --> B{TSAT >45%?}
    B -->|No| C[Unlikely Haemochromatosis]
    B -->|Yes| D[Check Ferritin]
    D -->|Ferritin >1000| E[HFE Genotyping]
    D -->|Ferritin 300-1000| F[Consider other causes: Alcohol, MetS, Inflammation, Liver disease]
    F -->|Other causes excluded| E
    E --> G{C282Y Homozygous?}
    G -->|Yes| H[Hereditary Haemochromatosis Confirmed]
    G -->|Compound Het (C282Y/H63D)| I[Milder phenotype; monitor]
    G -->|Het only| J[Carrier; not clinical haemochromatosis]
```

### Treatment: Venesection (Phlebotomy)

| Phase | Protocol |
|-------|----------|
| **Induction** | **500 mL weekly** until **Ferritin <50 µg/L** and **TSAT <50%** |
| **Maintenance** | **500 mL every 2-4 months** (adjust to keep Ferritin 50-100 µg/L, TSAT <50%) |

| Monitoring | Frequency |
|------------|-----------|
| **Ferritin, TSAT, Hb, FBC** | **Each venesection** |
| **LFTs, Glucose, Cardiac echo** | 6-12 monthly |
| **HCC Surveillance** | **If cirrhosis present**: 6-monthly US ± AFP |

### Complications
- **Cirrhosis** → HCC risk (20-30%)
- **Diabetes** ("Bronze diabetes") — pancreatic iron deposition
- **Cardiomyopathy** — restrictive
- **Hypogonadism** — pituitary iron
- **Arthropathy** — MCP joints (2nd/3rd), chondrocalcinosis
- **Skin pigmentation** — "Bronze" skin

> **Screening**: First-degree relatives → TSAT + Ferritin + HFE genotyping

---

## 3. Alpha-1 Antitrypsin Deficiency (A1AT)

### Genetics
- **Gene**: **SERPINA1** (chromosome 14)
- **Inheritance**: **Autosomal co-dominant**
- **Alleles**: **M** (normal), **Z** (Glu342Lys, misfolded polymer), **S** (Glu264Val, reduced secretion)
- **Phenotypes**: **MM** (normal), **MZ** (carrier, ~20% population), **SZ** (intermediate), **ZZ** (severe deficiency, 1:2500 Caucasians)

### Clinical Features
| System | Features |
|--------|----------|
| **Liver** | Neonatal cholestasis, childhood cirrhosis, adult cirrhosis (ZZ), HCC risk |
| **Lung** | **Panacinar emphysema** (basal predominant), onset 30-40y (smokers earlier), no smoking → later onset |
| **Other** | Panniculitis, ANCA+ vasculitis, panniculitis |

### Diagnosis

| Test | Normal | ZZ Deficiency |
|------|--------|---------------|
| **Serum A1AT Level** | **20-53 µmol/L** (20-48 mg/dL) | **<11 µmol/L** (<57 mg/dL) |
| **Phenotype** | **MM** | **ZZ** |
| **Genotype** | MM | **ZZ** |

> **SZ phenotype**: Level 11-20 µmol/L; increased risk if smoker

### Management

| System | Intervention |

*...continued (truncated for renderer performance)*