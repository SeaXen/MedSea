---
tags: [medicine, davidson, hematology, hit, heparin-induced-thrombocytopenia, fcps, mrcp]
davidson_chapter: Chapter 25: Haematology and Transfusion Medicine
status: full-fcps-mrcp-note
priority: high
exam_relevance: "FCPS: Essential | MRCP: Core | 4Ts score, PF4/heparin ELISA/SRA, stop heparin, alternative anticoagulation (argatroban/bivalirudin/fondaparinux/DOAC), DO NOT use warfarin alone"
see_also: "[[DIC]], [[TTP/HUS]], [[VTE]], [[Anticoagulation]], [[Platelet Transfusion]]"
created: 2025-06-16
modified: 2025-06-16
---

# Heparin-Induced Thrombocytopenia (HIT)

> [!info] **Davidson Ch 25 Alignment**: Bleeding and Thrombotic Disorders → Platelet Disorders → HIT
> **FCPS/MRCP Focus**: 4Ts score, PF4/heparin ELISA & SRA, immediate heparin cessation, alternative anticoagulants, NO warfarin alone, NO platelet transfusion unless bleeding

---

## 🎯 Learning Objectives

- [ ] Define HIT: **Immune-mediated** adverse drug reaction to heparin → **anti-PF4/heparin antibodies** → platelet activation → **thrombocytopenia + thrombosis (HITT)**
- [ ] Apply **4Ts Score** for pre-test probability: Thrombocytopenia, Timing, Thrombosis, oTher causes
- [ ] Diagnose: **PF4/Heparin ELISA** (screening, high sensitivity) → **Serotonin Release Assay (SRA)** (confirmatory, gold standard)
- [ ] Manage: **STOP ALL HEPARIN** (UFH, LMWH, heparin flushes/catheters) → **START ALTERNATIVE ANTICOAGULANT** (Argatroban, Bivalirudin, Fondaparinux, DOAC)
- [ ] Avoid: **Warfarin alone** (warfarin-induced skin necrosis), **Platelet transfusion** (unless life-threatening bleed), **LMWH** (cross-reactivity)
- [ ] Monitor: Platelet count recovery, transition to VKA/DOAC after platelet recovery >150

---

## 📖 Definition & Pathophysiology

```mermaid
flowchart TD
    A[Heparin (UFH/LMWH)] --> B[PF4 (Platelet Factor 4) Release from Platelets]
    B --> C[PF4/Heparin Complex Formation]
    C --> D[Anti-PF4/Heparin IgG Antibody Formation]
    D --> E[Immune Complex Binds FcγRIIa on Platelets]
    E --> F[Platelet Activation → Thrombin Generation]
    F --> G1[Thrombocytopenia: Platelet Consumption]
    F --> G2[Thrombosis: HITT (Arterial + Venous)]
    F --> G3[Microparticle Release → Procoagulant State]
```

| Type | Timing | Mechanism |
|------|--------|-----------|
| **HIT Type I** | **Days 1-4** | Non-immune, direct platelet aggregation; **mild, transient, benign** |
| **HIT Type II (Classic HIT)** | **Days 5-14** (typically 5-10) | **Immune-mediated (IgG anti-PF4/heparin)**; **Thrombocytopenia + Thrombosis risk** |
| **Delayed-onset HIT** | **After heparin stopped** (up to 3-4 weeks) | Antibodies persist; presents after discharge |
| **Spontaneous HIT** | **No recent heparin** | PF4 antibodies from prior exposure; rare |

> [!tip] **FCPS/MRCP**: **HIT = 4Ts score → PF4 ELISA → SRA**. **STOP HEPARIN → START Argatroban/Bivalirudin/Fondaparinux/DOAC**. **NO Warfarin alone** (skin necrosis). **NO LMWH** (cross-reactivity). **NO Platelet transfusion** (worsens thrombosis).

---

## 🔬 Diagnostic Workup – 4Ts Score

| Category | 2 Points | 1 Point | 0 Points |
|----------|----------|---------|----------|
| **Thrombocytopenia** | **Plt >20** fall >50% or nadir 10-19 | **Plt <10** or fall 30-50% or nadir <10 | Fall <30% or nadir >20 |
| **Timing** | **Days 5-10** (clear) or ≤1 day (prior exposure) | **Days 10-14** or ≤1 day (no prior exposure) | **<4 days** (no prior exposure) or **>14 days** |
| **Thrombosis** | **New thrombosis** (venous/arterial) or skin necrosis | **Progressive/recurrent** thrombosis | **None** |
| **oTher Causes** | **None apparent** | **Possible** (sepsis, DIC, drugs) | **Definite** other cause |

**4Ts Score Interpretation**:
- **≥6 = High probability** (treat empirically while testing)
- **4-5 = Intermediate** (test; treat if positive)
- **≤3 = Low** (unlikely; test if clinical suspicion)

---

## 🔬 Laboratory Testing

| Test | Sensitivity | Specificity | Role |
|------|-------------|-------------|------|
| **PF4/Heparin ELISA** | **High (~90-95%)** | Moderate (~80-90%) | **Screening** (high NPV) |
| **Serotonin Release Assay (SRA)** | **High (~95%)** | **High (>95%)** | **Confirmatory (Gold Standard)** |
| **Heparin-Induced Platelet Activation (HIPA)** | High | High | Alternative functional assay |

> [!warning] **ELISA false positives common** (PF4 antibodies without HIT) → **SRA required for confirmation**. **Do NOT delay treatment in high 4Ts while awaiting SRA**.

---

## 💊 Management

### Immediate Actions (On Suspicion)

```mermaid
flowchart TD
    A[Suspected HIT: 4Ts ≥4] --> B[**STOP ALL HEPARIN IMMEDIATELY**]
    B --> C[**START ALTERNATIVE ANTICOAGULANT**]
    C --> D1[**Argatroban** (IV, direct thrombin inhibitor, hepatic clearance)]
    C --> D2[**Bivalirudin** (IV, direct thrombin inhibitor, renal/hepatic clearance)]
    C --> D3[**Fondaparinux** (SC, anti-Xa, renal clearance - off-label for HIT)]
    C --> D4[**DOAC (Rivaroxaban/Apixaban)** - emerging, off-label]
    D1 & D2 & D3 & D4 --> E[**Monitor Platelets Daily**]
    E --> F{Plts >150×10⁹/L?}
    F -->|Yes| G[**Transition to VKA/DOAC**]
    F -->|No| H[Continue Alternative Anticoagulant]
```

### Alternative Anticoagulants

| Drug | Dose | Monitoring | Key Points |
|------|------|------------|------------|
| **Argatroban** | **2 µg/kg/min IV** (adjust to aPTT 1.5-3x) | **aPTT** (target 1.5-3x baseline) | **Hepatic clearance** (avoid in liver failure); **No renal adjust**; Short half-life (40-50 min) |
| **Bivalirudin** | **0.15-0.20 mg/kg/h IV** (adjust to aPTT) | **aPTT** / **ACT** (PCI) | **Renal + Hepatic clearance**; Short half-life (25 min); Used in PCI |
| **Fondaparinux** | **7.5 mg SC daily** (adjust for weight <50/>100, renal) | **Anti-Xa** (optional) | **Renal clearance** (avoid if CrCl <30); **Off-label for HIT**; Long half-life (17-21h) |
| **DOAC (Rivaroxaban/Apixaban)** | Rivaroxaban 15mg BD → 20mg OD; Apixaban 5mg BD | None routine | **Emerging evidence**; **Off-label**; Renal/hepatic adjust |

### What NOT to Do

| Action | Reason |
|--------|--------|
| **Continue any heparin** (UFH, LMWH, flushes) | Triggers ongoing immune activation |
| **Switch to LMWH** | **Cross-reactivity >90%** |
| **Start Warfarin alone** | **Warfarin-induced skin necrosis** (Protein C depletion before Factors II/IX/X) |
| **Platelet transfusion** | **Worsens thrombosis** (fuel for prothrombotic state) – **ONLY if life-threatening bleed** |
| **Delay alternative anticoagulation** | **Thrombosis risk highest at diagnosis** |

### Transition to Oral Anticoagulation

1. **Platelets >150×10⁹/L** (recovery)
2. **Overlap alternative anticoagulant + Warfarin/DOAC** for ≥5 days AND **INR therapeutic (2-3)** if warfarin
3. **Stop alternative anticoagulant** once therapeutic
3. **Duration**: **3 months** for HIT with thrombosis (HITT); **3 months** for isolated HIT (controversial, some 1-3 months)

---

## 🩺 Clinical Features

| Feature | Typical Presentation |
|---------|---------------------|
| **Thrombocytopenia** | **Fall >50%** from baseline; **Nadir 20-100×10⁹/L** (rarely <10) |
| **Timing** | **Days 5-10** after heparin start (or ≤1 day if prior exposure <100 days) |
| **Thrombosis (HITT)** | **Venous (DVT, PE, unusual sites: adrenal, cerebral sinus) > Arterial (limb ischaemia, stroke, MI)** |
| **Skin Necrosis** | At heparin injection sites; **warfarin-induced** if VKA started alone |
| **Adrenal Haemorrhage** | Bilateral (Waterhouse-Friderichsen-like) – venous thrombosis |
| **Systemic Reaction** | Fever, chills, hypertension, flushing (heparin flush) |

---

## 🔄 Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **Other Drug-induced Thrombocytopenia** | Quinine, vancomycin, linezolid, sulpha – **no thrombosis**, rapid recovery on stopping |
| **DIC** | **PT↑, Fibrinogen↓, D-dimer↑↑**, underlying sepsis/trauma; **HIT: normal PT/Fib** |
| **TTP** | **ADAMTS13<10%, Schistocytes**, no heparin exposure |
| **Sepsis / ICU Thrombocytopenia** | Multiple causes (DIC, drugs, consumption); **4Ts helps differentiate** |
| **Heparin-associated Thrombocytopenia (HAT)** | **Type I**: Days 1-4, mild, non-immune, benign; **recovers on heparin** |

---

## 💡 FCPS/MRCP High-Yield Summary

| Topic | Key Point |
|-------|-----------|
| **Definition** | **Anti-PF4/heparin IgG** → platelet activation → **Thrombocytopenia + Thrombosis** |
| **4Ts Score** | **Thrombocytopenia, Timing, Thrombosis, oTher** → **≥6 High, 4-5 Intermediate, ≤3 Low** |
| **Diagnosis** | **PF4/Heparin ELISA (screen)** → **SRA (confirm)** |
| **Immediate Action** | **STOP ALL HEPARIN** → **START Argatroban/Bivalirudin/Fondaparinux/DOAC** |
| **NO Warfarin Alone** | **Warfarin-induced skin necrosis** (Protein C depletion) |
| **NO LMWH** | **Cross-reactivity >90%** |
| **NO Platelet Transfusion** | **Worsens thrombosis** (unless life-threatening bleed) |
| **Transition** | **Plts >150** → overlap Warfarin/DOAC ≥5 days + INR 2-3 |
| **Duration** | **3 months** anticoagulation |
| **Skin Necrosis** | Warfarin-induced (if VKA started alone) or heparin injection sites |

---

## ❓ Viva Questions

1. **What is the 4Ts score and how is it used?**
   - **Thrombocytopenia, Timing, Thrombosis, oTher causes** – pre-test probability; **≥6 High, 4-5 Intermediate, ≤3 Low**

2. **What is the diagnostic algorithm for HIT?**
   - **4Ts → PF4/Heparin ELISA (screen) → SRA (confirm)**; **Treat empirically if High 4Ts**

3. **Why must you stop ALL heparin immediately in suspected HIT?**
   - Heparin continues to form PF4/heparin complexes → ongoing antibody-mediated platelet activation → thrombosis

4. **Why is warfarin alone contraindicated in acute HIT?**
   - **Warfarin depletes Protein C (short half-life) before Factors II/IX/X** → transient hypercoagulable state → **warfarin-induced skin necrosis**

5. **Why is LMWH contraindicated in HIT?**
   - **Cross-reactivity >90%** with anti-PF4/heparin antibodies

6. **What are the alternative anticoagulants for HIT and their monitoring?**
   - **Argatroban (aPTT, hepatic)**; **Bivalirudin (aPTT/ACT, renal+hepatic)**; **Fondaparinux (anti-Xa, renal)**; **DOACs (emerging)**

7. **When can you transition to warfarin/DOAC in HIT?**
   - **Platelets >150×10⁹/L** (recovery); **Overlap ≥5 days + INR 2-3** (if warfarin)

8. **Why is platelet transfusion avoided in HIT?**
   - **Fuels prothrombotic state** → worsens thrombosis; **ONLY for life-threatening bleeding**

9. **What is the typical timing of HIT onset?**
   - **Days 5-10** after heparin start (or ≤1 day if prior heparin exposure within 100 days)

10. **Differentiate HIT from DIC and TTP.**
    - **HIT: Normal PT/Fibrinogen, PF4 Ab+, Thrombosis**; **DIC: PT↑, Fib↓, D-dimer↑↑, Trigger**; **TTP: ADAMTS13<10%, Schistocytes**

---

## 🧠 Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **HIT Type I vs II** | **Type I: Days 1-4, mild, non-immune, benign**; **Type II: Days 5-14, immune, thrombosis** |
| **HIT vs Other Drug ITP** | **HIT = Thrombosis + PF4 Ab**; **Drug ITP = Bleeding only, no PF4 Ab** |
| **Warfarin in HIT** | **NEVER alone** – must overlap with alternative anticoagulant until platelets recover |
| **Platelet Transfusion** | **Contraindicated** (worsens thrombosis) – only for life-threatening bleed |
| **LMWH in HIT** | **Cross-reacts** – contraindicated |

| Mnemonic | Meaning |
|----------|---------|
| **"4Ts = Thrombocytopenia, Timing, Thrombosis, oTher"** | Pre-test probability |
| **"STOP Heparin, START Argatroban/Bivalirudin/Fondaparinux"** | Immediate management |
| **"NO Warfarin Alone, NO LMWH, NO Platelets"** | Contraindications |
| **"HIT = PF4/Heperin Ab = SRA Confirms"** | Diagnosis |
| **"Plts >150 = Transition to Warfarin/DOAC"** | Transition timing |
| **"Skin Necrosis = Warfarin Alone = Protein C Depletion"** | Warfarin complication |

---

## 🗺️ Mind Map

```mermaid
mindmap
  root((Heparin-Induced Thrombocytopenia))
    Pathophysiology
      Heparin + PF4 → Complex
      Anti-PF4/Heparin IgG
      FcγRIIa → Platelet Activation
      Thrombin Generation
    Clinical
      Thrombocytopenia (Fall >50%)
      Timing: Days 5-10
      Thrombosis (HITT): Venous > Arterial
      Skin Necrosis
    Diagnosis
      4Ts Score
      PF4/Heperin ELISA (Screen)
      SRA (Gold Standard Confirm)
    Management
      STOP ALL HEPARIN
      START: Argatroban / Bivalirudin / Fondaparinux / DOAC
      NO Warfarin Alone
      NO LMWH
      NO Platelet Transfusion
      Plts >150 → Transition to VKA/DOAC
    Duration
      3 Months Anticoagulation
```

---

## 📋 One-Page Revision Card

| **HIT – FCPS/MRCP REVISION CARD** |
|-------------------------------------|
| **Mechanism**: **Anti-PF4/Heparin IgG** → Platelet activation → Thrombocytopenia + Thrombosis |
| **4Ts Score**: **Thrombocytopenia, Timing, Thrombosis, oTher** → **≥6 High, 4-5 Int, ≤3 Low** |
| **Diagnosis**: **PF4/Heparin ELISA (Screen)** → **SRA (Confirm)** |
| **IMMEDIATE**: **STOP ALL HEPARIN** → **START Argatroban/Bivalirudin/Fondaparinux/DOAC** |
| **CONTRAINDICATED**: **Warfarin alone** (skin necrosis), **LMWH** (cross-reactivity), **Platelet Tx** (worsens thrombosis) |
| **Alternative Anticoagulants**: Argatroban (aPTT, hepatic), Bivalirudin (aPTT, renal+hepatic), Fondaparinux (anti-Xa, renal), DOACs |
| **Transition**: **Plts >150** → Overlap VKA/DOAC ≥5 days + INR 2-3 |
| **Duration**: **3 Months** anticoagulation |
| **Skin Necrosis**: Warfarin alone (Protein C depletion) or heparin injection sites |

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
| **Must Know** | 4Ts score, PF4 ELISA/SRA, STOP heparin → START alternative, NO warfarin alone, NO LMWH, NO platelets, argatroban/bivalirudin/fondaparinux, transition at Plts>150, 3-month duration, HIT vs DIC vs TTP |
| **Should Know** | Argatroban hepatic vs bivalirudin renal clearance, fondaparinux renal dosing, DOAC emerging evidence, delayed-onset/spontaneous HIT, heparin flush prophylaxis, HIT in pregnancy (argatroban/fondaparinux), fondaparinux off-label, SRA methodology, warfarin overlap duration |
| **Nice to Know** | PF4/heparin complex structure, FcγRIIa polymorphism (H131R) risk, fondaparinux HIT incidence (rare), danaparoid (historical, unavailable), heparin cessation alone (insufficient), HIT in cardiac surgery (CPB), bovine vs porcine heparin, anti-PF4 IgA/IgM significance, post-HIT heparin re-exposure |

---

## ✅ Self-Test Scorecard

| Section | Score (0-10) | Notes |
|---------|--------------|-------|
| 4Ts Score & Pre-test Probability | | |
| Diagnostic Algorithm | | |
| Immediate Management | | |
| Alternative Anticoagulants | | |
| Contraindications & Avoidance | | |
| Transition & Duration | | |
| Viva Questions | | |

---

## 🔗 Local Navigation

- **Previous**: [[DIC]]
- **Next**: [[Antiphospholipid Syndrome]]
- **Section Hub**: [[Bleeding and Thrombotic Disorders]]
- **MOC**: [[Hematology MOC]]
- **Template**: [[../Templates/Hematology Topic Template]]

---

*Generated for FCPS/MRCP exam preparation. Based on Davidson Medicine 24th Ed Chapter 25.*
---

> Auto-generated study sections for "Hematology" — Ch 24: Haematology & Transfusion Medicine.

## Flashcards (13 generated)

- Q: What is the definition of Hematology?
  A: [!info] Davidson Ch 25 Alignment: Bleeding and Thrombotic Disorders → Platelet Disorders → HIT
- Q: What is Thrombocytopenia of Hematology?
  A: Fall >50% from baseline; Nadir 20-100×10⁹/L (rarely <10)
- Q: What is Timing of Hematology?
  A: Days 5-10 after heparin start (or ≤1 day if prior exposure <100 days)
- Q: What is Thrombosis (HITT) of Hematology?
  A: Venous (DVT, PE, unusual sites: adrenal, cerebral sinus) > Arterial (limb ischaemia, stroke, MI)
- Q: What is Skin Necrosis of Hematology?
  A: At heparin injection sites; warfarin-induced if VKA started alone
- Q: What is Adrenal Haemorrhage of Hematology?
  A: Bilateral (Waterhouse-Friderichsen-like) – venous thrombosis
- Q: What is Systemic Reaction of Hematology?
  A: Fever, chills, hypertension, flushing (heparin flush)
- Q: What is Thrombocytopenia of Hematology?
  A: Fall >50% from baseline; Nadir 20-100×10⁹/L (rarely <10)
- Q: What is Timing of Hematology?
  A: Days 5-10 after heparin start (or ≤1 day if prior exposure <100 days)
- Q: What is Thrombosis (HITT) of Hematology?
  A: Venous (DVT, PE, unusual sites: adrenal, cerebral sinus) > Arterial (limb ischaemia, stroke, MI)
- Q: What is Skin Necrosis of Hematology?
  A: At heparin injection sites; warfarin-induced if VKA started alone
- Q: What is Adrenal Haemorrhage of Hematology?
  A: Bilateral (Waterhouse-Friderichsen-like) – venous thrombosis
- Q: What is Systemic Reaction of Hematology?
  A: Fever, chills, hypertension, flushing (heparin flush)

## MCQs (1 generated)

1. **Which of the following best describes Hematology?**
   A. **[!info] Davidson Ch 25 Alignment: Bleeding and Thrombotic Disorders → Platelet Disorders → HIT**
   B. An unrelated condition not matching the clinical picture of Hematology
   C. A complication seen late in the disease course of Hematology
   D. A condition that mimics Hematology but has a different underlying cause

## SBA Questions (1 generated)

1. A patient with suspected Hematology presents with: A[Heparin (UFH/LMWH)] --> B[PF4 (Platelet Factor 4) Release from Platelets]; B --> C[PF4/Heparin Complex Formation]; C --> D[Anti-PF4/Heparin IgG Antibody Formation]. What is the most likely diagnosis?
   A. **Hematology**
   B. A condition that mimics Hematology but is not the same entity
   C. A complication of Hematology rather than the primary diagnosis
   D. An unrelated condition in the same clinical category as Hematology

## PasTest Scenario SBAs (Clinical Vignettes)

> **Auto-generated PasTest/Mediscope-style scenario SBAs** grounded in the authored source content. Each scenario is a clinical vignette with 4 options. **Source: Ch 24: Haematology / HIT**

**Q1.** A patient is diagnosed with HIT. What is the most appropriate first-line management approach?

  - **A.** Standard guideline-directed first-line therapy
  - **B.** Most aggressive advanced therapy as first-line
  - **C.** No treatment needed in most cases
  - **D.** Investigational/compassionate-use therapy only

  > **Answer: A** — Standard guideline-directed first-line therapy

**Q2.** Which of the following best describes the underlying pathophysiology / definition of HIT?

  - **A.** A[Heparin (UFH/LMWH)] --> B[PF4 (Platelet Factor 4) Release from Platelets]
  - **B.** A common misattribution to a similar but distinct condition
  - **C.** An outdated or disproven mechanism
  - **D.** A complication rather than the underlying disease process

  > **Answer: A** — A[Heparin (UFH/LMWH)] --> B[PF4 (Platelet Factor 4) Release from Platelets]

