---
tags: [medicine, diabetes, davidson, hypoglycaemia-in-hospital-insulin-error, fcps, mrcp]
davidson_part: Part 3: Clinical Medicine
davidson_chapter: Chapter 25: Endocrinology and Diabetes
status: full-fcps-mrcp-note
priority: HIGH
exam_relevance: "FCPS/MRCP High Yield - Core diabetes topic"
see_also: ["Hypoglycaemia in hospital/insulin error"]
created: 2026-06-13
modified: 2026-06-13
---

# Hypoglycaemia in hospital/insulin error

## 1. Learning Objectives
- [ ] Identify common causes of in-hospital hypoglycaemia (insulin errors, NPO, renal failure)
- [ ] Implement insulin safety protocols (insulin passport, double-check, prescribing standards)
- [ ] Manage NPO patients on glucose-lowering therapy
- [ ] Apply CGM in hospital for high-risk patients

## 2. Definition & Epidemiology
| Feature | Detail |
|--------|--------|
| **Definition** | Blood glucose <3.9 mmol/L in hospitalised patient with diabetes |
| **Incidence** | 10–25% of inpatients with diabetes; severe (<3.0) 3–8% |
| **Mortality association** | Hospital hypoglycaemia → ↑30-day mortality (independent predictor) |
| **Common settings** | ICU, general wards, pre/post-op, renal units, elderly care |

## 3. Clinical Features / Presentation
| Scenario | Typical Presentation |
|----------|---------------------|
| **Insulin prescribing error** | Wrong dose (10x), wrong insulin (rapid vs basal), wrong patient |
| **NPO without adjustment** | Pre-op fasting, procedure delays, unrecognised NPO status |
| **Renal failure** | ↓Insulin/SU clearance; eGFR <30 on glargine/SU/glibenclamide |
| **Sliding scale over-reliance** | Reactive correction without basal coverage → erratic glucose |
| **Corticosteroid taper** | Insulin dose not reduced as steroid tapered |

## 4. Classification / Staging / Grading
| Severity | Glucose | Hospital Action |
|----------|---------|----------------|
| **Level 1 (Alert)** | <3.9 mmol/L | Oral carbs if able; review insulin |
| **Level 2 (Clinical)** | <3.0 mmol/L | Oral/IV carbs; mandatory insulin review |
| **Level 3 (Severe)** | Requires assistance | Glucagon/IV dextrose; incident report; root cause analysis |

## 5. Diagnosis & Investigations
| Investigation | Role |
|---------------|------|
| **CGM (real-time)** | Detects nocturnal/unrecognised hypo; alerts staff |
| **Capillary glucose** | Point-of-care confirmation; q4h if on insulin |
| **Medication review** | Identify culprit (insulin, SU, GLP-1 RA + insulin) |
| **Renal function** | eGFR for dose adjustment |

## 6. Differential Diagnosis
| Cause | Distinguishing Features |
|-------|------------------------|
| **Insulin error** | Sudden hypo after dose; check prescription vs administration |
| **NPO-related** | Hypo during fasting; insulin not held/reduced |
| **Renal failure** | Progressive hypo over days; eGFR <30 on renal-cleared drugs |
| **Factitious** | Self-administered insulin (staff/patient); inconsistent stories |

## 7. Management

### Prevention Protocols
| Protocol | Key Elements |
|----------|--------------|
| **Insulin prescribing** | **Insulin passport**; **double-check** by 2 nurses; **standard concentrations**; separate rapid/basal syringes; **no abbreviations** (U for units) |
| **NPO protocol** | **Basal insulin continued** (50–80% dose); **rapid insulin held**; **glucose 5–10% infusion** if NPO >12h; **pre-procedure checklist** |
| **Renal dosing** | **Auto-alerts** if eGFR<30 on insulin/SU; pharmacist review; dose reduction 25–50% |
| **Corticosteroid taper** | **Insulin reduction protocol** parallel to steroid taper |
| **Sliding scale** | **Avoid standalone** — use basal-bolus with correction doses; if sliding scale → add basal |

### Acute Management in Hospital
```mermaid
flowchart TD
    A[Hospital Hypo <3.9] --> B{Patient conscious?}
    B -->|Yes| C[15-20g fast carbs (oral/NG)]
    B -->|No| D[IV access?]
    D -->|Yes| E[75-80ml 20% dextrose IV → 10% infusion]
    D -->|No| F[Glucagon 1mg IM/SC]
    C --> G[Recheck 15min]
    E --> G
    F --> G
    G --> H{Glucose >3.9?}
    H -->|No| I[Repeat carbs/dextrose]
    H -->|Yes| J[Complex carbs + insulin review]
    I --> G
    J --> K[Root cause analysis within 24h]
```

### Root Cause Analysis (Required for Level 2/3)
| Step | Action |
|------|--------|
| **1. Identify** | Drug, dose, timing, prescriber, administrator |
| **2. Classify** | Prescribing / dispensing / administration / monitoring error |
| **3. System fix** | Protocol update, education, IT alert, formulary change |
| **4. Feedback** | To team, patient, governance |

## 8. FCPS/MRCP High-Yield Summary
| Topic | Key Points |
|-------|------------|
| **Incidence** | 10–25% inpatients with diabetes; severe 3–8% |
| **Top causes** | Insulin errors (wrong dose/type/patient), NPO without adjustment, renal failure, sliding scale overuse |
| **Insulin safety** | Passport, double-check, no abbreviations, standard concentrations |
| **NPO protocol** | Continue basal (50–80%), hold rapid, glucose infusion if >12h NPO |
| **Renal failure** | eGFR<30 → ↓insulin/SU 50%; pharmacist alert |
| **CGM in hospital** | Reduces severe hypo 50%; real-time alerts |
| **Mortality** | Hospital hypo → ↑30-day mortality (independent) |

## 9. Viva Questions
| Question | Expected Answer |
|----------|-----------------|
| **What are the common causes of in-hospital hypoglycaemia?** | Insulin prescribing errors (dose, type, patient), NPO without insulin adjustment, renal failure with unchanged insulin/SU dose, sliding scale over-reliance, corticosteroid taper without insulin reduction |
| **What is the NPO protocol for patients on insulin?** | **Continue basal insulin at 50–80% dose**; **hold rapid insulin**; start **5–10% glucose infusion** if NPO >12h; pre-procedure checklist |
| **How do you adjust insulin in renal failure?** | eGFR <30: **reduce insulin/SU dose by 25–50%**; monitor glucose closely; avoid glibenclamide; consider GLP-1 RA/SGLT2i/DPP-4i |
| **What is an insulin passport?** | Patient-held record of insulin type, dose, device, recent changes; **double-check by 2 nurses** at each administration; reduces errors |
| **What is the role of CGM in hospital?** | Real-time glucose alerts; detects nocturnal/unrecognised hypo; **reduces severe hypoglycaemia by 50%** |
| **Why is sliding scale insulin alone dangerous?** | Reactive only; no basal coverage → erratic glucose; ↑hypo and hyperglycaemia; use basal-bolus with correction |

## 10. Confusions & Mnemonics
| Confusion | Clarification |
|-----------|---------------|
| **Hold all insulin if NPO?** | NO — **continue basal at 50–80%**; only hold rapid/bolus |
| **Glucagon always available in hospital?** | Should be; but IV dextrose faster if access; glucagon for no IV access |
| **Hospital hypo = outpatient hypo?** | Different causes (system errors, NPO, renal); requires system fixes not just patient education |

**Mnemonic: HOSPITAL-HYPO**
- **H**ypoglycaemia in hospital: 10-25% incidence
- **O**ver-reliance on sliding scale → dangerous
- **S**ystem errors: insulin prescribing (dose/type/patient)
- **P**rescribing: **Insulin passport**, double-check, no abbreviations
- **I**nsulin NPO: **basal 50-80%**, hold rapid, glucose infusion
- **T**hree causes: errors, NPO, renal failure
- **A**lert: CGM reduces severe hypo 50%
- **L**evel 2/3: mandatory root cause analysis
- **H**old basal in NPO? NO — 50-80% continued
- **Y**earning for safety: protocolise everything
- **P**harmacist review: eGFR<30 on insulin/SU
- **O**utcome: hypo → ↑30-day mortality

### Local Navigation
- **Parent Heading**: [[Diabetic Emergencies/Severe hypoglycaemia|Diabetic Emergencies/Severe hypoglycaemia]]
- **Chapter Map**: [[../../Davidson Chapter 25 - Diabetes Hierarchy|Diabetes Hierarchy]]
- **Chapter MOC**: [[../../Diabetes MOC|Diabetes MOC]]
- **Drug Reference": [[../../../Clinical Therapeutics and Good Prescribing|Drugs]]
- **Related": [[]]

---
## Tags
#medicine #diabetes #davidson #fcps #mrcp #full-fcps-mrcp-note
