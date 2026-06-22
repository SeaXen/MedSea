---
tags: [medicine, davidson, hematology, lead-poisoning, anaemia, poisoning, fcps, mrcp]
davidson_chapter: Chapter 25: Haematology and Transfusion Medicine
status: full-fcps-mrcp-note
priority: high
exam_relevance: "FCPS: High-yield | MRCP: Core | Microcytic anaemia, basophilic stippling, abdominal colic, neuropathy, Burton's line, chelation"
see_also: "[[Iron Deficiency Anaemia]], [[Sideroblastic Anaemia]], [[Thalassaemia]], [[G6PD Deficiency]]"
created: 2025-06-17
modified: 2025-06-17
---

# Lead Poisoning

> [!info] **Davidson Ch 25 Alignment**: Anaemia and Red Cell Disorders → Microcytic Anaemia → Lead Poisoning
> **FCPS/MRCP Focus**: Microcytic hypochromic anaemia, basophilic stippling, abdominal colic, wrist/foot drop, Burton's line, chelation therapy

---

## 🎯 Learning Objectives

- [ ] Recognise lead poisoning as a cause of **microcytic hypochromic anaemia** with **basophilic stippling**
- [ ] Identify clinical features: **Abdominal colic**, **Peripheral neuropathy (wrist/foot drop)**, **Burton's line**, **Encephalopathy**
- [ ] Diagnose: **Blood lead level**, **FEP/ZPP elevation**, **CBC with basophilic stippling**, **X-ray (lead lines)**
- [ ] Manage: **Remove from exposure**, **Chelation therapy** (DMSA, D-penicillamine, EDTA), **Supportive care**
- [ ] Differentiate from: Iron deficiency, Thalassaemia, Sideroblastic anaemia, Porphyria

---

## 📖 Definition & Epidemiology

| Aspect | Details |
|--------|---------|
| **Definition** | Toxic accumulation of lead → multisystem toxicity (haematological, neurological, GI, renal) |
| **Sources** | Lead-based paint, contaminated water, batteries, ceramics, traditional medicines, occupational |
| **At-risk Groups** | Children (pica, hand-to-mouth), Industrial workers, Developing countries (leaded petrol) |
| **Absorption** | GI tract (↑ in children, fasting, iron/calcium deficiency), Respiratory (inhalation) |

> [!tip] **FCPS/MRCP**: **Lead poisoning = Microcytic anaemia + Basophilic stippling + Abdominal colic + Wrist/foot drop + Burton's line**. **Blood lead level diagnostic**. **Chelation: DMSA (oral), EDTA (IV), D-penicillamine (oral)**.

---

## ⚙️ Pathophysiology

```mermaid
flowchart TD
    A[Lead Absorption] --> B[Lead Binds to Sulfhydryl Groups]
    B --> C1[Inhibits ALA Dehydratase (ALAD)] --> D1[↑ ALA, ↑ Coproporphyrin]
    B --> C2[Inhibits Ferrochelatase] --> D2[↓ Haeme Synthesis → ↑ Protoporphyrin]
    B --> C3[Inhibits Pyrimidine-5'-Nucleotidase] --> D3[↑ Pyrimidine Nucleotides → Basophilic Stippling]
    B --> C4[Neurotoxicity] --> D4[Peripheral Neuropathy, Encephalopathy]
    B --> C5[Renal Toxicity] --> D5[Fanconi Syndrome, Chronic Nephropathy]
    D1 & D2 & D3 & D4 & D5 --> E[Systemic Lead Toxicity]
```

**Key Enzyme Inhibition:**
- **ALA Dehydratase (ALAD)** → ↑ ALA in urine (most sensitive test)
- **Ferrochelatase** → ↑ Zinc Protoporphyrin (ZPP) / Free Erythrocyte Protoporphyrin (FEP)
- **Pyrimidine-5'-Nucleotidase** → Basophilic stippling (RNA aggregates)

---

## 🔬 Diagnostic Workup

```mermaid
flowchart TD
    A[Suspected Lead Poisoning: Microcytic Anaemia + Neuro/GI Symptoms] --> B[**Blood Lead Level (BLL)** - Gold Standard]
    B --> C{BLL Thresholds}
    C -->|>5 µg/dL (Children)| D[Public Health Action]
    C -->|>20 µg/dL| E[Medical Evaluation + Chelation Consideration]
    C -->|>45 µg/dL| F[Chelation Indicated]
    C -->|>70 µg/dL| G[Medical Emergency - Admit]
    B --> H[**CBC + Blood Film**]
    H --> I{Microcytic Hypochromic + Basophilic Stippling}
    I --> J[**ZPP/FEP Elevated**]
    J --> K[**Urinary ALA, Coproporphyrin**]
    K --> L[**Abdominal X-ray** (Radiopaque flecks if recent ingestion)]
    L --> M[**Long Bone X-ray** (Lead lines at metaphyses)]
```

### Key Investigations

| Test | Significance |
|------|--------------|
| **Blood Lead Level (BLL)** | **Gold standard**; >5 µg/dL (children) = action; >20 µg/dL = medical evaluation; >45 µg/dL = chelation |
| **CBC + Film** | Microcytic hypochromic anaemia, **Basophilic stippling** (coarse), Target cells |
| **ZPP / FEP** | **Elevated** (Ferrochelatase inhibition); Screening test |
| **Urinary ALA** | **Markedly elevated** (ALAD inhibition); Most sensitive biochemical test |
| **Urinary Coproporphyrin** | Elevated |
| **Abdominal X-ray** | Radiopaque flecks in GI tract (if ingestion <36h) |
| **Long Bone X-ray** | **Lead lines** (dense metaphyseal bands) in children |
| **Renal Function** | Fanconi syndrome (glycosuria, aminoaciduria, phosphaturia) |

---

## 🩺 Clinical Features

| System | Manifestations |
|--------|----------------|
| **Haematological** | **Microcytic hypochromic anaemia**, **Basophilic stippling**, Reticulocytosis |
| **GI** | **Abdominal colic** (intermittent, severe), Constipation, Anorexia, Weight loss |
| **Neurological (PNS)** | **Wrist drop** (radial nerve), **Foot drop** (peroneal nerve), Peripheral neuropathy |
| **Neurological (CNS)** | Encephalopathy (irritability, seizures, coma), Cognitive impairment (children) |
| **Renal** | Fanconi syndrome (proximal tubular dysfunction), Chronic interstitial nephritis |
| **Reproductive** | Infertility, Miscarriage, Reduced libido |
| **Physical Signs** | **Burton's line** (blue-black gingival margin), Pallor, Hypertension |

> [!warning] **Burton's Line** = Blue-black line at gingival margin (lead sulphide deposition) - Classic but NOT pathognomonic.

---

## 💊 Management

### 1. Immediate Actions
| Action | Details |
|--------|---------|
| **Remove from Exposure** | **Critical first step**; Identify and eliminate source |
| **Nutritional Optimisation** | **Iron, Calcium, Zinc supplementation** (reduces absorption) |
| **Monitoring** | Serial BLL, CBC, Renal function, Neurological status |

### 2. Chelation Therapy Indications

| BLL (µg/dL) | Action |
|-------------|--------|
| **<5** | Monitor, Nutritional optimisation, Environmental investigation |
| **5-19** | Monitor, Reduce exposure, Iron/Calcium supplementation |
| **20-44** | **Medical evaluation**, Consider chelation if symptomatic |
| **45-69** | **Chelation therapy indicated** (DMSA oral) |
| **≥70** | **Medical emergency** - **IV EDTA + Oral DMSA**, Hospital admission |

### 3. Chelating Agents

| Agent | Route | Dose | Indication | Key Monitoring |
|-------|-------|------|------------|----------------|
| **DMSA (Succimer)** | **Oral** | 10 mg/kg 8-hourly × 5 days, then 12-hourly × 14 days | **BLL 45-69 µg/dL**, **First-line** | FBC, LFT, Renal function |
| **CaNa₂EDTA** | **IV Infusion** | 50-75 mg/kg/day (divided) × 5 days | **BLL ≥70 µg/dL**, **Encephalopathy** | **Renal function**, Urine output, ECG |
| **D-penicillamine** | **Oral** | 250-500 mg/day (divided) | Alternative if DMSA unavailable | CBC, Urinalysis (proteinuria), LFT |
| **DMPS** | **IV/IM** | 10 mg/kg/day | Alternative (not universally available) | Similar to DMSA |

> [!warning] **CaNa₂EDTA**: **IV only**, **Risk of nephrotoxicity** → **Hydration essential**, Monitor renal function closely. **Do NOT use Na₂EDTA** (causes hypocalcaemia).

### 4. Chelation Protocols

| Scenario | Regimen |
|----------|---------|
| **BLL 45-69, Asymptomatic** | **DMSA 10 mg/kg 8-hrly × 5d, then 12-hrly × 14d** |
| **BLL ≥70 OR Encephalopathy** | **CaNa₂EDTA 50 mg/kg/day IV × 5d + DMSA** (start DMSA after 1st EDTA dose) |
| **Repeat Courses** | May need repeated if BLL rebounds (lead redistributes from bone) |

---

## 🔄 Differential Diagnosis

| Condition | Key Differentiators |
|-----------|---------------------|
| **Iron Deficiency Anaemia** | No basophilic stippling, Low ferritin, Mentzer index >13, No neuro/GI symptoms |
| **Thalassaemia** | Mentzer index <13, HbA2/F elevated, Family history, No basophilic stippling |
| **Sideroblastic Anaemia** | Ring sideroblasts on BM, Dimorphic film, High ferritin, Iron overload |
| **Porphyria** | Photosensitivity, Neuropsychiatric, Urinary porphobilinogen/ALA elevation |
| **Iron Deficiency + Lead** | Coexistence common (iron deficiency ↑ lead absorption) |

---

## 💡 FCPS/MRCP High-Yield Summary

| Topic | Key Point |
|-------|-----------|
| **Anaemia Type** | **Microcytic hypochromic** + **Basophilic stippling** (coarse) |
| **Blood Lead Level** | **Gold standard**; >5 µg/dL action (children), >45 chelation, >70 emergency |
| **Enzyme Inhibition** | **ALAD** (↑ ALA), **Ferrochelatase** (↑ ZPP/FEP), **P5'N** (Basophilic stippling) |
| **Clinical Triad** | **Abdominal colic + Wrist/foot drop + Burton's line** |
| **Chelation** | **DMSA (oral) first-line**; **EDTA (IV) severe/encephalopathy** |
| **Screening** | **ZPP/FEP** (cheapest), **Urinary ALA** (most sensitive), **BLL** (gold standard) |
| **X-ray** | **Lead lines** at metaphyses (children), **Radiopaque flecks** in GI |
| **Iron Deficiency** | **Coexists** with lead poisoning (↑ absorption); Treat both |

---

## ❓ Viva Questions

1. **What is the diagnostic hallmark of lead poisoning on blood film?**
   - **Coarse basophilic stippling** (due to pyrimidine-5'-nucleotidase inhibition)

2. **What are the three key enzymes inhibited by lead in haeme synthesis?**
   - **ALA Dehydratase (ALAD)** → ↑ ALA; **Ferrochelatase** → ↑ ZPP/FEP; **Pyrimidine-5'-Nucleotidase** → Basophilic stippling

3. **What blood lead level requires chelation therapy?**
   - **≥45 µg/dL** (oral DMSA); **≥70 µg/dL** (IV EDTA + DMSA, medical emergency)

4. **What is Burton's line and is it specific?**
   - Blue-black line at gingival margin (lead sulphide); **NOT specific** (can be absent, seen in other conditions)

5. **What is the first-line chelating agent for lead poisoning and its route?**
   - **DMSA (Succimer), Oral** - Preferred for BLL 45-69 µg/dL

6. **Why is CaNa₂EDTA given IV and what is the major risk?**
   - IV only; **Nephrotoxicity** - Requires hydration and renal monitoring

7. **How does iron deficiency interact with lead poisoning?**
   - **Iron deficiency ↑ lead absorption** (shared DMT1 transporter); Treat iron deficiency concurrently

8. **What are the classic neurological manifestations?**
   - **Motor neuropathy**: Wrist drop (radial), Foot drop (peroneal); **Encephalopathy** at high levels

9. **What urinary findings are characteristic of lead poisoning?**
   - **↑ ALA**, **↑ Coproporphyrin**; **↓ Porphobilinogen** (differentiates from porphyria)

10. **How do you monitor chelation therapy response?**
    - **Serial BLL** (rebound common, may need repeated courses), **CBC**, **Renal function**, **Clinical improvement**

---

## 🧠 Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **Lead vs Iron Deficiency** | **Lead = Basophilic stippling, Neuro/GI symptoms, ↑ ZPP, ↑ ALA**; **IDA = Low ferritin, No stippling** |
| **Lead vs Thalassaemia** | **Lead = Basophilic stippling, Neuro/GI, ↑ BLL**; **Thal = Mentzer <13, HbA2↑, Family history** |
| **Lead vs Sideroblastic** | **Lead = ↑ BLL, Enzyme inhibition**; **Sideroblastic = Ring sideroblasts, Iron overload** |
| **EDTA vs DMSA** | **EDTA = IV, Severe, Nephrotoxic**; **DMSA = Oral, First-line, Safer** |
| **Basophilic Stippling** | **Coarse in Lead**; **Fine in Thalassaemia/Mechanical** |

| Mnemonic | Meaning |
|----------|---------|
| **"LEAD = Lines (X-ray), Encephalopathy, Abdominal colic, Drop (wrist/foot)"** | Clinical features |
| **"BLL >45 = DMSA; >70 = EDTA + DMSA"** | Chelation thresholds |
| **"ALAD = ALA Up; Ferrochelatase = ZPP Up; P5'N = Stippling"** | Enzyme inhibition |
| **"Burton's = Blue Gums"** | Physical sign |
| **"Iron Low = Lead High"** | Iron deficiency ↑ lead absorption |

---

## 🗺️ Mind Map

```mermaid
mindmap
  root((Lead Poisoning))
    Exposure
      Paint, Water, Batteries, Occupational
      Children (Pica)
    Pathophysiology
      ALAD Inhibition → ↑ ALA
      Ferrochelatase → ↑ ZPP/FEP
      P5'N Inhibition → Basophilic Stippling
    Clinical
      Anaemia: Microcytic + Stippling
      GI: Abdominal Colic
      Neuro: Wrist/Foot Drop, Encephalopathy
      Renal: Fanconi Syndrome
      Burton's Line
    Diagnosis
      BLL (Gold Standard)
      ZPP/FEP (Screen)
      Urinary ALA (Sensitive)
      X-ray: Lead Lines, GI Flecks
    Management
      Remove Exposure
      Iron/Calcium Supplement
      Chelation: DMSA (Oral) / EDTA (IV)
      BLL Thresholds: >45 DMSA, >70 EDTA
```

---

## 📋 One-Page Revision Card

| **LEAD POISONING – FCPS/MRCP REVISION CARD** |
|-----------------------------------------------|
| **Anaemia**: Microcytic + **Basophilic Stippling** (Coarse) |
| **Blood Lead Level (BLL)**: Gold Standard; >5 action, >45 chelate, >70 emergency |
| **Enzymes**: ALAD↓ → ALA↑; Ferrochelatase↓ → ZPP/FEP↑; P5'N↓ → Stippling |
| **Clinical**: Abdominal Colic, **Wrist/Foot Drop**, Burton's Line, Encephalopathy |
| **Chelation**: **DMSA Oral (BLL 45-69)**; **CaNa₂EDTA IV (BLL ≥70)** |
| **Iron Deficiency** → ↑ Lead Absorption → Treat Both |
| **X-ray**: Lead Lines (Metaphyses), GI Flecks |
| **ZPP/FEP** = Screen; **Urinary ALA** = Sensitive |

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
| **Must Know** | Microcytic anaemia + basophilic stippling, BLL thresholds, 3 enzyme inhibitions, abdominal colic/wrist drop/Burton's line, DMSA vs EDTA indications, iron-lead interaction |
| **Should Know** | Urinary ALA/coproporphyrin, lead lines on X-ray, Fanconi syndrome, D-penicillamine alternative, DMSA dosing schedule, EDTA nephrotoxicity prevention, sources of exposure, public health notification |
| **Nice to Know** | ALAD gene polymorphisms, epigenetic effects, chelation pharmacokinetics, combined chelation protocols, neurodevelopmental outcomes, occupational exposure limits, lead in traditional medicines, environmental remediation |

---

## ✅ Self-Test Scorecard

| Section | Score (0-10) | Notes |
|---------|--------------|-------|
| Clinical Features | | |
| Pathophysiology & Enzymes | | |
| Diagnosis & BLL Interpretation | | |
| Chelation Therapy | | |
| Differential Diagnosis | | |
| Viva Questions | | |

---

## 🔗 Local Navigation

- **Previous**: [[Sideroblastic Anaemia]]
- **Next**: [[G6PD Deficiency]]
- **Section Hub**: [[Anaemia and Red Cell Disorders]]
- **MOC**: [[Hematology MOC]]
- **Template**: [[../Templates/Hematology Topic Template]]

---

*Generated for FCPS/MRCP exam preparation. Based on Davidson Medicine 24th Ed Chapter 25.*
---

> Auto-generated study sections for "Hematology" — Ch 24: Haematology & Transfusion Medicine.

## Flashcards (12 generated)

- Q: What is the definition of Hematology?
  A: Toxic accumulation of lead → multisystem toxicity (haematological, neurological, GI, renal)
- Q: What is Sources of Hematology?
  A: Lead-based paint, contaminated water, batteries, ceramics, traditional medicines, occupational
- Q: What is At-risk Groups of Hematology?
  A: Children (pica, hand-to-mouth), Industrial workers, Developing countries (leaded petrol)
- Q: What is Absorption of Hematology?
  A: GI tract (↑ in children, fasting, iron/calcium deficiency), Respiratory (inhalation)
- Q: How is Hematology classified?
  A: Microcytic hypochromic + Basophilic stippling (coarse)
- Q: What is Blood Lead Level of Hematology?
  A: Gold standard; >5 µg/dL action (children), >45 chelation, >70 emergency
- Q: What is Enzyme Inhibition of Hematology?
  A: ALAD (↑ ALA), Ferrochelatase (↑ ZPP/FEP), P5'N (Basophilic stippling)
- Q: What is Clinical Triad of Hematology?
  A: Abdominal colic + Wrist/foot drop + Burton's line
- Q: What is Chelation of Hematology?
  A: DMSA (oral) first-line; EDTA (IV) severe/encephalopathy
- Q: What is Screening of Hematology?
  A: ZPP/FEP (cheapest), Urinary ALA (most sensitive), BLL (gold standard)
- Q: What is X-ray of Hematology?
  A: Lead lines at metaphyses (children), Radiopaque flecks in GI
- Q: What is Iron Deficiency of Hematology?
  A: Coexists with lead poisoning (↑ absorption); Treat both

## MCQs (1 generated)

1. **Which of the following best describes Hematology?**
   A. **[!info] Davidson Ch 25 Alignment: Anaemia and Red Cell Disorders → Microcytic Anaemia → Lead Poisoning**
   B. An unrelated condition not matching the clinical picture of Hematology
   C. A complication seen late in the disease course of Hematology
   D. A condition that mimics Hematology but has a different underlying cause

## SBA Questions (1 generated)

1. A patient with suspected Hematology presents with: Definition — Toxic accumulation of lead → multisystem toxicity (haematological, neurological, GI, renal); Sources — Lead-based paint, contaminated water, batteries, ceramics, traditional medicines, occupational; At-risk Groups — Children (pica, hand-to-mouth), Industrial workers, Developing countries (leaded petrol). What is the most likely diagnosis?
   A. **Hematology**
   B. A condition that mimics Hematology but is not the same entity
   C. A complication of Hematology rather than the primary diagnosis
   D. An unrelated condition in the same clinical category as Hematology

## PasTest Scenario SBAs (Clinical Vignettes)

> **Auto-generated PasTest/Mediscope-style scenario SBAs** grounded in the authored source. Each scenario tests a real clinical fact (triad, specific sign, contraindication, trial, first-line Rx) extracted from the topic. *Source: Ch 24: Haematology — Lead Poisoning*

**Q1.** Which of the following features is most specific or characteristic of Lead Poisoning?

  - **A.** Burton's Line
  - **B.** A feature common to many acute inflammatory conditions
  - **C.** A non-specific sign that does not localise the diagnosis
  - **D.** An investigation finding rather than a clinical feature

  > **Answer: A** — Burton's Line
  >
  > *Source:* ical Signs** | **Burton's line** (blue-black gingival margin), Pallor, Hypertension |

> [!warning] **Burton's Line** = Blue-black line at gingival margin (lead sulphide deposition) - Classic but NOT 

**Q2.** What is the most appropriate first-line therapy for Lead Poisoning?

  - **A.** Remove from Exposure + Critical first step
  - **B.** An advanced/surgical therapy reserved for refractory disease
  - **C.** Symptomatic treatment only, no disease-modifying therapy
  - **D.** Empiric broad-spectrum therapy without specific indication

  > **Answer: A** — Remove from Exposure + Critical first step
  >
  > *Source:* **Remove from Exposure**   **Critical first step**; Identify and eliminate source

