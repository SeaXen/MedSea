## 1. Learning Objectives
- [ ] Apply non-invasive fibrosis scores (FIB-4, NFS, APRI, ELF, FibroScan)
- [ ] Interpret FibroScan (VCTE) results with CAP and LSM
- [ ] Know indications and contraindications for liver biopsy
- [ ] Apply diagnostic algorithms for NAFLD/NASH diagnosis
- [ ] Identify FCPS/MRCP high-yield diagnostic thresholds

---

## 2. Diagnostic Approach

```mermaid
flowchart TD
    A[Suspect NAFLD: Metabolic Risk Factors + Steatosis on US] --> B[Exclude Alcohol & Secondary Causes]
    B --> C[Calculate FIB-4 / NFS / APRI]
    C --> D{Fibrosis Risk?}
    D -->|Low| E[Monitor: LFTs, US Annually]
    D -->|Intermediate| F[FibroScan (VCTE) / ELF]
    D -->|High| G[Consider Liver Biopsy / Referral]
    F --> H{FibroScan/ELF}
    H -->|Low Risk| I[Monitor]
    H -->|Intermediate| J[Consider Biopsy / Referral]
    H -->|High Risk| K[Consider Biopsy / Referral]
```

---

## 3. Non-Invasive Fibrosis Scores

### 1. FIB-4 (First-Line, Cheap, Widely Available)

```
FIB-4 = (Age × AST) / (Platelets × √ALT)
```

| Cut-off | Interpretation |
|---------|----------------|
| **<1.30** | **Low Risk** Advanced Fibrosis (NPV >90%) |
| **1.30-2.67** | **Indeterminate** — Need Further Testing |
| **>2.67** | **High Risk** Advanced Fibrosis (PPV ~65%) |

> **Age-Adjusted**: For >65y use **<2.0 / >3.0**; For <35y use **<1.45 / >3.0**

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

> **FibroScan Limitations**: Obesity (XL Probe), Ascites, Acute Inflammation, Biliary Obstruction

---

## 4. FibroScan Probe Selection

| Probe | Indication |
|-------|------------|
| **M Probe (Standard)** | BMI <30, Skin-Capsule Distance <25mm |
| **XL Probe** | **BMI ≥30**, Skin-Capsule Distance ≥25mm |

> **Failure Rate**: M Probe 10-15% in Obese; XL Probe Reduces Failure to <5%

---

## 5. Diagnostic Algorithm (EASL 2024 / AASLD 2023)

```mermaid
flowchart TD
    A[Suspect NAFLD: Metabolic Risk Factors + Steatosis on US] --> B[Calculate FIB-4]
    B --> C{FIB-4}
    C -->|<1.30| D[Low Risk: Monitor Annually]
    C -->|1.30-2.67| E[FibroScan (VCTE)]
    C -->|>2.67| F[High Risk: Refer / Consider Biopsy]
    E --> G{FibroScan LSM}
    G -->|<8 kPa| H[Low Risk: Monitor]
    G -->|8-12 kPa| I[Significant Fibrosis: Referral]
    G -->|>12 kPa| J[**Cirrhosis Likely**]
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

## 7. Histological Scoring (NASH CRN)

| Component | Score |

*...continued (truncated for renderer performance)*