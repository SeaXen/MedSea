## 1. Learning Objectives
- [ ] Calculate Child-Pugh score from clinical parameters
- [ ] Calculate MELD and MELD-Na scores
- [ ] Interpret scores for prognosis and transplant referral
- [ ] Compare and contrast the two systems
- [ ] Identify FCPS/MRCP high-yield calculation details and thresholds

---

## 2. Child-Pugh Score (Child-Turcotte-Pugh)

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

## 3. MELD Score (Model for End-Stage Liver Disease)

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

## 4. MELD-Na (Current Standard Since 2016)

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

## 5. Comparison: Child-Pugh vs MELD

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

## 6. Transplant Referral Thresholds

| System | Threshold | Action |
|-------|-----------|--------|
| **MELD / MELD-Na** | **≥15** | Refer for Transplant Assessment |
| **MELD / MELD-Na** | **≥20** | High Priority Listing |
| **Child-Pugh** | **B (7-9) or C (10-15)** | Consider Referral |
| **Child-Pugh C** | **10-15** | **Urgent Referral** |

> **UK/Europe**: **MELD-Na ≥15** → Transplant Assessment
> **US (UNOS)**: **MELD-Na ≥15** → Listing; **Status 1A** for ALF

---

## 7. MELD Exceptions (Standardised Exception Points)

| Condition | MELD Exception Points |
|-----------|----------------------|
| **HCC (Within Milan)** | **22-28** (Region-Dependent) |
| **Hepatopulmonary Syndrome (PaO₂ <60)** | **22** |
| **Portopulmonary Hypertension** | **22** (If mPAP >35, PVR >240) |
| **Familial Amyloid Polyneuropathy** | **24** |
| **Primary Hyperoxaluria** | **28** |
| **Recurrent Cholangitis (PSC)** | Case-by-Case |

---

## 8. MELD vs Child-Pugh: When to Use Which?

| Clinical Scenario | Preferred Score |
|-------------------|-----------------|
| **Transplant Listing/Allocation** | **MELD-Na** (Gold Standard) |
| **Clinical Prognostication (Bedside)** | Child-Pugh (Faster, Clinical) |
| **Clinical Trial Stratification** | Child-Pugh (Historical Standard) |
| **Surgical Risk Assessment** | Child-Pugh (Traditional) |
| **Clinical Trials (Modern)** | MELD-Na (Increasingly Used) |
| **ACLF Prognosis** | CLIF-C ACLF (Not MELD/Child-Pugh) |

---

## 9. Quick Calculation Reference

### Child-Pugh (Mental Math)
| Parameter | 1 Pt | 2 Pts | 3 Pts |
|-----------|------|-------|-------|
| Bilirubin (μmol/L) | <34 | 34-50 | >50 |
| Albumin (g/L) | >35 | 28-35 | <28 |
| INR | <1.7 | 1.7-2.3 | >2.3 |
| Ascites | None | Controlled | Refractory |
| HE | None | G1-2 | G3-4 |


*...continued (truncated for renderer performance)*
---

> Auto-generated study sections for "Chronic Liver Disease and Cirrhosis" — Ch 23: Hepatology.

## Flashcards (1 generated)

- Q: What is the definition of Chronic Liver Disease and Cirrhosis?
  A: | Bilirubin | 1.0 mg/dL | 4.0 mg/dL |

## MCQs (1 generated)

1. **Which of the following best describes Chronic Liver Disease and Cirrhosis?**
   A. **| Bilirubin | 1.0 mg/dL | 4.0 mg/dL |**
   B. An unrelated condition not matching the clinical picture of Chronic Liver Disease and Cirrhosis
   C. A complication seen late in the disease course of Chronic Liver Disease and Cirrhosis
   D. A condition that mimics Chronic Liver Disease and Cirrhosis but has a different underlying cause

