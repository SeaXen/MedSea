---
tags: [medicine, davidson, hematology, pnh, paroxysmal-nocturnal-haemoglobinuria, haemolytic-anaemia, fcps, mrcp]
davidson_chapter: Chapter 25: Haematology and Transfusion Medicine
status: full-fcps-mrcp-note
priority: high
exam_relevance: "FCPS: Essential | MRCP: Core | PIGA mutation, flow CD55/CD59, thrombosis, eculizumab, ravulizumab, bone marrow failure overlap"
see_also: "[[Haemolytic Anaemias]], [[Aplastic Anaemia]], [[TTP/HUS]], [[Eculizumab]], [[Thrombosis in PNH]]"
created: 2025-06-16
modified: 2025-06-16
---

# Paroxysmal Nocturnal Haemoglobinuria (PNH)

> [!info] **Davidson Ch 25 Alignment**: Haemolytic Anaemias → Paroxysmal Nocturnal Haemoglobinuria
> **FCPS/MRCP Focus**: PIGA mutation, GPI anchor deficiency, flow CD55/CD59, intravascular haemolysis, thrombosis, eculizumab/ravulizumab

---

## 🎯 Learning Objectives

- [ ] Define PNH: **Acquired somatic PIGA mutation** → **GPI anchor deficiency** → loss of CD55 (DAF) & CD59 (MIRL) → complement-mediated intravascular haemolysis
- [ ] Classify: **Classic PNH**, **PNH in setting of AA/MDS** (bone marrow failure), **Subclinical PNH** (small clone)
- [ ] Diagnose: **Flow cytometry (CD55/CD59 on granulocytes, monocytes, RBCs)** – gold standard; **Ham test / sucrose lysis (historical)**
- [ ] Manage **haemolysis**: **Eculizumab / Ravulizumab** (anti-C5); folic acid; iron management
- [ ] Manage **thrombosis**: **Anticoagulation** (DOAC/warfarin); **C5 inhibitor reduces risk**
- [ ] Monitor: **Clone size (%), LDH, Hb, reticulocytes, renal function, thrombosis surveillance**
- [ ] Understand **bone marrow failure overlap**: AA → PNH clone evolution; PNH → AA/MDS

---

## 📖 Definition & Classification

| Category | Clone Size | Clinical Picture |
|----------|------------|------------------|
| **Classic PNH** | Large (>50% granulocytes) | **Intravascular haemolysis**, haemoglobinuria, thrombosis, cytopenias |
| **PNH-AA/MDS** | Variable | **Bone marrow failure** dominant; PNH clone detected incidentally |
| **Subclinical PNH** | Small (<10-20%) | Asymptomatic; detected on screening (AA workup) |

> [!tip] **FCPS/MRCP**: **PNH = Acquired PIGA mutation on chr X** → **GPI anchor defect** → **CD55 (DAF) & CD59 (MIRL) loss** → **Uncontrolled complement activation** → **Intravascular haemolysis + Thrombosis**.

---

## ⚙️ Pathophysiology

```mermaid
flowchart TD
    A[Somatic PIGA Mutation (Xp22)] --> B[Defective GPI Anchor Synthesis]
    B --> C[Loss of GPI-Anchored Proteins on Cell Surface]
    C --> D1[**CD55 (DAF) Loss** → No Decay Acceleration of C3 Convertase]
    C --> D2[**CD59 (MIRL) Loss** → No Inhibition of MAC (C5b-9) Formation]
    D1 & D2 --> E[Uncontrolled Alternative Complement Pathway]
    E --> F1[**C3b Deposition on RBCs** → Opsonisation → Extravascular Haemolysis (Spleen)]
    E --> F2[**MAC (C5b-9) Formation** → **Intravascular Haemolysis**]
    F1 --> G[Haemoglobinuria, Haemosiderinuria]
    F2 --> H[Free Hb → NO Scavenging → **Thrombosis, Dysphagia, Erectile Dysfunction**]
    G & H --> I[Renal Tubular Damage (Haemosiderinuria), Pulm HTN]
```

---

## 🔬 Diagnostic Workup

```mermaid
flowchart TD
    A[Intravascular Haemolysis + Thrombosis + Cytopenias] --> B[CBC + Film]
    B --> C{Schistocytes? No. Spherocytes? No.}
    C --> D[Haemolysis Markers: **LDH↑↑, Haptoglobin↓, Hb↑, Retic↑, Bilirubin↑**]
    D --> E[**Flow Cytometry: CD55/CD59 on Granulocytes/Monocytes/RBCs**]
    E --> F{**GPI-Deficient Clone Detected**}
    F -->|Yes| G[**Diagnosis: PNH**]
    F -->|No| H[Consider Other Haemolytic Anaemias]
    G --> I[**Clone Size %** (Type II = partial, Type III = complete loss)]
    G --> J[**Bone Marrow** (if cytopenias: rule out AA/MDS)]
    G --> K[**PIGA Mutation Sequencing** (confirmatory)]
    G --> L[Thrombophilia Screen, Renal Function, Pulm Echo]
```

### Key Diagnostic Findings

| Test | PNH Finding |
|------|-------------|
| **Flow Cytometry (Gold Standard)** | **CD55 (DAF) & CD59 (MIRL) ABSENT/DECREASED** on granulocytes, monocytes, RBCs |
| **Clone Classification** | **Type I (Normal)**, **Type II (Partial loss, 10-70%)**, **Type III (Complete loss, <10% normal)** |
| **Granulocyte Clone** | **Most stable** (lifespan days); preferred for monitoring |
| **RBC Clone** | Underestimates (haemolysed); Type III lost fastest |
| **Ham Test / Sucrose Lysis** | Historical (positive in PNH); replaced by flow |
| **PIGA Sequencing** | Confirms somatic mutation |
| **FLAER (Fluorescent AER)** | **High sensitivity** for GPI deficiency (binds GPI anchor directly) |

---

## 🩺 Clinical Features

| Manifestation | Mechanism | Frequency |
|---------------|-----------|-----------|
| **Intravascular Haemolysis** | MAC lysis | **Classic** (nocturnal due to relative acidosis during sleep) |
| **Haemoglobinuria** | Free Hb exceeds haptoglobin | Dark urine (morning) |
| **Thrombosis** | **Platelet activation + NO scavenging + MP release** | **40-50% lifetime risk**; **Budd-Chiari (hepatic vein), cerebral sinus, abdominal veins** |
| **Cytopenias** | BM failure overlap | Anaemia, neutropenia, thrombocytopenia |
| **Dysphagia** | NO scavenging → oesophageal spasm | Characteristic |
| **Erectile Dysfunction** | NO scavenging | Common |
| **Renal Impairment** | Haemosiderinuria, tubular damage | Chronic |
| **Pulmonary Hypertension** | NO scavenging, chronic haemolysis | Late complication |

---

## 💊 Management

### Complement Inhibition (C5 Inhibitors) – **Standard of Care**

| Drug | Dose | Schedule | Key Points |
|------|------|----------|------------|
| **Eculizumab** | 600 mg weekly × 4 → 900 mg weekly × 1 → **900 mg q2wk** | IV | **Meningococcal vaccine REQUIRED 2wks before**; Penicillin prophylaxis; **Reduces haemolysis, thrombosis, improves survival** |
| **Ravulizumab** | **Weight-based LD → q8wk maintenance** | IV | **Longer half-life (q8wk)**; Same meningococcal prophylaxis; **Preferred for adherence** |
| **Pegcetacoplan (C3 inhibitor)** | **Subcutaneous q2wk** | SC | **Newer**; Controls both intravascular & extravascular haemolysis; **ASPIRE trial** |

> [!tip] **FCPS/MRCP**: **Eculizumab/Ravulizumab = Anti-C5 monoclonal antibodies**. **Meningococcal vaccination (MenACWY + MenB) MANDATORY 2 weeks before first dose**. **Penicillin prophylaxis during treatment**.

### Supportive Care

| Measure | Details |
|---------|---------|
| **Folic Acid** | 5 mg daily (increased erythropoiesis) |
| **Iron Management** | **Oral iron** if deficient (chronic Hb loss); **IV iron** if non-compliant/malabsorption; Monitor ferritin |
| **Anticoagulation** | **DOAC preferred** (apixaban/rivaroxaban); Target INR 2-3 if warfarin; **Consider prophylactic in large clones** |
| **Transfusion** | If symptomatic anaemia; **Leucodepleted, irradiated**; Avoid in haemolysis flare if possible |
| **Renal Protection** | Hydration, alkalinisation during haemolytic crisis |

### Bone Marrow Failure Overlap (PNH-AA/MDS)

| Scenario | Management |
|----------|------------|
| **AA with PNH clone** | **IST (ATC + CsA)** if SAA/VSAA; **HSCT** if young/fit |
| **PNH → AA/MDS evolution** | Monitor BM annually; treat per AA/MDS guidelines |
| **Allogeneic HSCT** | **Curative for both PNH + BM failure**; Indicated in AA/MDS with PNH clone if fit |

---

## ⚠️ Thrombosis in PNH

| Feature | Details |
|---------|---------|
| **Risk** | 40-50% lifetime (untreated); **Highest in first 1-2 years** |
| **Sites** | **Budd-Chiari (hepatic vein)**, **Cerebral venous sinus**, **Portal/splanchnic**, DVT/PE, Dermal necrosis |
| **Prophylaxis** | **Anticoagulation if large clone (>50%) or prior thrombosis**; **C5 inhibitor reduces risk by >90%** |
| **Treatment** | **Full anticoagulation**; **C5 inhibitor**; **Thrombolysis** for acute venous thrombosis |

---

## 🔄 Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **AIHA** | **DAT POSITIVE**, extravascular, spherocytes |
| **TTP/HUS** | **Schistocytes, Thrombocytopenia, ADAMTS13<10%**, normal flow |
| **DIC** | **PT/APTT↑, Fibrinogen↓, D-dimer↑, Schistocytes** |
| **March Haemoglobinuria** | **Traumatic** (running, marching); transient, no clone |
| **Paroxysmal Cold Haemoglobinuria** | **Donath-Landsteiner +**, post-viral, self-limiting |
| **AA with PNH clone** | **Hypocellular marrow**, PNH clone incidental |

---

## 💡 FCPS/MRCP High-Yield Summary

| Topic | Key Point |
|-------|-----------|
| **Mutation** | **Somatic PIGA (Xp22)** → GPI anchor defect |
| **Key Defect** | **Loss of CD55 (DAF) & CD59 (MIRL)** → uncontrolled complement |
| **Diagnosis** | **Flow cytometry CD55/CD59 (granulocytes best)**; **FLAER** |
| **Haemolysis** | **Intravascular** → haemoglobinuria (nocturnal), haemosiderinuria |
| **Thrombosis** | **40-50% risk**; Budd-Chiari, cerebral sinus, splanchnic veins |
| **Treatment** | **Eculizumab (q2wk IV) / Ravulizumab (q8wk IV) / Pegcetacoplan (q2wk SC)** |
| **Vaccination** | **MenACWY + MenB 2 WEEKS BEFORE** starting C5 inhibitor |
| **Prophylaxis** | **Penicillin** during C5 inhibitor therapy |
| **Folic Acid** | 5 mg daily |
| **Iron** | Chronicloss → iron deficiency → replace |
| **BM Failure Overlap** | PNH clone in AA/MDS; IST/HSCT per BM failure guidelines |

---

## ❓ Viva Questions

1. **What is the molecular defect in PNH?**
   - **Somatic PIGA mutation (Xp22)** → defective GPI anchor synthesis → loss of CD55 (DAF) & CD59 (MIRL)

2. **Which flow cytometry markers are used to diagnose PNH?**
   - **CD55 (DAF) and CD59 (MIRL)** on granulocytes, monocytes, RBCs; **FLAER** (high sensitivity)

3. **Why is haemolysis intravascular in PNH?**
   - **CD59 (MIRL) loss** → uncontrolled **MAC (C5b-9) formation** → direct RBC lysis

4. **What is the classic thrombosis site in PNH?**
   - **Budd-Chiari syndrome (hepatic vein thrombosis)**, cerebral venous sinus, splanchnic veins

5. **How does eculizumab work and what is the mandatory pre-treatment requirement?**
   - **Anti-C5 monoclonal antibody** prevents MAC formation; **Meningococcal vaccine (MenACWY + MenB) 2 weeks before**

6. **Differentiate Type II and Type III PNH cells.**
   - **Type II: Partial CD55/CD59 loss**; **Type III: Complete loss** (most susceptible to lysis)

7. **Why is granulocyte clone size preferred for monitoring?**
   - **Granulocytes have short lifespan (days)**, not lysed by complement; RBC clone underestimates

8. **What is the role of anticoagulation in PNH?**
   - **Prophylactic if large clone (>50%)**; **Therapeutic for thrombosis**; **DOAC preferred**

9. **How does PNH overlap with Aplastic Anaemia?**
   - **PNH clone emerges in AA** (immune escape); treat per AA guidelines (IST/HSCT); C5 inhibitor for haemolysis

10. **What is Pegcetacoplan and how does it differ from eculizumab?**
    - **C3 inhibitor (subcutaneous)**; controls **both intravascular (MAC) and extravascular (C3b opsonisation)** haemolysis

---

## 🧠 Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **PNH vs AIHA** | **PNH: DAT negative, flow CD55/CD59-, intravascular**; **AIHA: DAT positive, extravascular** |
| **PNH vs TTP** | **PNH: No schistocytes, no thrombocytopenia (initially), flow CD55/CD59-**; **TTP: Schistocytes, thrombocytopenia, ADAMTS13<10%** |
| **CD55 vs CD59** | **CD55 = Decay Accelerating Factor (C3 convertase)**; **CD59 = MAC Inhibitory Protein (C5b-9)** |
| **Eculizumab vs Ravulizumab** | **Ravulizumab = Longer half-life (q8wk vs q2wk)**; same mechanism, same meningococcal prophylaxis |
| **Morning Haemoglobinuria** | **Nocturnal relative acidosis** → complement activation during sleep |

| Mnemonic | Meaning |
|----------|---------|
| **"PNH = PIGA = GPI Anchor Lost"** | Molecular defect |
| **"CD55 = Decay C3 convertase; CD59 = Stop MAC"** | Complement regulation |
| **"Haemoglobinuria = Morning"** | Nocturnal haemolysis |
| **"Thrombosis = Budd-Chiari + Cerebral Sinus"** | Classic sites |
| **"Eculizumab = MenVax 2wks Before"** | Mandatory vaccination |
| **"FLAER = Flow GPI Direct"** | High sensitivity test |

---

## 🗺️ Mind Map

```mermaid
mindmap
  root((Paroxysmal Nocturnal Haemoglobinuria))
    Genetics
      Somatic PIGA Mutation (Xp22)
      GPI Anchor Defect
    Pathophysiology
      CD55 (DAF) Loss → C3 Convertase Uncontrolled
      CD59 (MIRL) Loss → MAC Formation
      Intravascular Haemolysis + NO Scavenging
    Diagnosis
      Flow: CD55/CD59 (Granulocytes)
      FLAER (High Sens)
      Type II Partial, Type III Complete
    Clinical
      Morning Haemoglobinuria
      Thrombosis (Budd-Chiari, Cerebral Sinus)
      Dysphagia, ED (NO Scavenging)
      Cytopenias (BM Failure Overlap)
    Treatment
      Eculizumab (q2wk IV)
      Ravulizumab (q8wk IV)
      Pegcetacoplan (C3i, q2wk SC)
      MenVax 2wks Before
    Complications
      Thrombosis 40-50%
      Renal (Haemosiderinuria)
      Pulm HTN
```

---

## 📋 One-Page Revision Card

| **PNH – FCPS/MRCP REVISION CARD** |
|-------------------------------------|
| **Defect**: **Somatic PIGA mutation** → **GPI anchor loss** → **CD55 (DAF) & CD59 (MIRL) absent** |
| **Diagnosis**: **Flow cytometry CD55/CD59 on granulocytes** (gold standard); **FLAER** |
| **Haemolysis**: **Intravascular** → **Morning haemoglobinuria**, haemosiderinuria, LDH↑↑ |
| **Thrombosis**: **40-50% risk**; **Budd-Chiari, Cerebral Sinus, Splanchnic** |
| **NO Scavenging**: Dysphagia, Erectile Dysfunction, Pulm HTN |
| **Treatment**: **Eculizumab (q2wk IV) / Ravulizumab (q8wk IV) / Pegcetacoplan (C3i, q2wk SC)** |
| **Mandatory**: **MenACWY + MenB vaccine 2 WEEKS BEFORE** C5 inhibitor |
| **Prophylaxis**: **Penicillin** during C5 inhibitor; **DOAC** if large clone |
| **Folic Acid**: 5 mg daily; **Iron** if deficient (chronic loss) |
| **BM Failure Overlap**: PNH clone in AA → IST/HSCT per AA guidelines |

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
| **Must Know** | PIGA mutation, GPI anchor defect, CD55/CD59 loss, flow cytometry diagnosis, intravascular haemolysis, thrombosis sites, eculizumab/ravulizumab, meningococcal vaccine 2wks before, penicillin prophylaxis, folic acid, Budd-Chiari |
| **Should Know** | Type II/III clone classification, granulocyte vs RBC clone monitoring, FLAER, ravulizumab q8wk, pegcetacoplan (C3 inhibitor), NO scavenging complications, AA/PNH overlap management, anticoagulation indications |
| **Nice to Know** | PIGA gene structure, complement pathway details (alternative vs classical), eculizumab pharmacokinetics, ravulizumab recycling (FcRn), crovalimab (anti-C5 recycling), iptacopan (factor B inhibitor), danicopan (factor D inhibitor), HSCT in PNH-AA, pregnancy in PNH |

---

## ✅ Self-Test Scorecard

| Section | Score (0-10) | Notes |
|---------|--------------|-------|
| Molecular Pathophysiology | | |
| Diagnostic Flow Cytometry | | |
| Clinical Features & Thrombosis | | |
| Complement Inhibitor Therapy | | |
| Vaccination & Prophylaxis | | |
| BM Failure Overlap | | |
| Viva Questions | | |

---

## 🔗 Local Navigation

- **Previous**: [[G6PD Deficiency]]
- **Next**: [[TTP/HUS]]
- **Section Hub**: [[Anaemia and Red Cell Disorders]]
- **MOC**: [[Hematology MOC]]
- **Template**: [[../Templates/Hematology Topic Template]]

---

*Generated for FCPS/MRCP exam preparation. Based on Davidson Medicine 24th Ed Chapter 25.*
---

> Auto-generated study sections for "Hematology" — Ch 24: Haematology & Transfusion Medicine.

## Flashcards (34 generated)

- Q: What is the definition of Hematology?
  A: [!info] Davidson Ch 25 Alignment: Haemolytic Anaemias → Paroxysmal Nocturnal Haemoglobinuria
- Q: What is Flow Cytometry (Gold Standard) of Hematology?
  A: CD55 (DAF) & CD59 (MIRL) ABSENT/DECREASED on granulocytes, monocytes, RBCs
- Q: How is Hematology classified?
  A: Type I (Normal), Type II (Partial loss, 10-70%), Type III (Complete loss, <10% normal)
- Q: What is Granulocyte Clone of Hematology?
  A: Most stable (lifespan days); preferred for monitoring
- Q: What is RBC Clone of Hematology?
  A: Underestimates (haemolysed); Type III lost fastest
- Q: What is the investigation of choice for Hematology?
  A: Historical (positive in PNH); replaced by flow
- Q: What is PIGA Sequencing of Hematology?
  A: Confirms somatic mutation
- Q: What is FLAER (Fluorescent AER) of Hematology?
  A: High sensitivity for GPI deficiency (binds GPI anchor directly)
- Q: What is Risk of Hematology?
  A: 40-50% lifetime (untreated); Highest in first 1-2 years
- Q: What is Sites of Hematology?
  A: Budd-Chiari (hepatic vein), Cerebral venous sinus, Portal/splanchnic, DVT/PE, Dermal necrosis
- Q: What is Prophylaxis of Hematology?
  A: Anticoagulation if large clone (>50%) or prior thrombosis; C5 inhibitor reduces risk by >90%
- Q: How is Hematology managed?
  A: Full anticoagulation; C5 inhibitor; Thrombolysis for acute venous thrombosis
- Q: What is Flow Cytometry (Gold Standard) of Hematology?
  A: CD55 (DAF) & CD59 (MIRL) ABSENT/DECREASED on granulocytes, monocytes, RBCs
- Q: How is Hematology classified?
  A: Type I (Normal), Type II (Partial loss, 10-70%), Type III (Complete loss, <10% normal)
- Q: What is Granulocyte Clone of Hematology?
  A: Most stable (lifespan days); preferred for monitoring
- Q: What is RBC Clone of Hematology?
  A: Underestimates (haemolysed); Type III lost fastest
- Q: What is the investigation of choice for Hematology?
  A: Historical (positive in PNH); replaced by flow
- Q: What is PIGA Sequencing of Hematology?
  A: Confirms somatic mutation
- Q: What is FLAER (Fluorescent AER) of Hematology?
  A: High sensitivity for GPI deficiency (binds GPI anchor directly)
- Q: What is Risk of Hematology?
  A: 40-50% lifetime (untreated); Highest in first 1-2 years
- Q: What is Sites of Hematology?
  A: Budd-Chiari (hepatic vein), Cerebral venous sinus, Portal/splanchnic, DVT/PE, Dermal necrosis
- Q: What is Prophylaxis of Hematology?
  A: Anticoagulation if large clone (>50%) or prior thrombosis; C5 inhibitor reduces risk by >90%
- Q: How is Hematology managed?
  A: Full anticoagulation; C5 inhibitor; Thrombolysis for acute venous thrombosis
- Q: What is Mutation of Hematology?
  A: Somatic PIGA (Xp22) → GPI anchor defect
- Q: What is Key Defect of Hematology?
  A: Loss of CD55 (DAF) & CD59 (MIRL) → uncontrolled complement
- Q: What is the investigation of choice for Hematology?
  A: Flow cytometry CD55/CD59 (granulocytes best); FLAER
- Q: What is Haemolysis of Hematology?
  A: Intravascular → haemoglobinuria (nocturnal), haemosiderinuria
- Q: What is Thrombosis of Hematology?
  A: 40-50% risk; Budd-Chiari, cerebral sinus, splanchnic veins
- Q: How is Hematology managed?
  A: Eculizumab (q2wk IV) / Ravulizumab (q8wk IV) / Pegcetacoplan (q2wk SC)
- Q: What is Vaccination of Hematology?
  A: MenACWY + MenB 2 WEEKS BEFORE starting C5 inhibitor
- Q: What is Prophylaxis of Hematology?
  A: Penicillin during C5 inhibitor therapy
- Q: What is Folic Acid of Hematology?
  A: 5 mg daily
- Q: What is Iron of Hematology?
  A: Chronicloss → iron deficiency → replace
- Q: What is BM Failure Overlap of Hematology?
  A: PNH clone in AA/MDS; IST/HSCT per BM failure guidelines

## MCQs (1 generated)

1. **Which of the following best describes Hematology?**
   A. **[!info] Davidson Ch 25 Alignment: Haemolytic Anaemias → Paroxysmal Nocturnal Haemoglobinuria**
   B. An unrelated condition not matching the clinical picture of Hematology
   C. A complication seen late in the disease course of Hematology
   D. A condition that mimics Hematology but has a different underlying cause

## SBA Questions (1 generated)

1. A patient with suspected Hematology presents with: Category — Clone Size; Classic PNH — Large (>50% granulocytes); Subclinical PNH — Small (<10-20%). What is the most likely diagnosis?
   A. **Hematology**
   B. A condition that mimics Hematology but is not the same entity
   C. A complication of Hematology rather than the primary diagnosis
   D. An unrelated condition in the same clinical category as Hematology

