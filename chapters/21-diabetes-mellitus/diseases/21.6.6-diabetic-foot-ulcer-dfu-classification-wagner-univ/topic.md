---
tags: [medicine, diabetes, davidson, diabetic-foot-ulcer-dfu-classification-wagner-university-of-texas, fcps, mrcp]
davidson_part: Part 3: Clinical Medicine
davidson_chapter: Chapter 25: Endocrinology and Diabetes
status: full-fcps-mrcp-note
priority: HIGH
exam_relevance: "FCPS/MRCP High Yield - Core diabetes topic"
see_also: ["Diabetic foot ulcer (DFU) classification (Wagner, University of Texas)"]
created: 2026-06-13
modified: 2026-06-13
---

# Diabetic foot ulcer (DFU) classification (Wagner, University of Texas)

## 1. Learning Objectives
By the end of this note you should be able to:
- [ ] Apply Wagner classification (depth-based, grades 0-5)
- [ ] Apply University of Texas classification (depth x infection x ischaemia)
- [ ] Understand why UT classification predicts outcomes better
- [ ] Communicate ulcer stage clearly to MDT

## 2. Definition & Epidemiology
| Feature | Detail |
|--------|--------|
| **Purpose** | Standardise DFU description for prognosis, communication, research |
| **Wagner** | Depth only (0-5); simple but limited |
| **University of Texas** | Depth (Grade 0-3) x Stage (A-D infection/ischaemia); **better prognostic value** |
| **Usage** | Wagner: historical/UK; UT: international/research |

## 3. Clinical Features / Presentation
(N/A - classification based on examination)

## 4. Classification / Staging / Grading

### Wagner Ulcer Classification (1981)
| Grade | Description | Depth |
|-------|-------------|-------|
| **0** | Pre-ulcer (callus, deformity, intact skin) | None |
| **1** | Superficial ulcer (skin/subcutaneous) | <=Subcut |
| **2** | Deep ulcer to tendon, capsule, or bone | Tendon/capsule/bone |
| **3** | Deep + abscess or osteomyelitis | Bone + infection |
| **4** | Forefoot gangrene | Gangrene (partial) |
| **5** | Whole foot gangrene | Gangrene (complete) |

### University of Texas (UT) Classification (1996)
| Grade (Depth) | Stage A (Clean) | Stage B (Infected) | Stage C (Ischaemic) | Stage D (Infected + Ischaemic) |
|---------------|-----------------|-------------------|--------------------|-------------------------------|
| **0** | Pre-ulcer | - | - | - |
| **1** | Superficial | Infected | Ischaemic | Infected + Ischaemic |
| **2** | Deep to tendon/capsule | Infected | Ischaemic | Infected + Ischaemic |
| **3** | Deep to bone/joint | Infected | Ischaemic | Infected + Ischaemic |

> **Infection (Stage B/D)**: >=2 of: purulence, erythema >2cm, warmth, induration, pain, fever, leukocytosis
> **Ischaemia (Stage C/D)**: Absent pulses OR ABI <0.9 OR TBI <0.7

### Comparison: Wagner vs UT
| Aspect | Wagner | UT |
|--------|--------|-----|
| **Dimensions** | Depth only | Depth + Infection + Ischaemia |
| **Grades** | 0-5 | Grade 0-3 x Stage A-D (16 combos) |
| **Prognostic value** | Limited | **Superior** (predicts healing/amp) |
| **Clinical use** | Simple, historical | Preferred for MDT/research |

## 5. Diagnosis & Investigations
| Investigation | Role |
|---------------|------|
| **Clinical exam** | Depth (probe-to-bone), infection signs, pulses |
| **Probe-to-bone** | Positive -> osteomyelitis likely (Wagner 3 / UT Grade 3) |
| **ABI / TBI** | Ischaemia assessment (Stage C/D) |
| **X-ray / MRI** | Osteomyelitis depth (Wagner 2 vs 3 / UT Grade 3) |
| **ESR / CRP** | Infection monitoring |

## 6. Differential Diagnosis
| Condition | Distinguishing Feature |
|-----------|------------------------|
| **Neuropathic ulcer** | Plantar, painless, callus rim, warm, pulses present |
| **Neuroischaemic** | Margins, painful, cool, absent pulses |
| **Ischaemic** | Distal/toes, painful, gangrene, absent pulses |
| **Venous ulcer** | Gaiter area, oedema, lipodermatosclerosis, pulses present |

## 7. Management by Classification
| Classification | Typical Management |
|----------------|-------------------|
| **Wagner 0 / UT 0** | Preventive: callus debridement, offloading insoles |
| **Wagner 1 / UT 1A** | Offloading (TCC), debridement, dressings |
| **Wagner 1 / UT 1B** | Offloading + **oral antibiotics** (PEDIS 2) |
| **Wagner 1 / UT 1C** | Offloading + **vascular assessment** |
| **Wagner 2 / UT 2A/2B** | Offloading + debridement +/- antibiotics |
| **Wagner 2 / UT 2C/2D** | Offloading + **vascular referral** +/- antibiotics |
| **Wagner 3 / UT 3A/3B** | **Antibiotics** (IV if PEDIS 3) + **MRI** for osteomyelitis |
| **Wagner 3 / UT 3C/3D** | **IV antibiotics + vascular referral** + MRI |
| **Wagner 4-5 / UT n/a** | **Urgent vascular + surgical** (amputation likely) |

### PEDIS Infection Grading (for UT Stage B/D)
| Grade | Definition | Treatment |
|-------|------------|-----------|
| **1** | Uninfected | Local care |
| **2** | Mild (superficial, <2cm erythema) | Oral antibiotics |
| **3** | Moderate (deep, >2cm, abscess) | IV antibiotics |
| **4** | Severe (sepsis/SIRS) | IV abx + ICU + urgent surgical |

```mermaid
flowchart TD
    A[DFU Identified] --> B[Assess Depth]
    B --> C{Probe-to-bone?}
    C -->|Yes| D[Wagner 3 / UT Grade 3]
    C -->|No| E{Depth to tendon/capsule?}
    E -->|Yes| F[Wagner 2 / UT Grade 2]
    E -->|No| G[Wagner 1 / UT Grade 1]
    D --> H[Assess Infection]
    F --> H
    G --> H
    H --> I{Purulence/erythema>2cm?}
    I -->|Yes| J[UT Stage B/D + PEDIS 2-3]
    I -->|No| K[UT Stage A/C]
    J --> L[Antibiotics: oral (2) / IV (3)]
    K --> M[Assess Ischaemia]
    L --> M
    M --> N{Absent pulses / ABI<0.9?}
    N -->|Yes| O[UT Stage C/D -> Vascular referral]
    N -->|No| P[UT Stage A/B]
```

## 8. FCPS/MRCP High-Yield Summary
| Topic | Key Points |
|-------|------------|
| **Wagner** | 0: pre-ulcer; 1: superficial; 2: deep to tendon; 3: bone/abscess; 4: forefoot gangrene; 5: whole foot gangrene |
| **UT** | Grade 0-3 (depth) x Stage A-D (A=clean, B=infected, C=ischaemic, D=both) |
| **UT vs Wagner** | UT **superior** - incorporates infection & ischaemia; better prognostic value |
| **PEDIS** | 1: uninfected; 2: mild (oral abx); 3: moderate (IV abx); 4: severe (sepsis/surgery) |
| **Probe-to-bone** | Positive -> Wagner 3 / UT Grade 3; osteomyelitis likely |

## 9. Viva Questions
| Question | Expected Answer |
|----------|-----------------|
| **What is the Wagner classification for diabetic foot ulcers?** | 0: pre-ulcer; 1: superficial; 2: deep to tendon/capsule; 3: bone/abscess; 4: forefoot gangrene; 5: whole foot gangrene |
| **What is the University of Texas classification?** | Grade 0-3 (depth) x Stage A-D (A=clean, B=infected, C=ischaemic, D=both) |
| **Why is UT preferred over Wagner?** | UT incorporates **infection and ischaemia** (Stage B/C/D); better prognostic value for healing/amputation |
| **What defines infection in UT classification?** | >=2 of: purulence, erythema >2cm, warmth, induration, pain, fever, leukocytosis -> Stage B/D |
| **What defines ischaemia in UT classification?** | Absent pedal pulses OR ABI <0.9 OR TBI <0.7 -> Stage C/D |
| **What is the probe-to-bone test?** | Sterile blunt probe through ulcer to bone; **positive PPV 89% for osteomyelitis** (Wagner 3 / UT Grade 3) |

## 10. Confusions & Mnemonics
| Confusion | Clarification |
|-----------|---------------|
| **Wagner 3 = osteomyelitis?** | Wagner 3 = deep + abscess/osteomyelitis; probe-to-bone confirms |
| **UT Grade = Wagner Grade?** | No - UT Grade 3 = bone/joint (like Wagner 3); UT Grade 2 = tendon/capsule (Wagner 2); UT adds infection/ischaemia stages |
| **PEDIS = UT Stage?** | PEDIS grades infection severity (1-4); UT Stage B/D = presence of infection; PEDIS guides antibiotic choice |

**Mnemonic: DFU-WAGNER-UT**
- **D**FU classification: Wagner (depth) vs UT (depth x infection x ischaemia)
- **F**irst: Wagner 0-5 (simple, historical)
- **U**T: Grade 0-3 x Stage A-D (superior, prognostic)
- **W**agner 0: pre-ulcer; 1: superficial; 2: tendon; 3: bone; 4: forefoot gangrene; 5: whole foot
- **A**ssess depth: probe-to-bone -> Wagner 3 / UT Grade 3
- **G**rade UT: 0=pre, 1=superficial, 2=tendon, 3=bone
- **N**o infection = Stage A; **I**nfected = Stage B; **I**schaemic = Stage C; **B**oth = Stage D
- **E**vidence: UT better prognostic value
- **R**esult: MDT uses UT for communication
- **U**lcer depth: probe-to-bone = bone involvement
- **T**x: PEDIS 1-4 guides antibiotics (1=none, 2=oral, 3=IV, 4=sepsis/surgery)

### Local Navigation
- **Parent Heading**: [[Microvascular Complications/Diabetic foot disease|Microvascular Complications/Diabetic foot disease]]
- **Chapter Map": [[../../Davidson Chapter 25 - Diabetes Hierarchy|Diabetes Hierarchy]]
- **Chapter MOC": [[../../Diabetes MOC|Diabetes MOC]]
- **Drug Reference": [[../../../Clinical Therapeutics and Good Prescribing|Drugs]]
- **Related": [[]]

---
## Tags
#medicine #diabetes #davidson #fcps #mrcp #full-fcps-mrcp-note
