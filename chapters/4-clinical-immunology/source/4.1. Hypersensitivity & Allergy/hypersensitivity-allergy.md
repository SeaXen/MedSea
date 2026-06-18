# 4.1-4.4 Hypersensitivity & Allergic Disorders

**Parent Topic:** [Clinical Immunology MOC](../Clinical%20Immunology%20MOC.md) → [Chapter 4 Hierarchy](../Davidson%20Chapter%204%20-%20Clinical%20Immunology%20Hierarchy.md)  
**Status:** `full-fcps-mrcp-note`  
**Priority:** ⭐⭐⭐ HIGHEST (FCPS/MRCP — Gell & Coombs Classification, Anaphylaxis, Asthma, Drug Allergy, Allergy Testing)  
**Source:** Davidson 24th Ed Ch 4; BSACI/WAO Guidelines; NICE/BSR; FCPS/MRCP/MRCPCH Syllabus

---

## 1. 🎯 Learning Objectives
- [ ] Apply **Gell & Coombs Classification** — Type I-IV (and V) Hypersensitivity mechanisms, Examples
- [ ] Manage **Anaphylaxis** — Algorithm (Adrenaline IM, IV Fluids, Oxygen, Adjuncts), Biphasic, Tryptase
- [ ] Diagnose & Manage **Asthma** — Phenotypes/Endotypes, Stepwise Management (BTS/SIGN), Biologics
- [ ] Manage **Allergic Rhinitis/Conjunctivitis** — ARIA Guidelines, Immunotherapy (SCIT/SLIT)
- [ ] Diagnose **Food Allergy** — IgE vs Non-IgE, Component-Resolved Diagnostics, Oral Food Challenge
- [ ] Manage **Drug Hypersensitivity** — SJS/TEN/DRESS/AGEP, HLA Associations, Cross-Reactivity, Desensitisation
- [ ] Apply **Allergy Diagnostics** — SPT, sIgE, Component-Resolved Diagnostics, BAT, Patch Testing, Oral Food Challenge
- [ ] Answer viva: "Anaphylaxis Algorithm" and "SJS vs TEN vs DRESS" and "Component-Resolved Diagnostics"

---

## 2. 🧠 Core Concept: Gell & Coombs Classification

```mermaid
flowchart TD
    A[Hypersensitivity Reactions] --> B[Type I: IgE-Mediated (Immediate)]
    A --> C[Type II: Antibody-Mediated (Cytotoxic)]
    A --> D[Type III: Immune Complex-Mediated]
    A --> E[Type IV: T-Cell Mediated (Delayed)]
    A --> F[Type V: Stimulatory (Autoantibody)]
    
    B --> B1[Anaphylaxis, Asthma, Allergic Rhinitis, Food Allergy, Atopic Dermatitis]
    C --> C1[AIHA, ITP, Goodpasture, Graves, Myasthenia Gravis, Drug-Induced]
    D --> D1[SLE, Serum Sickness, Vasculitis, Arthus, Farmer's Lung]
    E --> E1[Contact Dermatitis, TB Test, Drug Hypersensitivity (SJS/TEN/DRESS), TB, Granulomas]
    F --> F1[Graves (TSHR Stimulating), MG (AChR Block), Pemphigus (AChR Modulating)]
```

---

## 3. ️⃣ Type I Hypersensitivity (IgE-Mediated / Immediate)

### Pathophysiology
| Phase | Mechanism |
|-------|-----------|
| **Sensitisation** | Allergen → DC → Th2 → IL-4/IL-13 → B cell class switch → **IgE** → Binds **FcεRI** on Mast cells/Basophils |
| **Effector** | Re-exposure → Allergen cross-links **IgE-FcεRI** → **Degranulation** (Histamine, Tryptase, PGD2, LTC4, PAF) + **Cytokines** (IL-4, IL-5, IL-13) |
| **Late Phase** (4-12h) | **Eosinophils, Th2 cells, Basophils** → Tissue damage, Remodelling |

### Key Mediators
| Mediator | Source | Effects |
|----------|--------|---------|
| **Histamine** | Mast cells, Basophils | Vasodilation, ↑ Vascular permeability, Bronchoconstriction, Pruritus |
| **Tryptase** | Mast cells | **Biomarker** (Peak 1-2h, Half-life 2h), Fibrosis, Airway remodelling |
| **PGD2** | Mast cells | Bronchoconstriction, Vasodilation, Flushing |
| **LTC4, LTD4, LTE4** (CysLTs) | Mast cells, Eosinophils | **Potent bronchoconstriction**, Mucus, Vascular permeability |
| **PAF** | Mast cells, Basophils, Platelets | Platelet activation, Vascular permeability, Bronchoconstriction |
| **IL-4, IL-5, IL-13** | Th2, ILC2, Mast cells | **IL-5 → Eosinophilia**, **IL-13 → IgE, Airway remodelling**, **IL-4 → IgE switching** |

---

## 4. ️⃣ Anaphylaxis

### Diagnostic Criteria (WAO/RS)
**Anaphylaxis HIGHLY LIKELY if ANY 1 of 3:**
1. **Acute onset** (mins-hours) **+ Skin/Mucosal** (Urticaria, Angioedema, Flushing) **+ Respiratory** (Wheeze, Stridor, Dyspnoea) **OR** **Cardiovascular** (Hypotension, Syncope, Tachycardia)
2. **Acute onset** **+ 2+ Systems**: Skin + Respiratory + Cardiovascular + GI
3. **Acute hypotension** after known allergen exposure

### Emergency Algorithm (RCUK/WAO/RCUK 2021)
```mermaid
flowchart TD
    A[Recognise Anaphylaxis] --> B[Call for Help / Code Blue]
    B --> C[**ADRENALINE IM 0.5mg (1:1000) Anterolateral Thigh**]
    C --> D{Response?}
    D -->|No improvement in 5 min| E[**Repeat Adrenaline IM q5min**<br/>Max 3 doses]
    D -->|Improving| F[Position: Supine + Legs Raised<br/>(If Breathless: Semi-recumbent)]
    F --> G[**O2 High Flow** (15L/min)]
    F --> H[**IV Fluid Challenge**<br/>500-1000ml Crystalloid Bolus]
    F --> I[**Chlorphenamine 10mg IV** (Adjunct)]
    F --> J[**Hydrocortisone 200mg IV** (Adjunct — Late effect)]
    F --> K[**Salbutamol Neb** (If Bronchospasm)]
    K --> L[Continuous Monitoring<br/>ECG, SpO2, BP, RR, Peak Flow]
    L --> M[Observe 6-12h<br/>(Biphasic Reaction Risk 20%)]
```

### Adrenaline Dosing
| Age/Weight | IM Dose (1:1000) |
|------------|------------------|
| **Adult** | **0.5 mg (0.5 mL)** |
| **Child >12y / >50kg** | 0.5 mg (0.5 mL) |
| **Child 6-12y / 25-50kg** | 0.3 mg (0.3 mL) |
| **Child 6m-6y / 7.5-25kg** | 0.15 mg (0.15 mL) |
| **Infant <6m / <7.5kg** | 0.1 mg (0.1 mL) |

> **Key**: **Adrenaline IM is FIRST-LINE and LIFE-SAVING** — No contraindication in anaphylaxis. Repeat q5min if no improvement.

### Biphasic Reaction
| Feature | Detail |
|---------|--------|
| **Incidence** | 1-20% (Higher if delayed adrenaline) |
| **Timing** | 1-72h after initial resolution (Peak 3-10h) |
| **Risk Factors** | Delayed adrenaline, Severe initial reaction, Inadequate initial dose, No observation |
| **Management** | **Observe 6-12h** post-resolution; **Adrenaline available** |

### Serum Tryptase
| Timing | Interpretation |
|--------|----------------|
| **Baseline** | Pre-reaction (if known) |
| **Peak (1-2h post-onset)** | **>11.4 ng/mL OR >2x Baseline + 1.2x** = Supports anaphylaxis |
| **24h** | Returns to baseline (Half-life ~2h) |
| **Elevated Baseline** | **Mastocytosis**, **Clonal mast cell disease** |

---

## 5. ️⃣ Bronchial Asthma

### Phenotypes & Endotypes
| Phenotype | Key Features | Endotype | Key Biomarkers |
|-----------|--------------|----------|----------------|
| **Allergic (Early-onset)** | Atopy, Childhood onset, RH | **Type 2 High** | **FeNO >25 ppb**, Eos >150/μL, IgE↑, Periostin |
| **Non-Allergic (Late-onset)** | Non-atopic, Adult onset, Obesity | **Type 2 Low / Non-Type 2** | Neutrophilia, Low FeNO, Obesity |
| **Eosinophilic** | Sputum Eos >3% | **Type 2 High** | Blood Eos >300/μL, FeNO >50 ppb |
| **Neutrophilic** | Sputum Neut >60% | **Non-Type 2 / Th17** | Neutrophilia, IL-17, IL-8 |
| **Aspirin-Exacerbated Respiratory Disease (AERD)** | Asthma + Nasal Polyps + NSAID Sensitivity | **CysLT Overproduction** | High CysLTs, Eosinophilia |
| **Obese Asthma** | BMI >30, Late-onset, Poor control | **Mixed / Non-Type 2** | Low FeNO, Low Eos, Metabolic syndrome |

### BTS/SIGN 2024 Stepwise Management (Adults)
| Step | Treatment | Dose/Details |
|------|-----------|--------------|
| **Step 1** | **SABA PRN** (Salbutamol 100-200mcg) | As needed |
| **Step 2** | **Low-dose ICS** (Beclomethasone 200-400mcg/d) + SABA PRN | **Regular ICS** — Start if symptoms >2/wk or night waking |
| **Step 3** | **Low-dose ICS + LABA** (Fixed combination) | Add LABA if not controlled on ICS alone |
| **Step 4** | **Medium-dose ICS + LABA** | Increase ICS to medium dose (Beclo 800mcg/d) |
| **Step 5** | **High-dose ICS + LABA** + **Add-on** | **LAMA (Tiotropium)**, **LTRA (Montelukast)**, **Theophylline** |
| **Step 6** | **High-dose ICS + LABA + Biologic** | **Anti-IL5 (Mepolizumab/Reslizumab/Benralizumab)**, **Anti-IL4Rα (Dupilumab)**, **Anti-TSLP (Tezepelumab)**, **Anti-IgE (Omalizumab)** |

> **Step Down**: Review q3m, Step down if controlled 3m
> **SMART/MART**: **Single Maintenance and Reliever Therapy** (Budesonide/Formoterol, Beclo/Formoterol) — Preferred for Steps 3-5

### Severe Asthma Biologics (GINA 2024 / NICE)
| Biologic | Target | Indication | Dose |
|----------|--------|------------|------|
| **Omalizumab** | Anti-IgE | **Severe Allergic Asthma** (IgE 30-1500 IU/mL, Sensitisation) | 75-600mg SC q2-4w |
| **Mepolizumab / Reslizumab** | Anti-IL-5 | **Severe Eosinophilic Asthma** (Blood Eos ≥150-300/μL) | 100mg SC q4w / 3mg/kg IV q4w |
| **Benralizumab** | Anti-IL-5Rα | **Severe Eosinophilic Asthma** (Eos ≥300/μL) | 30mg SC q4w ×3, then q8w |
| **Dupilumab** | Anti-IL-4Rα | **Severe Type 2 High** (Eos ≥150; FeNO ≥25) | 600mg SC loading → 300mg q2w |
| **Tezepelumab** | Anti-TSLP | **Severe Asthma** (Broad Type 2) | 210mg SC q4w |

### Acute Severe Asthma (Life-Threatening)
| Feature | Threshold |
|---------|-----------|
| **PEF** | <33% Best/Predicted |
| **SpO₂** | <92% on Air |
| **PaCO₂** | Normal/Raised (Normal = Impending Respiratory Failure) |
| **Silent Chest** | — |
| **Cyanosis / Exhaustion / Confusion** | — |

| Treatment | Dose |
|-----------|------|
| **O₂** (Target SpO₂ 94-98%) | High Flow (15L) |
| **Salbutamol Neb** | 5mg q15-30min (Continuous if severe) |
| **Ipratropium Neb** | 500mcg q20-30min (Add to Salbutamol) |
| **IV Magnesium Sulphate** | **2g IV over 20min** (Single dose) |
| **IV Hydrocortisone** | 100mg (or Pred 40-50mg PO) |
| **IV Aminophylline** | **Only if Life-Threatening** (5mg/kg loading, 0.5-0.7mg/kg/h) |
| **Escalation** | **ICU, IV Salbutamol Infusion, NIV/Intubation, ECMO** |

---

## 6. ️⃣ Allergic Rhinitis & Conjunctivitis (ARIA Guidelines)

### Classification
| Duration | Intermittent | Persistent |
|----------|--------------|------------|
| **Severity** | **Mild** (Normal sleep, No impairment) | **Mild** |
| | **Moderate-Severe** (≥1: Sleep disturbance, Impairment, Troublesome) | **Moderate-Severe** |

### Management (ARIA 2020)
| Step | Intermittent | Persistent |
|------|--------------|------------|
| **Mild** | **Oral/Intranasal H1-Antihistamine** PRN | **Intranasal Corticosteroid (INCS)** + H1-Antihistamine PRN |
| **Moderate-Severe** | **INCS + H1-Antihistamine** (Regular) | **INCS + H1-Antihistamine** (Regular) + **LTRA (Montelukast)** if ASTHMA |
| **Refractory** | **INCS + H1 + LTRA** OR **Short Oral Steroid** | **INCS + H1 + LTRA** OR **Immunotherapy** |

### Allergen Immunotherapy (AIT)
| Type | Indication | Protocol |
|------|------------|----------|
| **SCIT** (Subcutaneous) | **Perennial/Seasonal IgE-mediated** | Build-up (Weekly × 3-6m) → Maintenance (Monthly × 3-5y) |
| **SLIT** (Sublingual) | **Perennial/Seasonal** | Daily drops/tablet (3-5y) |
| **Indications** | **IgE-mediated**, Mod-Severe, Pharmacotherapy failure, Allergen avoidance impossible | |
| **Contraindications** | **Uncontrolled Asthma**, Severe CVD, Immunodeficiency, β-blockers, Pregnancy (Initiation) | |

---

## 7. ️⃣ Food Allergy

### Classification
| Type | Mechanism | Onset | Examples |
|------|-----------|--------|----------|
| **IgE-Mediated** | **Type I** | Minutes-2h | Peanut, Egg, Milk, Fish, Shellfish, Tree nuts, Soy, Wheat |
| **Non-IgE Mediated** | **Type IV (T-cell)** | Hours-Days | **FPIES** (Food Protein-Induced Enterocolitis), **FPIAP** (Proctocolitis), **EoE** (Eosinophilic Oesophagitis) |
| **Mixed** | IgE + Non-IgE | Variable | EoE, Some Atopic Dermatitis |

### Diagnosis
| Test | Utility |
|------|---------|
| **History** | **Cornerstone** — Timing, Reproducibility, Co-factors (Exercise, Alcohol, NSAIDs) |
| **SPT** | **Sensitivity 90%**, PPV ~50% (Wheal ≥3mm) |
| **sIgE** | **Sensitivity 90%**, Component-resolved useful |
| **Component-Resolved Diagnostics (CRD)** | **Identifies specific proteins** (Ara h 2 for Peanut, Ara h 8 for Cross-reactivity) |
| **Basophil Activation Test (BAT)** | **Functional**, High specificity, Research/Refractory |
| **Oral Food Challenge (OFC)** | **Gold Standard** — Double-blind, Placebo-controlled (DBPCFC) |

### Component-Resolved Diagnostics (CRD) — Peanut Example
| Component | Clinical Significance |
|-----------|----------------------|
| **Ara h 1, 2, 3** | **Primary Sensitisers** — High risk systemic reaction |
| **Ara h 8** | **PR-10 (Bet v 1 Homolog)** — **Cross-reactivity** (Birch pollen), Usually mild |
| **Ara h 9** | **LTP** — **Severe reactions**, Heat stable, Mediterranean |

### Management
| Step | Action |
|------|--------|
| **Avoidance** | Strict allergen avoidance, Label reading, **Adrenaline Auto-Injector (AAI)** — **2 devices at all times** |
| **Acute Reaction** | **Adrenaline IM** (Anaphylaxis) → **Antihistamine** (If mild) |
| **Immunotherapy** | **OIT (Oral Immunotherapy)** — Palforzia (Peanut), **EPIT** (Epicutaneous — Viaskin) |
| **Prevention** | **Early Introduction** (LEAP Study: Peanut 4-11m → ↓ Allergy 80%) |

---

## 8. ️⃣ Drug Hypersensitivity

### Classification (Pichler)
| Type | Mechanism | Timing | Examples |
|------|-----------|--------|----------|
| **Type I (IgE)** | Immediate | <1h | Penicillins, NMBA, Latex |
| **Type II (Cytotoxic)** | Antibody-dependent | 5-10d | Penicillin-induced AIHA, Heparin-Induced Thrombocytopenia (HIT) |
| **Type III** | Immune Complex | 1-3w | Serum Sickness, Serum Sickness-Like Reaction (SSR) |
| **Type IVa (Th1)** | Macrophage activation | 2-6w | **DRESS, AGEP, TB Test** |
| **Type IVb (Th2)** | Eosinophil recruitment | 2-6w | **DRESS, SJS/TEN, AGEP, Maculopapular Exanthema (MPE)** |
| **Type IVc (CTL)** | Cytotoxic T cells | 2-6w | **SJS/TEN**, **DRESS**, Fixed Drug Eruption |
| **Type IVd (Th17)** | Neutrophil recruitment | 2-6w | **AGEP**, Pustular Psoriasis |

### Severe Cutaneous Adverse Reactions (SCARs)

| Syndrome | Time to Onset | Key Features | Mortality | Management |
|----------|---------------|--------------|-----------|------------|
| **SJS** (Stevens-Johnson Syndrome) | 7-21d | **<10% BSA Detachment**, **Mucosal ≥2 sites**, Target lesions, Fever | ~5% | **Stop Drug**, **IVIG 2-3g/kg** or **Plasma Exchange**, Supportive |
| **TEN** (Toxic Epidermal Necrolysis) | 7-21d | **>30% BSA Detachment**, **Mucosal ≥2 sites**, Nikolsky+, Sepsis Risk | 25-30% | **Immediate ICU**, **Supportive**, **IVIG 2-3g/kg** / **PLEX**, Ciclosporin, Etanercept |
| **SJS/TEN Overlap** | 7-21d | **10-30% BSA Detachment** | 10-15% | Same as TEN |
| **DRESS** | 2-8w | **Fever, Rash, Eosinophilia, Lymphadenopathy, Visceral (Liver > Kidney), HHV-6 Reactivation** | 10% | **Stop Drug**, **Steroid (Pred 1mg/kg)**, **IVIG** if severe |
| **AGEP** | 1-5d | **Acute Febrile Neutrophilic Pustulosis**, Neutrophilia, Fever, **No Mucosal** | <5% | **Stop Drug**, **Topical Steroids**, Self-limiting |

### SCORTEN (TEN Severity Score)
| Parameter | Score 1 Point |
|-----------|---------------|
| Age >40y | |
| Malignancy | |
| Heart Rate >120 | |
| BSA Detached >10% | |
| Serum Urea >10mmol/L | |
| Serum Bicarbonate <20mmol/L | |
| Glucose >14mmol/L | |

| Score | Mortality |
|-------|-----------|
| 0-1 | 3.2% |
| 2 | 12.1% |
| 3 | 35.3% |
| 4 | 58.3% |
| ≥5 | 90% |

### Drug Cross-Reactivity (Key)
| Drug Class | Cross-Reactivity |
|------------|------------------|
| **Penicillins** | **Carbapenems (1%)**, Cephalosporins (1-2% 1st/2nd gen, <1% 3rd/4th gen) |
| **Sulfonamides** | **Sulfonamide cross-reactivity** (Sulfamethoxazole, Sulfasalazine, Dapsone) |
| **NSAIDs** | **Cross-reactivity within class** (Aspirin → Ibuprofen/Naproxen) |
| **ARBs/ACEi** | Low cross-reactivity |
| **Statins** | Low cross-reactivity |

### Desensitisation
| Scenario | Protocol |
|----------|----------|
| **Penicillin (IgE)** | **Rapid (4-6h)** or **Slow (Days)** — Incremental doses under monitoring |
| **Aspirin (AERD)** | **Incremental Oral Aspirin** (Start 20mg, Double q1-2h → 650mg) |
| **Carboplatin/Oxaliplatin** | **12-step Protocol** (Pre-med: Dexamethasone, Antihistamine, H2-blocker) |
| **Allopurinol** | **Not Recommended** (High failure) — Avoid, Switch to Febuxostat |

### HLA-Drug Hypersensitivity Associations (High-Yield)
| HLA Allele | Drug | Reaction | Population | Screening |
|------------|------|----------|------------|-----------|
| **HLA-B*57:01** | **Abacavir** | Hypersensitivity (fever, rash, GI, respiratory) | All (NPV >98%) | **Mandatory pre-prescription** |
| **HLA-B*15:02** | **Carbamazepine** | SJS/TEN | Han Chinese, Thai, Malaysian, Indian | **Mandatory pre-prescription** (Asian ancestry) |
| **HLA-B*58:01** | **Allopurinol** | SJS/TEN/DRESS | Han Chinese, Korean, Thai, European | **Strongly recommended** (all ancestries) |
| **HLA-A*31:01** | **Carbamazepine** | SJS/TEN/DRESS/Maculopapular | European, Japanese | Recommended |
| **HLA-DRB1*07:01** | **Flucloxacillin** | DILI (Drug-induced liver injury) | European | Consider |
| **HLA-B*57:01** | **Flucloxacillin** | DILI | European | Consider |

---

## 9. ️⃣ Allergy Testing

### Skin Prick Testing (SPT)
| Feature | Detail |
|---------|--------|
| **Principle** | Allergen → Mast cell degranulation → Wheal/Flare |
| **Positive** | **Wheal ≥3mm** (vs Negative Control) |
| **Controls** | **Positive**: Histamine 10mg/mL; **Negative**: Saline/Glycerol |
| **Contraindications** | Severe anaphylaxis risk, Severe uncontrolled asthma, **Antihistamines (Stop 48-72h)**, Tricyclics, **Severe Dermographism** |
| **Sensitivity/Specificity** | **90%/90%** (Aeroallergens), **Food: Sens 90%, PPV 50%** |

### Intradermal Testing (IDT)
| Feature | Detail |
|---------|--------|
| **Principle** | Allergen injected **intradermally** (0.02-0.05 mL) → Wheal/Flare |
| **Indications** | **Drug allergy** (Penicillin, Venom), **Aeroallergens** when SPT negative but high suspicion |
| **Positive** | **Wheal ≥5mm** (erythema) at 15-20 min |
| **Sensitivity** | **Higher than SPT** (esp. drug/venom), but ↓ specificity |
| **Risk** | **Higher anaphylaxis risk** than SPT — Resuscitation equipment required |
| **Concentrations** | 1:100 to 1:1000 of SPT concentration |

### Patch Testing (Type IV)
| Feature | Detail |
|---------|--------|
| **Sensitivity** | 90% (Aeroallergens) |
| **Specificity** | 90% (Depends on allergen) |
| **ISAC (ImmunoCAP ISAC)** | **112 Components** on microarray — Component-resolved |
| **Advantages** | No antihistamine stop, Quantitative, Component-resolved |

### Component-Resolved Diagnostics (CRD)
| Application | Benefit |
|-------------|---------|
| **Peanut (Ara h 1/2/3 vs Ara h 8/9)** | **Ara h 1/2/3 = Primary = High Risk**; **Ara h 8/9 = Cross-reactivity (Bet v 1, LTP) = Lower Risk** |
| **Hazelnut (Cor a 1 vs 9/14)** | **Cor a 1 = PR-10 (Birch)**, **Cor a 9/14 = Storage (High Risk)** |
| **Apple (Mal d 1 vs 3)** | **Mal d 1 = PR-10 (Birch) = Mild**; **Mal d 3 = LTP = Severe** |
| **Wheat (Tri a 19/ω-5 Gliadin)** | **ω-5 Gliadin = Severe (WDEIA)** |

### Basophil Activation Test (BAT)
| Feature | Detail |
|---------|--------|
| **Principle** | Allergen → Basophil CD63/CD203c upregulation (Flow Cytometry) |
| **Sensitivity/Specificity** | **90-95% / 90-95%** (Superior to sIgE for some foods/drugs) |
| **Indications** | **Food/Drug Allergy** (sIgE/SPT discordant), **Venom**, **CRD Equivocal** |

### Patch Testing (Type IV)
| Feature | Detail |
|---------|--------|
| **Allergens** | **Baseline Series** (Fragrance, Nickel, Cobalt, Potassium Dichromate, Balsam of Peru, Parabens, Formaldehyde, etc.) |
| **Reading** | **Day 2 (48h) + Day 3-4 (72-96h)** |
| **Grading (ICDRG)** | **+** (Erythema), **++** (Papules/Infiltration), **+++** (Vesicles) |
| **Irritant vs Allergic** | Irritant: Fades by Day 3; Allergic: Persists/Increases |

### Oral Food Challenge (OFC)
| Type | Protocol |
|------|----------|
| **Open** | Knows allergen — Clinical practice |
| **Single-Blind** | Patient blinded | 
| **Double-Blind, Placebo-Controlled (DBPCFC)** | **Gold Standard** — Research, Diagnostic uncertainty |

---

## 10. ⚡ FCPS/MRCP High-Yield Summary

| Topic | Key Points |
|-------|------------|
| **Hypersensitivity Types** | **Type I**: IgE, Mast cells, Anaphylaxis/Asthma; **Type II**: Antibody-mediated (AIHA, ITP); **Type III**: Immune complexes (SLE, Serum Sickness); **Type IV**: T-cell (Contact, TB, Drug); **Type V**: Stimulatory (Graves) |
| **Anaphylaxis** | **Adrenaline IM 0.5mg (1:1000) Anterolateral Thigh** — Repeat q5min; **Obs 6-12h** (Biphasic); **Tryptase** 1-2h peak |
| **Asthma** | **BTS/SIGN Steps 1-6**; **SMART/MART** (Buda/Form, Beclo/Form); **Biologics**: Anti-IgE, Anti-IL5/5R, Anti-IL4Rα, Anti-TSLP |
| **Allergic Rhinitis** | ARIA: Intermittent/Persistent × Mild/Mod-Severe → **INCS ± H1 ± LTRA**; **AIT (SCIT/SLIT)** 3-5y |
| **Food Allergy** | IgE (Minutes-2h) vs Non-IgE (Hours-Days); **CRD** (Ara h 1/2/3 = Risk, Ara h 8/9 = Cross-reactivity); **OFC = Gold Standard** |
| **Drug Hypersensitivity** | **SJS/TEN/DRESS/AGEP** — **SCORTEN** (TEN); **Stop Drug → ICU/Supportive/IVIG/PLEX**; **Desensitisation** (Penicillin, Aspirin, Carboplatin) |
| **Allergy Testing** | **SPT** (Wheal ≥3mm); **sIgE** (ImmunoCAP); **CRD** (Ara h 1/2/3 = Risk, 8/9 = Cross-reactivity); **BAT** (CD63/CD203c); **Patch** (Type IV); **OFC = Gold Standard** |
| **Anaphylaxis** | **Adrenaline IM 0.5mg (1:1000) Anterolateral Thigh** — q5min; **Observation 6-12h**; **Tryptase 1-2h peak** |

---

## 11. 🎤 Viva Questions (Expected Answers)

| # | Question | Expected Answer |
|---|----------|-----------------|
| 1 | Anaphylaxis — first-line treatment? | **Adrenaline IM 0.5mg (1:1000) Anterolateral Thigh** — Repeat q5min if no improvement; **No contraindication** |
| 2 | Anaphylaxis — biphasic reaction risk factors? | Delayed adrenaline, Severe initial reaction, Inadequate initial dose, No observation period |
| 3. | Asthma — stepwise management? | BTS/SIGN 1-6: SABA → Low ICS → Low ICS+LABA → Med ICS+LABA → High ICS+LABA+Add-on → Biologics (Anti-IgE, IL-5, IL-4R, TSLP) |
| 4. | SJS vs TEN — difference? | **SJS: <10% BSA detachment**; **TEN: >30% BSA detachment**; **Overlap 10-30%**; **SCORTEN** for prognosis |
| 5. | DRESS vs SJS/TEN — key differences? | **DRESS: 2-8w onset, Fever, Rash, Eosinophilia, Lymphadenopathy, Visceral (Liver), HHV-6**; **SJS/TEN: 7-21d, Mucosal ≥2 sites, BSA Detachment, Nikolsky+** |
| 5. | Anaphylaxis — adrenaline dose? | **0.5mg IM (1:1000) anterolateral thigh**; Repeat q5min |
| 6. | Biphasic anaphylaxis — observation period? | **6-12 hours** post-resolution |
| 6. | Serum tryptase — timing? | **Peak 1-2h post-onset**; >11.4 ng/mL or >2x baseline + 1.2x supports anaphylaxis |
| 7. | Asthma biologics — anti-IL5 indication? | **Severe Eosinophilic Asthma** (Blood Eos ≥150-300/μL) |
| 8. | Food allergy — component-resolved diagnostics? | **Ara h 1/2/3 = Primary sensitisation (High risk)**; **Ara h 8/9 = Cross-reactivity (Bet v 1/LTP)** |
| 8. | SJS vs TEN — BSA detachment? | **SJS <10%**, **SJS/TEN 10-30%**, **TEN >30%** |
| 9. | SJS vs DRESS — key difference? | **DRESS: 2-8w onset, Fever, Eosinophilia, Visceral (Liver), HHV-6**; **SJS/TEN: 7-21d, Mucosal ≥2, Nikolsky+** |
| 10. | Penicillin allergy — desensitisation protocol? | **Rapid (4-6h) or Slow (Days)** — Incremental doses under monitoring; Not for SJS/TEN history |

---

## 12. 🧩 Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **"Anaphylaxis = Only with hives"** | **NO.** Can present **WITHOUT Skin** (Cardiovascular/Respiratory only) — Still anaphylaxis! |
| **"Adrenaline = Contraindicated in Heart Disease"** | **NO.** **NO Absolute Contraindication** in Anaphylaxis — Life-saving! |
| **"SPT = Diagnostic for Food Allergy"** | **NO.** **SPT/sIgE = Sensitisation**, Not Allergy; **OFC = Gold Standard** for diagnosis |
| **"SJS = Mild, TEN = Severe"** | **NO.** **Spectrum**: SJS (<10% BSA), SJS/TEN Overlap (10-30%), TEN (>30%); **Mortality**: SJS 5%, SJS/TEN 10%, TEN 25-30% |
| **"DRESS = Just Rash"** | **NO.** **Multisystem**: Fever, Rash, Eosinophilia, Lymphadenopathy, **Hepatitis (ALT↑), Nephritis, HHV-6 Reactivation** |
| **"All Drug Rashes = Allergy"** | **NO.** **Morbilliform (MPE)** = Most common, Benign; **SCARs (SJS/TEN/DRESS/AGEP)** = Severe |
| **"AGEP = Pustular Psoriasis"** | **NO.** **AGEP**: Acute Febrile Neutrophilic Pustulosis, Drug-induced, **Neutrophilia**, Self-limiting |
| **"SPT Positive = Allergy"** | **NO.** **Sensitisation ≠ Clinical Allergy**; Need History + **OFC (Gold Standard)** |
| **"All Penicillin Allergic = Avoid All β-lactams"** | **NO.** **Cross-reactivity Low** (Carbapenems 1%, 3rd/4th Gen Cephalosporins <1%); Assess individually |
| **"Adrenaline IV = Better than IM"** | **NO.** **IM Preferred** (Rapid absorption, Safer); IV only in **Cardiac Arrest** or **Refractory Shock** with monitoring |

> **Mnemonic: HYPERSENSITIVITY ALLERGY ESSENTIALS**  
> **H**ypersensitivity Types: **I (IgE/Immediate), II (Ab-Mediated), III (IC-Mediated), IV (T-Cell), V (Stimulatory)**  
> **Y** (Anaphylaxis): **Adrenaline IM 0.5mg 1:1000 → q5min; O2, IV Fluids, Chlorphenamine, Hydrocortisone, Salbutamol; Observe 6-12h (Biphasic)**  
> **P** (Types): **I (IgE/Anaphylaxis/Asthma), II (Ab-Med/AIHA/ITP), III (IC/SLE/Serum Sickness), IV (T-Cell/Contact/TB/Drug), V (Stimulatory/Graves)**  
> **E**ndotypes Asthma: **T2-High (Eos, FeNO, IgE)** vs **T2-Low (Neutrophilic, Obese)** — **Biologics Target T2**  
> **R** (Rhinitis): **ARIA: Intermittent/Persistent × Mild/Mod-Sev → INCS ± H1 ± LTRA → AIT (SCIT/SLIT 3-5y)**  
> **S** (Skin Tests): **SPT (Wheal ≥3mm, Stop Antihist 48-72h), sIgE (ImmunoCAP), CRD (Ara h 1/2/3=Risk, 8/9=Cross), BAT (CD63/CD203c), Patch (Type IV, Day 48/72h), OFC=Gold Standard**  
> **H**ypersensitivity Types: **I (IgE), II (Ab-Med Cytotoxic), III (IC-Med), IV (T-Cell), V (Stimulatory)**  
> **S**CARs: **SJS (<10% BSA), SJS/TEN (10-30%), TEN (>30%)**; **SCORTEN (Age>40, Malig, HR>120, BSA>10%, Urea>10, Bicarb<20, Gluc>14)**  
> **E** DRESS: **2-8w, Fever, Rash, Eos, Lymphadeno, Viscera (Liver), HHV-6**  
> **N** AGEP: **1-5d, Neutrophilic Pustules, Neutrophilia, Self-Limiting**  
> **S**tudies: **OFC=Gold Standard**, **SPT (Wheal≥3mm, Stop AntiH 48-72h), sIgE (ImmunoCAP), CRD (Ara h 1/2/3=Risk, 8/9=Cross), BAT (CD63/CD203c), Patch (Day 48/72h)**  
> **I**mmune: **Type I (IgE), II (Ab), III (IC), IV (T-Cell)**  
> **T**reatment: **Anaphylaxis = Adrenaline IM 0.5mg 1:1000**, Asthma (BTS/SIGN Steps), Rhinitis (ARIA), Drug Desens (Penicillin, Aspirin)  
> **I**gE: **High Affinity FcεRI on Mast/Baso**, Degranulation (Histamine, Tryptase, PGD2, CysLTs)  
> **V** (Viva): **Anaphylaxis=Adrenaline; Asthma=BTS Steps; SJS/TEN=BSA%; DRESS=Liver/HHV-6; CRD=Ara h 2/3 Risk**  
> **V** (Viva): **SJS<10%, SJS/TEN 10-30%, TEN>30%; SCORTEN; DRESS=Liver/HHV-6; CRD=Ara h 1/2/3=Risk**  
> **E**xam: **Anaphylaxis=Adrenaline IM; Asthma=BTS Steps; SJS/TEN=BSA%; DRESS=Liver; CRD=Ara h 1/2/3**  

---

## 13. 🗺️ Mind Map

```mermaid
mindmap
  root((Hypersensitivity & Allergy))
    Gell & Coombs
      Type I: IgE, Mast Cell, Anaphylaxis, Asthma, Rhinitis, Food
      Type II: Antibody, AIHA, ITP, Goodpasture, Graves, MG, Drug
      Type III: IC, SLE, Serum Sickness, Arthus, Vasculitis
      Type IV: T-Cell, Contact, TB, Drug (SJS/TEN/DRESS), TB Test
      Type V: Stimulatory, Graves, MG
    Anaphylaxis
      Adrenaline IM 0.5mg 1:1000
      O2, IV Fluids, Chlorphenamine, Hydrocortisone
      Biphasic: Observe 6-12h
      Tryptase Peak 1-2h
    Asthma
      BTS/SIGN Steps 1-6
      SMART/MART (Buda/Form, Beclo/Form)
      Biologics: Omalizumab, Mepolizumab, Benralizumab, Dupilumab, Tezepelumab
      Acute Severe: MgSO4, IV Hydrocortisone, Aminophylline
    Rhinitis
      ARIA: Intermittent/Persistent × Mild/Mod-Sev
      INCS ± H1 ± LTRA
      AIT: SCIT/SLIT (3-5y)
    Food Allergy
      IgE (Min-2h) vs Non-IgE (Hrs-Days)
      CRD: Ara h 1/2/3=Risk, 8/9=Cross
      OFC = Gold Standard
    Drug Hypersensitivity
      SJS/TEN/DRESS/AGEP
      SCORTEN (TEN), RegiSCAR
      Desensitisation: Penicillin, Aspirin, Carboplatin
    Allergy Testing
      SPT (Wheal≥3mm, Stop AntiH 48-72h)
      sIgE (ImmunoCAP), CRD (Ara h 1/2/3=Risk, 8/9=Cross)
      BAT (CD63/CD203c), Patch (Day 48/72h), OFC=Gold Standard
    Drug Hypersensitivity
      SJS/TEN/DRESS/AGEP
      SCORTEN, RegiSCAR
      Desensitisation (Penicillin, Aspirin, Carboplatin)
      Cross-Reactivity (Penicillins, Sulfonamides, NSAIDs)
```

---

## 14. 📅 Spaced Repetition Tracker

| Review | Date | Score (0–5) | Notes |
|--------|------|-------------|-------|
| Day 1 | | | |
| Day 3 | | | |
| Day 7 | | | |
| Day 14 | | | |
| Day 30 | | | |
| Day 90 | | | |

---

## 15. 📝 Self-Test Scorecard

| Section | Max | Score | % |
|---------|-----|-------|---|
| Gell & Coombs Classification | 2 | | |
| Anaphylaxis Algorithm | 3 | | |
| Asthma Management | 3 | | |
| Allergic Rhinitis/Conjunctivitis | 2 | | |
| Food Allergy & CRD | 3 | | |
| Drug Hypersensitivity (SCARs) | 3 | | |
| Allergy Testing Methods | 2 | | |
| Anaphylaxis Management | 2 | | |
| **Total** | **20** | | |

---

## 16. 💬 Exam Answer Modes

| Format | Prompt | Key Points |
|--------|--------|------------|
| **Long Essay** | "Describe the classification, clinical features, and management of anaphylaxis." | Gell & Coombs Type I, WAO Criteria, Adrenaline IM Algorithm, Biphasic, Tryptase, Adjuncts, Observation |
| **Short Note** | "SJS vs TEN vs DRESS — differentiation." | BSA Detachment thresholds, Onset timing, Mucosal involvement, Systemic features, SCORTEN, Management |
| **Viva** | "Patient on allopurinol develops fever, rash, eosinophilia, hepatitis. Diagnosis and management?" | **DRESS** (Drug Reaction with Eosinophilia and Systemic Symptoms) — Stop drug, Steroids, IVIG if severe, HHV-6 reactivation, RegiSCAR |
| **Ward Round** | "Patient with peanut allergy given peanut butter. Develops wheeze, lip swelling, hypotension. Immediate management?" | **Anaphylaxis** — **Adrenaline IM 0.5mg (1:1000) Anterolateral Thigh**, Oxygen, IV Fluids, Chlorphenamine, Hydrocortisone, Observe 6-12h |
| **Last-Night** | "Types: I(IgE/Anaphylaxis), II(Ab/AIHA/ITP), III(IC/SLE/Serum Sickness), IV(T-Cell/Contact/TB/Drug), V(Stimulatory/Graves). Anaphylaxis: Adrenaline IM 0.5mg 1:1000 anterolateral thigh q5min → O2/IV Fluids/Chlorphenamine/Hydrocortisone → Observe 6-12h Biphasic → Tryptase 1-2h peak. Asthma: BTS Steps 1-6 → SMART/MART → Biologics (Anti-IgE/IL5/IL-4R/TSLP). SJS/TEN/DRESS: BSA<10%/10-30%/>30%, DRESS=Liver/HHV-6/2-8w, SCORTEN. Allergy: SPT/sIgE/CRD/BAT/OFC. Desensitisation: Penicillin/Aspirin/Carboplatin." | Compressed. |

---

## 17. 📌 Summary
- **Gell & Coombs**: Type I (IgE/Anaphylaxis), Type II (Ab-mediated), Type III (IC/SLE), Type IV (T-cell/Contact/Drug), Type V (Stimulatory/Graves)
- **Anaphylaxis**: **Adrenaline IM 0.5mg (1:1000) Anterolateral Thigh** — **FIRST-LINE, NO CONTRAINDICATION**; Repeat q5min; **Observe 6-12h** (Biphasic); **Tryptase 1-2h peak**
- **Asthma**: **BTS/SIGN Steps 1-6**, **SMART/MART** (Buda/Form, Beclo/Form), **Biologics** (Anti-IgE, Anti-IL5, Anti-IL4R, Anti-TSLP)
- **Allergic Rhinitis**: **ARIA** (Intermittent/Persistent × Mild/Mod-Sev); **INCS ± H1 ± LTRA**; **AIT (SCIT/SLIT 3-5y)**
- **Food Allergy**: **IgE (Min-2h) vs Non-IgE (Hrs-Days)**; **CRD** (Ara h 1/2/3 = Risk, 8/9 = Cross); **OFC = Gold Standard**
- **Drug Hypersensitivity**: **SCARs** — **SJS/TEN/DRESS/AGEP**; **SCORTEN (TEN), RegiSCAR (DRESS)**; **Desensitisation** (Penicillin, Aspirin, Carboplatin)
- **Allergy Testing**: **SPT** (Wheal ≥3mm, Stop AntiH 48-72h); **sIgE (ImmunoCAP)**; **CRD** (Ara h 1/2/3 = Risk, 8/9 = Cross); **BAT (CD63/CD203c)**; **Patch (Day 48/72h)**; **OFC = Gold Standard**
- **Drug Desensitisation**: Penicillin (Rapid/Slow), Aspirin (AERD), Carboplatin (12-step), Allopurinol (Avoid)

---

## 18. ❓ MCQs (10)

1. **First-line treatment for anaphylaxis:**  
   A. IV Hydrocortisone  B. **Adrenaline IM 0.5mg (1:1000)**  C. Chlorphenamine  D. Salbutamol Nebuliser  
   *Answer: B. Adrenaline IM 0.5mg (1:1000) anterolateral thigh — FIRST-LINE, NO contraindication.*

2. **Biphasic anaphylaxis — observation period?**  
   A. 1 hour  B. **6-12 hours**  C. 24 hours  D. 48 hours  
   *Answer: B. Observe 6-12 hours post-resolution (Biphasic peak 3-10h).*

3. **Serum tryptase — optimal timing for anaphylaxis confirmation?**  
   A. Immediately  B. **1-2 hours post-onset**  C. 6 hours  D. 24 hours  
   *Answer: B. Peak at 1-2 hours; half-life ~2h; >11.4 ng/mL or >2x baseline supports diagnosis.*

4. **SJS vs TEN — key differentiator?**  
   A. Mucosal involvement  B. **BSA Detachment (<10% SJS, >30% TEN)**  C. Fever  D. Drug cause  
   *Answer: B. BSA Detachment: SJS <10%, SJS/TEN 10-30%, TEN >30%.*

5. **DRESS vs SJS/TEN — key distinguishing feature?**  
   A. Mucosal involvement  B. **Fever, Eosinophilia, Visceral (Liver), HHV-6 Reactivation**  C. Nikolsky sign  D. Drug cause  
   *Answer: B. DRESS = Fever, Eosinophilia, Lymphadenopathy, Visceral (Liver), HHV-6 Reactivation (2-8w onset).*

6. **Asthma biologics — Anti-IL5 (Mepolizumab) indication?**  
   A. All severe asthma  B. **Severe Eosinophilic Asthma (Blood Eos ≥150-300/μL)**  C. Allergic asthma only  D. Exercise-induced asthma  
   *Answer: B. Severe Eosinophilic Asthma (Blood Eos ≥150-300/μL).*

7. **Food allergy — Component-Resolved Diagnostics for Peanut:**  
   A. Ara h 8 = High risk  B. **Ara h 1/2/3 = Primary sensitisers (High Risk); Ara h 8/9 = Cross-reactivity**  C. Ara h 9 = Primary  D. All equal  
   *Answer: B. Ara h 1/2/3 = Primary sensitisation (High risk); Ara h 8/9 = Cross-reactivity (Bet v 1/LTP).*

7. **Penicillin allergy — desensitisation approach?**  
   A. Not possible  B. **Rapid (4-6h) or Slow (Days) — Incremental doses under monitoring**  C. Single dose challenge  D. Only with antihistamine cover  
   *Answer: B. Rapid (4-6h) or Slow (Days) — Incremental doses under monitoring.*

8. **Skin Prick Test — positive criteria?**  
   A. Wheal ≥2mm  B. **Wheal ≥3mm (vs Negative Control)**  C. Flare ≥10mm  D. Any wheal  
   *Answer: B. Wheal ≥3mm larger than negative control.*

9. **Oral Food Challenge — gold standard for?**  
   A. Aeroallergy  B. **Food Allergy Diagnosis**  C. Drug Allergy  D. Contact Dermatitis  
   *Answer: B. Double-Blind Placebo-Controlled Food Challenge (DBPCFC) = Gold Standard for Food Allergy.*

10. **Drug desensitisation — when indicated?**  
    A. All drug allergies  B. **No Alternative Drug Available (e.g., Penicillin in Syphilis, Aspirin in AERD, Carboplatin in Ovarian Cancer)**  C. Only for IgE-mediated  D. Never  
    *Answer: B. When no safe alternative exists (Penicillin in Syphilis, Aspirin in AERD, Carboplatin in Ovarian Cancer).*

---

## 19. 📋 SBAs (10)

1. **25F with anaphylaxis to peanut. Adrenaline IM 0.5mg given. Still wheezy, BP 80/50 after 5min. Next step?**  
   A. **Repeat Adrenaline IM 0.5mg**  B. IV Hydrocortisone  C. IV Chlorphenamine  D. Salbutamol Neb  
   *Answer: A. Repeat Adrenaline IM 0.5mg q5min if no improvement.*

2. **Patient on carbamazepine develops fever, rash, eosinophilia 3.5x10⁹/L, ALT 300, HHV-6 PCR+. Diagnosis?**  
   A. SJS  B. TEN  C. **DRESS**  D. AGEP  
   *Answer: C. DRESS (Drug Reaction with Eosinophilia and Systemic Symptoms) — Fever, Rash, Eosinophilia, Hepatitis, HHV-6 reactivation.*

3. **Asthma patient on Step 4 (Medium-dose ICS/LABA) still uncontrolled. Blood Eos 400/μL, FeNO 45ppb. Add-on?**  
   A. Tiotropium  B. Montelukast  C. **Mepolizumab (Anti-IL5)**  D. Omalizumab  
   *Answer: C. Anti-IL5 (Mepolizumab/Reslizumab/Benralizumab) for Severe Eosinophilic Asthma (Eos ≥150-300/μL).*

4. **Child with peanut allergy — Ara h 2 positive, Ara h 8 negative. Risk?**  
   A. Low (Cross-reactivity)  B. **High (Primary Sensitisation)**  C. Moderate  D. None  
   *Answer: B. Ara h 2 = Primary Sensitiser = High Risk for Systemic Reaction.*

5. **Patient on allopurinol develops fever, rash, eosinophilia 2x10⁹/L, pustules. Onset Day 3. Diagnosis?**  
   A. SJS  B. DRESS  C. **AGEP** (Acute Generalised Exanthematous Pustulosis)  D. TEN  
   *Answer: C. AGEP — Acute onset (1-5d), Neutrophilic Pustules, Neutrophilia, Self-limiting.*

---

## 20. 🔑 Answer Keys
| MCQs | SBAs |
|------|------|
| 1-B, 2-B, 3-B, 4-B, 5-B, 6-B, 7-B, 8-B, 9-B, 10-B | 1-B, 2-C, 3-C, 4-B, 5-C |

---

## 21. 🔗 Cross-Links
- [[3.1 Mechanisms of Autoimmunity]] — Type II/III/IV hypersensitivity in autoimmunity
- [[3.2 Systemic Autoimmune Diseases]] — SLE, Vasculitis, Drug-induced autoimmunity
- [[3.3 Organ-Specific Autoimmune Diseases]] — MG, MS, Thyroid, Coeliac hypersensitivity
- [[4.3 X-Linked Disorders]] — G6PD deficiency (Drug-induced haemolysis)
- [[5.1-5.4 Genetic Testing Technologies]] — HLA typing for drug hypersensitivity (HLA-B*15:02, HLA-B*57:01, HLA-B*58:01)
- [[5.4 Prenatal & Preimplantation Testing]] — Allergy prevention in pregnancy
- [[5.5 Genetic Counselling]] — Allergy risk counselling, Family history
- [[6.1 Hereditary Cancer Syndromes]] — Paraneoplastic syndromes (Autoimmune)
- [[6.2-6.3 Tumour Immunology & Immunotherapy]] — irAEs (Checkpoint inhibitor colitis, thyroiditis, pneumonitis)
- [[7.1-7.6 Immune-Based Therapies]] — Biologics used for allergy/asthma (Omalizumab, Mepolizumab, Dupilumab)
- [[8.1-8.6 Special Situations Immunology]] — Pregnancy (Allergy), Ageing (Immunosenescence)
- [[9. ELSI]] — Genetic discrimination in allergy, DTC testing
- [[10. System-Based Clinical Genetics]] — Allergy genetics (IL4, IL13, FLG, TSLP)

---

**Last Updated:** 2026-06-15  
**Next:** Build `5.1-5.4 Transplant Immunology.md`
