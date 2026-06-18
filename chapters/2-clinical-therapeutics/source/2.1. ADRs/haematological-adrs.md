# Haematological ADRs

**Status**: `full-fcps-mrcp-note` | **Chapter**: 2 — Clinical Therapeutics and Good Prescribing | **Heading**: Adverse Drug Reactions → System-Specific Patterns | **Exam Priority**: ⭐⭐⭐ **HIGH** (Agranulocytosis, Thrombocytopenia, HIT, Haemolysis — VIVA, emergency recognition)

---

## 1. 🎯 Learning Objectives
- [ ] Classify drug-induced haematological toxicity by cell line
- [ ] Differentiate immune vs non-immune thrombocytopenia (HIT, DITP, TTP)
- [ ] Recognise agranulocytosis — immediate management
- [ ] Identify drug-induced haemolysis (G6PD, immune, microangiopathic)
- [ ] Apply monitoring protocols (clozapine, carbamazepine, antithyroid drugs)
- [ ] Execute emergency algorithms (HIT 4Ts, agranulocytosis)

---

## 2. 📊 Classification by Cell Line

| Cell Line | Reaction | Mechanism | Key Drugs |
|-----------|----------|-----------|-----------|
| **Neutrophils** | **Agranulocytosis** (<0.5×10⁹/L) | Immune (hapten/antibody) / Direct toxicity | **Clozapine, Carbamazepine, Sulfonamides, Antithyroid (carbimazole, PTU), Ticlopidine, Chemotherapy, Valproate** |
| | Neutropenia (0.5–1.5×10⁹/L) | Dose-dependent / Idiosyncratic | Chemotherapy, G-CSF, Antibiotics, Antivirals |
| **Platelets** | **Thrombocytopenia** (<100×10⁹/L) | **Immune (DITP)**, **HIT**, TMA, Bone marrow suppression | **Heparin (HIT), Quinine, GPIIb/IIIa inhibitors, Valproate, Carbamazepine, Sulfonamides, Gold, Heparin, Chemotherapy** |
| **Red Cells** | **Haemolytic Anaemia** | **Immune (Type II)**, **G6PD deficiency** (oxidative), **Microangiopathic (TMA)** | **Penicillins (AIHA), Cephalosporins, Methyldopa, NSAIDs, Quinidine, Sulfonamides (G6PD), Dapsone, Methylene blue, Clopidogrel (TMA)** |
| | Pure Red Cell Aplasia (PRCA) | Immune / T-cell mediated | **Erythropoietin (anti-EPO antibodies), Azathioprine, Phenytoin, Carbamazepine, Isoniazid** |
| **All Lines** | **Aplastic Anaemia** | Idiosyncratic / Stem cell toxicity | **Chloramphenicol, Carbamazepine, Phenytoin, Gold, Benzene, Chemotherapy** |

---

## 3. ⚠️ Agranulocytosis — **Medical Emergency**

| Features | **Agranulocytosis** (<0.5 × 10⁹/L) | **Neutropenia** (0.5–1.5 × 10⁹/L) |
|----------|-----------------------------------|----------------------------------|
| **Risk** | Life-threatening sepsis | Infection risk ↑ |
| **Onset** | Days–weeks (immune); immediate (chemo) | Variable |
| **Presentation** | Fever, sore throat, sepsis, mouth ulcers | Often asymptomatic |
| **Immediate Action** | **STOP drug**, **IV antibiotics**, **G-CSF**, **reverse isolation**, **blood cultures** | Stop drug if severe; monitor; G-CSF if <1.0 |

### High-Risk Drugs for Agranulocytosis
| Drug | Monitoring | Risk |
|------|------------|------|
| **Clozapine** | **Mandatory**: Weekly ×18wks → fortnightly ×1yr → monthly | **~1%** risk; register; restart only if ANC>2.0 |
| **Carbamazepine** | Baseline + periodic (no formal mandate) | ~0.1%; HLA-B*15:02 screening (Asians) |
| **Antithyroid (Carbimazole/PTU)** | Patient education (sore throat → urgent FBC) | ~0.1–0.5%; no routine monitoring |
| **Sulfonamides** | Clinical vigilance | Idiosyncratic |
| **Ticlopidine** | FBC 2-weekly ×3mo | ~1%; largely replaced by clopidogrel |
| **Chemotherapy** | Protocol-driven (nadir day 7–14) | Expected; G-CSF support |

### Management Algorithm
```mermaid
flowchart TD
    A[Patient on high-risk drug presents with FEVER] --> B[**URGENT FBC + DIFFERENTIAL**]
    B --> C{ANC <0.5 × 10⁹/L?}
    C -->|YES| D[**AGRANULOCYTOSIS**<br/>**STOP DRUG IMMEDIATELY**<br/>**IV Broad-spectrum antibiotics** (Piperacillin-tazobactam / Meropenem)<br/>**G-CSF** (Filgrastim 5mcg/kg/day until ANC>1.0)<br/>**Reverse isolation**<br/>Blood/urine cultures<br/>No routine antifungals unless persistent fever>4-5d]
    C -->|ANC 0.5-1.0| E[**SEVERE NEUTROPENIA**<br/>Stop drug<br/>IV antibiotics if febrile<br/>G-CSF consideration<br/>Close monitoring]
    C -->|ANC 1.0-1.5| F[**MODERATE NEUTROPENIA**<br/>Stop drug if possible<br/>Oral antibiotics if febrile<br/>Monitor FBC 2-3x/week]
    C -->|ANC >1.5| G[**NOT NEUTROPENIC**<br/>Evaluate other causes of fever<br/>Continue drug if benefit>risk]
```

---

## 4. 🩸 Drug-Induced Thrombocytopenia (DITP) & HIT

### DITP (Non-HIT Immune Thrombocytopenia)
| Feature | DITP |
|---------|------|
| **Mechanism** | **Drug-dependent antibody** (IgG) binds platelet GPIIb/IIIa or Ib/IX → FcγR-mediated clearance |
| **Onset** | 5–14 days (first exposure); hours (re-exposure) |
| **Platelet Count** | Often **<20×10⁹/L** (severe) |
| **Key Drugs** | **Quinine/Quinidine**, Sulfonamides, **GPIIb/IIIa inhibitors (Abciximab, Eptifibatide, Tirofiban)**, Valproate, Carbamazepine, Heparin (non-HIT), Gold, Rifampicin |
| **Diagnosis** | Drug cessation → platelet recovery **within 3–7 days**; drug-dependent antibody assay (specialised) |
| **Management** | **STOP drug** → platelets recover in days; **IVIG** if bleeding/severe; **avoid re-exposure** |

### Heparin-Induced Thrombocytopenia (HIT) — **Critical**
| Feature | **HIT (Type II)** |
|---------|-------------------|
| **Mechanism** | **IgG antibody** to **PF4-heparin complex** → platelet activation → **prothrombotic state** (NOT bleeding) |
| **Onset** | **5–14 days** (UFH > LMWH > Fondaparinux) |
| **Platelet Count** | **↓ 30–50% from baseline** (rarely <20×10⁹/L); **thrombosis > bleeding** |
| **4Ts Score** (Pre-test Probability) | |
| **Thrombocytopenia** | >50% fall & nadir ≥20 = 2; 30–50% or nadir 10–19 = 1; <30% or nadir <10 = 0 |
| **Timing** | 5–10d = 2; ≤1d (prior exposure) = 1; >10d = 0 |
| **Thrombosis** | New thrombosis = 2; progressive/recurrent = 1; none = 0 |
| **Other causes** | None = 2; possible = 1; definite = 0 |
| **Score** | **4Ts ≥4 = High**; 3–4 = Intermediate; ≤2 = Low |

### HIT Management Algorithm
```mermaid
flowchart TD
    A[Suspect HIT: Thrombocytopenia 5-14d post-heparin] --> B[Calculate 4Ts Score]
    B --> C{4Ts Score}
    C -->|**Low (≤2)**| D[**HIT UNLIKELY**<br/>Continue heparin if needed<br/>Monitor platelets]
    C -->|**Intermediate (3-4)**| E[**STOP ALL HEPARIN** (UFH, LMWH, flushes)<br/>**Start non-heparin anticoagulant**:<br/>Argatroban (IV, hepatic adj) / Bivalirudin (IV, renal adj) / Fondaparinux (SC, off-label)<br/>Send **HIT antibody (PF4 ELISA)**<br/>If ELISA +ve → continue anticoagulation]
    C -->|**High (≥5)**| F[**STOP ALL HEPARIN IMMEDIATELY**<br/>**Start non-heparin anticoagulant** (Argatroban/Bivalirudin/Fondaparinux)<br/>Send HIT antibody<br/>**Do NOT wait for result**<br/>**No platelet transfusion** (unless active bleed)<br/>**No warfarin alone** (risk WISN — wait for platelet recovery >150)]
    D & E & F --> G[**Anticoagulation duration**: 3 months if thrombosis; 4–6 weeks if isolated HIT<br/>Transition to DOAC/Warfarin after platelet recovery >150]
```

### HIT vs DITP Comparison
| Feature | **HIT** | **DITP** |
|---------|---------|----------|
| **Mechanism** | PF4-heparin IgG → platelet activation | Drug-dependent IgG → platelet clearance |
| **Clinical** | **Thrombosis >> Bleeding** | **Bleeding >> Thrombosis** |
| **Platelet Count** | ↓30–50%, rarely <20 | Often **<20** |
| **Timing** | 5–14 days | 5–14 days (first); hours (re-exposure) |
| **Anticoagulation** | **Must continue** (non-heparin) | Stop drug; no anticoagulation needed |
| **Platelet Transfusion** | **Contraindicated** (unless life-threatening bleed) | OK if bleeding |
| **Warfarin** | **Delay until platelets >150** (WISN risk) | N/A |

---

## 5. 🔴 Haemolytic Anaemia

### Immune Haemolytic Anaemia (Type II)
| Type | Mechanism | Drugs | Features |
|------|-----------|-------|----------|
| **Penicillin-type** | Drug binds RBC membrane → antibody to **drug-RBC complex** | **Penicillins, Cephalosporins** | DAT **IgG + C3d** (drug-dependent); **spherocytes**; ↓ drug = recovery |
| **Methyldopa-type** | **Autoantibody** to RBC (Rh-like) — **true autoimmune** | **Methyldopa** | DAT **IgG + C3d** (no drug needed); **warm AIHA**; may persist months after stop |
| **Ternary Complex** | Drug-antibody complex binds RBC weakly | **Cephalosporins, Rifampicin** | DAT **C3d only** (IgG weak); high-titre antibody |

### G6PD Deficiency (Oxidative Haemolysis)
| Drug | Risk |
|------|------|
| **Dapsone** | **High** |
| **Sulfonamides** (TMP-SMX, sulfonylureas) | High |
| **Primaquine / Tafenoquine** | **Contraindicated** |
| **Methylene blue** | High |
| **Rasburicase** | Contraindicated |
| **High-dose Vitamin C / Nitrofurantoin** | Moderate |

### Microangiopathic Haemolytic Anaemia (MAHA/TMA)
| Drug | Context |
|------|---------|
| **Ciclosporin / Tacrolimus / Sirolimus** | Transplant (dose-dependent) |
| **Clopidogrel / Ticlopidine** | TTP-like (ADAMTS13 inhibition) |
| **Quinine** | Immune-mediated |
| **Gemcitabine / VEGF inhibitors** | Chemotherapy |
| **HIT** | PF4-heparin → thrombosis + MAHA |

---

## 6. 🎯 FCPS/MRCP High-Yield Summary

| Emergency | Key Drug | Immediate Action |
|-----------|----------|------------------|
| **Agranulocytosis + Fever** | Clozapine, Carbimazole, Carbamazepine | **STOP drug, IV antibiotics, G-CSF, reverse isolation** |
| **HIT (4Ts ≥4) + Thrombosis** | UFH, LMWH | **STOP heparin, START argatroban/bivalirudin/fondaparinux, NO warfarin alone, NO platelet transfusion** |
| **DITP + Bleeding (Platelets <10)** | Quinine, GPIIb/IIIa, Valproate | **STOP drug, IVIG 1g/kg ×2d, platelets if life-threatening bleed** |
| **G6PD Haemolysis** | Dapsone, Sulfonamides, Primaquine | **STOP drug, transfuse if severe, folic acid, avoid oxidants** |
| **Methyldopa AIHA** | Methyldopa | **STOP drug, steroids if severe, may take months to resolve** |

---

## 7. ❓ Viva Questions (12)

| Q | Answer |
|---|--------|
| 1. Define agranulocytosis. Immediate management of febrile patient on clozapine? | ANC <0.5×10⁹/L; **STOP clozapine, IV broad-spectrum antibiotics, G-CSF 5mcg/kg/day, reverse isolation, cultures** |
| 2. Clozapine monitoring schedule? | Weekly ×18wks → fortnightly ×1yr → monthly thereafter; ANC must be >1.5 (green), 1.0–1.5 (amber), <1.0 (red — stop) |
| 3. HIT vs DITP — key clinical difference? | **HIT = thrombotic (prothrombotic)**; **DITP = bleeding (thrombocytopenia)** |
| 4. 4Ts score components? Threshold for high probability? | Thrombocytopenia, Timing, Thrombosis, Other causes; **≥4 = High** |
| 5. HIT management — why NO warfarin alone? | **Warfarin-induced skin necrosis (WISN)** — protein C depletion before factor II/X; must overlap with parenteral anticoagulant until platelets >150 |
| 6. HIT — why NO platelet transfusion? | Fuels thrombosis (platelets = prothrombotic fuel) — only if life-threatening bleeding |
| 7. Penicillin-type vs Methyldopa-type immune haemolysis? | Penicillin: **drug-dependent antibody** (DAT IgG+C3d, recover on stop); Methyldopa: **true autoantibody** (DAT IgG+C3d, warm AIHA, persists after stop) |
| 8. G6PD deficiency — 3 high-risk drugs contraindicated? | **Primaquine/tafenoquine, dapsone, rasburicase**; also sulfonamides, methylene blue |
| 9. TMA — drug causes? Management of tacrolimus TMA? | CNIs (tacro/ciclo/siro), clopidogrel, quinine, gemcitabine, HIT; **Tacro TMA: ↓ dose or stop, consider sirolimus/mTOR switch** |
| 10. DITP — platelet recovery time after drug cessation? | **3–7 days** (if immune); recover quickly once antibody cleared |
| 11. Carbimazole/PTU agranulocytosis — monitoring? | **No routine FBC**; **Patient education: sore throat/fever → urgent FBC same day** |
| 12. Valproate thrombocytopenia — mechanism? Dose relationship? | **Dose-dependent** bone marrow suppression + platelet dysfunction; **>100 mcg/mL or >50mg/kg/day** ↑ risk; monitor FBC |

---

## 8. 🤯 Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **HIT = Thrombotic vs Bleeding** | HIT = **PROTHROMBOTIC** (thrombosis >> bleeding) — "HIT = Hypercoagulable" |
| **HIT vs DITP platelet count** | HIT: ↓30–50% (rarely <20); DITP: often **<20** |
| **HIT antibody = PF4-heparin** | **PF4-heparin complex** → IgG → platelet activation via FcγRIIa |
| **Methyldopa AIHA vs Penicillin AIHA** | Methyldopa = **true autoantibody** (persists); Penicillin = **drug-dependent** (recovers on stop) |
| **G6PD drugs** | **Oxidative** drugs: dapsone, sulfonamides, primaquine, methylene blue, rasburicase |
| **Clozapine agranulocytosis** | **Mandatory monitoring register**; cannot prescribe without |

**Mnemonics:**
- **"4Ts"** = **T**hrombocytopenia, **T**iming, **T**hrombosis, **T** (o)ther causes
- **"HIT = HYPERCOAGULABLE"** = **H**eparin **I**nduced **T**hrombosis (not bleeding)
- **"ARGATROBAN/BIVALIRUDIN/FONDAPARINUX"** = **HIT anticoagulants** (NO heparin, NO warfarin alone)
- **"WISN"** = **Warfarin-Induced Skin Necrosis** (start warfarin ONLY after platelets >150 in HIT)
- **"PLATELET RECOVERY 3-7 DAYS"** = DITP platelet recovery after drug stop
- **"G6PD NO-GO"** = **P**rimaquine, **D**apsone, **S**ulfonamides, **M**ethylene blue, **R**asburicase
- **"METHYLDOPA = TRUE AUTO"** = **Autoantibody** (persists after stop)
- **"PENICILLIN = DRUG-DEPENDENT"** = Antibody needs drug on RBC (recovers on stop)

---

## 9. 🧠 Mind Map (Mermaid)

```mermaid
mindmap
  root((Haematological ADRs))
    Neutrophils
      Agranulocytosis (<0.5)
        Clozapine (mandatory monitoring)
        Carbamazepine
        Antithyroid (carbimazole/PTU)
        Sulfonamides
        Ticlopidine
        Chemotherapy
      Management: STOP, IV Abx, G-CSF, isolation
    Platelets
      DITP (immune)
        Quinine, GPIIb/IIIa, Valproate, Carbamazepine, Heparin (non-HIT)
        Recovery 3-7d post stop
        IVIG if bleeding
      HIT (Type II)
        PF4-heparin IgG
        5-14d, thrombosis > bleeding
        4Ts score
        Stop heparin → Argatroban/Bivalirudin/Fondaparinux
        NO warfarin alone until platelets >150
        NO platelet transfusion
    Red Cells
      Immune Haemolysis (Type II)
        Penicillin-type: drug-dependent (recovers on stop)
        Methyldopa-type: true autoantibody (persists)
      G6PD Deficiency (oxidative)
        Dapsone, Sulfonamides, Primaquine, Methylene blue, Rasburicase
      MAHA/TMA
        CNIs (tacro/ciclo/siro), Clopidogrel, Quinine, Gemcitabine, HIT
```

---

## 10. 📅 Spaced Repetition Tracker

| Review | Date | Score | Next |
|--------|------|-------|------|
| 1 | | | 1d |
| 2 | | | 3d |
| 3 | | | 1w |
| 4 | | | 2w |
| 5 | | | 1m |
| 6 | | | 3m |

---

## 11. 🧪 Self-Test Scorecard

| Section | Max | Score |
|---------|-----|-------|
| Classification table | 8 | |
| Agranulocytosis + monitoring | 10 | |
| HIT (4Ts, management) | 12 | |
| DITP vs HIT | 8 | |
| Haemolytic anaemia types | 10 | |
| G6PD drugs | 6 | |
| Viva answers | 12 | |
| **Total** | **66** | |

**Target**: ≥53/66 (80%)

---

## 12. 📝 Exam Answer Modes

### Long Question (10 marks): *"Discuss heparin-induced thrombocytopenia (HIT) — pathophysiology, diagnosis, and management."*
1. **Pathophysiology** (2): PF4-heparin complex → IgG antibody → platelet activation via FcγRIIa → thrombin generation, prothrombotic state
2. **Diagnosis** (3): 4Ts score (Thrombocytopenia, Timing, Thrombosis, Other causes); High ≥4, Intermediate 3–4, Low ≤2; PF4 ELISA confirmation
3. **Management** (4): STOP all heparin immediately; start **non-heparin anticoagulant** (argatroban/bivalirudin/fondaparinux); **NO warfarin alone** until platelets >150 (WISN risk); **NO platelet transfusion** unless life-threatening bleed; anticoagulate 3mo if thrombosis, 4–6wk if isolated HIT
4. **HIT vs DITP** (1): HIT = thrombotic; DITP = bleeding; DITP platelet recovery 3–7 days

### Short Question (5 marks): *"HIT 4Ts Score"*
| Component | 2 Points | 1 Point | 0 Points |
|-----------|----------|---------|----------|
| **Thrombocytopenia** | >50% fall, nadir ≥20 | 30–50% fall or nadir 10–19 | <30% fall or nadir <10 |
| **Timing** | 5–10 days | ≤1 day (prior exposure) or >10 days | — |
| **Thrombosis** | New thrombosis | Progressive/recurrent | None |
| **Other causes** | None apparent | Possible | Definite |

**≥4 = High probability; 3–4 = Intermediate; ≤2 = Low**

### Viva (2 min): *"Patient on UFH 7 days, platelets 80 (baseline 250), new DVT. 4Ts? Management?"*
- **4Ts**: Thrombocytopenia 2 (>50% fall, nadir ≥20), Timing 2 (5–10d), Thrombosis 2 (new DVT), Other causes 2 (none) = **8 = HIGH**
- **STOP all heparin immediately**
- **Start argatroban (IV, hepatic adjust) or bivalirudin (IV, renal adjust) or fondaparinux (SC)**
- Send PF4 ELISA
- **NO warfarin alone** — wait for platelets >150
- **NO platelet transfusion**
- Anticoagulate 3 months (thrombosis present)

### Ward Round (30 sec): *"Patient on clozapine 3 months, temp 38.5°C. Immediate steps?"*
- **Agranulocytosis until proven otherwise**
- **URGENT FBC + differential**
- If ANC <0.5 → **STOP clozapine, IV piperacillin-tazobactam/meropenem, G-CSF 5mcg/kg, reverse isolation, cultures**

### Last-Night Revision (1-liners):
- Agranulocytosis = ANC<0.5 → STOP drug, IV Abx, G-CSF, isolation
- Clozapine: Weekly×18wk → 2wk×1yr → monthly
- Carbimazole: No routine FBC; sore throat = urgent FBC
- HIT = PF4-heparin IgG → thrombotic (not bleeding)
- 4Ts: Thrombocytopenia, Timing, Thrombosis, Other causes; ≥4 = High
- HIT management: STOP heparin → Argatroban/Bivalirudin/Fondaparinux; NO warfarin alone; NO platelet transfusion
- DITP = bleeding, platelets often <20, recovery 3–7d, IVIG if bleeding
- Penicillin AIHA = drug-dependent (recovers); Methyldopa AIHA = true auto (persists)
- G6PD: Dapsone, Sulfonamides, Primaquine, Methylene blue, Rasburicase
- TMA: CNIs, Clopidogrel, Quinine, Gemcitabine, HIT

---

## 13. 📚 Summary Card

> **HAEMATOLOGICAL EMERGENCY TRIAD:**
> 1. **AGRANULOCYTOSIS + FEVER** → **STOP drug, IV Abx, G-CSF, Isolation** (Clozapine, Carbimazole, CZP)
> 2. **HIT (4Ts ≥4)** → **STOP heparin, Argatroban/Bivalirudin, NO Warfarin alone, NO Platelets** (Thrombosis not bleeding!)
> 3. **DITP + BLEEDING** → **STOP drug, IVIG 1g/kg** (Platelets often <20, recovery 3–7d)
>
> **G6PD**: Avoid Primaquine, Dapsone, Sulfonamides, Methylene blue, Rasburicase
> **Methyldopa AIHA** = True autoantibody (persists); **Penicillin AIHA** = Drug-dependent (recovers)

---

## 14. ❓ MCQs (15)

1. **Agranulocytosis is defined as absolute neutrophil count (ANC):**
   A. <1.0 × 10⁹/L
   B. **<0.5 × 10⁹/L** ✓
   C. <1.5 × 10⁹/L
   D. <0.2 × 10⁹/L
   E. <0.1 × 10⁹/L

2. **Clozapine monitoring schedule after 1 year of treatment:**
   A. Weekly
   B. Fortnightly
   C. **Monthly** ✓
   D. Every 3 months
   E. No monitoring needed

3. **Carbimazole-induced agranulocytosis — recommended monitoring:**
   A. Weekly FBC
   B. Fortnightly FBC
   C. **No routine FBC; patient education (sore throat → urgent FBC)** ✓
   D. Monthly FBC
   E. Only if symptomatic

4. **HIT (Type II) — primary clinical manifestation:**
   A. Severe bleeding
   B. **Thrombosis (arterial and venous)** ✓
   C. Asymptomatic thrombocytopenia
   D. DIC
   E. Haemolysis

5. **4Ts score — high probability threshold:**
   A. ≥3
   B. **≥4** ✓
   C. ≥5
   D. ≥6
   E. ≥2

6. **HIT management — which is CONTRAINDICATED?**
   A. Argatroban
   B. Bivalirudin
   C. Fondaparinux
   D. **Warfarin alone (without parenteral overlap)** ✓
   E. Platelet transfusion (if life-threatening bleed)

7. **HIT — platelet transfusion is:**
   A. Routinely recommended
   B. **Contraindicated (fuels thrombosis)** ✓
   C. Required if platelets <20
   D. Required if platelets <10
   D. Only if bleeding

8. **Penicillin-type vs Methyldopa-type immune haemolysis — key difference:**
   A. Penicillin causes intravascular haemolysis only
   B. **Methyldopa produces true autoantibody (persists after stop); Penicillin is drug-dependent (recovers on stop)** ✓
   C. Methyldopa causes Coombs-negative haemolysis
   D. Penicillin causes warm AIHA only
   E. No difference

9. **G6PD deficiency — drug CONTRAINDICATED:**
   A. Dapsone
   B. **Primaquine** ✓
   C. Sulfonamides
   D. Methylene blue
   E. Nitrofurantoin

10. **DITP — platelet recovery after drug cessation:**
    A. 24–48 hours
    B. **3–7 days** ✓
    C. 2–3 weeks
    D. 1–2 months
    E. Never recovers

11. **Valproate thrombocytopenia — mechanism:**
    A. Immune-mediated platelet destruction
    B. **Dose-dependent bone marrow suppression + platelet dysfunction** ✓
    C. Heparin-induced
    D. TMA
    E. Dilutional

12. **Tacrolimus/ciclosporin — associated haematological toxicity:**
    A. Agranulocytosis
    B. **Thrombotic microangiopathy (TMA)** ✓
    C. Pure red cell aplasia
    D. Immune haemolytic anaemia
    E. Aplastic anaemia

13. **Clopidogrel-associated TMA — mechanism:**
    A. Dose-dependent endothelial injury
    B. **ADAMTS13 inhibition (immune-mediated)** ✓
    C. Complement activation
    D. Drug-dependent antibody
    E. Oxidative stress

14. **Drug-induced pure red cell aplasia (PRCA) — associated with:**
    A. Heparin
    B. **Erythropoietin (anti-EPO antibodies)** ✓
    C. Warfarin
    D. Aspirin
    E. Clopidogrel

15. **HIT antibody target:**
    A. Platelet GPIIb/IIIa
    B. **PF4-heparin complex** ✓
    C. von Willebrand factor
    D. Fibrinogen
    E. Protein C

---

## 15. 🃏 Flashcards (Anki-ready)

| Front | Back |
|-------|------|
| Agranulocytosis definition | ANC <0.5 × 10⁹/L |
| Clozapine monitoring | Weekly×18wk → Fortnightly×1yr → Monthly |
| Carbimazole agranulocytosis | No routine FBC; sore throat = urgent FBC |
| Ticlopidine monitoring | FBC 2-weekly ×3mo (largely replaced by clopidogrel) |
| HIT mechanism | PF4-heparin complex → IgG → platelet activation (FcγRIIa) → prothrombotic |
| 4Ts components | Thrombocytopenia, Timing, Thrombosis, Other causes |
| 4Ts high probability | ≥4 |
| HIT management | STOP heparin → Argatroban/Bivalirudin/Fondaparinux; NO warfarin alone; NO platelets |
| WISN | Warfarin-induced skin necrosis (protein C depletion) |
| DITP | Drug-dependent IgG → platelet clearance; recovery 3–7d; bleeding > thrombosis |
| DITP key drugs | Quinine, GPIIb/IIIa inhibitors, Valproate, Carbamazepine |
| Penicillin AIHA | Drug-dependent antibody → recovers on stop |
| Methyldopa AIHA | True autoantibody → warm AIHA, persists months |
| G6PD drugs to avoid | Primaquine, Dapsone, Sulfonamides, Methylene blue, Rasburicase |
| TMA drugs | CNIs (tacro/ciclo/siro), Clopidogrel, Quinine, Gemcitabine, HIT |
| Valproate thrombocytopenia | Dose-dependent BM suppression + platelet dysfunction |
| PRCA drugs | EPO (anti-EPO Abs), Azathioprine, Phenytoin, Carbamazepine, INH |

---

## 16. ✅ Answer Keys

### MCQs
1. **B** — ANC <0.5 × 10⁹/L
2. **C** — Monthly after 1 year
3. **C** — No routine FBC; patient education
4. **B** — HIT = thrombotic (prothrombotic)
5. **B** — 4Ts ≥4 = High
6. **D** — Warfarin alone contraindicated (WISN risk)
7. **B** — Platelet transfusion contraindicated (fuels thrombosis)
8. **B** — Methyldopa = true autoantibody (persists); Penicillin = drug-dependent (recovers)
9. **B** — Primaquine contraindicated in G6PD
10. **B** — DITP platelet recovery 3–7 days
11. **B** — Valproate = dose-dependent BM suppression
12. **B** — CNIs → TMA
13. **B** — Clopidogrel → ADAMTS13 inhibition
14. **B** — EPO → anti-EPO antibodies
15. **B** — PF4-heparin complex

---

*File: `/mnt/tb/Medicine/Clinical Therapeutics and Good Prescribing/ADRs/Haematological ADRs.md` | Status: `full-fcps-mrcp-note`*
