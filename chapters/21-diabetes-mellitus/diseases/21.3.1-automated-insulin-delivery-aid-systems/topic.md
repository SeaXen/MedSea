---
tags: [medicine, diabetes, davidson, aid, automated-insulin-delivery, bihormonal, full-closed-loop, fcps, mrcp]
davidson_part: Part 3: Clinical Medicine
davidson_chapter: Chapter 25: Endocrinology and Diabetes
status: full-fcps-mrcp-note
priority: HIGH
exam_relevance: "FCPS/MRCP High Yield - AID evolution from HCL to full closed-loop; bihormonal (insulin + glucagon); faster insulins (faster aspart, Lyumjev); artificial pancreas pipeline"
see_also: ["Hybrid closed-loop (670G, 780G, CamAPS, Loop)", "Pump types (tethered, patch, closed-loop)", "CGM-guided insulin adjustment", "Insulin analogues (rapid, long-acting, ultra-long)"]
created: 2026-06-13
modified: 2026-06-13
---

# Automated Insulin Delivery (AID) Systems — Beyond Hybrid Closed-Loop

> [!info]
> **AID spectrum**: HCL (basal only) → Advanced HCL (auto-correction) → Full closed-loop (basal + bolus) → Bihormonal (insulin + glucagon) → Multi-hormone (amylin, GLP-1).

---

## 1. Learning Objectives
By the end of this note you should be able to:
- [ ] Classify AID systems by automation level
- [ ] Explain limitations of HCL (meal announcement burden)
- [ ] Describe bihormonal systems and glucagon stability challenges
- [ ] Understand role of faster insulins (faster aspart, Lyumjev, FiAsp)
- [ ] Identify emerging multi-hormone approaches

---

## 2. AID Automation Levels

| Level | Name | Basal | Meal Bolus | Correction Bolus | Status |
|-------|------|-------|------------|------------------|--------|
| **0** | SMBG/MDI | Manual | Manual | Manual | Standard |
| **1** | CSII + CGM | Manual | Manual | Manual | Open loop |
| **2** | PLGS / LGS | Suspend on low | Manual | Manual | Predictive suspend |
| **3** | **HCL** (Hybrid) | **Automated** | **Manual** | Manual/semi-auto | **Current standard** |
| **4** | **AHCL** (Advanced HCL) | Automated | Manual | **Automated** | 780G, Control-IQ, Omnipod 5 |
| **5** | **Full Closed-Loop** | Automated | **Automated** | Automated | Experimental |
| **6** | **Bihormonal** | Automated (insulin + glucagon) | Automated | Automated | Experimental |
| **7** | **Multi-hormone** | Insulin + glucagon + amylin/GLP-1 | Automated | Automated | Preclinical |

---

## 3. Advanced HCL (Current Commercial) — Auto-Correction

| System | Auto-Correction | Meal Detection | Algorithm |
|--------|-----------------|----------------|-----------|
| **Medtronic 780G** | **Yes** (when glucose > target + rising) | **Yes** (rises >2 mg/dL/min post-meal) | PID |
| **Tandem Control-IQ** | **Yes** (predictive >180 mg/dL at 30 min) | No (user bolus) | MPC |
| **Omnipod 5** | **Yes** (SmartAdjust, predicted >target) | No | MPC |
| **CamAPS FX** | **Yes** (adaptive, predicted) | **Yes** (boost feature) | MPC |

**Impact**: AHCL adds ~5–8% TIR over HCL; reduces HbA1c additional 0.1–0.2%.

---

## 4. Full Closed-Loop — The Meal Challenge

**Why not yet commercial?**
1. **Insulin pharmacokinetics too slow**: Even rapid analogues peak 60–90 min; meal glucose peaks 30–60 min
2. **Carb estimation error**: ±20–30% typical → incorrect bolus
3. **No "feedforward" signal**: No reliable meal detection (ghrelin, gastric motility sensors experimental)
4. **Safety**: Unannounced meal + full auto-bolus = hypoglycaemia risk

**Solutions in development**:
- **Faster insulins** (faster aspart, Lyumjev): Peak 30–40 min, offset 10–15 min earlier
- **Peritoneal insulin delivery**: IP route → portal vein → hepatic first pass (faster)
- **Meal detection sensors**: Wearable gastric electrography, acoustic, impedance
- **AI carb estimation**: Photo-based (food recognition), voice logging

---

## 5. Bihormonal Systems (Insulin + Glucagon)

| System | Configuration | Status | Key Challenge |
|--------|--------------|--------|---------------|
| **Beta Bionics iLet** | Dual-chamber pump (insulin + glucagon) | FDA approved 2023 (insulin-only); bihormonal trials | **Glucagon stability** (aqueous: 24–48h); catheter occlusion |
| **Oregon Health (Dual-hormone)** | Research | Proven ↓ TBR further | Glucagon cost, stability, dual catheter |
| **DIY bihormonal** | Experimental | Very limited | Not practical |

**Glucagon formulations in development**:
- **Dasiglucagon** (Zealand Pharma): Stable aqueous, room temp — Phase 3
- **Glucagon analog (Xeris)**: Stable liquid — approved for rescue; pump stability studied
- **Lyophilised + dual-chamber cartridge**: Reconstitute at use (adds complexity)

---

## 6. Faster Insulins — Enabling Full Closed-Loop

| Insulin | Brand | Onset | Peak | Duration | Advantage for AID |
|---------|-------|-------|------|----------|-------------------|
| **Faster aspart** | Fiasp | **5–10 min** | 40–60 min | 3–5h | Niacinamide + arginine → faster absorption |
| **Insulin lispro-aabc** | Lyumjev | 5–10 min | 30–45 min | 3–5h | Citrate + treprostinil → vasodilation |
| **Ultra-rapid lispro** | URLi (experimental) | <5 min | ~30 min | 2–3h | Even faster |

**Evidence in AID**: Faster aspart in HCL → ↓ post-prandial glucose, ↓ meal announcement time, ↑ TIR 3–5%.

---

## 7. Alternative Delivery Routes

| Route | System | Advantage for AID |
|-------|--------|-------------------|
| **Subcutaneous (current)** | All commercial | Standard; slow PK |
| **Intraperitoneal (IP)** | Medtronic IP pump (research) | **Portal delivery** → hepatic first pass; faster glucose lowering; physiological |
| **Inhaled** | Afrezza (Technosphere) | Ultra-rapid (peak 12–15 min); meal bolus only; cough risk |
| **Intradermal / Microneedle** | Experimental | Faster absorption; less variability |

---

## 8. Artificial Pancreas Pipeline (2024–2028)

| Timeline | Milestone |
|----------|-----------|
| **2024–2025** | AHCL standard (780G, Control-IQ, Omnipod 5, CamAPS) |
| **2025–2026** | Faster insulin integration (Fiasp/Lyumjev in AID) |
| **2026–2027** | Bihormonal approval (iLet dual-hormone) |
| **2027–2028** | **Full closed-loop** (with faster insulin + meal detection) |
| **2028+** | Multi-hormone (amylin/pramlintide + GLP-1 co-delivery) |

---

## 9. Clinical Decision Framework

| Patient | Current Best AID Option |
|---------|-------------------------|
| **T1DM, wants tubed pump, best automation** | **Medtronic 780G** (auto-correction + meal detection) |
| **T1DM, wants predictive algorithm, Dexcom user** | **Tandem Control-IQ** or **Omnipod 5** |
| **T1DM, wants tubeless, phone control** | **Omnipod 5** |
| **T1DM, wants flexibility, Android user** | **CamAPS FX + Ypsomed/Dana** |
| **T1DM, tech-savvy, DIY acceptable** | **Loop / AndroidAPS** |
| **T1DM, recurrent severe hypos despite HCL** | Consider **bihormonal trial** or **IP insulin** |

---

## 10. Exam Pearls (FCPS/MRCP)

| Topic | Key Point |
|-------|-----------|
| **HCL vs AHCL** | HCL = basal only; AHCL = basal + **auto-correction bolus** |
| **Full closed-loop barrier** | **Insulin too slow** (peak 60–90 min vs meal 30–60 min) |
| **Faster insulins** | **Fiasp / Lyumjev** — onset 5–10 min, peak 30–45 min |
| **Bihormonal** | Insulin + **glucagon**; glucagon stability main challenge (24–48h aqueous) |
| **iLet (Beta Bionics)** | Dual-chamber pump; FDA approved insulin-only 2023; bihormonal in trials |
| **Dasiglucagon** | Stable aqueous glucagon (Zealand) — Phase 3 for pump use |
| **IP insulin** | Intraperitoneal → portal → hepatic first pass; physiological; research |
| **AID levels** | 0=SMBG → 3=HCL → 4=AHCL → 5=Full CL → 6=Bihormonal |
| **CamAPS FX unique** | App-based, works on multiple pumps, adaptive MPC |
| **DIY systems** | Loop, AndroidAPS, OpenAPS — support safety, document off-label |

---

## 11. Local Navigation (for Dashboard UI)
> **Parent**: [[../Insulin pump therapy (CSII)|Insulin pump therapy (CSII)]]  
> **Hierarchy**: [[../../Davidson Chapter 25 - Diabetes Hierarchy|Diabetes Hierarchy]]  
> **Template**: [[../../../Templates/Diabetes Topic Template|Diabetes Topic Template]]  
> **See also**: [[Hybrid closed-loop (670G, 780G, CamAPS, Loop)]], [[Pump types (tethered, patch, closed-loop)]], [[Insulin analogues (rapid, long-acting, ultra-long)]], [[CGM-guided insulin adjustment]]

## PasTest Scenario SBAs (Clinical Vignettes)

> **Auto-generated PasTest/Mediscope-style scenario SBAs** grounded in the authored source. Each scenario tests a real clinical fact (triad, specific sign, contraindication, trial, first-line Rx) extracted from the topic. *Source: Ch 21: Diabetes — Automated insulin delivery (AID) systems*

**Q1.** Which of the following features is most specific or characteristic of Automated insulin delivery (AID) systems?

  - **A.** Carb estimation error
  - **B.** A feature common to many acute inflammatory conditions
  - **C.** A non-specific sign that does not localise the diagnosis
  - **D.** An investigation finding rather than a clinical feature

  > **Answer: A** — Carb estimation error
  >
  > *Source:* **Carb estimation error**: ±20–30% typical → incorrect bolus
3
---

> Auto-generated study sections for "Insulin pump therapy (CSII)" — Ch 21: Diabetes Mellitus.

## Flashcards (11 generated)

- Q: What is the definition of Insulin pump therapy (CSII)?
  A: # Automated Insulin Delivery (AID) Systems — Beyond Hybrid Closed-Loop
- Q: What is HCL vs AHCL of Insulin pump therapy (CSII)?
  A: HCL = basal only; AHCL = basal + auto-correction bolus
- Q: What is Full closed-loop barrier of Insulin pump therapy (CSII)?
  A: Insulin too slow (peak 60–90 min vs meal 30–60 min)
- Q: What is Faster insulins of Insulin pump therapy (CSII)?
  A: Fiasp / Lyumjev — onset 5–10 min, peak 30–45 min
- Q: What is Bihormonal of Insulin pump therapy (CSII)?
  A: Insulin + glucagon; glucagon stability main challenge (24–48h aqueous)
- Q: What is iLet (Beta Bionics) of Insulin pump therapy (CSII)?
  A: Dual-chamber pump; FDA approved insulin-only 2023; bihormonal in trials
- Q: What is Dasiglucagon of Insulin pump therapy (CSII)?
  A: Stable aqueous glucagon (Zealand) — Phase 3 for pump use
- Q: What is IP insulin of Insulin pump therapy (CSII)?
  A: Intraperitoneal → portal → hepatic first pass; physiological; research
- Q: What is AID levels of Insulin pump therapy (CSII)?
  A: 0=SMBG → 3=HCL → 4=AHCL → 5=Full CL → 6=Bihormonal
- Q: What is CamAPS FX unique of Insulin pump therapy (CSII)?
  A: App-based, works on multiple pumps, adaptive MPC
- Q: What is DIY systems of Insulin pump therapy (CSII)?
  A: Loop, AndroidAPS, OpenAPS — support safety, document off-label

## MCQs (1 generated)

1. **Which of the following best describes Insulin pump therapy (CSII)?**
   A. **# Automated Insulin Delivery (AID) Systems — Beyond Hybrid Closed-Loop**
   B. An unrelated condition not matching the clinical picture of Insulin pump therapy (CSII)
   C. A complication seen late in the disease course of Insulin pump therapy (CSII)
   D. A condition that mimics Insulin pump therapy (CSII) but has a different underlying cause

## SBA Questions (1 generated)

1. A patient with suspected Insulin pump therapy (CSII) presents with: Patient — Current Best AID Option; T1DM, wants tubed pump, best automation — Medtronic 780G (auto-correction + meal detection); T1DM, wants predictive algorithm, Dexcom user — Tandem Control-IQ or Omnipod 5. What is the most likely diagnosis?
   A. **Insulin pump therapy (CSII)**
   B. A condition that mimics Insulin pump therapy (CSII) but is not the same entity
   C. A complication of Insulin pump therapy (CSII) rather than the primary diagnosis
   D. An unrelated condition in the same clinical category as Insulin pump therapy (CSII)

