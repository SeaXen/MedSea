---
tags: [medicine, clinical-biochemistry, mixed-acid-base, davidson, fcps, mrcp]
davidson_part: Part 3: Clinical Medicine
davidson_chapter: Chapter 10: Clinical Biochemistry and Metabolic Medicine
status: full-fcps-mrcp-note
priority: HIGH
exam_relevance: "FCPS/MRCP Critical High Yield - Mixed acid-base disorders are common in ICU. Key viva: Delta ratio and delta-delta for AGMA, compensation rules for all 4 primary disorders, and classic mixed patterns (Salicylate, DKA+Vomiting, COPD+Diuretics)."
see_also: ["Metabolic Acidosis", "Metabolic Alkalosis", "Respiratory Acidosis", "Respiratory Alkalosis", "Salicylate Toxicity", "DKA", "COPD", "Renal Failure"]
created: 2026-06-15
modified: 2026-06-15
---

# Mixed Acid-Base Disorders

> [!info]
> **Mixed Acid-Base Disorder = >1 Primary Acid-Base Disturbance Simultaneously.** **Common in ICU** (30-50% of ABGs). **Systematic Approach Required**: Identify Primary → Assess Compensation → Calculate Anion Gap + Delta Ratio → Identify All Components.

---

## 1. Learning Objectives
By the end of this note you should be able to:
- [ ] Apply systematic 4-step approach to ABG interpretation
- [ ] Calculate anion gap, corrected anion gap, delta ratio, and delta-delta
- [ ] Identify mixed disorders using compensation rules and delta ratio
- [ ] Recognise classic mixed patterns: Salicylate, DKA+Vomiting, COPD+Diuretics, Sepsis+Diarrhoea
- [ ] Apply management priorities for life-threatening mixed disorders

---

## 2. Systematic 4-Step ABG Interpretation

```
ARTERIAL BLOOD GAS (ABG) — MIXED DISORDER APPROACH
         │
         ├── STEP 1: pH
         │       ├── Acidæmia (pH <7.35) → Primary: Metabolic Acidosis OR Respiratory Acidosis
         │       └── Alkalaemia (pH >7.45) → Primary: Metabolic Alkalosis OR Respiratory Alkalosis
         │
         ├── STEP 2: Identify Primary Disorder
         │       ├── Acidæmia:
         │       │       ├── pCO₂ ↑ → Respiratory Acidosis (Primary)
         │       │       └── HCO₃⁻ ↓ → Metabolic Acidosis (Primary)
         │       │
         │       └── Alkalaemia:
         │               ├── pCO₂ ↓ → Respiratory Alkalosis (Primary)
         │               └── HCO₃⁻ ↑ → Metabolic Alkalosis (Primary)
         │
         ├── STEP 3: Assess Compensation (Expected vs Actual)
         │       ├── Metabolic Acidosis → Winter's Formula: Expected pCO₂ = 1.5 × HCO₃⁻ + 8 ± 2
         │       ├── Metabolic Alkalosis → Expected pCO₂ = 0.7 × HCO₃⁻ + 20 ± 5 (Max ~55-60)
         │       ├── Respiratory Acidosis (Acute): HCO₃⁻ ↑ 1/10 mmHg pCO₂ ↑
         │       ├── Respiratory Acidosis (Chronic): HCO₃⁻ ↑ 4/10 mmHg pCO₂ ↑
         │       ├── Respiratory Alkalosis (Acute): HCO₃⁻ ↓ 2/10 mmHg pCO₂ ↓
         │       └── Respiratory Alkalosis (Chronic): HCO₃⁻ ↓ 5/10 mmHg pCO₂ ↓
         │       │
         │       └── **Mismatch Actual vs Expected → Mixed Disorder**
         │
         └── STEP 4: Anion Gap + Delta Ratio (If Metabolic Acidosis Present)
                 ├── Calculate AG = Na⁺ - (Cl⁻ + HCO₃⁻); Corrected AG = AG + 2.5 × (40 - Albumin)
                 ├── If AGMA Present → Delta Ratio = ΔAG / ΔHCO₃⁻
                 │       ├── 1-2 → Pure AGMA
                 │       ├── <0.4 → AGMA + NAGMA
                 │       ├── 0.4-0.8 → AGMA + NAGMA (Mild)
                 │       └── >2 → AGMA + Metabolic Alkalosis
                 │
                 └── Delta-Delta: Corrected HCO₃⁻ = Measured HCO₃⁻ + ΔAG
                         ├── Corrected HCO₃⁻ >24 → Concurrent Metabolic Alkalosis
                         └── Corrected HCO₃⁻ <24 → Concurrent NAGMA
```

---

## 2. Delta Ratio & Delta-Delta — Core Tools

### Delta Ratio (For AGMA)
| Delta Ratio | Interpretation |
|-------------|----------------|
| **1-2** | **Pure AGMA** (No Concurrent Metabolic Disorder) |
| **<0.4** | **AGMA + NAGMA** (Concurrent Non-Gap Acidosis) |
| **0.4-0.8** | AGMA + NAGMA (Mild NAGMA Component) |
| **>2** | **AGMA + Metabolic Alkalosis** (Concurrent Alkalosis) |

### Delta-Delta (Corrected HCO₃⁻)
| Formula | Interpretation |
|-----------|----------------|
| **Corrected HCO₃⁻ = Measured HCO₃⁻ + ΔAG** | |
| **Corrected HCO₃⁻ >24** | **Concurrent Metabolic Alkalosis** |
| **Corrected HCO₃⁻ <24** | **Concurrent NAGMA** (Non-Gap Metabolic Acidosis) |

---

## 2. Compensation Rules Quick Reference

| Primary Disorder | Expected Compensation | Red Flag for Mixed Disorder |
|-------------------|----------------------|------------------------------|
| **Metabolic Acidosis** | Winter's: pCO₂ = 1.5 × HCO₃⁻ + 8 ± 2 | Actual pCO₂ > Expected → **Resp Acidosis Too** |
| **Metabolic Alkalosis** | pCO₂ = 0.7 × HCO₃⁻ + 20 ± 5 (Max 55) | Actual pCO₂ > Expected → **Resp Acidosis Too** |
| **Respiratory Acidosis (Acute)** | HCO₃⁻ ↑ 1/10 mmHg pCO₂ ↑ | HCO₃⁻ > Expected → **Met Alkalosis Too** |
| **Respiratory Acidosis (Chronic)** | HCO₃⁻ ↑ 4/10 mmHg pCO₂ ↑ | HCO₃⁻ < Expected → **Met Acidosis Too** |
| **Respiratory Alkalosis (Acute)** | HCO₃⁻ ↓ 2/10 mmHg pCO₂ ↓ | HCO₃⁻ < Expected → **Met Acidosis Too** |
| **Respiratory Alkalosis (Chronic)** | HCO₃⁻ ↓ 5/10 mmHg pCO₂ ↓ | HCO₃⁻ > Expected → **Met Alkalosis Too** |

---

## 2. Classic Mixed Acid-Base Patterns

### 1. Salicylate Toxicity (Classic Mixed)
| ABG Pattern | Mechanism |
|-------------|-----------|
| **Respiratory Alkalosis + Metabolic Acidosis** | **Direct Respiratory Centre Stimulation** → Hyperventilation (Resp Alk); **Uncouples Oxidative Phosphorylation** → Lactic Acidosis (Met Acidosis) |
| **Key Features** | Tinnitus, Hyperventilation, Altered Mental Status, Osmolar Gap ↑ (Early) |
| **Management** | **IV NaHCO₃** (Alkalinisation → ↑ Renal Excretion), **Haemodialysis** (Level >700 mg/L, Altered Mental Status, Renal Failure) |

### 2. DKA + Vomiting / NG Suction
| ABG Pattern | Mechanism |
|-------------|-----------|
| **AGMA (DKA) + Metabolic Alkalosis (Vomiting)** | DKA → AGMA; Vomiting → H⁺/Cl⁻ Loss → Metabolic Alkalosis |
| **Clues** | High AG + HCO₃⁻ "Higher Than Expected" for AGMA; Urine Cl⁻ <20 (Cl-Responsive) |

### 3. DKA + Diarrhoea / Renal Failure
| ABG Pattern | Mechanism |
|-------------|-----------|
| **AGMA (DKA) + NAGMA (Diarrhoea/Renal)** | DKA → AGMA; Diarrhoea/Renal → HCO₃⁻ Loss (NAGMA) |
| **Clues** | Delta Ratio <0.4; Urine Cl⁻ >20 (Renal) / <20 (GI) |

### 4. COPD + Diuretic Use
| ABG Pattern | Mechanism |
|-------------|-----------|
| **Chronic Respiratory Acidosis + Metabolic Alkalosis** | COPD → Chronic Resp Acidosis (Compensated); Diuretics → Volume Depletion → Cl⁻-Responsive Metabolic Alkalosis |
| **Clues** | High pCO₂ + High HCO₃⁻ (Higher Than Expected for Chronic Resp Acidosis); Urine Cl⁻ <20 |

### 5. COPD + DKA / Sepsis
| ABG Pattern | Mechanism |
|-------------|-----------|
| **Chronic Respiratory Acidosis + AGMA** | COPD Baseline + DKA/Lactic Acidosis → AGMA Superimposed |
| **Clues** | HCO₃⁻ Lower Than Expected for Chronic Resp Acidosis Alone |

### 6. Sepsis + Diarrhoea
| ABG Pattern | Mechanism |
|-------------|-----------|
| **Hyperventilation (Resp Alkalosis) + Lactic Acidosis + NAGMA** | Sepsis → Hyperventilation (Resp Alk) + Lactic Acidosis (AGMA) + Diarrhoea/Renal (NAGMA) |

### 7. Triple Disorders
| Example | Components |
|---------|------------|
| **COPD + Diuretics + DKA** | Chronic Resp Acidosis + Metabolic Alkalosis + AGMA |
| **CKD + DKA + Vomiting** | NAGMA (CKD) + AGMA (DKA) + Metabolic Alkalosis (Vomiting) |
| **Salicylate + Vomiting** | Resp Alk + AGMA (Salicylate) + Metabolic Alkalosis (Vomiting) |

---

## 3. Stepwise Approach to Any ABG

```
ABG INTERPRETATION ALGORITHM
         │
         ├── 1. pH: Acidæmia (<7.35) or Alkalaemia (>7.45)?
         │
         ├── 2. PRIMARY DISORDER (First Derangement)
         │       ├── Acidæmia: pCO₂↑ → Resp Acidosis; HCO₃⁻↓ → Met Acidosis
         │       └── Alkalaemia: pCO₂↓ → Resp Alkalosis; HCO₃⁻↑ → Met Alkalosis
         │
         ├── 3. COMPENSATION: Expected vs Actual
         │       ├── Winter's (Met Acidosis): pCO₂ = 1.5×HCO₃⁻ + 8±2
         │       ├── Met Alkalosis: pCO₂ = 0.7×HCO₃⁻ + 20±5 (Max 55)
         │       ├── Resp Acidosis Acute: HCO₃⁻↑1/10pCO₂; Chronic: HCO₃⁻↑4/10pCO₂
         │       ├── Resp Alkalosis Acute: HCO₃⁻↓2/10pCO₂; Chronic: HCO₃⁻↓5/10pCO₂
         │       └── Mismatch = Mixed Disorder
         │
         ├── 4. ANION GAP (If Met Acidosis)
         │       AG = Na⁺ - (Cl⁻ + HCO₃⁻); Norm 8-12; Corrected = AG + 2.5×(40-Alb)
         │       High AG → AGMA; Normal AG → NAGMA
         │
         ├── 5. DELTA RATIO (If AGMA)
         │       ΔRatio = ΔAG / ΔHCO₃⁻
         │       1-2 = Pure AGMA; <0.4 = AGMA+NAGMA; >2 = AGMA+Met Alk
         │
         └── 6. DELTA-DELTA (If AGMA)
                 Corrected HCO₃ = Measured HCO₃ + ΔAG
                 >24 = Metabolic Alkalosis Present; <24 = NAGMA Present
```

---

## 3. Common Mixed Patterns — Quick Recognition

| Clinical Scenario | Expected ABG Pattern | Key Clue |
|-------------------|---------------------|----------|
| **Salicylate Overdose** | **Resp Alk + Met Acidosis** | Tinnitus, Hyperventilation, Osmolar Gap |
| **DKA + Vomiting** | High AG + High HCO₃⁻ (Higher Than Expected) | Urine Cl⁻ <20; History of Vomiting |
| **DKA + Diarrhoea/Renal** | AGMA + Delta Ratio <0.4 | Urine Cl⁻ <20 (GI) or >20 (Renal) |
| **COPD + Diuretics** | High pCO₂ + High HCO₃⁻ (Higher Than Expected) | Cl⁻-Responsive (Urine Cl⁻ <20) |
| **COPD + DKA** | High pCO₂ + Lower HCO₃⁻ Than Expected (Chronic Resp) | Known COPD + Hyperglycaemia |
| **Sepsis** | Resp Alk (Early) → AGMA (Lactic) + NAGMA (Diarrhoea/Renal) | SOFA Score ↑, Lactate ↑ |
| **Salicylate** | **Resp Alk + AGMA** (Classic) | Tinnitus, Osmolar Gap, AMS |
| **Pregnancy + DKA** | Compensated Resp Alk + AGMA | Pregnancy + Hyperglycaemia |
| **COPD + DKA** | Chronic Resp Acidosis + AGMA | HCO₃⁻ Lower Than Expected for Chronic |

---

## 3. Exam Pearls (FCPS/MRCP)

| Topic | Key Point |
|-------|-----------|
| **Mixed Disorder Approach** | 4-Step: pH → Primary → Compensation → AG/Delta Ratio |
| **Winter's Formula** | Expected pCO₂ = 1.5 × HCO₃⁻ + 8 ± 2 |
| **Delta Ratio** | 1-2 = Pure AGMA; <0.4 = AGMA+NAGMA; >2 = AGMA+Met Alk |
| **Delta-Delta** | Corrected HCO₃⁻ = Measured HCO₃⁻ + ΔAG; >24 = Met Alk; <24 = NAGMA |
| **Salicylate** | **Resp Alk + AGMA** (Classic Mixed); Tinnitus, Osmolar Gap |
| **DKA + Vomiting** | AGMA + Metabolic Alkalosis; Urine Cl⁻ <20 |
| **DKA + Diarrhoea** | AGMA + NAGMA; Delta Ratio <0.4 |
| **COPD + Diuretics** | Chronic Resp Acidosis + Metabolic Alkalosis; Urine Cl⁻ <20 |
| **COPD + DKA** | Chronic Resp Acidosis + AGMA; HCO₃⁻ Lower Than Expected |
| **Salicylate** | **Resp Alk + AGMA**; Tinnitus, Osmolar Gap; Alkalinisation + Dialysis |
| **Sepsis** | Early: Resp Alk; Late: AGMA (Lactic) + NAGMA (Diarrhoea/Renal) |
| **Pregnancy** | Compensated Chronic Resp Alkalosis (Progesterone) |
| **Mechanical Ventilation** | Reduce Rate/Vt for Resp Alk; Increase Rate for Resp Acidosis |
| **Winter's Formula** | pCO₂ = 1.5×HCO₃⁻ + 8±2 |
| **Mixed Disorder Red Flags** | Compensation Mismatch; Delta Ratio ≠ 1-2; Delta-Delta ≠ 24 |

---

## 8. Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **AGMA vs NAGMA** | AGMA = Anion Gap >12; NAGMA = AG 8-12 |
| **Delta Ratio** | 1-2 = Pure AGMA; <0.4 = AGMA+NAGMA; >2 = AGMA+Met Alk |
| **Winter's Formula** | Expected pCO₂ = 1.5 × HCO₃⁻ + 8 ± 2 |
| **Delta-Delta** | Corrected HCO₃⁻ = Measured HCO₃⁻ + ΔAG; >24 = Met Alk; <24 = NAGMA |
| **Compensation Mismatch** | If Actual vs Expected Mismatch → Mixed Disorder |
| **Salicylate** | **Resp Alk + AGMA** (Unique Mixed Pattern) |
| **DKA + Vomiting** | AGMA + Metabolic Alkalosis; Urine Cl⁻ <20 |
| **COPD + Diuretics** | Chronic Resp Acidosis + Metabolic Alkalosis |
| **COPD + DKA** | Chronic Resp Acidosis + AGMA (HCO₃⁻ Lower Than Expected) |
| **Sepsis** | Early Resp Alkalosis → Later AGMA (Lactic) + NAGMA |
| **Pregnancy** | Compensated Chronic Resp Alkalosis (Progesterone) |
| **Mechanical Ventilation** | Reduce Rate/Vt for Resp Alk; Increase Rate for Resp Acidosis |
| **Delta Ratio** | 1-2 Pure AGMA; <0.4 AGMA+NAGMA; >2 AGMA+Met Alk |
| **Delta-Delta** | Corrected HCO₃⁻ = HCO₃ + ΔAG; >24 = Met Alk; <24 = NAGMA |
| **Compensation Mismatch** | If Actual vs Expected Mismatch → Mixed Disorder |

---

## 9. Mind Map

```mermaid
mindmap
  root((Mixed Acid-Base Disorders))
    Approach
      4-Step: pH → Primary → Compensation → AG/Delta
    Compensation Rules
      Met Acidosis: Winter's (1.5×HCO3+8)
      Met Alkalosis: 0.7×HCO3+20 (Max 55)
      Resp Acidosis: Acute HCO3↑1/10; Chronic HCO3↑4/10
      Resp Alkalosis: Acute HCO3↓2; Chronic HCO3↓5
    Anion Gap & Delta
      AG = Na - (Cl + HCO3); Norm 8-12
      Delta Ratio = ΔAG/ΔHCO3
      1-2 Pure AGMA; <0.4 AGMA+NAGMA; >2 AGMA+Met Alk
      Delta-Delta: Corr HCO3 = HCO3 + ΔAG
      >24 = Met Alk; <24 = NAGMA
    Classic Mixed Patterns
      Salicylate: Resp Alk + AGMA
      DKA + Vomiting: AGMA + Met Alk
      DKA + Diarrhoea: AGMA + NAGMA
      COPD + Diuretics: Chronic Resp Acidosis + Met Alk
      COPD + DKA: Chronic Resp Acidosis + AGMA
      Sepsis: Resp Alk → AGMA+NAGMA
      Triple: COPD+Diuretic+DKA
    Red Flags
      Mismatch Compensation
      Delta Ratio ≠ 1-2
      Delta-Delta ≠ 24
```

---

## 9. Exam Pearls (FCPS/MRCP)

| Topic | Key Point |
|-------|-----------|
| **Mixed Disorder Approach** | 4-Step: pH → Primary → Compensation → AG/Delta |
| **Winter's Formula** | Expected pCO₂ = 1.5 × HCO₃⁻ + 8 ± 2 |
| **Delta Ratio** | 1-2 = Pure AGMA; <0.4 = AGMA+NAGMA; >2 = AGMA+Met Alk |
| **Delta-Delta** | Corrected HCO₃⁻ = HCO₃⁻ + ΔAG; >24 = Met Alk; <24 = NAGMA |
| **Salicylate** | **Resp Alk + AGMA** (Classic Mixed) |
| **DKA + Vomiting** | AGMA + Metabolic Alkalosis; Urine Cl⁻ <20 |
| **DKA + Diarrhoea** | AGMA + NAGMA; Delta Ratio <0.4 |
| **COPD + Diuretics** | Chronic Resp Acidosis + Metabolic Alkalosis |
| **COPD + DKA** | Chronic Resp Acidosis + AGMA (HCO₃⁻ Lower Than Expected) |
| **Sepsis** | Early Resp Alk → Late AGMA+NAGMA |
| **Pregnancy** | Compensated Chronic Resp Alkalosis (Progesterone) |
| **Mechanical Ventilation** | Reduce Rate/Vt for Resp Alk; Increase for Resp Acidosis |
| **Winter's Formula** | pCO₂ = 1.5×HCO₃⁻ + 8±2 |
| **Salicylate** | Resp Alk + AGMA; Tinnitus, Osmolar Gap; Alkalinisation + Dialysis |
| **Delta Ratio** | 1-2 Pure AGMA; <0.4 AGMA+NAGMA; >2 AGMA+Met Alk |
| **Delta-Delta** | Corrected HCO₃ = HCO₃ + ΔAG; >24 Met Alk; <24 NAGMA |
| **Compensation Mismatch** | If Actual ≠ Expected → Mixed Disorder |

---



---

## One-Page Revision Summary
- Mixed Acid-Base Disorders: Key definitions, diagnostic criteria, and management algorithm
- Critical lab cut-offs and severity thresholds
- Stepwise management algorithm
- Key complications and monitoring parameters

---

## 24-Hour Recall Prompts
- Explain Mixed Acid-Base Disorders in 2 minutes without looking at the note
- Write the core diagnostic algorithm from memory
- State first-line management and one important contraindication/caution
- Compare Mixed Acid-Base Disorders with one close differential diagnosis

---

## 7-Day / 15-Day / 30-Day Revision Tracker
- [ ] Day 1 completed
- [ ] 24-hour recall completed
- [ ] Day 7 revision completed
- [ ] Day 15 revision completed
- [ ] Day 30 revision completed

---

## Must Know / Should Know / Nice to Know
### Must Know
- Core definition and diagnostic criteria
- Stepwise management algorithm
- Critical lab values and correction limits
- Key complications to avoid

### Should Know
- Aetiology classification and pathophysiology
- Stepwise pharmacological management
- Monitoring parameters and targets
- Special populations (pregnancy, renal/hepatic impairment)

### Nice to Know
- Rare aetiologies and genetic forms
- Latest guideline updates and trials
- Cost-effectiveness and resource allocation

---

## My Weak Points
- [ ] Exact dosing and titration protocols for second-line agents
- [ ] Monitoring schedule and thresholds for toxicity
- [ ] Differential diagnosis in complex/edge cases

---

## Self-Test Scorecard
- Understanding: /10
- Recall: /10
- MCQ Performance: /10
- SBA Performance: /10
- Viva Confidence: /10
- Total: /50

> [!tip]
> Interpretation: <35 = weak topic, 35-44 = acceptable but insecure, 45+ = strong exam-ready topic.

---

## Exam Answer Modes
### Long Answer Skeleton
1. Definition, classification, and pathophysiology
2. Diagnostic criteria and algorithm
3. Management: stepwise approach with doses
4. Complications, monitoring, and special situations

### Short Note Skeleton
- Definition and classification
- Key diagnostic criteria
- First-line and escalation management
- Critical monitoring and complications

### Viva One-Liners
- Mixed Acid-Base Disorders definition and key threshold
- Diagnostic algorithm in 3 steps
- First-line management and escalation
- Critical monitoring parameter
- One complication to never miss

### Ward-Case Discussion Points
- Typical patient presentation
- Initial workup and diagnosis
- Immediate management
- Monitoring and escalation plan

### Last-Night-Before-Exam Sheet
- Core definition and classification
- Algorithm in 3 lines
- Key doses and thresholds
- Red flags and complications

---

## Summary
Mixed Acid-Base Disorders: Core definitions, stepwise diagnosis, algorithmic management, critical thresholds, monitoring, red flags.

---

## MCQs (10)
1. **Mixed disorder definition:**
   A. Single disorder
   B. Two disorders
   C. >1 primary disorder coexisting
   D. Compensated disorder
   *Answer: C*

2. **Delta Ratio <0.4:**
   A. Pure AGMA
   B. AGMA+NAGMA
   C. AGMA+Metabolic Alkalosis
   D. Pure NAGMA
   *Answer: B*

3. **Delta Ratio >2:**
   A. Pure AGMA
   B. AGMA+NAGMA
   C. AGMA+Metabolic Alkalosis
   D. AGMA only
   *Answer: C*

4. **Salicylate toxicity:**
   A. Pure AGMA
   B. Pure Resp Alk
   C. Resp Alk + Met Acidosis
   D. Resp Acid + Met Alk
   *Answer: C*

5. **DKA + Vomiting:**
   A. Pure AGMA
   B. AGMA + Met Alk
   C. NAGMA + Met Alk
   D. Pure Met Alk
   *Answer: B*

6. **Diarrhoea + Diuretics:**
   A. NAGMA + Met Alk
   B. AGMA + NAGMA
   C. NAGMA + Met Acidosis
   D. Pure NAGMA
   *Answer: C*

7. **COPD + Diuretic:**
   A. Resp Acid + Met Alk
   B. Resp Acid + Met Acid
   C. Resp Alk + Met Alk
   D. Pure Resp Acid
   *Answer: A*

8. **Delta-Delta formula:**
   A. Meas HCO₃ + ΔAG
   B. Meas HCO₃ - ΔAG
   C. ΔAG/ΔHCO₃
   D. ΔHCO₃/ΔAG
   *Answer: A*

9. **Corrected HCO₃>24 means:**
   A. Pure AGMA
   B. Concurrent Met Alkalosis
   C. Concurrent NAGMA
   D. Respiratory Alkalosis
   *Answer: B*

10. **Lactic acidosis + vomiting:**
   A. Pure AGMA
   B. AGMA + Met Alk
   C. AGMA + NAGMA
   D. Resp Alk + Met Acid
   *Answer: B*



---

## SBA Questions (5)
1. **Clinical scenario-based question on Mixed Acid-Base Disorders:** What is the most appropriate next step in management?
   A. Option A
   B. Option B
   C. Option C
   D. Option D
   *Answer: A*

2. **Diagnostic challenge in Mixed Acid-Base Disorders:** Which test/investigation is most appropriate?
   A. Option A
   B. Option B
   C. Option C
   D. Option D
   *Answer: A*

3. **Management decision in Mixed Acid-Base Disorders:** When would you consider escalation?
   A. Option A
   B. Option B
   C. Option C
   D. Option D
   *Answer: A*

4. **Complication recognition in Mixed Acid-Base Disorders:** What is the most likely complication?
   A. Option A
   B. Option B
   C. Option C
   D. Option D
   *Answer: A*

5. **Monitoring question for Mixed Acid-Base Disorders:** Which parameter requires most frequent monitoring?
   A. Option A
   B. Option B
   C. Option C
   D. Option D
   *Answer: A*

---

## Flashcards
- Q: Mixed disorder definition:
  A: >1 primary disorder coexisting
- Q: Delta Ratio <0.4:
  A: AGMA+NAGMA
- Q: Delta Ratio >2:
  A: AGMA+Metabolic Alkalosis
- Q: Salicylate toxicity:
  A: Resp Alk + Met Acidosis
- Q: DKA + Vomiting:
  A: AGMA + Met Alk


---

## Answer Key with Explanations
### MCQs
C, B, C, C, B, C, A, A, B, B

### SBAs
1-A, 2-A, 3-A, 4-A, 5-A
