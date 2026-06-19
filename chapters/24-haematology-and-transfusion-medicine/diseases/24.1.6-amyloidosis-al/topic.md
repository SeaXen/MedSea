---
tags: [medicine, davidson, hematology, amyloidosis, al-amyloidosis, plasma-cell-disorder, fcps, mrcp]
davidson_chapter: Chapter 25: Haematology and Transfusion Medicine
status: full-fcps-mrcp-note
priority: high
exam_relevance: "FCPS: Essential | MRCP: Core | Congo red +ve, FLC elevation, cardiac/kidney/liver/nerve involvement, chemo (CyBorD/Dara-CyBorD), SCT, organ-specific management"
see_also: "[[Multiple Myeloma]], [[MGUS]], [[Waldenström Macroglobulinaemia]], [[POEMS Syndrome]]"
created: 2025-06-16
modified: 2025-06-16
---

# AL Amyloidosis (Primary Amyloidosis)

> [!info] **Davidson Ch 25 Alignment**: Haematological Malignancies → Plasma Cell Disorders → AL Amyloidosis
> **FCPS/MRCP Focus**: Congo red +ve with apple-green birefringence, FLC elevation, organ involvement (heart, kidney, liver, nerve), CyBorD/Dara-CyBorD, SCT eligibility, organ-specific management

---

## 🎯 Learning Objectives

- [ ] Define AL Amyloidosis: **Misfolded light chain (κ/λ) deposition** as amyloid fibrils → **organ dysfunction**
- [ ] Diagnose: **Congo red +ve with apple-green birefringence** (gold standard), **Mass spectrometry** for typing (AL vs ATTR), **FLC elevation** (involved > uninvolved)
- [ ] Apply **Mayo Stage** (2012/2014): **NT-proBNP, Troponin, FLC difference (dFLC)** → Stage I-IV
- [ ] Manage **Plasma Cell Clone**: **CyBorD** (Cyclophosphamide, Bortezomib, Dexamethasone) or **Dara-CyBorD** (ANDROMEDA trial)
- [ ] Assess **SCT Eligibility**: **Stage I-II, Age <70, No severe cardiac involvement** → **Mel 200 + Auto-SCT**
- [ ] Manage **Organ-Specific Complications**: Heart failure (diuretics, NO ACEi/BB initially), Nephrotic syndrome, Autonomic neuropathy, GI dysmotility
- [ ] Monitor **Response**: **FLC difference (dFLC)** – **CR = dFLC <10 mg/L + normal FLC ratio**

---

## 📖 Definition & Pathophysiology

```mermaid
flowchart TD
    A[Clonal Plasma Cell Disorder] --> B[Production of Monoclonal Light Chains (κ/λ)]
    B --> C[Misfolding → β-pleated Sheet Structure]
    C --> D[Amyloid Fibril Formation]
    D --> E[Tissue Deposition → Organ Dysfunction]
    E --> F1[Heart: Restrictive Cardiomyopathy]
    E --> F2[Kidney: Nephrotic Syndrome → ESRD]
    E --> F3[Liver: Hepatomegaly, Cholestasis]
    E --> F4[Nerve: Peripheral + Autonomic Neuropathy]
    E --> F5[GI: Malabsorption, Pseudo-obstruction, Bleeding]
    E --> F6[Soft Tissue: Macroglossia, Periorbital Purpura, Carpal Tunnel]
```

| Feature | AL Amyloidosis | ATTR (Transthyretin) |
|---------|----------------|----------------------|
| **Precursor** | **Immunoglobulin Light Chain (κ/λ)** | Transthyretin (Wild-type or Mutant) |
| **Plasma Cell Clone** | **Present** (often low burden) | Absent |
| **FLC** | **Elevated (Involved > Uninvolved)** | Normal |
| **Mass Spec Typing** | **AL** | **ATTR** |
| **Cardiac Uptake (PYP/DPD Scan)** | Negative | **Positive (Grade 2-3)** |
| **Treatment** | **Chemo + Anti-plasma cell** | **Tafamidis, RNAi, CRISPR** |

> [!tip] **FCPS/MRCP**: **AL Amyloid = Congo red +ve + apple-green birefringence + AL typing**. **FLC involved > uninvolved**. **Mayo Stage = NT-proBNP + Troponin + dFLC**. **CyBorD / Dara-CyBorD**. **SCT for Stage I-II**. **NO ACEi/BB initially in cardiac AL**.

---

## 🔬 Diagnostic Workup

```mermaid
flowchart TD
    A[Suspected Amyloidosis: Nephrotic + Cardiomyopathy + Neuropathy] --> B[**Serum/Urinary FLC**]
    B --> C{**dFLC Elevated?** (Involved - Uninvolved)}
    C -->|Yes| D[**Tissue Biopsy**]
    D --> E[**Congo Red Stain + Apple-Green Birefringence**]
    E -->|Positive| F[**Mass Spectrometry / Immunohistochemistry**]
    F -->|AL| G[**Bone Marrow: BMPC%, Flow, Cytogenetics**]
    F -->|ATTR| H[**PYP/DPD Scan + TTR Genetic Test**]
    G --> I[**Organ Assessment**]
    I --> J1[**Heart: Echo, NT-proBNP, Troponin, CMR (Late Gadolinium Enhancement)**]
    I --> J2[**Kidney: UACR, eGFR, Proteinuria**]
    I --> J3[**Liver: LFT, Imaging**]
    I --> J4[**Nerve: NCS, Autonomic Testing**]
    I --> J5[**GI: Endoscopy, Biopsy**]
    J1 & J2 & J3 & J4 & J5 --> K[**Mayo Staging**]
```

### Essential Investigations

| Test | Purpose |
|------|---------|
| **sFLC (κ/λ)** | **dFLC = Involved - Uninvolved**; **Involved/Uninvolved Ratio** |
| **Congo Red + Polarised Light** | **Gold Standard**: Apple-green birefringence |
| **Mass Spectrometry (Proteomics)** | **Definitive Typing**: AL vs ATTR vs AA vs others |
| **Bone Marrow** | BMPC% (usually <10%), Flow, Cytogenetics (t(11;14) common) |
| **NT-proBNP, Troponin** | **Mayo Staging** + Baseline cardiac function |
| **CMR (Cardiac MRI)** | **Late Gadolinium Enhancement (LGE)** – diffuse subendocardial = AL amyloid |
| **PYP/DPD Scan (Bone Scintigraphy)** | **ATTR: Positive (Grade 2-3)**; **AL: Negative** |
| **SAP Scintigraphy** | Whole-body amyloid load (UK) |

---

## 🩺 Organ Involvement & Clinical Features

| Organ | Manifestations | Key Findings |
|-------|----------------|--------------|
| **Heart** | **Restrictive Cardiomyopathy**: HFpEF, ↑ LV wall thickness, **Low voltage ECG**, **Pseudo-infarct pattern**, Arrhythmias | **Echo**: Thickened walls, **Sparkling appearance**, **Diastolic dysfunction**, **Preserved EF**; **CMR: LGE**; **PYP Scan: Negative** |
| **Kidney** | **Nephrotic Syndrome**: Proteinuria >3.5g/d, Hypoalbuminaemia, Oedema; **Renal failure** | **Proteinuria >3.5g**, **eGFR decline**; **Biopsy: Congo red +ve glomeruli/vessels** |
| **Liver** | Hepatomegaly, **Cholestasis** (↑ ALP, GGT), Portal hypertension, Ascites | **Hepatomegaly**, ↑ ALP/GGT, Normal transaminases |
| **Nerve** | **Peripheral Neuropathy** (length-dependent, painful), **Autonomic Neuropathy** (orthostatic hypotension, GI dysmotility, ED) | **NCS: Axonal sensory-motor**; **Autonomic: HRV, Tilt table** |
| **GI** | Macroglossia, **GI bleeding** (angiodysplasia/amyloid), **Pseudo-obstruction**, Malabsorption, Diarrhoea | **Macroglossia** (specific); **Endoscopy: Amyloid deposits** |
| **Soft Tissue** | **Periorbital purpura** (racoon eyes), **Macroglossia**, **Carpal tunnel**, **Shoulder pad sign** | **Periorbital purpura** (pinch purpura), **Macroglossia** |

> [!warning] **Cardiac AL Amyloid: AVOID ACEi/ARB/Beta-blockers INITIALLY** – can cause severe hypotension (autonomic dysfunction + fixed stroke volume). **Loop diuretics mainstay**.

---

## 📊 Mayo Staging (2012/2014)

| Stage | Criteria | Median OS |
|-------|----------|-----------|
| **I** | **NT-proBNP <1800, Troponin <0.025, dFLC <180** | ~94 months |
| **II** | **1 abnormal** | ~40 months |
| **III** | **2 abnormal** | ~14 months |
| **IV** (2014) | **3 abnormal** (NT-proBNP ≥1800, Troponin ≥0.025, dFLC ≥180) | ~6 months |

> [!tip] **dFLC = Involved FLC - Uninvolved FLC** (mg/L). **Mayo 2014 added Stage IV** for highest risk.

---

## 💊 Management

### Plasma Cell-Directed Therapy

| Regimen | Indication | Key Points |
|---------|------------|------------|
| **CyBorD** | **Standard first-line** | Cyclophosphamide 300mg/m² d1,8,15 + Bortezomib 1.3mg/m² d1,4,8,11 + Dex 40mg d1,2,8,9,15,16 (21d cycle) |
| **Dara-CyBorD** | **Preferred first-line (ANDROMEDA)** | **Daratumumab 1800mg SC** + CyBorD → **~90% haematological CR**, **~50% cardiac response** |
| **Bortezomib + Dex** | If cyclophosphamide contraindicated | Bortezomib 1.3mg/m² d1,4,8,11 + Dex 20-40mg |
| **Venetoclax** | **t(11;14) positive** (BCL-2 dependent) | Venetoclax + Dex ± Bortezomib |

### Autologous SCT

| Eligibility | Criteria |
|-------------|----------|
| **Mayo Stage I-II** | No Stage III/IV |
| **Age** | **<70 years** (physiologic age) |
| **Cardiac Function** | **NYHA I-II**, EF >40%, **Troponin <0.06**, **NT-proBNP <5000** |
| **Performance Status** | ECOG 0-1 |
| **Renal** | eGFR >30 (or on dialysis) |

**Conditioning**: **Melphalan 200 mg/m² (Mel 200)** or **Mel 140** if renal/age risk

### Organ-Specific Supportive Care

| Organ | Management |
|-------|------------|
| **Heart** | **Loop diuretics** (Furosemide ± Spironolactone); **AVOID ACEi/ARB/BB initially**; **Digoxin** caution (binds amyloid); **Pacemaker** for conduction disease; **Heart transplant** (rare, with SCT) |
| **Kidney** | **ACEi/ARB** (if tolerated) for proteinuria; **Dialysis** if ESRD; **Renal transplant** (with SCT) |
| **Nerve** | **Gabapentin/Pregabalin/Duloxetine** for neuropathic pain; **Midodrine/Fludrocortisone** for orthostatic hypotension; **Pyridostigmine** for GI dysmotility |
| **GI** | **Small frequent meals**, **Prokinetics** (Metoclopramide, Domperidone), **Octreotide** for diarrhoea |
| **Bleeding** | **Factor X deficiency** (amyloid binds FX) – **FFP/PCC** for procedures; **Tranexamic acid** |

---

## 🔄 Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **ATTR Amyloidosis** | **PYP Scan Positive**, **TTR Genetic Test**, **Normal FLC**, **No plasma cell clone** |
| **AA Amyloidosis** | **Chronic Inflammation** (RA, IBD, FMF), **SAA Protein** precursor, **Kidney dominant**, **Treat underlying inflammation** |
| **Multiple Myeloma** | **CRAB/SLiM Present**, **BMPC ≥10%**, **Higher BM burden** |
| **MGUS** | **No Organ Damage**, **Lower FLC**, **No Amyloid Deposits** |
| **Hypertrophic Cardiomyopathy** | **Genetic (Sarcomere)**, **No Systemic Amyloid**, **Normal FLC/NT-proBNP pattern** |
| **Diabetic Nephropathy** | **Diabetes History**, **Retinopathy**, **No Cardiac Amyloid** |

---

## 💡 FCPS/MRCP High-Yield Summary

| Topic | Key Point |
|-------|-----------|
| **Diagnosis** | **Congo Red + Apple-green birefringence + Mass Spec (AL)** |
| **FLC** | **dFLC = Involved - Uninvolved**; **Involved/Uninvolved Ratio** |
| **Cardiac** | **Low voltage ECG**, **Thickened walls**, **Sparkling Echo**, **LGE on CMR**, **PYP Scan Negative** |
| **Mayo Stage** | **NT-proBNP, Troponin, dFLC** → Stage I-IV → Prognosis |
| **First-line** | **Dara-CyBorD** (ANDROMEDA: ~90% CR, ~50% cardiac response) |
| **SCT** | **Stage I-II, Age <70, No Severe Cardiac** → Mel 200 |
| **Cardiac Management** | **Loop Diuretics**; **AVOID ACEi/ARB/BB Initially** |
| **Renal** | **Nephrotic Syndrome**; **Congo Red +ve on Biopsy** |
| **Monitoring** | **dFLC** (CR = dFLC <10 + normal ratio); **NT-proBNP, Troponin** |
| **t(11;14)** | **~40-50% AL Amyloid** → **Venetoclax Sensitive** |

---

## ❓ Viva Questions

1. **What is the gold standard for diagnosing AL Amyloidosis?**
   - **Tissue biopsy with Congo Red stain showing apple-green birefringence under polarised light + Mass Spectrometry confirming AL type**

2. **How is the diagnosis of AL Amyloidosis confirmed and typed?**
   - **Congo Red + Mass Spectrometry (Proteomics)** – definitive for AL vs ATTR vs AA

3. **What are the Mayo Staging criteria for AL Amyloidosis?**
   - **NT-proBNP ≥1800, Troponin ≥0.025, dFLC ≥180** → 0 factors = Stage I, 1 = II, 2 = III, 3 = IV

4. **What is dFLC and how is it used in monitoring?**
   - **dFLC = Involved FLC - Uninvolved FLC**; **CR = dFLC <10 mg/L + normal FLC ratio**; **PR = dFLC ↓ >50%**

4. **What is the first-line treatment for AL Amyloidosis?**
   - **CyBorD** or **Dara-CyBorD** (ANDROMEDA trial: superior response rates)

5. **When is autologous SCT considered in AL Amyloidosis?**
   - **Mayo Stage I-II**, **Age <70**, **No severe cardiac involvement** (NYHA I-II, Troponin <0.06, NT-proBNP <5000)

6. **Why are ACE inhibitors and Beta-blockers avoided initially in cardiac AL Amyloidosis?**
   - **Autonomic dysfunction + fixed stroke volume** → **Severe hypotension**; **Diuretics first-line**

7. **What is the PYP/DPD scan used for in amyloidosis?**
   - **ATTR: Positive (Grade 2-3)**; **AL: Negative** – differentiates ATTR from AL

8. **How does t(11;14) affect treatment in AL Amyloidosis?**
   - **~40-50% have t(11;14)** → **BCL-2 dependent** → **Venetoclax effective** (add to Bortezomib/Dex)

9. **What is the difference between AL and ATTR Amyloidosis on PYP scan?**
   - **AL: Negative**; **ATTR: Positive (Grade 2-3)** – "Grade 2-3 uptake = ATTR"

10. **How do you monitor response to treatment in AL Amyloidosis?**
    - **dFLC (difference between Involved and Uninvolved FLC)**; **CR = dFLC <10 + normal ratio**; **NT-proBNP, Troponin for cardiac response**

---

## 🧠 Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **AL vs ATTR** | **AL: FLC Elevated, PYP Negative, Plasma Cell Clone**; **ATTR: Normal FLC, PYP Positive, TTR Gene** |
| **AL vs Myeloma** | **Myeloma = CRAB/SLiM + BMPC ≥10%**; **AL = Organ Amyloid, BMPC usually <10%** |
| **Cardiac Meds in AL** | **AVOID ACEi/ARB/BB Initially** (hypotension); **Diuretics First** |
| **dFLC Calculation** | **Involved FLC - Uninvolved FLC** (not ratio) |
| **PYP Scan** | **Positive = ATTR**; **Negative = AL** |

| Mnemonic | Meaning |
|----------|---------|
| **"Congo Red = Green Apple = Amyloid"** | Diagnostic stain |
| **"AL = Light Chain = FLC Elevation"** | Precursor |
| **"Mayo = NT-proBNP + Trop + dFLC"** | Staging criteria |
| **"Dara-CyBorD = 90% CR"** | First-line |
| **"Cardiac AL = Diuretics Only"** | Avoid ACEi/BB |
| **"PYP Positive = ATTR"** | Scan interpretation |
| **"t(11;14) = Venetoclax"** | Targeted therapy |

---

## 🗺️ Mind Map

```mermaid
mindmap
  root((AL Amyloidosis))
    Diagnosis
      Congo Red + Apple-Green
      Mass Spec = AL
      FLC: dFLC Elevated
    Organ Involvement
      Heart: Restrictive CM, Low Voltage, LGE, PYP -
      Kidney: Nephrotic Syndrome
      Nerve: Peripheral + Autonomic
      GI: Macroglossia, Bleeding, Pseudo-obstruction
      Liver: Hepatomegaly, Cholestasis
    Staging (Mayo)
      NT-proBNP, Troponin, dFLC
      Stage I-IV
    Treatment
      Dara-CyBorD (1st Line)
      CyBorD (Alternative)
      Venetoclax (t(11;14))
      SCT: Stage I-II, <70, No Severe Cardiac
    Cardiac Management
      Loop Diuretics
      NO ACEi/ARB/BB Initially
    Monitoring
      dFLC (CR <10 + Normal Ratio)
      NT-proBNP, Troponin
```

---

## 📋 One-Page Revision Card

| **AL AMYLOIDOSIS – FCPS/MRCP REVISION CARD** |
|-----------------------------------------------|
| **Diagnosis**: **Congo Red + Apple-Green + Mass Spec (AL)** |
| **FLC**: **dFLC = Involved - Uninvolved**; **Involved FLC ↑** |
| **Heart**: Restrictive CM, **Low Voltage**, **Sparkling Echo**, **LGE on CMR**, **PYP Negative** |
| **Mayo Stage**: NT-proBNP ≥1800, Trop ≥0.025, dFLC ≥180 |
| **1st Line**: **Dara-CyBorD** (ANDROMEDA) or **CyBorD** |
| **SCT**: **Stage I-II, <70yr, No Severe Cardiac** (Mel 200) |
| **Cardiac Rx**: **Loop Diuretics; NO ACEi/ARB/BB Initially** |
| **Renal**: Nephrotic Syndrome; Congo Red +ve Biopsy |
| **Monitor**: **dFLC (CR <10 + Normal Ratio)**, NT-proBNP, Troponin |
| **t(11;14)**: ~40-50% → **Venetoclax Sensitive** |
| **PYP Scan**: **Negative = AL; Positive (Gr 2-3) = ATTR** |

---

## 📅 Spaced Repetition Tracker

| Review | Date | Score (1-5) | Next Review |
|--------|------|-------------|-------------|
| Day 1 | 2025-06-16 | | 2025-06-17 |
| Day 3 | | | |
| Day 7 | | | |
| Day 15 | | | |
| Day 30 | | | |

---

## 🎯 Must Know / Should Know / Nice to Know

| Level | Content |
|-------|---------|
| **Must Know** | Congo red + apple-green + mass spec, dFLC concept, cardiac features (low voltage, LGE, PYP neg), Mayo staging, Dara-CyBorD first-line, SCT eligibility, avoid ACEi/BB in cardiac AL, dFLC monitoring, PYP scan negative, t(11;14) → venetoclax |
| **Should Know** | ANDROMEDA trial details, CyBorD dosing, venetoclax in t(11;14), organ-specific supportive care (autonomic neuropathy, GI, bleeding), Factor X deficiency, renal transplant considerations, cardiac transplant with SCT, SAP scintigraphy, AA amyloidosis differentiation, ATTR (wt/mutant), tafamidis/diflunisal for ATTR |
| **Nice to Know** | Amyloid fibril structure, SAP scintigraphy methodology, PRISM trial (dara-cybor-dara maintenance), CAEL-101 (anti-amyloid antibody), NEOD001 (failed), gene expression profiling, amyloid clearance mechanisms, cardiac PET imaging, cost-effectiveness of Dara-CyBorD, paediatric amyloidosis, hereditary amyloidoses other than ATTR |

---

## ✅ Self-Test Scorecard

| Section | Score (0-10) | Notes |
|---------|--------------|-------|
| Diagnosis & Typing | | |
| Organ Involvement & Cardiac Features | | |
| Mayo Staging | | |
| Treatment (Dara-CyBorD, SCT) | | |
| Cardiac & Organ Management | | |
| Monitoring (dFLC) | | |
| Viva Questions | | |

---

## 🔗 Local Navigation

- **Previous**: [[MGUS]]
- **Next**: [[Waldenström Macroglobulinaemia]]
- **Section Hub**: [[Haematological Malignancies]]
- **MOC**: [[Hematology MOC]]
- **Template**: [[../Templates/Hematology Topic Template]]

---

*Generated for FCPS/MRCP exam preparation. Based on Davidson Medicine 24th Ed Chapter 25.*