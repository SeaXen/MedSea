# CGM metrics (TIR, TBR, TAR, GMI, CV)

---
tags: [medicine, diabetes, davidson, cgm, metrics, tir, tbr, tar, gmi, cv, rtCGM, isCGM, fcps, mrcp]
davidson_part: Part 3: Clinical Medicine
davidson_chapter: Chapter 25: Endocrinology and Diabetes
status: full-fcps-mrcp-note
priority: HIGH
exam_relevance: "FCPS/MRCP High Yield - CGM metrics now standard of care; TIR targets replace HbA1c for daily decisions; GMI estimates HbA1c; CV measures variability"
see_also: ["Continuous glucose monitoring (CGM)", "CGM-guided insulin adjustment", "rtCGM vs isCGM", "Time in range (TIR) targets", "HbA1c targets (individualised)"]
created: 2026-06-13
modified: 2026-06-13
---

# CGM Metrics (TIR, TBR, TAR, GMI, CV) — International Consensus

> [!info]
> **Standardised CGM metrics (ATTD 2019, 2023)** — TIR 70–180 mg/dL is primary outcome; TBR/TAR for safety; GMI estimates HbA1c; CV <36% = low variability.

---

## 1. Learning Objectives
By the end of this note you should be able to:
- [ ] Define all standard CGM metrics and their targets
- [ ] Apply TIR/TBR/TAR targets for T1DM, T2DM, pregnancy, elderly
- [ ] Interpret GMI vs HbA1c concordance/discordance
- [ ] Use CV and SD for glycaemic variability assessment
- [ ] Apply Ambulatory Glucose Profile (AGP) visual analysis

---

## 2. Core CGM Metrics (ATTD Consensus 2019/2023)

| Metric | Definition | Target (Most Adults T1/T2) | Target (Pregnancy) | Target (Elderly/High Risk) |
|--------|------------|----------------------------|-------------------|----------------------------|
| **TIR** (Time in Range) | % time 70–180 mg/dL (3.9–10.0 mmol/L) | **>70%** (>16.8 h/day) | **>70%** (3.5–7.8 mmol/L) | **>50%** |
| **TAR** (Time Above Range) | % time >180 mg/dL (>10.0 mmol/L) | **<25%** (<6 h/day) | **<25%** | **<10% >250 mg/dL** |
| **TAR Level 2** | % time >250 mg/dL (>13.9 mmol/L) | **<5%** (<1.2 h/day) | **<5%** | **<5%** |
| **TBR** (Time Below Range) | % time <70 mg/dL (<3.9 mmol/L) | **<4%** (<1 h/day) | **<4%** | **<1%** |
| **TBR Level 2** | % time <54 mg/dL (<3.0 mmol/L) | **<1%** (<15 min/day) | **<1%** | **<1%** |

**Minimum CGM wear for valid report**: **≥70% data capture over 14 days** (10 days minimum).

---

## 3. Derived Metrics

| Metric | Formula | Target | Clinical Use |
|--------|---------|--------|--------------|
| **GMI** (Glucose Management Indicator) | 3.31 + 0.02392 × mean sensor glucose (mg/dL) | Matches HbA1c target | Estimates HbA1c from CGM; replaces "eHbA1c" |
| **CV** (Coefficient of Variation) | (SD / Mean glucose) × 100% | **<36%** (stable); 36–50% (moderate); >50% (high variability) | **Best single variability metric** |
| **SD** | Standard deviation of glucose | <Mean/3 | Less robust than CV |
| **MAGE** | Mean Amplitude of Glycaemic Excursions | — | Research; complex to calculate |
| **LBGI/HBGI** | Low/High Blood Glucose Indices | — | Risk quantification |

---

## 4. TIR Targets by Population (ATTD 2023)

| Population | TIR (70–180) | TBR (<70) | TBR (<54) | TAR (>180) | TAR (>250) |
|------------|--------------|-----------|-----------|------------|------------|
| **T1DM / T2DM (most adults)** | **>70%** | <4% | <1% | <25% | <5% |
| **Pregnancy T1DM** | **>70%** (3.5–7.8) | <4% | <1% | <25% | — |
| **Pregnancy T2DM/GDM** | **>70%** (3.5–7.8) | <4% | <1% | <25% | — |
| **Older / High Risk** (frailty, CKD, CVD) | **>50%** | <1% | <1% | <10% (>250) | <5% |

**Each 5% TIR increase ≈ 0.3–0.5% HbA1c reduction ≈ 15–20% microvascular risk reduction.**

---

## 5. GMI vs HbA1c — Discordance

| Scenario | GMI vs HbA1c | Cause |
|----------|--------------|-------|
| **Concordant** | Within ±0.5% (5.5 mmol/mol) | Normal RBC turnover |
| **GMI > HbA1c** | GMI higher | Anaemia, haemolysis, CKD, pregnancy, Hb variants, recent transfusion |
| **HbA1c > GMI** | HbA1c higher | Iron deficiency, splenectomy, certain Hb variants |

**GMI formula**: GMI (%) = 3.31 + 0.02392 × mean glucose (mg/dL)
- Mean 154 mg/dL → GMI 7.0%
- Mean 183 mg/dL → GMI 7.7%
- Mean 212 mg/dL → GMI 8.4%

---

## 6. Coefficient of Variation (CV) — Glycaemic Variability

| CV | Interpretation | Action |
|-----|----------------|--------|
| **<36%** | **Low variability** — stable | Continue current regimen |
| **36–50%** | **Moderate** | Review insulin timing, carb counting, basal rates |
| **>50%** | **High variability** | High hypo/hyper risk; consider technology (AID, CGM alerts) |

**Why CV over SD**: CV normalises for mean glucose — two people with same SD but different means have different variability risk.

---

## 7. Ambulatory Glucose Profile (AGP) — Visual Analysis

**Standardised 14-day AGP report** (ATTD):
1. **Median line** (50th percentile)
2. **Interquartile range (IQR)** 25–75th percentile — "glucose corridor"
3. **10–90th percentile** — extremes
4. **Reference ranges** (green 70–180, yellow >180, red <70)

**Pattern recognition**:
- **Dawn phenomenon**: Rise 3–8 AM
- **Post-prandial spikes**: After meals
- **Nocturnal hypoglycaemia**: Flat line or dips 2–4 AM
- **Basal too high**: Overnight gradual decline
- **Bolus mismatch**: Sharp post-meal rise + late drop

---

## 8. rtCGM vs isCGM — Metric Availability

| Feature | rtCGM (Dexcom G6/G7, Guardian, FreeStyle Libre 3) | isCGM (FreeStyle Libre 1/2) |
|---------|---------------------------------------------------|----------------------------|
| **Real-time alerts** | Yes (predictive) | No (Libre 2 has optional alarms) |
| **Data completeness** | Automatic (Bluetooth) | Requires scan (≥8-hourly for 100%) |
| **TIR validity** | High (≥70% auto) | User-dependent (scanning frequency) |
| **Calibration** | None (factory) | None (factory) |
| **GMI/CV accuracy** | High | High if scanned regularly |

---

## 9. Clinical Application Workflow

```
1. Review AGP (14-day)
   ├─ Data completeness >70%?
   ├─ TIR >70%? → Continue
   ├─ TBR >4% or Level 2 >1%? → Reduce basal/bolus, review hypos
   ├─ TAR >25%? → Increase basal/bolus, carb counting, timing
   ├─ CV >36%? → Regular meals, pre-bolus, technology
   └─ GMI vs HbA1c discordant? → Check RBC indices

2. Shared decision-making with patient
3. Adjust 1 parameter at a time (basal → bolus → correction)
4. Re-review at 2–4 weeks
```

---

## 10. Exam Pearls (FCPS/MRCP)

| Topic | Key Point |
|-------|-----------|
| **TIR target (most adults)** | **>70%** (70–180 mg/dL / 3.9–10.0 mmol/L) |
| **TBR target** | **<4%** (<70 mg/dL); Level 2 <54 mg/dL **<1%** |
| **TAR target** | **<25%** (>180 mg/dL); Level 2 >250 mg/dL **<5%** |
| **Pregnancy TIR range** | **3.5–7.8 mmol/L** (63–140 mg/dL); target >70% |
| **Elderly/frail TIR** | **>50%**; TBR <1% (<70); TAR <10% (>250) |
| **GMI formula** | 3.31 + 0.02392 × mean glucose (mg/dL) |
| **CV target** | **<36%** = low variability |
| **AGP minimum wear** | **14 days, >70% data capture** |
| **Each 5% TIR ↑** | ≈ 0.3–0.5% HbA1c ↓ ≈ 15–20% microvascular risk ↓ |
| **rtCGM vs isCGM** | rtCGM = real-time alerts; isCGM = scan-dependent |

---

## 11. Local Navigation (for Dashboard UI)
> **Parent**: [[../Continuous glucose monitoring (CGM)|Continuous glucose monitoring (CGM)]]  
> **Hierarchy**: [[../../Davidson Chapter 25 - Diabetes Hierarchy|Diabetes Hierarchy]]  
> **Template**: [[../../../Templates/Diabetes Topic Template|Diabetes Topic Template]]  
> **See also**: [[CGM-guided insulin adjustment]], [[rtCGM vs isCGM]], [[Time in range (TIR) targets]], [[HbA1c targets (individualised)]], [[HbA1c interpretation in CKD]]