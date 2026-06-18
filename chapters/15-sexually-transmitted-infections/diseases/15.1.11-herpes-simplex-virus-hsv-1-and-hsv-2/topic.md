**Parent Topic:** [STI MOC](../Sexually%20Transmitted%20Infections%20MOC.md) → [STI Hierarchy](../Davidson%20Chapter%2013%20-%20STI%20Hierarchy.md)  
**Status:** `full-fcps-mrcp-note`  
**Priority:** ⭐⭐⭐ HIGHEST (FCPS/MRCP — Common Viral STI, Recurrence, Neonatal, Serology, Suppressive Therapy)  
**Source:** Davidson 24th Ed Ch 13; WHO/BASHH/CDC Guidelines; FCPS/MRCP Syllabus; NICE NG196

---

## 1. 🎯 Learning Objectives
- [ ] Differentiate **HSV-1 vs HSV-2** epidemiology, clinical features, recurrence patterns
- [ ] Diagnose **Primary vs Recurrent Genital Herpes** and **Extra-genital Manifestations** (Pharyngeal, Rectal, Sacral, Neonatal)
- [ ] Apply **Diagnostic Algorithms** (NAAT, PCR, Culture, Serology, Tzanck) and Interpret Results
- [ ] Apply **Episodic vs Suppressive Antiviral Therapy** (Acyclovir, Valacyclovir, Famciclovir)
- [ ] Manage **HSV in Pregnancy** (Neonatal Prevention, Cesarean Indication, Acyclovir Suppression)
- [ ] Manage **Neonatal HSV** (Disseminated, CNS, SEM — Classification & Treatment)
- [ ] Manage **HSV in Immunocompromised** (Severe Mucocutaneous, Resistance)
- [ ] Answer viva: "Primary vs Recurrent HSV" and "Neonatal HSV Classification" and "Cesarean Indication" and "Suppressive Therapy Indications"

---

## 2. 🧠 Core Concept: HSV Biology & Pathogenesis

```mermaid
flowchart TD
    A[Herpes Simplex Virus] --> B[HSV-1 (Oral/Facial, Genital via Oral Sex)]
    A --> C[HSV-2 (Primarily Genital)]
    B & C --> D[Alpha-Herpesvirus]
    D --> D1[Enveloped, dsDNA, Linear]
    D --> D2[Neurotropic — Latency in Sensory Ganglia]
    D2 --> D2a[HSV-1 → Trigeminal Ganglion (Oral/Facial)]
    D2 --> D2b[HSV-2 → Sacral Ganglion (Genital/Anorectal)]
    D --> D3[Reactivation Triggers]
    D3 --> D3a[Stress, UV, Fever, Menstruation, Immunosuppression, Trauma, Surgery]
    D3 --> D3b[Asymptomatic Shedding (HSV-2 > HSV-1 Genital)]
    D --> D4[Transmission]
    D4 --> D4a[Direct Mucosal/Skin Contact]
    D4 --> D4b[Viral Shedding Without Lesions]
```

---

## 1️⃣ Epidemiology & HSV-1 vs HSV-2

| Feature | **HSV-1** | **HSV-2** |
|---------|-----------|-----------|
| **Primary Site** | **Oral/Facial** (Labialis, Gingivostomatitis) | **Genital** (Genital Herpes) |
| **Genital Infection** | **Increasing** (Oral-Genital Sex) — **Up to 50% New Genital Herpes in Some Regions** | **Traditional Cause** — Still Majority of Recurrent Genital Herpes |
| **Seroprevalence (Global Adults)** | **~67% (3.7 Billion)** | **~13% (491 Million)** |
| **Age of Acquisition** | **Childhood** (Non-Sexual) | **Sexual Debut Onwards** |
| **Recurrence Rate (Genital)** | **Low** (Median 0.5-1/Year) | **High** (Median 4-5/Year Without Suppression) |
| **Asymptomatic Shedding (Genital)** | **Low** (~5-10% Days) | **High** (~20% Days) |
| **Neonatal Herpes Risk** | **Primary Genital HSV-1 = High Risk** | **Primary Genital HSV-2 = High Risk** |
| **Key Populations** | Universal; Higher in Low SES | Women > Men; MSM High; HIV+ High |

> **Trend**: **HSV-1 Increasing as Genital Pathogen** (Oral Sex Practices); **HSV-2 Remains Major Cause of Recurrent Genital Disease**

---

## 2️⃣ Clinical Manifestations

### Primary Genital Herpes (First Episode)

| Feature | Presentation |
|---------|--------------|
| **Incubation** | **2-12 Days** (Average 4 Days) |
| **Systemic** | **Fever, Malaise, Myalgia, Headache, Inguinal Lymphadenopathy (Tender, Bilateral)** |
| **Local** | **Multiple Vesicles on Erythematous Base → Painful Shallow Ulcers** (Coalesce); **Vulva/Vagina/Cervix (F), Penis/Scrotum (M), Perianal** |
| **Duration (Untreated)** | **2-3 Weeks** (Viral Shedding ~12 Days) |
| **Complications** | **Aseptic Meningitis (10-15% Women, 5% Men)**, **Urinary Retention (Sacral Radiculopathy)**, **Proctitis (MSM)**, **Pharyngitis (Oral Sex)** |

### Recurrent Genital Herpes

| Feature | Presentation |
|---------|--------------|
| **Prodrome** | **Tingling, Burning, Itching, Pain** (Often Sacral/Buttock/Thigh) — **Hours to Days Before Lesions** |
| **Lesions** | **Fewer, Smaller, Less Painful** Than Primary; **Vesicles → Ulcers → Crust**; **Unilateral Often** |
| **Duration (Untreated)** | **7-10 Days** (Viral Shedding ~5 Days) |
| **Frequency** | **Median 4-5/Year (HSV-2)**; **0.5-1/Year (HSV-1 Genital)**; **Decreases Over Time** |
| **Asymptomatic Shedding** | **HSV-2: ~20% Days**; **HSV-1 Genital: ~5-10% Days**; **Major Transmission Driver** |

### Extra-Genital Manifestations

| Syndrome | Population | Features |
|----------|------------|----------|
| **Herpetic Whitlow** | Healthcare Workers, Children (Thumb Sucking) | Painful Vesicles on Fingertip, Lymphangitis |
| **Herpes Gladiatorum** | Wrestlers, Contact Sports | Vesicles on Face/Neck/Arms (Skin-to-Skin) |
| **Eczema Herpeticum** | Atopic Dermatitis | **Disseminated Vesicles on Eczematous Skin, Fever, Malaise — EMERGENCY** |
| **HSV Encephalitis** | All (HSV-1 Typical) | Fever, Altered Mental Status, Temporal Lobe Signs — **ACYCLOVIR IV STAT** |
| **Sacral Radiculopathy (Elsberg Syndrome)** | Recurrent Genital | Urinary Retention, Constipation, Sacral Paraesthesia, Areflexia |
| **HSV Pharyngitis** | Oral Sex Exposure | Exudative Pharyngitis, Ulcers, Cervical Lymphadenopathy |

---

## 3️⃣ Diagnostic Algorithms

### Testing Hierarchy

```mermaid
flowchart TD
    A[Clinical Suspicion] --> B{Lesions Present?}
    B -->|Yes| C[NAAT/PCR from Vesicle/Ulcer Base — GOLD STANDARD]
    C --> C1[Sensitivity 95-100%, Specificity >99%]
    C --> C2[Differentiates HSV-1 vs HSV-2]
    C --> C3[Swab: Dacron/Rayon/Polyester — NOT Cotton, NOT Calcium Alginate]
    B -->|No (Healed/Recurrent History)| D[Type-Specific Serology (IgG)]
    D --> D1[HSV-1 IgG vs HSV-2 IgG (gG-1, gG-2 Epitopes)]
    D --> D2[Sensitivity 90-98%, Specificity 95-99%]
    D --> D3[Interpretation: Positive = Past Infection; Seroconversion = Recent]
    D --> D4[Limitations: Window Period 2-12 Weeks; Cannot Determine Site]
    B -->|Research/Atypical| E[Viral Culture (Gold Standard Historical)]
    E --> E1[Lower Sensitivity (70-80%), Slower (2-5 Days), Typing Possible]
    B -->|Point-of-Care| F[POC NAAT (GeneXpert, etc.)]
    F --> F1[30-90 Min, High Sensitivity/Specificity]
    B -->|Obsolete| G[Tzanck Smear (Multinucleate Giant Cells)]
    G --> G1[Low Sensitivity/Specificity, Cannot Type — NOT RECOMMENDED]
```

| Test | Specimen | Sensitivity | Specificity | Turnaround | Use Case |
|------|----------|-------------|-------------|------------|----------|
| **NAAT/PCR (Gold Standard)** | Vesicle Fluid, Ulcer Base Swab, CSF, Blood, Amniotic Fluid | **95-100%** | **>99%** | **2-24h** | **Acute Lesions, Neonatal, CNS, Typing (HSV-1/2)** |
| **Type-Specific Serology (IgG)** | Serum | **90-98%** | **95-99%** | **1-24h** | **Asymptomatic, Partner of Known+, Recurrent History No Lesions, Pregnancy Screening** |
| **Viral Culture** | Vesicle Fluid, Ulcer Base | 70-80% | 100% | 2-5 Days | **Historical Gold Standard; Typing Possible; Low Sensitivity Late** |
| **Direct Fluorescent Antibody (DFA)** | Vesicle/Ulcer Scraping | 80-90% | 95% | Hours | **Lower Sensitivity Than NAAT; Typing Possible** |
| **Tzanck Smear** | Base of Vesicle | 50-70% | 80-90% | Minutes | **Obsolete — Multinucleate Giant Cells (Not HSV-Specific)** |

### Interpretation of Serology

| Result | Interpretation |
|--------|----------------|
| **HSV-1 IgG -, HSV-2 IgG -** | **Susceptible to Both** (No Past Infection) |
| **HSV-1 IgG +, HSV-2 IgG -** | **Past HSV-1 Infection** (Oral/Genital); **Susceptible to HSV-2** |
| **HSV-1 IgG -, HSV-2 IgG +** | **Past HSV-2 Infection** (Genital); **Susceptible to HSV-1** |
| **HSV-1 IgG +, HSV-2 IgG +** | **Past Infection with Both**; **Most Likely Genital HSV-2 + Oral HSV-1** |
| **Seroconversion (IgM or 4-Fold IgG Rise)** | **Recent Infection (2-12 Weeks)** — **Distinguishes Primary from Recurrent** |

---

## 4️⃣ Treatment Regimens

### Episodic Therapy (Primary & Recurrent Episodes)

| Regimen | Primary Episode | Recurrent Episode | Notes |
|---------|-----------------|-------------------|-------|
| **Acyclovir** | 400mg PO **TDS × 10 Days** | 400mg PO **TDS × 5 Days** OR 800mg PO **TDS × 2 Days** | **1st Line**; Low Cost; Renal Adjust if CrCl<10 |
| **Valacyclovir** | 1g PO **BD × 10 Days** | 1g PO **BD × 5 Days** OR 500mg PO **BD × 3 Days** | **Preferred (Better Bioavailability, Less Frequent Dosing)**; Converts to Acyclovir |
| **Famciclovir** | 250mg PO **TDS × 10 Days** | 125mg PO **BD × 5 Days** OR 1g PO **Stat × 2 Days** | Alternative |

> **Start ASAP After Onset (Ideally Within 24h of Prodrome/Lesions)**; **Primary = 10 Days; Recurrent = 5 Days (or Shorter High-Dose Courses)**

### Suppressive Therapy (Chronic Suppression)

| Indication | Regimen | Duration | Review |
|------------|---------|----------|--------|
| **≥6 Recurrences/Year** | **Acyclovir 400mg PO BD** OR **Valacyclovir 500mg PO OD** OR **Famciclovir 250mg PO BD** | **12 Months Initially** | Review Annually; Stop if <Recurrences; Restart if Relapse |
| **Severe/Psycho-social Impact** | Same as Above | 12 Months | Individualised |
| **Partner HIV+/Immunocompromised** | Same as Above | Ongoing | Reduce Transmission Risk |
| **Pregnancy (See Below)** | **Acyclovir 400mg TDS from 36w** | Until Delivery | Neonatal Prevention |

> **Suppressive Therapy Reduces**: **Recurrences by 70-80%**, **Asymptomatic Shedding by 80-90%**, **Transmission to Partner by ~50% (Valacyclovir Data)**

### Severe/Complicated HSV

| Condition | Regimen | Duration |
|-----------|---------|----------|
| **HSV Encephalitis** | **Acyclovir 10mg/kg IV 8-Hourly** (Adjust for Renal) | **14-21 Days** |
| **Neonatal HSV (Disseminated/CNS)** | **Acyclovir 20mg/kg IV 8-Hourly** | **21 Days (Disseminated), 21 Days (CNS)** |
| **Neonatal HSV (SEM)** | **Acyclovir 20mg/kg IV 8-Hourly** | **14 Days** |
| **Eczema Herpeticum** | **Acyclovir 10-15mg/kg IV 8-Hourly** (or PO if Mild) | **7-14 Days** |
| **Immunocompromised (Severe Mucocutaneous)** | **Acyclovir 5-10mg/kg IV 8-Hourly** → Step Down to PO | Until Healed + 7 Days |

### Acyclovir-Resistant HSV (Rare, Immunocompromised)

| Scenario | Definition | Treatment |
|----------|------------|-----------|
| **Suspected Resistance** | **No Clinical Improvement After 7-10 Days IV Acyclovir** | **Foscarnet 40mg/kg IV 8-Hourly** (Nephrotoxic, Monitor Electrolytes) |
| **Confirmed Resistance** | **TK-Negative or TK-Altered Mutants (Phenotypic/Genotypic Testing)** | **Foscarnet IV** OR **Cidofovir IV (Nephrotoxic)**; **Topical Trifluridine/Cidofovir for Localised** |

---

## 5️⃣ HSV in Pregnancy & Neonatal Herpes

### Pregnancy Management

| Scenario | Management |
|----------|------------|
| **Known Genital HSV (Any Type), No Active Lesions at Labour** | **Suppressive Acyclovir 400mg TDS from 36 Weeks** → **Vaginal Delivery Allowed** |
| **Primary Genital HSV in 1st/2nd Trimester** | **Episodic Acyclovir; Suppressive from 36w; Vaginal Delivery if No Active Lesions** |
| **Primary Genital HSV in 3rd Trimester (>28w)** | **High Neonatal Risk (Transmission 50%)**; **Acyclovir IV/PO; Suppressive from 36w**; **C-Section Strongly Considered if <6 Weeks to Delivery**; **Neonatal Prophylaxis/Monitoring** |
| **Recurrent Genital HSV at Labour with Active Lesions/Prodrome** | **Cesarean Section** (Reduces Neonatal Transmission from ~5% to <1%) |
| **Recurrent Genital HSV at Labour, NO Active Lesions** | **Vaginal Delivery** (Low Transmission Risk ~1-3%) |
| **Acyclovir Safety in Pregnancy** | **Category B (US) / No Teratogenicity in Large Registries**; **Valacyclovir/Famciclovir Less Data** |

### Neonatal HSV Classification & Management

```mermaid
flowchart TD
    A[Neonatal HSV] --> B[**SEM (Skin, Eye, Mouth)** — 45%<br/>Vesicles on Skin/Conjunctiva/Oral Mucosa<br/>No CNS/Disseminated Involvement<br/>Best Prognosis if Treated]
    A --> C[**CNS (Central Nervous System)** — 30%<br/>Encephalitis: Seizures, Lethargy, Irritability, CSF Pleocytosis<br/>± Skin Lesions (70% Have)]
    A --> D[**Disseminated** — 25%<br/>Multi-Organ: Hepatitis (↑ALT/AST), Pneumonitis, Coagulopathy (DIC), Adrenal Necrosis<br/>± Skin Lesions (80% Have)<br/>Highest Mortality]
    B & C & D --> E[Treatment: **Acyclovir 20mg/kg IV 8-Hourly**]
    E --> F[SEM: **14 Days**]
    E --> G[CNS: **21 Days** + Repeat CSF PCR at End]
    E --> H[Disseminated: **21 Days** + Supportive (Coagulopathy, Hepatic, Respiratory)]
    F & G & H --> I[**Follow-Up: Oral Acyclovir Suppression 300mg/m² TDS × 6 Months** (Improves Neurodevelopmental Outcomes)]
```

| Classification | Features | Acyclovir IV Duration | Prognosis (Treated) |
|----------------|----------|----------------------|---------------------|
| **SEM (Skin, Eye, Mouth)** | Vesicles on Skin/Conjunctiva/Oral; No CNS/Disseminated | **14 Days** | **Excellent** (Normal Development if Treated) |
| **CNS (Encephalitis)** | Seizures, Lethargy, CSF Pleocytosis, ± Skin Lesions | **21 Days** | **Moderate** (Neurodevelopmental Sequelae Possible; Oral Suppression 6mo Helps) |
| **Disseminated** | Hepatitis, Pneumonitis, DIC, Adrenal Necrosis, ± Skin Lesions | **21 Days** | **Guarded** (Mortality 15-30% Even Treated; Sequelae Common) |

---

## 6️⃣ HSV in Immunocompromised / HIV

| Population | Clinical Features | Management |
|------------|-------------------|------------|
| **HIV (Advanced/CD4<200)** | **Severe, Extensive, Deep, Non-Healing Ulcers**; **Atypical (Necrotic, Verrucous)**; **Prolonged Shedding**; **Resistance More Common** | **IV Acyclovir if Severe**; **Suppressive Therapy Standard**; **Monitor for Resistance (Foscarnet if Resistant)** |
| **Transplant/Steroids/Chemo** | **Severe Mucocutaneous, Disseminated Risk**; **HSV Encephalitis Risk** | **Prophylaxis (Acyclovir/Valacyclovir) During High-Risk Periods**; **Early IV for Severe** |
| **Acute HIV Seroconversion** | **Severe Primary Genital/Perianal Herpes** | **Treat as Primary (10d); Consider ART Initiation** |

---

## 3. ⚡ FCPS/MRCP High-Yield Summary

| Topic | Key Points |
|-------|------------|
| **HSV-1 vs HSV-2** | **HSV-1: Oral/Facial, ↑Genital via Oral Sex, Low Recurrence, Low Shedding**; **HSV-2: Genital, High Recurrence (4-5/yr), High Shedding (~20% Days), Major Transmission Driver** |
| **Primary vs Recurrent** | **Primary: Systemic (Fever, Malaise, Nodes), Multiple Painful Ulcers, 2-3 Weeks**; **Recurrent: Prodrome (Tingling), Fewer/Smaller Lesions, 7-10 Days, Frequency ↓ Over Time** |
| **Diagnosis** | **NAAT/PCR = Gold Standard (Active Lesions)**; **Type-Specific IgG Serology = Past Infection/Asymptomatic**; **Tzanck = Obsolete** |
| **Episodic Tx** | **Primary: Acyclovir 400mg TDS × 10d / Valacyclovir 1g BD × 10d**; **Recurrent: Acyclovir 400mg TDS × 5d / Valacyclovir 1g BD × 5d (or Short High-Dose Courses)** |
| **Suppressive Tx** | **Indication: ≥6 Recurrences/Year OR Severe Psychosocial Impact OR Partner HIV+**; **Acyclovir 400mg BD / Valacyclovir 500mg OD / Famciclovir 250mg BD × 12mo Review** |
| **Neonatal HSV** | **SEM (14d IV Acz), CNS (21d IV Acz), Disseminated (21d IV Acz)**; **All → Oral Suppression 6mo**; **C-Section if Active Lesions/Prodrome at Labour** |
| **Pregnancy** | **Suppressive Acyclovir 400mg TDS from 36w**; **Primary 3rd Trimester = High Risk (50% Trans); C-Section if Active at Labour** |
| **Resistance** | **Rare (Immunocompromised)**; **TK-Negative Mutants**; **Foscarnet IV (Nephrotoxic); Cidofovir IV** |
| **HIV Co-infection** | **More Severe, Frequent, Atypical Ulcers**; **Suppressive Therapy Standard**; **ART Reduces Recurrences** |
| **Viva** | "Primary vs Recurrent HSV", "Neonatal HSV Classification & Tx", "Cesarean Indication", "Suppressive Therapy Indications", "HSV in HIV" |

---

## 4. 🎤 Viva Questions (Expected Answers)

| # | Question | Expected Answer |
|---|----------|-----------------|
| 1 | Differentiate HSV-1 and HSV-2 epidemiology and clinical features. | **HSV-1: Oral/Facial (Childhood Acquisition), ~67% Seroprevalence, Increasing Genital (Oral Sex), Low Genital Recurrence (0.5-1/yr), Low Shedding**; **HSV-2: Genital (Sexual Acquisition), ~13% Seroprevalence, High Genital Recurrence (4-5/yr), High Shedding (~20% Days), Major Transmission Driver** |
| 2 | Primary vs Recurrent Genital Herpes — Clinical Differences? | **Primary: Systemic (Fever, Malaise, Tender Bilateral Inguinal Nodes), Multiple Vesicles→Shallow Ulcers (Confluent), Duration 2-3 Weeks, Viral Shedding ~12d, Complications (Meningitis, Urinary Retention)**; **Recurrent: Prodrome (Tingling/Burning), Fewer/Smaller/Unilateral Lesions, Less Painful/Systemic, Duration 7-10d, Shedding ~5d, Median 4-5/yr (HSV-2)** |
| 3 | Diagnostic test of choice for active genital herpes lesions? | **NAAT/PCR from Vesicle/Ulcer Base — Sensitivity 95-100%, Specificity >99%, Differentiates HSV-1 vs HSV-2, Results 2-24h**; **Serology = Past Infection/Asymptomatic (Not for Acute)** |
| 4 | First-line episodic treatment for Primary Genital Herpes? | **Acyclovir 400mg PO TDS × 10 Days OR Valacyclovir 1g PO BD × 10 Days (Preferred — Better Bioavailability, BD Dosing)**; **Start ASAP (Within 24h of Prodrome/Lesions)** |
| 5 | Indications for Suppressive Therapy? | **≥6 Recurrences/Year**; **Severe Psychosocial Impact**; **Partner HIV+/Immunocompromised (Transmission Reduction)**; **Pregnancy from 36w (Neonatal Prevention)**; **Regimen: Acyclovir 400mg BD / Valacyclovir 500mg OD / Famciclovir 250mg BD × 12mo Review** |
| 6 | Neonatal HSV — Classification and Treatment Durations? | **SEM (Skin/Eye/Mouth): Acyclovir 20mg/kg IV 8hrly × 14d**; **CNS (Encephalitis): Acyclovir 20mg/kg IV 8hrly × 21d + Repeat CSF PCR at End**; **Disseminated: Acyclovir 20mg/kg IV 8hrly × 21d + Supportive**; **All → Oral Acyclovir Suppression 300mg/m² TDS × 6 Months** |
| 7 | Cesarean Section Indication for HSV in Pregnancy? | **Active Genital Lesions OR Prodromal Symptoms at Onset of Labour** → **C-Section Reduces Transmission from ~5% to <1%**; **No Active Lesions at Labour → Vaginal Delivery OK (Risk ~1-3%)**; **Primary 3rd Trimester → Strong Consideration for C-Section if <6 Weeks to Delivery** |
| 8 | Acyclovir safety in Pregnancy? | **Category B (US FDA) / No Teratogenicity in Large Pregnancy Registries (Acyclovir Pregnancy Registry)**; **Valacyclovir/Famciclovir Less Data (Acyclovir Preferred)**; **Standard Doses Safe Throughout Pregnancy** |
| 9 | HSV in HIV — Clinical Features & Management? | **More Severe, Extensive, Deep, Non-Healing Ulcers; Atypical (Necrotic, Verrucous); Prolonged Shedding; Higher Resistance Risk**; **Suppressive Therapy Standard (Reduces Recurrences/Shedding/Transmission); ART Reduces Recurrence Frequency; IV Acyclovir for Severe; Foscarnet if Resistance** |
| 10 | Acyclovir-Resistant HSV — When Suspect & How Treat? | **Suspect: No Improvement After 7-10 Days IV Acyclovir in Immunocompromised**; **Confirm: Phenotypic/Genotypic Resistance Testing (TK Mutations)**; **Treat: Foscarnet 40mg/kg IV 8hrly (Nephrotoxic, Monitor Electrolytes/Cr); Alternative: Cidofovir IV (Nephrotoxic); Topical Trifluridine/Cidofovir for Localised** |

---

## 5. 🧩 Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **"HSV-1 = Oral, HSV-2 = Genital — Never Cross"** | **OUTDATED.** **HSV-1 Now Causes Up to 50% New Genital Herpes (Oral Sex)**; **HSV-2 Can Cause Oral (Oral Sex)**; **Site ≠ Type** |
| **"Serology = Diagnose Acute Herpes"** | **NO.** **Serology = Past Infection (IgG)**; **Acute = NAAT/PCR from Lesion**; **Seroconversion (4-Fold IgG Rise) = Recent (2-12 Weeks)** |
| **"Tzanck Test = HSV Diagnosis"** | **OBSOLETE.** **Multinucleate Giant Cells = Not HSV-Specific (VZV, Pemphigus Also)**; **Low Sensitivity/Specificity; No Typing** |
| **"Suppressive Therapy = Cures HSV"** | **NO.** **Suppresses Recurrences/Shedding/Transmission**; **Virus Remains Latent in Ganglia**; **Stop → Recurrences Return** |
| **"All Pregnant Women with HSV Need C-Section"** | **NO.** **Only if Active Lesions/Prodrome at Labour**; **Suppressive Acyclovir from 36w Allows Vaginal Delivery if No Active Lesions** |
| **"Neonatal HSV = Always Fatal"** | **Treated SEM = Excellent; CNS = Moderate Sequelae; Disseminated = Guarded**; **Early IV Acyclovir + 6mo Oral Suppression Improves Outcomes** |
| **"HSV Shedding = Only With Lesions"** | **MYTH.** **Asymptomatic Shedding: HSV-2 ~20% Days, HSV-1 Genital ~5-10% Days**; **Major Transmission Driver** |
| **"Valacyclovir = Just Expensive Acyclovir"** | **BETTER BIOAVAILABILITY (54% vs 15-20%); BD vs TDS Dosing; Better Adherence; Preferred for Suppression** |
| **"HSV in HIV = Same as Immunocompetent"** | **NO.** **More Severe, Frequent, Atypical, Resistance Risk**; **Suppressive Therapy Standard; ART Helps** |
| **"Foscarnet = 2nd Line for All HSV"** | **ONLY for Confirmed/Strongly Suspected Acyclovir Resistance (TK Mutants)**; **Nephrotoxic, Electrolyte Disturbances; Not for Routine Use** |

> **Mnemonic: HSV MASTER KEY**  
> **H**SV Types: **HSV-1 (Oral/↑Genital via Oral Sex, Low Recur/ Shed)** vs **HSV-2 (Genital, High Recur 4-5/yr, High Shed 20%)**  
> **S**ite ≠ Type: **Both Can Infect Oral/Genital**  
> **V** Primary vs Recurrent: **Primary = Systemic (Fever, Nodes), Multiple Ulcers, 2-3wk**; **Recurrent = Prodrome, Fewer/Unilateral, 7-10d**  
> **M** Diagnosis: **NAAT/PCR = Gold Standard (Active Lesions, Types HSV-1/2)**; **IgG Serology = Past/Asymptomatic**; **Tzanck = Obsolete**  
> **A** Episodic Tx: **Primary: Acz 400mg TDS/Va 1g BD × 10d**; **Recurrent: Acz 400mg TDS/Va 1g BD × 5d (Start <24h Prodrome)**  
> **S** Suppressive Tx: **Indication: ≥6/yr OR Psychosocial OR Partner HIV+ OR Pregnancy 36w+**; **Acz 400mg BD / Va 500mg OD / Fa 250mg BD × 12mo Review**  
> **T** Neonatal: **SEM 14d IV Acz 20mg/kg 8hrly**; **CNS 21d IV Acz + CSF PCR**; **Disseminated 21d IV Acz + Support**  
> **E** Oral Suppression Post-IV: **Acz 300mg/m² TDS × 6mo → Neurodevelopmental Benefit**  
> **R** Pregnancy: **Suppress Acz 400mg TDS from 36w**; **Active Lesions/Prodrome at Labour → C-Section**; **Primary 3rd Tri = High Risk (50% Trans)**  
> **K** Resistance: **Rare (Immunocomp); TK Mutants; Foscarnet 40mg/kg IV 8hrly (Nephrotoxic); Cidofovir Alt**  
> **E** HIV Co-infection: **Severe/Extensive/Atypical/Non-Healing; Suppressive Standard; ART ↓ Recurrence**  
> **Y** Asymptomatic Shedding: **HSV-2 ~20% Days, HSV-1 Genital ~5-10% Days → Major Transmission Driver**  

---

## 6. 🗺️ Mind Map

```mermaid
mindmap
  root((Herpes Simplex Virus))
    Virology
      Alpha-Herpesvirus, dsDNA, Enveloped
      Neurotropic: Latency in Sensory Ganglia
      HSV-1: Trigeminal (Oral)
      HSV-2: Sacral (Genital)
      Reactivation Triggers: Stress, UV, Immunosuppression, Menses
    Epidemiology
      HSV-1: 67% Global, Childhood, ↑ Genital (Oral Sex), Low Recur/Shed
      HSV-2: 13% Global, Sexual, High Recur (4-5/yr), High Shed (20%)
    Clinical
      Primary: Systemic (Fever, Malaise, Nodes), Multiple Vesicles→Ulcers, 2-3wk
      Recurrent: Prodrome (Tingling), Fewer/Smaller/Unilateral, 7-10d
      Extra-Genital: Whitlow, Gladiatorum, Eczema Herpeticum, Encephalitis, Radiculopathy
    Diagnosis
      NAAT/PCR: Gold Standard (Active Lesions, Types HSV-1/2)
      Type-Specific IgG: Past Infection/Asymptomatic
      Culture: Historical, Slower, Lower Sensitivity
      Tzanck: Obsolete (Not HSV-Specific)
    Treatment
      Episodic: Primary Acz 400mg TDS/Va 1g BD ×10d; Recurrent ×5d
      Suppressive: ≥6/yr → Acz 400mg BD/Va 500mg OD/Fa 250mg BD ×12mo
      Severe/Encephalitis: Acz 10mg/kg IV 8hrly ×14-21d
      Resistance: Foscarnet 40mg/kg IV 8hrly (TK Mutants)
    Neonatal
      SEM: 14d IV Acz 20mg/kg
      CNS: 21d IV Acz + CSF PCR
      Disseminated: 21d IV Acz + Support
      All → Oral Acz Suppression 6mo
    Pregnancy
      Suppress Acz 400mg TDS from 36w
      Active Lesions/Prodrome at Labour → C-Section
      Primary 3rd Tri: High Risk (50% Trans), C-Section Considered
    HIV/Immunocompromised
      Severe/Extensive/Atypical/Non-Healing
      Suppressive Standard, ART ↓ Recurrence
      Resistance Risk → Foscarnet if Confirmed
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
| Virology & Epidemiology (HSV-1 vs HSV-2) | 3 | | |
| Clinical (Primary, Recurrent, Extra-Genital) | 4 | | |
| Diagnosis (NAAT, Serology, Culture) | 3 | | |
| Episodic & Suppressive Therapy | 4 | | |
| Neonatal HSV (Classification, Treatment) | 3 | | |
| Pregnancy Management | 2 | | |
| HIV/Immunocompromised | 1 | | |
| Viva Readiness | 1 | | |
| **Total** | **20** | | |

---

## 9. 💬 Exam Answer Modes

| Format | Prompt | Key Points |
|--------|--------|------------|
| **Long Essay** | "Describe the clinical features, diagnosis, and management of Herpes Simplex Virus infection including neonatal herpes." | **Virology: Alpha-Herpesvirus, dsDNA, Neurotropic (Latency: HSV-1 Trigeminal, HSV-2 Sacral); Reactivation Triggers**; **Epidemiology: HSV-1 67% (Oral/Facial, ↑Genital), HSV-2 13% (Genital, High Recurrence 4-5/yr, High Shedding 20% Days)**; **Clinical: Primary (Systemic, Multiple Ulcers, 2-3wk) vs Recurrent (Prodrome, Fewer Lesions, 7-10d); Extra-Genital (Whitlow, Gladiatorum, Eczema Herpeticum, Encephalitis, Radiculopathy)**; **Diagnosis: NAAT/PCR = Gold Standard (Active Lesions, Types); Type-Specific IgG = Past/Asymptomatic; Tzanck Obsolete**; **Treatment: Episodic Primary Acz 400mg TDS/Va 1g BD ×10d, Recurrent ×5d; Suppressive ≥6/yr: Acz 400mg BD/Va 500mg OD/Fa 250mg BD ×12mo; Encephalitis: Acz 10mg/kg IV 8hrly ×14-21d; Resistance: Foscarnet 40mg/kg IV 8hrly**; **Neonatal: SEM 14d IV Acz 20mg/kg, CNS 21d IV Acz+CSF PCR, Disseminated 21d IV Acz+Support → All Oral Acz Suppression 6mo**; **Pregnancy: Suppress Acz 400mg TDS from 36w; Active Lesions/Prodrome at Labour → C-Section; Primary 3rd Tri High Risk**; **HIV: Severe/Atypical, Suppressive Standard, ART ↓ Recurrence** |
| **Short Note** | "Neonatal HSV — Classification and Treatment." | **Transmission: Perinatal (Primary 3rd Tri 50%, Recurrent 1-3%); C-Section if Active Lesions/Prodrome at Labour**; **Classification**: **SEM (Skin/Eye/Mouth, 45%): Vesicles on Skin/Conjunctiva/Oral, No CNS/Disseminated → Acyclovir 20mg/kg IV 8hrly × 14 Days**; **CNS (30%): Encephalitis (Seizures, Lethargy, CSF Pleocytosis) ± Skin Lesions → Acyclovir 20mg/kg IV 8hrly × 21 Days + Repeat CSF PCR at End**; **Disseminated (25%): Hepatitis, Pneumonitis, DIC, Adrenal Necrosis ± Skin Lesions → Acyclovir 20mg/kg IV 8hrly × 21 Days + Supportive**; **All → Oral Acyclovir Suppression 300mg/m² TDS × 6 Months (Neurodevelopmental Benefit)** |
| **Viva** | "Primary vs Recurrent Genital Herpes — Clinical differences and management." | **Primary: Incubation 4d Avg, Systemic (Fever, Malaise, Tender Bilateral Inguinal Nodes), Multiple Coalescing Vesicles→Shallow Ulcers, Duration 2-3 Weeks, Viral Shedding ~12d, Complications (Aseptic Meningitis 10-15%, Urinary Retention)**; **Recurrent: Prodrome (Tingling/Burning Hours-Days Before), Fewer/Smaller/Unilateral Lesions, Less Painful/Systemic, Duration 7-10d, Shedding ~5d, Median 4-5/yr (HSV-2)**; **Tx: Primary 10d, Recurrent 5d (Acyclovir 400mg TDS / Valacyclovir 1g BD)**; **Suppressive if ≥6/yr** |
| **Ward Round** | "28-week Primigravida, Primary Genital HSV (HSV-2 confirmed). Management?" | **Episodic Acyclovir 400mg TDS × 10d Now**; **Suppressive Acyclovir 400mg TDS from 36 Weeks**; **Counsel: High Neonatal Risk (50% Transmission Primary 3rd Trimester); C-Section Strongly Considered if <6 Weeks to Delivery**; **Neonatal: Acyclovir IV if Membranes Ruptured >4h or Fetal Scalp Monitoring; Post-Delivery Neonatal Monitoring/Prophylaxis**; **Partner: Test/Treat if Symptoms, Condoms, Avoid Sex During Outbreaks** |
| **Last-Night** | "HSV-1 Oral/↑Genital (Low Recur/Shed 5-10%), HSV-2 Genital (High Recur 4-5/yr, High Shed 20%). Primary: Systemic+Multiple Ulcers 2-3wk. Recurrent: Prodrome+Fewer Unilateral 7-10d. Dx: NAAT/PCR Gold Standard (Active), IgG Past. Tx: Episodic Primary Acz 400mg TDS/Va 1g BD×10d, Recurrent ×5d. Suppressive: ≥6/yr → Acz 400mg BD/Va 500mg OD×12mo. Neonatal: SEM 14d IV, CNS 21d IV+CSF PCR, Dissem 21d IV→All Oral Suppr 6mo. Preg: Suppr Acz 400mg TDS from 36w, Active Labour→C-Section. HIV: Severe/Atypical, Suppr Standard. Resist: Foscarnet (TK Mutants)." | Compressed. |

---

## 10. 📌 Summary
- **Virology**: **Alpha-Herpesvirus, dsDNA, Enveloped, Neurotropic**; **Latency: HSV-1 Trigeminal (Oral), HSV-2 Sacral (Genital)**; **Reactivation Triggers: Stress, UV, Immunosuppression, Menses**
- **Epidemiology**: **HSV-1: 67% Global, Childhood, ↑Genital via Oral Sex, Low Recurrence (0.5-1/yr), Low Shedding (5-10%)**; **HSV-2: 13% Global, Sexual, High Recurrence (4-5/yr), High Shedding (~20% Days), Major Transmission Driver**
- **Clinical**: **Primary = Systemic (Fever, Malaise, Nodes) + Multiple Painful Ulcers (2-3 Weeks)**; **Recurrent = Prodrome (Tingling) + Fewer/Smaller/Unilateral Lesions (7-10 Days)**; **Extra-Genital: Whitlow, Gladiatorum, Eczema Herpeticum (EMERGENCY), Encephalitis, Radiculopathy**
- **Diagnosis**: **NAAT/PCR = Gold Standard (Active Lesions, Differentiates HSV-1/2)**; **Type-Specific IgG Serology = Past/Asymptomatic Infection**; **Tzanck = Obsolete**
- **Episodic Treatment**: **Primary: Acyclovir 400mg TDS × 10d / Valacyclovir 1g BD × 10d**; **Recurrent: Acyclovir 400mg TDS × 5d / Valacyclovir 1g BD × 5d**; **Start Within 24h of Prodrome/Lesions**
- **Suppressive Therapy**: **Indications: ≥6 Recurrences/Year, Severe Psychosocial Impact, Partner HIV+/Immunocompromised, Pregnancy from 36w**; **Regimens: Acyclovir 400mg BD / Valacyclovir 500mg OD / Famciclovir 250mg BD × 12 Months Review**
- **Neonatal HSV**: **SEM (14d IV), CNS (21d IV + CSF PCR), Disseminated (21d IV + Support)**; **All → Oral Acyclovir Suppression 300mg/m² TDS × 6 Months**
- **Pregnancy**: **Suppressive Acyclovir 400mg TDS from 36w**; **Active Lesions/Prodrome at Labour → Cesarean Section**; **Primary 3rd Trimester = High Neonatal Risk (50% Transmission)**
- **Resistance**: **Rare (Immunocompromised); TK-Negative Mutants**; **Foscarnet 40mg/kg IV 8hrly (Nephrotoxic) / Cidofovir IV**
- **HIV Co-infection**: **More Severe, Extensive, Atypical, Non-Healing Ulcers**; **Suppressive Therapy Standard; ART Reduces Recurrences**

---

## 11. ❓ MCQs (10)

1. **Which type of HSV is the most common cause of recurrent genital herpes?**  
   A. HSV-1  B. **HSV-2**  C. Both Equal  D. Neither  
   *Answer: B. HSV-2 Causes Majority of Recurrent Genital Herpes (Median 4-5/yr vs 0.5-1/yr for HSV-1 Genital).*

1. **Gold Standard Diagnostic Test for Active Genital Herpes Lesions?**  
   A. Tzanck Smear  B. Viral Culture  C. **NAAT/PCR from Lesion Base**  D. Type-Specific IgG Serology  
   *Answer: C. NAAT/PCR — Sensitivity 95-100%, Specificity >99%, Differentiates HSV-1 vs HSV-2, Results 2-24h.*

2. **Episodic Treatment Duration for Primary Genital Herpes?**  
   A. 5 Days  B. **10 Days**  C. 7 Days  D. 14 Days  
   *Answer: B. Primary Episode = 10 Days (Acyclovir 400mg TDS or Valacyclovir 1g BD); Recurrent = 5 Days.*

3. **Indication for Suppressive Antiviral Therapy?**  
   A. 1 Recurrence/Year  B. **≥6 Recurrences/Year**  C. Any Recurrence  D. Only in HIV  
   *Answer: B. ≥6 Recurrences/Year (Or Severe Psychosocial Impact, Partner HIV+, Pregnancy from 36w).*

4. **Neonatal HSV — SEM (Skin, Eye, Mouth) Treatment Duration?**  
   A. 10 Days  B. **14 Days**  C. 21 Days  D. 28 Days  
   *Answer: B. SEM: Acyclovir 20mg/kg IV 8hrly × 14 Days; CNS = 21 Days; Disseminated = 21 Days.*

5. **Cesarean Section Indication for HSV in Pregnancy?**  
   A. Any History of Genital HSV  B. **Active Genital Lesions OR Prodromal Symptoms at Labour**  C. Positive HSV Serology  D. Primary Infection 1st Trimester Only  
   *Answer: B. Active Lesions/Prodrome at Labour → C-Section (Reduces Transmission from ~5% to <1%).*

6. **Acyclovir Safety in Pregnancy?**  
   A. Contraindicated  B. Category X  C. **Category B / No Teratogenicity in Large Registries**  D. Category D  
   *Answer: C. Acyclovir Pregnancy Registry — No Increased Teratogenicity; Category B (US FDA).*

7. **Asymptomatic Viral Shedding — HSV-2 Genital?**  
   A. <1% Days  B. 5-10% Days  C. **~20% Days**  D. >50% Days  
   *Answer: C. HSV-2 Genital Sheds Asymptomatically on ~20% of Days (Major Transmission Driver).*

8. **Acyclovir-Resistant HSV — Treatment of Choice?**  
   A. Valacyclovir High Dose  B. **Foscarnet 40mg/kg IV 8-Hourly**  C. Cidofovir IV  D. Topical Acyclovir  
   *Answer: B. Foscarnet 40mg/kg IV 8hrly (Nephrotoxic, Monitor Electrolytes); Cidofovir Alternative.*

9. **HSV in Advanced HIV (CD4<200) — Typical Features?**  
   A. Mild, Self-Limiting  B. **Severe, Extensive, Deep, Non-Healing, Atypical (Necrotic/Verrucous) Ulcers**  C. No Difference  D. Only Oral Lesions  
   *Answer: B. Severe, Extensive, Deep, Non-Healing, Atypical Ulcers; Prolonged Shedding; Higher Resistance Risk.*

---

## 12. 📋 SBAs (5)

1. **32-week Primigravida with Primary Genital HSV-2 (Confirmed NAAT). Best Management?**  
   A. Acyclovir 400mg TDS × 10d Only  B. **Acyclovir 400mg TDS × 10d + Suppressive Acyclovir 400mg TDS from 36w + C-Section if Active Lesions/Prodrome at Labour**  C. Immediate C-Section  D. No Antiviral Until Labour  
   *Answer: B. Primary 3rd Trimester = High Neonatal Risk (50%); Episodic Tx Now + Suppressive from 36w + C-Section if Active Lesions at Labour.*

2. **Neonate Day 10: Vesicles on Scalp (Fetal Scalp Electrode Site), Conjunctivitis. Mother: Recurrent HSV, No Active Lesions at Vaginal Delivery. Best Management?**  
   A. Observe Only  B. **Acyclovir 20mg/kg IV 8hrly × 14 Days (SEM) + Oral Suppression 6 Months**  C. Acyclovir 20mg/kg IV 8hrly × 21 Days  D. Valacyclovir PO  
   *Answer: B. SEM Neonatal HSV → Acyclovir IV 20mg/kg 8hrly × 14 Days + Oral Suppression 6 Months.*

---

## 13. 🔑 Answer Keys
| MCQs | SBAs |
|------|------|
| 1-B, 2-C, 3-B, 4-B, 5-B, 6-C, 7-C, 8-B, 9-B, 10-B | 1-B, 2-B |

---

## 14. 🔗 Cross-Links
- [[3.2 HSV.md]] — Main Detailed HSV Note (New Format)
- [[Genital Ulcer Disease Syndrome (GUD).md]] — GUD Syndromic Management
- [[5.1-5.8 Syndromic Management.md]] — WHO Algorithm
- [[6. HIV-AIDS Cross-Reference.md]] — HSV in HIV
- [[Contact Tracing and Partner Notification.md]] — PN (60-Day Lookback for HSV)
- [[Sexually Transmitted Infections MOC.md]] — Master Index

---

**Last Updated:** 2026-06-15  
**Version:** Full FCPS/MRCP Template Upgrade