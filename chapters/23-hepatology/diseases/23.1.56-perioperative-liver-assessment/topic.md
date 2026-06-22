## 1. Learning Objectives
- [ ] Perform preoperative liver risk stratification
- [ ] Interpret preoperative liver function tests
- [ ] Assess surgical risk in cirrhosis (Child-Pugh, MELD, CPET)
- [ ] Manage intraoperative and postoperative liver dysfunction
- [ ] Identify FCPS/MRCP high-yield perioperative hepatology

---

## 2. Preoperative Hepatic Risk Stratification

```mermaid
flowchart TD
    A[Patient for Surgery] --> B{Known Liver Disease?}
    B -->|Yes| C[Formal Assessment]
    B -->|No| D[Screening LFTs if Risk Factors]
    C --> E[Child-Pugh Score]
    C --> F[MELD/MELD-Na Score]
    C --> G[CPET (If Major Surgery)]
    C --> H[Frailty Assessment (CFS)]
    C --> H1[Portal Hypertension Screen (US, Platelets)]
    E & F & G & H --> I{Risk Category}
    I -->|Low| J[Proceed with Standard Care]
    I -->|Moderate| K[Optimise → Proceed with Caution]
    I -->|High| L[Defer / Palliative / Transplant Eval]
```

---

## 3. Preoperative Liver Function Tests

### Standard Screening Panel

| Test | Purpose | Abnormal → Action |
|------|---------|-------------------|
| **ALT, AST** | Hepatocellular Injury | Investigate Cause |
| **ALP, GGT** | Cholestasis / Biliary Obstruction | US Abdomen, MRCP if Needed |
| **Bilirubin** | Synthetic/Excretory Function | MELD Calculation |
| **Albumin** | Synthetic Function / Nutrition | Nutritional Optimisation |
| **INR / PT** | Synthetic Function | Transfuse if >1.5 (Procedure) |
| **Platelets** | Portal Hypertension / Hypersplenism | Transfuse if <50k (Major Surgery) |

> **FCPS/MRCP**: **Do NOT Routinely Correct INR/Platelets** Unless Active Bleeding or High-Risk Procedure

---

## 4. Surgical Risk Stratification in Cirrhosis

### Child-Pugh Classification

| Class | Score | 30-Day Postoperative Mortality | Elective Surgery |
|-------|-------|-------------------------------|------------------|
| **A** | 5-6 | **~10%** | **Safe** (Standard Consent) |
| **B** | 7-9 | **~30%** | **High Risk** (MDT, Optimise First) |
| **C** | 10-15 | **>50%** | **Contraindicated** (Except Transplant) |

### MELD Score

| MELD Score | 30-Day Mortality | Elective Surgery |
|------------|------------------|------------------|
| **<10** | <5% | Low Risk |
| **10-19** | 10-20% | Moderate Risk (Optimise) |
| **≥20** | >30% | **High Risk / Contraindicated** |
| **≥30** | >50% | **Contraindicated** |

> **FCPS/MRCP**: **Child-Pugh B/C or MELD ≥15 = High Surgical Risk** — Requires MDT

---

## 5. Comprehensive Preoperative Assessment

### 1. Hepatic Reserve Assessment

| Test | Purpose | Threshold |
|------|---------|-----------|
| **Child-Pugh Score** | Global Synthetic Function | Class B/C = High Risk |
| **MELD/MELD-Na** | Objective Mortality Prediction | **≥15 = High Risk** |
| **ICG Clearance (ICG-PDR)** | Functional Hepatic Reserve | **<14%/min = High Risk** |
| **LiMAx Test** | Hepatic Function Capacity | **<300 μg/kg/h = High Risk** |
| **CT Volumetry (FLR)** | Future Liver Remnant | **<20% (Healthy), <30% (Cirrhosis)** |

### 2. Portal Hypertension Assessment

| Test | Indication | Finding |
|------|------------|---------|
| **US + Doppler** | All Cirrhosis | Portal Vein Flow, Diameter, Collaterals |
| **Platelet Count** | Surrogate for PH | **<150k = CSPH Likely** |
| **Spleen Size** | Surrogate for PH | **>13-15 cm = CSPH** |
| **HVPG** | Gold Standard | **≥10 mmHg = CSPH; ≥20 = High Risk** |

### 3. Cardiopulmonary Assessment

| Test | Indication |
|------|------------|
| **CPET (VO2 max)** | Major Hepatic Resection, Transplant |
| **Echocardiography** | All Major Surgery (Diastolic Dysfunction, PoPH) |
| **ABG / PFTs** | If COPD/Pulmonary Disease Suspected |

### 4. Frailty & Nutritional Assessment

| Tool | Purpose |
|------|---------|
| **Clinical Frailty Scale (CFS)** | Predicts Postoperative Complications, Mortality |
| **Sarcopenia (CT L3 SMI)** | Predicts Complications, Mortality |
| **MNA (Mini Nutritional Assessment)** | Malnutrition = Poor Outcomes |
| **Handgrip Strength** | Sarcopenia Proxy |

---

## 6. Intraoperative Liver Protection

### Anaesthetic Considerations

| Drug | Hepatic Effect | Preference |
|-------|----------------|------------|
| **Volatile Agents** | ↓ Hepatic Blood Flow (Dose-Dependent) | **Sevoflurane/Desflurane > Isoflurane** |
| **IV Agents (Propofol)** | Minimal Hepatic Effect | **Preferred** |
| **Opioids** | Minimal Direct Effect | **Monitor Sedation** |
| **Muscle Relaxants** | Rocuronium/Cisatracurium (Hepatic Clearance) | **Cisatracurium (Hofmann Elimination)** |

### Haemodynamic Goals

| Parameter | Target | Rationale |
|-----------|--------|-----------|
| **MAP** | **≥65 mmHg** | Hepatic Perfusion Pressure |
| **CVP** | **<10-12 mmHg** | Avoid ↑ IVC Pressure → ↓ Hepatic Venous Outflow |
| **Urine Output** | **>0.5 ml/kg/h** | Renal Perfusion → Hepatorenal Syndrome Prevention |
| **Hb** | **>80 g/L** (Restrictive) | Avoid Over-Transfusion (Portal Pressure) |

---

## 7. Postoperative Liver Dysfunction

### Classification

| Syndrome | Definition | Timing | Mortality |
|----------|------------|--------|-----------|
| **Postoperative Liver Failure (50-50 Criteria)** | Bilirubin >50 μmol/L + PT <50% on Day 5 | Day 5 | High |
| **Acute Liver Failure** | INR ≥1.5 + Encephalopathy | <26 Weeks | Very High |
| **Transient Elevation** | AST/ALT >3×ULN, Resolving | Days 1-3 | Low |
| **Ischaemic Hepatitis** | AST/ALT >2000, Rapid Rise/Fall | Post-Hypotension | High (If Severe) |

---

## 8. Management of Postoperative Liver Dysfunction

```mermaid
flowchart TD
    A[Postop LFT Derangement] --> B{Severity / Pattern}
    B -->|Mild Transient| C[Monitor, Supportive]

*...continued (truncated for renderer performance)*
---

> Auto-generated study sections for "Hepatology in Special Situations" — Ch 23: Hepatology.

## Flashcards (6 generated)

- Q: What is the definition of Hepatology in Special Situations?
  A: | Test | Purpose | Abnormal → Action |
- Q: What is CPET (VO2 max) of Hepatology in Special Situations?
  A: Major Hepatic Resection, Transplant
- Q: What is Echocardiography of Hepatology in Special Situations?
  A: All Major Surgery (Diastolic Dysfunction, PoPH)
- Q: What is ABG / PFTs of Hepatology in Special Situations?
  A: If COPD/Pulmonary Disease Suspected
- Q: What is CPET (VO2 max) of Hepatology in Special Situations?
  A: Major Hepatic Resection, Transplant
- Q: What is Echocardiography of Hepatology in Special Situations?
  A: All Major Surgery (Diastolic Dysfunction, PoPH)

## MCQs (1 generated)

1. **Which of the following best describes Hepatology in Special Situations?**
   A. **| Test | Purpose | Abnormal → Action |**
   B. An unrelated condition not matching the clinical picture of Hepatology in Special Situations
   C. A complication seen late in the disease course of Hepatology in Special Situations
   D. A condition that mimics Hepatology in Special Situations but has a different underlying cause

