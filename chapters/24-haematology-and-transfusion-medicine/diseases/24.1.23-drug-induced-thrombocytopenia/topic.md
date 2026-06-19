---
tags: [medicine, davidson, hematology, drug-induced-thrombocytopenia, bleeding-disorder, fcps, mrcp]
davidson_chapter: Chapter 25: Haematology and Transfusion Medicine
status: full-fcps-mrcp-note
priority: high
exam_relevance: "FCPS: High-yield | MRCP: Core | Heparin, Quinine, Vancomycin, Linezolid, Sulfonamides, Gold, Penicillamine, mechanism, diagnosis, management"
see_also: "[[HIT]], [[ITP]], [[TTP HUS]], [[DIC]], [[Thrombocytopenia]]"
created: 2025-06-17
modified: 2025-06-17
---

# Drug-induced Thrombocytopenia

> [!info] **Davidson Ch 25 Alignment**: Bleeding and Thrombotic Disorders → Platelet Disorders → Drug-induced Thrombocytopenia
> **FCPS/MRCP Focus**: Common causative drugs, mechanisms (immune vs non-immune), diagnosis (temporal relationship, rechallenge), management (stop drug, treat bleeding)

---

## 🎯 Learning Objectives

- [ ] Define **Drug-induced Thrombocytopenia (DITP)**: Thrombocytopenia occurring 5-14 days after drug initiation, resolving after discontinuation
- [ ] Classify **Mechanisms**: **Immune** (hapten, autoantibody, immune complex) vs **Non-immune** (direct myelosuppression)
- [ ] Identify **High-risk Drugs**: **Heparin (HIT)**, **Quinine**, **Vancomycin**, **Linezolid**, **Sulfonamides**, **Gold**, **Penicillamine**, **Carbamazepine**
- [ ] Apply **Diagnosis**: Temporal relationship, Exclusion of other causes, **Rechallenge** (if safe)
- [ ] Manage: **STOP DRUG**, **Monitor platelets**, **Treat bleeding**, **Avoid rechallenge**

---

## 📖 Mechanisms & Classification

| Mechanism | Description | Examples |
|-----------|-------------|----------|
| **Immune-mediated** | Drug-dependent antibody binds platelet GP → Destruction | **Heparin (HIT), Quinine, Vancomycin, Sulfonamides, Gold, Penicillamine** |
| **Hapten** | Drug binds platelet membrane → Neoantigen → Antibody | **Penicillins, Cephalosporins** |
| **Autoantibody Induction** | Drug induces true autoantibody against platelet GP | **Gold, Penicillamine, Procainamide** |
| **Immune Complex** | Drug-antibody complex binds FcγR on platelets | **Quinine, Quinidine, Rifampicin, Stibophen** |
| **Non-immune (Myelosuppression)** | **Direct bone marrow toxicity** → Reduced platelet production | **Chemotherapy, Alcohol, Valproate, Linezolid, Ganciclovir** |

> [!tip] **Drug-induced Thrombocytopenia = Thrombocytopenia + Temporal relationship (5-14 days) + Resolution on withdrawal**. **HIT = Special category (immune + thrombosis)**.

---

## 🔬 High-risk Drugs & Mechanisms

| Drug | Mechanism | Typical Onset | Features |
|------|-----------|---------------|----------|
| **Heparin (UFH/LMWH)** | **HIT: PF4/Heparin Ab** (Type II) | **5-14 days** | Thrombosis > Bleeding |
| **Quinine/Quinidine** | **Immune complex** (Drug-Ab-FcγR) | **Hours (re-exposure); 5-10d (first)** | Severe thrombocytopenia, RBC/WBC involvement |
| **Vancomycin** | **Immune (hapten/immune complex)** | **7-14 days** | Often with fever, rash |
| **Linezolid** | **Myelosuppression** (Non-immune) | **>2 weeks** | **Reversible**, Also causes anaemia |
| **Sulfonamides (TMP-SMX)** | **Immune (hapten/immune complex)** | **5-14 days** | Often with rash, fever |
| **Gold (Auranofin)** | **Autoantibody induction** | **Months** | Also proteinuria, rash |
| **Penicillamine** | **Autoantibody induction** | **Months** | Also proteinuria, taste loss |
| **Carbamazepine** | **Aplastic / Myelosuppression** | **Weeks-Months** | Also neutropenia, aplasia risk |
| **Valproate** | **Myelosuppression** | **Dose-related** | Also tremor, weight gain |
| **Ganciclovir/Valganciclovir** | **Myelosuppression** | **2-4 weeks** | Also neutropenia |
| **Rifampicin** | **Immune complex** (Intermittent dosing) | **Hours (re-exposure)** | Also haemolysis, hepatitis |
| **Ticlopidine/Clopidogrel** | **TTP-like (ADAMTS13 inhibition)** | **1-4 weeks** | **TTP syndrome** |

---

## 🔬 Diagnostic Workup

```mermaid
flowchart TD
    A[New Thrombocytopenia] --> B[**Drug History (All: Prescription, OTC, Herbal)**]
    B --> C{**Timeline: 5-14 days after start?**}
    C -->|Yes| D[**Exclude Other Causes**]
    D --> E1[**HIT? 4Ts Score** → PF4/Heparin ELISA]
    D --> E2[**ITP?** → Exclusion]
    D --> E3[**TTP/HUS?** → ADAMTS13, Schistocytes]
    D --> E4[**DIC?** → PT, Fib, D-dimer]
    D --> E5[**Sepsis?** → Cultures]
    D --> E6[**Malignancy/Infiltration?** → BM]
    F[{All Negative}] --> G[**Probable DITP**]
    G --> H[**Stop Suspect Drug**]
    H --> I{**Plt Recovery <7-10d?**}
    I -->|Yes| J[**Confirmed DITP**]
    I -->|No| K[**Reconsider Diagnosis**]
```

### Diagnostic Criteria (George & Aster)

| Criterion | Requirement |
|-----------|-------------|
| **Temporal** | **Onset 5-14 days** after drug start (or hours if re-exposure) |
| **Response** | **Platelet recovery** within **7-10 days** of drug cessation |
| **Exclusion** | No other cause (ITP, TTP, HIT, DIC, Sepsis, Malignancy) |
| **Rechallenge** | **Recurrence** on re-exposure (if ethically feasible) |

---

## 🩺 Key Drug Profiles

### Heparin (HIT) - **Special Category**
| Aspect | Details |
|--------|---------|
| **Mechanism** | **Anti-PF4/Heparin IgG** → Platelet activation |
| **4Ts Score** | Thrombocytopenia, Timing, Thrombosis, oTher |
| **Diagnosis** | **PF4/Heparin ELISA** → **SRA** |
| **Management** | **STOP ALL Heparin** → **Argatroban/Bivalirudin/Fondaparinux/DOAC** |

### Quinine/Quinidine
| Aspect | Details |
|--------|---------|
| **Mechanism** | **Immune complex** (Drug-Ab binds FcγRIIa on platelets) |
| **Onset** | **Hours** (re-exposure); **5-10 days** (first exposure) |
| **Severity** | **Profound thrombocytopenia** (<10), Often **Pancytopenia** |
| **Management** | **STOP DRUG**, **Platelet transfusion if bleeding**, **Avoid forever** |

### Linezolid
| Aspect | Details |
|--------|---------|
| **Mechanism** | **Myelosuppression** (Mitochondrial protein synthesis inhibition) |
| **Onset** | **>2 weeks** (dose/duration dependent) |
| **Features** | **Reversible thrombocytopenia**, Also **Anaemia**, **Neutropenia** |
| **Management** | **Stop or Reduce dose**, **Platelets recover in 1-2 weeks** |

### Gold / Penicillamine
| Aspect | Details |
|--------|---------|
| **Mechanism** | **Autoantibody induction** (IgG against GPIIb/IIIa) |
| **Onset** | **Months** (Cumulative dose) |
| **Management** | **STOP DRUG**, **Platelets recover in 2-4 weeks** |

---

## 💊 Management

### General Principles

| Step | Action |
|------|--------|
| **1. STOP Suspect Drug** | **Immediately** (Do not wait for confirmation) |
| **2. Monitor Platelets** | **Daily** until recovery >50, then q2-3d |
| **3. Treat Bleeding** | **Platelet transfusion** if active bleed + Plt <50 |
| **4. Avoid Rechallenge** | **Contraindicated** (Rapid, severe recurrence) |
| **5. Substitute** | **Alternative drug** from different class |

### Platelet Transfusion in DITP

| Situation | Action |
|-----------|--------|
| **Active Bleeding** | **Transfuse** (Stop drug first) |
| **Severe Thrombocytopenia (<10) + No Bleeding** | **Consider** if high bleed risk / planned procedure |
| **Prophylactic** | **NOT routinely** (Transfused platelets also destroyed) |

---

## 🔄 Differential Diagnosis

| Condition | Differentiating Features |
|-----------|-------------------------|
| **ITP** | **Exclusion diagnosis**; No temporal drug relationship; Chronic |
| **HIT** | **Heparin 5-14d, PF4/heparin Ab+, Thrombosis > Bleeding** |
| **TTP** | **Schistocytes, ADAMTS13<10%, Neuro/Renal** |
| **DIC** | **PT↑, Fib↓, D-dimer↑↑, Underlying trigger** |
| **Sepsis** | **Fever, Positive cultures, Multiple organ involvement** |
| **Aplastic Anaemia** | **Pancytopenia, Hypocellular BM** |
| **Chemotherapy** | **Expected, Timing known, Myelosuppression** |

---

## 💡 FCPS/MRCP High-Yield Summary

| Topic | Key Point |
|-------|-----------|
| **Definition** | **Thrombocytopenia + Temporal drug relationship (5-14d) + Recovery on withdrawal** |
| **Mechanisms** | **Immune (Hapten, Autoantibody, Immune complex)** vs **Myelosuppression** |
| **Top Drugs** | **Heparin (HIT), Quinine, Vancomycin, Linezolid, Sulfonamides, Gold, Penicillamine, Rifampicin, Ticlopidine** |
| **Diagnosis** | **Temporal (5-14d)**, **Exclusion**, **Recovery on withdrawal (7-10d)** |
| **Management** | **STOP DRUG** → Monitor → Platelets if bleeding → **Avoid forever** |
| **HIT** | **Special category** → **PF4/heparin Ab, Thrombosis, STOP Heparin, Argatroban** |
| **Quinine** | **Immune complex**, Profound thrombocytopenia, **Avoid re-exposure** |
| **Linezolid** | **Myelosuppression (>2wks)**, Reversible, Also anaemia/neutropenia |
| **Rechallenge** | **CONTRAINDICATED** (Rapid, severe recurrence) |

---

## ❓ Viva Questions

1. **What is the typical time course for drug-induced thrombocytopenia?**
   - **Onset 5-14 days** after drug initiation; **Recovery within 7-10 days** of stopping drug

2. **Which drugs are most commonly associated with immune-mediated thrombocytopenia?**
   - **Heparin (HIT), Quinine, Vancomycin, Sulfonamides, Gold, Penicillamine, Rifampicin**

3. **How does Linezolid cause thrombocytopenia?**
   - **Myelosuppression** (Mitochondrial protein synthesis inhibition); **Onset >2 weeks**, Reversible on stopping

4. **What is the mechanism of Quinine-induced thrombocytopenia?**
   - **Immune complex** (Quinine-antibody binds FcγRIIa on platelets) → Platelet activation/destruction

5. **How do you diagnose drug-induced thrombocytopenia?**
   - **Temporal relationship (5-14 days)**, **Exclusion of other causes**, **Platelet recovery on drug cessation**

6. **Why is heparin-induced thrombocytopenia (HIT) managed differently?**
   - **High thrombosis risk**, Requires **alternative anticoagulant (Argatroban/Bivalirudin/Fondaparinux)**, **NO platelet transfusion**

6. **What is the management of Linezolid-induced thrombocytopenia?**
   - **Stop Linezolid** (if possible) or **Reduce dose**; Platelets recover in 1-2 weeks

7. **Can drug-induced thrombocytopenia be caused by over-the-counter drugs?**
   - **Yes** - Quinine (tonic water), Herbal supplements, NSAIDs (rare)

7. **What is the difference between immune-mediated and myelosuppressive drug-induced thrombocytopenia?**
   - **Immune: 5-14d onset, Drug-dependent Ab, Rapid recovery on stop**; **Myelosuppression: Dose/duration dependent, Gradual onset, Gradual recovery**

8. **Why is rechallenge contraindicated in drug-induced thrombocytopenia?**
   - **Rapid, severe recurrence** (Hours with immune mechanisms; Anamnestic response)

9. **How do you differentiate Drug-induced thrombocytopenia from ITP?**
   - **DITP: Clear temporal drug relationship, Recovery on withdrawal**; **ITP: No drug trigger, Chronic, Exclusion diagnosis**

10. **Which drug causes TTP-like syndrome (ADAMTS13 inhibition)?**
    - **Ticlopidine / Clopidogrel** (Also **Quinine, Ticlopidine, Cyclosporine, Mitomycin C**)

---

## 🧠 Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **DITP vs ITP** | **DITP = Temporal drug link, Recovery on stop**; **ITP = No drug, Chronic** |
| **HIT vs Other DITP** | **HIT = Thrombosis > Bleeding, PF4 Ab+, Alt Anticoag Needed** |
| **Quinine vs Heparin** | **Quinine = Immune complex, Hours on re-exposure, Pancytopenia**; **Heparin = PF4 Ab, Thrombosis** |
| **Linezolid vs Chemo** | **Linezolid = Reversible, Late (>2wks)**; **Chemo = Expected, Scheduled** |
| **Autoantibody vs Hapten** | **Autoantibody (Gold/Pen): Months, True Ab**; **Hapten (Pens): Drug on platelet = Neoantigen** |

| Mnemonic | Meaning |
|----------|---------|
| **"DITP = Drug + Time (5-14d) + Recovery on Stop"** | Definition |
| **"QUININE = Quick Immune = Hours on Re-exposure"** | Quinine kinetics |
| **"LINEZOLID = Late (2wks) = Myelosuppression"** | Linezolid timing |
| **"HIT = Heparin = Thrombosis + PF4 Ab"** | HIT special |
| **"STOP DRUG = First Step Always"** | Management |
| **"RECHALLENGE = NEVER"** | Contraindication |

---

## 🗺️ Mind Map

```mermaid
mindmap
  root((Drug-induced Thrombocytopenia))
    Definition
      Plt <100 + Drug 5-14d + Recovery on Stop
    Mechanisms
      Immune: Hapten, AutoAb, Immune Complex
      Myelosuppression: Chemo, Linezolid, Valproate
    Key Drugs
      Heparin (HIT): PF4 Ab, Thrombosis
      Quinine: Immune Complex, Hours on Re-exposure
      Vancomycin: Hapten/Immune Complex
      Linezolid: Myelosuppression (>2wks)
      Sulfonamides: Hapten/Immune Complex
      Gold/Penicillamine: AutoAb (Months)
      Rifampicin: Immune Complex (Intermittent)
      Ticlopidine/Clopidogrel: TTP-like
    Diagnosis
      Temporal (5-14d)
      Exclusion (ITP, HIT, TTP, DIC)
      Recovery on Stop (7-10d)
    Management
      STOP DRUG Immediately
      Monitor Daily
      Platelets if Bleeding
      NEVER Rechallenge
      Substitute Alternative
```

---

## 📋 One-Page Revision Card

| **DRUG-INDUCED THROMBOCYTOPENIA – FCPS/MRCP REVISION CARD** |
|---------------------------------------------------------------|
| **Definition**: **Thrombocytopenia + Drug 5-14d + Recovery on Stop** |
| **Mechanisms**: **Immune** (Hapten, AutoAb, Immune Complex) vs **Myelosuppression** |
| **Top Drugs**: **Heparin (HIT), Quinine, Vancomycin, Linezolid, Sulfonamides, Gold, Penicillamine, Rifampicin, Ticlopidine** |
| **HIT**: **PF4 Ab + Thrombosis** → **Argatroban/Bivalirudin/Fondaparinux** (NO Heparin/LMWH) |
| **Quinine**: **Immune Complex**, **Hours on Re-exposure**, **Avoid Forever** |
| **Linezolid**: **Myelosuppression** (Late >2wks), Reversible |
| **Diagnosis**: **Temporal (5-14d) + Exclusion + Recovery on Stop** |
| **Management**: **STOP DRUG → Monitor → Platelets if Bleeding → NEVER Rechallenge** |
| **Rechallenge**: **CONTRAINDICATED** (Rapid, Severe) |

---

## 📅 Spaced Repetition Tracker

| Review | Date | Score (1-5) | Next Review |
|--------|------|-------------|-------------|
| Day 1 | 2025-06-17 | | 2025-06-18 |
| Day 3 | | | |
| Day 7 | | | |
| Day 15 | | | |
| Day 30 | | | |

---

## 🎯 Must Know / Should Know / Nice to Know

| Level | Content |
|-------|---------|
| **Must Know** | Definition (temporal 5-14d + recovery), Top drugs (Heparin, Quinine, Vancomycin, Linezolid, Sulfonamides, Gold, Penicillamine), HIT special management, Diagnosis criteria, Stop drug immediately, Never rechallenge |
| **Should Know** | Mechanism details (hapten vs autoimmune vs immune complex vs myelosuppression), Quinine immune complex mechanism, Linezolid dose/duration relationship, Gold/penicillamine autoantibody induction, Rifampicin intermittent dosing effect, Ticlopidine/clopidogrel ADAMTS13 inhibition, Platelet transfusion indications in DITP |
| **Nice to Know** | Molecular mechanisms (FcγRIIa, GPIIb/IIIa, GP1b), Drug-specific antibody assays, Incidence rates, Genetic predisposition (HLA associations), Paediatric DITP, Cost-effectiveness of testing, Novel anticoagulants in HIT, Platelet transfusion refractoriness in DITP, Rituximab in refractory DITP |

---

## ✅ Self-Test Scorecard

| Section | Score (0-10) | Notes |
|---------|--------------|-------|
| Definition & Mechanisms | | |
| Key Drug Profiles (HIT, Quinine, Linezolid, etc.) | | |
| Diagnosis Criteria | | |
| Management Principles | | |
| Differential Diagnosis | | |
| Viva Questions | | |

---

## 🔗 Local Navigation

- **Previous**: [[ITP]]
- **Next**: [[Hypermethaemia]]
- **Section Hub**: [[Bleeding and Thrombotic Disorders]]
- **MOC**: [[Hematology MOC]]
- **Template**: [[../Templates/Hematology Topic Template]]

---

*Generated for FCPS/MRCP exam preparation. Based on Davidson Medicine 24th Ed Chapter 25.*