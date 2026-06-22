---
tags: [medicine, davidson, hematology, ttp, hus, tmA, microangiopathic, fcps, mrcp]
davidson_chapter: Chapter 25: Haematology and Transfusion Medicine
status: full-fcps-mrcp-note
priority: high
exam_relevance: "FCPS: Essential | MRCP: Core | ADAMTS13, plasma exchange, caplacizumab, complement, STEC, pregnancy"
see_also: "[[Haemolytic Anaemias]], [[DIC]], [[HIT]], [[PNH]], [[Eculizumab]], [[Caplacizumab]]"
created: 2025-06-16
modified: 2025-06-16
---

# Thrombotic Thrombocytopenic Purpura (TTP) & Haemolytic Uraemic Syndrome (HUS)

> [!info] **Davidson Ch 25 Alignment**: Haemolytic Anaemias → Microangiopathic Haemolytic Anaemias (MAHA) → TTP/HUS
> **FCPS/MRCP Focus**: ADAMTS13 deficiency, plasma exchange, caplacizumab, STEC-HUS, complement-mediated HUS (aHUS), eculizumab, pregnancy

---

## 🎯 Learning Objectives

- [ ] Define **TMA**: Microangiopathic haemolytic anaemia (MAHA) + thrombocytopenia + organ dysfunction
- [ ] Differentiate **TTP** (ADAMTS13 <10%) from **HUS** (STEC / complement-mediated)
- [ ] Diagnose: **Schistocytes**, **ADAMTS13 activity**, **STEC PCR/culture**, **Complement studies**
- [ ] Manage **TTP**: **Emergency Plasma Exchange (PEX) + Corticosteroids + Caplacizumab + Rituximab**
- [ ] Manage **STEC-HUS**: **Supportive (NO PEX, NO antibiotics/antimotility)**; dialysis if needed
- [ ] Manage **aHUS**: **Eculizumab/Ravulizumab** (anti-C5); complement genetics
- [ ] Recognise **pregnancy-associated TMA**: TTP, HELLP, AFLP, aHUS – multidisciplinary

---

## 📖 Classification of TMA

| Type | Pathophysiology | Key Features |
|------|-----------------|--------------|
| **Immune TTP (iTTP)** | **Anti-ADAMTS13 autoantibodies** → ADAMTS13 <10% | **Acquired**, adult, female predominance, relapse common |
| **Congenital TTP (cTTP / Upshaw-Schulman)** | **ADAMTS13 gene mutation** (autosomal recessive) | **Childhood onset**, family history, recurrent |
| **STEC-HUS (Typical HUS)** | **Shiga toxin** (E. coli O157:H7) → endothelial damage | **Children**, diarrhoea (bloody), **NO PEX**, supportive |
| **Complement-mediated HUS (aHUS)** | **Complement dysregulation** (CFH, CFI, MCP, C3, CFB, THBD, DGKE mutations) | **Atypical**, any age, **eculizumab**, genetic testing |
| **Secondary TMA** | Drugs (ticlopidine, clopidogrel, quinine, chemo), Malignancy, Transplant, Pregnancy, Autoimmune (SLE, APS) | Treat underlying; PEX for drug-induced TTP-like |

> [!tip] **FCPS/MRCP**: **TTP = ADAMTS13 <10% → PEX EMERGENCY**. **STEC-HUS = Shiga toxin, GI prodrome, supportive only**. **aHUS = Complement mutation → Eculizumab**. **Pentad: MAHA, Thrombocytopenia, Neurological, Renal, Fever**.

---

## ⚙️ Pathophysiology

```mermaid
flowchart TD
    A[Endothelial Injury] --> B[ULVWF Multimer Release]
    B --> C{ADAMTS13 Activity}
    C -->|**<10% (TTP)**| D[Uncleaved ULVWF → Platelet Strings → Microthrombi]
    C -->|Normal (HUS)| E1[Shiga Toxin (STEC) → Direct Endothelial Damage]
    C -->|Normal (aHUS)| E2[Complement Dysregulation → Alternative Pathway Overactivation]
    D & E1 & E2 --> F[Microvascular Thrombosis]
    F --> G[**MAHA: Schistocytes** (mechanical RBC fragmentation)]
    F --> H[**Thrombocytopenia** (platelet consumption)]
    F --> I[Organ Ischaemia: Brain, Kidney, Heart, GI, Pancreas]
```

---

## 🔬 Diagnostic Workup

```mermaid
flowchart TD
    A[MAHA + Thrombocytopenia] --> B[**Schistocytes on Film** (Helmet cells, Burr cells)]
    B --> C[**ADAMTS13 Activity Assay** (Send BEFORE PEX)]
    C --> D{ADAMTS13 <10%?}
    D -->|Yes| E[**TTP (Immune vs Congenital)**]
    D -->|No| F[**HUS / Other TMA**]
    E --> G[**Anti-ADAMTS13 Antibody**]
    F --> H[**Stool Culture/PCR for STEC** (O157:H7)]
    F --> I[**Complement Studies** (C3, C4, CFH, CFI, MCP, C3, CFB, Genetic Panel)]
    F --> J[**Drug History** (Ticlopidine, Clopidogrel, Quinine, Chemo)]
    F --> K[**Pregnancy Test** (HELLP, AFLP, TTP, aHUS)]
    F --> L[**HIV, Malignancy, Transplant, SLE/APS Screen**]
```

### Key Investigations

| Test | TTP | STEC-HUS | aHUS |
|------|-----|----------|------|
| **ADAMTS13 Activity** | **<10% (Severe deficiency)** | Normal/mildly reduced | Normal/mildly reduced |
| **Anti-ADAMTS13 Ab** | **Positive (iTTP)** | Negative | Negative |
| **STEC PCR/Culture** | Negative | **Positive (O157:H7)** | Negative |
| **Complement (C3/C4)** | Normal | Normal | **C3↓, C4 normal** |
| **Complement Genetics** | Not routine | Not routine | **CFH, CFI, MCP, C3, CFB, THBD, DGKE** |
| **Shiga Toxin ELISA** | Negative | **Positive** | Negative |

---

## 💊 Management

### Immune TTP (iTTP) – **MEDICAL EMERGENCY**

```mermaid
flowchart TD
    A[Suspected TTP: MAHA + Thrombocytopenia + Neuro/Renal] --> B[**START PEX IMMEDIATELY** (Do NOT wait for ADAMTS13)]
    B --> C[**High-dose Corticosteroids** (Methylprednisolone 1g IV × 3d → Pred 1mg/kg)]
    C --> D[**Caplacizumab 10 mg IV** (with PEX) → 10 mg SC daily × 30d post-PEX]
    D --> E[**Rituximab 375 mg/m² weekly × 4** (early, reduces relapse)]
    E --> F[Daily CBC, ADAMTS13 monitoring, LDH, Renal, Neuro]
    F --> G{Platelets >150 × 2 consecutive days?}
    G -->|Yes| H[Taper PEX → Stop PEX → Continue Caplacizumab 30d total]
    G -->|No| I[Continue PEX Daily]
```

| Component | Details |
|-----------|---------|
| **Plasma Exchange (PEX)** | **1-1.5 plasma volumes daily** until platelets >150 × 2 days; **FFP replacement** |
| **Corticosteroids** | **Methylprednisolone 1g IV × 3 days** → Prednisolone 1 mg/kg → taper over weeks |
| **Caplacizumab** | **Anti-vWF nanobody**; 10 mg IV with PEX → 10 mg SC daily; **continue 30 days after last PEX** |
| **Rituximab** | **375 mg/m² weekly × 4**; **early use reduces relapse rate** from 30-50% to <10% |
| **Refractory TTP** | **Bortezomib**, **Cyclophosphamide**, **Splenectomy** (historical), **Daratumumab** |

> [!warning] **NEVER DELAY PEX** for ADAMTS13 result. **CBC daily**. **Caplacizumab + PEX + Steroids + Rituximab = modern standard**.

### Congenital TTP (cTTP)
- **Plasma infusion (10-20 mL/kg q2-3wk)** prophylactically; **PEX for acute episodes**
- **Recombinant ADAMTS13 (rADAMTS13 - TAK-755)** emerging therapy

### STEC-HUS (Typical HUS)
| Management | Key Points |
|------------|------------|
| **Supportive Care** | **Hydration**, **electrolytes**, **renal replacement** if AKI |
| **NO Plasma Exchange** | **NOT BENEFICIAL** (may worsen) |
| **NO Antibiotics** | **May increase Shiga toxin release** (controversial) |
| **NO Antimotility Agents** | **Contraindicated** (prolongs toxin exposure) |
| **Eculizumab** | **Not routinely recommended** (except severe neurological) |

### Atypical HUS (aHUS) – Complement-Mediated
| Treatment | Details |
|-----------|---------|
| **Eculizumab** | **900 mg weekly × 4 → 1200 mg q2wk**; **Meningococcal vaccine 2wks before** |
| **Ravulizumab** | **Weight-based LD → q8wk**; same vaccine/prophylaxis |
| **Genetic Testing** | **CFH, CFI, MCP (CD46), C3, CFB, THBD, DGKE**; guides duration (lifelong if mutation) |
| **Plasma Exchange** | **Bridge to eculizumab** if delay; not definitive |

---

## 🤰 Pregnancy-Associated TMA

| Condition | Features | Management |
|-----------|----------|------------|
| **TTP in Pregnancy** | ADAMTS13 <10%, any trimester → **PEX + Steroids + Caplacizumab** | **Caplacizumab safe in pregnancy** (no placental transfer); Rituximab avoid |
| **HELLP Syndrome** | Haemolysis, Elevated Liver enzymes, Low Platelets; **3rd trimester**, HTN/proteinuria | **Delivery** (definitive); supportive |
| **Acute Fatty Liver of Pregnancy (AFLP)** | Microvesicular steatosis, hypoglycaemia, coagulopathy, **3rd trimester** | **Urgent delivery**; supportive |
| **aHUS in Pregnancy** | Complement mutation; **Eculizumab safe** (continue) | **Multidisciplinary**; delivery planning |

---

## 🔄 Differential Diagnosis

| Condition | Key Differentiators |
|-----------|---------------------|
| **DIC** | **PT/APTT↑, Fibrinogen↓, D-dimer↑↑**, underlying sepsis/malignancy/obstetric |
| **HIT** | **Heparin exposure 5-14d**, **PF4/heparin Ab+**, thrombosis, **no schistocytes** (usually) |
| **PNH** | **Flow CD55/CD59-**, haemoglobinuria, **no thrombocytopenia** (initially) |
| **Malignant Hypertension** | **BP >180/120**, retinopathy, renal failure, MAHA |
| **Scleroderma Renal Crisis** | **Scleroderma**, **HTN**, **renal failure**, MAHA, **ACEi urgent** |
| **Drug-induced TMA** | **Ticlopidine, clopidogrel, quinine, chemo, gemcitabine** → stop drug, PEX if TTP-like |

---

## 💡 FCPS/MRCP High-Yield Summary

| Topic | Key Point |
|-------|-----------|
| **TTP Pentad** | MAHA, Thrombocytopenia, Neuro, Renal, Fever (classic but incomplete at presentation) |
| **TTP Diagnostic** | **ADAMTS13 <10%**; **Anti-ADAMTS13 Ab+ (immune)** |
| **TTP Treatment** | **PEX + Methylprednisolone 1g IV × 3d + Caplacizumab + Rituximab** (all ASAP) |
| **Caplacizumab** | **Anti-vWF**; 10 mg IV with PEX → 10 mg SC daily × 30d post-PEX |
| **STEC-HUS** | **O157:H7**, bloody diarrhoea, **children**, **Supportive ONLY (NO PEX)** |
| **aHUS** | **Complement mutation (CFH, CFI, MCP, C3...)**, **Eculizumab/Ravulizumab** |
| **Pregnancy TMA** | **TTP: PEX safe; HELLP: Delivery; AFLP: Delivery; aHUS: Eculizumab safe** |
| **DIC vs TTP** | **DIC: PT/APTT↑, Fibrinogen↓, D-dimer↑**; **TTP: Normal coagulation** |
| **HIT vs TTP** | **HIT: Heparin 5-14d, PF4 Ab+, thrombosis**; **TTP: ADAMTS13<10%** |

---

## ❓ Viva Questions

1. **What is the diagnostic hallmark of TTP?**
   - **ADAMTS13 activity <10%** (severe deficiency)

2. **Why is Plasma Exchange the emergency treatment for TTP?**
   - **Removes anti-ADAMTS13 antibodies + replenishes ADAMTS13**; reverses microthrombi formation

3. **What is the role of Caplacizumab in TTP?**
   - **Anti-vWF nanobody**; prevents platelet adhesion to ULVWF; **10 mg IV with PEX → 10 mg SC daily × 30 days post-PEX**

4. **Why is Rituximab given early in TTP?**
   - **Reduces relapse rate** from 30-50% to <10% by depleting anti-ADAMTS13 antibody-producing B-cells

5. **How does STEC-HUS differ from TTP in management?**
   - **STEC-HUS: SUPPORTIVE ONLY**; **NO PEX**, **NO antibiotics** (↑ toxin), **NO antimotility**

6. **What complement mutations cause atypical HUS (aHUS)?**
   - **CFH, CFI, MCP (CD46), C3, CFB, THBD, DGKE** (loss-of-function in regulators, gain-of-function in activators)

7. **What is the treatment for aHUS?**
   - **Eculizumab/Ravulizumab (anti-C5)**; **Meningococcal vaccine 2wks before**

8. **How do you differentiate DIC from TTP?**
   - **DIC: PT/APTT↑, Fibrinogen↓, D-dimer↑↑, underlying cause**; **TTP: Normal PT/APTT/Fibrinogen/D-dimer, ADAMTS13<10%**

9. **What is the management of TTP in pregnancy?**
   - **PEX + Steroids + Caplacizumab** (safe); **Avoid Rituximab**; multidisciplinary

10. **Why are antibiotics contraindicated in STEC-HUS?**
    - **May induce Shiga toxin release** (SOS response) → worsened outcome

---

## 🧠 Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **TTP vs STEC-HUS** | **TTP = ADAMTS13<10% → PEX**; **STEC-HUS = Shiga toxin → Supportive only** |
| **TTP vs DIC** | **TTP = Normal coagulation**; **DIC = Abnormal PT/APTT/Fibrinogen/D-dimer** |
| **TTP vs aHUS** | **TTP = ADAMTS13<10%**; **aHUS = Normal ADAMTS13 + Complement mutation** |
| **Caplacizumab** | **Anti-vWF**, **NOT anti-ADAMTS13**; adjunct to PEX |
| **PEX in STEC-HUS** | **CONTRAINDICATED/NOT BENEFICIAL** |

| Mnemonic | Meaning |
|----------|---------|
| **"TTP = ADAMTS13 <10 = PEX STAT"** | Emergency management |
| **"CAP = Caplacizumab = Anti-vWF"** | Mechanism |
| **"RITUX = Relapse Reduction"** | Early rituximab |
| **"STEC = Supportive, NO PEX"** | HUS management |
| **"aHUS = Complement = Eculizumab"** | aHUS treatment |
| **"HELLP = Delivery; AFLP = Delivery"** | Pregnancy TMA |

---

## 🗺️ Mind Map

```mermaid
mindmap
  root((TMA: TTP/HUS))
    TTP
      ADAMTS13 <10%
      Immune (Ab+) vs Congenital
      PEX + Steroids + Caplacizumab + Rituximab
      Relapse: Rituximab early
    STEC-HUS
      O157:H7 Shiga Toxin
      Bloody Diarrhoea
      Children
      SUPPORTIVE ONLY (No PEX)
    aHUS
      Complement Mutation (CFH, CFI, MCP...)
      Eculizumab / Ravulizumab
      Genetic Testing
    Pregnancy
      TTP: PEX + Caplacizumab
      HELLP/AFLP: Delivery
      aHUS: Eculizumab Continue
    Differential
      DIC: Coagulopathy
      HIT: Heparin + PF4 Ab
      PNH: Flow CD55/59-
      Malignant HTN: BP
```

---

## 📋 One-Page Revision Card

| **TTP/HUS – FCPS/MRCP REVISION CARD** |
|----------------------------------------|
| **TTP**: **ADAMTS13 <10%** → **PEX + Methylpred 1g IV ×3d + Caplacizumab + Rituximab** |
| **Caplacizumab**: **Anti-vWF**, 10mg IV/PEX → 10mg SC daily ×30d post-PEX |
| **STEC-HUS**: **O157:H7**, bloody diarrhoea → **Supportive ONLY (NO PEX, NO Abx)** |
| **aHUS**: **Complement mutation** (CFH, CFI, MCP, C3...) → **Eculizumab/Ravulizumab** |
| **Pentad**: MAHA, Thrombocytopenia, Neuro, Renal, Fever |
| **DIC vs TTP**: **DIC = PT↑ APTT↑ Fib↓ D-dimer↑**; **TTP = Normal coagulation** |
| **HIT vs TTP**: **HIT = Heparin 5-14d + PF4 Ab+**; **TTP = ADAMTS13<10%** |
| **Pregnancy TTP**: PEX + Caplacizumab (safe); **No Rituximab** |
| **HELLP/AFLP**: **Delivery definitive** |
| **ADAMTS13 Assay**: **SEND BEFORE PEX** (but don't delay PEX) |

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
| **Must Know** | ADAMTS13<10% = TTP, PEX emergency, caplacizumab + steroids + rituximab, STEC-HUS supportive only, aHUS = eculizumab, DIC vs TTP coagulation, HIT vs TTP, pregnancy management |
| **Should Know** | Caplacizumab dosing details, rituximab timing, congenital TTP (plasma infusion), STEC-HUS antibiotics controversy, aHUS genetics (CFH, CFI, MCP, C3, CFB), cTTP recombinant ADAMTS13, PEX replacement fluid (FFP), caplacizumab pregnancy safety |
| **Nice to Know** | ADAMTS13 structure/function, ULVWF multimer biology, caplacizumab clinical trials (HERCULES, TITAN), iptacopan (factor B inhibitor) in aHUS, plasminogen activation in TTP, long-term TTP outcomes (cognitive, depression), TTP registry data |

---

## ✅ Self-Test Scorecard

| Section | Score (0-10) | Notes |
|---------|--------------|-------|
| TTP Pathophysiology & Diagnosis | | |
| TTP Acute Management (PEX + Capla + Ritu) | | |
| STEC-HUS vs aHUS | | |
| Pregnancy-Associated TMA | | |
| Differential Diagnosis (DIC, HIT, PNH) | | |
| Viva Questions | | |

---

## 🔗 Local Navigation

- **Previous**: [[PNH]]
- **Next**: [[Polycythaemia Vera]]
- **Section Hub**: [[Anaemia and Red Cell Disorders]] / [[Bleeding and Thrombotic Disorders]]
- **MOC**: [[Hematology MOC]]
- **Template**: [[../Templates/Hematology Topic Template]]

---

*Generated for FCPS/MRCP exam preparation. Based on Davidson Medicine 24th Ed Chapter 25.*
---

> Auto-generated study sections for "Hematology" — Ch 24: Haematology & Transfusion Medicine.

## Flashcards (18 generated)

- Q: What is the definition of Hematology?
  A: # Thrombotic Thrombocytopenic Purpura (TTP) & Haemolytic Uraemic Syndrome (HUS)
- Q: What is Eculizumab of Hematology?
  A: 900 mg weekly × 4 → 1200 mg q2wk; Meningococcal vaccine 2wks before
- Q: What is Ravulizumab of Hematology?
  A: Weight-based LD → q8wk; same vaccine/prophylaxis
- Q: What is the investigation of choice for Hematology?
  A: CFH, CFI, MCP (CD46), C3, CFB, THBD, DGKE; guides duration (lifelong if mutation)
- Q: What is Plasma Exchange of Hematology?
  A: Bridge to eculizumab if delay; not definitive
- Q: What is Eculizumab of Hematology?
  A: 900 mg weekly × 4 → 1200 mg q2wk; Meningococcal vaccine 2wks before
- Q: What is Ravulizumab of Hematology?
  A: Weight-based LD → q8wk; same vaccine/prophylaxis
- Q: What is the investigation of choice for Hematology?
  A: CFH, CFI, MCP (CD46), C3, CFB, THBD, DGKE; guides duration (lifelong if mutation)
- Q: What is Plasma Exchange of Hematology?
  A: Bridge to eculizumab if delay; not definitive
- Q: What is TTP Pentad of Hematology?
  A: MAHA, Thrombocytopenia, Neuro, Renal, Fever (classic but incomplete at presentation)
- Q: What is TTP Diagnostic of Hematology?
  A: ADAMTS13 <10%; Anti-ADAMTS13 Ab+ (immune)
- Q: How is Hematology managed?
  A: PEX + Methylprednisolone 1g IV × 3d + Caplacizumab + Rituximab (all ASAP)
- Q: What is Caplacizumab of Hematology?
  A: Anti-vWF; 10 mg IV with PEX → 10 mg SC daily × 30d post-PEX
- Q: What is STEC-HUS of Hematology?
  A: O157:H7, bloody diarrhoea, children, Supportive ONLY (NO PEX)
- Q: What is aHUS of Hematology?
  A: Complement mutation (CFH, CFI, MCP, C3...), Eculizumab/Ravulizumab
- Q: What is Pregnancy TMA of Hematology?
  A: TTP: PEX safe; HELLP: Delivery; AFLP: Delivery; aHUS: Eculizumab safe
- Q: What is DIC vs TTP of Hematology?
  A: DIC: PT/APTT↑, Fibrinogen↓, D-dimer↑; TTP: Normal coagulation
- Q: What is HIT vs TTP of Hematology?
  A: HIT: Heparin 5-14d, PF4 Ab+, thrombosis; TTP: ADAMTS13<10%

## MCQs (1 generated)

1. **Which of the following best describes Hematology?**
   A. **# Thrombotic Thrombocytopenic Purpura (TTP) & Haemolytic Uraemic Syndrome (HUS)**
   B. An unrelated condition not matching the clinical picture of Hematology
   C. A complication seen late in the disease course of Hematology
   D. A condition that mimics Hematology but has a different underlying cause

## SBA Questions (1 generated)

1. A patient with suspected Hematology presents with: Immune TTP (iTTP) — Anti-ADAMTS13 autoantibodies → ADAMTS13 <10%; Congenital TTP (cTTP / Upshaw-Schulman) — ADAMTS13 gene mutation (autosomal recessive); STEC-HUS (Typical HUS) — Shiga toxin (E. coli O157:H7) → endothelial damage. What is the most likely diagnosis?
   A. **Hematology**
   B. A condition that mimics Hematology but is not the same entity
   C. A complication of Hematology rather than the primary diagnosis
   D. An unrelated condition in the same clinical category as Hematology

