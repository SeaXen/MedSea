---
tags: [hepatology, inherited_metabolic, haematocromatosis, fcps, mrcp]
davidson_chapter: Chapter 24
status: full-fcps-mrcp-note
priority: high
exam_relevance: "Haemochromatosis diagnosis (ferritin, transferrin saturation, genetics) and venesection - FCPS/MRCP core inherited metabolic disease"
see_also: ["Inherited and Metabolic Liver Disease/Wilson Disease", "Inherited and Metabolic Liver Disease/Alpha-1 antitrypsin deficiency", "Inherited and Metabolic Liver Disease/Porphyrias", "Chronic Liver Disease and Cirrhosis/Aetiology/Inherited metabolic disorders"]
created: 2025-06-13
modified: 2025-06-13
---

# Haemochromatosis (HFE and Non-HFE): Diagnosis & Management

## Learning Objectives
- [ ] Apply diagnostic criteria (transferrin saturation, ferritin, genetics)
- [ ] Differentiate HFE vs non-HFE haemochromatosis
- [ ] Initiate and monitor venesection therapy
- [ ] Screen family members
- [ ] Identify FCPS/MRCP high-yield complications (cirrhosis, HCC, diabetes, cardiomyopathy)

---

## Definition & Types

| Type | Gene | Inheritance | Features |
|------|------|-------------|----------|
| **Type 1 (HFE)** | **HFE (C282Y, H63D)** | **Autosomal recessive** | **90% of cases**; Adult onset; Penetrance variable |
| **Type 2A (Juvenile)** | **HJV (Hemojuvelin)** | Autosomal recessive | Severe; age 15-30; cardiac/endocrine dominant |
| **Type 2B (Juvenile)** | **HAMP (Hepcidin)** | Autosomal recessive | Severe; similar to 2A |
| **Type 3** | **TFR2** | Autosomal recessive | Intermediate severity |
| **Type 4 (Ferroportin Disease)** | **SLC40A1** | **Autosomal dominant** | High ferritin, **low/normal TSAT**, macrophage iron loading |

> **FCPS/MRCP**: **HFE Type 1 = vast majority**; Focus on C282Y homozygosity

---

## Pathophysiology

```mermaid
flowchart LR
    A[HFE Mutation (C282Y)] --> B[Impaired Hepcidin Regulation]
    B --> C[Low Hepcidin]
    C --> D[Increased Ferroportin Activity]
    D --> E[Increased Intestinal Iron Absorption]
    D --> F[Increased Macrophage Iron Release]
    E & F --> G[Systemic Iron Overload]
    G --> H[Organ Deposition: Liver, Heart, Pancreas, Joints, Pituitary, Skin]
```

**Hepcidin** = Master iron regulator (liver); suppresses ferroportin → blocks iron export from enterocytes/macrophages

---

## Diagnostic Criteria (HFE Type 1)

### Stepwise Approach

```mermaid
flowchart TD
    A[Suspect Iron Overload: Fatigue, Arthralgia, Abnormal LFTs, Diabetes, Cardiomyopathy, Skin Bronze] --> B[Step 1: Transferrin Saturation (TSAT)]
    B --> C{TSAT ≥45%?}
    C -->|No| D[Unlikely Haemochromatosis]
    C -->|Yes| E[Step 2: Serum Ferritin]
    E --> F{Ferritin >200 (women) / >300 (men)?}
    F -->|No| G[Latent Iron Overload / Monitor]
    F -->|Yes| H[Step 3: HFE Genetic Testing]
    H --> I{C282Y Homozygous?}
    I -->|Yes| J[Diagnose HFE Haemochromatosis]
    I -->|C282Y/H63D Compound Het| K[Mild Risk / Monitor]
    I -->|Negative| L[Consider Non-HFE: Juvenile, TFR2, Ferroportin]
    J --> M[Family Screening]
```

### Diagnostic Thresholds

| Test | Threshold | Significance |
|------|-----------|--------------|
| **Transferrin Saturation (TSAT)** | **≥45%** | **Screening test** (high sensitivity) |
| **Ferritin** | **>200 μg/L (women), >300 μg/L (men)** | Reflects iron stores; acute phase reactant |
| **Genetics** | **C282Y homozygous** | **Definitive for Type 1** |

---

## Genetic Testing Interpretation

| Genotype | Risk | Penetrance |
|----------|------|------------|
| **C282Y / C282Y** (Homozygous) | **High** | **Clinical disease ~10-30%** (men > women) |
| **C282Y / H63D** (Compound Heterozygous) | Low-Moderate | Mild iron overload possible |
| **H63D / H63D** (Homozygous) | Very Low | Rarely clinical |
| **C282Y / WT** (Heterozygous) | Carrier | No clinical disease |

> **Most C282Y homozygotes NEVER develop clinical disease** — penetrance incomplete

---

## Staging & Organ Involvement

### Liver
| Stage | Features |
|-------|----------|
| **Iron overload only** | Hepatomegaly, elevated ferritin, normal LFTs |
| **Fibrosis** | Progressive with iron burden |
| **Cirrhosis** | **Risk factor for HCC** (20-30% with cirrhosis) |
| **HCC** | Surveillance if cirrhosis |

### Extrahepatic
| Organ | Manifestation |
|-------|---------------|
| **Pancreas** | **Diabetes mellitus** (bronze diabetes) — insulin deficiency + resistance |
| **Heart** | **Cardiomyopathy** (restrictive → dilated); arrhythmias |
| **Pituitary** | **Hypogonadotropic hypogonadism** (loss of libido, impotence) |
| **Joints** | **Arthropathy** (MCP 2nd/3rd — "iron fist") |
| **Skin** | **Bronze pigmentation** (melanin + iron) |
| **Thyroid** | Hypothyroidism |

---

## Treatment: Venesection (Phlebotomy)

### Induction Phase
| Parameter | Detail |
|-----------|--------|
| **Volume** | **400-500 mL** per session |
| **Frequency** | **Weekly** (or twice weekly if Hb allows) |
| **Target** | **Ferritin 50-100 μg/L** |
| **Hb monitoring** | Maintain Hb >110 g/L (men), >100 g/L (women) |
| **Duration** | Months to 1-2 years (depends on iron burden) |

### Maintenance Phase
| Parameter | Detail |
|-----------|--------|
| **Frequency** | **Every 3-4 months** (adjust to keep ferritin 50-100) |
| **Volume** | 400-500 mL |
| **Lifelong** | Yes |

### Chelation (If Venesection Contraindicated)
| Drug | Dose | Indication |
|------|------|------------|
| **Deferasirox** | 20-30 mg/kg/day | Anaemia, cardiac failure, poor venous access |
| **Deferoxamine** | 40-50 mg/kg/day SC/IV | Alternative |

---

## Family Screening

| Relative | Testing |
|----------|---------|
| **First-degree (parents, siblings, children)** | **TSAT + Ferritin + HFE Genotyping** |
| **C282Y homozygote proband** | Siblings: 25% chance homozygous |
| **Children** | Test partner first; if partner negative → children only carriers |

> **Screen ALL first-degree relatives** — early detection prevents organ damage

---

## Complications & Surveillance

| Complication | Surveillance |
|--------------|--------------|
| **Liver Fibrosis/Cirrhosis** | **Transient Elastography (FibroScan)** or **Liver Biopsy** if ferritin >1000 or LFTs elevated |
| **HCC** | **If Cirrhosis: 6-monthly US ± AFP** |
| **Diabetes** | Annual HbA1c / Fasting glucose |
| **Cardiomyopathy** | Echo if symptoms; baseline at diagnosis |
| **Hypogonadism** | Testosterone, LH, FSH if symptoms |
| **Arthropathy** | Clinical; X-ray MCP joints |
| **Osteoporosis** | DEXA (iron + hypogonadism) |

---

## FCPS/MRCP High-Yield Summary

| Concept | Key Points |
|---------|------------|
| **Gene** | **HFE (C282Y)** — Autosomal recessive |
| **Screening** | **TSAT ≥45%** → Ferritin → **Genetics** |
| **Definitive** | **C282Y homozygote** |
| **Penetrance** | **Incomplete** (10-30% clinical disease) |
| **Target Organs** | Liver (cirrhosis, HCC), Pancreas (DM), Heart (CM), Pituitary (Hypogonadism), Joints (MCP), Skin (Bronze) |
| **Treatment** | **Venesection 400-500mL weekly → ferritin 50-100 → maintenance 3-4 monthly** |
| **Chelation** | Deferasirox if venesection contraindicated |
| **Screening** | **All first-degree relatives** (TSAT + Ferritin + Genetics) |
| **HCC** | Cirrhosis = 6m US ± AFP |

---

## Viva Questions

1. **What is the diagnostic pathway for haemochromatosis?**
2. **What TSAT and ferritin thresholds trigger genetic testing?**
3. **What does C282Y homozygous mean? What about compound heterozygous?**
4. **What is the penetrance of HFE haemochromatosis?**
5. **Describe the venesection protocol (induction and maintenance).**
6. **When do you use chelation instead of venesection?**
7. **What are the extrahepatic manifestations?**
8. **What is the "iron fist" arthropathy?**
9. **Who needs family screening and what tests?**
10. **HCC surveillance in haemochromatosis?**

---

## Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| TSAT vs Ferritin | **TSAT = screening** (early, sensitive); **Ferritin = iron stores** (also acute phase reactant) |
| C282Y homozygous vs compound het | Homozygous = high risk; Compound het = mild risk |
| Penetrance | **Most C282Y homozygotes asymptomatic** — low clinical penetrance |
| Venesection target | **Ferritin 50-100 μg/L** (not "normal") — mild iron deficiency prevents re-accumulation |
| Ferroportin disease (Type 4) | **Autosomal dominant**; **High ferritin, LOW/normal TSAT** (macrophage iron trapping) |
| Juvenile haemochromatosis | HJV/HAMP; severe; teens/20s; cardiac/endocrine dominant |
| Bronze diabetes | **Pancreatic iron → DM + Skin bronze** (melanin + iron) |
| MCP arthropathy | **2nd/3rd MCP joints** — characteristic |

---

## Mind Map

```mermaid
mindmap
  root((Haemochromatosis))
    Type 1 (HFE)
      C282Y / C282Y = High risk
      C282Y / H63D = Mild
      Penetrance incomplete
    Non-HFE
      Type 2: Juvenile (HJV, HAMP)
      Type 3: TFR2
      Type 4: Ferroportin (AD, high Ferritin, normal TSAT)
    Diagnosis
      TSAT >=45% -> Ferritin -> Genetics
      C282Y Homozygous = Definitive
    Treatment
      Venesection 400-500mL weekly
      Target Ferritin 50-100
      Maintenance 3-4 monthly
      Chelation if contraindicated
    Complications
      Liver: Cirrhosis, HCC
      Pancreas: Diabetes
      Heart: Cardiomyopathy
      Pituitary: Hypogonadism
      Joints: MCP (Iron Fist)
      Skin: Bronze
    Screening
      First-degree relatives: TSAT + Ferritin + Genetics
```

---

## One-Page Revision Card

| **Diagnostic Pathway** | **Threshold** |
|------------------------|---------------|
| TSAT (Screening) | **≥45%** |
| Ferritin (Women) | **>200 μg/L** |
| Ferritin (Men) | **>300 μg/L** |
| Genetics | **C282Y Homozygous = Definitive** |

| **Genotype** | **Risk** |
|--------------|----------|
| C282Y / C282Y | High (10-30% clinical) |
| C282Y / H63D | Low-Moderate |
| H63D / H63D | Very Low |

| **Venesection** | **Details** |
|-----------------|-------------|
| Induction | 400-500mL weekly → Ferritin 50-100 |
| Maintenance | 400-500mL every 3-4 months |
| Hb Floor | 110 (men) / 100 (women) g/L |

| **Complications** | **Surveillance** |
|-------------------|------------------|
| Cirrhosis / HCC | FibroScan/Biopsy; 6m US if cirrhotic |
| Diabetes | Annual HbA1c |
| Cardiomyopathy | Echo if symptoms |
| Hypogonadism | Testosterone/LH/FSH if symptomatic |
| Arthropathy | MCP 2nd/3rd (Iron Fist) |

---

## Spaced Repetition Tracker

| Day | 1 | 3 | 7 | 15 | 30 |
|-----|---|---|---|----|----|
| TSAT/Ferritin thresholds | ☐ | ☐ | ☐ | ☐ | ☐ |
| C282Y genotypes | ☐ | ☐ | ☐ | ☐ | ☐ |
| Venesection protocol | ☐ | ☐ | ☐ | ☐ | ☐ |
| Extrahepatic manifestations | ☐ | ☐ | ☐ | ☐ | ☐ |
| Family screening | ☐ | ☐ | ☐ | ☐ | ☐ |

---

## Self-Test Scorecard

| Question | My Answer | Correct? |
|----------|-----------|----------|
| TSAT threshold |  |  |
| C282Y homozygous vs compound het |  |  |
| Penetrance |  |  |
| Venesection target ferritin |  |  |
| Extrahepatic manifestations |  |  |

---

## Local Navigation

- [[Inherited and Metabolic Liver Disease/Wilson Disease|Wilson Disease]]
- [[Inherited and Metabolic Liver Disease/Alpha-1 antitrypsin deficiency|Alpha-1 AT]]
- [[Inherited and Metabolic Liver Disease/Porphyrias|Porphyrias]]
- [[Chronic Liver Disease and Cirrhosis/Aetiology|Inherited Metabolic in Cirrhosis]]
---

> Auto-generated study sections for "Inherited and Metabolic Liver Disease" — Ch 23: Hepatology.

## Flashcards (24 generated)

- Q: What is the definition of Inherited and Metabolic Liver Disease?
  A: # Haemochromatosis (HFE and Non-HFE): Diagnosis & Management
- Q: What is Volume of Inherited and Metabolic Liver Disease?
  A: 400-500 mL per session
- Q: What is Frequency of Inherited and Metabolic Liver Disease?
  A: Weekly (or twice weekly if Hb allows)
- Q: What is Target of Inherited and Metabolic Liver Disease?
  A: Ferritin 50-100 μg/L
- Q: How is Inherited and Metabolic Liver Disease monitored?
  A: Maintain Hb >110 g/L (men), >100 g/L (women)
- Q: What is Duration of Inherited and Metabolic Liver Disease?
  A: Months to 1-2 years (depends on iron burden)
- Q: What is Liver Fibrosis/Cirrhosis of Inherited and Metabolic Liver Disease?
  A: Transient Elastography (FibroScan) or Liver Biopsy if ferritin >1000 or LFTs elevated
- Q: What is HCC of Inherited and Metabolic Liver Disease?
  A: If Cirrhosis: 6-monthly US ± AFP
- Q: What is Diabetes of Inherited and Metabolic Liver Disease?
  A: Annual HbA1c / Fasting glucose
- Q: What is Cardiomyopathy of Inherited and Metabolic Liver Disease?
  A: Echo if symptoms; baseline at diagnosis
- Q: What is Hypogonadism of Inherited and Metabolic Liver Disease?
  A: Testosterone, LH, FSH if symptoms
- Q: What is Arthropathy of Inherited and Metabolic Liver Disease?
  A: Clinical; X-ray MCP joints
- Q: What is Osteoporosis of Inherited and Metabolic Liver Disease?
  A: DEXA (iron + hypogonadism)
- Q: What is Volume of Inherited and Metabolic Liver Disease?
  A: 400-500 mL per session
- Q: What is Frequency of Inherited and Metabolic Liver Disease?
  A: Weekly (or twice weekly if Hb allows)
- Q: What is Target of Inherited and Metabolic Liver Disease?
  A: Ferritin 50-100 μg/L
- Q: How is Inherited and Metabolic Liver Disease monitored?
  A: Maintain Hb >110 g/L (men), >100 g/L (women)
- Q: What is Liver Fibrosis/Cirrhosis of Inherited and Metabolic Liver Disease?
  A: Transient Elastography (FibroScan) or Liver Biopsy if ferritin >1000 or LFTs elevated
- Q: What is HCC of Inherited and Metabolic Liver Disease?
  A: If Cirrhosis: 6-monthly US ± AFP
- Q: What is Diabetes of Inherited and Metabolic Liver Disease?
  A: Annual HbA1c / Fasting glucose
- Q: What is Cardiomyopathy of Inherited and Metabolic Liver Disease?
  A: Echo if symptoms; baseline at diagnosis
- Q: What is Hypogonadism of Inherited and Metabolic Liver Disease?
  A: Testosterone, LH, FSH if symptoms
- Q: What is Arthropathy of Inherited and Metabolic Liver Disease?
  A: Clinical; X-ray MCP joints
- Q: What is Osteoporosis of Inherited and Metabolic Liver Disease?
  A: DEXA (iron + hypogonadism)

## MCQs (1 generated)

1. **Which of the following best describes Inherited and Metabolic Liver Disease?**
   A. **# Haemochromatosis (HFE and Non-HFE): Diagnosis & Management**
   B. An unrelated condition not matching the clinical picture of Inherited and Metabolic Liver Disease
   C. A complication seen late in the disease course of Inherited and Metabolic Liver Disease
   D. A condition that mimics Inherited and Metabolic Liver Disease but has a different underlying cause

## SBA Questions (1 generated)

1. A patient with suspected Inherited and Metabolic Liver Disease presents with: Type 1 (HFE) — HFE (C282Y, H63D); Type 2A (Juvenile) — HJV (Hemojuvelin); Type 2B (Juvenile) — HAMP (Hepcidin). What is the most likely diagnosis?
   A. **Inherited and Metabolic Liver Disease**
   B. A condition that mimics Inherited and Metabolic Liver Disease but is not the same entity
   C. A complication of Inherited and Metabolic Liver Disease rather than the primary diagnosis
   D. An unrelated condition in the same clinical category as Inherited and Metabolic Liver Disease

