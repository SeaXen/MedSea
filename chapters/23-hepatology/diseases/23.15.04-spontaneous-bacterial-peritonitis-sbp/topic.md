## 1. Learning Objectives
- [ ] Apply diagnostic criteria (PMN count ≥250 cells/mm³)
- [ ] Differentiate SBP variants (culture-negative, bacterascites, secondary peritonitis)
- [ ] Initiate empirical antibiotics (ceftriaxone/cefotaxime) + albumin
- [ ] Know secondary prophylaxis indications
- [ ] Identify FCPS/MRCP high-yield management steps

---

## 2. Definition & Epidemiology

| Feature | SBP |
|---------|-----|
| **Definition** | Infection of ascitic fluid **without** surgically treatable intra-abdominal source |
| **Incidence** | 10-30% of hospitalized cirrhotics with ascites |
| **Mortality** | 20-40% in-hospital (improved with albumin) |
| **Common organisms** | E. coli (40%), Klebsiella (20%), Strep pneumoniae (10%), Enterococci (10%) |
| **Culture-negative** | 40-60% (despite PMN ≥250) — "Culture-negative neutrocytic ascites" |

---

## 3. Diagnostic Criteria

```mermaid
flowchart TD
    A[Clinical Suspicion: Fever, Abdo Pain, Worsening HE, Unexplained Deterioration] --> B[Diagnostic Paracentesis]
    B --> C[Ascitic Fluid Analysis]
    C --> D{PMN Count}
    D -->|≥250 cells/mm³| E[DIAGNOSE SBP]
    D -->|<250| F{Clinical suspicion HIGH?}
    F -->|Yes| G[Culture + Repeat in 48h]
    F -->|No| H[No SBP]
    E --> I[Send Culture (Blood culture bottles at bedside!)]
    E --> J[Start Empirical Antibiotics IMMEDIATELY]
    E --> K[Albumin 1.5g/kg Day 1 + 1g/kg Day 3]
```

### Ascitic Fluid Analysis: Key Values

| Parameter | SBP | Secondary Peritonitis | Notes |
|-----------|-----|----------------------|-------|
| **PMN count** | **≥250/mm³** | ≥250/mm³ | Main diagnostic criterion |
| **Culture** | Often negative | Usually positive | Inoculate at bedside |
| **Total protein** | Low (<1 g/dL) | High (>1 g/dL) | Low protein = risk factor |
| **Glucose** | Normal | **Low (<50 mg/dL)** | Low glucose = secondary |
| **LDH** | Normal | **High (>upper limit serum)** | High LDH = secondary |
| **Multiple organisms** | Rare | **Common** | Polymicrobial = secondary |

### Runyon's Criteria for Secondary Peritonitis (Any 2 of 3)
1. Ascitic fluid **total protein >1 g/dL**
2. Ascitic fluid **glucose <50 mg/dL**
3. Ascitic fluid **LDH >upper limit of normal serum**

> **If secondary peritonitis suspected**: Urgent surgical consultation + CT abdomen

---

## 4. Variants of SBP

| Variant | Definition | Management |
|---------|------------|------------|
| **Classic SBP** | PMN ≥250 + positive culture | Antibiotics + Albumin |
| **Culture-negative neutrocytic ascites (CNNA)** | PMN ≥250 + negative culture | **Same as SBP** (treat empirically) |
| **Bacterascites** | PMN <250 + positive culture | If symptomatic → treat as SBP; If asymptomatic → repeat paracentesis, treat if PMN rises |
| **Monicrobial non-neutrocytic bacterascites** | Single organism, PMN <250 | Usually transient; monitor |

---

## 5. Empirical Antibiotic Therapy

| Drug | Dose | Duration | Notes |
|------|------|----------|-------|
| **Ceftriaxone** (Preferred) | 2 g IV daily | **5-7 days** | Once daily; good Gram-neg coverage; no renal adjust |
| **Cefotaxime** | 2 g IV q6-8h | 5-7 days | Traditional; q6h dosing |
| **Alternative (allergy)** | Ciprofloxacin 400mg IV q12h | 5-7 days | If local resistance low |
| **Nosocomial/Recurrent** | Piperacillin-tazobactam 4.5g q6h OR Meropenem 1g q8h | 7-10 days | Cover ESBL, Enterococcus |

> **Start antibiotics BEFORE culture results** — delay increases mortality

---

## 6. Albumin Adjunct Therapy

| Dose | Timing | Evidence |
|------|--------|----------|
| **1.5 g/kg** (max 100g) | **Day 1** (at diagnosis) | **Reduces HRS & mortality** (RCT: Sort et al.) |
| **1 g/kg** (max 100g) | **Day 3** | Completes course |

**Indication**: All SBP (especially if Cr >1, BUN >30, bilirubin >4)
**Mechanism**: Volume expansion → prevents renal vasoconstriction → prevents HRS

---

## 7. Management Algorithm

```mermaid
flowchart TD
    A[Suspect SBP] --> B[Diagnostic Paracentesis: PMN, Culture, Protein, Glucose, LDH]
    B --> C{PMN >=250?}
    C -->|Yes| D[DIAGNOSE SBP]
    D --> E[START Ceftriaxone 2g IV daily]
    D --> F[Albumin 1.5g/kg Day 1 + 1g/kg Day 3]
    D --> G[Blood cultures x2]
    D --> H[Urinalysis, CXR, other cultures]
    E --> I{Clinical Improvement at 48h?}
    I -->|Yes| J[Continue 5-7 days total]
    I -->|No| K[Repeat paracentesis: PMN should ↓]
    K --> L{PMN ↓25%?}
    L -->|Yes| M[Continue current antibiotics]
    L -->|No| N[Escalate antibiotics: Consider resistance, secondary peritonitis]
    C -->|No| O{High suspicion?}
    O -->|Yes| P[Blood culture bottles at bedside + Repeat paracentesis 48h]
    O -->|No| Q[No SBP; Look for other cause]
```

---

## 8. Secondary Prophylaxis (After SBP Episode)

| Indication | Regimen | Duration |
|------------|---------|----------|
| **All survivors of SBP** | **Norfloxacin 400 mg PO daily** | **Long-term** (until transplant/death) |
| **Alternative** | Ciprofloxacin 500 mg PO daily | Long-term |
| **Alternative** | TMP-SMX 1 DS daily | Long-term |

**Rationale**: Recurrence rate 40-70% at 1 year without prophylaxis

---

## 9. Primary Prophylaxis (High-Risk Without Prior SBP)

| Indication | Regimen |
|------------|---------|
| **Ascitic fluid protein <1.5 g/dL** + **Child-Pugh ≥9** OR **Renal impairment (Cr≥1.5, BUN≥25, Na≤130)** | Norfloxacin 400 mg PO daily |
| **Acute variceal bleed** | Ceftriaxone 1g IV daily × 7 days (already covered) |

---

## 10. FCPS/MRCP High-Yield Summary

| Concept | Key Points |
|---------|------------|
| **Diagnosis** | PMN ≥250 cells/mm³ ( cultura-negative = still SBP) |
| **Culture** | Inoculate **at bedside** into blood culture bottles |
| **Empirical antibiotics** | **Ceftriaxone 2g IV daily** × 5-7 days |
| **Albumin** | 1.5g/kg Day 1 + 1g/kg Day 3 — prevents HRS/mortality |
| **Secondary peritonitis** | Suspect if: protein >1, glucose <50, LDH high, polymicrobial |
| **Secondary prophylaxis** | Norfloxacin 400mg daily lifelong after SBP |
| **Primary prophylaxis** | Ascitic protein <1.5 + (Child≥9 or renal impairment) |

---

## 11. Viva Questions

1. **What is the diagnostic criterion for SBP?**
2. **What is culture-negative neutrocytic ascites? How to manage?**
3. **What antibiotics for empirical SBP treatment? Dose? Duration?**
4. **When do you give albumin in SBP? Dose?**
5. **Differentiate SBP from secondary peritonitis.**
6. **What is bacterascites? Management?**
7. **Secondary prophylaxis after SBP: drug, dose, duration?**
8. **Primary prophylaxis indications?**
9. **Why inoculate culture at bedside?**
10. **SBP recurrence rate without prophylaxis?**

---

## 12. Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| PMN vs total WCC | **PMN (polymorphonuclear) ≥250** — not total white count |
| Culture-negative SBP | **Still treat as SBP** — 40-60% culture-negative despite PMN≥250 |
| SBP vs Secondary peritonitis | Secondary: high protein, low glucose, high LDH, polymicrobial — needs surgery |
| Albumin timing | **Day 1 (1.5g/kg) + Day 3 (1g/kg)** — not single dose |
| Ceftriaxone vs Cefotaxime | Ceftriaxone preferred: once daily, no renal adjust, same efficacy |
| Primary vs Secondary prophylaxis | Primary: high-risk NO prior SBP; Secondary: ALL SBP survivors |

---

## 13. Mind Map

```mermaid
mindmap
  root((Spontaneous Bacterial Peritonitis))
    Diagnosis
      PMN >=250 cells/mm3
      Culture at bedside
      Culture-negative = still SBP
    Variants
      Classic SBP
      Culture-negative neutrocytic ascites
      Bacterascites (PMN<250 + culture+)
    Treatment
      Ceftriaxone 2g IV daily 5-7d
      Albumin 1.5g/kg D1 + 1g/kg D3
      Repeat paracentesis 48h if no improvement
    Secondary Peritonitis
      Protein >1, Glucose <50, LDH high
      Polymicrobial
      Surgical emergency
    Prophylaxis
      Secondary: Norfloxacin 400mg daily lifelong
      Primary: Ascitic protein<1.5 + Child>=9 or renal impairment
```

---

## 14. One-Page Revision Card

| **SBP** | **Details** |
|---------|-------------|
| **Diagnosis** | PMN ≥250/mm³ (culture-negative = still SBP) |
| **Culture** | Bedside inoculation in blood culture bottles |
| **Empirical Abx** | Ceftriaxone 2g IV daily × 5-7d (preferred) |
| **Albumin** | 1.5g/kg Day 1 + 1g/kg Day 3 |
| **Secondary Peritonitis** | Protein>1, Glucose<50, LDH high, polymicrobial → Surgery |
| **Secondary Prophylaxis** | Norfloxacin 400mg PO daily lifelong |
| **Primary Prophylaxis** | Ascitic protein<1.5 + (Child≥9 or Cr≥1.5/Na≤130) |

---

## 15. Spaced Repetition Tracker

| Day | 1 | 3 | 7 | 15 | 30 |
|-----|---|---|---|----|----|
| PMN criterion | ☐ | ☐ | ☐ | ☐ | ☐ |
| Ceftriaxone dose | ☐ | ☐ | ☐ | ☐ | ☐ |
| Albumin doses | ☐ | ☐ | ☐ | ☐ | ☐ |
| SBP vs secondary peritonitis | ☐ | ☐ | ☐ | ☐ | ☐ |
| Prophylaxis indications | ☐ | ☐ | ☐ | ☐ | ☐ |

---

## 16. Self-Test Scorecard

| Question | My Answer | Correct? |
|----------|-----------|----------|
| PMN cutoff |  |  |
| Ceftriaxone regimen |  |  |
| Albumin Day 1 + Day 3 |  |  |
| Runyon's criteria |  |  |
| Secondary prophylaxis |  |  |

---

## 17. Local Navigation

- [[Portal Hypertension and Complications/Ascites|Ascites Overview]]
- [[Portal Hypertension and Complications/Ascites diagnosis and SAAG|Ascites Diagnosis]]
- [[Portal Hypertension and Complications/Ascites management|Ascites Management]]
- [[Portal Hypertension and Complications/Hepatic Encephalopathy|HE]]
- [[Portal Hypertension and Complications/Hepatorenal Syndrome|HRS]]
- [[Acute Liver Failure/CLIF-C ACLF and ACLF grades|ACLF]]
---

> Auto-generated study sections for "Portal Hypertension and Complications" — Ch 23: Hepatology.

## Flashcards (12 generated)

- Q: What is the definition of Portal Hypertension and Complications?
  A: Infection of ascitic fluid without surgically treatable intra-abdominal source
- Q: What is the epidemiology of Portal Hypertension and Complications?
  A: 10-30% of hospitalized cirrhotics with ascites
- Q: What is Mortality of Portal Hypertension and Complications?
  A: 20-40% in-hospital (improved with albumin)
- Q: What is Common organisms of Portal Hypertension and Complications?
  A: E. coli (40%), Klebsiella (20%), Strep pneumoniae (10%), Enterococci (10%)
- Q: What is Culture-negative of Portal Hypertension and Complications?
  A: 40-60% (despite PMN ≥250) — "Culture-negative neutrocytic ascites"
- Q: What is the investigation of choice for Portal Hypertension and Complications?
  A: PMN ≥250 cells/mm³ ( cultura-negative = still SBP)
- Q: What is Culture of Portal Hypertension and Complications?
  A: Inoculate at bedside into blood culture bottles
- Q: What is Empirical antibiotics of Portal Hypertension and Complications?
  A: Ceftriaxone 2g IV daily × 5-7 days
- Q: What is Albumin of Portal Hypertension and Complications?
  A: 1.5g/kg Day 1 + 1g/kg Day 3 — prevents HRS/mortality
- Q: What is Secondary peritonitis of Portal Hypertension and Complications?
  A: Suspect if: protein >1, glucose <50, LDH high, polymicrobial
- Q: What is Secondary prophylaxis of Portal Hypertension and Complications?
  A: Norfloxacin 400mg daily lifelong after SBP
- Q: What is Primary prophylaxis of Portal Hypertension and Complications?
  A: Ascitic protein <1.5 + (Child≥9 or renal impairment)

## MCQs (1 generated)

1. **Which of the following best describes Portal Hypertension and Complications?**
   A. **A[Clinical Suspicion: Fever, Abdo Pain, Worsening HE, Unexplained Deterioration] --> B[Diagnostic Paracentesis]**
   B. An unrelated condition not matching the clinical picture of Portal Hypertension and Complications
   C. A complication seen late in the disease course of Portal Hypertension and Complications
   D. A condition that mimics Portal Hypertension and Complications but has a different underlying cause

## SBA Questions (1 generated)

1. A patient with suspected Portal Hypertension and Complications presents with: Definition — Infection of ascitic fluid without surgically treatable intra-abdominal source; Incidence — 10-30% of hospitalized cirrhotics with ascites; Mortality — 20-40% in-hospital (improved with albumin). What is the most likely diagnosis?
   A. **Portal Hypertension and Complications**
   B. A condition that mimics Portal Hypertension and Complications but is not the same entity
   C. A complication of Portal Hypertension and Complications rather than the primary diagnosis
   D. An unrelated condition in the same clinical category as Portal Hypertension and Complications

