# CGM-guided insulin adjustment

---
tags: [medicine, diabetes, davidson, cgm-guided-insulin, insulin-adjustment, fcps, mrcp]
davidson_part: Part 3: Clinical Medicine
davidson_chapter: Chapter 25: Endocrinology and Diabetes
status: full-fcps-mrcp-note
priority: HIGH
exam_relevance: "FCPS/MRCP High Yield - CGM-guided insulin adjustment replaces SMBG-based decisions; pattern management > reactive corrections; basis for AID systems"
see_also: ["CGM metrics (TIR, TBR, TAR, GMI, CV)", "rtCGM vs isCGM", "Continuous glucose monitoring (CGM)", "Insulin pump therapy (CSII)/CGM-guided insulin adjustment", "Time in range (TIR) targets"]
created: 2026-06-13
modified: 2026-06-13
---

# CGM-Guided Insulin Adjustment

> [!info]
> **Pattern management using CGM trends** replaces reactive SMBG corrections; adjust basal/bolus based on AGP patterns; pre-bolus timing critical; foundation for automated insulin delivery (AID).

---

## 1. Learning Objectives
By the end of this note you should be able to:
- [ ] Apply CGM trend arrows for real-time dose decisions
- [ ] Interpret AGP for pattern-based basal/bolus adjustments
- [ ] Use "insulin sensitivity factor" (ISF) and "carb ratio" (ICR) with CGM
- [ ] Adjust for exercise, illness, dawn phenomenon using CGM
- [ ] Understand AID system algorithms (PID, MPC, fuzzy logic)

---

## 2. Trend Arrows — Real-Time Decisions (Dexcom/Guardian/Libre 3)

| Arrow | Glucose Change | Action (Pre-Meal) | Action (Correction) |
|-------|----------------|-------------------|---------------------|
| **↑↑** (Double up) | >3 mg/dL/min (>0.17 mmol/L/min) | Add 10–20% to bolus | Add 20–30% to correction |
| **↑** (Single up) | 2–3 mg/dL/min (0.11–0.17) | Add 10% to bolus | Add 10–15% to correction |
| **→** (Straight) | <2 mg/dL/min | Standard bolus | Standard correction |
| **↓** (Single down) | 2–3 mg/dL/min | Reduce 10% from bolus | Reduce 10–15% correction |
| **↓↓** (Double down) | >3 mg/dL/min | **Reduce 20% or delay bolus** | **Reduce 20–30% or delay** |

**Rule**: Never correct based on trend alone — confirm with current glucose value.

---

## 3. AGP-Based Pattern Adjustment (14-Day Review)

### Stepwise Approach (Dawson/ADA)

| Pattern | AGP Finding | Adjustment |
|---------|-------------|------------|
| **Overnight drift up** (dawn phenomenon) | Gradual rise 3–8 AM, median >10 at 7 AM | ↑ Basal 10–20% at 2–3 AM; or shift basal later |
| **Overnight drift down** | Gradual fall 12–6 AM, median <4 at 6 AM | ↓ Basal 10–20% at 10 PM–2 AM |
| **Post-breakfast spike** | Sharp rise 8–10 AM, >10 at 2-hr | ↑ Breakfast ICR (less carb/unit); pre-bolus 15–20 min |
| **Post-lunch spike** | Similar pattern 12–2 PM | ↑ Lunch ICR; pre-bolus |
| **Late post-prandial dip** | Rise then fall <4 at 3–4 HR | ↓ Bolus or ↑ carb ratio; check protein/fat effect |
| **High variability (CV >36%)** | Wide IQR, erratic median | Regular meals, accurate carb count, consistent timing; consider AID |

---

## 4. Calculating & Refining Parameters with CGM

### Insulin Sensitivity Factor (ISF) / Correction Factor
- **Rule of 100** (T1DM): ISF = 100 ÷ TDD (units) → mmol/L per unit
- **Rule of 1800** (mg/dL): ISF = 1800 ÷ TDD → mg/dL per unit
- **CGM refinement**: Test correction when glucose stable (→), measure drop over 2–3h

### Carbohydrate Ratio (ICR)
- **Rule of 500**: ICR = 500 ÷ TDD → grams carb per unit
- **CGM refinement**: Standard meal, pre-bolus 15 min, check 2-hr (target 3.9–10.0, <3 rise)

### Basal Testing (CGM Era)
- **Old**: 4-hour fast + SMBG hourly
- **CGM**: Skip meal, watch trend → flat trend (→) = correct basal
- **Automated**: AID systems adjust basal continuously (micro-boluses)

---

## 5. Special Situations

| Situation | CGM-Guided Approach |
|-----------|---------------------|
| **Exercise (aerobic)** | Start if glucose 7–10, trend →/↑; reduce basal 50–80% 60–90 min prior; snack if <7 or ↓ trend |
| **Exercise (HIIT/anaerobic)** | May ↑ glucose initially; monitor for late hypo (6–12h post) |
| **Illness / Sick day** | ↑ Basal 20–50% (temp basal); check ketones if >14; correction doses per ISF; CGM q1–2h |
| **Dawn phenomenon** | ↑ Basal 2–3 AM (10–20%); or NPH at bedtime if MDI |
| **Somogyi (rebound)** | Nocturnal hypoglycaemia → counter-regulatory surge → morning high; CGM catches nocturnal low; ↓ basal |
| **Travel (time zones)** | Westward: extend basal intervals; Eastward: compress; CGM guides real-time |

---

## 6. Automated Insulin Delivery (AID) Algorithms

| Algorithm Type | Systems | Principle |
|----------------|---------|-----------|
| **PID** (Proportional-Integral-Derivative) | **Medtronic 670G/780G** | Error from target → proportional + integral + derivative correction |
| **MPC** (Model Predictive Control) | **Tandem Control-IQ, CamAPS FX** | Predicts glucose 30–60 min ahead using model; optimises insulin delivery |
| **Fuzzy Logic** | **Diabeloop, Insulet Omnipod 5** | Rule-based "if-then" mimicking clinician decisions |
| **Hybrid Closed-Loop (HCL)** | All current commercial | **Automates basal only**; user gives meal boluses |
| **Full Closed-Loop** | Experimental (Bihormonal, faster insulin) | Automates basal + bolus |

**Key CGM inputs to AID**: Current glucose, trend arrow (rate of change), time of day, IOB (insulin on board), COB (carbs on board).

---

## 7. MDI (Multiple Daily Injections) + CGM

**CGM adds value without pump**:
- **Basal adjustment**: Long-acting analogue dose/timing per AGP overnight pattern
- **Bolus calculator apps**: Input carb, glucose, trend → dose recommendation (e.g., mySugr, Diabox, Hedia)
- **Trend arrow adjustments**: As per Section 2
- **Remote monitoring**: Parent/partner/care team alerts

---

## 8. Documentation & Shared Decision-Making

**AGP Review Template**:
1. **Data quality**: Wear time >70%, calibration (if applicable)
2. **Global metrics**: TIR, TBR, TAR, GMI, CV
3. **Pattern identification**: 3 priority patterns (overnight, post-prandial, variability)
4. **Agreed changes**: One parameter at a time (basal → breakfast bolus → other meals)
5. **Follow-up**: 2–4 weeks (CGM re-review)

---

## 9. Exam Pearls (FCPS/MRCP)

| Topic | Key Point |
|-------|-----------|
| **Trend arrow ↑↑** | Add 10–20% to pre-meal bolus; 20–30% to correction |
| **Trend arrow ↓↓** | Reduce 20% or delay bolus; reduce/cancel correction |
| **Dawn phenomenon** | Overnight rise 3–8 AM → ↑ basal 2–3 AM |
| **Somogyi** | Nocturnal hypo → morning high → CGM proves nocturnal low → ↓ basal |
| **ISF (Rule of 100)** | 100 ÷ TDD = mmol/L per unit (T1DM) |
| **ICR (Rule of 500)** | 500 ÷ TDD = g carb per unit |
| **Pre-bolus timing** | **15–20 min** before meal (rapid analogue) |
| **AID systems** | HCL = automates basal only; user does meal bolus |
| **CGM basal test** | Skip meal, watch trend → flat (→) = correct basal |
| **Exercise aerobic** | Reduce basal 50–80% 60–90 min prior; snack if <7 or ↓ |

---

## 10. Local Navigation (for Dashboard UI)
> **Parent**: [[../Continuous glucose monitoring (CGM)|Continuous glucose monitoring (CGM)]]  
> **Hierarchy**: [[../../Davidson Chapter 25 - Diabetes Hierarchy|Diabetes Hierarchy]]  
> **Template**: [[../../../Templates/Diabetes Topic Template|Diabetes Topic Template]]  
> **See also**: [[CGM metrics (TIR, TBR, TAR, GMI, CV)]], [[rtCGM vs isCGM]], [[Insulin pump therapy (CSII)/Hybrid closed-loop]], [[Insulin pump therapy (CSII)/Automated insulin delivery (AID) systems]]