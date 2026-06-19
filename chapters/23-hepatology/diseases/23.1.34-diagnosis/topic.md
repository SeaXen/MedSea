---
tags: [hepatology, chronic_liver_disease, cirrhosis, diagnosis, fibroscan, elf, fib4, apri, biopsy, fcps, mrcp]
davidson_chapter: Chapter 24
status: full-fcps-mrcp-note
priority: high
exam_relevance: "Diagnosis of cirrhosis - non-invasive fibrosis assessment (FibroScan, ELF, FIB-4, APRI) and liver biopsy indications - FCPS/MRCP diagnostic pathway"
see_also: ["Chronic Liver Disease and Cirrhosis/Definition and classification", "Chronic Liver Disease and Cirrhosis/Compensated vs decompensated cirrhosis", "Chronic Liver Disease and Cirrhosis/Aetiology", "Portal Hypertension and Complications/Ascites", "Liver Transplantation/Liver Transplantation"]
created: 2025-06-13
modified: 2025-06-13
---

# Diagnosis of Cirrhosis: Non-Invasive Fibrosis Assessment & Biopsy

## Learning Objectives
- [ ] Apply non-invasive fibrosis scores (FIB-4, NFS, APRI, ELF, FibroScan)
- [ ] Interpret FibroScan (VCTE) results with CAP and LSM
- [ ] Know indications and contraindications for liver biopsy
- [ ] Apply diagnostic algorithms for cirrhosis diagnosis
- [ ] Identify FCPS/MRCP high-yield diagnostic thresholds

---

## Diagnostic Approach

```mermaid
flowchart TD
    A[Suspect Cirrhosis: Risk Factors + Abnormal LFTs/Platelets] --> B[Non-Invasive Fibrosis Assessment]
    B --> C[Calculate FIB-4 / NFS / APRI]
    B --> D[FibroScan (VCTE) if Available]
    C --> E{Score Interpretation}
    D --> E
    E -->|Low Risk| F[Monitor / Exclude Cirrhosis]
    E -->|Intermediate| G[FibroScan / ELF / Referral]
    E -->|High Risk| H[Consider Liver Biopsy if Indicated]
    H --> I[Diagnose Cirrhosis]
    F --> J[Surveillance if Risk Factors]
```

---

## Non-Invasive Fibrosis Scores

### 1. FIB-4 (First-Line, Cheap, Widely Available)
```
FIB-4 = (Age × AST) / (Platelets × √ALT)
```
| Cut-off | Interpretation |
|---------|----------------|
| **<1.3** | **Low Risk** Advanced Fibrosis (NPV >90%) |
| **1.3-2.67** | **Indeterminate** — Need Further Testing |
| **>2.67** | **High Risk** Advanced Fibrosis (PPV ~65%) |

> **Age-Adjusted**: For >65y use <2.0 / >3.0; For <35y use <1.45 / >3.0

### 2. NFS (NAFLD Fibrosis Score)
```
NFS = -1.675 + 0.037×Age + 0.094×BMI + 1.13×IFG/DM + 0.99×AST/ALT - 0.013×Platelets - 0.66×Albumin
```
| Cut-off | Interpretation |
|---------|----------------|
| **<-1.455** | Low Risk Advanced Fibrosis |
| **-1.455 to 0.676** | Indeterminate |
| **>0.676** | High Risk Advanced Fibrosis |

### 3. APRI (AST to Platelet Ratio Index)
```
APRI = (AST / ULN_AST) × 100 / Platelets (10⁹/L)
```
| Cut-off | Interpretation |
|---------|----------------|
| **<0.5** | No Significant Fibrosis |
| **0.5-1.5** | Indeterminate |
| **>1.5** | Significant Fibrosis |
| **>2.0** | Cirrhosis |

### 4. ELF (Enhanced Liver Fibrosis) — Blood Test Panel
| Components | HA (Hyaluronic Acid), PIIINP, TIMP-1 |
|------------|--------------------------------------|
| **Cut-off** | **<7.7**: No Advanced Fibrosis; **7.7-9.7**: Indeterminate; **>9.7**: Advanced Fibrosis |
| **Advantage** | Better Accuracy than FIB-4/NFS; Not Widely Available |

### 5. FibroScan (VCTE) — Gold Standard Non-Invasive
| Measurement | Cut-off (kPa) | Fibrosis Stage |
|-------------|---------------|----------------|
| **LSM** (Liver Stiffness) | **<7.0** | F0-F1 (No/Mild) |
| | **7.0-9.5** | F2 (Significant) |
| | **9.5-12.5** | F3 (Advanced) |
| | **>12.5-15.0** | **F4 (Cirrhosis)** |
| **CAP** (Controlled Attenuation Parameter) | **>238 dB/m** | Steatosis ≥S1 |
| | **>260 dB/m** | Steatosis ≥S2 |
| | **>290 dB/m** | Steatosis ≥S3 |

> **FibroScan Limitations**: Obesity (Use XL Probe), Ascites, Acute Inflammation, Biliary Obstruction

---

## FibroScan Probe Selection
| Probe | Indication |
|-------|------------|
| **M Probe (Standard)** | BMI <30, Skin-Capsule Distance <25mm |
| **XL Probe** | **BMI ≥30**, Skin-Capsule Distance ≥25mm |

> **Failure Rate**: M Probe 10-15% in Obese; XL Probe Reduces Failure to <5%

---

## Diagnostic Algorithm

```mermaid
flowchart TD
    A[Suspect CLD] --> B[Calculate FIB-4 / NFS]
    B --> C{FIB-4 / NFS}
    C -->|Low Risk| D[Monitor Annually]
    C -->|Indeterminate| E[FibroScan (VCTE)]
    C -->|High Risk| F[Consider Biopsy / Referral]
    E --> G{FibroScan LSM}
    G -->|<7 kPa| H[Exclude Cirrhosis]
    G -->|7-12.5 kPa| I[Significant/Advanced Fibrosis → Referral]
    G -->|>12.5-15 kPa| J[**Cirrhosis Likely** → Manage as Cirrhosis]
    G -->|>15 kPa| K[**Cirrhosis** → Manage as Cirrhosis]
    J & K --> L[Clinical Correlation + Referral]
```

---

## Liver Biopsy Indications

### When to Biopsy
| Indication | Detail |
|-----------|--------|
| **Indeterminate Non-Invasive Tests** | FIB-4 1.3-2.67 + FibroScan Discordant/Unavailable |
| **Atypical Features** | Suspected Alternative Diagnosis (AIH, DILI, Wilson, Drug) |
| **Clinical Trial Enrollment** | Histologic Endpoints Required |
| **Pre-Treatment Baseline** | Some Guidelines (Optional for DAA) |
| **Post-Transplant** | Rejection, Recurrence, Protocol Biopsies |

### Contraindications
| Absolute | Relative |
|----------|----------|
| Uncorrectable Coagulopathy (INR>1.5, Plt<50k) | Morbid Obesity (Technical Difficulty) |
| Uncontrolled Ascites (Large Volume) | Acute Infection |
| Patient Refusal | Amyloidosis (Bleeding Risk) |
| Suspected Vascular Tumour (HCC) | Right Heart Failure (↑ Bleeding Risk) |

### Biopsy Techniques
| Technique | Indication |
|-----------|------------|
| **Percutaneous** | Standard (Ultrasound-Guided) |
| **Transjugular (TJLB)** | Coagulopathy, Ascites (TIPS Setting) |
| **Laparoscopic** | During Laparoscopy for Other Reason |
| **EUS-Guided** | Targeted Lesion Sampling |

---

## Histological Staging Systems

### METAVIR (Most Common)
| Stage | Description |
|-------|-------------|
| **F0** | No Fibrosis |
| **F1** | Portal Fibrosis Without Septa |
| **F2** | Portal Fibrosis With Rare Septa |
| **F3** | Numerous Septa Without Cirrhosis |
| **F4** | **Cirrhosis** (Bridging Fibrosis + Nodules) |

### Ishak / Knodell (More Granular)
| Ishak Stage | Description |
|-------------|-------------|
| 0 | No Fibrosis |
| 1-2 | Portal Fibrosis |
| 3-4 | Bridging Fibrosis |
| 5 | Incomplete Cirrhosis |
| 6 | **Established Cirrhosis** |

---

## NASH CRN Histologic Scoring (Biopsy)
| Component | Score |
|-----------|-------|
| **Steatosis** (0-3) | 0: <5%, 1: 5-33%, 2: 33-66%, 3: >66% |
| **Ballooning** (0-2) | 0: None, 1: Few, 2: Many |
| **Lobular Inflammation** (0-3) | 0: None, 1: <2 Foci, 2: 2-4, 3: >4 |
| **NAS Score** | **Steatosis + Ballooning + Inflammation (0-8)** |
| **NAS ≥5** = **NASH**; **NAS 3-4** = Borderline; **NAS <3** = Not NASH |
| **Fibrosis** (0-4) | Per METAVIR |

---

## Diagnostic Accuracy Comparison

| Test | Sensitivity (F4) | Specificity (F4) | Advantages |
|------|------------------|------------------|------------|
| **FibroScan LSM** | 85-95% | 85-95% | **Best Overall**, Instant, Repeatable |
| **FIB-4** | 70-80% | 70-80% | Free, Universal (Age, AST, ALT, Plt) |
| **NFS** | 75-85% | 75-85% | Adds BMI, DM, Albumin |
| **ELF** | 85-95% | 85-95% | Best Blood Test; Limited Availability |
| **APRI** | 60-75% | 70-85% | Simple (AST, Platelets) |
| **Biopsy** | **Gold Standard** | **Gold Standard** | Invasive, Sampling Error |

---

## FCPS/MRCP High-Yield Summary

| Concept | Key Points |
|---------|------------|
| **FIB-4 Formula** | (Age × AST) / (Platelets × √ALT) |
| **FIB-4 Cut-offs** | **<1.3 Low**, **>2.67 High** (Age-Adjusted >65y) |
| **FibroScan LSM** | **<7 F0-F1, 7-9.5 F2, 9.5-12.5 F3, >12.5-15 F4** |
| **CAP** | **>238 S1, >260 S2, >290 S3** |
| **Biopsy Indications** | Indeterminate Non-Invasive, Atypical, Trials |
| **Biopsy Contraindications** | INR>1.5, Plt<50k, Large Ascites, Refusal |
| **METAVIR F4** | Cirrhosis (Bridging Fibrosis + Nodules) |
| **NASH NAS Score** | **≥5 = NASH**, 3-4 Borderline, <3 Not NASH |
| **FibroScan XL Probe** | BMI ≥30 or Skin-Capsule >25mm |

---

## Viva Questions

1. **What is the FIB-4 formula and cut-offs?**
2. **What are FibroScan LSM cut-offs for F0-F4?**
3. **When do you use XL probe vs M probe for FibroScan?**
4. **What are the indications for liver biopsy in cirrhosis?**
4. **What are the contraindications to liver biopsy?**
5. **What is METAVIR F4?**
5. **How does CAP differ from LSM?**
6. **What is the FIB-4 cut-off for high risk?**
6. **What is APRI and its cut-off for cirrhosis?**
7. **When do you order ELF test?**
7. **What is the NAS score for NASH diagnosis?**

---

## Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| FIB-4 vs NFS | FIB-4: Age, AST, ALT, Platelets; NFS: Adds BMI, DM, Albumin, AST/ALT Ratio |
| FibroScan Probes | **M Probe** (Standard); **XL Probe** for BMI>30 or Skin-Capsule >25mm |
| F4 vs Cirrhosis | **METAVIR F4 = Cirrhosis** (Bridging Fibrosis + Nodules) |
| CAP vs LSM | **CAP = Steatosis (dB/m)**; **LSM = Stiffness/Fibrosis (kPa)** |
| FIB-4 Age Adjustment | >65y: Low <2.0, High >3.0; <35y: Low <1.45, High >3.0 |
| APRI vs FIB-4 | APRI: AST/Platelets Only; FIB-4: Adds Age, ALT |
| ELF Availability | **Not Widely Available** — Specialized Centers Only |
| Biopsy in Cirrhosis | Not Routine — Only if Indeterminate/Atypical/Clinical Trials |

---

## Mind Map

```mermaid
mindmap
  root((Cirrhosis Diagnosis))
    Non-Invasive Scores
      FIB-4: Age, AST, ALT, Platelets
      <1.3 Low, >2.67 High
      NFS: BMI, DM, Albumin
      APRI: AST/Platelets
      ELF: HA, PIIINP, TIMP-1
    FibroScan
      LSM: <7 F0-F1, 7-9.5 F2, 9.5-12.5 F3, >12.5 F4
      CAP: >238 S1, >260 S2, >290 S3
      Probes: M (Standard) vs XL (BMI>30)
    Biopsy
      Indications: Indeterminate, Atypical, Trials
      Contraindications: INR>1.5, Plt<50k, Ascites
      METAVIR: F0-F4 (F4=Cirrhosis)
      NAS Score: Steatosis+Ballooning+Inflammation
      NAS>=5 = NASH
    Algorithm
      FIB-4/NFS → Low=Monitor, Indeterminate=FibroScan, High=Referral
      FibroScan <7=Exclude, 7-12.5=Refer, >12.5=Cirrhosis
```

---

## One-Page Revision Card

| **Non-Invasive Scores** | **Low Risk** | **High Risk** |
|-------------------------|--------------|---------------|
| **FIB-4** | <1.3 | >2.67 |
| **NFS** | <-1.455 | >0.676 |
| **APRI** | <0.5 | >2.0 |
| **FibroScan LSM** | <7.0 kPa | >12.5 kPa |
| **CAP** | <238 dB/m | >290 dB/m |

| **FibroScan** | **Cut-off (kPa)** | **Stage** |
|---------------|-------------------|-----------|
| F0-F1 | <7.0 | No/Mild Fibrosis |
| F2 | 7.0-9.5 | Significant |
| F3 | 9.5-12.5 | Advanced |
| **F4 (Cirrhosis)** | **>12.5-15.0** | **Cirrhosis** |

| **Biopsy** | |
|------------|--|
| **Indications** | Indeterminate Non-Invasive, Atypical, Trials |
| **Contraindications** | INR>1.5, Plt<50k, Large Ascites, Refusal |
| **METAVIR F4** | **Cirrhosis** (Bridging Fibrosis + Nodules) |

| **NAS Score** | **Steatosis + Ballooning + Inflammation** |
|---------------|------------------------------------------|
| **≥5** | **NASH** |
| 3-4 | Borderline |
| <3 | Not NASH |

---

## Spaced Repetition Tracker

| Day | 1 | 3 | 7 | 15 | 30 |
|-----|---|---|---|----|----|
| FIB-4 Formula & Cut-offs | ☐ | ☐ | ☐ | ☐ | ☐ |
| FibroScan LSM F0-F4 | ☐ | ☐ | ☐ | ☐ | ☐ |
| CAP Cut-offs | ☐ | ☐ | ☐ | ☐ | ☐ |
| Biopsy Indications | ☐ | ☐ | ☐ | ☐ | ☐ |
| METAVIR Stages | ☐ | ☐ | ☐ | ☐ | ☐ |

---

## Self-Test Scorecard

| Question | My Answer | Correct? |
|----------|-----------|----------|
| FIB-4 Formula |  |  |
| FibroScan F4 Cut-off |  |  |
| XL Probe Indication |  |  |
| Biopsy Contraindications |  |  |
| NAS ≥5 = ? |  |  |

---

## Local Navigation

- [[Chronic Liver Disease and Cirrhosis/Definition and classification|Definition & Classification]]
- [[Chronic Liver Disease and Cirrhosis/Compensated vs decompensated cirrhosis|Compensated vs Decompensated]]
- [[Chronic Liver Disease and Cirrhosis/Child-Pugh and MELD scores|Child-Pugh & MELD]]
- [[Chronic Liver Disease and Cirrhosis/Aetiology|Aetiology]]
- [[Portal Hypertension and Complications/Ascites|Ascites]]
- [[Liver Transplantation/Liver Transplantation|Liver Transplant]]