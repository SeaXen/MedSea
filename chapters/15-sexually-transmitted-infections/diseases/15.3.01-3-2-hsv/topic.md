**Parent Topic:** [STI MOC](../Sexually%20Transmitted%20Infections%20MOC.md) → [STI Hierarchy](../Davidson%20Chapter%2013%20-%20STI%20Hierarchy.md)  
**Status:** `full-fcps-mrcp-note`  
**Priority:** ⭐⭐⭐ HIGHEST (FCPS/MRCP — Common, Recurrent, Neonatal, Serology, Suppressive Therapy)  
**Source:** Davidson 24th Ed Ch 13; WHO/BASHH/CDC Guidelines; FCPS/MRCP Syllabus; NICE NG196

---

## 1. 🎯 Learning Objectives
- [ ] Differentiate **HSV-1 vs HSV-2** epidemiology, clinical features, recurrence patterns
- [ ] Diagnose **primary vs recurrent genital herpes** and **extra-genital manifestations** (Pharyngeal, Rectal, Sacral, Neonatal)
- [ ] Apply **diagnostic algorithms** (NAAT, PCR, Culture, Serology, Tzanck) and interpret results
- [ ] Apply **episodic vs suppressive antiviral therapy** (Acyclovir, Valacyclovir, Famciclovir)
- [ ] Manage **HSV in Pregnancy** (Neonatal Prevention, Cesarean Indication, Acyclovir Suppression)
- [ ] Manage **Neonatal HSV** (Disseminated, CNS, SEM — Classification & Treatment)
- [ ] Manage **HSV in Immunocompromised** (Severe Mucocutaneous, Resistance)
- [ ] Answer viva: "Primary vs Recurrent HSV" and "Neonatal HSV Classification" and "Cesarean Indication" and "Suppressive Therapy Indications"

---

## 2. 🧠 Core Concept: HSV Biology & Pathogenesis

```mermaid
flowchart TD
    A[Herpes Simplex Virus] --> B[HSV-1 (Oral/Facial)]
    A --> C[HSV-2 (Genital)]
    B & C --> D[Alpha-Herpesvirus]
    D --> D1[Enveloped, dsDNA]
    D --> D2[Neurotropic]
    D --> D3[Latency in Sensory Ganglia]
    B & C --> E[Transmission]
    E --> E1[Direct Contact (Viral Shedding)]
    E --> E2[Asymptomatic Shedding (Major Driver)]
    E --> E3[Vertical (Neonatal)]
    D3 --> F[Reactivation Triggers]
    F --> F1[Stress, UV, Fever, Trauma, Immunosuppression, Hormonal]
    D3 --> G[Clinical Manifestations]
    G --> G1[Primary Infection]
    G --> G2[Recurrent Episodes]
    G --> G3[Asymptomatic Shedding]
    G --> G4[Neonatal HSV]
    G --> G5[Extra-Genital (Whitelow, Keratitis, Encephalitis)]
```

---

## 1️⃣ HSV-1 vs HSV-2 — Epidemiology & Clinical Differences

| Feature | HSV-1 | HSV-2 |
|---------|-------|-------|
| **Traditional Site** | **Orolabial** (Cold Sores) | **Genital** |
| **Current Trend** | **Increasing Genital HSV-1** (Oral Sex) | Still Predominantly Genital |
| **Global Seroprevalence** | **67% (<50y)** — 3.7 Billion | **13% (15-49y)** — 491 Million |
| **Genital Infection** | **Rising** (30-50% New Genital Herpes = HSV-1) | **Declining Proportion** |
| **Recurrence Rate (Genital)** | **Low** (~1/Year After 1st Year) | **High** (~4-5/Year) |
| **Asymptomatic Shedding** | Less Frequent (Genital) | **More Frequent** (Genital) |
| **Neonatal Transmission** | **Higher Risk** (Primary Infection in Pregnancy) | **Lower Risk** (But More Common Source) |
| **Primary Episode Severity** | Often Mild | Often Severe |

> **Key**: **HSV-1 = Increasing Cause of Genital Herpes**; **HSV-2 = More Frequent Recurrences, More Asymptomatic Shedding**

---

## 2️⃣ Clinical Manifestations

### Primary Genital Herpes (First Episode)

| Feature | Detail |
|---------|--------|
| **Incubation** | **2-12 Days** (Median 4 Days) |
| **Systemic Symptoms** | **Fever, Malaise, Myalgia, Headache, Inguinal Lymphadenopathy** (Bilateral, Tender) |
| **Local Symptoms** | **Pain, Burning, Pruritus** → **Multiple Vesicles → Painful Ulcers** (Coalesce), Mucopurulent Discharge |
| **Lesion Distribution** | **Vulva, Vagina, Cervix, Penis, Perianal, Thighs, Buttocks** |
| **Duration (Untreated)** | **2-4 Weeks** (Viral Shedding ~12 Days) |
| **Complications** | **Aseptic Meningitis** (10-15%, HSV-2), **Urinary Retention** (Sacral Radiculopathy), **Proctitis** (MSM), **Pharyngitis** (Oral Sex) |

### Recurrent Genital Herpes

| Feature | Detail |
|---------|--------|
| **Prodrome** | **Burning, Tingling, Pruritus** at Recurrence Site (Hours-Days Before Lesions) |
| **Lesions** | **Fewer Vesicles/Ulcers**, **Smaller**, **Less Painful**, **Shorter Duration** |
| **Systemic Symptoms** | **Absent or Mild** (No Fever, Minimal Lymphadenopathy) |
| **Duration (Untreated)** | **5-10 Days** (Viral Shedding ~5 Days) |
| **Frequency** | **HSV-2: 4-5/Year** (Range 0-12+); **HSV-1: ~1/Year** |
| **Triggers** | **Stress, UV, Fever, Trauma, Immunosuppression, Menstruation, Friction** |

### Extra-Genital Manifestations

| Manifestation | Features |
|---------------|----------|
| **Herpetic Whitlow** | **Vesicular/Pustular Lesions on Fingers** (Healthcare Workers, Autoinoculation), Painful, Tender |
| **Herpes Keratitis** | **Dendritic Ulcer** (Cornea), Pain, Photophobia, Blurred Vision — **Ophthalmic Emergency** |
| **Herpes Encephalitis** | **HSV-1** (Temporal Lobe), Fever, Confusion, Seizures, Focal Deficits — **Acute Emergency** |
| **Eczema Herpeticum** | **Disseminated Vesicles** on Eczematous Skin, Fever, Malaise — **Dermatological Emergency** |
| **Sacral/Radiculomyelitis** | **Urinary Retention**, Saddle Anaesthesia, Leg Weakness (S2-S4 Roots) |
| **Herpes Gladiatorum** | **Wrestlers/Contact Sports** — Face, Neck, Arms |

---

## 3️⃣ Diagnosis — Algorithms & Interpretation

### Diagnostic Algorithm
```mermaid
flowchart TD
    A[Suspected Genital Herpes] --> B{Lesions Present?}
    B -->|Yes| C[NAAT (PCR) — Preferred<br/>(Vesicle Fluid, Ulcer Base Swab)]
    B -->|No (Screening/Asymptomatic)| D[Type-Specific Serology (IgG)<br/>HSV-1 vs HSV-2 gG-Based]
    C --> E{NAAT Result}
    E -->|Positive| F[Type Subtyping (HSV-1 vs HSV-2)<br/>→ Counselling, Prognosis, Tx]
    E -->|Negative| G[Consider Alternative<br/>(Syphilis, Chancroid, LGV, Aphthosis)]
    D --> H{Serology Result}
    H -->|HSV-2 +ve| I[Genital Herpes Likely<br/>(HSV-2 = Genital)] 
    H -->|HSV-1 Only| J[Genital HSV-1 Possible<br/>(Oral→Genital) or Past Oral]
    H -->|Both +ve| K[Dual Infection or Cross-Reactivity]
```

### Diagnostic Test Comparison

| Test | Sensitivity | Specificity | TAT | Best Use |
|------|-------------|-------------|-----|----------|
| **NAAT (PCR)** | **>95%** | **>98%** | 1-24h | **1st Line (Lesions)** — Vesicle Fluid/Ulcer Swab |
| **Viral Culture** | 70-80% | **100%** | 24-48h | **Viability, Typing, Resistance** (If NAAT Unavailable) |
| **Type-Specific Serology (IgG)** | 90-95% | 95-98% | Hours-Days | **Asymptomatic Screening, Partner Testing, Pregnancy** — **gG-Based (HSV-1 gG1, HSV-2 gG2)** |
| **Tzanck Smear** | 60-70% | 80-90% | Minutes | **Bedside** (Multinucleated Giant Cells) — Not Type-Specific |
| **DFA (Direct Fluorescent Antibody)** | 80-90% | 95% | Hours | **Rapid** (Lesion Smear) — Type-Specific |
| **Non-Type-Specific Serology** | Poor | Poor | — | **NOT RECOMMENDED** (Cross-Reactivity, Confusing) |

> **Key**: **NAAT = 1st Line for Lesions**; **Type-Specific IgG (gG-Based) = 1st Line for Asymptomatic/Pregnancy/Partner Testing**

### Type-Specific Serology Interpretation

| Result | Interpretation |
|--------|----------------|
| **HSV-2 IgG +ve** | **Genital Herpes Likely** (HSV-2 = Genital) — Counsel on Transmission, Recurrence, Suppressive Therapy |
| **HSV-1 IgG +ve, HSV-2 IgG -ve** | **Past Oral HSV-1** OR **Genital HSV-1** (If Genital Symptoms) — Increasing Genital HSV-1 |
| **Both +ve** | **Dual Infection** OR **Cross-Reactivity** (Older Assays) — **gG-Based = High Specificity** |
| **Both -ve** | **Susceptible** — Primary Infection Risk (Neonatal Risk if Partner +ve) |

> **Important**: **IgM Not Recommended** (Poor Specificity, Persistent After Primary); **IgG gG-Based = Standard**

---

## 4️⃣ Treatment — Antiviral Therapy

### Antiviral Agents

| Drug | Bioavailability | Half-Life | Dosing Frequency | Key Advantage |
|------|----------------|-----------|------------------|---------------|
| **Acyclovir** | 15-30% (Oral) | 2.5-3.3h | **5x Daily** (Standard) | **Cheapest**, IV Formulation |
| **Valacyclovir** | 54% (Prodrug → Acyclovir) | 2.5-3.3h | **2-3x Daily** | **Better Bioavailability**, Less Frequent Dosing |
| **Famciclovir** | 77% (Prodrug → Penciclovir) | 2.5-3.3h | **2-3x Daily** | **Longer Intracellular Half-Life**, Good Compliance |

> **Mechanism**: **Viral Thymidine Kinase** → Phosphorylation → **DNA Polymerase Inhibition** → **Chain Termination**

### Episodic Treatment (Primary & Recurrent)

| Episode | Regimen (Choose One) |
|---------|----------------------|
| **Primary** | **Acyclovir 400mg 5x Daily × 7-10 Days** OR **Valacyclovir 1g BD × 7-10 Days** OR **Famciclovir 250mg TDS × 7-10 Days** |
| **Recurrent** | **Acyclovir 400mg 5x Daily × 5 Days** OR **Valacyclovir 500mg BD × 3-5 Days** OR **Famciclovir 125mg BD × 5 Days** (Or **Famciclovir 1g Stat × 2 Doses 12h Apart**) |
| **Initiation** | **Within 24h of Prodrome/Lesion Onset** — **Earlier = Better** |

> **Key**: **Start Within 24h of Prodrome/Onset**; **Valacyclovir/Famciclovir Preferred** (Better Compliance, Less Frequent Dosing)

### Suppressive Therapy (Chronic Suppression)

| Indication | Criteria |
|------------|----------|
| **Frequent Recurrences** | **≥6 Episodes/Year** (Or ≥4 if Severe/Distressing) |
| **Psychosocial Impact** | **Significant Anxiety, Relationship Issues, Sexual Dysfunction** |
| **Discordant Couple** | **HSV-2 +ve Partner** → Reduce Transmission to Susceptible Partner |
| **Pregnancy (3rd Trimester)** | **HSV-2 +ve or Primary HSV in Pregnancy** → **36 Weeks to Delivery** |
| **Immunocompromised** | **HIV, Transplant, Immunosuppression** — Reduce Severity/Shedding |

### Suppressive Regimens

| Drug | Regimen | Duration | Monitoring |
|------|---------|----------|------------|
| **Acyclovir** | **400mg BD** (Or 200mg QID) | **6-12 Months** (Reassess) | Renal Function (If Renal Impairment: Dose Adjust) |
| **Valacyclovir** | **500mg OD** (500mg BD if HIV+) | **6-12 Months** | Renal Function |
| **Famciclovir** | **250mg BD** | **6-12 Months** | Hepatic Function |

> **Reassessment**: **After 6-12 Months** — Attempt **Drug Holiday** (Stop 3-6 Months, Reassess Recurrence Frequency)

### Treatment Efficacy (Suppressive Therapy)
| Outcome | Reduction |
|---------|-----------|
| **Recurrence Frequency** | **70-80%** |
| **Asymptomatic Shedding** | **80-90%** |
| **Transmission to Partner** | **~50%** (Valacyclovir 500mg OD) |

---

## 5️⃣ HSV in Pregnancy & Neonatal Prevention

### Maternal HSV Infection Risk to Neonate

| Maternal Scenario | Neonatal Risk | Management |
|-------------------|---------------|------------|
| **Primary HSV (1st/2nd Trimester)** | **Low (<1%)** (Maternal Antibodies Transfer) | **Acyclovir 400mg TDS 36w→Delivery** (Consider) |
| **Primary HSV (3rd Trimester/Peripartum)** | **HIGH (30-50%)** (No Maternal Antibodies, High Viral Load) | **Acyclovir 400mg TDS 36w→Delivery**; **Cesarean if Active Lesions/Prodrome at Labour** |
| **Recurrent HSV (Any Trimester)** | **Low (1-3%)** (Maternal Antibodies Protective) | **Acyclovir 400mg TDS 36w→Delivery** (Standard); **Cesarean ONLY if Active Lesions/Prodrome at Labour** |
| **Primary HSV at Labour** | **VERY HIGH (50%+)** | **Urgent Cesarean** (Within 4-6h of Membrane Rupture) + **Neonatal Acyclovir IV** |
| **Unknown Status (Lesions at Labour)** | **Assume Primary** | **Cesarean** (If Within 4-6h of Rupture) + **Maternal/Neonatal Acyclovir** |

### Suppressive Therapy in Pregnancy
| Scenario | Regimen |
|----------|---------|
| **HSV-2 +ve (Recurrent)** | **Acyclovir 400mg TDS from 36 Weeks → Delivery** (Standard) |
| **Primary HSV in 3rd Trimester** | **Acyclovir 400mg TDS from Diagnosis → Delivery** + **Cesarean if Active Lesions at Labour** |
| **HIV Co-infection** | **Valacyclovir 500mg BD** (Preferred — Better Bioavailability) |

### Cesarean Section Indications
| Scenario | Recommendation |
|----------|----------------|
| **Active Genital Lesions at Onset of Labour** | **Elective Cesarean** (Before Membrane Rupture) |
| **Prodromal Symptoms (Pain, Tingling) at Labour** | **Cesarean** (Viral Shedding Likely) |
| **Primary HSV in 3rd Trimester/Peripartum** | **Cesarean** (Ideally Before Membrane Rupture, ≤4-6h After Rupture) |
| **Recurrent HSV (No Lesions/Prodrome)** | **Vaginal Delivery OK** (Suppressive Therapy from 36w) |
| **Membrane Rupture >4-6h with Active Lesions** | **Cesarean Benefit Diminished** — Vaginal Delivery + Neonatal Prophylaxis |

---

## 6️⃣ Neonatal HSV — Classification & Management

### Classification (Kimberlin)

| Type | Features | Mortality (Untreated) | Sequelae |
|------|----------|----------------------|----------|
| **SEM (Skin, Eye, Mouth)** | **Vesicles on Skin, Conjunctivitis, Oral Mucosa** | **4%** | Minimal if Treated Early |
| **CNS (Central Nervous System)** | **Encephalitis** (Seizures, Lethargy, Irritability, Bulging Fontanelle), CSF Pleocytosis | **15%** | **Significant Neurodevelopmental Delay** (50%+) |
| **DIS (Disseminated)** | **Multi-Organ** (Hepatitis, Pneumonitis, Coagulopathy, Thrombocytopenia, Adrenal Necrosis, Skin Lesions ± CNS) | **57%** | **High Neurodevelopmental Disability** (Survivors) |

> **Note**: **~45% SEM**, **30% CNS**, **25% DIS**; **Overlap Common** (SEM + CNS = CNS Disease)

### Neonatal HSV — Diagnosis

| Test | Sample | Timing |
|------|--------|--------|
| **HSV PCR (NAAT)** | **CSF (Mandatory)**, Blood, Surface Swabs (Conjunctiva, Oral, Rectal, Skin Lesions) | **At Suspicion / 24-48h Post-Birth** (If High Risk) |
| **Viral Culture** | CSF, Blood, Surface Swabs | If PCR Unavailable |
| **CSF Analysis** | WBC, Protein, Glucose, HSV PCR | **Mandatory** (CNS/DIS Classification) |
| **Liver Function** | ALT, AST, Coagulation | DIS Monitoring |

> **Critical**: **HSV PCR on CSF = Gold Standard for CNS/DIS**; **Surface Swabs (Conjunctiva, Oral, Rectal) at 24h** for SEM

### Neonatal HSV — Treatment (IV Acyclovir)

| Classification | Regimen | Duration |
|----------------|---------|----------|
| **SEM** | **Acyclovir 20mg/kg IV q8h** | **14 Days** |
| **CNS** | **Acyclovir 20mg/kg IV q8h** | **21 Days** |
| **DIS** | **Acyclovir 20mg/kg IV q8h** | **21 Days** (Longer if Persistent Viremia) |

> **Key**: **Acyclovir IV 20mg/kg q8h**; **Adjust for Renal Function**; **CSF PCR at End of Therapy (CNS/DIS) — If +ve → Extend**

### Neonatal HSV — Post-Treatment Suppression

| Regimen | Duration |
|---------|----------|
| **Oral Acyclovir 300mg/m²/dose TDS** | **6 Months** (Post-IV) — **Improves Neurodevelopmental Outcomes** (CNS/DIS) |

---

## 6️⃣ HSV in Immunocompromised & Resistance

### Immunocompromised (HIV, Transplant, Chemotherapy)

| Feature | Detail |
|---------|--------|
| **Clinical** | **Severe, Extensive, Chronic, Non-Healing Ulcers**, Atypical Presentations, Higher Dissemination Risk |
| **Diagnosis** | **NAAT + Culture (Resistance Testing)** |
| **Treatment** | **Higher Doses/Longer Durations** — Acyclovir 400mg 5x Daily (Episodic), **Suppressive: Valacyclovir 500mg BD** (HIV) |
| **Resistance** | **Thymidine Kinase (TK) Mutations** → **Acyclovir/Valacyclovir/Famciclovir Cross-Resistance** |
| **Resistant HSV Treatment** | **Foscarnet 40mg/kg IV q8h** (TK Mutants); **Cidofovir 5mg/kg IV Weekly** (Alternative); **Topical Cidofovir/Imuquimod** (Mucocutaneous) |

### HSV Resistance
| Mutation | Mechanism | Cross-Resistance |
|----------|-----------|------------------|
| **TK (Thymidine Kinase)** | Defective Phosphorylation | **Acyclovir/Valacyclovir/Famciclovir** (All) |
| **DNA Polymerase** | Altered Drug Binding | **Foscarnet/Cidofovir** (Usually Sensitive) |

---

## 6️⃣ Counselling & Partner Management

### Key Counselling Points
| Topic | Key Messages |
|-------|--------------|
| **Transmission** | **Asymptomatic Shedding = Major Driver**; **HSV-2 > HSV-1**; **Condoms Reduce Risk ~30-50%** |
| **Recurrence** | **Prodrome = Infectious**; **Suppressive Therapy Reduces Frequency/Shedding/Transmission** |
| **Pregnancy** | **Primary = High Risk; Recurrent = Low Risk**; **Cesarean if Active Lesions at Labour** |
| **Neonatal** | **Rare but Serious**; **Suppression 36w→Delivery Reduces Risk** |
| **Psychosocial** | **Stigma, Anxiety, Relationship Impact** — **Counselling, Support Groups, Accurate Information** |
| **Partner Testing** | **Type-Specific Serology** — If Partner -ve → Discordant Couple → Suppressive Therapy + Condoms |
| **Disclosure** | **Ethical/Legal Duty** (Varies by Jurisdiction) — **Before Sexual Contact** |

---

## 3. ⚡ FCPS/MRCP High-Yield Summary

| Topic | Key Points |
|-------|------------|
| **HSV-1 vs HSV-2** | **HSV-1: Orolabial → Increasing Genital (Oral Sex); HSV-2: Predominantly Genital**; **HSV-2 > Recurrences, Asymptomatic Shedding** |
| **Primary vs Recurrent** | **Primary: Systemic (Fever, Lymphadenopathy), Severe, 2-4 Weeks**; **Recurrent: Prodrome, Fewer Lesions, Shorter (5-10 Days), No Systemic** |
| **Diagnosis** | **NAAT (PCR) = 1st Line (Lesions)**; **Type-Specific IgG (gG-Based) = Asymptomatic/Pregnancy/Partner**; **Tzanck = Bedside (Multinucleated Giant Cells)** |
| **Episodic Treatment** | **Acyclovir 400mg 5x/d × 7-10d (Primary), ×5d (Recurrent)**; **Valacyclovir 1g BD × 7-10d (Primary), 500mg BD × 3-5d (Recurrent)** |
| **Suppressive Therapy** | **≥6 Recurrences/Year**, Discordant Couple, Pregnancy (36w→Delivery), Psychosocial; **Valacyclovir 500mg OD / Acyclovir 400mg BD** |
| **Pregnancy** | **Primary 3rd Trimester = HIGH Risk (Cesarean if Active Lesions at Labour)**; **Recurrent = Low Risk (Vaginal OK if No Lesions)**; **Suppression 36w→Delivery** |
| **Neonatal HSV** | **SEM (Skin/Eye/Mouth) = 14d IV Acyclovir**; **CNS = 21d IV Acyclovir + 6mo Oral Suppression**; **DIS = 21d IV Acyclovir** |
| **Neonatal Prevention** | **Primary at Labour = Cesarean + Neonatal IV Acyclovir**; **Recurrent = Suppression 36w→Delivery, Cesarean if Active Lesions** |
| **Resistance** | **TK Mutations → Acyclovir/Valacyclovir/Famciclovir Cross-R** → **Foscarnet IV** |
| **Suppressive Therapy Reduces** | **Recurrences 70-80%**, **Shedding 80-90%**, **Transmission ~50%** |

---

## 4. 🎤 Viva Questions (Expected Answers)

| # | Question | Expected Answer |
|---|----------|-----------------|
| 1 | Primary vs Recurrent genital herpes — clinical differences? | **Primary: Fever, Bilateral Tender Lymphadenopathy, Multiple Vesicles/Ulcers, 2-4 Weeks**; **Recurrent: Prodrome (Tingling/Burning), Fewer/Smaller Lesions, No Systemic Symptoms, 5-10 Days** |
| 2 | HSV-1 vs HSV-2 genital infection — key differences? | **HSV-1: Increasing Genital (Oral Sex), Lower Recurrence Rate (~1/Year), Less Shedding**; **HSV-2: Predominantly Genital, High Recurrence (~4-5/Year), More Asymptomatic Shedding** |
| 3 | Neonatal HSV classification & treatment durations? | **SEM (Skin/Eye/Mouth): IV Acyclovir 20mg/kg q8h × 14 Days**; **CNS: IV Acyclovir 20mg/kg q8h × 21 Days + 6mo Oral Suppression**; **DIS: IV Acyclovir 20mg/kg q8h × 21 Days** |
| 4 | HSV in pregnancy — management algorithm? | **Primary 3rd Trimester/Peripartum = HIGH Risk → Cesarean if Active Lesions at Labour + Neonatal IV Acyclovir**; **Recurrent = Low Risk → Vaginal OK if No Lesions; Suppression 36w→Delivery**; **Primary at Labour = Cesarean Within 4-6h of Membrane Rupture** |
| 5. Neonatal HSV — when is Cesarean indicated? | **Active Genital Lesions at Onset of Labour**; **Prodromal Symptoms at Labour**; **Primary HSV in 3rd Trimester/Peripartum**; **Membrane Rupture <4-6h with Active Lesions** |
| 6. HSV suppressive therapy — indications & regimen? | **≥6 Recurrences/Year, Discordant Couple, Pregnancy (36w→Delivery), Psychosocial Distress**; **Valacyclovir 500mg OD or Acyclovir 400mg BD**; **Reassess at 6-12 Months** |
| 7. HSV resistance — mechanism & treatment? | **TK (Thymidine Kinase) Mutations → Acyclovir/Valacyclovir/Famciclovir Cross-Resistance** → **Foscarnet 40mg/kg IV q8h** (IV Only); **Cidofovir Alternative** |
| 8. HSV diagnosis — when to use NAAT vs Serology? | **NAAT (PCR) = Lesions Present (1st Line, Type-Specific)**; **Type-Specific IgG (gG-Based) = Asymptomatic, Pregnancy, Partner Testing, No Lesions** |
| 9. HSV in HIV — differences in management? | **Higher Doses/Longer Duration**; **Episodic: Acyclovir 400mg 5x/d (Higher); Suppressive: Valacyclovir 500mg BD**; **Resistance More Common (TK Mutations)** |
| 10. Cesarean for HSV — timing relative to membrane rupture? | **Before Membrane Rupture (Ideally)**; **Within 4-6 Hours of Rupture if Already Ruptured**; **Benefit Diminished After 6h** |

---

## 5. 🧩 Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **"HSV-1 = Only Oral, HSV-2 = Only Genital"** | **NO.** **HSV-1 Increasingly Causes Genital Herpes** (Oral Sex); **HSV-2 Can Cause Oral** (Oral Sex) |
| **"Recurrent HSV = Always Mild"** | **NO.** **Can Be Severe** (Immunocompromised, Extensive, Prolonged); **Sacral Radiculopathy (Urinary Retention) Possible** |
| **"Asymptomatic = Not Infectious"** | **NO.** **Asymptomatic Shedding = Major Driver of Transmission** (HSV-2 > HSV-1) |
| **"Suppressive Therapy = Cure"** | **NO.** **Reduces Frequency/Shedding/Transmission** — **Not Eradication**; **Latency Persists** |
| **"Cesarean = 100% Prevents Neonatal HSV"** | **NO.** **Risk Reduced ~85%**; **Transascending Infection Possible (Membrane Rupture to Delivery)**; **Also Intrauterine Infection Rare** |
| **"Acyclovir Resistance = Just Use Valacyclovir"** | **NO.** **TK Mutation = Cross-Resistance to Acyclovir/Valacyclovir/Famciclovir** → **Foscarnet** |
| **"HSV IgM = Acute Infection"** | **NO.** **IgM Poor Specificity, Persists, Not Recommended**; **Type-Specific IgG (gG-Based) = Standard** |
| **"All Genital Ulcers = HSV"** | **NO.** **DDx: Syphilis (Painless Indurated), Chancroid (Painful+Suppurative Buboes), LGV (Painless Primary→Buboes), Behçet, Aphthous, Drug Eruption** |
| **"Suppressive Therapy = Lifelong Mandatory"** | **NO.** **Reassess at 6-12 Months**; **Drug Holiday (Stop 3-6 Months), Reassess Recurrence** |
| **"HSV-1 Genital = Less Severe Than HSV-2"** | **Primary HSV-1 Can Be Severe**; **But Recurrences Much Less Frequent (~1/Year vs 4-5/Year)** |

> **Mnemonic: HSV MASTER MANAGEMENT**  
> **H**SV-1 vs HSV-2: **HSV-1 Oral→Genital (Oral Sex), Low Recurrence; HSV-2 Genital, High Recurrence/High Shedding**  
> **S**erology: **Type-Specific IgG (gG-Based) = Standard; IgM NOT Recommended**  
> **V**iral NAAT: **Lesions → PCR (1st Line, Type-Specific); No Lesions → Type-Specific IgG**  
> **P**rimary vs Recurrent: **Primary = Systemic (Fever, LAD), Severe, 2-4w; Recurrent = Prodrome, Fewer Lesions, 5-10d**  
> **E**pisodic Tx: **Acyclovir 400mg 5x/d ×7-10d (Primary), ×5d (Recurrent); Valacyclovir 1g BD (Primary), 500mg BD (Recurrent)**  
> **S**uppressive: **≥6/Year, Discordant Couple, Pregnancy (36w→Delivery), Psychosocial**; **Valacyclovir 500mg OD / Aci 400mg BD**  
> **R**esistance: **TK Mutations → ACV/VCV/FCV Cross-R → Foscarnet IV**  
> **P**regnancy: **Primary 3rd Tri = HIGH Risk (Cesarean if Active); Recurrent = Low Risk; Suppression 36w→Delivery**  
> **N**eonatal: **SEM (14d), CNS (21d + 6mo Oral Suppression), DIS (21d)** — **IV Acyclovir 20mg/kg q8h**  
> **C**esarean Indication: **Active Lesions/Prodrome at Labour; Primary 3rd Tri/Peripartum**; **Vaginal OK if Recurrent + No Lesions**  
> **T**reatment Adjustment: **HIV: Higher Doses/Longer (Aci 400mg 5x/d, Val 500mg BD); Renal: Dose Adjust**  
> **H**SV Encephalitis: **HSV-1, Temporal Lobe, Fever/Confusion/Seizures** — **IV Acyclovir 10mg/kg q8h × 14-21d** (Emergency)  
> **E**xtra-Genital: **Whitlow (Fingers), Keratitis (Dendritic Ulcer - Emergency), Eczema Herpeticum**  
> **T**riggers: **Stress, UV, Fever, Trauma, Menstruation, Immunosuppression**  
> **K**ey Counselling: **Asymptomatic Shedding = Transmission; Suppressive Reduces 50%; Discordant Couple = Suppression + Condoms**  
> **I**n Pregnancy: **Primary = High Risk; Recurrent = Low Risk; Suppression 36w→Delivery**  
> **N**eonatal: **SEM 14d, CNS 21d+6mo Oral, DIS 21d** — **IV Aci 20mg/kg q8h**  
> **M**onitoring: **Suppressive: Reassess 6-12mo (Drug Holiday); Neonatal: Neurodevelopmental Follow-Up**  

---

## 6. 🗺️ Mind Map

```mermaid
mindmap
  root((HSV))
    Types
      HSV-1: Oral→Genital, Low Recurrence
      HSV-2: Genital, High Recurrence, High Shedding
    Clinical
      Primary: Systemic, Severe, 2-4w
      Recurrent: Prodrome, Fewer Lesions, 5-10d
      Extra-Genital: Whitlow, Keratitis, Encephalitis, Eczema Herpeticum
    Diagnosis
      Lesions: NAAT (PCR) 1st Line, Type-Specific
      Asymptomatic: Type-Specific IgG (gG-Based)
      Bedside: Tzanck (Multinucleated Giant Cells)
    Treatment
      Episodic: Aci 400mg 5x/d / Val 1g BD
      Suppressive: Val 500mg OD / Aci 400mg BD
      Indications: ≥6/yr, Discordant, Pregnancy, Psychosocial
      Resistance: TK Mutations → Foscarnet IV
    Pregnancy
      Primary 3rd Tri: HIGH Risk, Cesarean
      Recurrent: Low Risk, Vaginal OK
      Suppression 36w→Delivery
    Neonatal
      SEM: 14d IV Aci
      CNS: 21d IV Aci + 6mo Oral
      DIS: 21d IV Aci
      Prevention: Suppression 36w, Cesarean if Active Lesions
    Resistance
      TK Mutations → Foscarnet
      HIV: Higher Doses, Resistance More Common
```

---

## 7. 📅 Spaced Repetition Tracker

| Review | Date | Score (0–5) | Notes |
|--------|------|-------------|-------|
| Day 1 | | | |
| Day 3 | | | |
| Day 7 | | | |
| Day 14 | | | |
| Day 30 | | | |
| Day 90 | | | |

---

## 8. 📝 Self-Test Scorecard

| Section | Max | Score | % |
|---------|-----|-------|---|
| HSV-1 vs HSV-2 / Primary vs Recurrent | 3 | | |
| Diagnosis (NAAT, Serology, Tzanck) | 3 | | |
| Episodic & Suppressive Therapy | 3 | | |
| Pregnancy & Neonatal HSV | 4 | | |
| Resistance & Immunocompromised | 3 | | |
| Counselling & Partner Management | 2 | | |
| Extra-Genital Manifestations | 2 | | |
| **Total** | **20** | | |

---

## 9. 💬 Exam Answer Modes

| Format | Prompt | Key Points |
|--------|--------|------------|
| **Long Essay** | "Describe the clinical features, diagnosis, and management of genital herpes including special situations in pregnancy and neonate." | HSV-1 vs HSV-2, Primary vs Recurrent, NAAT/Serology, Episodic/Suppressive Tx, Pregnancy Algorithm (Primary=High Risk/Cesarean, Recurrent=Low Risk/Suppression), Neonatal Classification (SEM/CNS/DIS) & Treatment, Resistance (TK Mutations→Foscarnet), Counselling |
| **Short Note** | "Neonatal HSV — classification, diagnosis, and treatment." | **SEM (Skin/Eye/Mouth): IV Acyclovir 20mg/kg q8h × 14d**; **CNS (Encephalitis): IV Acyclovir 20mg/kg q8h × 21d + 6mo Oral Suppression**; **DIS (Disseminated): IV Acyclovir 20mg/kg q8h × 21d**; **PCR CSF = Gold Standard**; **Prevention: Suppression 36w→Delivery, Cesarean if Active Lesions** |
| **Viva** | "25-year-old pregnant woman at 34 weeks with first episode genital herpes. Management?" | **Primary Genital HSV in 3rd Trimester = HIGH Risk**; **Acyclovir 400mg TDS from Diagnosis → Delivery**; **MRI/US for Fetal Assessment**; **Cesarean if Active Lesions/Prodrome at Onset of Labour (Ideally Before Membrane Rupture, ≤4-6h After Rupture)**; **Neonatal IV Acyclovir 20mg/kg q8h × 14-21d Based on Classification**; **Maternal/Neonatal HSV PCR at Birth** |
| **Ward Round** | "3-day-old neonate with vesicular rash, lethargy, seizures. CSF: Lymphocytic pleocytosis, HSV PCR positive. Diagnosis and management?" | **Neonatal HSV — CNS Disease (Encephalitis)**; **IV Acyclovir 20mg/kg IV q8h × 21 Days**; **Supportive Care (Anticonvulsants, Fluids, Respiratory Support)**; **Oral Acyclovir Suppression 300mg/m² TDS × 6 Months Post-IV**; **Neurodevelopmental Follow-Up**; **Maternal HSV Status + Serology** |
| **Last-Night** | "HSV-1/2: Oral/Genital, Recurrence/Shedding. Primary vs Recurrent: Systemic/Severe/2-4w vs Prodrome/Mild/5-10d. NAAT (Lesions), IgG (Asymptomatic). Episodic: Aci 400mg 5x/d (Prim 7-10d, Rec 5d). Suppressive: ≥6/yr, Discordant, Preg 36w→Del, Val 500mg OD. Preg: Primary 3rd Tri=High/Cesarean, Rec=Low/Vaginal OK. Neonatal: SEM 14d, CNS 21d+6mo Oral, DIS 21d. Resist: TK Mut→Foscarnet. Cesarean: Active Lesions/Prodrome at Labour." | Compressed. |

---

## 10. 📌 Summary
- **HSV-1 vs HSV-2**: **HSV-1** (Oral→Increasing Genital, Lower Recurrence); **HSV-2** (Predominantly Genital, Higher Recurrence ~4-5/Year, More Asymptomatic Shedding)
- **Primary Genital Herpes**: **Systemic** (Fever, Bilateral Tender Lymphadenopathy), **Multiple Vesicles/Ulcers**, **2-4 Weeks**
- **Recurrent Genital Herpes**: **Prodrome** (Tingling/Burning), **Fewer/Smaller Lesions**, **No Systemic Symptoms**, **5-10 Days**
- **Diagnosis**: **NAAT (PCR) = 1st Line (Lesions, Type-Specific)**; **Type-Specific IgG (gG-Based) = Asymptomatic/Pregnancy/Partner Screening**
- **Episodic Treatment**: **Acyclovir 400mg 5x Daily × 7-10 Days (Primary), ×5 Days (Recurrent)**; **Valacyclovir 1g BD (Primary), 500mg BD (Recurrent)**
- **Suppressive Therapy**: **Indications: ≥6 Recurrences/Year, Discordant Couple, Pregnancy (36w→Delivery), Psychosocial**; **Valacyclovir 500mg OD / Acyclovir 400mg BD**
- **Pregnancy**: **Primary 3rd Trimester = HIGH Neonatal Risk → Cesarean if Active Lesions at Labour**; **Recurrent = Low Risk → Vaginal Delivery OK if No Lesions**; **Suppression 36w→Delivery Standard**
- **Neonatal HSV**: **SEM (Skin/Eye/Mouth) = 14d IV Acyclovir**; **CNS (Encephalitis) = 21d IV Acyclovir + 6mo Oral Suppression**; **DIS (Disseminated) = 21d IV Acyclovir**
- **Resistance**: **TK Mutations → Acyclovir/Valacyclovir/Famciclovir Cross-Resistance** → **Foscarnet IV**
- **Cesarean Indication**: **Active Genital Lesions at Labour**, **Prodrome at Labour**, **Primary HSV 3rd Trimester/Peripartum**
- **HSV in HIV**: **Higher Doses, Longer Duration, Resistance More Common** — **Valacyclovir 500mg BD for Suppression**

---

## 11. ❓ MCQs (10)

1. **Primary genital herpes — characteristic systemic features?**  
   A. Asymptomatic  B. **Fever, Malaise, Bilateral Tender Inguinal Lymphadenopathy**  C. Only Local Lesions  D. Pruritus Only  
   *Answer: B. Fever, Malaise, Bilateral Tender Inguinal Lymphadenopathy.*

2. **HSV-1 vs HSV-2 genital infection — which has higher recurrence rate?**  
   A. HSV-1  B. **HSV-2**  C. Equal  D. Neither Recur  
   *Answer: B. HSV-2: ~4-5 Recurrences/Year; HSV-1: ~1/Year.*

3. **Neonatal HSV — CNS disease treatment duration?**  
   A. 14 Days  B. **21 Days IV Acyclovir + 6 Months Oral Suppression**  C. 10 Days  D. 7 Days  
   *Answer: B. CNS: IV Acyclovir 20mg/kg q8h × 21 Days + Oral Acyclovir Suppression × 6 Months.*

4. **HSV suppressive therapy — indication?**  
   A. 1 Recurrence/Year  B. **≥6 Recurrences/Year**  C. No Recurrences  D. Only in Pregnancy  
   *Answer: B. ≥6 Episodes/Year (or ≥4 if Severe/Distressing), Discordant Couple, Pregnancy (36w→Delivery), Psychosocial.*

5. **Cesarean section for HSV — when indicated?**  
   A. All HSV+ Women  B. **Active Genital Lesions or Prodrome at Onset of Labour**  C. Recurrent HSV Only  D. Never Indicated  
   *Answer: B. Active Lesions/Prodrome at Labour; Primary HSV 3rd Trimester/Peripartum.*

6. **HSV resistance — mechanism and treatment?**  
   A. DNA Pol Mutation → Foscarnet  B. **TK (Thymidine Kinase) Mutation → Acyclovir/Valacyclovir/Famciclovir Cross-Resistance → Foscarnet IV**  C. Efflux Pump → Cidofovir  D. Beta-Lactamase → Acyclovir  
   *Answer: B. TK Mutation → Cross-Resistance to Acyclovir/Valacyclovir/Famciclovir → Foscarnet IV.*

6. **HSV in pregnancy — primary infection at 36 weeks. Management?**  
   A. Vaginal Delivery  B. **Cesarean (Ideally Before Membrane Rupture) + Maternal/Neonatal IV Acyclovir**  C. Expectant Management  D. Induction of Labor  
   *Answer: B. Primary HSV in 3rd Trimester/Peripartum → Cesarean (Before Rupture/Within 4-6h) + Maternal/Neonatal IV Acyclovir.*

8. **HSV diagnosis — test of choice for active lesions?**  
   A. Type-Specific IgG  B. **NAAT (PCR) — Type-Specific**  C. Tzanck Smear  D. Viral Culture  
   *Answer: B. NAAT (PCR) = 1st Line for Active Lesions (High Sensitivity/Specificity, Type-Specific).*

9. **Neonatal HSV — SEM (Skin, Eye, Mouth) treatment duration?**  
   A. 7 Days  B. **14 Days**  C. 21 Days  D. 28 Days  
   *Answer: B. SEM: IV Acyclovir 20mg/kg q8h × 14 Days.*

10. **HSV resistance — TK mutation cross-resistance pattern?**  
    A. Acyclovir Only  B. **Acyclovir, Valacyclovir, Famciclovir (All)**  C. Foscarnet Only  D. Cidofovir Only  
    *Answer: B. TK Mutation → Cross-Resistance to Acyclovir, Valacyclovir, Famciclovir → Foscarnet IV.*

---

## 12. 📋 SBAs (10)

1. **Pregnant woman at 34 weeks with first-episode genital herpes. Management?**  
   A. Expectant Vaginal Delivery  B. **Acyclovir 400mg TDS → Delivery + Cesarean if Active Lesions at Labour**  C. Cesarean at 36 Weeks  D. No Treatment Needed  
   *Answer: B. Primary HSV 3rd Trimester → Acyclovir 400mg TDS → Delivery + Cesarean if Active Lesions/Prodrome at Labour.*

2. **Neonate with vesicular rash, conjunctivitis, oral ulcers. CSF normal. Classification & treatment?**  
   A. CNS, 21d IV Aci + 6mo Oral  B. **SEM, 14d IV Aci**  C. DIS, 21d IV Aci  D. CNS, 14d IV Aci  
   *Answer: B. SEM (Skin/Eye/Mouth) → IV Acyclovir 20mg/kg q8h × 14 Days.*

3. **Woman with 8 recurrences/year genital HSV-2, distressed. Best management?**  
   A. Episodic Acyclovir Each Episode  B. **Suppressive Valacyclovir 500mg OD**  C. No Treatment  D. Cesarean Section  
   *Answer: B. Suppressive Therapy Indicated (≥6/Year): Valacyclovir 500mg OD or Acyclovir 400mg BD.*

4. **HSV-2 positive woman, 3rd trimester, no lesions. Delivery plan?**  
   A. Elective Cesarean  B. **Vaginal Delivery (Suppressive Acyclovir 400mg TDS from 36w)**  C. Induction at 37 Weeks  D. Cesarean at 38 Weeks  
   *Answer: B. Recurrent HSV, No Lesions → Vaginal Delivery OK + Suppressive Therapy from 36 Weeks.*

5. **Immunocompromised patient with acyclovir-resistant HSV. Treatment?**  
   A. Increase Acyclovir Dose  B. **Foscarnet 40mg/kg IV q8h**  C. Valacyclovir  C. Famciclovir  
   *Answer: B. TK Mutation → Cross-Resistance → Foscarnet 40mg/kg IV q8h (IV Only).*

---

## 13. 🔑 Answer Keys
| MCQs | SBAs |
|------|------|
| 1-B, 2-B, 3-B, 4-B, 5-B, 6-B, 7-B, 8-B, 9-B, 10-B | 1-B, 2-B, 3-B, 4-B, 5-B |

---

## 14. 🔗 Cross-Links
- [[2.1 Chlamydia.md]] — Differential (Urethritis), Co-infection
- [[2.2 Gonorrhoea.md]] — Differential (Urethritis), Co-infection
- [[2.3 Syphilis.md]] — Differential (GUD), Co-infection
- [[5.1-5.8 Syndromic Management.md]] — GUD Algorithm, Neonatal STIs
- [[HIV/AIDS Cross-Reference]] — HSV in HIV, Severe Mucocutaneous, Resistance
- [[9. ELSI]] — Serology Ethics, Disclosure, Stigma
- [[Population & Newborn Screening]] — Antenatal Screening, Neonatal HSV Prevention

---

**Last Updated:** 2026-06-15  
**Next:** Build `3.3 HPV.md`, `3.4 Hepatitis B & C.md`, `3.5 Mpox.md`, `3.6 Other Viral STIs.md`