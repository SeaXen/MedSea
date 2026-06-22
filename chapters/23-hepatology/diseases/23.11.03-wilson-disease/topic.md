## 1. Learning Objectives
- [ ] Apply diagnostic criteria (ceruloplasmin, urinary copper, KF rings, genetics)
- [ ] Calculate Leipzig score
- [ ] Differentiate hepatic vs neurological presentations
- [ ] Initiate chelation therapy (penicillamine, trientine) and zinc
- [ ] Identify FCPS/MRCP high-yield features (Kayser-Fleischer rings, Coombs-negative haemolysis)

---

## 2. Definition & Pathogenesis

| Feature | Wilson Disease |
|---------|----------------|
| **Genetics** | **Autosomal recessive**: **ATP7B** gene (chromosome 13) |
| **Protein** | ATP7B = Copper-transporting ATPase (biliary excretion) |
| **Defect** | Impaired biliary copper excretion → hepatic copper accumulation → oxidative damage |
| **Prevalence** | 1:30,000; carrier frequency 1:90 |
| **Age of onset** | **5-35 years** (hepatic); **10-50 years** (neurological) |

---

## 3. Clinical Presentations

```mermaid
flowchart TD
    A[Wilson Disease] --> B[Hepatic Presentation]
    B --> C[Asymptomatic / Elevated LFTs]
    B --> D[Chronic Hepatitis]
    B --> E[Cirrhosis]
    B --> F[**Acute Liver Failure** (5-10% of young ALF)]
    A --> G[Neurological Presentation]
    G --> H[Tremor (wing-beating)]
    G --> I[Dystonia, rigidity, dysarthria]
    G --> J[Psychiatric: depression, psychosis, personality change]
    A --> K[Other]
    K --> L[Kayser-Fleischer Rings]
    K --> M[Renal: Fanconi syndrome, nephrolithiasis]
    K --> N[Cardiac: cardiomyopathy]
    K --> O[Bone: osteoporosis, arthritis]
    K --> P[Haematologic: Coombs-neg haemolytic anaemia]
```

---

## 4. Diagnostic Criteria (Leipzig Score)

| Feature | Score |
|---------|-------|
| **Kayser-Fleischer rings** | Present: +2; Absent: 0 |
| **Neurological symptoms** | Severe: +2; Mild: +1; None: 0 |
| **Ceruloplasmin (mg/dL)** | <10: +2; 10-20: +1; >20: 0 |
| **Coombs-negative haemolytic anaemia** | Present: +1; Absent: 0 |
| **Liver copper (μg/g dry weight)** | >250: +2; 50-250: +1; <50: -1 |
| **Urinary copper (μg/24h)** | >100: +2; 40-100: +1; <40: 0 |
| **Mutation analysis** | 2 mutations: +4; 1 mutation: +1; 0: 0 |

| Total Score | Interpretation |
|-------------|----------------|
| **≥4** | **Wilson disease confirmed** |
| **3** | Probable — needs more testing |
| **≤2** | Unlikely |

---

## 5. Key Diagnostic Tests

### 1. Ceruloplasmin
| Aspect | Detail |
|--------|--------|
| **Normal** | 20-40 mg/dL |
| **Wilson** | **Low (<20 mg/dL)** in 85-90% |
| **Pitfalls** | **Acute phase reactant** → may be NORMAL in ALF, inflammation, pregnancy, estrogen |
| **Specificity** | Not specific (low in malnutrition, nephrotic syndrome, Menkes disease) |

> **FCPS/MRCP**: **Low ceruloplasmin + clinical picture = Wilson until proven otherwise**

### 2. Urinary Copper (24-hour)
| Aspect | Detail |
|--------|--------|
| **Normal** | <40 μg/24h |
| **Wilson** | **>100 μg/24h** (often >500 in symptomatic) |
| **Post-penicillamine challenge** | Not routinely needed |

### 3. Kayser-Fleischer (KF) Rings
| Aspect | Detail |
|--------|--------|
| **Cause** | Copper deposition in Descemet's membrane |
| **Detection** | **Slit-lamp examination** (essential — not visible to naked eye usually) |
| **Sensitivity** | Neurological: **95-100%**; Hepatic: **50-60%**; ALF: often absent |
| **Specificity** | **High** (also in chronic cholestasis: PBC, PSC — but rare) |

### 4. Liver Copper (Biopsy)
| Aspect | Detail |
|--------|--------|
| **Normal** | <50 μg/g dry weight |
| **Wilson** | **>250 μg/g** (diagnostic) |
| **Caveat** | Sampling error in cirrhosis; **cholestatic diseases also high** |

### 5. Genetic Testing (ATP7B)
| Aspect | Detail |
|--------|--------|
| **Diagnostic** | **2 pathogenic mutations = definite** |
| **Carrier** | 1 mutation |
| **Limitations** | >500 mutations described; not all detected by panels |

---

## 6. Wilson Disease Presenting as ALF (High-Yield)

| Feature | Wilson ALF |
|---------|------------|
| **ALP : Bilirubin ratio** | **<2** (ALP disproportionately low) |
| **AST : ALT ratio** | **>2.2** |
| **Haemolysis** | **Coombs-negative (90%)** |
| **Ceruloplasmin** | Low (but acute phase may ↑ it) |
| **Urinary copper** | >500 μg/24h typical |
| **KF rings** | Often **ABSENT** (acute) |
| **Survival without transplant** | **<20%** |

> **Any young person <40 with ALF of unknown cause = Wilson until proven otherwise**

---

## 7. Treatment

### 1. Chelation Therapy

| Drug | Dose | Mechanism | Monitoring |
|------|------|-----------|------------|
| **Penicillamine** | 250-500 mg QID (500-1500 mg/day) | Chelates copper → urinary excretion | CBC, U&E, LFTs, urine protein q1-3mo; **pyridoxine 25mg daily** |
| **Trientine** | 500-750 mg QID (1000-2000 mg/day) | Chelates copper (less side effects) | Similar; preferred if penicillamine intolerant |
| **Tetrathiomolybdate** | Experimental | Inhibits copper absorption + chelates | Pulmonary fibrosis risk |

> **First-line**: Penicillamine OR Trientine (trientine preferred for neuro/less side effects)

### 2. Zinc Acetate (Maintenance / Initial if Mild)
| Dose | 50 mg TID (elemental zinc) |
|------|----------------------------|
| **Mechanism** | Induces intestinal metallothionein → blocks copper absorption |
| **Use** | Maintenance after decoppering; Initial for presymptomatic/mild |
| **Monitoring** | Urinary copper <100 μg/24h; Zinc levels |

### 3. Treatment Algorithm

```mermaid
flowchart TD
    A[Diagnose Wilson Disease] --> B{Presentation}
    B -->|ALF| C[URGENT: Penicillamine/Trientine + Zinc + Transplant Evaluation]
    B -->|Neurological / Hepatic (Symptomatic)| D[Penicillamine 750-1500mg/d OR Trientine 1000-2000mg/d + Zinc 50mg TID]
    B -->|Presymptomatic / Mild| E[Zinc 50mg TID alone (or + low-dose chelator)]

*...continued (truncated for renderer performance)*
---

> Auto-generated study sections for "Inherited and Metabolic Liver Disease" — Ch 23: Hepatology.

## Flashcards (23 generated)

- Q: What is the definition of Inherited and Metabolic Liver Disease?
  A: B --> F[Acute Liver Failure (5-10% of young ALF)]
- Q: What is Genetics of Inherited and Metabolic Liver Disease?
  A: Autosomal recessive: ATP7B gene (chromosome 13)
- Q: What is Protein of Inherited and Metabolic Liver Disease?
  A: ATP7B = Copper-transporting ATPase (biliary excretion)
- Q: What is Defect of Inherited and Metabolic Liver Disease?
  A: Impaired biliary copper excretion → hepatic copper accumulation → oxidative damage
- Q: What is the epidemiology of Inherited and Metabolic Liver Disease?
  A: 1:30,000; carrier frequency 1:90
- Q: What is Age of onset of Inherited and Metabolic Liver Disease?
  A: 5-35 years (hepatic); 10-50 years (neurological)
- Q: What causes Inherited and Metabolic Liver Disease?
  A: Copper deposition in Descemet's membrane
- Q: What is Detection of Inherited and Metabolic Liver Disease?
  A: Slit-lamp examination (essential — not visible to naked eye usually)
- Q: What is Sensitivity of Inherited and Metabolic Liver Disease?
  A: Neurological: 95-100%; Hepatic: 50-60%; ALF: often absent
- Q: What is Specificity of Inherited and Metabolic Liver Disease?
  A: High (also in chronic cholestasis: PBC, PSC — but rare)
- Q: What is Normal of Inherited and Metabolic Liver Disease?
  A: <50 μg/g dry weight
- Q: What is Wilson of Inherited and Metabolic Liver Disease?
  A: >250 μg/g (diagnostic)
- Q: What is Caveat of Inherited and Metabolic Liver Disease?
  A: Sampling error in cirrhosis; cholestatic diseases also high
- Q: What is the mechanism of Inherited and Metabolic Liver Disease?
  A: Induces intestinal metallothionein → blocks copper absorption
- Q: What is Use of Inherited and Metabolic Liver Disease?
  A: Maintenance after decoppering; Initial for presymptomatic/mild
- Q: How is Inherited and Metabolic Liver Disease monitored?
  A: Urinary copper <100 μg/24h; Zinc levels
- Q: What causes Inherited and Metabolic Liver Disease?
  A: Copper deposition in Descemet's membrane
- Q: What is Detection of Inherited and Metabolic Liver Disease?
  A: Slit-lamp examination (essential — not visible to naked eye usually)
- Q: What is Sensitivity of Inherited and Metabolic Liver Disease?
  A: Neurological: 95-100%; Hepatic: 50-60%; ALF: often absent
- Q: What is Normal of Inherited and Metabolic Liver Disease?
  A: <50 μg/g dry weight
- Q: What is Wilson of Inherited and Metabolic Liver Disease?
  A: >250 μg/g (diagnostic)
- Q: What is the mechanism of Inherited and Metabolic Liver Disease?
  A: Induces intestinal metallothionein → blocks copper absorption
- Q: What is Use of Inherited and Metabolic Liver Disease?
  A: Maintenance after decoppering; Initial for presymptomatic/mild

## MCQs (1 generated)

1. **Which of the following best describes Inherited and Metabolic Liver Disease?**
   A. **B --> F[Acute Liver Failure (5-10% of young ALF)]**
   B. An unrelated condition not matching the clinical picture of Inherited and Metabolic Liver Disease
   C. A complication seen late in the disease course of Inherited and Metabolic Liver Disease
   D. A condition that mimics Inherited and Metabolic Liver Disease but has a different underlying cause

## SBA Questions (1 generated)

1. A patient with suspected Inherited and Metabolic Liver Disease presents with: Feature — Wilson Disease; Genetics — Autosomal recessive: ATP7B gene (chromosome 13); Protein — ATP7B = Copper-transporting ATPase (biliary excretion). What is the most likely diagnosis?
   A. **Inherited and Metabolic Liver Disease**
   B. A condition that mimics Inherited and Metabolic Liver Disease but is not the same entity
   C. A complication of Inherited and Metabolic Liver Disease rather than the primary diagnosis
   D. An unrelated condition in the same clinical category as Inherited and Metabolic Liver Disease

## PasTest Scenario SBAs (Clinical Vignettes)

> **Auto-generated PasTest/Mediscope-style scenario SBAs** grounded in the authored source. Each scenario tests a real clinical fact (triad, specific sign, contraindication, trial, first-line Rx) extracted from the topic. *Source: Ch 23: Hepatology — Wilson Disease*

**Q1.** Which of the following features is most specific or characteristic of Wilson Disease?

  - **A.** Specificity
  - **B.** A feature common to many acute inflammatory conditions
  - **C.** A non-specific sign that does not localise the diagnosis
  - **D.** An investigation finding rather than a clinical feature

  > **Answer: A** — Specificity
  >
  > *Source:* Pitfalls** | **Acute phase reactant** → may be NORMAL in ALF, inflammation, pregnancy, estrogen |
| **Specificity** | Not specific (low in malnutrition, nephrotic syndrome, Menkes disease) |

> **FCPS

**Q2.** What is the most appropriate first-line therapy for Wilson Disease?

  - **A.** Tetrathiomolybdate
  - **B.** An advanced/surgical therapy reserved for refractory disease
  - **C.** Symptomatic treatment only, no disease-modifying therapy
  - **D.** Empiric broad-spectrum therapy without specific indication

  > **Answer: A** — Tetrathiomolybdate
  >
  > *Source:* **Tetrathiomolybdate**   Experimental   Inhibits copper absorption + chelates   Pulmonary fibrosis risk  

> **First-line**: Penicillamine OR Trientine (trientine preferred for neuro/less side effects

