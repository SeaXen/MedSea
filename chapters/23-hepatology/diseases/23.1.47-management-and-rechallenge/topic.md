## 1. Learning Objectives
- [ ] Apply immediate management steps for suspected DILI
- [ ] Determine when to use corticosteroids in DILI
- [ ] Apply rechallenge principles and contraindications
- [ ] Monitor and follow-up after DILI
- [ ] Identify FCPS/MRCP high-yield management decisions

---

## 2. Immediate Management of Suspected DILI

```mermaid
flowchart TD
    A[Suspect DILI] --> B[IMMEDIATE: STOP Suspect Drug(s)]
    B --> C[Assess Severity: ALF? Severe DILI? Mild/Moderate?]
    C --> D{ALF Criteria Met?}
    D -->|Yes| E[ICU Admission, NAC, Transplant Evaluation]
    D -->|No| F{Severe DILI?}
    F -->|ALT>10xULN or Jaundice/Coagulopathy| G[Hospital Admission, Close Monitoring]
    F -->|No| H[Outpatient: Stop Drug, Monitor LFTs 2-3x/Week]
    G & H --> I[Monitor LFTs: Daily (Inpatient) / 2-3x/Week (Outpatient)]
    I --> J{Improving?}
    J -->|Yes| K[Continue Monitoring Until Normalisation]
    J -->|No| L[Reassess Diagnosis / Consider Biopsy / Transplant Referral]
```

---

## 3. Stepwise Management

### 1. Immediate Cessation
| Action | Detail |
|--------|--------|
| **STOP Suspect Drug(s)** | **Immediately** — Most Critical Step |
| **All Concomitant Hepatotoxic Drugs** | Stop if Possible (Review Entire Drug List) |
| **Document** | Drug Names, Doses, Duration, Timing Relative to Onset |

> **Exception**: **Do NOT Stop Life-Sustaining Drugs** (e.g., ART for HIV, Anti-rejection for Transplant, Chemotherapy) Without Specialist Input — Use Alternative if Available

### 2. Supportive Care
| Domain | Management |
|--------|------------|
| **Hydration** | IV Fluids if Dehydrated/Nausea/Vomiting |
| **Nausea/Vomiting** | Anti-emetics (Ondansetron, Metoclopramide) |
| **Nutrition** | Small Frequent Meals, Adequate Calories/Protein |
| **Pruritus (Cholestatic)** | Cholestyramine 4g QID (1st Line), Rifampicin 150mg BD, Naltrexone 50mg, Sertraline |
| **Coagulopathy** | Vitamin K 10mg IV/PO if INR >2; FFP Only if Bleeding/Procedure |
| **Encephalopathy** | Lactulose 15-30ml BD → 2-3 Soft Stools; Rifaximin 550mg BD Add-On |
| **Infection Prevention** | No Routine Antibiotics; Surveillance if ICU/Long Stay |

---

## 4. Specific DILI Management by Pattern

### 1. Paracetamol DILI
| Step | Action |
|------|--------|
| **1. NAC Protocol** | IV: 150mg/kg/1h → 50mg/kg/4h → 100mg/kg/16h (Total 300mg/kg/21h) |
| **2. Timing** | Within 8h Optimal; Beneficial up to 24-48h; Staggered/Unknown = Empiric NAC |
| **3. Monitoring** | LFTs, INR, Glucose, Lactate, Renal Function 6-12 Hourly |
| **4. Transplant Referral** | King's College Criteria Met |

### 2. Anti-TB DILI (Isoniazid/Rifampicin/PZA)
| Severity | Action |
|----------|--------|
| **ALT >5×ULN** or **>3×ULN + Symptoms** | **STOP ALL Anti-TB Drugs** |
| **ALT 3-5×ULN Asymptomatic** | Hold Hepatotoxic Drugs (INH, PZA, Rifampicin); Continue Non-Hepatotoxic (Ethambutol, Streptomycin) |
| **Reintroduction** | Sequential: Rifampicin → INH → Ethambutol → PZA (Monitor LFTs Weekly ×2) |

### 3. Immune Checkpoint Inhibitor (ICI) Hepatitis
| Grade | ALT/AST | Management |
|------|---------|------------|
| **Grade 1** | <3×ULN | Continue ICI, Monitor Weekly |
| **Grade 2** | 3-5×ULN | **Hold ICI**, Prednisolone 0.5-1mg/kg, Restart if <3×ULN |
| **Grade 3** | 5-10×ULN | **Hold ICI**, IV Methylprednisolone 1-2mg/kg, Taper Over 4-6 Weeks |
| **Grade 4** | >10×ULN | **Permanently Discontinue ICI**, IV Methylpred 2mg/kg, Taper 6+ Weeks |

---

## 5. Corticosteroid Use in DILI

### Indications for Steroids
| Scenario | Evidence |
|-----------|----------|
| **Autoimmune Features** | High IgG, Autoantibodies, Histology Suggests AIH-Like DILI |
| **Severe Hypersensitivity** | DRESS (Allopurinol, Anticonvulsants, Sulfonamides) |
| **ICI Hepatitis Grade ≥2** | Standard of Care |
| **Severe DILI with AIH-Like Features** | Some Guidelines (Controversial) |
| **Paracetamol DILI** | **NO** (NAC Only — Steroids Harmful in Animal Models) |

### Steroid Regimen (When Indicated)
| Drug | Dose | Taper |
|------|------|-------|
| **Prednisolone** | 0.5-1 mg/kg/day (Max 40-60mg) | Taper Over 4-8 Weeks (Slow: 5-10mg/week) |
| **Methylprednisolone IV** | 1-2 mg/kg/day (If Oral Not Possible) | Switch to Oral Once Improving |
| **Duration** | **Minimum 4-6 Weeks** After Normalisation | Slow Taper (5mg/week) to Prevent Rebound |

> **Contraindications**: Active Infection, Uncontrolled Diabetes, Severe Osteoporosis, Active GI Bleed

---

## 6. Rechallenge Principles

### When to Consider Rechallenge
| Scenario | Approach |
|----------|----------|
| **Essential Drug, No Alternative** | Consider Rechallenge (e.g., Anti-TB, ART, Life-Saving Chemotherapy) |
| **Non-Essential Drug** | **DO NOT Rechallenge** — Avoid |
| **Multiple Drugs Involved** | Reintroduce **One at a Time** (2-4 Week Intervals) |
| **Previous Severe DILI (ALF, DRESS, SJS/TEN)** | **CONTRAINDICATED** — Absolutely Avoid |

### Rechallenge Protocol
```mermaid
flowchart TD
    A[Consider Rechallenge] --> B{Essential Drug?}
    B -->|No| C[DO NOT Rechallenge]
    B -->|Yes| D[RUCAM Causality Confirmed?]
    D -->|Probable/Definite| E[Risk-Benefit Discussion with Patient]
    E --> F[Rechallenge Protocol]
    F --> G[Start Low Dose (25-50% Usual)]
    G --> H[Monitor LFTs Every 3-7 Days]
    H --> I{ALT >3xULN or Symptoms?}
    I -->|Yes| J[STOP Immediately]
    I -->|No| K[Gradual Dose Escalation Over 2-4 Weeks]
    K --> L[Full Dose Achieved → Continue Monitoring Monthly ×3]
```

### Rechallenge Contraindications (Absolute)
| Condition | Rechallenge |
|----------|-------------|
| **Previous ALF** | **Never** |
| **DRESS / SJS / TEN** | **Never** |
| **Autoimmune Hepatitis Triggered by Drug** | **Never** (Risk of Flare) |
| **ICI Grade 4 Hepatitis** | **Never** (Permanent Discontinuation) |
| **Severe Hypersensitivity (Anaphylaxis, SJS/TEN)** | **Never** |

---

## 7. Monitoring After DILI

### Inpatient (Severe DILI)
| Parameter | Frequency |
|-----------|-----------|
| **LFTs (ALT, AST, Bilirubin, ALP, GGT, Albumin)** | Daily → 2-3x/Week as Improving |
| **Coagulation (PT/INR, Fibrinogen)** | Daily → 2-3x/Week |
| **Renal Function (Cr, Urea, Electrolytes)** | Daily |
| **Glucose** | 6-Hourly (If Steroids/NAC) |
| **FBC** | Daily → 2-3x/Week |
| **Ammonia** | If Encephalopathy Suspected |


*...continued (truncated for renderer performance)*
---

> Auto-generated study sections for "Drug Induced Liver Injury" — Ch 23: Hepatology.

## Flashcards (1 generated)

- Q: What is the definition of Drug Induced Liver Injury?
  A: | STOP Suspect Drug(s) | Immediately — Most Critical Step |

## MCQs (1 generated)

1. **Which of the following best describes Drug Induced Liver Injury?**
   A. **| STOP Suspect Drug(s) | Immediately — Most Critical Step |**
   B. An unrelated condition not matching the clinical picture of Drug Induced Liver Injury
   C. A complication seen late in the disease course of Drug Induced Liver Injury
   D. A condition that mimics Drug Induced Liver Injury but has a different underlying cause

