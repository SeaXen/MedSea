---
tags: [medicine, davidson, hematology, vitamin-k-deficiency, coagulopathy, warfarin, fcps, mrcp]
davidson_chapter: Chapter 25: Haematology and Transfusion Medicine
status: full-fcps-mrcp-note
priority: high
exam_relevance: "FCPS: High-yield | MRCP: Core | Malabsorption, antibiotics, warfarin effect, neonates (VKDB), vitamin K reversal, PT/INR correction"
see_also: "[[Warfarin]], [[Liver Disease Coagulopathy]], [[DIC]], [[Neonatal Haemorrhagic Disease]]"
created: 2025-06-17
modified: 2025-06-17
---

# Vitamin K Deficiency

> [!info] **Davidson Ch 25 Alignment**: Bleeding and Thrombotic Disorders → Coagulation Disorders → Vitamin K Deficiency
> **FCPS/MRCP Focus**: Causes (malabsorption, antibiotics, warfarin), PT/INR elevation, vitamin K reversal, neonates (VKDB), warfarin management

---

## 🎯 Learning Objectives

- [ ] Define **Vitamin K Deficiency**: Impaired γ-carboxylation of Factors II, VII, IX, X → prolonged PT/INR
- [ ] Identify **Causes**: Malabsorption (cholestasis, CF, IBD), Antibiotics (broad-spectrum), Warfarin, Dietary deficiency, Neonatal (VKDB)
- [ ] Diagnose: **PT/INR ↑↑, Normal APTT** (early), **Normal platelet count**, **Vitamin K level low**, **PIVKA-II elevated**
- [ ] Manage: **Vitamin K1 (Phytomenadione)** IV/IM/PO, **Fresh Frozen Plasma** if bleeding/urgent, **Warfarin dose adjustment**
- [ ] Recognise **Neonatal Vitamin K Deficiency Bleeding (VKDB)**: Early, Classical, Late → **Prophylaxis: Vitamin K 1mg IM at birth**
- [ ] Manage **Warfarin Over-anticoagulation**: Vitamin K dose based on INR/bleeding
- [ ] Differentiate from: **Liver Disease, DIC, Warfarin Overdose, Factor VII Deficiency**

---

## 📖 Definition & Pathophysiology

| Aspect | Details |
|--------|---------|
| **Essential Nutrient** | **Vitamin K1 (Phylloquinone)** – dietary (green leafy vegetables); **Vitamin K2 (Menaquinone)** – gut bacterial synthesis |
| **Function** | **Co-factor for γ-glutamyl carboxylase** → **γ-carboxylation of Glu residues** on Factors II, VII, IX, X, Protein C, Protein S, Factor Z |
| **γ-Carboxylation** | Enables **Ca²⁺ binding** → **Factor activation** on phospholipid surfaces |
| **Deficiency Effect** | **Under-carboxylated proteins (PIVKAs)** → **Impaired coagulation** → **Prolonged PT/INR** |

> [!tip] **Vitamin K = Fat-soluble**. **Absorption requires bile salts + pancreatic enzymes**. **Stored minimally** (days-weeks). **Factors II, VII, IX, X, Protein C, S, Z = Vitamin K-dependent**.

---

## 📖 Causes of Vitamin K Deficiency

| Category | Causes |
|----------|--------|
| **Malabsorption** | **Cholestasis** (obstructive jaundice, PSC, PBC), **Cystic Fibrosis**, **IBD (Crohn's)**, **Short Bowel Syndrome**, **Bariatric Surgery**, **Pancreatic Insufficiency** |
| **Antibiotics** | **Broad-spectrum** (Cephalosporins, Carbapenems) → **Eradicate gut flora** (↓ K2 synthesis); **High-dose/Prolonged** |
| **Dietary** | **Severe malnutrition**, **Anorexia nervosa**, **Total Parenteral Nutrition (TPN) without K** |
| **Drug Interference** | **Warfarin** (Vitamin K antagonist), **Broad-spectrum antibiotics**, **Salicylates (high dose)** |
| **Neonatal** | **VKDB**: Low placental transfer, Low breast milk K, Sterile gut, Immature liver |
| **Other** | **Enoxaparin** (rare), **Cholestyramine** (binds bile acids) |

> [!tip] **Vitamin K Deficiency = Malabsorption + Antibiotics + Warfarin + Neonatal**. **PT/INR ↑↑, APTT normal (early), Normal platelets, Normal fibrinogen**.

---

## 🔬 Diagnostic Workup

```mermaid
flowchart TD
    A[Bleeding/Bruising + Prolonged PT/INR] --> B[**CBC + PT/INR + APTT + Fibrinogen + D-dimer**]
    B --> C{**PT/INR ↑↑, APTT Normal (Early), Plat/Norm, Fib/Norm**}
    C -->|Yes| D[**Vitamin K Deficiency Likely**]
    C -->|APTT ↑| E[Consider Liver Disease / DIC / Heparin]
    D --> F[**Vitamin K1 Level** (Low)]
    D --> G[**PIVKA-II (Des-γ-carboxy Prothrombin)** Elevated]
    F & G --> H[**Identify Cause**]
    H --> I1[**Malabsorption?** → LFT, US Abdomen, Bile Acids]
    H --> I2[**Antibiotics?** → Drug History]
    H --> I3[**Warfarin?** → INR Trend]
    H --> I4[**Neonatal?** → Age, Feeding, Prophylaxis]
```

### Key Investigations

| Test | Vitamin K Deficiency | Liver Disease | DIC | Warfarin |
|------|----------------------|---------------|-----|----------|
| **PT/INR** | **↑↑ (Early, Marked)** | **↑↑** | **↑↑** | **↑↑** |
| **APTT** | **Normal (Early)** | **↑** | **↑** | Normal/↑ |
| **Platelets** | **Normal** | **↓ (Thrombocytopenia)** | **↓** | Normal |
| **Fibrinogen** | **Normal** | **↓/Normal** | **↓↓** | Normal |
| **D-dimer** | **Normal** | **↑** | **↑↑↑** | Normal |
| **Factor VII** | **↓↓ (Shortest t½)** | **↓** | **↓** | **↓** |
| **PIVKA-II** | **↑↑** | **↑** | **↑** | **↑** |
| **Vitamin K Level** | **Low** | Low/Normal | Normal | Normal |

> [!tip] **Factor VII = Shortest half-life (4-6h)** → **First to fall in Vit K deficiency** → **PT/INR rises first**. **APTT normal early** (Factors IX, X, II have longer t½).

---

## 🩺 Clinical Features

| Manifestation | Details |
|---------------|---------|
| **Bleeding** | Ecchymoses, Haematuria, GI bleed, Epistaxis, Haemarthrosis, Retroperitoneal bleed |
| **Skin** | Petechiae, Ecchymoses, Prolonged bleeding from venepuncture |
| **Neonatal (VKDB)** | **Early (<24h)**: Maternal drugs; **Classical (2-7 days)**: Breastfed, no prophylaxis; **Late (2-12 weeks)**: Cholestasis, malabsorption, exclusively breastfed |
| **Bone** | **Reduced bone density** (Vit K role in osteocalcin carboxylation) |

---

## 💊 Management

### Vitamin K1 (Phytomenadione) Replacement

| Route | Dose | Onset | Indication |
|-------|------|-------|------------|
| **IV** | **5-10 mg** (slow over 30 min) | **6-12 hours** | **Severe bleeding, Urgent surgery, INR >10** |
| **IM** | **5-10 mg** | **12-24 hours** | If IV access unavailable |
| **PO** | **5-10 mg** (can repeat) | **24 hours** | **Asymptomatic, INR 5-10, Non-urgent** |
| **SC** | **Avoid** (Erratic absorption) | - | - |

> [!warning] **IV Vitamin K: Anaphylaxis risk (rare)** → **Give slowly over 30 min**, Monitor. **IV preferred for urgent reversal**. **Oral preferred for non-urgent**.

### Warfarin Reversal (Vitamin K Dosing)

| INR / Clinical | Vitamin K1 Dose | Route | Notes |
|----------------|-----------------|-------|-------|
| **INR 5-9, No Bleeding** | **1-2 mg** | **PO** | Hold warfarin, Recheck INR 24h |
| **INR >10, No Bleeding** | **3-5 mg** | **PO** | Hold warfarin, Recheck INR 24h |
| **Minor Bleed, INR >2** | **2-5 mg** | **IV/PO** | Hold warfarin |
| **Major Bleed / Urgent Surgery** | **5-10 mg** | **IV** (slow) | **+ FFP/PCC if life-threatening** |
| **Life-threatening Bleed** | **10 mg IV** + **PCC/FFP** | IV | **PCC preferred over FFP** |

> [!warning] **Vitamin K takes 6-24h to work**. **For urgent reversal → PCC/FFP + Vitamin K**. **Avoid subcutaneous (erratic absorption)**.

### Neonatal Vitamin K Deficiency Bleeding (VKDB)

| Type | Timing | Risk Factors | Prophylaxis |
|------|--------|--------------|-------------|
| **Early** | **<24 hours** | Maternal drugs (Warfarin, Anticonvulsants, Rifampicin, Isoniazid) | **Maternal Vit K 10mg oral × 2wks before delivery** |
| **Classical** | **2-7 days** | **Exclusive breastfeeding**, No prophylaxis | **Vit K 1mg IM at birth** (Standard) |
| **Late** | **2-12 weeks** | **Exclusive breastfeeding**, **Cholestasis**, **Cystic Fibrosis**, **Malabsorption** | **Vit K 1mg IM at birth** + **Oral 2mg weekly × 12wks** (if breastfed) |

> [!warning] **VKDB = Medical Emergency in Neonates**. **IM Vit K at birth = Standard of Care**. **Oral only if parents refuse IM** (3 doses: birth, 1 week, 6 weeks).

---

## 🔄 Differential Diagnosis

| Condition | PT/INR | APTT | Platelets | Fibrinogen | D-dimer | Key Differentiator |
|-----------|--------|------|-----------|------------|---------|-------------------|
| **Vitamin K Deficiency** | **↑↑** | **Normal (Early)** | Normal | Normal | Normal | **Factor VII ↓ first**, PIVKA-II ↑ |
| **Liver Disease** | ↑↑ | ↑ | **↓** | ↓/Normal | ↑ | **All factors ↓**, Ascites, Encephalopathy |
| **DIC** | ↑ | ↑ | **↓** | **↓↓** | **↑↑↑** | **Consumptive**, Underlying trigger |
| **Warfarin Overdose** | ↑↑ | Normal/↑ | Normal | Normal | Normal | **History**, INR correlates with dose |
| **Factor VII Deficiency** | ↑↑ | **Normal** | Normal | Normal | Normal | **Isolated Factor VII ↓**, Genetic |

---

## 💡 FCPS/MRCP High-Yield Summary

| Topic | Key Point |
|-------|-----------|
| **γ-Carboxylation** | **Vit K-dependent**: Factors II, VII, IX, X, Protein C, S, Z |
| **Factor VII** | **Shortest t½ (4-6h)** → **PT/INR rises FIRST** in Vit K deficiency |
| **PT/INR** | **↑↑**, **APTT Normal (Early)** → **Key differentiator from Liver/DIC** |
| **PIVKA-II** | **Des-γ-carboxy Prothrombin** → **Elevated** (Sensitive marker) |
| **Vitamin K1 Dose** | **IV 5-10mg (Urgent)**, **PO 5-10mg (Non-urgent)**, **Avoid SC** |
| **Warfarin Reversal** | **INR 5-9: 1-2mg PO**; **INR >10: 3-5mg PO**; **Bleed: 5-10mg IV + PCC** |
| **Neonatal VKDB** | **1mg IM at birth** (Standard); **Late VKDB: Oral 2mg weekly × 12wks if breastfed** |
| **Differentiation** | **Vit K Def: PT↑, APTT Normal, Plt/Fib Normal**; **Liver: APTT↑, Plt↓**; **DIC: Plt↓, Fib↓, D-dimer↑↑** |

---

## ❓ Viva Questions

1. **Which coagulation factor has the shortest half-life and why is it relevant in Vitamin K deficiency?**
   - **Factor VII (t½ 4-6h)** → **PT/INR rises first** in Vit K deficiency

2. **What is PIVKA-II and its significance?**
   - **Des-γ-carboxy Prothrombin** → **Under-carboxylated Factor II** → **Elevated in Vit K deficiency/Warfarin/Liver disease** (Sensitive marker)

3. **What is the recommended prophylactic dose of Vitamin K for neonates?**
   - **1 mg IM at birth** (Standard); **Oral 2mg at birth, 1 week, 6 weeks** if parents refuse IM

6. **How do you differentiate Vitamin K deficiency from Liver Disease on coagulation screen?**
   - **Vit K Def: PT↑, APTT Normal, Platelets/Fibrinogen Normal**; **Liver: PT↑, APTT↑, Platelets↓, Fibrinogen↓**

7. **What is the Vitamin K1 dose for urgent warfarin reversal (major bleeding)?**
   - **5-10 mg IV (slow) + PCC/FFP**; **Vitamin K alone takes 6-24h**

7. **Why is subcutaneous Vitamin K avoided?**
   - **Erratic absorption** → Unpredictable response

8. **What are the three types of Neonatal VKDB and their timing?**
   - **Early (<24h)**, **Classical (2-7 days)**, **Late (2-12 weeks)**

8. **How does broad-spectrum antibiotics cause Vitamin K deficiency?**
   - **Eradicates gut flora** → ↓ Vitamin K2 (Menaquinone) synthesis

9. **What is the difference between PT and APTT in early Vitamin K deficiency?**
   - **PT/INR prolonged** (Factor VII↓), **APTT normal** (Factors IX, X, II still adequate)

10. **How do you manage a patient with obstructive jaundice and bleeding before surgery?**
    - **Vitamin K 10mg IV** (urgent); **If no response → FFP**; **Correct coagulopathy before surgery**

---

## 🧠 Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **Vit K Def vs Liver Disease** | **Vit K: APTT Normal, Plt/Fib Normal**; **Liver: APTT↑, Plt↓, Fib↓** |
| **Vit K Def vs Warfarin** | **Both: PT↑, APTT Normal**; **Warfarin: History, INR correlates with dose**; **Vit K: Malabsorption/Antibiotics** |
| **Vit K Def vs DIC** | **Vit K: APTT Normal, Plt/Fib Normal, D-dimer Normal**; **DIC: APTT↑, Plt↓, Fib↓, D-dimer↑↑** |
| **Oral vs IV Vit K** | **IV = 6-12h onset, Urgent**; **PO = 24h, Non-urgent**; **SC = Avoid** |
| **PIVKA-II vs INR** | **PIVKA-II = Direct marker of Vit K status**; **INR = Functional (PT)** |

| Mnemonic | Meaning |
|----------|---------|
| **"Factor VII = Fastest Fall = PT Rises First"** | Factor VII shortest t½ |
| **"Vit K = PT Up, APTT Normal"** | Differentiation |
| **"PIVKA-II = Vit K Marker"** | Diagnostic marker |
| **"Neonate = 1mg IM = VKDB Prevention"** | Neonatal prophylaxis |
| **"Warfarin Reversal: INR>10 = Vit K 3-5mg PO; Bleed = 10mg IV + PCC"** | Warfarin reversal |
| **"Vit K = γ-Carboxylation = Factors 2,7,9,10 + C,S,Z"** | Vit K-dependent factors |

---

## 🗺️ Mind Map

```mermaid
mindmap
  root((Vitamin K Deficiency))
    Causes
      Malabsorption (Cholestasis, CF, IBD)
      Antibiotics (Broad-spectrum)
      Warfarin (Vit K Antagonist)
      Neonatal (VKDB)
      Dietary/TPN
    Pathophysiology
      ↓ γ-Carboxylation
      Factors II, VII, IX, X, C, S, Z
      Factor VII t½ = 4-6h (Shortest)
    Diagnosis
      PT/INR ↑↑, APTT Normal
      Platelets/Fibrinogen Normal
      PIVKA-II ↑
      Vit K Level Low
    Clinical
      Bleeding/Bruising
      Neonatal VKDB: Early/Classical/Late
    Management
      Vit K1: IV 5-10mg (Urgent), PO 5-10mg (Non-urgent)
      Warfarin Reversal: INR-based Dosing
      Neonatal: 1mg IM at Birth
    Differential
      Vit K Def: PT↑, APTT Normal
      Liver: APTT↑, Plt↓
      DIC: Plt↓, Fib↓, D-dimer↑↑
      Warfarin: History + INR
```

---

## 📋 One-Page Revision Card

| **VITAMIN K DEFICIENCY – FCPS/MRCP REVISION CARD** |
|-----------------------------------------------------|
| **γ-Carboxylation**: Factors **II, VII, IX, X, Protein C, S, Z** |
| **Factor VII**: **Shortest t½ (4-6h)** → **PT ↑ First** |
| **Coagulation Screen**: **PT/INR ↑↑, APTT Normal, Plt/Fib Normal** |
| **Diagnosis**: **PIVKA-II ↑**, **Vit K Level Low** |
| **Causes**: **Malabsorption**, **Antibiotics**, **Warfarin**, **Neonatal** |
| **Treatment**: **Vit K1: IV 5-10mg (Urgent), PO 5-10mg (Non-urgent), NO SC** |
| **Warfarin Reversal**: INR 5-9: 1-2mg PO; >10: 3-5mg PO; Bleed: **10mg IV + PCC** |
| **Neonatal VKDB**: **1mg IM at Birth**; Late: Oral 2mg weekly × 12wks (Breastfed) |
| **Differential**: **Vit K Def = PT↑, APTT Normal**; Liver = APTT↑, Plt↓; DIC = Plt↓, Fib↓ |

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
| **Must Know** | Vit K-dependent factors, Factor VII shortest t½, PT↑ APTT normal pattern, PIVKA-II, Vit K1 dosing (IV/PO), warfarin reversal dosing, neonatal VKDB types & prophylaxis, differential (Liver, DIC, Warfarin) |
| **Should Know** | γ-carboxylation biochemistry, Vit K cycle (epoxide reductase), warfarin mechanism (VKORC1), PIVKA-II assay methodology, oral vs IV bioavailability, anaphylaxis risk with IV Vit K, late VKDB in breastfed infants, bile acid malabsorption, Vit K in bone health (osteocalcin) |
| **Nice to Know** | Vit K2 (MK-4, MK-7) sources, gut microbiome role, VKORC1 polymorphisms, warfarin pharmacogenomics, Vit K in vascular calcification, matrix Gla protein, PIVKA-II in HCC diagnosis, oral Vit K prophylaxis regimens worldwide, cost-effectiveness of neonatal prophylaxis |

---

## ✅ Self-Test Scorecard

| Section | Score (0-10) | Notes |
|---------|--------------|-------|
| Pathophysiology & Causes | | |
| Diagnosis & PIVKA-II | | |
| Treatment (Vit K1 Dosing) | | |
| Warfarin Reversal | | |
| Neonatal VKDB | | |
| Differential Diagnosis | | |
| Viva Questions | | |

---

## 🔗 Local Navigation

- **Previous**: [[Prothrombin Gene Mutation]]
- **Next**: [[Liver Disease Coagulopathy]]
- **Section Hub**: [[Bleeding and Thrombotic Disorders]]
- **MOC**: [[Hematology MOC]]
- **Template**: [[../Templates/Hematology Topic Template]]

---

*Generated for FCPS/MRCP exam preparation. Based on Davidson Medicine 24th Ed Chapter 25.*
---

> Auto-generated study sections for "Hematology" — Ch 24: Haematology & Transfusion Medicine.

## Flashcards (13 generated)

- Q: What is the definition of Hematology?
  A: [!info] Davidson Ch 25 Alignment: Bleeding and Thrombotic Disorders → Coagulation Disorders → Vitamin K Deficiency
- Q: What is Essential Nutrient of Hematology?
  A: Vitamin K1 (Phylloquinone) – dietary (green leafy vegetables); Vitamin K2 (Menaquinone) – gut bacterial synthesis
- Q: What is Function of Hematology?
  A: Co-factor for γ-glutamyl carboxylase → γ-carboxylation of Glu residues on Factors II, VII, IX, X, Protein C, Protein S, Factor Z
- Q: What is γ-Carboxylation of Hematology?
  A: Enables Ca²⁺ binding → Factor activation on phospholipid surfaces
- Q: What is Deficiency Effect of Hematology?
  A: Under-carboxylated proteins (PIVKAs) → Impaired coagulation → Prolonged PT/INR
- Q: What is γ-Carboxylation of Hematology?
  A: Vit K-dependent: Factors II, VII, IX, X, Protein C, S, Z
- Q: What is Factor VII of Hematology?
  A: Shortest t½ (4-6h) → PT/INR rises FIRST in Vit K deficiency
- Q: What is PT/INR of Hematology?
  A: ↑↑, APTT Normal (Early) → Key differentiator from Liver/DIC
- Q: What is PIVKA-II of Hematology?
  A: Des-γ-carboxy Prothrombin → Elevated (Sensitive marker)
- Q: What is the dose of Hematology?
  A: IV 5-10mg (Urgent), PO 5-10mg (Non-urgent), Avoid SC
- Q: What is Warfarin Reversal of Hematology?
  A: INR 5-9: 1-2mg PO; INR >10: 3-5mg PO; Bleed: 5-10mg IV + PCC
- Q: What is Neonatal VKDB of Hematology?
  A: 1mg IM at birth (Standard); Late VKDB: Oral 2mg weekly × 12wks if breastfed
- Q: What is Differentiation of Hematology?
  A: Vit K Def: PT↑, APTT Normal, Plt/Fib Normal; Liver: APTT↑, Plt↓; DIC: Plt↓, Fib↓, D-dimer↑↑

## MCQs (1 generated)

1. **Which of the following best describes Hematology?**
   A. **[!info] Davidson Ch 25 Alignment: Bleeding and Thrombotic Disorders → Coagulation Disorders → Vitamin K Deficiency**
   B. An unrelated condition not matching the clinical picture of Hematology
   C. A complication seen late in the disease course of Hematology
   D. A condition that mimics Hematology but has a different underlying cause

## SBA Questions (1 generated)

1. A patient with suspected Hematology presents with: Essential Nutrient — Vitamin K1 (Phylloquinone) – dietary (green leafy vegetables); Vitamin K2 (Menaquinone) – gut bacterial synthesis; Function — Co-factor for γ-glutamyl carboxylase → γ-carboxylation of Glu residues on Factors II, VII, IX, X, Protein C, Protein S, Factor Z; γ-Carboxylation — Enables Ca²⁺ binding → Factor activation on phospholipid surfaces. What is the most likely diagnosis?
   A. **Hematology**
   B. A condition that mimics Hematology but is not the same entity
   C. A complication of Hematology rather than the primary diagnosis
   D. An unrelated condition in the same clinical category as Hematology

## PasTest Scenario SBAs (Clinical Vignettes)

> **Auto-generated PasTest/Mediscope-style scenario SBAs** grounded in the authored source. Each scenario tests a real clinical fact (triad, specific sign, contraindication, trial, first-line Rx) extracted from the topic. *Source: Ch 24: Haematology — Vitamin K Deficiency*

**Q1.** Which of the following features is most specific or characteristic of Vitamin K Deficiency?

  - **A.** "PIVKA-II = Vit K Marker"
  - **B.** A feature common to many acute inflammatory conditions
  - **C.** A non-specific sign that does not localise the diagnosis
  - **D.** An investigation finding rather than a clinical feature

  > **Answer: A** — "PIVKA-II = Vit K Marker"
  >
  > *Source:* Rises First"** | Factor VII shortest t½ |
| **"Vit K = PT Up, APTT Normal"** | Differentiation |
| **"PIVKA-II = Vit K Marker"** | Diagnostic marker |
| **"Neonate = 1mg IM = VKDB Prevention"** | Neon

**Q2.** What is the most appropriate first-line therapy for Vitamin K Deficiency?

  - **A.** Oral preferred for non-urgent
  - **B.** An advanced/surgical therapy reserved for refractory disease
  - **C.** Symptomatic treatment only, no disease-modifying therapy
  - **D.** Empiric broad-spectrum therapy without specific indication

  > **Answer: A** — Oral preferred for non-urgent
  >
  > *Source:* **Oral preferred for non-urgent**.

### Warfarin Reversal (Vitamin K Dosing)

