**Parent Topic:** [STI MOC](../Sexually%20Transmitted%20Infections%20MOC.md) → [STI Hierarchy](../Davidson%20Chapter%2013%20-%20STI%20Hierarchy.md)  
**Status:** `full-fcps-mrcp-note`  
**Priority:** ⭐⭐⭐ HIGHEST (FCPS/MRCP — 2022 Global Outbreak, Sexual Transmission, Emerging STI, Vaccination)  
**Source:** Davidson 24th Ed Ch 13; WHO/CDC/UKHSA; FCPS/MRCP Syllabus; NEJM/Lancet 2022-2024

---

## 1. 🎯 Learning Objectives
- [ ] Understand **Mpox virology** (Orthopoxvirus, Clades Ia, Ib, II) and **transmission dynamics**
- [ ] Recognise **clinical presentations** (Classic vs 2022 Outbreak: Genital/Perianal Predominant, Mucosal Lesions)
- [ ] Apply **diagnostic algorithms** (PCR, Lesion Swab, Serology) and interpret results
- [ ] Apply **management strategies** (Supportive, Tecovirimat, Vaccination, Infection Control)
- [ ] Apply **vaccination strategies** (Pre-Exposure, Post-Exposure, Priority Groups)
- [ ] Manage **Mpox in special populations** (HIV, Immunocompromised, Pregnancy, Children)
- [ ] Apply **infection prevention & control** (Isolation, Contact Tracing, PPE)
- [ ] Answer viva: "Mpox Clades" and "2022 Outbreak Clinical Features" and "Tecovirimat Indications" and "Vaccination Strategy"

---

## 2. 🧠 Core Concept: Mpox Virology & Transmission

```mermaid
flowchart TD
    A[Mpox Virus (MPXV)] --> B[Orthopoxvirus, dsDNA]
    B --> C[Clades]
    C --> C1[**Clade I (Congo Basin)** — Higher Severity, CFR ~10%]
    C --> C2[**Clade II (West African)** — Lower Severity, CFR ~1-3%]
    C2 --> C2a[**Clade IIa** — Endemic West Africa]
    C2 --> C2b[**Clade IIb** — **2022 Global Outbreak** (B.1 Lineage)]
    B --> D[Transmission]
    D --> D1[Close Contact (Skin-to-Skin, Lesion Fluid)]
    D --> D2[Respiratory Droplets (Prolonged Face-to-Face)]
    D --> D3[Fomites (Bedding, Towels, Sex Toys)]
    D --> D4[**Sexual Contact** (Genital/Perianal Mucosa — **2022 Outbreak Driver**)]
    D --> D5[Vertical (Mother→Fetus), Animal→Human (Zoonotic)]
    B --> E[Incubation: 5-21 Days (Median 6-13 Days)]
```

---

## 1️⃣ Mpox Clades — Epidemiology & Severity

| Clade | Geographic Origin | Case Fatality Rate (CFR) | Clinical Severity | 2022 Outbreak |
|-------|-------------------|--------------------------|-------------------|---------------|
| **Clade I (Congo Basin)** | Central Africa (DRC) | **~10%** (Up to 15% in Children) | **Severe** (More Complications, Sepsis, Encephalitis) | Not in 2022 Global Outbreak |
| **Clade IIa (West African Endemic)** | West Africa | **~1-3%** | Moderate | Endemic, Not 2022 Outbreak |
| **Clade IIb (B.1 Lineage)** | **Global (2022 Outbreak)** | **<1%** (0.1-0.3% in Non-Endemic) | **Milder** (Less Systemic, Genital/Perianal Predominant) | **2022-2023 Global Outbreak** (MSM Networks) |

> **Key**: **2022 Outbreak = Clade IIb (B.1 Lineage)**; **>95% Cases in MSM**; **Genital/Perianal Lesions Predominant**; **Lower CFR**

---

## 2️⃣ Clinical Presentation — 2022 Outbreak vs Classic

### Classic Mpox (Clade I/IIa Endemic)
| Feature | Detail |
|---------|--------|
| **Prodrome (1-5 Days)** | Fever, Headache, Myalgia, Backache, **Marked Lymphadenopathy** (Generalised) |
| **Rash** | **Centrifugal** (Face → Extremities → Palms/Soles), **Synchronous** (Same Stage) |
| **Lesion Evolution** | **Macule → Papule → Vesicle → Pustule → Crust → Scab** (2-4 Weeks) |
| **Distribution** | **Face (95%), Palms/Soles (75%), Oral Mucosa (70%), Genital (30%)** |
| **Complications** | Secondary Infection, Sepsis, Encephalitis, Corneal Scarring, Pneumonia |

### 2022 Outbreak (Clade IIb) — Atypical Presentation
| Feature | Detail |
|---------|--------|
| **Prodrome** | **Often Absent or Mild** (Fever in ~50%, Lymphadenopathy Localised) |
| **Rash** | **Anogenital Predominant** (Genital, Perianal, Perioral), **Often Single/Scattered Lesions** |
| **Lesion Evolution** | **Asynchronous** (Different Stages Simultaneously), **Pseudopustules** (Umbilicated) |
| **Distribution** | **Genital (60-70%), Perianal (40-50%), Perioral/Oral (20-30%), Face/Extremities (<20%)** |
| **Mucosal Lesions** | **Proctitis** (Rectal Pain, Bleeding, Tenesmus), **Pharyngitis**, **Urethritis**, **Conjunctivitis** |
| **Systemic Symptoms** | **Milder** (Fever <50%, Lymphadenopathy Localised to Draining Nodes) |
| **Atypical Presentations** | **Single Genital Lesion** (Mimics HSV/Syphilis), **Tonsillitis**, **Proctitis Only**, **Penile Swelling** |

> **Key**: **2022 Outbreak = Genital/Perianal Predominant, Often Mild Prodrome, Asynchronous Lesions, MSM Networks**

---

## 3️⃣ Diagnosis — Algorithms & Interpretation

### Case Definition (WHO/ICMR)
| Category | Criteria |
|---------|----------|
| **Suspected** | Acute Rash (Acute Onset) + **Epidemiological Link** (Contact/Travel) + **No Other Explanation** |
| **Probable** | Suspected + **Orthopoxvirus Positive** (PCR Non-Variola) **OR** Epidemiological Link + Compatible Rash |
| **Confirmed** | **MPXV DNA Positive by PCR** (Lesion Swab, Crust, Blood) |

### Diagnostic Algorithm
```mermaid
flowchart TD
    A[Suspected Mpox] --> B{Lesions Present?}
    B -->|Yes| C[Lesion Swab (Vesicle/Pustule/Crust)<br/>→ MPXV PCR (Orthopoxvirus/MPXV Specific)]
    B -->|No (Screening/Asymptomatic)| D[Serology (IgM/IgG)<br/>Not for Acute Diagnosis]
    C --> E{PCR Result}
    E -->|Positive| F[Confirmed Mpox<br/>→ Type Clade (IIb vs I) if Available]
    E -->|Negative| G[Consider Alternative<br/>(HSV, Syphilis, VZV, Molluscum, Chancroid)]
    F --> H[Isolate, Contact Trace, Notify]
```

### Diagnostic Tests

| Test | Sample | Timing | Utility |
|------|--------|--------|---------|
| **MPXV PCR (Real-Time)** | **Lesion Swab (Vesicle/Pustule Fluid, Crust, Scab)** | **Acute (Day 1-21)** | **Gold Standard** (Type-Specific, Clade Differentiation) |
| **Orthopoxvirus PCR** | Lesion Swab | Acute | **Screening** (If MPXV-Specific Unavailable) |
| **Viral Culture** | Lesion Fluid | Acute | **Reference Lab Only** (BSL-3) |
| **Serology (IgM/IgG)** | Blood | **Convalescent (Day 7-14+)** | **Retrospective, Surveillance**; **Cross-Reactive with Vaccinia/Smallpox Vaccine** |
| **Electron Microscopy** | Lesion Fluid | Acute | **Research/Reference** (Brick-Shaped Virions) |

> **Key**: **Lesion Swab PCR = Gold Standard**; **Swab Base of Lesion (Unroof Vesicle/Pustule)**; **Multiple Sites if Atypical**

---

## 4️⃣ Management — Supportive & Antiviral

### General Principles
| Principle | Detail |
|-----------|--------|
| **Isolation** | **Until All Lesions Crusted, Scabs Fallen Off, Fresh Skin Formed** (~2-4 Weeks) |
| **Supportive Care** | Analgesia (Topical Lidocaine, Oral NSAIDs/Opioids), Hydration, Wound Care (Antiseptic, Prevent Secondary Infection), Antipyretics |
| **Psychosocial Support** | Stigma Reduction, Mental Health, Sexual Health Counselling |

### Antiviral Therapy — Tecovirimat (First-Line)

| Indication | Detail |
|------------|--------|
| **Severe Disease** | Extensive Lesions (>100), Sepsis, Encephalitis, Ocular Involvement, Immunocompromised |
| **High-Risk Groups** | **HIV (CD4<200), Uncontrolled HIV, Immunosuppression, Pregnancy, Children <8y, Atopic Dermatitis/Eczema, Comorbidities** |
| **Complications** | Proctitis (Severe Pain/Rectal Bleeding), Pharyngitis (Dysphagia), Urethritis (Retention), Secondary Bacterial Infection |

| Drug | Dose (Adult) | Duration | Route | Key Notes |
|------|--------------|----------|-------|-----------|
| **Tecovirimat (TPOXX)** | **600mg (3×200mg) BD** | **14 Days** | **Oral (Preferred)** | **With High-Fat Meal (↑ Absorption)**; **IV Formulation Available** |
| **Tecovirimat IV** | **200mg q12h** | 14 Days | IV | If Oral Not Tolerated/Malabsorption |
| **Cidofovir** | 5mg/kg IV Weekly | 2-3 Doses | IV | **Nephrotoxic** (Probenecid + Hydration); **Second-Line** |
| **Brincidofovir** | 200mg Weekly × 3 | Oral | Oral | **GI Toxicity**; **Second-Line** |

> **Tecovirimat Mechanism**: **VP37 Envelope Protein Inhibitor** → Blocks Viral Egress → **Orthopoxvirus Specific**

### Tecovirimat — Monitoring & Resistance
| Monitoring | Frequency |
|------------|-----------|
| **Liver Function (ALT/AST)** | Baseline, Weekly |
| **Renal Function** | Baseline, Weekly (If IV) |
| **Clinical Response** | Daily (Lesion Progression, Pain, Systemic Signs) |
| **Resistance** | **VP37 Mutations** (Emerging) — **Monitor if Clinical Failure** |

---

## 5️⃣ Vaccination — Pre-Exposure (PrEP) & Post-Exposure (PEP)

### Vaccines Available

| Vaccine | Type | Doses | Key Features |
|---------|------|-------|--------------|
| **MVA-BN (JYNNEOS / IMVANEX / IMVAMUNE)** | **Modified Vaccinia Ankara (Non-Replicating)** | **2 Doses (28 Days Apart)** | **Preferred** (Safe in Immunocompromised, HIV, Pregnancy); **No Visible "Take"** |
| **ACAM2000** | **Live Replicating Vaccinia** | **1 Dose (Percutaneous)** | **Contraindicated in Immunocompromised, HIV, Pregnancy, Eczema**; **"Take" (Pustule) Forms** |
| **LC16m8** | **Attenuated Vaccinia (LC16)** | 1 Dose | Japan, Limited Global Use |

> **MVA-BN = Preferred for All Groups** (Including Immunocompromised, HIV, Pregnancy)

### Pre-Exposure Prophylaxis (PrEP) — Priority Groups
| Priority | Groups |
|----------|--------|
| **Highest** | **MSM (High Risk: Multiple Partners, PrEP Users, Recent STIs)**, **Sex Workers**, **Lab Workers (Orthopoxvirus)**, **Healthcare Workers (High-Risk Exposure)** |
| **High** | **Immunocompromised (HIV CD4<200)**, **Close Contacts of Cases** |
| **Consider** | **Healthcare Workers (ID/EM/ Sexual Health)**, **Travelers to Endemic Areas** |

### Post-Exposure Prophylaxis (PEP)
| Timing | Action |
|--------|--------|
| **≤4 Days Post-Exposure** | **Vaccine (MVA-BN) — Ideally Within 4 Days, Up to 14 Days** (May Modify Disease) |
| **>4 to ≤14 Days** | **Vaccine (May Reduce Severity)** |
| **Co-Administration** | **Vaccine + Tecovirimat** (If High-Risk Exposure + High-Risk Individual) |

| Exposure Risk | PEP Recommendation |
|---------------|-------------------|
| **High (Unprotected Sex with Case, Household Contact, Needlestick)** | **MVA-BN 2 Doses (Day 0, Day 28) + Tecovirimat (If High-Risk Individual)** |
| **Intermediate (Protected Sex with Condom Break, Brief Contact)** | **MVA-BN 2 Doses (Day 0, Day 28)** |
| **Low (Brief Casual Contact, PPE Used)** | **Monitor (No PEP)** |

> **PEP Window**: **Ideally ≤4 Days (Up to 14 Days for Vaccine)**; **Tecovirimat Added for High-Risk Individuals (HIV CD4<200, Immunocompromised, Pregnancy, Severe Disease Risk)**

---

## 6️⃣ Mpox in Special Populations

### HIV Co-infection
| Aspect | Management |
|--------|------------|
| **Severity** | **CD4<200: Severe, Prolonged, Disseminated, Higher Mortality** |
| **Antiretroviral Therapy** | **Continue/Initiate ART** (Immune Reconstitution Critical) |
| **Antiviral** | **Tecovirimat Strongly Indicated (CD4<200)**; **Drug Interactions (Tecovirimat ↔ ART — Check Liverpool Database)** |
| **ART & Tecovirimat** | **Tecovirimat ↔ CYP3A4 Inducers/Inhibitors** (Rifampicin, Efavirenz, Boosted PIs) — **Dose Adjust/Monitor** |
| **Vaccination** | **MVA-BN Safe (2 Doses)** — **Prioritise** |

### Pregnancy & Breastfeeding
| Aspect | Management |
|--------|------------|
| **Severity** | **Potentially Severe (Vertical Transmission Risk, Fetal Loss)** |
| **Vertical Transmission** | **Possible (Placental, Perinatal, Postnatal)** — **Fetal Loss, Preterm, Neonatal Mpox** |
| **Antiviral** | **Tecovirimat Safe (Animal Data)** — **Indicated if Severe/High-Risk** |
| **Vaccination** | **MVA-BN Safe** (Non-Replicating) — **Can Be Given in Pregnancy** |
| **Delivery** | **Cesarean if Active Genital Lesions** (Reduce Neonatal Exposure); **Vaginal if No Lesions** |
| **Breastfeeding** | **Avoid if Active Lesions on Breast**; **Express/Discard Milk if Lesions Elsewhere** |

### Children
| Aspect | Management |
|--------|------------|
| **Severity** | **Higher CFR (Clade I), Complications (Encephalitis, Sepsis)** |
| **Antiviral** | **Tecovirimat Weight-Based Dosing** (Oral Suspension Available) |
| **Vaccination** | **MVA-BN (Off-Label <18y, Use with Caution)**; **ACAM2000 Contraindicated** |

---

## 6️⃣ Infection Prevention & Control (IPC)

### Isolation Precautions
| Setting | Precautions |
|---------|-------------|
| **Hospital** | **Contact + Droplet Precautions** (Private Room, Negative Pressure if Aerosol-Generating Procedures) |
| **Community** | **Self-Isolation at Home** (Separate Room, Own Bathroom, No Visitors, Separate Utensils/Bedding) |
| **Duration** | **Until All Lesions Crusted, Scabs Fallen Off, Fresh Skin Formed** (~2-4 Weeks) |

### Contact Tracing & Monitoring
| Contact Category | Monitoring | PEP |
|----------------|------------|-----|
| **High-Risk (Sexual, Household, Unprotected Contact)** | **21-Day Monitoring** (Daily Symptom Check) | **MVA-BN PEP (≤4 Days Ideal, Up to 14 Days)** |
| **Intermediate (Healthcare with PPE Breach, Brief Contact)** | **21-Day Self-Monitoring** | **Vaccine if High-Risk Individual** |
| **Low (Casual, PPE Intact)** | **Self-Monitoring 21 Days** | None |

### Environmental Decontamination
| Surface | Agent |
|--------|-------|
| **Non-Porous** | **0.1% Sodium Hypochlorite (Bleach), 70% Ethanol, EPA-Registered Virucides** |
| **Porous (Bedding, Clothing)** | **Hot Wash (≥60°C) + Detergent**, **Steam Cleaning** |
| **Waste** | **Category B Infectious Waste** (Double Bag, Incinerate/Autoclave) |

---

## 6️⃣ Complications & Sequelae

| Complication | Frequency | Management |
|--------------|-----------|------------|
| **Secondary Bacterial Infection** | Common | Topical/Systemic Antibiotics (Based on Culture) |
| **Proctitis** | 20-30% (MSM) | **Tecovirimat**, Analgesia, Stool Softeners, Topical Steroids (If Inflammatory) |
| **Pharyngitis/Esophagitis** | 10-20% | Analgesia, Hydration, Tecovirimat if Severe |
| **Urethritis** | 5-10% | Analgesia, Catheterisation if Retention |
| **Ocular Mpox** | Rare | **Ophthalmology Referral**, Tecovirimat, Topical Antivirals (Trifluridine) |
| **Encephalitis** | Rare (<1%) | **ICU**, Tecovirimat IV, Supportive |
| **Sepsis** | Rare | **ICU**, Broad-Spectrum Antibiotics, Tecovirimat |
| **Scarring/Pigmentation** | Common | Reassurance, Sunscreen, Dermatology Referral |

---

## 3. ⚡ FCPS/MRCP High-Yield Summary

| Topic | Key Points |
|-------|------------|
| **Clades** | **Clade I (Congo) = Severe, CFR ~10%; Clade IIb (2022 Outbreak) = Milder, CFR <1%** |
| **Transmission** | **Close Contact (Skin-to-Skin, Sexual), Respiratory, Fomites**; **2022 Outbreak = MSM Networks, Sexual Transmission Predominant** |
| **Clinical (2022 Outbreak)** | **Genital/Perianal Predominant**, **Often Mild/No Prodrome**, **Asynchronous Lesions**, **Proctitis/Pharyngitis/Urethritis Common** |
| **Diagnosis** | **Lesion Swab PCR (Gold Standard)**; **Swab Base of Lesion (Unroof Vesicle/Pustule)** |
| **Isolation** | **Until All Crusted, Scabs Fallen, Fresh Skin (2-4 Weeks)** |
| **Antiviral** | **Tecovirimat 600mg BD × 14d (Oral)** — **Severe Disease, High-Risk (HIV CD4<200, Immunocompromised, Pregnancy, Children)** |
| **Vaccine** | **MVA-BN (JYNNEOS) 2 Doses (28d Apart)** — **Safe in Immunocompromised, HIV, Pregnancy** |
| **PrEP** | **MSM (High Risk), Sex Workers, Lab/HCW** |
| **PEP** | **MVA-BN ≤4 Days (Up to 14 Days) + Tecovirimat if High-Risk** |
| **HIV Co-infection** | **CD4<200 = Severe; Tecovirimat Indicated; ART Continue; Drug Interactions** |
| **Pregnancy** | **MVA-BN Safe; Tecovirimat if Severe; Cesarean if Genital Lesions** |
| **IPC** | **Contact + Droplet; Isolate Until All Crusted/Scabs Fallen (2-4w); Contact Trace 21d** |

---

## 4. 🎤 Viva Questions (Expected Answers)

| # | Question | Expected Answer |
|---|----------|-----------------|
| 1 | Mpox clades — which caused 2022 global outbreak? | **Clade IIb (B.1 Lineage)** — West African Clade, Milder, CFR <1%, MSM Sexual Networks |
| 2 | 2022 outbreak clinical features vs classic mpox? | **Genital/Perianal Predominant**, **Mild/No Prodrome**, **Asynchronous Lesions**, **Proctitis/Pharyngitis/Urethritis Common**, **Often Single/Scattered Lesions** |
| 3 | Mpox diagnosis — gold standard test? | **Lesion Swab PCR (MPXV Specific)** — Swab Base of Vesicle/Pustule/Crust |
| 4 | Tecovirimat — indications, dose, duration? | **Severe Disease, High-Risk (HIV CD4<200, Immunocompromised, Pregnancy, Children, Complications)**; **600mg BD Oral × 14 Days (With Fatty Meal)** |
| 5. Mpox vaccination — which vaccine, schedule, priority groups? | **MVA-BN (JYNNEOS) 2 Doses (28 Days Apart)**; **Priority: MSM (High Risk), Sex Workers, Lab/HCW, Immunocompromised (HIV CD4<200)** |
| 6. Mpox PEP — timing and regimen? | **MVA-BN Ideally Within 4 Days (Up to 14 Days) 2 Doses (Day 0, 28)**; **Add Tecovirimat if High-Risk Individual (HIV CD4<200, Immunocompromised, Pregnancy)** |
| 7. Mpox in HIV — severity and management? | **CD4<200 = Severe, Prolonged, Disseminated**; **Tecovirimat Indicated**; **Continue ART**; **Drug Interactions (Tecovirimat ↔ CYP3A4)**; **MVA-BN Safe (2 Doses)** |
| 8. Mpox in pregnancy — management? | **MVA-BN Safe (Non-Replicating)**; **Tecovirimat if Severe/High-Risk**; **Cesarean if Active Genital Lesions**; **Breastfeeding Avoid if Breast Lesions** |
| 9. Mpox isolation duration? | **Until All Lesions Crusted, Scabs Fallen Off, Fresh Skin Formed (2-4 Weeks)** |
| 10. Mpox contact tracing — high-risk contacts PEP? | **MVA-BN 2 Doses (Day 0, 28) Ideally Within 4 Days (Up to 14 Days)**; **Add Tecovirimat if High-Risk Individual** |

---

## 5. 🧩 Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **"Mpox = Smallpox"** | **NO.** **Mpox = Orthopoxvirus (Related to Smallpox/Variola)**, **Lower CFR, Less Transmissible, Different Clades** |
| **"Mpox = Only MSM Disease"** | **NO.** **MSM = 2022 Outbreak Driver (Sexual Networks)**; **Can Spread to Anyone via Close Contact (Household, Healthcare, Community)** |
| **"Mpox = Only Genital Lesions"** | **NO.** **Classic = Face/Extremities/Palms/Soles**; **2022 Outbreak = Genital/Perianal Predominant (But Can Be Anywhere)** |
| **"Tecovirimat = For All Mpox Cases"** | **NO.** **Indicated for Severe/High-Risk Only**; **Mild Cases = Supportive Care Only** |
| **"Mpox Vaccine = ACAM2000 (Smallpox Vaccine)"** | **NO.** **MVA-BN (JYNNEOS) = Preferred (Non-Replicating, Safe in Immunocompromised/Pregnancy)**; **ACAM2000 = Live, Contraindicated in Immunocompromised** |
| **"Mpox = Only Spread by Sex"** | **NO.** **Close Contact (Skin-to-Skin, Household, Fomites, Respiratory Droplets)**; **Sexual = Major Driver in 2022 Outbreak** |
| **"Mpox = Only in Africa"** | **NO.** **2022 Outbreak = Global (110+ Countries)**; **Endemic in Central/West Africa (Clade I/IIa)** |
| **"Mpox = No Vaccine"** | **NO.** **MVA-BN (JYNNEOS/IMVANEX) = Licensed, 2 Doses (28d Apart), Safe in Immunocompromised/Pregnancy** |
| **"Mpox = Always Severe"** | **NO.** **2022 Outbreak (Clade IIb) = Milder, CFR <1%**; **Clade I (Congo) = Severe, CFR ~10%** |
| **"Mpox = No Antiviral"** | **NO.** **Tecovirimat (TPOXX) = Licensed, Oral/IV, 14 Days, VP37 Inhibitor** |

> **Mnemonic: MPOX OUTBREAK MASTER**  
> **M**pox Clades: **I (Congo, Severe, CFR 10%); IIa (West Africa Endemic); IIb (2022 Global, Mild, CFR <1%)**  
> **P**resentation 2022: **Genital/Perianal Predominant, Mild/No Prodrome, Asynchronous Lesions, Proctitis/Pharyngitis/Urethritis**  
> **O**rthopoxvirus: **dsDNA, Brick-Shaped, Related to Smallpox/Vaccinia**  
> **X** Transmission: **Close Contact (Skin, Sexual, Respiratory, Fomites), 2022 = MSM Sexual Networks**  
> **O**utbreak 2022: **Clade IIb (B.1), MSM Networks, >95% MSM, Genital/Perianal Predominant**  
> **B**iopsy/Diagnosis: **Lesion Swab PCR (Gold Standard), Swab Base of Lesion**  
> **R**eservoir: **Rodents (Suspected), Primates (Spillover)**  
> **E**pidemiology: **2022-23 Global: 87k+ Cases, 110+ Countries, >95% MSM, CFR <1%**  
> **A**ntiviral: **Tecovirimat 600mg BD × 14d (Oral, Fatty Meal)** — **VP37 Inhibitor**  
> **I**ndications Tecovirimat: **Severe, High-Risk (HIV CD4<200, Immunocomp, Pregnancy, Children, Complications)**  
> **V**accine: **MVA-BN (JYNNEOS) 2 Doses (Day 0, 28), Non-Replicating, Safe in HIV/Pregnancy**  
> **A**CM2000: **Live Replicating, Contraindicated in Immunocompromised/Pregnancy**  
> **L** PR/PEP: **PrEP (MSM High Risk, Lab/HCW); PEP (MVA-BN ≤4d, Up to 14d + Tecovirimat if High-Risk)**  
> **I**solation: **Contact + Droplet, Until All Crusted/Scabs Fallen/Fresh Skin (2-4w)**  
> **C**omplications: **Proctitis, Pharyngitis, Urethritis, Ocular, Encephalitis, Sepsis, Scarring**  
> **H**IV Co-infection: **CD4<200 = Severe; Tecovirimat Indicated; ART Continue; MVA-BN Safe 2 Doses**  
> **P**regnancy: **MVA-BN Safe; Tecovirimat if Severe; Cesarean if Genital Lesions**  
> **O**cular: **Ophthalmology Referral, Tecovirimat, Topical Trifluridine**  
> **U**rethritis/Proctitis: **Common in 2022 Outbreak, Tecovirimat + Symptomatic**  
> **T**ecovirimat Resistance: **VP37 Mutations (Emerging), Monitor Clinical Failure**  
> **B**leach/Decon: **0.1% Hypochlorite, 70% Ethanol, Hot Wash (≥60°C)**  

---

## 6. 🗺️ Mind Map

```mermaid
mindmap
  root((Mpox))
    Clades
      I: Congo, Severe, CFR 10%
      IIa: West Africa Endemic
      IIb: 2022 Global, Mild, CFR <1%
    Transmission
      Close Contact (Skin, Sexual, Respiratory, Fomites)
      2022: MSM Sexual Networks
    Clinical
      Classic: Centrifugal, Sync, Prodrome
      2022 Outbreak: Genital/Perianal Predominant, Mild/No Prodrome, Async, Proctitis/Pharyngitis
    Diagnosis
      Lesion Swab PCR (Gold Standard)
      Swab Base of Lesion
    Treatment
      Supportive Analgesia, Hydration, Wound Care
      Tecovirimat 600mg BD x14d (Severe/High-Risk)
      Cidofovir/Brincidofovir (2nd Line)
    Vaccine
      MVA-BN (JYNNEOS) 2 Doses (28d)
      Safe in HIV, Pregnancy, Immunocompromised
      ACAM2000: Live, Contraindicated Immunocomp
    PrEP/PEP
      PrEP: MSM High Risk, Sex Workers, Lab/HCW
      PEP: MVA-BN ≤4d (Up to 14d) + Tecovirimat if High-Risk
    Special Pops
      HIV: CD4<200 Severe, Tecovirimat, ART Continue, MVA-BN Safe
      Pregnancy: MVA-BN Safe, Tecovirimat if Severe, Cesarean if Lesions
      Children: Higher Severity, Tecovirimat Weight-Based
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
| Virology, Clades, Epidemiology | 3 | | |
| Clinical Presentation (Classic vs 2022) | 3 | | |
| Diagnosis & Testing | 2 | | |
| Management (Supportive, Tecovirimat, Vaccine) | 4 | | |
| Special Populations (HIV, Pregnancy, Children) | 3 | | |
| IPC, Isolation, Contact Tracing, PEP | 3 | | |
| Complications & Sequelae | 2 | | |
| **Total** | **20** | | |

---

## 9. 💬 Exam Answer Modes

| Format | Prompt | Key Points |
|--------|--------|------------|
| **Long Essay** | "Describe the clinical features, diagnosis, and management of Mpox with reference to the 2022 global outbreak." | Clades (I/IIa/IIb), 2022 Outbreak (Clade IIb, MSM, Genital/Perianal, Mild Prodrome, Async Lesions), Diagnosis (Lesion PCR), Management (Supportive, Tecovirimat for Severe/High-Risk), Vaccination (MVA-BN 2 Doses, PrEP/PEP), IPC (Isolation, Contact Tracing), Special Pops (HIV, Pregnancy) |
| **Short Note** | "Tecovirimat — indications, dosage, and mechanism of action." | **VP37 Envelope Protein Inhibitor** → Blocks Viral Egress; **Indications: Severe Disease, High-Risk (HIV CD4<200, Immunocompromised, Pregnancy, Children, Complications)**; **600mg BD Oral × 14 Days (With Fatty Meal)**; IV Available; Resistance: VP37 Mutations |
| **Viva** | "30-year-old MSM with 5-day history of painful perianal lesions, no fever. PCR positive for Mpox. Management?" | **Mild Mpox (Clade IIb Typical)** → **Supportive Care** (Analgesia, Hydration, Wound Care, Isolation Until Crusted); **Monitor for Complications (Proctitis, Secondary Infection)**; **Contact Tracing (PEP for High-Risk Contacts: MVA-BN ≤4d)**; **Tecovirimat NOT Indicated (Not Severe/High-Risk)**; **HIV Test, STI Screen** |
| **Ward Round** | "HIV+ patient (CD4 150) with Mpox, extensive lesions, rectal pain, bleeding. Management?" | **Severe Mpox in HIV (CD4<200) = High-Risk** → **Tecovirimat 600mg BD Oral × 14 Days (With Fatty Meal)** + **Supportive Care**; **Continue ART (Check Tecovirimat ↔ ART Interactions — CYP3A4)**; **Monitor Liver/Renal Function**; **Isolation Until All Crusted**; **Contact Tracing + PEP for High-Risk Contacts**; **MVA-BN Vaccination (2 Doses) if Not Vaccinated** |
| **Last-Night** | "Clades: I (Congo, Severe), IIa (Endemic), IIb (2022 Global, Mild). 2022: Genital/Perianal, Mild/No Prodrome, Async, Proctitis. Dx: Lesion PCR. Mgmt: Supportive, Tecovirimat 600mg BD x14d (Severe/High-Risk: HIV CD4<200, Preg, Kids, Comp). Vaccine: MVA-BN 2 doses (28d). PrEP: MSM High Risk. PEP: MVA-BN ≤4d + Tecovirimat if High-Risk. HIV CD4<200: Severe, Tecovirimat. Preg: MVA-BN Safe, Tecovirimat if Severe, Cesarean if Lesions. Isolation: All Crusted/Scabs Fallen (2-4w). IPC: Contact+Droplet, Contact Trace 21d." | Compressed. |

---

## 10. 📌 Summary
- **Clades**: **I (Congo, Severe, CFR ~10%), IIa (West Africa Endemic), IIb (2022 Global Outbreak, Milder, CFR <1%)**
- **2022 Outbreak Clinical**: **Genital/Perianal Predominant**, **Mild/No Prodrome**, **Asynchronous Lesions**, **Proctitis/Pharyngitis/Urethritis Common**
- **Diagnosis**: **Lesion Swab PCR (Gold Standard)** — Swab Base of Vesicle/Pustule/Crust
- **Management**: **Supportive** (Analgesia, Hydration, Wound Care); **Tecovirimat 600mg BD × 14 Days** for **Severe/High-Risk** (HIV CD4<200, Immunocompromised, Pregnancy, Children, Complications)
- **Vaccine**: **MVA-BN (JYNNEOS) 2 Doses (28 Days Apart)** — **Safe in Immunocompromised, HIV, Pregnancy**
- **PrEP**: **MSM (High Risk), Sex Workers, Lab/HCW**
- **PEP**: **MVA-BN ≤4 Days (Up to 14 Days) + Tecovirimat if High-Risk Individual**
- **HIV Co-infection**: **CD4<200 = Severe**; **Tecovirimat Indicated**; **Continue ART**; **MVA-BN Safe (2 Doses)**
- **Pregnancy**: **MVA-BN Safe**; **Tecovirimat if Severe**; **Cesarean if Active Genital Lesions**
- **Isolation**: **Contact + Droplet Precautions** Until **All Lesions Crusted, Scabs Fallen Off, Fresh Skin Formed (2-4 Weeks)**
- **Contact Tracing**: **21-Day Monitoring**; **High-Risk Contacts → MVA-BN PEP (≤4 Days Ideal, Up to 14 Days) + Tecovirimat if High-Risk**
- **Tecovirimat Resistance**: **VP37 Mutations (Emerging)** — Monitor Clinical Failure

---

## 11. ❓ MCQs (10)

1. **Mpox clade responsible for 2022 global outbreak?**  
   A. Clade I  B. Clade IIa  C. **Clade IIb (B.1 Lineage)**  D. Clade III  
   *Answer: C. Clade IIb (B.1 Lineage) — 2022 Global Outbreak.*

2. **Classic Mpox (Clade I) clinical presentation?**  
   A. Genital/perianal predominant, mild prodrome  B. **Centrifugal rash, synchronous lesions, marked lymphadenopathy, systemic prodrome**  C. Asynchronous lesions, no systemic symptoms  D. Single genital lesion only  
   *Answer: B. Centrifugal (Face→Extremities), Synchronous Lesions, Marked Lymphadenopathy, Systemic Prodrome (Fever, Myalgia).*

3. **Gold standard diagnostic test for Mpox?**  
   A. Serology (IgM/IgG)  B. **Lesion Swab PCR (MPXV Specific)**  C. Viral Culture  D. Electron Microscopy  
   *Answer: B. Lesion Swab PCR (MPXV Specific) — Gold Standard.*

4. **Tecovirimat — mechanism of action?**  
   A. DNA Polymerase Inhibitor  B. **VP37 Envelope Protein Inhibitor (Blocks Viral Egress)**  C. Thymidine Kinase Inhibitor  D. Neuraminidase Inhibitor  
   *Answer: B. VP37 Envelope Protein Inhibitor — Blocks Viral Egress (Orthopoxvirus Specific).*

5. **Tecovirimat — indications for use?**  
   A. All Mpox Cases  B. **Severe Disease, High-Risk (HIV CD4<200, Immunocompromised, Pregnancy, Children, Complications)**  C. Mild Cases Only  D. Prophylaxis Only  
   *Answer: B. Severe Disease, High-Risk (HIV CD4<200, Immunocompromised, Pregnancy, Children, Complications).*

6. **Mpox vaccine — preferred for immunocompromised and pregnancy?**  
   A. ACAM2000  B. **MVA-BN (JYNNEOS/IMVANEX) — Non-Replicating**  C. LC16m8  D. Dryvax  
   *Answer: B. MVA-BN (JYNNEOS/IMVANEX) — Non-Replicating, Safe in Immunocompromised, HIV, Pregnancy.*

6. **Mpox PEP — optimal timing?**  
   A. Within 24 Hours Only  B. **Ideally ≤4 Days Post-Exposure (Up to 14 Days for Vaccine)**  C. Within 72 Hours Only  D. Up to 21 Days  
   *Answer: B. Ideally ≤4 Days Post-Exposure (Up to 14 Days for Vaccine); Tecovirimat Added if High-Risk.*

8. **Mpox isolation duration?**  
   A. 7 Days from Onset  B. **Until All Lesions Crusted, Scabs Fallen Off, Fresh Skin Formed (2-4 Weeks)**  C. 14 Days from Onset  D. 10 Days from Last Lesion  
   *Answer: B. Until All Lesions Crusted, Scabs Fallen Off, Fresh Skin Formed (2-4 Weeks).*

9. **Mpox in HIV — severity threshold for severe disease?**  
   A. CD4 <350  B. **CD4 <200**  C. CD4 <500  D. Any HIV+  
   *Answer: B. CD4 <200 = Severe, Prolonged, Disseminated, Higher Mortality — Tecovirimat Indicated.*

10. **Mpox contact tracing — high-risk contacts PEP?**  
    A. Monitor Only  B. **MVA-BN 2 Doses (Day 0, 28) Ideally ≤4 Days Post-Exposure + Tecovirimat if High-Risk Individual**  C. ACAM2000  D. Tecovirimat Only  
    *Answer: B. MVA-BN 2 Doses (Day 0, 28) Ideally Within 4 Days (Up to 14 Days) + Tecovirimat if High-Risk Individual.*

---

## 12. 📋 SBAs (10)

1. **30M, MSM, painless perianal ulcer, no fever. Mpox PCR positive. Management?**  
   A. Tecovirimat 600mg BD × 14d  B. **Supportive Care, Isolation, Contact Tracing (No Tecovirimat — Mild, Not High-Risk)**  C. Ceftriaxone  D. Acyclovir  
   *Answer: B. Mild Mpox (Clade IIb Typical) → Supportive Care Only; Tecovirimat for Severe/High-Risk Only.*

2. **HIV+ patient (CD4 150) with Mpox, extensive lesions, rectal bleeding. Management?**  
   A. Supportive Only  B. **Tecovirimat 600mg BD × 14d + Continue ART (Check Interactions)**  C. MVA-BN Vaccine Only  D. Cidofovir  
   *Answer: B. HIV CD4<200 = High-Risk → Tecovirimat 600mg BD × 14d + Continue ART (Check CYP3A4 Interactions).*

3. **Pregnant woman at 28 weeks diagnosed with Mpox, mild disease. Vaccination?**  
   A. ACAM2000  B. **MVA-BN (Safe in Pregnancy, Non-Replicating)**  C. No Vaccine  D. Defer Until Postpartum  
   *Answer: B. MVA-BN Safe in Pregnancy (Non-Replicating); ACAM2000 Contraindicated.*

4. **Mpox contact — household member, unprotected contact, immunocompetent. PEP?**  
   A. No PEP Needed  B. **MVA-BN 2 Doses (Day 0, 28) Ideally Within 4 Days**  C. Tecovirimat Only  D. ACAM2000  
   *Answer: B. MVA-BN 2 Doses (Day 0, 28) Ideally Within 4 Days (Up to 14 Days).*

5. **Mpox isolation — when can patient be released?**  
   A. 7 Days After Onset  B. **All Lesions Crusted, Scabs Fallen Off, Fresh Skin Formed**  C. PCR Negative  D. 14 Days After Onset  
   *Answer: B. Until All Lesions Crusted, Scabs Fallen Off, Fresh Skin Formed (2-4 Weeks).*

---

## 13. 🔑 Answer Keys
| MCQs | SBAs |
|------|------|
| 1-C, 2-B, 3-B, 4-B, 5-B, 6-B, 7-B, 8-B, 9-B, 10-B | 1-B, 2-B, 3-B, 4-B, 5-B |

---

## 14. 🔗 Cross-Links
- [[2.1 Chlamydia.md]] — Co-infection, STI Screening
- [[2.2 Gonorrhoea.md]] — Co-infection
- [[2.3 Syphilis.md]] — Differential (GUD), Co-infection
- [[2.4-2.6 Other Bacterial STIs.md]] — Co-infection
- [[3.2 HSV.md]] — Differential (Genital Ulcers/Proctitis), Co-infection
- [[3.3 HPV.md]] — Co-infection, Vaccination
- [[3.4 Hepatitis B & C.md]] — Co-infection, Co-infection Management
- [[3.6 Other Viral STIs.md]] — Other Emerging Viral STIs
- [[5.1-5.8 Syndromic Management.md]] — GUD Algorithm, Proctitis
- [[HIV/AIDS Cross-Reference]] — Mpox in HIV, Severe Disease, Vaccination, ART Interactions
- [[9. ELSI]] — Stigma, Vaccine Equity, Contact Tracing Ethics, Public Health Emergency Powers

---

**Last Updated:** 2026-06-15  
**Next:** Build `3.6 Other Viral STIs.md`