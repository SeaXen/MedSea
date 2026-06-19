---
tags: [medicine, diabetes, davidson, dfu-management-offloading-debridement-infection-revascularisation, fcps, mrcp]
davidson_part: Part 3: Clinical Medicine
davidson_chapter: Chapter 25: Endocrinology and Diabetes
status: full-fcps-mrcp-note
priority: HIGH
exam_relevance: "FCPS/MRCP High Yield - Core diabetes topic"
see_also: ["DFU management (offloading, debridement, infection, revascularisation)"]
created: 2026-06-13
modified: 2026-06-13
---

# DFU management (offloading, debridement, infection, revascularisation)

## 1. Learning Objectives
By the end of this note you should be able to:
- [ ] Execute DFU management: offloading (TCC), debridement, infection (PEDIS), revascularisation
- [ ] Select offloading modality: TCC (gold standard), RCW, felted foam
- [ ] Apply PEDIS infection grading for antibiotic selection
- [ ] Coordinate revascularisation: endovascular 1st -> surgical bypass
- [ ] Integrate MDT care (diabetologist, podiatrist, vascular, orthotist, microbiology, orthopaedics)

## 2. Definition & Epidemiology
| Feature | Detail |
|--------|--------|
| **Goal** | Heal ulcer, prevent amputation, preserve function |
| **Healing rate** | Neuropathic plantar: 80-90% with TCC at 12 weeks |
| **MDT impact** | Reduces major amputations 50-80% |
| **Key principle** | **Offloading is cornerstone**; infection control; revascularisation if PAD |

## 3. Clinical Features / Presentation
(N/A - management of diagnosed DFU)

## 4. Classification / Staging / Grading
(See DFU classification + PEDIS infection grading)

## 5. Diagnosis & Investigations
| Investigation | Role |
|---------------|------|
| **Probe-to-bone** | Osteomyelitis screening (PPV 89%) |
| **X-ray / MRI** | Osteomyelitis extent; Charcot differentiation |
| **ABI / TBI / Angio** | PAD assessment for revascularisation |
| **ESR / CRP / Cultures** | Infection monitoring |
| **HbA1c** | Glycaemic control target |

## 6. Differential Diagnosis
(N/A - management of confirmed DFU)

## 7. Management

### Offloading (Cornerstone of Healing)
| Modality | Efficacy | Indications | Contraindications |
|----------|----------|-------------|-------------------|
| **TCC (Total Contact Cast)** | **Gold standard** - heals 80-90% neuropathic plantar ulcers at 12wk | Plantar neuropathic ulcers; compliant patient | Active infection (PEDIS 3-4), severe PAD (ABI<0.5), non-compliance, severe oedema |
| **Removable Cast Walker (RCW)** | Good IF worn 24/7 | TCC contraindicated; patient preference | Non-compliance risk |
| **Felted foam / Insoles** | Adjunct / prevention | Minor ulcers, prevention | Insufficient alone for active ulcer |
| **Surgical offloading** | Tendon lengthening, metatarsal head resection | Recurrent ulcers despite conservative | - |

> **TCC protocol**: Fibreglass/plaster; molded to contour; window for wound access; changed weekly; non-weightbearing if possible

### Debridement
| Type | Frequency | Technique |
|------|-----------|-----------|
| **Sharp (scalpel/curette)** | Weekly at dressing change | Remove all necrotic tissue, callus, slough; bleed = viable |
| **Autolytic** | Between changes | Hydrogel/hydrocolloid dressings |
| **Enzymatic** | If sharp not possible | Collagenase/santyl |
| **Biological** | Maggot therapy | Specialist centres |

### Infection Management (PEDIS-Based)
| PEDIS Grade | Definition | Antibiotics | Duration |
|-------------|------------|-------------|----------|
| **1** | Uninfected | None | - |
| **2** | Mild (superficial, <2cm erythema) | **Oral**: Flucloxacillin 500mg QDS OR Co-amoxiclav 625mg TDS | 1-2 weeks |
| **3** | Moderate (deep, >2cm, abscess, lymphangitis) | **IV**: Piperacillin-tazobactam 4.5g TDS OR Ceftriaxone 2g OD + Metronidazole 500mg TDS | 2-4 weeks |
| **4** | Severe (sepsis/SIRS) | Same IV + ICU + **urgent surgical debridement** | 4-6 weeks |

> **Osteomyelitis**: Add **rifampicin** 300mg BD (biofilm) if prosthetic material; surgical debridement often needed

### Revascularisation
| Indication | Approach |
|------------|----------|
| **Tissue loss (Wagner >=3 / UT Stage C/D)** | **Urgent** CT/MR angiography -> Endovascular 1st (angioplasty/stent) -> Surgical bypass if unsuitable |
| **Rest pain** | Same pathway |
| **Contraindication** | Non-reconstructible (diffuse tibial disease) -> consider amputation |

### Charcot Neuroarthropathy (Eichenholtz Staging)
| Stage | Features | Management |
|-------|----------|------------|
| **0 (Development)** | Hot, swollen, erythematous; normal X-ray; MRI: marrow oedema | **TCC immobilisation** (non-WB 8-12wk -> WB in TCC 4-8wk) |
| **1 (Fragmentation)** | Bone fragmentation, joint dislocation, debris; "rocker-bottom" | TCC until quiescent |
| **2 (Coalescence)** | Decreased heat/swelling; early fusion | Transition to custom footwear/orthoses |
| **3 (Reconstruction)** | Consolidated, stable deformity | Custom footwear, accommodative orthoses, surgery if unstable |

> **Differentiation from osteomyelitis**: Charcot = hot swollen foot, **preserved pulses**, bilateral rare, X-ray fragmentation/dislocation, no systemic sepsis

### MDT Composition & Outcomes
| Member | Role |
|--------|------|
| **Diabetologist** | Glycaemic control, medical optimisation |
| **Podiatrist** | Debridement, offloading, wound care |
| **Vascular surgeon** | Revascularisation (endovascular/surgical) |
| **Orthotist** | Custom footwear, insoles, TCC application |
| **Microbiologist** | Antibiotic stewardship, culture interpretation |
| **Orthopaedic surgeon** | Debridement, amputation, Charcot reconstruction |
| **Nurse specialist** | Wound dressing, patient education, coordination |

> **MDT Outcome**: Major amputations reduced 50-80%; healing rates increased; cost-effective

```mermaid
flowchart TD
    A[New DFU] --> B[Assess: IWGDF risk, Wagner/UT, PEDIS, ABI]
    B --> C{PEDIS Grade?}
    C -->|1 (Uninfected)| D[TCC offloading + sharp debridement + dressings]
    C -->|2 (Mild)| E[TCC + oral abx + debridement]
    C -->|3 (Moderate)| F[TCC + IV abx + debridement +/- vascular]
    C -->|4 (Severe)| G[ICU + IV abx + URGENT surgical debridement +/- amputation]
    D --> H{Healing at 4wk?}
    E --> H
    F --> H
    G --> H
    H -->|No| I[Review: infection? ischaemia? offloading adherence?]
    H -->|Yes| J[Continue -> preventive footwear]
    I --> K[MDT discussion: vascular imaging, MRI, surgical options]
    K --> L[Revascularisation if PAD]
    L --> M[Continue offloading + wound care]
```

## 8. FCPS/MRCP High-Yield Summary
| Topic | Key Points |
|-------|------------|
| **Offloading** | **TCC = gold standard** (80-90% heal); RCW if TCC contraindicated |
| **Debridement** | Sharp weekly; remove all necrotic/callus; bleed = viable |
| **Infection (PEDIS)** | 1: none; 2: mild (oral abx); 3: moderate (IV abx); 4: severe (sepsis/surgery) |
| **Osteomyelitis** | Probe-to-bone +ve (PPV 89%); MRI gold standard; rifampicin for biofilm |
| **Revascularisation** | Endovascular 1st -> surgical bypass; urgent if tissue loss |
| **Charcot** | Eichenholtz 0-3; **hot swollen foot + preserved pulses**; TCC immobilisation |
| **MDT** | Diabetologist, podiatrist, vascular, orthotist, microbiology, orthopaedics -> **amputations reduced 50-80%** |

## 9. Viva Questions
| Question | Expected Answer |
|----------|-----------------|
| **What is the gold standard offloading for neuropathic plantar ulcers?** | **Total Contact Cast (TCC)** - heals 80-90% at 12 weeks |
| **What are PEDIS infection grades?** | 1: uninfected; 2: mild (oral abx); 3: moderate (IV abx); 4: severe (sepsis + urgent surgery) |
| **How do you manage osteomyelitis in DFU?** | Probe-to-bone +ve -> MRI; **rifampicin 300mg BD** (biofilm); surgical debridement often needed; 6-week antibiotics |
| **When do you revascularise a diabetic foot?** | Tissue loss (Wagner >=3 / UT Stage C/D) -> urgent CT/MR angio -> endovascular 1st -> surgical bypass |
| **How do you differentiate Charcot from osteomyelitis?** | **Charcot**: hot swollen foot, **preserved pulses**, bilateral rare, X-ray fragmentation/dislocation, no systemic sepsis; **Osteomyelitis**: ulcer + probe-to-bone +ve, elevated ESR/CRP, MRI marrow oedema |
| **What is the MDT for diabetic foot?** | Diabetologist, podiatrist, vascular surgeon, orthotist, microbiologist, orthopaedic surgeon, nurse specialist - **reduces amputations 50-80%** |

## 10. Confusions & Mnemonics
| Confusion | Clarification |
|-----------|---------------|
| **TCC for all ulcers?** | NO - contraindicated in active infection (PEDIS 3-4), severe PAD (ABI<0.5), non-compliance |
| **Bisphosphonates for Charcot?** | Not standard; some use IV zoledronic acid 5mg for reduced bone turnover; limited evidence |
| **Charcot = osteomyelitis?** | NO - Charcot has **preserved pulses**, hot swollen foot; osteomyelitis has ulcer + probe-to-bone + elevated inflammatory markers |

**Mnemonic: DFU-MGMT-TCC**
- **D**FU management: offload, debride, infect, vascular
- **F**irst: **TCC gold standard** (80-90% heal)
- **U**lcer debridement: sharp weekly, bleed = viable
- **M**anage infection: PEDIS 1-4 (1=none, 2=oral, 3=IV, 4=sepsis/surgery)
- **G**old standard osteomyelitis: probe-to-bone + MRI; rifampicin + surgery
- **M**ulti-disciplinary: **amputations reduced 50-80%**
- **T**otal contact cast (TCC): non-WB 8-12wk
- **C**harcot: hot swollen + pulses = TCC (Eichenholtz 0-3)
- **C**ontraindications TCC: infection, severe PAD, non-compliance
- **R**evascularisation: endo 1st -> surgical
- **E**ichenholtz: 0=dev, 1=frag, 2=coal, 3=recon
- **V**ascular: endo 1st -> surgical bypass
- **E**ichenholtz: 0=dev, 1=frag, 2=coal, 3=recon
- **E**vidence: MDT reduces amputations 50-80%

### Local Navigation
- **Parent Heading**: [[Microvascular Complications/Diabetic foot disease|Microvascular Complications/Diabetic foot disease]]
- **Chapter Map": [[../../Davidson Chapter 25 - Diabetes Hierarchy|Diabetes Hierarchy]]
- **Chapter MOC": [[../../Diabetes MOC|Diabetes MOC]]
- **Drug Reference": [[../../../Clinical Therapeutics and Good Prescribing|Drugs]]
- **Related": [[]]

---
## Tags
#medicine #diabetes #davidson #fcps #mrcp #full-fcps-mrcp-note
