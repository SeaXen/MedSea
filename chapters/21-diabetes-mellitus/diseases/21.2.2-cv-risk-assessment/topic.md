# CV risk assessment

---
tags: [medicine, diabetes, davidson, cv-risk-assessment, fcps, mrcp]
davidson_part: Part 3: Clinical Medicine
davidson_chapter: Chapter 25: Endocrinology and Diabetes
status: full-fcps-mrcp-note
priority: HIGH
exam_relevance: "FCPS/MRCP High Yield - Core diabetes topic"
see_also: ["Diabetes as cardiovascular risk equivalent", "ASCVD risk calculators (QRISK3, ASCVD Pooled Cohort)", "Statin therapy in diabetes (intensity, targets)"]
created: 2026-06-13
modified: 2026-06-13
---

# CV risk assessment

## 1. Learning Objectives
By the end of this note you should be able to:
- [ ] Apply QRISK3 and ASCVD Pooled Cohort risk calculators
- [ ] Determine statin and aspirin indications
- [ ] Apply BP and lipid targets
- [ ] Apply SGLT2i/GLP-1 RA for CV risk reduction

## 2. Definition & Epidemiology
| Feature | Detail |
|--------|--------|
| **CV Risk** | Diabetes = 2-4x CVD risk |
| **Leading cause death** | CVD (50-60% of diabetes deaths) |
| **Equivalent** | T2DM age >40 = CHD risk equivalent (historical) |

## 3. Clinical Features / Presentation
(N/A - risk assessment)

## 4. Classification / Staging / Grading

### Risk Calculators
| Calculator | Region | Includes Diabetes |
|-----------|--------|-------------------|
| **QRISK3** | UK | Yes (type, duration, HbA1c, eGFR) |
| **ASCVD Pooled Cohort** | US | Binary (yes/no) |
| **SCORE2 / SCORE2-DP** | Europe | Duration, complications |

### QRISK3 Variables
| Variable | Included |
|----------|----------|
| **Diabetes** | Type, duration, HbA1c |
| **Renal** | eGFR, CKD |
| **Medications** | Steroids, antipsychotics |
| **Atrial fibrillation** | Yes |
| **Migraine** | Yes |
| **SLE/RA** | Yes |
| **Deprivation** | Townsend score |

### Statin Intensity Guidelines
| Guideline | Population | Statin | Target LDL |
|-----------|------------|--------|------------|
| **NICE (UK)** | T2DM age 40-84 | Atorvastatin 20mg (primary); 80mg (secondary) | <1.8mmol/L or ↓50% |
| **ADA/ACC (US)** | DM age 40-75 | High-intensity atorvastatin 40-80mg | <1.8mmol/L or ↓50% |
| **ADA/ACC (US)** | DM age >75 | Moderate-intensity | <1.8mmol/L or ↓30-50% |
| **ESC/EAS (EU)** | DM (very high risk) | High-intensity | <1.4mmol/L or ↓50% |
| **ESC/EAS (EU)** | DM + ASCVD | High-intensity + ezetimibe | <1.0mmol/L or ↓50% |

## 5. Diagnosis & Investigations
| Test | Frequency |
|------|-----------|
| **Lipid profile** | Baseline, 3 months post-statin, then 6-12 monthly |
| **HbA1c** | 3-monthly until target, then 6-monthly |
| **BP** | Every visit |
| **UACR/eGFR** | Annual |

## 5. Diagnosis & Investigations
| Test | Frequency |
|------|-----------|
| **Lipid profile** | Baseline, 3 months post-statin, then 6-12 monthly |
| **HbA1c** | 3-monthly until target, then 6-monthly |
| **BP** | Every visit |
| **UACR/eGFR** | Annual |

## 6. Differential Diagnosis
(N/A)

## 7. Management

### CV Risk Assessment Algorithm
```mermaid
flowchart TD
    A[Diabetes Patient] --> B{Established ASCVD?}
    B -->|Yes| C[High-intensity statin + aspirin 75mg]
    B -->|No| D{10-year Risk >=10% (QRISK3/ASCVD)?}
    D -->|Yes| E[High-intensity statin; consider aspirin (ADA)]
    D -->|No| F[Lifestyle; consider moderate statin]
    E --> G[LDL target <1.8mmol/L or ↓50%]
    F --> G
    G --> H{LDL target met?}
    H -->|No| I[Add ezetimibe 10mg]
    H -->|Yes| J[Continue + monitor 6-12mo]
```

### Aspirin Primary Prevention
| Guideline | Recommendation |
|-----------|----------------|
| **ADA 2024** | Age 50-70, ASCVD risk ≥10%, low bleeding risk |
| **ESC 2021** | **Not recommended** (net harm) |
| **NICE NG128** | **Do not offer** |
| **ASCEND Trial** | DM no CVD: ↓vascular events 12% but ↑major bleeding 29% → net neutral |

### BP Targets
| Guideline | Target |
|-----------|--------|
| **ADA/ESC** | **<130/80** |
| **NICE** | <140/90 clinic (<135/85 ABPM); <130/80 if CKD/albuminuria |
| **KDIGO** | CKD/Albuminuria: <130/80 |

## 8. FCPS/MRCP High-Yield Summary
| Topic | Key Points |
|-------|------------|
| **Risk calculators** | QRISK3 (UK, includes DM details); ASCVD Pooled Cohort (US, binary DM) |
| **Statin** | Age 40-75: high-intensity atorvastatin 40-80mg; target LDL <1.8mmol/L |
| **Aspirin primary** | ADA: age 50-70, risk≥10%; ESC/NICE: not routinely |
| **BP targets** | ADA/ESC: <130/80; NICE: <130/80 if CKD/albuminuria |
| **LDL targets** | Primary: <1.8mmol/L; Secondary: <1.4mmol/L; Extreme: <1.0mmol/L |

## 9. Viva Questions
| Question | Expected Answer |
|----------|-----------------|
| **What CVD risk calculator is used in the UK?** | **QRISK3** – includes age, sex, ethnicity, smoking, diabetes (type, duration, HbA1c), CKD, eGFR, steroids, AF, BP, cholesterol, BMI, FH, deprivation |
| **What statin intensity for T2DM age 40-75 without ASCVD?** | High-intensity atorvastatin 40-80mg (ADA/ACC); NICE: atorvastatin 20mg |
| **When is aspirin recommended for primary prevention in diabetes?** | ADA: age 50-70, 10-year ASCVD risk ≥10%, no bleeding risk; ESC/NICE: not routinely |
| **What is the LDL target for primary prevention in diabetes?** | <1.8mmol/L or ≥50% reduction from baseline |
| **What is the QRISK3 threshold for statin in UK?** | QRISK3 ≥10% 10-year CVD risk |

## 10. Confusions & Mnemonics
| Confusion | Clarification |
|-----------|---------------|
| **All diabetics need high-intensity statin?** | Age >75 or frail: moderate intensity; primary prevention age 40-75 = high-intensity |
| **Aspirin for all diabetics?** | NO - primary prevention: selective (ADA) or not recommended (ESC/NICE); secondary: ALWAYS |
| **LDL <1.8 for everyone?** | Secondary prevention: <1.4; extreme risk: <1.0 (ESC) |

**Mnemonic: CVD-RISK-DM-CALC**
- **C**VD risk: 2-4x in DM
- **V**ascular death: 50-60% of DM deaths
- **D**iabetes: risk enhancer in all calculators
- **R**ISK3 (UK): includes DM type, duration, HbA1c, eGFR
- **I**SCVD Pooled (US): binary DM only
- **S**CORE2 (EU): duration + complications
- **K**DIGO: CKD specific
- **C**alculator choice: by geography
- **A**spirin: primary prevention selective (ADA) or none (ESC/NICE)
- **L**DL targets: primary <1.8; secondary <1.4
- **C**alculator: don't mix (different populations)
- **U**ndersestimate: young T1DM (10yr low, lifetime high)
- **L**ipoproteins: apoB, non-HDL if high TG
- **A**ge: young T1DM low 10yr risk
- **T**hresholds: UK ≥10% (QRISK3); US ≥7.5% (ASCVD)
- **O**verestimation: well-controlled T2DM
- **R**efinement: CAC score, Lp(a) if intermediate risk**</think>
---

> Auto-generated study sections for "Annual review and complication screening" — Ch 21: Diabetes Mellitus.

## Flashcards (8 generated)

- Q: What is the definition of Annual review and complication screening?
  A: By the end of this note you should be able to:
- Q: What is CV Risk of Annual review and complication screening?
  A: Diabetes = 2-4x CVD risk
- Q: What causes Annual review and complication screening?
  A: CVD (50-60% of diabetes deaths)
- Q: What is Risk calculators of Annual review and complication screening?
  A: QRISK3 (UK, includes DM details); ASCVD Pooled Cohort (US, binary DM)
- Q: What is Statin of Annual review and complication screening?
  A: Age 40-75: high-intensity atorvastatin 40-80mg; target LDL <1.8mmol/L
- Q: What is Aspirin primary of Annual review and complication screening?
  A: ADA: age 50-70, risk≥10%; ESC/NICE: not routinely
- Q: What is BP targets of Annual review and complication screening?
  A: ADA/ESC: <130/80; NICE: <130/80 if CKD/albuminuria
- Q: What is LDL targets of Annual review and complication screening?
  A: Primary: <1.8mmol/L; Secondary: <1.4mmol/L; Extreme: <1.0mmol/L

## MCQs (1 generated)

1. **Which of the following best describes Annual review and complication screening?**
   A. **By the end of this note you should be able to:**
   B. An unrelated condition not matching the clinical picture of Annual review and complication screening
   C. A complication seen late in the disease course of Annual review and complication screening
   D. A condition that mimics Annual review and complication screening but has a different underlying cause

## SBA Questions (1 generated)

1. A patient with suspected Annual review and complication screening presents with: CV Risk — Diabetes = 2-4x CVD risk; Leading cause death — CVD (50-60% of diabetes deaths); Equivalent — T2DM age >40 = CHD risk equivalent (historical). What is the most likely diagnosis?
   A. **Annual review and complication screening**
   B. A condition that mimics Annual review and complication screening but is not the same entity
   C. A complication of Annual review and complication screening rather than the primary diagnosis
   D. An unrelated condition in the same clinical category as Annual review and complication screening

