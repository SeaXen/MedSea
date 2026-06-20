## 1. Learning Objectives
- [ ] Apply non-invasive fibrosis scores (FIB-4, NFS, APRI, ELF, FibroScan)
- [ ] Interpret FibroScan (VCTE) results with CAP and LSM
- [ ] Know indications and contraindications for liver biopsy
- [ ] Apply diagnostic algorithms for cirrhosis diagnosis
- [ ] Identify FCPS/MRCP high-yield diagnostic thresholds

---

## 2. Diagnostic Approach

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

## 3. Non-Invasive Fibrosis Scores

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

## 4. FibroScan Probe Selection
| Probe | Indication |
|-------|------------|
| **M Probe (Standard)** | BMI <30, Skin-Capsule Distance <25mm |
| **XL Probe** | **BMI ≥30**, Skin-Capsule Distance ≥25mm |

> **Failure Rate**: M Probe 10-15% in Obese; XL Probe Reduces Failure to <5%

---

## 5. Diagnostic Algorithm

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

## 6. Liver Biopsy Indications

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

## 7. Histological Staging Systems

### METAVIR (Most Common)
| Stage | Description |
|-------|-------------|
| **F0** | No Fibrosis |
| **F1** | Portal Fibrosis Without Septa |
| **F2** | Portal Fibrosis With Rare Septa |
| **F3** | Numerous Septa Without Cirrhosis |

*...continued (truncated for renderer performance)*