---
tags: [medicine, davidson, hematology, apml, aml-m3, fcps, mrcp]
davidson_chapter: Chapter 25: Haematology and Transfusion Medicine
status: full-fcps-mrcp-note
priority: high
exam_relevance: "FCPS: Essential | MRCP: Core | High-yield for vivas, DIC, ATRA syndrome, arsenic trioxide"
see_also: "[[Acute Myeloid Leukaemia (AML)]], [[DIC]], [[Differentiation Syndrome]], [[Acute Lymphoblastic Leukaemia (ALL)]]"
created: 2025-06-15
modified: 2025-06-15
---

# Acute Promyelocytic Leukaemia (APML / AML-M3)

> [!info] **Davidson Ch 25 Alignment**: Haematological Malignancies → Acute Leukaemias → APML (AML with t(15;17))
> **FCPS/MRCP Focus**: Medical emergency (DIC), ATRA + ATO protocol, differentiation syndrome, coagulopathy management, molecular monitoring (PML::RARA)

---

## 🎯 Learning Objectives

- [ ] Recognise APML as a **medical emergency** due to life-threatening DIC/bleeding
- [ ] Identify diagnostic features: promyelocytes with Auer rods (faggot cells), t(15;17), PML::RARA
- [ ] Initiate **emergency ATRA 45 mg/m²/day immediately** on suspicion (before genetic confirmation)
- [ ] Manage **DIC aggressively**: Platelets >50, Fibrinogen >1.5-2, Cryoprecipitate/FFP
- [ ] Apply **ATRA + Arsenic Trioxide (ATO)** standard induction/consolidation (LOAP/APL0406)
- [ ] Recognise and treat **ATRA Differentiation Syndrome**: Dexamethasone 10mg BD
- [ ] Monitor **MRD by RT-qPCR for PML::RARA** (every 3 months × 2 years)
- [ ] Understand CNS prophylaxis (intrathecal not routine; ATO crosses BBB)
- [ ] Know salvage: ATO ± Gemtuzumab ± HSCT for molecular/haematological relapse

---

## 📖 Definition & Classification

| Feature | Details |
|---------|---------|
| **WHO/ICC** | AML with **t(15;17)(q24;q21); PML::RARA** |
| **FAB M3** | Hypergranular promyelocytes |
| **FAB M3v (Microgranular)** | Hypogranular, bilobed nuclei, may mimic monoblastic; **WBC often higher** |
| **Genetics** | **t(15;17) → PML::RARA** (98%); Variant translocations (PLZF::RARA, NPM1::RARA, etc.) – **ATRA resistant** |

> [!tip] **FCPS/MRCP**: **APML = M3 = t(15;17) = PML::RARA = ATRA/ATO sensitive**. **Variant translocations = ATRA resistant** = treat as standard AML.

---

## ⚙️ Pathophysiology

```mermaid
flowchart TD
    A[t(15;17) Translocation] --> B[PML::RARA Fusion Protein]
    B --> C[Dominant Negative Inhibition of PML]
    C --> D[Blocked Differentiation at Promyelocyte Stage]
    D --> E[Accumulation of Promyelocytes]
    E --> F[Release of Procoagulant Granules]
    F --> G[DIC: Thrombosis + Haemorrhage]
    E --> H[Annexin II ↑ → Fibrinolysis]
    G & H --> I[Life-threatening Bleeding/Thrombosis]
```

**Key**: PML::RARA blocks transcription → differentiation arrest at promyelocyte → granules release tissue factor, annexin II → **DIC + hyperfibrinolysis**

---

## 🔬 Diagnostic Workup

### Emergency Recognition (Treat on Suspicion!)

| Feature | Finding |
|---------|---------|
| **Clinical** | Bleeding (mucosal, intracranial), thrombosis, fever, pancytopenia |
| **CBC** | Anaemia, thrombocytopenia (often severe), WBC variable (low/high) |
| **Blood Film** | **Abundant promyelocytes**, **Auer rods**, **Faggot cells** (bundles of Auer rods) |
| **Coagulation** | **PT/APTT ↑, Fibrinogen ↓↓, D-dimer ↑↑, FDP ↑, Platelets ↓** |
| **BM Aspirate** | >20% promyelocytes, strong MPO+, CD117+, CD33+, **CD34-, HLA-DR-** |
| **Genetics** | **RT-PCR for PML::RARA** (quantitative), FISH, Karyotype |

```mermaid
flowchart TD
    A[Suspected APML: Bleeding + Promyelocytes on Film] --> B[**START ATRA 45 mg/m²/day IMMEDIATELY**]
    B --> C[CBC, Coagulation Profile (PT/APTT, Fibrinogen, D-dimer)]
    C --> D[Blood Film: Promyelocytes, Auer rods, Faggot cells]
    D --> E[BM Aspirate: MPO++, CD34-, HLA-DR-]
    E --> F[**RT-PCR PML::RARA (Quantitative) + FISH**]
    F --> G[Confirm t(15;17) / PML::RARA]
    G --> H[Variant Translocation? → Treat as Standard AML]
    G --> I[**APML Protocol: ATRA + ATO**]
```

> [!warning] **NEVER DELAY ATRA** waiting for genetics. **ATRA within hours saves lives** by reversing DIC.

---

## 💊 Management – ATRA + Arsenic Trioxide (ATO) Protocol

### Induction (ATRA + ATO) – **Standard of Care (LOAP, APL0406)**

| Drug | Dose | Duration | Key Points |
|------|------|----------|------------|
| **ATRA** | 45 mg/m²/day PO/IV (divided BD) | Until CR (max 60 days) | **Start immediately on suspicion**; gives differentiation |
| **Arsenic Trioxide (ATO)** | 0.15 mg/kg/day IV | Until CR (max 60 days) | **Apoptosis + differentiation**; crosses BBB |

**Induction continues until CR (usually 30-50 days)**. Monitor: CBC, coagulation, LFT, electrolytes (K, Mg), ECG (QTc).

> [!tip] **FCPS/MRCP**: **ATRA + ATO = standard induction**; NO anthracycline in low-risk (WBC<10). **Anthracycline added for high-risk (WBC≥10)** or if ATO unavailable.

### Risk Stratification (Sanz Score)

| Risk Group | WBC | Platelets | Treatment |
|------------|-----|-----------|-----------|
| **Low** | <10 | >40 | **ATRA + ATO** (no chemo) |
| **Intermediate** | <10 | ≤40 | **ATRA + ATO** (+/- anthracycline) |
| **High** | ≥10 | Any | **ATRA + ATO + Anthracycline** (Idarubicin) **OR ATRA + Idarubicin + ATO consolidation** |

### Consolidation (Post-CR)

| Cycle | Regimen |
|-------|---------|
| **Consolidation 1** | ATO 0.15 mg/kg/day × 25 doses (5 weeks) |
| **Consolidation 2** | ATRA 45 mg/m²/day × 14 days (2 weeks on/2 weeks off × 7 cycles = 15 weeks) |
| **Consolidation 3** | ATO 0.15 mg/kg/day × 25 doses |
| **Consolidation 4** | ATRA 45 mg/m²/day × 14 days |

**Total consolidation ~8 months**. **Maintenance ATRA** (2 years) debated; not standard in ATO era.

---

## ⚠️ ATRA Differentiation Syndrome (ATRA Syndrome)

| Feature | Details |
|---------|---------|
| **Incidence** | 10-25% (usually days 7-21 of ATRA) |
| **Diagnosis** | Fever + Weight gain >5kg + Pulmonary infiltrates + Hypoxaemia + Pleural/pericardial effusion + Hypotension + Renal impairment |
| **Risk Factors** | **WBC >10**, rapid WBC rise |
| **Prophylaxis** | **Dexamethasone 10 mg BD PO/IV × 14 days** if WBC >10 or rising rapidly |
| **Treatment** | **Dexamethasone 10 mg IV BD** until resolution; **hold ATRA if severe** (hypoxia, hypotension, renal failure); resume after resolution |

> [!warning] **ATRA Syndrome = Medical Emergency**. **Dex 10mg BD** is treatment AND prophylaxis. Do NOT confuse with infection.

---

## 🩸 DIC Management – Critical for Survival

| Parameter | Target | Replacement |
|-----------|--------|-------------|
| **Platelets** | **>50** (100 if active bleed/CSF procedure) | **Platelet transfusion** (irradiated, HLA-matched if refractory) |
| **Fibrinogen** | **>1.5-2.0 g/L** | **Cryoprecipitate** (1 pool/10kg) or **Fibrinogen concentrate** |
| **PT/APTT** | <1.5x ULN | **FFP** (15 mL/kg) if invasive procedure/active bleed |
| **D-dimer/FDP** | Monitor trend | Treat underlying (ATRA/ATO) |

**Monitor q6-12h initially**. **ATRA itself reverses DIC** by inducing differentiation (stops granule release).

---

## 🔬 Molecular Monitoring (RT-qPCR PML::RARA)

| Timepoint | Action |
|-----------|--------|
| **Diagnosis** | Baseline quantitative RT-PCR (log reduction from here) |
| **End-Induction (CR)** | Should be **negative** (or >3-log reduction) |
| **Post-Consolidation** | **Negative** |
| **Follow-up** | **Every 3 months × 2 years**, then q6mo × 3 years |
| **Molecular Relapse** | **Positive PCR after prior negative** OR **>1-log increase** on 2 consecutive tests |
| **Action on Molecular Relapse** | **ATO monotherapy** → re-induction → HSCT if haematological relapse |

> [!tip] **FCPS/MRCP**: **RT-qPCR PML::RARA is standard MRD**. **Molecular relapse = re-treat with ATO**. **HSCT only for haematological relapse**.

---

## 🧠 CNS Prophylaxis

| Aspect | Recommendation |
|--------|----------------|
| **Routine IT Chemo** | **NOT routinely required** (ATO crosses BBB) |
| **High Risk (WBC≥10)** | Some protocols give **IT MTX during induction** |
| **CNS Relapse** | Rare (<2%); treated with **IT MTX/Ara-C + systemic ATO** |

---

## 🌱 Relapsed APML

| Relapse Type | Management |
|--------------|------------|
| **Molecular Relapse** (PCR+ only) | **ATO monotherapy** 0.15 mg/kg/day until PCR negative (max 60 days) |
| **Haematological Relapse** (Blasts >5%) | **ATO + ATRA ± Gemtuzumab** → **Allo-HSCT in CR2** |
| **Extramedullary/CNS** | ATO + IT chemotherapy → HSCT |

**Gemtuzumab Ozogamicin** (anti-CD33): 3-6 mg/m² × 1-2 doses – effective salvage, bridge to HSCT.

---

## 🔄 Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| **AML-M3v (Microgranular)** | Hypogranular, bilobed nuclei, **WBC often high**, same t(15;17), **ATRA/ATO sensitive** |
| **AML with variant RARA translocations** | t(11;17) PLZF::RARA, t(5;17) NPM1::RARA, t(11;17) NuMA::RARA – **ATRA RESISTANT** = treat as standard AML |
| **Other AML (non-M3)** | Different cytogenetics, no PML::RARA, no DIC typically, treated with 7+3 |
| **DIC from other causes** | Sepsis, trauma, obstetric – no promyelocytes, no t(15;17) |
| **ATRA Syndrome vs Sepsis** | ATRA syndrome: **Dex responsive**, temporal relation to ATRA, no positive cultures |

---

## 💡 FCPS/MRCP High-Yield Summary

| Topic | Key Point |
|-------|-----------|
| **Emergency** | **Start ATRA 45 mg/m²/day IMMEDIATELY** on clinical suspicion |
| **Genetics** | **t(15;17) → PML::RARA**; Variant translocations = ATRA resistant |
| **Film** | **Promyelocytes + Auer rods + Faggot cells (bundles)** |
| **Immunophenotype** | **CD34-, HLA-DR-, MPO++, CD33+, CD117+** |
| **DIC** | PT/APTT↑, **Fibrinogen↓↓**, D-dimer↑↑, Platelets↓ – **Target Plt>50, Fib>1.5** |
| **Induction** | **ATRA + ATO** (Low/Int risk); **ATRA + ATO + Idarubicin** (High risk WBC≥10) |
| **ATRA Syndrome** | Fever, weight gain, pulmonary infiltrates, hypoxia – **Dex 10mg BD** (prophylaxis if WBC>10, treatment) |
| **Consolidation** | Alternating ATO (25 doses) + ATRA (14 days) × 4 cycles |
| **MRD** | **RT-qPCR PML::RARA q3mo × 2y** |
| **Molecular Relapse** | **ATO monotherapy** |
| **Haematological Relapse** | ATO + ATRA ± Gemtuzumab → **Allo-HSCT in CR2** |
| **CNS Prophylaxis** | **Not routine** (ATO crosses BBB) |

---

## ❓ Viva Questions

1. **What is the first step in management of suspected APML?**
   - **Start ATRA 45 mg/m²/day IMMEDIATELY** – do not wait for genetic confirmation

2. **What is the genetic hallmark of APML and what is the fusion protein?**
   - **t(15;17)(q24;q21) → PML::RARA fusion protein**

3. **Describe the coagulation profile in APML DIC.**
   - **PT/APTT prolonged, Fibrinogen very low, D-dimer/FDP markedly elevated, Thrombocytopenia**

4. **What are the targets for platelet and fibrinogen replacement in APML?**
   - **Platelets >50 (100 if active bleed); Fibrinogen >1.5-2.0 g/L**

5. **What is ATRA differentiation syndrome and how is it managed?**
   - Fever, weight gain, pulmonary infiltrates, hypoxia, effusions – **Dexamethasone 10 mg IV BD**; prophylaxis if WBC>10

6. **What is the standard induction regimen for APML?**
   - **ATRA 45 mg/m²/day + ATO 0.15 mg/kg/day** until CR (add Idarubicin if WBC≥10)

7. **How do you monitor MRD in APML?**
   - **Quantitative RT-PCR for PML::RARA** every 3 months × 2 years

8. **What is the management of molecular relapse in APML?**
   - **ATO monotherapy** until PCR negative

9. **How do variant RARA translocations differ from classic t(15;17)?**
   - **ATRA resistant** – treat as standard AML (7+3 ± HSCT)

10. **Is intrathecal chemotherapy routinely required in APML?**
    - **No** – ATO crosses blood-brain barrier; CNS relapse rare (<2%)

---

## 🧠 Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **APML vs Other AML** | **APML = CD34-, HLA-DR-, MPO++, t(15;17), DIC** |
| **ATRA Syndrome vs Sepsis** | ATRA syndrome: **Dex responsive**, weeks 1-3 of ATRA, no positive cultures |
| **Variant RARA translocations** | **ATRA RESISTANT** = treat as standard AML |
| **ATO vs Arsenic Trioxide** | Same thing – **ATO = Arsenic Trioxide = As₂O₃** |
| **Molecular vs Haematological Relapse** | Molecular = PCR+ only → ATO; Haematological = blasts → ATO+ATRA±Gemtuzumab → HSCT |

| Mnemonic | Meaning |
|----------|---------|
| **"APML = ATRA Immediately"** | Start ATRA on suspicion |
| **"DIC: Fibrinogen Down, D-dimer Up"** | Coagulation profile |
| **"PML-RARA = Promyelocytic Leukaemia - RARA"** | Fusion gene mnemonic |
| **"ATRA Syndrome = Dex for Distress"** | Dexamethasone 10mg BD |
| **"WBC>10 = Dex for 14 days"** | ATRA syndrome prophylaxis |
| **"Molecular Relapse = ATO Alone"** | Salvage for PCR+ only |
| **"No IT routine, ATO crosses BBB"** | CNS prophylaxis |

---

## 🗺️ Mind Map

```mermaid
mindmap
  root((Acute Promyelocytic Leukaemia))
    Emergency
      Start ATRA 45 mg/m² IMMEDIATELY
    Genetics
      t(15;17) → PML::RARA (98%)
      Variants: PLZF::RARA, NPM1::RARA → ATRA Resistant
    Morphology
      Hypergranular (M3)
      Microgranular (M3v)
      Auer rods, Faggot cells
    Immunophenotype
      CD34-, HLA-DR-, MPO++, CD33+
    DIC
      PT/APTT↑, Fib↓↓, D-dimer↑↑, Plt↓
      Target: Plt>50, Fib>1.5
    Induction
      ATRA + ATO (Low/Int)
      + Idarubicin (High: WBC≥10)
    ATRA Syndrome
      Fever, weight gain, pulmonary infiltrates
      Dex 10mg BD (Prophylaxis if WBC>10)
    Consolidation
      Alternating ATO (25d) + ATRA (14d) × 4
    MRD
      RT-qPCR PML::RARA q3mo × 2y
    Relapse
      Molecular: ATO alone
      Haematological: ATO+ATRA±Gemtuzumab → HSCT
    CNS
      No routine IT (ATO crosses BBB)
```

---

## 📋 One-Page Revision Card

| **APML – FCPS/MRCP REVISION CARD** |
|------------------------------------|
| **Suspect APML? → START ATRA 45 mg/m²/day IMMEDIATELY** |
| **Genetics**: t(15;17) → **PML::RARA** (variants = ATRA resistant) |
| **Film**: Promyelocytes, **Auer rods, Faggot cells** |
| **Immunophenotype**: **CD34-, HLA-DR-, MPO++, CD33+** |
| **DIC**: PT/APTT↑, **Fibrinogen↓↓**, D-dimer↑↑, Plt↓ – **Target Plt>50, Fib>1.5** |
| **Induction**: **ATRA + ATO** (add Idarubicin if WBC≥10) |
| **ATRA Syndrome**: Fever, weight gain, pulmonary infiltrates → **Dex 10mg BD** |
| **Prophylaxis**: Dex 10mg BD × 14 days if **WBC>10** |
| **Consolidation**: Alternating **ATO (25d) + ATRA (14d) × 4 cycles** |
| **MRD**: **RT-qPCR PML::RARA q3mo × 2 years** |
| **Molecular Relapse**: **ATO monotherapy** |
| **Haematological Relapse**: ATO+ATRA±Gemtuzumab → **HSCT CR2** |
| **CNS**: **No routine IT** (ATO crosses BBB) |

---

## 📅 Spaced Repetition Tracker

| Review | Date | Score (1-5) | Next Review |
|--------|------|-------------|-------------|
| Day 1 | 2025-06-15 | | 2025-06-16 |
| Day 3 | | | |
| Day 7 | | | |
| Day 15 | | | |
| Day 30 | | | |

---

## 🎯 Must Know / Should Know / Nice to Know

| Level | Content |
|-------|---------|
| **Must Know** | Emergency ATRA start, t(15;17)/PML::RARA, DIC management targets, ATRA+ATO induction, ATRA syndrome (Dex 10mg BD), consolidation schedule, RT-qPCR monitoring, molecular vs haematological relapse management, variant translocation resistance |
| **Should Know** | Sanz risk stratification, WBC threshold for anthracycline/dex prophylaxis, ATO mechanism (apoptosis + differentiation), gemtuzumab in salvage, ATO crosses BBB, CD34-/HLA-DR- immunophenotype, faggot cells, fibrinogen concentrate vs cryoprecipitate |
| **Nice to Know** | Detailed LOAP/APL0406 trial data, PML nuclear bodies biology, annexin II hyperfibrinolysis mechanism, QTc prolongation with ATO, arsenic trioxide differentiation syndrome, paediatric vs adult protocol differences, FLT3 mutations in APML |

---

## ✅ Self-Test Scorecard

| Section | Score (0-10) | Notes |
|---------|--------------|-------|
| Emergency Recognition & ATRA Start | | |
| DIC Management | | |
| Induction Regimen (ATRA+ATO±Chemo) | | |
| ATRA Syndrome Recognition/Treatment | | |
| Consolidation Schedule | | |
| MRD Monitoring (RT-qPCR) | | |
| Relapse Management | | |
| Variant Translocations | | |
| Viva Questions | | |

---

## 🔗 Local Navigation

- **Previous**: [[Acute Lymphoblastic Leukaemia (ALL)]]
- **Next**: [[Chronic Myeloid Leukaemia (CML)]]
- **Section Hub**: [[Haematological Malignancies]]
- **MOC**: [[Hematology MOC]]
- **Template**: [[../Templates/Hematology Topic Template]]

---

*Generated for FCPS/MRCP exam preparation. Based on Davidson Medicine 24th Ed Chapter 25.*
---

> Auto-generated study sections for "Hematology" — Ch 24: Haematology & Transfusion Medicine.

## Flashcards (29 generated)

- Q: What is the definition of Hematology?
  A: [!info] Davidson Ch 25 Alignment: Haematological Malignancies → Acute Leukaemias → APML (AML with t(15;17))
- Q: What is Clinical of Hematology?
  A: Bleeding (mucosal, intracranial), thrombosis, fever, pancytopenia
- Q: What is CBC of Hematology?
  A: Anaemia, thrombocytopenia (often severe), WBC variable (low/high)
- Q: What is Blood Film of Hematology?
  A: Abundant promyelocytes, Auer rods, Faggot cells (bundles of Auer rods)
- Q: What is Coagulation of Hematology?
  A: PT/APTT ↑, Fibrinogen ↓↓, D-dimer ↑↑, FDP ↑, Platelets ↓
- Q: What is BM Aspirate of Hematology?
  A: >20% promyelocytes, strong MPO+, CD117+, CD33+, CD34-, HLA-DR-
- Q: What is Genetics of Hematology?
  A: RT-PCR for PML::RARA (quantitative), FISH, Karyotype
- Q: What is the epidemiology of Hematology?
  A: 10-25% (usually days 7-21 of ATRA)
- Q: What is the investigation of choice for Hematology?
  A: Fever + Weight gain >5kg + Pulmonary infiltrates + Hypoxaemia + Pleural/pericardial effusion + Hypotension + Renal impairment
- Q: What causes Hematology?
  A: WBC >10, rapid WBC rise
- Q: What is Prophylaxis of Hematology?
  A: Dexamethasone 10 mg BD PO/IV × 14 days if WBC >10 or rising rapidly
- Q: How is Hematology managed?
  A: Dexamethasone 10 mg IV BD until resolution; hold ATRA if severe (hypoxia, hypotension, renal failure); resume after resolution
- Q: What is Routine IT Chemo of Hematology?
  A: NOT routinely required (ATO crosses BBB)
- Q: What is High Risk (WBC≥10) of Hematology?
  A: Some protocols give IT MTX during induction
- Q: What is CNS Relapse of Hematology?
  A: Rare (<2%); treated with IT MTX/Ara-C + systemic ATO
- Q: What is Clinical of Hematology?
  A: Bleeding (mucosal, intracranial), thrombosis, fever, pancytopenia
- Q: What is CBC of Hematology?
  A: Anaemia, thrombocytopenia (often severe), WBC variable (low/high)
- Q: What is Blood Film of Hematology?
  A: Abundant promyelocytes, Auer rods, Faggot cells (bundles of Auer rods)
- Q: What is Coagulation of Hematology?
  A: PT/APTT ↑, Fibrinogen ↓↓, D-dimer ↑↑, FDP ↑, Platelets ↓
- Q: What is BM Aspirate of Hematology?
  A: >20% promyelocytes, strong MPO+, CD117+, CD33+, CD34-, HLA-DR-
- Q: What is Genetics of Hematology?
  A: RT-PCR for PML::RARA (quantitative), FISH, Karyotype
- Q: What is the epidemiology of Hematology?
  A: 10-25% (usually days 7-21 of ATRA)
- Q: What is the investigation of choice for Hematology?
  A: Fever + Weight gain >5kg + Pulmonary infiltrates + Hypoxaemia + Pleural/pericardial effusion + Hypotension + Renal impairment
- Q: What causes Hematology?
  A: WBC >10, rapid WBC rise
- Q: What is Prophylaxis of Hematology?
  A: Dexamethasone 10 mg BD PO/IV × 14 days if WBC >10 or rising rapidly
- Q: How is Hematology managed?
  A: Dexamethasone 10 mg IV BD until resolution; hold ATRA if severe (hypoxia, hypotension, renal failure); resume after resolution
- Q: What is Routine IT Chemo of Hematology?
  A: NOT routinely required (ATO crosses BBB)
- Q: What is High Risk (WBC≥10) of Hematology?
  A: Some protocols give IT MTX during induction
- Q: What is CNS Relapse of Hematology?
  A: Rare (<2%); treated with IT MTX/Ara-C + systemic ATO

## MCQs (1 generated)

1. **Which of the following best describes Hematology?**
   A. **[!info] Davidson Ch 25 Alignment: Haematological Malignancies → Acute Leukaemias → APML (AML with t(15;17))**
   B. An unrelated condition not matching the clinical picture of Hematology
   C. A complication seen late in the disease course of Hematology
   D. A condition that mimics Hematology but has a different underlying cause

## SBA Questions (1 generated)

1. A patient with suspected Hematology presents with: WHO/ICC — AML with t(15;17)(q24;q21); PML::RARA; FAB M3 — Hypergranular promyelocytes; FAB M3v (Microgranular) — Hypogranular, bilobed nuclei, may mimic monoblastic; WBC often higher. What is the most likely diagnosis?
   A. **Hematology**
   B. A condition that mimics Hematology but is not the same entity
   C. A complication of Hematology rather than the primary diagnosis
   D. An unrelated condition in the same clinical category as Hematology

