---
tags: [medicine, davidson, hematology, itp, immune-thrombocytopenia, fcps, mrcp]
davidson_chapter: Chapter 25: Haematology and Transfusion Medicine
status: full-fcps-mrcp-note
priority: high
exam_relevance: "FCPS: Essential | MRCP: Core | Platelet thresholds, steroids, IVIG, TPO-RA (eltrombopag/romiplostim), rituximab, splenectomy"
see_also: "[[Secondary ITP]], [[TTP/HUS]], [[HIT]], [[Evans Syndrome]], [[Platelet Transfusion]]"
created: 2025-06-16
modified: 2025-06-16
---

# Immune Thrombocytopenia (ITP)

> [!info] **Davidson Ch 25 Alignment**: Bleeding and Thrombotic Disorders → Platelet Disorders → Immune Thrombocytopenia
> **FCPS/MRCP Focus**: Diagnosis of exclusion, platelet thresholds, 1st line (steroids/IVIG), 2nd line (TPO-RA, rituximab), 3rd line (splenectomy, fostamatinib), pregnancy

---

## 🎯 Learning Objectives

- [ ] Define ITP: **Isolated thrombocytopenia (Plt <100×10⁹/L)** due to **autoantibody-mediated platelet destruction** + **impaired production**
- [ ] Apply **diagnosis of exclusion**: Rule out pseudothrombocytopenia, secondary causes, bone marrow failure
- [ ] Use **platelet count thresholds** to guide treatment: <30 (treat), 30-50 (monitor/treat if bleed risk), >50 (observe)
- [ ] Manage **1st line**: **Prednisolone/Dexamethasone** OR **IVIG** (urgent/pre-procedure)
- [ ] Manage **2nd line**: **TPO-RA (Eltrombopag/Romiplostim)**, **Rituximab**, **Fostamatinib**
- [ ] Manage **3rd line**: **Splenectomy**, **Immunosuppressants** (AZA, MMF, Cyc, CSA, TAC)
- [ ] Recognise **Secondary ITP**: SLE, HIV, HCV, H. pylori, drugs, CLL, lymphoproliferative
- [ ] Manage **Pregnancy in ITP**: Maternal/fetal platelet counts, delivery mode, neonatal monitoring

---

## 📖 Definition & Classification

| Category | Definition |
|----------|------------|
| **Primary ITP** | **Isolated Plt <100×10⁹/L** + no other cause; **Diagnosis of exclusion** |
| **Secondary ITP** | Associated with: **SLE, APS, HIV, HCV, H. pylori**, Drugs (heparin, quinine, vancomycin), **CLL, Lymphoma, CVID, ALPS** |
| **Newly Diagnosed** | <3 months from diagnosis |
| **Persistent ITP** | 3-12 months |
| **Chronic ITP** | **>12 months** |

> [!tip] **FCPS/MRCP**: **ITP = Diagnosis of exclusion**. **Plt <100, otherwise normal CBC/film**. **Antiplatelet autoantibodies (GPIIb/IIIa, GPIb/IX) – not routinely tested**. **Treat based on Plt count + bleeding symptoms, NOT absolute number alone**.

---

## ⚙️ Pathophysiology

```mermaid
flowchart TD
    A[Autoantibodies: Anti-GPIIb/IIIa, Anti-GPIb/IX] --> B[Fcγ Receptor-Mediated Phagocytosis]
    B --> C[Splenic Macrophage Clearance → **↑ Platelet Destruction**]
    A --> D[Anti-Megakaryocyte Antibodies]
    D --> E[**Impaired Platelet Production** (Megakaryocyte Apoptosis)]
    C & E --> F[**Thrombocytopenia**]
    F --> G[Bleeding Risk ∝ 1/Plt Count]
```

---

## 🔬 Diagnostic Workup

```mermaid
flowchart TD
    A[Isolated Thrombocytopenia] --> B[**Exclude Pseudothrombocytopenia**]
    B --> C[**EDTA Tube → Citrate/Heparin Tube / Blood Film for Clumps**]
    C --> D[**CBC + Film**]
    D --> E{**Isolated Plt <100**? Normal Hb, WBC, Film?}
    E -->|Yes| F[**Secondary Cause Screen**]
    F --> G1[**Virology: HIV, HCV, H. pylori**]
    F --> G2[**Autoimmune: ANA, dsDNA, ENA, APS screen**]
    F --> G3[**Drug History: Heparin, Quinine, Sulpha, Vancomycin, Linezolid**]
    F --> G4[**Lymphoproliferative: CLL, Lymphoma (Flow if nodes/splenomegaly)**]
    F --> G5[**CVID: IgG/IgA/IgM levels**]
    F --> G6[**Pregnancy Test**]
    G1 & G2 & G3 & G4 & G5 & G6 --> H[**BM Biopsy** if >60y, atypical features, refractory, or suspected MDS]
    H --> I[**Diagnosis: Primary ITP** (if all negative)]
```

### Essential Investigations

| Test | Purpose |
|------|---------|
| **CBC + Film** | **Isolated thrombocytopenia**, large platelets, **NO schistocytes/NRBCs** |
| **Blood Group + DAT** | Exclude Evans syndrome (AIHA + ITP) |
| **HIV / HCV / H. pylori** | Secondary ITP causes |
| **ANA, dsDNA, ENA, APS** | SLE, APS |
| **Immunoglobulins** | CVID (low IgG/IgA/IgM) |
| **Lymphoproliferative Screen** | Flow cytometry if lymphadenopathy/splenomegaly |
| **BM Biopsy** | **If >60y, refractory, atypical, or suspected MDS** – shows ↑ megakaryocytes |

---

## 🩺 Clinical Features & Bleeding Assessment

| Platelet Count | Bleeding Risk | Typical Presentation |
|----------------|---------------|----------------------|
| **>50** | Low | Often asymptomatic (incidental) |
| **30-50** | Moderate | Easy bruising, petechiae, menorrhagia |
| **20-30** | High | Mucosal bleeding, epistaxis, gum bleeding |
| **<20** | Very High | **Spontaneous mucosal bleeding**, haematuria, GI bleed |
| **<10** | Critical | **Intracranial haemorrhage risk** |

**Bleeding Assessment Tools**: **WHO Bleeding Scale**, **IBLS (ITP Bleeding Scale)**

---

## 💊 Management Algorithm

```mermaid
flowchart TD
    A[ITP Diagnosis: Plt <100] --> B{Plt Count & Bleeding}
    B -->|Plt >50, No bleeding| C[**Observe** (Monitor q1-3mo)]
    B -->|Plt 30-50, Minor bleeding| D[**Observe or Short Steroids** if symptomatic]
    B -->|Plt <30 OR Significant bleeding| E[**TREAT**]
    E --> F[**1st Line: Prednisolone 0.5-1 mg/kg/day** × 4-6wk taper<br/>OR **Dexamethasone 40 mg daily × 4d** (q2-4wk × 1-3 cycles)]<br/>& **IVIG 1 g/kg/day × 2d** (if urgent/pre-procedure/surgery)
    F --> G{Response at 2-4wk?}
    G -->|Response| H[Taper Steroids over 6-8wk<br/>Monitor q1-3mo]
    G -->|No Response / Relapse on taper| I[**2nd Line Options**]
    I --> J1[**TPO-RA: Eltrombopag 50mg/day** (25mg if Asian/Elderly) / **Romiplostim 1-10 µg/kg SC weekly**]
    I --> J2[**Rituximab 375 mg/m² weekly × 4**]
    I --> J3[**Fostamatinib** (Syk inhibitor) if TPO-RA/Ritux fail]
    J1 & J2 & J3 --> K{Response?}
    K -->|Sustained| L[Continue / Taper]
    K -->|Refractory| M[**3rd Line: Splenectomy** (laparoscopic)<br/>**Immunosuppressants**: AZA, MMF, CyA, Tac, Cyc]
```

---

## 💊 Treatment Details by Line

### 1st Line

| Agent | Dose | Indication | Response |
|-------|------|------------|----------|
| **Prednisolone** | **0.5-1 mg/kg/day** (max 80mg) × 2-4wk → **taper over 6-8wk** | Standard | 70-80% initial; ~30% sustained off steroids |
| **High-dose Dexamethasone** | **40 mg PO daily × 4 days** q2-4wk × 1-3 cycles | Alternative to prednisolone | Similar; less chronic side effects |
| **IVIG** | **1 g/kg/day × 2 days** (or 0.4 g/kg/day × 5d) | **Urgent** (pre-surgery, severe bleed, pregnancy) | Rapid (24-48h); transient (2-4wk) |

> [!warning] **Avoid prolonged high-dose steroids** (side effects). **IVIG = bridge**, not maintenance.

### 2nd Line

| Agent | Dose | Mechanism | Key Points |
|-------|------|-----------|------------|
| **Eltrombopag (TPO-RA)** | **50 mg/day** (25mg if Asian, hepatic impairment, elderly) | Oral TPO mimetic | **Take on empty stomach** (2h before/4h after food/Ca); **LFT monitoring** (hepatotoxicity); **Cataract risk** |
| **Romiplostim (TPO-RA)** | **1-10 µg/kg SC weekly** (adjust to Plt 50-200) | SC peptide-Fc fusion | No food restrictions; **No hepatotoxicity**; **Bone marrow fibrosis** (long-term) |
| **Rituximab** | **375 mg/m² weekly × 4** | Anti-CD20 (depletes autoreactive B-cells) | **60-70% response**; **Late response (2-3mo)**; **Hypogammaglobulinaemia risk**; **Retreatment effective** |
| **Fostamatinib** | **100-150 mg BD** | **Syk inhibitor** (blocks FcγR signaling) | **Diarrhoea, HTN, LFT↑**, neutropenia; **Refractory ITP** |

> [!tip] **TPO-RA = preferred 2nd line** (sustained response, oral/SC). **Rituximab = if TPO-RA contraindicated or young woman avoiding long-term TPO-RA**.

### 3rd Line (Refractory ITP)

| Option | Details |
|--------|---------|
| **Splenectomy** | **Laparoscopic**; **Response >70%**; **OPSI risk** → Vaccines (PCV13, PPSV23, MenACWY, Hib) + **Penicillin prophylaxis** |
| **Immunosuppressants** | **Azathioprine, Mycophenolate, Cyclosporine, Tacrolimus, Cyclophosphamide** – steroid-sparing |
| **Combination** | **TPO-RA + Rituximab + Immunosuppressant** |
| **Dapsone / Danazol** | Historical, limited evidence |

---

## 🤰 ITP in Pregnancy

| Trimester | Platelet Target | Management |
|-----------|-----------------|------------|
| **1st/2nd** | **>20-30** (asymptomatic) / **>50** (symptomatic/procedure) | **Observe if Plt >20-30**; **Prednisolone 10-20 mg/day** if <20 |
| **3rd / Delivery** | **>50** (vaginal) / **>80-100** (caesarean/neuraxial) | **IVIG 1g/kg × 2d** + **Prednisolone** to raise Plt; **Delivery at 37-38wk** |
| **Neonatal** | **Cord blood Plt** | **Risk of neonatal thrombocytopenia** (~10-15% <50); **No routine cordocentesis**; **Mode of delivery not determined by fetal Plt** |

> [!warning] **Avoid**: Eltrombopag/Romiplostim (Category C), Rituximab (B-cell depletion in fetus), Fostamatinib, Splenectomy. **Safe**: Steroids, IVIG.

---

## 🔄 Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **Pseudothrombocytopenia** | **EDTA-induced clumping** → **Citrate/Heparin tube normal**, clumps on film |
| **TTP/HUS** | **MAHA (schistocytes), ADAMTS13<10% (TTP), Shiga toxin (HUS)** |
| **HIT** | **Heparin 5-14d, PF4/heparin Ab+, thrombosis** |
| **DIC** | **PT/APTT↑, Fibrinogen↓, D-dimer↑↑**, underlying cause |
| **MDS / AA** | **Pancytopenia / Dysplasia / Hypocellular BM** |
| **Drug-induced Thrombocytopenia** | **Temporal relation to drug** (heparin, quinine, vancomycin, linezolid, sulpha) |
| **Hypersplenism** | **Splenomegaly + Pancytopenia**, portal hypertension |
| **Congenital Thrombocytopenia** | **Lifelong, family history** (MYH9-RD, WAS, GATA1, ANKRD26) |

---

## 💡 FCPS/MRCP High-Yield Summary

| Topic | Key Point |
|-------|-----------|
| **Diagnosis** | **Isolated Plt <100** + **Exclusion** (pseudothrombocytopenia, secondary causes, BM failure) |
| **Thresholds** | **>50 observe**; **30-50 treat if bleed risk**; **<30 treat** |
| **1st Line** | **Prednisolone 0.5-1 mg/kg × 4-6wk taper** OR **Dex 40mg × 4d q2-4wk**; **IVIG for urgent/pre-proc** |
| **2nd Line** | **TPO-RA: Eltrombopag (oral, LFT) / Romiplostim (SC, BM fibrosis)**; **Rituximab 375mg/m² × 4** |
| **3rd Line** | **Splenectomy** (lap, OPSI risk → vaccines + penicillin); **Immunosuppressants** |
| **Fostamatinib** | **Syk inhibitor** – refractory ITP; diarrhoea, HTN, LFT↑ |
| **Pregnancy** | **Steroids + IVIG**; **Target Plt >50 (vaginal) / >80-100 (C-section)**; **No TPO-RA/Ritux** |
| **Secondary ITP** | **SLE, HIV, HCV, H. pylori, Drugs, CLL, CVID** – treat underlying |
| **Helicobacter pylori** | **Eradication → Plt recovery in ~50%** (especially in high-prevalence areas) |

---

## ❓ Viva Questions

1. **What is the diagnostic approach to ITP?**
   - **Diagnosis of exclusion**: Isolated Plt <100 + **exclude pseudothrombocytopenia (citrate tube)**, secondary causes (HIV, HCV, H. pylori, SLE, drugs, CLL), BM failure

2. **What platelet count thresholds guide treatment in ITP?**
   - **>50 asymptomatic = observe**; **30-50 symptomatic = treat**; **<30 = treat**; **<20 = high bleed risk; <10 = ICH risk**

3. **What are the first-line treatments for ITP and when is IVIG preferred?**
   - **Prednisolone 0.5-1 mg/kg/day × 4-6wk taper** OR **Dexamethasone 40mg × 4d q2-4wk**; **IVIG = urgent/pre-procedure/pregnancy/severe bleed**

4. **Compare Eltrombopag vs Romiplostim as TPO-RA.**
   - **Eltrombopag**: Oral, **empty stomach, LFT monitoring, cataract risk**; **Romiplostim**: SC weekly, **no food restriction, BM fibrosis risk**

5. **What is the role of Rituximab in ITP?**
   - **2nd line**; **375 mg/m² weekly × 4**; **60-70% response**, delayed (2-3mo); **retreatment effective**; avoid in pregnancy

6. **How is ITP managed in pregnancy?**
   - **Target Plt >20-30 (asymptomatic) / >50 (symptomatic/delivery)**; **Prednisolone 10-20mg + IVIG**; **Delivery 37-38wk**; **No TPO-RA/Rituximab**

7. **What is the role of H. pylori eradication in ITP?**
   - **Eradication → Plt recovery in ~50%** (especially high-prevalence areas); test all ITP patients

8. **When is splenectomy indicated in ITP and what are the precautions?**
   - **Refractory to 2nd line**; **Laparoscopic**; **Vaccines 2wk pre-op (PCV13, PPSV23, MenACWY, Hib) + Penicillin prophylaxis lifelong**

9. **What is Fostamatinib and when is it used?**
   - **Syk inhibitor** (blocks FcγR signaling); **Refractory ITP after TPO-RA/Rituximab**; **Diarrhoea, HTN, LFT↑, neutropenia**

10. **How do you differentiate ITP from TTP/HUS?**
    - **ITP: Isolated thrombocytopenia, normal Hb/film, no schistocytes, ADAMTS13 normal**; **TTP/HUS: MAHA (schistocytes), anaemia, ADAMTS13<10%/Shiga toxin**

---

## 🧠 Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **ITP vs TTP** | **ITP = Isolated Plt low, normal film**; **TTP = MAHA + schistocytes + ADAMTS13<10%** |
| **ITP vs HIT** | **HIT = Heparin 5-14d, PF4 Ab+, thrombosis**; **ITP = no heparin, bleeding** |
| **ITP vs Pseudothrombocytopenia** | **EDTA clumps → Citrate tube normal** |
| **Eltrombopag vs Romiplostim** | **Eltrombopag = Oral, food restriction, LFT**; **Romiplostim = SC, BM fibrosis** |
| **Primary vs Secondary ITP** | **Secondary = SLE, HIV, HCV, H. pylori, Drugs, CLL** – treat underlying |

| Mnemonic | Meaning |
|----------|---------|
| **"ITP = Isolated Thrombocytopenia, Primary = Exclusion"** | Diagnosis |
| **"<30 = Treat; >50 = Observe"** | Platelet thresholds |
| **"1st = Steroids/IVIG; 2nd = TPO-RA/Ritux; 3rd = Spleen"** | Treatment lines |
| **"Eltrombopag = Empty Stomach, LFT"** | Key points |
| **"Rituximab = Late Response (2-3mo)"** | Timing |
| **"Pregnancy = Steroids + IVIG, NO TPO-RA/Ritux"** | Pregnancy management |
| **"H. pylori = Eradicate = Cure 50%"** | Secondary ITP |

---

## 🗺️ Mind Map

```mermaid
mindmap
  root((Immune Thrombocytopenia))
    Diagnosis
      Plt <100, Isolated
      Exclude: Pseudo, Secondary, BM Failure
      H. pylori, HIV, HCV, SLE, Drugs, CLL
    Thresholds
      >50: Observe
      30-50: Treat if bleed
      <30: Treat
      <20: High bleed risk
    1st Line
      Prednisolone 0.5-1mg/kg
      Dex 40mg x4d
      IVIG (Urgent)
    2nd Line
      TPO-RA: Eltrombopag (Oral, LFT) / Romiplostim (SC)
      Rituximab 375mg/m2 x4
      Fostamatinib (Syk inhibitor)
    3rd Line
      Splenectomy (Lap, Vaccines, Penicillin)
      Immunosuppressants (AZA, MMF, CyA)
    Pregnancy
      Target >50 (vaginal) / >80 (CS)
      Steroids + IVIG
      NO TPO-RA / Rituximab
```

---

## 📋 One-Page Revision Card

| **ITP – FCPS/MRCP REVISION CARD** |
|-------------------------------------|
| **Diagnosis**: **Isolated Plt <100** + **Exclusion** (pseudothrombocytopenia, secondary, BM failure) |
| **Thresholds**: **>50 observe**; **30-50 treat if bleed**; **<30 treat**; **<10 ICH risk** |
| **1st Line**: **Pred 0.5-1mg/kg × 4-6wk taper** OR **Dex 40mg × 4d q2-4wk**; **IVIG (urgent)** |
| **2nd Line**: **TPO-RA: Eltrombopag (Oral, empty stomach, LFT) / Romiplostim (SC weekly, BM fibrosis)**; **Rituximab 375mg/m² × 4** |
| **3rd Line**: **Splenectomy** (Lap, Vaccines + Penicillin); **Immunosuppressants** |
| **Fostamatinib**: **Syk inhibitor** – refractory; Diarrhoea, HTN, LFT↑ |
| **Pregnancy**: Target >50 (vaginal) / >80 (CS); **Pred + IVIG**; **NO TPO-RA/Ritux** |
| **H. pylori**: **Eradicate → 50% response** |
| **Secondary ITP**: SLE, HIV, HCV, Drugs, CLL, CVID – treat underlying |

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
| **Must Know** | Diagnosis of exclusion, platelet thresholds, 1st line (steroids/IVIG/dex), 2nd line (TPO-RA/rituximab/fostamatinib), 3rd line (splenectomy/immunosuppressants), pregnancy management, H. pylori, secondary causes |
| **Should Know** | WHO/ICBLS bleeding scales, eltrombopag vs romiplostim details, rituximab retreatment, fostamatinib mechanism, IVIG dosing (1g/kg×2d vs 0.4g/kg×5d), dexamethasone pulse regimen, splenectomy OPSI prophylaxis, neonatal thrombocytopenia management, CVID screen |
| **Nice to Know** | Anti-GPIIb/IIIa vs GPIb/IX pathophysiology, TPO-RA bone marrow fibrosis mechanism, rituximab B-cell depletion kinetics, splenectomy laparoscopic vs open, eltrombopag drug interactions (Ca, antacids), romiplostim immunogenicity, novel agents (ruxolitinib, ianalumab, telitacicept), ITP registry data, cost-effectiveness |

---

## ✅ Self-Test Scorecard

| Section | Score (0-10) | Notes |
|---------|--------------|-------|
| Diagnosis & Differential | | |
| Platelet Thresholds & Indications | | |
| 1st Line Management | | |
| 2nd Line (TPO-RA, Rituximab, Fostamatinib) | | |
| 3rd Line & Splenectomy | | |
| Pregnancy Management | | |
| Secondary ITP | | |
| Viva Questions | | |

---

## 🔗 Local Navigation

- **Previous**: [[MDS Classification & Management]]
- **Next**: [[DIC]]
- **Section Hub**: [[Bleeding and Thrombotic Disorders]]
- **MOC**: [[Hematology MOC]]
- **Template**: [[../Templates/Hematology Topic Template]]

---

*Generated for FCPS/MRCP exam preparation. Based on Davidson Medicine 24th Ed Chapter 25.*
---

> Auto-generated study sections for "Hematology" — Ch 24: Haematology & Transfusion Medicine.

## Flashcards (18 generated)

- Q: What is the definition of Hematology?
  A: [!info] Davidson Ch 25 Alignment: Bleeding and Thrombotic Disorders → Platelet Disorders → Immune Thrombocytopenia
- Q: What is Splenectomy of Hematology?
  A: Laparoscopic; Response >70%; OPSI risk → Vaccines (PCV13, PPSV23, MenACWY, Hib) + Penicillin prophylaxis
- Q: What is Immunosuppressants of Hematology?
  A: Azathioprine, Mycophenolate, Cyclosporine, Tacrolimus, Cyclophosphamide – steroid-sparing
- Q: What is Combination of Hematology?
  A: TPO-RA + Rituximab + Immunosuppressant
- Q: What is Dapsone / Danazol of Hematology?
  A: Historical, limited evidence
- Q: What is Splenectomy of Hematology?
  A: Laparoscopic; Response >70%; OPSI risk → Vaccines (PCV13, PPSV23, MenACWY, Hib) + Penicillin prophylaxis
- Q: What is Immunosuppressants of Hematology?
  A: Azathioprine, Mycophenolate, Cyclosporine, Tacrolimus, Cyclophosphamide – steroid-sparing
- Q: What is Combination of Hematology?
  A: TPO-RA + Rituximab + Immunosuppressant
- Q: What is Dapsone / Danazol of Hematology?
  A: Historical, limited evidence
- Q: What is the investigation of choice for Hematology?
  A: Isolated Plt <100 + Exclusion (pseudothrombocytopenia, secondary causes, BM failure)
- Q: What is Thresholds of Hematology?
  A: >50 observe; 30-50 treat if bleed risk; <30 treat
- Q: What is 1st Line of Hematology?
  A: Prednisolone 0.5-1 mg/kg × 4-6wk taper OR Dex 40mg × 4d q2-4wk; IVIG for urgent/pre-proc
- Q: What is 2nd Line of Hematology?
  A: TPO-RA: Eltrombopag (oral, LFT) / Romiplostim (SC, BM fibrosis); Rituximab 375mg/m² × 4
- Q: What is 3rd Line of Hematology?
  A: Splenectomy (lap, OPSI risk → vaccines + penicillin); Immunosuppressants
- Q: What is Fostamatinib of Hematology?
  A: Syk inhibitor – refractory ITP; diarrhoea, HTN, LFT↑
- Q: What is Pregnancy of Hematology?
  A: Steroids + IVIG; Target Plt >50 (vaginal) / >80-100 (C-section); No TPO-RA/Ritux
- Q: What is Secondary ITP of Hematology?
  A: SLE, HIV, HCV, H. pylori, Drugs, CLL, CVID – treat underlying
- Q: What is Helicobacter pylori of Hematology?
  A: Eradication → Plt recovery in ~50% (especially in high-prevalence areas)

## MCQs (1 generated)

1. **Which of the following best describes Hematology?**
   A. **[!info] Davidson Ch 25 Alignment: Bleeding and Thrombotic Disorders → Platelet Disorders → Immune Thrombocytopenia**
   B. An unrelated condition not matching the clinical picture of Hematology
   C. A complication seen late in the disease course of Hematology
   D. A condition that mimics Hematology but has a different underlying cause

## SBA Questions (1 generated)

1. A patient with suspected Hematology presents with: Primary ITP — Isolated Plt <100×10⁹/L + no other cause; Diagnosis of exclusion; Secondary ITP — Associated with: SLE, APS, HIV, HCV, H. pylori, Drugs (heparin, quinine, vancomycin), CLL, Lymphoma, CVID, ALPS; Newly Diagnosed — <3 months from diagnosis. What is the most likely diagnosis?
   A. **Hematology**
   B. A condition that mimics Hematology but is not the same entity
   C. A complication of Hematology rather than the primary diagnosis
   D. An unrelated condition in the same clinical category as Hematology

## PasTest Scenario SBAs (Clinical Vignettes)

> **Auto-generated PasTest/Mediscope-style scenario SBAs** grounded in the authored source content. Each scenario is a clinical vignette with 4 options. **Source: Ch 24: Haematology / ITP**

**Q1.** A patient presents with features consistent with ITP. The clinical picture is most consistent with: Bleeding Assessment Tools: **WHO Bleeding Scale**, **IBLS (ITP Bleeding Scale)** What is the most likely diagnosis?

  - **A.** ITP
  - **B.** A closely related condition in the same clinical area
  - **C.** A complication of ITP
  - **D.** An unrelated mimic with overlapping features

  > **Answer: A** — ITP

**Q2.** A patient is diagnosed with ITP. What is the most appropriate first-line management approach?

  - **A.** Standard guideline-directed first-line therapy
  - **B.** Most aggressive advanced therapy as first-line
  - **C.** No treatment needed in most cases
  - **D.** Investigational/compassionate-use therapy only

  > **Answer: A** — Standard guideline-directed first-line therapy

**Q3.** Which of the following best describes the underlying pathophysiology / definition of ITP?

  - **A.** [!tip] **FCPS/MRCP**: **ITP = Diagnosis of exclusion**. **Plt <100, otherwise normal CBC/film**. **Antiplatelet autoantibodies (GPIIb/IIIa, GPIb/IX) – not routinely tested**. **Tre
  - **B.** A common misattribution to a similar but distinct condition
  - **C.** An outdated or disproven mechanism
  - **D.** A complication rather than the underlying disease process

  > **Answer: A** — [!tip] **FCPS/MRCP**: **ITP = Diagnosis of exclusion**. **Plt <100, otherwise normal CBC/film**. **Antiplatelet autoantibodies (GPIIb/IIIa, GPIb/IX) –

