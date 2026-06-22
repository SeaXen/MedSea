## 1. Learning Objectives
- [ ] Apply RUCAM (Roussel Uclaf Causality Assessment Method) for causality assessment
- [ ] Systematically exclude alternative causes of liver injury
- [ ] Identify key diagnostic criteria for DILI
- [ ] Apply FCPS/MRCP high-yield diagnostic approach

---

## 2. DILI Diagnosis: Two-Stage Process

```mermaid
flowchart TD
    A[Suspect DILI] --> B[Stage 1: Exclusion of Alternative Causes]
    B --> C[Viral Serology: HAV, HBV, HCV, HEV, EBV, CMV, HSV]
    B --> C1[Autoimmune: ANA, SMA, LKM1, IgG, AMA]
    B --> C2[Metabolic: Wilson (Ceruloplasmin, Cu), HFE, Alpha-1 AT]
    B --> C3[Vascular: US Doppler (Budd-Chiari, PVT)]
    B --> C4[Alcohol: History, GGT, AST:ALT>2, CDT]
    B --> C5[Other: Pregnancy (AFLP/HELLP), Infiltrative, Sepsis]
    C --> D{Alternative Cause Found?}
    D -->|Yes| E[Treat Alternative Cause]
    D -->|No| F[Stage 2: RUCAM Causality Assessment]
    F --> G[RUCAM Score]
    G --> H{Causality ≥6?}
    H -->|Yes| I[Probable/Definite DILI]
    H -->|No| J[Unlikely DILI → Reconsider Alternatives]
```

---

## 3. Stage 1: Exclusion of Alternative Causes

### Essential Exclusion Panel
| Category | Tests |
|----------|-------|
| **Viral Hepatitis** | HAV IgM, HBsAg, anti-HBc IgM, HCV Ab, HCV RNA, HEV IgM, HEV RNA, EBV/CMV/HSV Serology |
| **Autoimmune** | **ANA, SMA, LKM1, IgG, AMA** (Rule Out AIH, PBC, IgG4-SC) |
| **Metabolic** | **Ceruloplasmin, 24h Urinary Copper** (Wilson), **Ferritin, TSAT, HFE Genotyping** (Haemochromatosis), **Alpha-1 AT Level/Phenotype** |
| **Vascular** | **US Doppler** (Portal/Hepatic Vein Thrombosis, Budd-Chiari) |
| **Alcohol** | History, CDT, PEth, AST:ALT >2, GGT↑ |
| **Other** | Pregnancy Test (AFLP/HELLP), Sepsis Screen, Infiltrative (CT/MRI) |

> **FCPS/MRCP**: **DILI = Diagnosis of Exclusion** — Must Rule Out Above Before Attributing to Drug

---

## 4. Stage 2: RUCAM (Roussel Uclaf Causality Assessment Method)

> **Standardised, Validated Tool** for DILI Causality Assessment

### RUCAM Components (7 Domains)

```mermaid
flowchart TD
    A[RUCAM Total Score] --> B[1. Time to Onset]
    A --> C[2. Course After Cessation (Dechallenge)]
    A --> D[3. Risk Factors]
    A --> E[4. Concomitant Drugs]
    A --> F[5. Exclusion of Other Causes]
    A --> G[6. Previous Information on Drug]
    A --> H[7. Response to Rechallenge]
```

### Detailed Scoring (Original RUCAM)

| Domain | Criteria | Points |
|--------|----------|--------|
| **1. Time to Onset** (From Drug Start to ALT Rise) | 5-90 days (5-180 for Phenytoin/Valproate) | **+2** |
| | <5 or >90 days (>180 for Phenytoin/Valproate) | **+1** |
| **2. Course After Cessation (Dechallenge)** | ALT ↓≥50% within 8 days | **+3** |
| | ALT ↓≥50% within 30 days | **+2** |
| | No Information | **0** |
| | No Decrease / Increase | **-2** |
| **3. Risk Factors** | Alcohol Use OR Age ≥55 | **+1** |
| | Neither | **0** |
| **4. Concomitant Drugs** | None | **0** |
| | Possible (Same Timing) | **-1** |
| | Probable | **-2** |
| | Highly Probable | **-3** |
| **5. Exclusion of Other Causes** | All 6 Ruled Out (Viral A/B/C/E, Alcohol, AIH, Metabolic, Vascular, Pregnancy) | **+2** |
| | 5 of 6 Ruled Out | **+1** |
| | 4 of 6 Ruled Out | **-1** |
| | Non-Drug Cause Highly Probable | **-3** |
| **6. Previous Information on Drug** | Reaction in Package Insert | **+2** |
| | Published Cases but Not in Label | **+1** |
| | Unknown | **0** |
| **7. Response to Rechallenge** | Positive (ALT Doubles with Drug Alone) | **+3** |
| | Positive (Clinical Only) | **+1** |
| | Negative | **-2** |
| | Not Done | **0** |

### Total Score Interpretation
| Total Score | Causality Level |
|-------------|-----------------|
| **≥9** | **Highly Probable** |
| **6-8** | **Probable** |
| **3-5** | Possible |
| **1-2** | Unlikely |
| **≤0** | Excluded |

> **FCPS/MRCP**: **RUCAM ≥6 = Probable/Definite DILI**; **RUCAM is Standardised Tool** for Causality

---

## 5. Updated RUCAM (2016) — Key Changes

| Domain | Original | Updated (2016) |
|--------|----------|----------------|
| **Time to Onset** | 5-90d = +2; <5 or >90 = +1 | 5-90d = +2; <5 or >90 = +1 (Same) |
| **Dechallenge** | ≥50% in 8d = +3; ≥50% in 30d = +2; None = -2 | Same |
| **Risk Factors** | Alcohol + Age≥55 = +1 | Alcohol + Age≥55 = +1 (Same) |
| **Concomitant Drugs** | None=0, Possible=-1, Probable=-2, Highly=-3 | Same |
| **Exclusion** | All 6 = +2; 5=+1; 4=-1; Non-drug=-3 | **All 7** (Added Pregnancy) = +2; 6=+1; 5=0; 4=-1; 3=-2; <3=-3 |
| **Previous Info** | Label=+2, Published=+1, Unknown=0 | Same |
| **Rechallenge** | Positive=+3, Clinical=+1, Negative=-2, Not Done=0 | Same |

---

## 6. Practical Diagnostic Approach

```mermaid
flowchart TD
    A[Patient with Acute Liver Injury + Drug Exposure] --> B[Detailed Drug History]
    B --> C[Timeline: Drug Start → Symptom Onset → Presentation]
    C --> D[Exclusion Panel: Viral, Autoimmune, Metabolic, Vascular, Alcohol]
    D --> E{Alternative Cause?}
    E -->|Yes| F[Treat Alternative]
    E -->|No| G[Calculate RUCAM]
    G --> H{RUCAM ≥6?}
    H -->|Yes| I[Probable/Definite DILI → STOP Drug]
    H -->|No| J[Consider Alternative / Monitor]
    I --> K[Stop Suspect Drug(s)]
    K --> L[Monitor LFTs 2-3x/Week Until Improving]
    L --> M{Improving?}
    M -->|Yes| N[Continue Monitoring, Rechallenge if Essential]
    M -->|No| O[Reassess Causality / Consider Biopsy]
```

---

## 7. Key Exclusion Diagnoses (Must Rule Out)

| Diagnosis | Key Exclusion Tests |
|-----------|---------------------|
| **Acute Viral Hepatitis** | HAV IgM, HBsAg, anti-HBc IgM, HCV Ab/RNA, HEV IgM |
| **Autoimmune Hepatitis** | ANA, SMA, LKM1, IgG, Liver Biopsy (Interface Hepatitis) |
| **PBC** | AMA, ALP, Biopsy (Florid Duct Lesion) |
| **PSC** | MRCP (Beading), Exclude Secondary Sclerosing Cholangitis |
| **Wilson Disease** | Ceruloplasmin <20, 24h Urine Cu >100, KF Rings, ATP7B Mutations |
| **Haemochromatosis** | TSAT >45%, Ferritin >300/200, HFE C282Y Homozygous |

*...continued (truncated for renderer performance)*
---

> Auto-generated study sections for "Drug Induced Liver Injury" — Ch 23: Hepatology.

## Flashcards (1 generated)

- Q: What is the definition of Drug Induced Liver Injury?
  A: | Viral Hepatitis | HAV IgM, HBsAg, anti-HBc IgM, HCV Ab, HCV RNA, HEV IgM, HEV RNA, EBV/CMV/HSV Serology |

## MCQs (1 generated)

1. **Which of the following best describes Drug Induced Liver Injury?**
   A. **| Viral Hepatitis | HAV IgM, HBsAg, anti-HBc IgM, HCV Ab, HCV RNA, HEV IgM, HEV RNA, EBV/CMV/HSV Serology |**
   B. An unrelated condition not matching the clinical picture of Drug Induced Liver Injury
   C. A complication seen late in the disease course of Drug Induced Liver Injury
   D. A condition that mimics Drug Induced Liver Injury but has a different underlying cause

