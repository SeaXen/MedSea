---
tags: [medicine, davidson, clinical-biochemistry, acid-base, metabolic-acidosis, metabolic-alkalosis, respiratory-acidosis, respiratory-alkalosis, mixed-disorders, fcps, mrcp]
davidson_part: Part 3: Clinical Medicine
davidson_chapter: Chapter 10: Clinical Biochemistry and Metabolic Medicine
status: scaffold-hub
---

# Acid-Base Disorders
> **Chapter 10 Theme Group Hub | Acid-Base Disorders**
> Covers metabolic acidosis, metabolic alkalosis, respiratory acidosis, respiratory alkalosis, and mixed acid-base disorders.

---

## Disease-Level Topics in this Group

| # | Topic | File | Status |
|---|-------|------|--------|
| 1 | **Metabolic Acidosis** (Anion Gap, Non-Gap, Management) | `Metabolic Acidosis.md` | scaffold |
| 2 | **Metabolic Alkalosis** (Chloride-Responsive/Resistant) | `Metabolic Alkalosis.md` | scaffold |
| 3 | **Respiratory Acidosis** (Acute/Chronic, Ventilation) | `Respiratory Acidosis.md` | scaffold |
| 4 | **Respiratory Alkalosis** (Hyperventilation, Causes) | `Respiratory Alkalosis.md` | scaffold |
| 5 | **Mixed Acid-Base Disorders** (Delta Ratio, Delta-Delta) | `Mixed Acid-Base Disorders.md` | scaffold |

---

## Clinical Algorithms: Acid-Base Analysis

```
ARTERIAL BLOOD GAS (ABG) INTERPRETATION
         │
         ├── STEP 1: ASSESS pH
         │       ├── pH <7.35 → **ACIDAEMIA**
         │       └── pH >7.45 → **ALKALAEMIA**
         │
         ├── STEP 2: IDENTIFY PRIMARY DISORDER
         │       ├── ACIDAEMIA:
         │       │       ├── pCO₂ ↑ → **Respiratory Acidosis** (Primary)
         │       │       └── HCO₃⁻ ↓ → **Metabolic Acidosis** (Primary)
         │       │
         │       └── ALKALAEMIA:
         │               ├── pCO₂ ↓ → **Respiratory Alkalosis** (Primary)
         │               └── HCO₃⁻ ↑ → **Metabolic Alkalosis** (Primary)
         │
         ├── STEP 3: ASSESS COMPENSATION
         │       ├── Metabolic Acidosis → **Winter's Formula**: Expected pCO₂ = 1.5 × HCO₃⁻ + 8 ± 2
         │       ├── Metabolic Alkalosis → Expected pCO₂ = 0.7 × HCO₃⁻ + 20 ± 5
         │       ├── Respiratory Acidosis (Acute): HCO₃⁻ ↑ 1 mmol/L per 10 mmHg pCO₂ ↑
         │       ├── Respiratory Acidosis (Chronic): HCO₃⁻ ↑ 4 mmol/L per 10 mmHg pCO₂ ↑
         │       ├── Respiratory Alkalosis (Acute): HCO₃⁻ ↓ 2 mmol/L per 10 mmHg pCO₂ ↓
         │       └── Respiratory Alkalosis (Chronic): HCO₃⁻ ↓ 5 mmol/L per 10 mmHg pCO₂ ↓
         │
         └── STEP 4: IDENTIFY SECOND DISORDER (Mixed)
                 ├── Calculate Anion Gap & Delta Ratio (for Metabolic Acidosis)
                 ├── Delta Ratio = ΔAG / ΔHCO₃⁻
                 │       ├── 1-2 → Pure AGMA
                 │       ├── <0.4 → AGMA + NAGMA
                 │       └── >2 → AGMA + Metabolic Alkalosis
                 └── Delta-Delta: Corrected HCO₃⁻ = Measured HCO₃⁻ + ΔAG
```

---

## Clinical Algorithms: Specific Disorders

### Metabolic Acidosis

```
METABOLIC ACIDOSIS (HCO₃⁻ <22, pH <7.35)
         │
         ├── CALCULATE ANION GAP (AG = Na⁺ - Cl⁻ - HCO₃⁻)
         │       ├── **HIGH AG (>12)** → **HIGH AG METABOLIC ACIDOSIS (AGMA)**
         │       │       ├── **MUDPILES** Mnemonic:
         │       │       │       ├── M: Methanol
         │       │       │       ├── U: Uraemia
         │       │       │       ├── D: DKA (Diabetic Ketoacidosis)
         │       │       │       ├── P: Paraldehyde / Propylene Glycol
         │       │       │       ├── I: Iron / Isoniazid
         │       │       │       ├── L: Lactic Acidosis (Type A: Hypoperfusion; Type B: Metabolic)
         │       │       │       ├── E: Ethylene Glycol / Ethanol
         │       │       │       └── S: Salicylates / Sepsis
         │       │       │
         │       │       └── **CALCULATE DELTA RATIO** (ΔAG / ΔHCO₃⁻)
         │       │               ├── 1-2 → Pure AGMA
         │       │               ├── <0.4 → AGMA + NAGMA
         │       │               └── >2 → AGMA + Metabolic Alkalosis
         │       │
         │       └── **NORMAL AG (8-12)** → **NORMAL AG METABOLIC ACIDOSIS (NAGMA)**
         │               ├── **HARDASS** Mnemonic:
         │               │       ├── H: Hyperalimentation (TPN)
         │               │       ├── A: Acetazolamide
         │               │       ├── R: Renal Tubular Acidosis (RTA)
         │               │       ├── D: Diarrhoea
         │               │       ├── A: Adrenal Insufficiency (Addison's)
         │               │       └── S: Saline Infusion (0.9% NaCl → Hyperchloraemic)
         │               └── Spironolactone / Ureteric Diversion
         │
         └── MANAGEMENT
                 ├── Treat Underlying Cause
                 └── **Bicarbonate Indications**: pH <7.1 / Severe AKI / Severe Sepsis / Cardiac Arrest
                     └── 8.4% NaHCO₃: 50-100 mmol over 30-60 min (Target pH >7.2)
```

### Metabolic Alkalosis

```
METABOLIC ALKALOSIS (HCO₃⁻ >26, pH >7.45)
         │
         ├── URINE CHLORIDE (<20 vs >20 mmol/L)
         │       ├── **Urine Cl⁻ <20** → **CHLORIDE-RESPONSIVE** (Volume Depleted)
         │       │       ├── Vomiting / NG Suction
         │       │       ├── Diuretic Use (Post-Diuretic Phase)
         │       │       ├── Post-Hypercapnic State
         │       │       └── **MANAGEMENT**: 0.9% NaCl + KCl Replacement
         │       │
         │       └── **Urine Cl⁻ >20** → **CHLORIDE-RESISTANT** (Volume Normal/Expanded)
         │               ├── Primary Hyperaldosteronism (Conn's)
         │               ├── Cushing's Syndrome
         │               ├── Bartter / Gitelman Syndrome
         │               ├── Liquorice / Carbenoxolone
         │               ├── Severe Hypokalaemia (Maintains Alkalosis)
         │               └── **MANAGEMENT**: Treat Cause + Acetazolamide / Amiloride / Spironolactone
         │
         └── MAINTENANCE FACTORS (Why Alkalosis Persists)
                 ├── Volume Depletion → ↑ Aldosterone → ↑ H⁺ Secretion
                 ├── Hypokalaemia → H⁺ Shift In / K⁺ Shift Out → ↑ Renal HCO₃⁻ Reabsorption
                 └── Hypochloraemia → ↓ Cl⁻/HCO₃⁻ Exchange → ↑ HCO₃⁻ Reabsorption
```

### Respiratory Acidosis

```
RESPIRATORY ACIDOSIS (pCO₂ >6.0 kPa / 45 mmHg, pH <7.35)
         │
         ├── ACUTE vs CHRONIC (Compensation)
         │       ├── **Acute**: HCO₃⁻ ↑ 1 mmol/L per 10 mmHg pCO₂ ↑
         │       │       └── Expected pH ↓ 0.08 per 10 mmHg pCO₂ ↑
         │       │
         │       └── **Chronic**: HCO₃⁻ ↑ 4 mmol/L per 10 mmHg pCO₂ ↑
         │               └── Expected pH ↓ 0.03 per 10 mmHg pCO₂ ↑
         │
         ├── CAUSES
         │       ├── **Airway Obstruction** (COPD, Asthma, Croup, Foreign Body)
         │       ├── **Hypoventilation** (Obesity Hypoventilation, CNS Depression, Neuromuscular)
         │       ├── **Respiratory Centre Depression** (Opiates, Sedatives, Stroke)
         │       └── **Mechanical Ventilation** (Inadequate Settings)
         │
         └── MANAGEMENT
                 ├── Treat Underlying Cause (Bronchodilators, Steroids, NIV/Intubation)
                 ├── **Non-Invasive Ventilation (NIV)** → 1st Line for COPD Exacerbation
                 ├── **Intubation** if pH <7.25, GCS <8, Exhaustion
                 └── **Avoid Excessive O₂** in COPD (Risk of ↑ pCO₂)
```

### Respiratory Alkalosis

```
RESPIRATORY ALKALOSIS (pCO₂ <4.5 kPa / 35 mmHg, pH >7.45)
         │
         ├── ACUTE vs CHRONIC
         │       ├── **Acute**: HCO₃⁻ ↓ 2 mmol/L per 10 mmHg pCO₂ ↓
         │       └── **Chronic**: HCO₃⁻ ↓ 5 mmol/L per 10 mmHg pCO₂ ↓
         │
         ├── CAUSES
         │       ├── **Hyperventilation** (Anxiety, Pain, Panic, Hysteria)
         │       ├── **CNS** (Stroke, Tumour, Meningitis, Encephalitis)
         │       ├── **Pulmonary** (PE, Pneumonia, Interstitial Lung Disease)
         │       ├── **Drugs** (Salicylates, Progesterone, Caffeine, Theophylline)
         │       ├── **Sepsis** (Early), **Pregnancy**, **Hepatic Encephalopathy**
         │       └── **Mechanical Ventilation** (Excessive Rate/Tidal Volume)
         │
         └── MANAGEMENT
                 ├── Treat Underlying Cause
                 ├── **Rebreathing (Paper Bag)** for Anxiety-Induced
                 ├── Treat Pain, Sepsis, PE, Salicylate Toxicity
                 └── **Reduce Ventilator Rate/Tidal Volume** if Iatrogenic
```

### Mixed Acid-Base Disorders

```
MIXED ACID-BASE DISORDERS
         │
         ├── STEP 1: Primary Disorder (pH, Primary Parameter)
         ├── STEP 2: Assess Compensation (Expected vs Actual)
         ├── STEP 3: Anion Gap + Delta Ratio (if Metabolic Acidosis Present)
         │       ├── **Delta Ratio** = ΔAG / ΔHCO₃⁻
         │       │       ├── 1-2 → Pure High AG Metabolic Acidosis
         │       │       ├── <0.4 → AGMA + NAGMA
         │       │       ├── 0.4-0.8 → AGMA + NAGMA (Mild)
         │       │       └── >2 → AGMA + Metabolic Alkalosis
         │       │
         │       └── **Delta-Delta** (Corrected HCO₃⁻ = Measured HCO₃⁻ + ΔAG)
         │               ├── Corrected HCO₃⁻ >24 → Concurrent Metabolic Alkalosis
         │               └── Corrected HCO₃⁻ <24 → Concurrent NAGMA
         │
         ├── COMMON MIXED PATTERNS
         │       ├── **AGMA + NAGMA** (e.g., DKA + Diarrhoea/Renal Failure)
         │       ├── **AGMA + Metabolic Alkalosis** (e.g., DKA + Vomiting/Diuretics)
         │       ├── **Metabolic Acidosis + Respiratory Alkalosis** (e.g., Salicylate Toxicity, Sepsis)
         │       ├── **Metabolic Alkalosis + Respiratory Acidosis** (e.g., COPD + Diuretics/Vomiting)
         │       └── **Triple Disorders** (e.g., COPD + Diuretics + DKA)
         │
         └── APPROACH
                 ├── Identify All Components
                 ├── Treat Each Underlying Cause
                 └── Prioritise Life-Threatening Components (Severe Acidosis, Hypoxia)
```

---

## Key Formulae & Compensation Rules

| Disorder | Expected Compensation |
|----------|----------------------|
| **Metabolic Acidosis** | **Winter's Formula**: Expected pCO₂ = 1.5 × HCO₃⁻ + 8 ± 2 |
| **Metabolic Alkalosis** | Expected pCO₂ = 0.7 × HCO₃⁻ + 20 ± 5 (Max 55-60 mmHg) |
| **Respiratory Acidosis (Acute)** | HCO₃⁻ ↑ 1 mmol/L per 10 mmHg pCO₂ ↑ |
| **Respiratory Acidosis (Chronic)** | HCO₃⁻ ↑ 4 mmol/L per 10 mmHg pCO₂ ↑ |
| **Respiratory Alkalosis (Acute)** | HCO₃⁻ ↓ 2 mmol/L per 10 mmHg pCO₂ ↓ |
| **Respiratory Alkalosis (Chronic)** | HCO₃⁻ ↓ 5 mmol/L per 10 mmHg pCO₂ ↓ |

---

## Key Formulae & Cut-offs

| Parameter | Formula / Value |
|-----------|-----------------|
| **Anion Gap** | AG = Na⁺ - (Cl⁻ + HCO₃⁻) [Normal 8-12 mmol/L] |
| **Corrected AG (Hypoalbuminaemia)** | AG + 2.5 × (40 - Albumin g/L) |
| **Delta Ratio** | ΔAG / ΔHCO₃⁻ (1-2 = Pure AGMA; <0.4 = AGMA+NAGMA; >2 = AGMA+Met Alk) |
| **Delta-Delta** | Corrected HCO₃⁻ = Measured HCO₃⁻ + ΔAG |
| **Winter's Formula** | Expected pCO₂ = 1.5 × HCO₃⁻ + 8 ± 2 |
| **Urine Chloride** | <20 mmol/L = Chloride-Responsive; >20 = Chloride-Resistant (Metabolic Alkalosis) |
| **Expected pCO₂ (Met Alkalosis)** | 0.7 × HCO₃⁻ + 20 ± 5 (Max ~55 mmHg) |
| **Base Excess** | Normal -2 to +2 mmol/L |
| **pH/pCO₂ Relationship** | pH changes 0.08 per 10 mmHg pCO₂ (Acute Resp Acid); 0.03 (Chronic) |

---

## Local Navigation

> **Parent**: [Davidson Chapter 10 Hierarchy](./Davidson Chapter 10 - Clinical Biochemistry and Metabolic Medicine Hierarchy.md)  
> **Template**: `../../Templates/Clinical Biochemistry Topic Template.md`  
> **See also**: [Calcium Magnesium Phosphate](./Calcium Magnesium Phosphate.md) | [Sodium & Water Balance](../Sodium and Water Balance.md)