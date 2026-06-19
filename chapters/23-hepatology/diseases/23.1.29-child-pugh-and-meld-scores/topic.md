---
tags: [hepatology, chronic_liver_disease, cirrhosis, child_pugh, meld, scoring, fcps, mrcp]
davidson_chapter: Chapter 24
status: full-fcps-mrcp-note
priority: high
exam_relevance: "Child-Pugh and MELD scoring systems - calculation, interpretation, transplant thresholds - FCPS/MRCP essential scoring knowledge"
see_also: ["Chronic Liver Disease and Cirrhosis/Definition and classification", "Chronic Liver Disease and Cirrhosis/Compensated vs decompensated cirrhosis", "Liver Transplantation/Liver Transplantation", "Portal Hypertension and Complications/Ascites", "Portal Hypertension and Complications/Varices"]
created: 2025-06-13
modified: 2025-06-13
---

# Child-Pugh and MELD Scores

## Learning Objectives
- [ ] Calculate Child-Pugh score from clinical parameters
- [ ] Calculate MELD and MELD-Na scores
- [ ] Interpret scores for prognosis and transplant referral
- [ ] Compare and contrast the two systems
- [ ] Identify FCPS/MRCP high-yield calculation details and thresholds

---

## Child-Pugh Score (Child-Turcotte-Pugh)

> **Original**: 1964 (Child), Modified 1973 (Pugh) — Replaced Nutritional Status with INR

### Parameters & Scoring

| Parameter | 1 Point | 2 Points | 3 Points |
|-----------|---------|----------|----------|
| **Total Bilirubin (μmol/L)** | <34 | 34-50 | >50 |
| **Serum Albumin (g/L)** | >35 | 28-35 | <28 |
| **INR** | <1.7 | 1.7-2.3 | >2.3 |
| **Ascites** | None | Mild (Controlled with Diuretics) | Refractory (Tense, Diuretic-Resistant) |
| **Hepatic Encephalopathy** | None | Grade 1-2 (Mild/Moderate) | Grade 3-4 (Severe/Coma) |

> **Note**: Original used **Nutritional Status** instead of INR; **Prothrombin Time** in seconds was original, now INR standard

### Classification & Prognosis

| Class | Score | 1-Year Survival | 2-Year Survival | Clinical Status |
|-------|-------|-----------------|-----------------|-----------------|
| **A** | 5-6 | 100% | 85% | Well-Compensated |
| **B** | 7-9 | 80% | 60% | Moderate / Decompensated |
| **C** | 10-15 | 45% | 35% | Decompensated / High Mortality |

> **FCPS/MRCP**: **Child A = Compensated**, **Child B = Early Decompensated**, **Child C = Advanced Decompensated**

---

## MELD Score (Model for End-Stage Liver Disease)

### Original MELD Formula (2002)
```
MELD = 3.78 × ln(Serum Bilirubin mg/dL) 
     + 11.2 × ln(INR) 
     + 9.57 × ln(Serum Creatinine mg/dL) 
     + 6.43
```

### Adjustments & Caps
| Variable | Minimum | Maximum |
|----------|---------|---------|
| **Bilirubin** | 1.0 mg/dL | 4.0 mg/dL |
| **INR** | 1.0 | 4.0 |
| **Creatinine** | 1.0 mg/dL | **4.0 mg/dL** (Dialysis = 4.0) |

> **If on Dialysis**: Creatinine **Automatically Set to 4.0**

### MELD Score Interpretation
| MELD Score | 3-Month Mortality | Transplant Priority |
|------------|-------------------|---------------------|
| **6-9** | <5% | Low |
| **10-19** | 5-15% | Moderate |
| **20-29** | 20-50% | High |
| **30-39** | 50-75% | Very High |
| **40** | >75% | Highest (Status 1A) |

---

## MELD-Na (Current Standard Since 2016)

### Formula
```
MELD-Na = MELD + 1.32 × (137 - Na) - [0.033 × MELD × (137 - Na)]
```

### Sodium Adjustment
| Sodium (mmol/L) | Used in Formula |
|-----------------|-----------------|
| **<125** | Capped at 125 |
| **125-137** | Actual Value |
| **>137** | Capped at 137 |

> **Why MELD-Na?**: Hyponatraemia = Poor Prognosis (Dilutional, High ADH) → Adds Prognostic Value

---

## Comparison: Child-Pugh vs MELD

| Feature | Child-Pugh | MELD / MELD-Na |
|-------|------------|----------------|
| **Type** | Semi-Quantitative (Clinical + Labs) | Fully Quantitative (Lab-Based) |
| **Parameters** | 5 (Bil, Alb, INR, Ascites, HE) | 3 (Bil, INR, Cr) + Na (MELD-Na) |
| **Subjectivity** | Ascites/HE = Clinical Judgement | Fully Objective |
| **Scale** | 5-15 (Categorical A/B/C) | 6-40 (Continuous) |
| **Primary Use** | Clinical Prognosis, Clinical Trials | **Organ Allocation (Transplant)** |
| **Sensitivity** | Less (Plateaus at Extremes) | High Across Range |
| **Reproducibility** | Moderate (Interobserver Variation) | High (Lab-Based) |

---

## Transplant Referral Thresholds

| System | Threshold | Action |
|-------|-----------|--------|
| **MELD / MELD-Na** | **≥15** | Refer for Transplant Assessment |
| **MELD / MELD-Na** | **≥20** | High Priority Listing |
| **Child-Pugh** | **B (7-9) or C (10-15)** | Consider Referral |
| **Child-Pugh C** | **10-15** | **Urgent Referral** |

> **UK/Europe**: **MELD-Na ≥15** → Transplant Assessment
> **US (UNOS)**: **MELD-Na ≥15** → Listing; **Status 1A** for ALF

---

## MELD Exceptions (Standardised Exception Points)

| Condition | MELD Exception Points |
|-----------|----------------------|
| **HCC (Within Milan)** | **22-28** (Region-Dependent) |
| **Hepatopulmonary Syndrome (PaO₂ <60)** | **22** |
| **Portopulmonary Hypertension** | **22** (If mPAP >35, PVR >240) |
| **Familial Amyloid Polyneuropathy** | **24** |
| **Primary Hyperoxaluria** | **28** |
| **Recurrent Cholangitis (PSC)** | Case-by-Case |

---

## MELD vs Child-Pugh: When to Use Which?

| Clinical Scenario | Preferred Score |
|-------------------|-----------------|
| **Transplant Listing/Allocation** | **MELD-Na** (Gold Standard) |
| **Clinical Prognostication (Bedside)** | Child-Pugh (Faster, Clinical) |
| **Clinical Trial Stratification** | Child-Pugh (Historical Standard) |
| **Surgical Risk Assessment** | Child-Pugh (Traditional) |
| **Clinical Trials (Modern)** | MELD-Na (Increasingly Used) |
| **ACLF Prognosis** | CLIF-C ACLF (Not MELD/Child-Pugh) |

---

## Quick Calculation Reference

### Child-Pugh (Mental Math)
| Parameter | 1 Pt | 2 Pts | 3 Pts |
|-----------|------|-------|-------|
| Bilirubin (μmol/L) | <34 | 34-50 | >50 |
| Albumin (g/L) | >35 | 28-35 | <28 |
| INR | <1.7 | 1.7-2.3 | >2.3 |
| Ascites | None | Controlled | Refractory |
| HE | None | G1-2 | G3-4 |

### MELD Mental Math (Approximate)
| MELD Components | Approximate Points |
|-----------------|-------------------|
| Bilirubin (mg/dL) | 1→0, 2→3, 3→5, 4→6, 5→7, 10→10, 20→13, 30→15 |
| INR | 1→0, 1.5→2, 2→3, 2.5→4, 3→5, 4→6 |
| Creatinine (mg/dL) | 0.5→0, 1→0, 1.5→4, 2→6, 3→8, 4→9 |

---

## FCPS/MRCP High-Yield Summary

| Concept | Key Points |
|---------|------------|
| **Child-Pugh** | 5 Parameters (Bil, Alb, INR, Ascites, HE); 5-15 → A(5-6)/B(7-9)/C(10-15) |
| **MELD** | 3 Labs (Bil, INR, Cr); 6-40; **≥15 = Transplant Referral** |
| **MELD-Na** | MELD + Sodium Adjustment; Current Standard |
| **Child-Pugh A** | 5-6 (Compensated); **100% 1-yr Survival** |
| **Child-Pugh B** | 7-9 (Decompensated); **80% 1-yr Survival** |
| **Child-Pugh C** | 10-15 (Advanced); **45% 1-yr Survival** |
| **MELD ≥15** | Transplant Referral Threshold |
| **MELD ≥20** | High Priority |
| **MELD on Dialysis** | Creatinine = 4.0 (Max) |
| **Child-Pugh C = Decompensated** | But Decompensated Can Be Child B |

---

## Viva Questions

1. **What are the 5 components of Child-Pugh score?**
2. **What is the MELD formula? What are the variable caps?**
3. **How does MELD-Na differ from MELD?**
4. **What is the transplant referral threshold for MELD?**
4. **Child-Pugh Class A/B/C survival rates?**
5. **When do you use Child-Pugh vs MELD?**
6. **How does dialysis affect MELD calculation?**
6. **What are standard MELD exception points for HCC?**
7. **Difference between Child-Pugh and MELD in transplant allocation?**
8. **What is the MELD score if bilirubin 5, INR 2.5, creatinine 2, Na 130?**
9. **Why was sodium added to MELD?**

---

## Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| Child-Pugh vs MELD | Child-Pugh = Clinical + Labs; MELD = Pure Lab-Based; MELD for Allocation |
| Child-Pugh Class | A=Compensated, B=Early Decomp, C=Advanced Decomp |
| MELD ≥15 | **Transplant Referral** — Not Automatic Listing |
| Dialysis in MELD | **Creatinine = 4.0** (Max, Not Actual) |
| Child-Pugh Ascites | None=1, Controlled=2, Refractory=3 |
| MELD vs MELD-Na | MELD-Na Adds Sodium (Better for Low Na Prognosis) |
| Child-Pugh C ≠ All Decompensated | Decompensated Can Be Child B (Early) |
| MELD Exception HCC | **28 Points (US)** / Variable (UK/Europe) |

---

## Mind Map

```mermaid
mindmap
  root((Child-Pugh vs MELD))
    Child-Pugh
      5 Parameters: Bil, Alb, INR, Ascites, HE
      Score 5-15
      Class A: 5-6 (Compensated)
      Class B: 7-9 (Decomp)
      Class C: 10-15 (Severe)
      Prognosis: A=100%, B=80%, C=45% (1yr)
    MELD
      3 Labs: Bilirubin, INR, Creatinine
      Formula: 3.78ln(Bil)+11.2ln(INR)+9.57ln(Cr)+6.43
      Caps: Bil/INR/Cr Max 4.0
      Dialysis: Cr=4.0
      Range: 6-40
    MELD-Na
      MELD + 1.32(137-Na) - 0.033×MELD×(137-Na)
      Na Capped 125-137
      Current Standard
    Comparison
      Child-Pugh: Subjective (Ascites/HE), Categorical A/B/C
      MELD: Objective, Continuous 6-40
      Allocation: MELD-Na
      Bedside: Child-Pugh
    Transplant Thresholds
      MELD-Na >=15: Referral
      MELD-Na >=20: High Priority
      Child B/C: Consider Referral
      Child C: Urgent Referral
    Exceptions
      HCC: 28 (US) / 22-28 (UK)
      HPS: 22
      PoPH: 22
      FAP: 24
```

---

## One-Page Revision Card

| **Child-Pugh** | **1 Point** | **2 Points** | **3 Points** |
|----------------|-------------|--------------|--------------|
| Bilirubin (μmol/L) | <34 | 34-50 | >50 |
| Albumin (g/L) | >35 | 28-35 | <28 |
| INR | <1.7 | 1.7-2.3 | >2.3 |
| Ascites | None | Controlled | Refractory |
| HE | None | Grade 1-2 | Grade 3-4 |

| **Class** | **Score** | **1-Yr Survival** | **Status** |
|-----------|-----------|-------------------|------------|
| **A** | 5-6 | 100% | Compensated |
| **B** | 7-9 | 80% | Decompensated |
| **C** | 10-15 | 45% | Severe |

| **MELD** | **Formula** |
|----------|-------------|
| **3.78×ln(Bil) + 11.2×ln(INR) + 9.57×ln(Cr) + 6.43** | |

| **MELD Caps** | **Min** | **Max** |
|---------------|--------|--------|
| Bilirubin | 1.0 | 4.0 |
| INR | 1.0 | 4.0 |
| Creatinine | 1.0 | **4.0 (Dialysis)** |

| **Thresholds** | **Value** | **Action** |
|----------------|----------|------------|
| **MELD/Na ≥15** | Transplant Referral |
| **MELD/Na ≥20** | High Priority |
| **Child-Pugh B/C** | Consider Referral |
| **Child-Pugh C** | **Urgent Referral** |

| **MELD-Na** | **MELD + 1.32(137-Na) - 0.033×MELD×(137-Na)** |
| Na Cap | 125-137 |

---

## Spaced Repetition Tracker

| Day | 1 | 3 | 7 | 15 | 30 |
|-----|---|---|---|----|----|
| Child-Pugh 5 Components | ☐ | ☐ | ☐ | ☐ | ☐ |
| Child-Pugh Class Scores | ☐ | ☐ | ☐ | ☐ | ☐ |
| MELD Formula | ☐ | ☐ | ☐ | ☐ | ☐ |
| MELD ≥15 Threshold | ☐ | ☐ | ☐ | ☐ | ☐ |
| MELD-Na Formula | ☐ | ☐ | ☐ | ☐ | ☐ |

---

## Self-Test Scorecard

| Question | My Answer | Correct? |
|----------|-----------|----------|
| Child-Pugh 5 Parameters |  |  |
| Class A/B/C Scores |  |  |
| MELD Formula |  |  |
| MELD ≥15 Meaning |  |  |
| MELD-Na vs MELD |  |  |

---

## Local Navigation

- [[Chronic Liver Disease and Cirrhosis/Definition and classification|Definition & Classification]]
- [[Chronic Liver Disease and Cirrhosis/Compensated vs decompensated cirrhosis|Compensated vs Decompensated]]
- [[Liver Transplantation/Liver Transplantation|Liver Transplant]]
- [[Portal Hypertension and Complications/Ascites|Ascites]]
- [[Portal Hypertension and Complications/Varices|Varices]]