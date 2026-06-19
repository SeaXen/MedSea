---
tags: [medicine, diabetes, davidson, hcl, hybrid-closed-loop, 670g, 780g, camaps, loop, omnipod5, control-IQ, fcps, mrcp]
davidson_part: Part 3: Clinical Medicine
davidson_chapter: Chapter 25: Endocrinology and Diabetes
status: full-fcps-mrcp-note
priority: HIGH
exam_relevance: "FCPS/MRCP High Yield - HCL systems are standard of care for T1DM; differ in algorithm (PID vs MPC), CGM integration, meal handling; evidence from RCTs shows ↑ TIR, ↓ TBR, ↓ HbA1c"
see_also: ["Insulin pump therapy (CSII)", "Pump types (tethered, patch, closed-loop)", "Automated insulin delivery (AID) systems", "CGM metrics (TIR, TBR, TAR, GMI, CV)"]
created: 2026-06-13
modified: 2026-06-13
---

# Hybrid Closed-Loop (HCL) Systems — 670G, 780G, CamAPS, Omnipod 5, Loop

> [!info]
> **HCL = Automated basal insulin + user meal boluses** — "Hybrid" because meals still need manual bolus; algorithms: PID (Medtronic) vs MPC (Tandem/Omnipod/CamAPS); all ↑ TIR 10–15%, ↓ TBR 50%.

---

## 1. Learning Objectives
By the end of this note you should be able to:
- [ ] Compare commercial HCL systems: algorithms, CGM, pump, targets
- [ ] Explain PID vs MPC control theory
- [ ] State key trial evidence (FLAIR, PIVOTAL, etc.)
- [ ] Apply NICE/ADA criteria for HCL access
- [ ] Troubleshoot common HCL issues

---

## 2. Commercial HCL Systems (UK/Global)

| System | Pump | CGM | Algorithm | Target Glucose | Key Features |
|--------|------|-----|-----------|----------------|--------------|
| **Medtronic 670G** | 670G | Guardian 3 | **PID** | **120 mg/dL (6.7)** fixed | First FDA HCL; auto-mode only; no Bluetooth |
| **Medtronic 780G** | 780G | Guardian 3/4 | **PID** (SmartGuard) | **100, 110, 120 mg/dL** adjustable | **Auto-correction bolus**; meal detection; Bluetooth; remote monitoring |
| **Tandem t:slim X2 + Control-IQ** | t:slim X2 | Dexcom G6/G7 | **MPC** | **110–160 mg/dL** (sleep 110) | Predictive 30 min; sleep/exercise modes; auto-correction; remote |
| **Omnipod 5** | Omnipod 5 (patch) | Dexcom G6/G7 | **MPC** (SmartAdjust) | **110–150 mg/dL** adjustable | Tubeless; phone controller; no separate PDM |
| **CamAPS FX** (app) | Ypsomed / DANA-i / Dana RS | Dexcom G6/G7 / Libre 3 | **MPC** | **100–150 mg/dL** adjustable | **App-based**; runs on Android; open to multiple pumps |
| **Loop (DIY)** | Medtronic 600/700 series, Omnipod Eros/DASH | Dexcom G6 / Libre | **MPC** (open-source) | User-defined | **DIY**; not regulated; Nightscout integration |

---

## 3. Algorithm Comparison: PID vs MPC

| Aspect | **PID** (Proportional-Integral-Derivative) | **MPC** (Model Predictive Control) |
|--------|-------------------------------------------|------------------------------------|
| **Used by** | Medtronic 670G/780G | Tandem Control-IQ, Omnipod 5, CamAPS FX, Loop |
| **Principle** | Reacts to **current error** (P), **past error** (I), **rate of change** (D) | **Predicts future** glucose (30–60 min) using physiological model; optimises delivery |
| **Meal handling** | 780G: meal detection → auto-correction | Pre-meal bolus still needed; predicts post-prandial rise |
| **Hypoglycaemia prevention** | Derivative term → suspends on rapid fall | Predictive suspend 30 min before predicted low |
| **Tuning** | Gain parameters (Kp, Ki, Kd) | Model parameters (insulin sensitivity, carb ratio, time constants) |
| **Adaptability** | Limited (fixed gains) | **Adaptive** (learns individual parameters over days) |

---

## 4. Key Clinical Trials Evidence

| Trial | System | Population | TIR Change | HbA1c Change | TBR Change |
|-------|--------|------------|------------|--------------|------------|
| **FLAIR** (2021) | 780G | T1DM adults | **+14%** (63→77%) | −0.4% | −50% |
| **PIVOTAL** (2023) | 780G | T1DM adolescents | +11% | −0.3% | −40% |
| **Control-IQ RCT** (2019) | Tandem | T1DM 6–70y | **+11%** (61→71%) | −0.33% | −52% |
| **Omnipod 5 Pivotal** (2021) | Omnipod 5 | T1DM 6–70y | **+13%** | −0.4% | −45% |
| **CamAPS FX RCT** (2021) | CamAPS | T1DM 1–65y | **+10–15%** | −0.3 to −0.5% | −50% |
| **KidsAP** (2022) | CamAPS | Children 1–7y | **+18%** | −0.5% | −60% |

**Consistent finding**: All HCL systems achieve **TIR >70%** in majority; **TBR <4%**; **HbA1c reduction 0.3–0.5%**.

---

## 5. NICE Guidance (TA829, TA830, TA831, TA944 — 2023/2024)

| System | NICE TA | Indication |
|--------|---------|------------|
| **Medtronic 780G** | TA829 | T1DM adults/children ≥7y; HbA1c ≥58 OR disabling hypos |
| **Tandem Control-IQ** | TA830 | T1DM adults/children ≥6y; HbA1c ≥58 OR disabling hypos |
| **Omnipod 5** | TA831 | T1DM adults/children ≥2y; HbA1c ≥58 OR disabling hypos |
| **CamAPS FX + Ypsomed/Dana** | TA944 | T1DM adults/children ≥1y; HbA1c ≥58 OR disabling hypos |

**Common criteria**: T1DM; structured education; carb counting; CGM use; HbA1c ≥58 mmol/mol (7.5%) OR recurrent severe/unpredictable hypos.

---

## 6. Practical HCL Management

### Settings to Optimise
| Parameter | Role | Adjustment |
|-----------|------|------------|
| **Target glucose** | Algorithm aims for this | Lower target → more insulin, ↓ TAR, ↑ TBR risk |
| **ICR / Carb ratio** | Meal bolus calculation | Test with standard meals; adjust until 2-hr in range |
| **ISF / Correction factor** | Auto-correction aggressiveness | Usually algorithm-managed; verify |
| **Max basal rate** | Safety ceiling | Set 2–3× usual max |
| **Active insulin time** | IOB duration | 3–5h (matches insulin action) |

### Common Issues
| Issue | Cause | Fix |
|-------|-------|-----|
| **Persistent highs post-meal** | Underestimated carbs, late bolus, ICR too weak | Accurate carb count; pre-bolus 15–20 min; tighten ICR |
| **Nocturnal hypoglycaemia** | Target too low, basal max too high, over-correction | Raise target; check basal max; reduce ISF |
| **"Algorithm fighting"** | CGM noise, calibration issues, sensor compression | Ensure good CGM data; avoid compression sites |
| **Exercise hypoglycaemia** | Algorithm doesn't know exercise planned | **Exercise mode** (Tandem, Omnipod 5, CamAPS); temp target ↑ |
| **Dawn phenomenon** | Algorithm may not anticipate | 780G: meal detection helps; others: check basal profile |

---

## 7. DIY Systems (Loop, AndroidAPS, OpenAPS)

| System | Status | Key Points |
|--------|--------|------------|
| **Loop** | DIY (iPhone) | MPC algorithm; RileyLink hardware; Nightscout; large community |
| **AndroidAPS** | DIY (Android) | OpenAPS port; works with Dana RS, Accu-Chek Insight, Ypsomed |
| **OpenAPS** | DIY (Raspberry Pi/Intel Edison) | Original DIY; "WeAreNotWaiting" |

**Clinician role**: Support safety (settings review, IOB, max basal); document "off-label use"; don't discourage if patient competent.

---

## 8. Exam Pearls (FCPS/MRCP)

| Topic | Key Point |
|-------|-----------|
| **HCL = Hybrid Closed-Loop** | Automates **basal only**; user gives meal bolus |
| **PID vs MPC** | PID = reactive (Medtronic); MPC = predictive (Tandem, Omnipod, CamAPS) |
| **780G key feature** | **Auto-correction bolus** (unique); adjustable target (100/110/120) |
| **Control-IQ key feature** | **Predictive 30 min**; sleep mode target 110; exercise mode |
| **Omnipod 5** | **Tubeless** HCL; phone controller; SmartAdjust MPC |
| **CamAPS FX** | **App-based** HCL; works on multiple pumps (Ypsomed, Dana) |
| **NICE criteria HCL** | T1DM; HbA1c ≥58 OR disabling hypos; education + carb counting |
| **Evidence** | All systems: TIR +10–15%, TBR −50%, HbA1c −0.3–0.5% |
| **Exercise mode** | Raises target (e.g., 140–160) → reduces insulin delivery |
| **DIY systems** | Not regulated; support safety, don't discourage competent users |

---

## 9. Local Navigation (for Dashboard UI)
> **Parent**: [[../Insulin pump therapy (CSII)|Insulin pump therapy (CSII)]]  
> **Hierarchy**: [[../../Davidson Chapter 25 - Diabetes Hierarchy|Diabetes Hierarchy]]  
> **Template**: [[../../../Templates/Diabetes Topic Template|Diabetes Topic Template]]  
> **See also**: [[Pump types (tethered, patch, closed-loop)]], [[Automated insulin delivery (AID) systems]], [[CGM-guided insulin adjustment]], [[Continuous glucose monitoring (CGM)]]