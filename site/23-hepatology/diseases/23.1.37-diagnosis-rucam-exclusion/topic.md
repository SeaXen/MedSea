---
tags: [hepatology, drug_induced_liver_injury, dilf, diagnosis, rucam, fcps, mrcp]
davidson_chapter: Chapter 24
status: full-fcps-mrcp-note
priority: high
exam_relevance: "DILI diagnosis using RUCAM and exclusion of alternatives - FCPS/MRCP diagnostic approach"
see_also: ["Drug-Induced Liver Injury/Classification and patterns", "Drug-Induced Liver Injury/Common culprit drugs", "Drug-Induced Liver Injury/Management and rechallenge", "Acute Liver Failure/Paracetamol-induced hepatotoxicity", "Acute Liver Failure/Non-paracetamol drug-induced liver injury", "Jaundice and LFT Interpretation/DILI patterns"]
created: 2025-06-13
modified: 2025-06-13
---

# DILI Diagnosis: RUCAM and Exclusion

## Learning Objectives
- [ ] Apply RUCAM (Roussel Uclaf Causality Assessment Method) for causality assessment
- [ ] Systematically exclude alternative causes of liver injury
- [ ] Identify key diagnostic criteria for DILI
- [ ] Apply FCPS/MRCP high-yield diagnostic approach

---

## DILI Diagnosis: Two-Stage Process

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

## Stage 1: Exclusion of Alternative Causes

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

## Stage 2: RUCAM (Roussel Uclaf Causality Assessment Method)

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

## Updated RUCAM (2016) — Key Changes

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

## Practical Diagnostic Approach

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

## Key Exclusion Diagnoses (Must Rule Out)

| Diagnosis | Key Exclusion Tests |
|-----------|---------------------|
| **Acute Viral Hepatitis** | HAV IgM, HBsAg, anti-HBc IgM, HCV Ab/RNA, HEV IgM |
| **Autoimmune Hepatitis** | ANA, SMA, LKM1, IgG, Liver Biopsy (Interface Hepatitis) |
| **PBC** | AMA, ALP, Biopsy (Florid Duct Lesion) |
| **PSC** | MRCP (Beading), Exclude Secondary Sclerosing Cholangitis |
| **Wilson Disease** | Ceruloplasmin <20, 24h Urine Cu >100, KF Rings, ATP7B Mutations |
| **Haemochromatosis** | TSAT >45%, Ferritin >300/200, HFE C282Y Homozygous |
| **Alpha-1 AT Deficiency** | Serum A1AT <11 μM, PiZZ Genotype |
| **Alcoholic Hepatitis** | History, AST:ALT>2, GGT↑, CDT/PEth |
| **Acute Fatty Liver of Pregnancy** | Pregnancy, 3rd Trimester, Hypoglycaemia, Uric Acid↑, Coagulopathy |
| **Ischaemic Hepatitis** | Shock/Hypotension History, Rapid ALT Rise/Fall, Lactate↑ |
| **Budd-Chiari / PVT** | US Doppler (Hepatic Vein Thrombosis / Portal Vein Thrombosis) |

---

## FCPS/MRCP High-Yield Summary

| Concept | Key Points |
|---------|------------|
| **DILI = Diagnosis of Exclusion** | Must Rule Out Viral, AIH, Wilson, Alcohol, Vascular, Pregnancy |
| **RUCAM** | Standardised Causality Tool; **≥6 = Probable/Definite** |
| **RUCAM Domains** | 7 (Time Onset, Dechallenge, Risk Factors, Concomitant Drugs, Exclusion, Previous Info, Rechallenge) |
| **RUCAM Score** | ≥9 Definite, 6-8 Probable, 3-5 Possible, 1-2 Unlikely, ≤0 Excluded |
| **Key Exclusions** | Viral (A/B/C/E), AIH, Wilson, Haemochromatosis, Alcohol, Vascular, Pregnancy |
| **RUCAM ≥6** | Probable/Definite DILI — **STOP Drug** |
| **RUCAM ≤0** | Excluded — Look Elsewhere |
| **RUCAM 2016 Update** | Added Pregnancy as 7th Exclusion Category |

---

## Viva Questions

1. **What are the 7 domains of RUCAM?**
2. **What RUCAM score indicates probable/definite DILI?**
3. **List the 7 causes you must exclude before diagnosing DILI.**
3. **What is the RUCAM score for "Highly Probable"?**
4. **How does RUCAM 2016 differ from original?**
4. **What is the dechallenge scoring in RUCAM?**
5. **How does a concomitant drug affect RUCAM score?**
6. **What RUCAM score means "DILI excluded"?**
7. **What exclusive causes must be ruled out for DILI diagnosis?**
8. **How does rechallenge affect RUCAM score?**
9. **What is the RUCAM score threshold for probable DILI?**
10. **List the 7 RUCAM domains.**

---

## Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| RUCAM Score Thresholds | **≥9 Definite, 6-8 Probable, 3-5 Possible, 1-2 Unlikely, ≤0 Excluded** |
| Dechallenge | **ALT ↓50% in 8d = +3** (Best); **30d = +2**; **None = 0**; **Worse = -2** |
| Concomitant Drugs | None=0; Possible=-1; Probable=-2; Highly Probable=-3 |
| Exclusion (2016) | **7 Categories** (Added Pregnancy); All 7 = +2; Non-drug = -3 |
| Rechallenge Positive | ALT Doubles with Drug Alone = +3; Clinical Only = +1; Negative = -2 |
| RUCAM for ALF | Used for Non-PCM DILI-ALF; PCM ALF Uses King's College |
| DILI vs AIH | AIH = IgG↑, AutoAbs+, Steroid Responsive; DILI = Drug Temporal Relation, RUCAM |
| DILI vs Viral | Viral = Serology+, No Drug Temporal Relation; DILI = Drug Timeline, RUCAM |
| RUCAM Threshold | **≥6 = Probable/Definite** (Action: STOP Drug) |
| RUCAM Updated | 2016 Version Added Pregnancy as 7th Exclusion Category |

---

## Mind Map

```mermaid
mindmap
  root((DILI Diagnosis))
    Stage 1: Exclusion
      Viral: HAV/HBV/HCV/HEV/EBV/CMV
      Autoimmune: ANA, SMA, LKM1, IgG, AMA
      Metabolic: Wilson (Cerulo, Cu), HFE, Alpha-1 AT
      Vascular: US Doppler (Budd-Chiari, PVT)
      Alcohol: History, CDT, AST:ALT>2
      Other: Pregnancy, Sepsis, Infiltrative
    Stage 2: RUCAM
      1. Time Onset (5-90d +2)
      2. Dechallenge (8d +3, 30d +2)
      3. Risk Factors (Alcohol/Age>55)
      4. Concomitant Drugs (-1 to -3)
      5. Exclusion (7 Categories, All +2)
      6. Previous Info (Label +2)
      7. Rechallenge (+3/+1/-2/0)
    Scoring
      >=9 Definite
      6-8 Probable
      3-5 Possible
      1-2 Unlikely
      <=0 Excluded
    Key Exclusions
      Viral A/B/C/E
      AIH
      Wilson
      Haemochromatosis
      Alcohol
      Vascular
      Pregnancy
```

---

## One-Page Revision Card

| **RUCAM Domain** | **Scoring** |
|------------------|-------------|
| 1. Time to Onset | 5-90d: +2; <5 or >90d: +1 |
| 2. Dechallenge | ≤8d ↓50%: +3; 30d: +2; None: 0; Worse: -2 |
| 3. Risk Factors | Alcohol or Age≥55: +1 |
| 4. Concomitant Drugs | None: 0; Possible: -1; Probable: -2; Highly Probable: -3 |
| 5. Exclusion (7 Cats) | All 7: +2; 6: +1; 5: 0; 4: -1; 3: -2; <3: -3 |
| 6. Previous Info | Label: +2; Published: +1; Unknown: 0 |
| 7. Rechallenge | ALT Doubles + Drug Alone: +3; Clinical Only: +1; Negative: -2; Not Done: 0 |

| **Score** | **Causality** | **Action** |
|----------|---------------|------------|
| **≥9** | **Definite** | STOP Drug |
| **6-8** | **Probable** | STOP Drug |
| 3-5 | Possible | Monitor / Investigate |
| 1-2 | Unlikely | Consider Alternative |
| ≤0 | Excluded | Alternative Cause |

| **7 Exclusion Categories (2016)** | |
|----------------------------------|--|
| 1. Viral Hepatitis (A/B/C/E) | |
| 2. Autoimmune Hepatitis | |
| 3. Wilson Disease | |
| 4. Alcoholic Hepatitis | |
| 5. Vascular (Budd-Chiari, PVT) | |
| 6. Pregnancy (AFLP/HELLP) | |
| 7. Other (Sepsis, Infiltrative) | |

---

## Spaced Repetition Tracker

| Day | 1 | 3 | 7 | 15 | 30 |
|-----|---|---|---|----|----|
| RUCAM 7 Domains | ☐ | ☐ | ☐ | ☐ | ☐ |
| RUCAM Thresholds | ☐ | ☐ | ☐ | ☐ | ☐ |
| 7 Exclusion Categories | ☐ | ☐ | ☐ | ☐ | ☐ |
| Dechallenge Scoring | ☐ | ☐ | ☐ | ☐ | ☐ |
| DILI vs AIH | ☐ | ☐ | ☐ | ☐ | ☐ |

---

## Self-Test Scorecard

| Question | My Answer | Correct? |
|----------|-----------|----------|
| RUCAM 7 Domains |  |  |
| RUCAM ≥6 Meaning |  |  |
| 7 Exclusions (2016) |  |  |
| Dechallenge +3 Criteria |  |  |
| DILI vs AIH |  |  |

---

## Local Navigation

- [[Drug-Induced Liver Injury/Classification and patterns|DILI Classification]]
- [[Drug-Induced Liver Injury/Common culprit drugs|Common Culprit Drugs]]
- [[Drug-Induced Liver Injury/Management and rechallenge|DILI Management]]
- [[Acute Liver Failure/Paracetamol-induced hepatotoxicity|Paracetamol ALF]]
- [[Acute Liver Failure/Non-paracetamol drug-induced liver injury|Non-PCM DILI ALF]]
- [[Jaundice and LFT Interpretation/DILI patterns|DILI Patterns in Jaundice]]