---
tags: [medicine, respiratory, wells, d-dimer, ctpa, pe-workup, davidson, fcps, mrcp]
chapter: Respiratory
davidson_part: Part 3: Clinical Medicine
davidson_chapter: Chapter 17: Respiratory medicine
topic: D-dimer, CTPA, and Wells score framework
exam: FCPS, MRCP
references:
  clinical: ["ESC 2019 PE", "BTS 2018", "Davidson", "PasTest"]
related: [Pulmonary Embolism, Subsegmental and incidental pulmonary embolism, ABG Interpretation, Right-heart strain in respiratory disease, Oxygen Therapy and NIV]
status: full-fcps-mrcp-note
last_updated: 2026-06-16
---

# D-dimer, CTPA, and Wells score framework

> [!important]
> The **Wells score + D-dimer** combination is the standard diagnostic approach for **suspected PE**. **CTPA** is the gold standard imaging. **Age-adjusted D-dimer** thresholds improve specificity without compromising safety. This framework avoids unnecessary imaging in low-probability patients.

Related: [[Pulmonary Embolism]], [[Subsegmental and incidental pulmonary embolism]], [[ABG Interpretation]]

> [!tip] **FCPS/MRCP pearl**: **Wells >4 = PE likely** → CTPA. **Wells ≤4 = PE unlikely** → D-dimer. If D-dimer <500 (or age-adjusted: age × 10 ng/mL in >50 y) → PE excluded. PERC rule (all 8 negative) can rule out PE without D-dimer in low-risk patients.

## Learning Objectives
- Apply Wells score to assess pre-test probability
- Interpret D-dimer (including age-adjusted)
- Use PERC rule
- Order and interpret CTPA
- Choose V/Q scan when CTPA contraindicated
- Recognise when further imaging needed

## Wells Score (PE)

| Feature | Points |
|---------|--------|
| Clinical signs of DVT | 3.0 |
| PE most likely diagnosis (vs alternative) | 3.0 |
| HR >100 | 1.5 |
| Immobilisation ≥3 days or surgery in 4 weeks | 1.5 |
| Previous DVT/PE | 1.5 |
| Haemoptysis | 1.0 |
| Active cancer | 1.0 |

### Interpretation
- **Two-tier**:
  - **>4 = PE likely** → proceed to CTPA
  - **≤4 = PE unlikely** → D-dimer
- **Three-tier**:
  - **>6 = high**
  - **2–6 = moderate**
  - **<2 = low**

## D-dimer

### What is D-dimer?
- Fibrin degradation product
- **↑ in any clot formation** (PE/DVT, but also infection, surgery, cancer, pregnancy)
- **High sensitivity, low specificity** for VTE

### Cut-offs
- **Standard**: <500 ng/mL (or <500 µg/L FEU) = negative
- **Age-adjusted** (more specific in >50 y): **age × 10 ng/mL**
  - 60 y → 600 ng/mL
  - 80 y → 800 ng/mL
- **Pregnancy-adjusted** (lower specificity): different thresholds by trimester

### Use
- **Rule out PE in low/intermediate pre-test probability**
- **Do NOT use** in high pre-test probability (proceed to imaging)

## PERC Rule (Pulmonary Embolism Rule-Out Criteria)

If **all 8** negative in low-risk patient, PE can be excluded without D-dimer:
1. Age <50
2. HR <100
3. SpO₂ ≥95%
4. No unilateral leg swelling
5. No haemoptysis
6. No surgery/trauma within 4 weeks
7. No prior VTE
8. No oral hormone use

## CTPA (CT Pulmonary Angiogram)

### Indication
- **PE likely** (Wells >4) OR
- **PE unlikely** + **D-dimer positive**

### Protocol
- IV contrast, thin slices
- Pulmonary arterial phase
- **Filling defect in PA** = diagnostic
- **RV/LV ratio ≥1.0** = marker of severe PE
- **RV strain signs** (septal bowing, reflux of contrast into IVC)

### Advantages
- Gold standard (sensitivity 83–100%, specificity 89–97%)
- Identifies alternative diagnoses
- Provides prognostic info (RV strain)

### Disadvantages
- **Radiation** (~10 mSv, ~200 CXRs; ↑breast cancer risk in women)
- **Contrast** (nephrotoxicity, allergy)
- **Overdiagnosis** of subsegmental PE

## V/Q Scan

### Indication
- CTPA contraindicated (contrast allergy, severe CKD, pregnancy)
- Persistent suspicion despite negative CTPA

### Interpretation
- **Normal**: PE excluded
- **High probability**: PE very likely
- **Intermediate (indeterminate)**: needs further imaging
- **Low probability**: PE unlikely (but cannot exclude in high pre-test)

## Diagnostic Algorithm

```mermaid
flowchart TD
    A[Suspected PE] --> B[Clinical assessment + Wells]
    B --> C{Wells >4?}
    C -->|Yes| D[CTPA]
    C -->|No| E[PERC all negative?]
    E -->|Yes| F[PE excluded]
    E -->|No| G{D-dimer}
    G -->|<500 (or age-adjusted)| H[PE excluded]
    G -->|Above threshold| I[CTPA]
    D --> J{CTPA positive?}
    I --> J
    J -->|Yes| K[Risk stratify + treat]
    J -->|No| L[Consider V/Q + leg Doppler]
```

## Special Populations

### Pregnancy
- **D-dimer** (cut-off debated; may be elevated normally)
- **CXR first** (if normal → V/Q scan; if abnormal → CTPA)
- **Lower radiation** to fetus with V/Q (in normal CXR)

### Renal failure / contrast allergy
- **V/Q scan** preferred (if CXR normal)
- Or CTPA with premedication (steroids, antihistamines)

### High pre-test probability
- **Skip D-dimer** — go directly to CTPA
- D-dimer may be unreliable

## FCPS/MRCP High-Yield Summary

| Domain | Key points |
|--------|------------|
| **Wells >4** | PE likely → CTPA |
| **Wells ≤4** | D-dimer |
| **D-dimer cut-off** | <500 ng/mL; age-adjusted (age × 10) in >50 y |
| **PERC** | All 8 negative = PE excluded |
| **CTPA** | Gold standard imaging |
| **V/Q** | Alternative (pregnancy, contrast contra) |
| **Pregnancy** | D-dimer + CXR + V/Q (low fetal dose) |
| **Sensitivity of CTPA** | 83–100% |
| **Specificity of CTPA** | 89–97% |
| **D-dimer in high pre-test** | Don't use — proceed to imaging |

## MCQs (10)

1. A patient with PE likely (Wells >4) and D-dimer 1500. Next step:
   A. Repeat D-dimer
   B. **CTPA**
   C. V/Q
   D. Discharge
   E. Wait
   **Answer: B** — CTPA.

2. A 70-year-old with Wells 3, D-dimer 600. Age-adjusted threshold:
   A. 200
   B. **700 (70 × 10)**
   C. 1000
   D. 500
   E. 50
   **Answer: B** — Age × 10.

3. PERC rule criteria include all EXCEPT:
   A. Age <50
   B. HR <100
   C. **HR >100**
   D. No prior VTE
   E. SpO₂ ≥95%
   **Answer: C** — HR <100 (not >100).

4. Gold standard imaging for PE:
   A. V/Q
   B. **CTPA**
   C. CXR
   D. Echo
   E. MRI
   **Answer: B** — CTPA.

5. D-dimer specificity is lowest in:
   A. Young healthy
   B. **Elderly, infection, cancer, pregnancy**
   C. Athletes
   D. Children
   E. None
   **Answer: B** — Low specificity in these.

6. V/Q scan is preferred over CTPA in:
   A. All patients
   B. **Pregnancy (with normal CXR) and contrast allergy**
   C. Massive PE
   D. Children
   E. None
   **Answer: B** — Selected cases.

7. D-dimer is most useful for:
   A. Confirming PE
   B. **Excluding PE in low/intermediate pre-test**
   C. Monitoring treatment
   D. Prognosis
   E. None
   **Answer: B** — Excluding.

8. D-dimer cut-off (standard, ng/mL):
   A. 100
   B. **500**
   C. 1000
   D. 2000
   E. 50
   **Answer: B** — 500.

9. CTPA finding suggestive of severe PE:
   A. Normal
   B. **RV/LV ratio ≥1.0**
   C. Pleural effusion
   D. Nodule
   E. None
   **Answer: B** — RV/LV ratio.

10. Wells score component with most points:
    A. HR >100
    B. **Clinical signs of DVT (3 points)**
    C. Active cancer
    D. Haemoptysis
    E. Previous VTE
    **Answer: B** — DVT signs (3 pts).

## SBA Questions (10)

1. A 30-year-old with sudden pleuritic pain, Wells 4.5, D-dimer 200. Next:
   A. CTPA
   B. **PE excluded (D-dimer <500)**
   C. V/Q
   D. Anticoagulate
   E. Discharge
   **Answer: B** — D-dimer <500, PE excluded.

2. A 65-year-old, Wells 3, D-dimer 700. Standard cut-off is 500. Should we proceed to CTPA?
   A. No
   B. **No if age-adjusted (65 × 10 = 650) → 700 > 650 → CTPA**
   C. Yes
   D. Repeat D-dimer
   E. None
   **Answer: B** — Age-adjusted: 700 > 650 → CTPA.

3. A patient with PE suspected, pregnant. Best next step:
   A. CTPA
   B. **CXR → if normal, V/Q; if abnormal, CTPA**
   C. MRI
   D. None
   E. Anticoagulate
   **Answer: B** — CXR first.

4. High pre-test probability (Wells >6), D-dimer normal. Next:
   A. Discharge
   B. **CTPA (D-dimer insufficient to rule out)**
   C. Repeat D-dimer
   D. Wait
   E. None
   **Answer: B** — Image.

5. CTPA shows segmental PE, no RV strain. Treatment:
   A. Thrombolysis
   B. **Anticoagulation (low-risk PE)**
   C. Embolectomy
   D. IVC filter
   E. None
   **Answer: B** — Anticoagulate.

6. The PERC rule allows PE to be excluded without D-dimer when:
   A. Always
   B. **All 8 criteria negative in low-pre-test-probability patient**
   C. Wells >4
   D. Only in pregnancy
   E. None
   **Answer: B** — All 8 negative + low pre-test.

7. Most common reason D-dimer is falsely elevated:
   A. Genetic
   B. **Infection, inflammation, age, cancer, pregnancy**
   C. Liver disease
   D. Anaemia
   E. None
   **Answer: B** — Many causes.

8. V/Q scan in a patient with COPD is most likely to be:
   A. Normal
   B. **Indeterminate (COPD is a confounder)**
   C. PE
   D. Matched defect
   E. None
   **Answer: B** — Indeterminate.

9. CTPA contraindication in:
   A. All
   B. **Severe contrast allergy + severe CKD (relative) + pregnancy (relative)**
   C. None
   D. Children
   E. Asthma
   **Answer: B** — Contrast issues.

10. A patient with D-dimer 480, Wells 2, no PERC. Final step:
    A. CTPA
    B. **PE excluded (D-dimer <500)**
    C. V/Q
    D. Anticoagulate
    E. None
    **Answer: B** — Excluded.

## Flashcards

- **Q: Wells >4 means?**
  A: PE likely → CTPA.

- **Q: Wells ≤4 means?**
  A: PE unlikely → D-dimer.

- **Q: D-dimer cut-off?**
  A: <500 ng/mL; age-adjusted (age × 10) in >50 y.

- **Q: PERC rule?**
  A: All 8 negative = PE excluded in low-risk.

- **Q: Gold standard imaging?**
  A: CTPA.

- **Q: V/Q preferred?**
  A: Pregnancy (with normal CXR), contrast contraindication.

- **Q: Age-adjusted D-dimer for 80 y?**
  A: 800 ng/mL.

- **Q: CTPA severity marker?**
  A: RV/LV ratio ≥1.0.

- **Q: D-dimer use?**
  A: Exclude PE in low/intermediate pre-test.

- **Q: Skip D-dimer in?**
  A: High pre-test probability → go to imaging.

## Answer Key with Explanations

### MCQs
1. **B**  2. **B**  3. **C**  4. **B**  5. **B**  6. **B**  7. **B**  8. **B**  9. **B**  10. **B**

### SBAs
1. **B**  2. **B**  3. **B**  4. **B**  5. **B**  6. **B**  7. **B**  8. **B**  9. **B**  10. **B**

## Summary

Wells score: >4 = PE likely → CTPA. ≤4 = D-dimer. D-dimer <500 (or age-adjusted) → PE excluded. PERC: all 8 negative in low-risk → exclude without D-dimer. CTPA = gold standard. V/Q preferred in pregnancy (normal CXR) and contrast contraindication. CTPA severity: RV/LV ratio ≥1.0.

## Local Navigation
- **Parent Heading**: [[../Pulmonary Vascular Diseases|Pulmonary Vascular Diseases]]
- **Parent Topic Group**: [[../Pulmonary Vascular Diseases/Venous thromboembolic disease|Venous thromboembolic disease]]
- **Chapter Map**: [[../Davidson Chapter 17 - Respiratory Medicine Hierarchy|Respiratory Medicine Hierarchy]]
- **Chapter MOC**: [[../Respiratory MOC|Respiratory MOC]]
- **Related**: [[Pulmonary Embolism]] · [[Subsegmental and incidental pulmonary embolism]] · [[ABG Interpretation]]