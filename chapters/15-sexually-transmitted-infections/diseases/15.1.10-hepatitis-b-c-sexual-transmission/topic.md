**Parent Topic:** [STI MOC](../Sexually%20Transmitted%20Infections%20MOC.md) → [STI Hierarchy](../Davidson%20Chapter%2013%20-%20STI%20Hierarchy.md)  
**Status:** `full-fcps-mrcp-note`  
**Priority:** ⭐⭐⭐ HIGHEST (FCPS/MRCP — Viral Hepatitis, Sexual Transmission, Treatment, Prevention)  
**Source:** Davidson 24th Ed Ch 13 & Ch 22; WHO/EASL/APASL/BASHH Guidelines; FCPS/MRCP Syllabus

---

## 1. 🎯 Learning Objectives
- [ ] Differentiate **HBV vs HCV** Virology, Transmission, Natural History
- [ ] Apply **Sexual Transmission Risk** by Practice Type and Viral Load
- [ ] Interpret **Serological Markers** (HBsAg, Anti-HBs, Anti-HBc IgM/IgG, HBeAg, Anti-HBe, HBV DNA; Anti-HCV, HCV RNA, Genotype)
- [ ] Manage **Acute vs Chronic HBV** (Treatment Indications, Regimens: TAF/TDF/ETV; Endpoints)
- [ ] Manage **HCV** (DAA Regimens: Pan-Genotypic, Duration, SVR12)
- [ ] Implement **Prevention** (HBV Vaccination, Post-Exposure Prophylaxis, Harm Reduction)
- [ ] Manage **Special Populations** (HIV Co-infection, Pregnancy, Renal Impairment, Transplant)
- [ ] Answer viva: "HBV Serology Interpretation" and "HCV DAA Regimens" and "HBV Reactivation Risk" and "Sexual Transmission Risk"

---

## 2. 🧠 Core Concept: HBV vs HCV Comparison

```mermaid
flowchart TD
    A[Viral Hepatitis] --> B[Hepatitis B Virus (HBV)]
    A --> C[Hepatitis C Virus (HCV)]
    B --> B1[DNA Virus (Hepadnaviridae)]
    B --> B2[Partially dsDNA, Relaxed Circular]
    B --> B3[Reverse Transcription Replication]
    B --> B4[cccDNA in Nucleus = Persistence]
    B --> B5[Genotypes A-J]
    C --> C1[RNA Virus (Flaviviridae)]
    C --> C2[Positive-Sense ssRNA]
    C --> C3[RNA-Dependent RNA Polymerase (No Proofreading)]
    C --> C4[High Mutation Rate = Quasispecies]
    C --> C5[Genotypes 1-8 (Subtypes a,b...)]
    B & C --> D[Sexual Transmission]
    D --> D1[HBV: HIGH (100x HIV) — Semen, Vaginal Fluids, Blood]
    D --> D2[HCV: LOW (Overall) — Blood Predominant; ↑ MSM/HIV/Trauma]
```

---

## 1️⃣ Hepatitis B Virus (HBV)

### Virology & Transmission

| Feature | Details |
|---------|---------|
| **Virus** | **DNA Virus (Hepadnaviridae)**; Partially dsDNA, Relaxed Circular; Reverse Transcriptase Replication |
| **Genotypes** | **A-J** (Geographic Distribution; A/D Europe/US; B/C Asia/Africa; Impacts Disease/Treatment) |
| **Key Antigens** | **HBsAg (Surface)**, **HBcAg (Core)**, **HBeAg (Secreted Core = Replication Marker)** |
| **Persistence** | **cccDNA in Hepatocyte Nucleus** = Template for Transcription → **True Cure Rare** |
| **Sexual Transmission** | **HIGH EFFICIENCY** — **100x HIV**; **Semen, Vaginal Secretions, Blood**; **Perinatal (Vertical) Major** |
| **Risk Groups** | **MSM, Multiple Partners, Sex Workers, PWID, Household Contacts, Healthcare Workers** |
| **Incubation** | **60-150 Days** (Average 90 Days) |

### Serological Markers (Critical for MRCP)

| Marker | Significance | Acute | Chronic | Resolved/Immune | Vaccinated |
|--------|--------------|-------|---------|-----------------|------------|
| **HBsAg** | Current Infection (Surface Antigen) | + | + | – | – |
| **Anti-HBs** | Protective Antibody (≥10 mIU/mL = Immune) | – (Late) | – | + | + |
| **Anti-HBc IgM** | **Acute/Recent Infection (<6 Months)** | **+** | –/+ (Flare) | – | – |
| **Anti-HBc IgG (Total Anti-HBc)** | Past/Current Infection (Core Antibody) | + | + | + | – |
| **HBeAg** | High Replication/Infectivity | + (Early) | + (Immune Tolerant/Active) | – | – |
| **Anti-HBe** | Lower Replication / Seroconversion | + (Late) | + (Inactive Carrier) | + | – |
| **HBV DNA** | Viral Load (Quantitative, IU/mL) | High | Variable (Phase-Dependent) | Undetectable | Undetectable |

### Natural History Phases (Chronic HBV)

```mermaid
flowchart LR
    A[Phase 1: Immune Tolerant] --> B[Phase 2: Immune Active (HBeAg+)]
    B --> C[Phase 3: Inactive Carrier (HBeAg-, Anti-HBe+)]
    C --> D[Phase 4: HBeAg-Negative Chronic Hepatitis (Reactivation)]
    D --> C
    
    A1[HBeAg+, High HBV DNA (>10^7), Normal ALT, Minimal Inflammation<br/>Common in Perinatal Infection, Children] --> A
    B1[HBeAg+, High HBV DNA, **Elevated ALT**, Active Inflammation/Fibrosis<br/>**Treatment Indicated**] --> B
    C1[HBeAg-, Anti-HBe+, **Low HBV DNA (<2000 IU/mL), Normal ALT**<br/>Low Infectivity, Good Prognosis] --> C
    D1[HBeAg-, Anti-HBe+, **HBV DNA >2000 IU/mL, Elevated ALT**<br/>Precore/Core Promoter Mutants, Progressive Fibrosis] --> D
```

### Treatment Indications (EASL/APASL 2024)

| Phase | Criteria | Treatment |
|-------|----------|-----------|
| **Immune Active (HBeAg+)** | **ALT >2x ULN** AND **HBV DNA >20,000 IU/mL** (≥20,000 EASL, ≥2,000 APASL) | **Treat** |
| **HBeAg-Negative CHB** | **ALT >ULN** AND **HBV DNA >2,000 IU/mL** | **Treat** |
| **Cirrhosis (Any HBeAg)** | **Any Detectable HBV DNA** | **Treat** |
| **Immune Tolerant / Inactive Carrier** | Normal ALT, High/Low DNA Respectively | **Monitor (No Tx Unless Cirrhosis/Immunosuppression)** |
| **Acute Liver Failure** | **HBV DNA High, ALT Very High, INR ↑** | **Urgent NUC (TAF/TDF/ETV) + Transplant Assessment** |

### Nucleos(t)ide Analogues (NUCs) — 1st Line

| Drug | Dose (Adult) | Renal Adjustment | Resistance Barrier | Preferred For |
|------|--------------|------------------|-------------------|---------------|
| **Tenofovir Alafenamide (TAF)** | **25mg OD** | **CrCl ≥15: No Adjust; <15: Avoid** | **High** | **All (Preferred — Bone/Renal Safety)** |
| **Tenofovir Disoproxil Fumarate (TDF)** | **245mg OD (300mg Salt)** | **CrCl 30-49: 48h; 15-29: 72-96h; <15: Avoid** | **High** | Alternative if TAF Unavailable |
| **Entecavir (ETV)** | **0.5mg OD (1mg if TDF-Experienced/Resistant)** | **CrCl 30-49: 0.25mg; 15-29: 0.15mg; <15: 0.05mg** | **High (Naive); Low (LAM-Experienced)** | Alternative (Renal Safe) |

> **Pegylated IFN-α**: **Finite Duration (48w HBeAg+, 48w HBeAg-)**, **HBeAg Seroconversion ~30%**, **Side Effects High**, **Contraindicated in Decompensated Cirrhosis**

### Treatment Endpoints

| Endpoint | Definition | Significance |
|----------|------------|--------------|
| **Virological Response** | **HBV DNA Undetectable (PCR <10-15 IU/mL)** | Primary On-Treatment Goal |
| **HBeAg Seroconversion** | **HBeAg Loss + Anti-HBe Detection** | **Functional Cure Marker (HBeAg+)**; Allows Finite Tx Consideration |
| **HBsAg Loss (Functional Cure)** | **HBsAg Loss + Anti-HBs Seroconversion** | **Ultimate Goal (Rare on NUCs ~1-3%/yr)**; Allows Stopping |
| **HBsAg Seroclearance** | HBsAg Loss Without Anti-HBs | Functional Cure (Less Robust) |
| **Histological Improvement** | Fibrosis Regression (Non-Invasive: FibroScan, APRI, FIB-4) | Long-Term Benefit |

### Stopping Rules (NUCs)

| Scenario | Criteria |
|----------|----------|
| **HBeAg+ Chronic HBV** | **Consolidation: Continue 12 Months AFTER HBeAg Seroconversion + Undetectable DNA** |
| **HBeAg-Negative CHB** | **No Definite Stopping Rule** — **Long-Term/Indefinite Usually Required** (Relapse High) |
| **HBsAg Loss** | **Can Stop (Functional Cure Achieved)** — Monitor q6-12m |
| **Cirrhosis** | **Do Not Stop (Lifelong)** — Risk of Decompensation |

---

## 2️⃣ Hepatitis C Virus (HCV)

### Virology & Transmission

| Feature | Details |
|---------|---------|
| **Virus** | **RNA Virus (Flaviviridae)**; Positive-Sense ssRNA; RNA-Dependent RNA Polymerase (No Proofreading) |
| **Genotypes** | **1-8** (Subtypes a,b...); **GT1 Most Common Global (46%), GT3 (30%), GT4 (MENA), GT6 (SE Asia)** |
| **Quasispecies** | **High Mutation Rate** → Immune Escape, Variable Disease Progression |
| **Sexual Transmission** | **LOW Overall (~1-3% Long-Term Partners)**; **↑ MSM (HIV+, PrEP, Trauma, Multiple Partners, STIs)**; **Blood = Major Route** |
| **Risk Groups** | **PWID (Major), Pre-1990 Blood Transfusions, Unsafe Medical Procedures, MSM (HIV+), Vertical (5-6%)** |
| **Incubation** | **2 Weeks - 6 Months** (Average 6-9 Weeks) |

### Natural History

```mermaid
flowchart LR
    A[Acute HCV] --> B{Spontaneous Clearance}
    B -->|~25-30%| C[Resolved (Anti-HCV+, HCV RNA-)]
    B -->|~70-75%| D[Chronic HCV]
    D --> E[Progressive Fibrosis (F0-F4)]
    E --> F[Cirrhosis (F4) ~15-30% over 20-30y]
    F --> G[Decompensated Cirrhosis / HCC]
    
    Cofactors --> H[↑ Progression: Age>40, Male, Alcohol, Obesity/NAFLD, HIV Co-inf, HBV Co-inf, Immunosuppression]
```

### Diagnosis Algorithm

```mermaid
flowchart TD
    A[Risk Factors / Screening] --> B[**Anti-HCV Antibody (EIA/CIA)**]
    B --> C{Result}
    C -->|Negative| D[No HCV Infection (Window: Retest if Recent Risk)]
    C -->|Positive| E[**HCV RNA PCR (Quantitative) — Confirm Viraemia**]
    E --> F{HCV RNA}
    F -->|Negative| G[**Past Infection (Spontaneous Clearance / Treated)**]
    F -->|Positive| H[**Current Chronic HCV Infection**]
    H --> I[**Genotype (If Non-Pan-Genotypic DAA) / Fibrosis Assessment (FibroScan, APRI, FIB-4, Biopsy)**]
    I --> J[**DAA Treatment Selection**]
```

### DAA Regimens (Pan-Genotypic, WHO/EASL 2024)

| Regimen | Genotypes | Duration (Non-Cirrhotics) | Duration (Compensated Cirrhosis) | Key Features |
|---------|-----------|---------------------------|----------------------------------|--------------|
| **Sofosbuvir/Velpatasvir (SOF/VEL)** | **1-6 (Pan-Genotypic)** | **12 Weeks** | **12 Weeks** | **Preferred 1st Line**; Renal Safe (SOF CrCl≥30) |
| **Glecaprevir/Pibrentasvir (GLE/PIB)** | **1-6 (Pan-Genotypic)** | **8 Weeks** | **8-12 Weeks (12w if GT3 Cirrhosis)** | **Shortest (8w); Contra: Decompensated (Child-Pugh B/C)** |
| **Sofosbuvir/Velpatasvir/Voxilaprevir (SOF/VEL/VOX)** | **1-6 (Pan-Genotypic)** | **12 Weeks** | **12 Weeks** | **Retreatment (Prior DAA Failure)** |
| **Sofosbuvir/Daclatasvir (SOF/DCV)** | **1-6 (Pan-Genotypic)** | **12 Weeks** | **12-24 Weeks** | **Low Cost (Generic); Renal Safe (DCV No Adjust)** |
| **Grazoprevir/Elbasvir (GZR/EBR)** | **1, 4, 6** | **12-16 Weeks** | **12-16 Weeks** | **RAS Testing for GT1a (NS5A)** |

> **Treatment Goal**: **SVR12 (Sustained Virological Response at 12 Weeks Post-Tx) = CURE (>95%)**
> **Monitoring**: **HCV RNA at 4w (Rapid VR), End of Tx, 12w Post-Tx (SVR12)**
> **Decompensated Cirrhosis (Child-Pugh B/C)**: **SOF/VEL + Ribavirin 12w (or 24w); Refer Transplant**

### Special Populations HCV

| Population | Regimen Adjustment |
|------------|-------------------|
| **CKD / ESRD (CrCl <30)** | **GLE/PIB (No Renal Adjust)** OR **GZR/EBR (No Renal Adjust)**; **Avoid SOF (Accumulation)** |
| **HIV Co-infection** | **Same Regimens (Check DDIs: ART)**; **SOF/VEL, GLE/PIB Preferred** |
| **Pregnancy** | **Defer Treatment (No DAA Safety Data)**; **Treat Postpartum** |
| **Transplant (Liver/Kidney)** | **Pre-Transplant Preferred**; **Post-Transplant: DDIs with Tacrolimus/Cyclosporine (GLE/PIB ↑ Levels, SOF/VEL Safer)** |
| **Prior DAA Failure** | **SOF/VEL/VOX 12 Weeks (Pan-GT)**; **Resistance Testing If Available** |

---

## 3️⃣ Sexual Transmission: HBV vs HCV

| Parameter | **HBV** | **HCV** |
|-----------|---------|---------|
| **Sexual Transmission Efficiency** | **HIGH (100x HIV)** | **LOW (Overall ~1-3% Long-Term Partners)** |
| **Key Fluids** | Semen, Vaginal Secretions, Blood, Saliva (Low) | Blood (Primary); Semen (Low, ↑ HIV/Trauma) |
| **High-Risk Practices** | Unprotected Vaginal/Anal/Oral Sex, Multiple Partners, Sex Work, MSM | **MSM + HIV+ / PrEP + Trauma (Fisting, Toys, Group Sex) + STIs** |
| **Viral Load Correlation** | **HBeAg+ / High HBV DNA = High Infectivity** | **HCV RNA+ = Infectious (But Sexual Transmission Rare Without Blood)** |
| **Prevention** | **Vaccination (100% Effective if Immune), Condoms, Partner Vaccination** | **No Vaccine; Condoms, Harm Reduction (PWID), Treat HCV (+ve Partner) = Prevention** |
| **Partner Testing** | **All Sexual/Household Contacts: HBsAg, Anti-HBs, Anti-HBc** | **Sexual Partners: Anti-HCV (If Positive → HCV RNA)**; **MSM/HIV: Test Regularly** |

---

## 4️⃣ Prevention

### HBV Vaccination

| Schedule | Doses | Interval | Target |
|----------|-------|----------|--------|
| **Standard** | **3** | **0, 1, 6 Months** | Adults, Catch-Up |
| **Accelerated** | **3** | **0, 1, 2 Months (+ Booster 12m)** | High Risk (Travel, PWID, MSM) |
| **Heplisav-B (CpG Adjuvant)** | **2** | **0, 1 Month** | Adults ≥18y (Higher Seroprotection) |
| **Post-Exposure Prophylaxis (PEP)** | **HBIG + Vaccine** | **HBIG 0.06 mL/kg IM + Vaccine (Separate Sites) within 24h (Max 7d)** | Needlestick, Sexual Assault, Perinatal |

### Post-Exposure Prophylaxis (PEP)

| Exposure | Source HBsAg+ | Source Unknown | Source HBsAg- |
|----------|---------------|----------------|---------------|
| **Unvaccinated / Non-Responder** | **HBIG + Vaccine (0,1,6m)** | **HBIG + Vaccine** | **Vaccine Only** |
| **Vaccinated, Anti-HBs ≥10** | **No PEP** | **No PEP** | **No PEP** |
| **Vaccinated, Anti-HBs <10** | **HBIG + Booster** | **Booster** | **Booster** |
| **Perinatal (Mother HBsAg+)** | **HBIG + Vaccine (Within 12h Birth)** | — | — |

### HCV Prevention
- **No Vaccine Available**
- **Harm Reduction**: Needle/Syringe Programs, OST (Opioid Substitution Therapy)
- **Safe Medical Practices**: Blood Screening, Sterile Equipment
- **Treat Infected Partners**: **Treatment as Prevention (TasP) — SVR = No Transmission**
- **MSM**: Condoms, Regular Testing (HIV/STI Clinics), Limit Trauma Practices

---

## 5️⃣ Special Populations

### HIV Co-infection

| Aspect | HBV/HIV | HCV/HIV |
|--------|---------|---------|
| **Prevalence** | **~10% HIV+ Have Chronic HBV** | **~25-30% HIV+ Have HCV (PWID/MSM)** |
| **Disease Progression** | **Faster Fibrosis, Higher HCC Risk** | **Faster Fibrosis, Lower Spontaneous Clearance** |
| **ART Interactions** | **TDF/TAF in ART = HBV Treatment Also** | **DAA + ART → Check DDIs (SOF/VEL, GLE/PIB OK with Most)** |
| **HBV Reactivation** | **Risk if ART Stopped / Immunosuppression** | — |
| **Monitoring** | **HBV DNA q3-6m (If Not on TDF/TAF)** | **HCV RNA / SVR12 Monitoring** |

### Pregnancy

| Virus | Management |
|-------|------------|
| **HBV** | **Screen All (HBsAg at Booking)**; **HBV DNA >200,000 IU/mL → TAF/TDF from 28w (Prevent Vertical Transmission)**; **Infant: HBIG + Vaccine <12h** |
| **HCV** | **Screen Risk-Based (or Universal)**; **No Vertical Tx Prevention (DAA Contraindicated)**; **Vertical Tx Rate ~5-6% (↑ if HIV+, High RNA)**; **Infant Test: Anti-HCV at 18m / HCV RNA at 2-3m** |

### Renal Impairment

| Drug | CrCl <30 / ESRD |
|------|-----------------|
| **TAF** | Avoid (Limited Data) |
| **TDF** | Avoid (Nephrotoxicity) |
| **ETV** | **Dose Adjust (0.05mg OD if <15)** — **Preferred for HBV** |
| **SOF** | Avoid (Accumulation) |
| **GLE/PIB** | **No Adjust — Preferred for HCV** |
| **GZR/EBR** | **No Adjust** |
| **DCV** | **No Adjust** |

### HBV Reactivation Risk

| Risk Category | Setting | Prophylaxis |
|---------------|---------|-------------|
| **High (≥10%)** | **Anti-CD20 (Rituximab), Stem Cell Transplant, High-Dose Steroids (>20mg Pred >4w)** | **TAF/TDF/ETV Prophylaxis (Start Before, Continue 12m Post)** |
| **Moderate (1-10%)** | **TNF-α Inhibitors, Moderate Steroids, TKIs** | **Monitor HBV DNA q1-3m OR Prophylaxis** |
| **Low (<1%)** | **Standard Chemo (Non-Haematologic), Intra-articular Steroids** | **Monitor ALT/HBV DNA q3m** |

> **Screen Before Immunosuppression: HBsAg, Anti-HBc, Anti-HBs** — **Anti-HBc+ (Resolved) = Reactivation Risk**

---

## 3. ⚡ FCPS/MRCP High-Yield Summary

| Topic | Key Points |
|-------|------------|
| **HBV Virology** | DNA Virus, cccDNA Persistence, Genotypes A-J, HBeAg = Replication Marker |
| **HBV Serology** | **HBsAg+/Anti-HBc IgM+ = Acute**; **HBsAg+/HBeAg+/High DNA = Immune Tolerant/Active**; **HBsAg+/Anti-HBe+/Low DNA = Inactive Carrier**; **HBsAg-/Anti-HBs+/Anti-HBc+ = Resolved**; **Anti-HBs+ Only = Vaccinated** |
| **HBV Treatment** | **NUCs: TAF 25mg OD (1st Line), TDF 245mg OD, ETV 0.5mg OD**; **Indications: Immune Active (ALT>2xULN+DNA>20k), HBeAg-Neg CHB (ALT>ULN+DNA>2k), Cirrhosis** |
| **HBV Endpoints** | **Virological Response (DNA Undetectable) → HBeAg Seroconversion → HBsAg Loss (Functional Cure)** |
| **HCV Virology** | RNA Virus, GT1-8, Quasispecies, High Mutation |
| **HCV Diagnosis** | **Anti-HCV → If Positive → HCV RNA PCR (Confirm Viraemia) → Genotype/Fibrosis** |
| **HCV Treatment** | **Pan-Genotypic DAAs: SOF/VEL 12w, GLE/PIB 8w (12w GT3 Cirrhosis)**; **SVR12 = Cure (>95%)** |
| **Sexual Transmission** | **HBV: HIGH (100x HIV); HCV: LOW (Except MSM/HIV/Trauma)** |
| **Prevention** | **HBV: Vaccine (3-dose 0,1,6m; Heplisav-B 2-dose); PEP: HBIG+Vaccine**; **HCV: Harm Reduction, TasP, No Vaccine** |
| **Special Pops** | **HIV: TDF/TAF in ART covers HBV; DAA+ART Check DDIs**; **Preg: HBV DNA>200k→TAF/TDF 28w+HBIG+Vaccine Infant; HCV Defer** |
| **HBV Reactivation** | **Screen Anti-HBc Before Immunosuppression; High Risk (Anti-CD20, SCT) → NUC Prophylaxis** |
| **Viva** | "HBV Serology Interpretation", "HCV DAA Regimens", "HBV Reactivation Risk", "Vertical Transmission Prevention" |

---

## 4. 🎤 Viva Questions (Expected Answers)

| # | Question | Expected Answer |
|---|----------|-----------------|
| 1 | Interpret HBV Serology: HBsAg+, HBeAg+, Anti-HBe-, Anti-HBc IgM+, High HBV DNA, Elevated ALT. | **Acute Hepatitis B (Immune Active Phase) — HBsAg+ = Current Infection; HBeAg+ = High Replication; Anti-HBc IgM+ = Acute (<6 Months); High DNA + Elevated ALT = Immune Clearance** |
| 2 | Chronic HBV Serology: HBsAg+, HBeAg-, Anti-HBe+, HBV DNA 1,500 IU/mL, Normal ALT. Phase? | **Inactive Carrier (Phase 3) — HBeAg Seroconversion Achieved; Low DNA (<2000); Normal ALT; Low Infectivity; Monitor q6-12m (No Tx Unless Cirrhosis/Immunosuppression)** |
| 3 | 1st Line Nucleos(t)ide Analogues for Chronic HBV — Dosing & Renal Adjustment. | **TAF 25mg OD (Preferred — Bone/Renal Safe, CrCl≥15 No Adjust); TDF 245mg OD (CrCl 30-49: 48h, 15-29: 72-96h); ETV 0.5mg OD (CrCl 30-49: 0.25mg, 15-29: 0.15mg, <15: 0.05mg)** |
| 4 | Treatment Indications for HBeAg-Negative Chronic Hepatitis B. | **ALT >ULN AND HBV DNA >2,000 IU/mL** (EASL/APASL); **Cirrhosis = Treat Any Detectable DNA** |
| 5 | HCV Diagnosis Algorithm — Anti-HCV Positive, What Next? | **HCV RNA PCR (Quantitative) — If Positive = Current Infection; If Negative = Past Infection (Spontaneous Clearance/Treated); Then Genotype (If Non-Pan-Genotypic) + Fibrosis Assessment** |
| 6 | Pan-Genotypic DAA Regimens for HCV — First-Line Options. | **SOF/VEL 12 Weeks (All GT, Renal Safe CrCl≥30); GLE/PIB 8 Weeks (All GT, Shortest, Contra Decompensated Cirrhosis); SOF/DCV 12 Weeks (Low Cost, Renal Safe)** |
| 7 | SVR12 Definition and Significance. | **Sustained Virological Response at 12 Weeks Post-Treatment = HCV RNA Undetectable = CURE (>95% with DAAs); No Further Monitoring Needed Unless Cirrhosis (HCC Surveillance Continues)** |
| 8 | Sexual Transmission Risk — HBV vs HCV. | **HBV: HIGH (100x HIV) — Semen, Vaginal Fluids, Blood; HCV: LOW Overall (~1-3% Long-Term Partners) — ↑ MSM with HIV/PrEP/Trauma/STIs** |
| 9 | HBV in Pregnancy — Vertical Transmission Prevention. | **Screen All (HBsAg at Booking); If HBsAg+: HBV DNA at 28w; If >200,000 IU/mL → TAF/TDF from 28w to 12w Postpartum; Infant: HBIG 0.06mL/kg + Vaccine (Separate Sites) <12h Birth; Complete Vaccine Series** |
| 10 | HBV Reactivation — Who Needs Prophylaxis? | **Screen Before Immunosuppression: HBsAg, Anti-HBc, Anti-HBs**; **Anti-HBc+ (Resolved) = At Risk**; **High Risk (Anti-CD20/Rituximab, Stem Cell Transplant, High-Dose Steroids): NUC Prophylaxis (TAF/TDF/ETV) Start Before, Continue 12m Post**; **Moderate Risk: Monitor or Prophylaxis**; **HBsAg+ Chronic: Always Prophylaxis** |

---

## 5. 🧩 Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **"Anti-HBc = Vaccination Response"** | **NO.** **Anti-HBc = Natural Infection Only**; **Vaccine = Anti-HBs ONLY** |
| **"HBeAg-Negative = Inactive Carrier Always"** | **NO.** **HBeAg-Negative CHB (Reactivation) = HBeAg-, Anti-HBe+, DNA >2000, ALT Elevated** — **Treat** |
| **"TDF and TAF = Same Drug"** | **TAF = Prodrug of TFV with Better Plasma Stability → Lower Renal/Bone Toxicity**; **Dose: TAF 25mg vs TDF 245mg (300mg Salt)** |
| **"HCV Antibody Positive = Active Infection"** | **NO.** **Anti-HCV+ = Exposure (Past or Current)**; **MUST Check HCV RNA to Confirm Viraemia** |
| **"All HCV Genotypes Need Genotyping Before Treatment"** | **NO.** **Pan-Genotypic DAAs (SOF/VEL, GLE/PIB, SOF/DCV) = No Genotyping Needed** |
| **"HCV = Sexually Transmitted Like HBV"** | **NO.** **HCV Sexual Transmission LOW (Except MSM/HIV/Trauma); Blood = Main Route** |
| **"HBV Vaccine = 3 Doses Always"** | **Standard 3-Dose (0,1,6m); Accelerated 3-Dose (0,1,2m+Booster); Heplisav-B = 2-Dose (0,1m)** |
| **"HBV Reactivation = Only in HBsAg+"** | **NO.** **Anti-HBc+ (Resolved) Also At Risk (Occult HBV)**; **Screen Both Before Immunosuppression** |
| **"DAA = Interferon-Free = No Side Effects"** | **Mostly Well Tolerated BUT: Fatigue, Headache, Nausea; Drug-Drug Interactions Critical (ART, Statins, Antacids, Amiodarone)** |
| **"SVR12 = Life-Long Immunity"** | **NO.** **SVR = Cure of Current Infection**; **Re-infection Possible with Re-Exposure (No Protective Immunity)** |

> **Mnemonic: HBV HCV MASTER SHIELD**  
> **H**BV: **DNA Virus, cccDNA Persistence, Genotypes A-J**  
> **B** Serology: **HBsAg+ = Infection; Anti-HBs+ = Immune (Vaccine/Resolved); Anti-HBc IgM+ = Acute; Anti-HBc Total = Past/Current; HBeAg+ = Replication; Anti-HBe+ = Lower Replication**  
> **V** Phases: **Immune Tolerant (HBeAg+/High DNA/NL ALT) → Immune Active (HBeAg+/High DNA/↑ALT=Tx) → Inactive Carrier (HBeAg-/Anti-HBe+/Low DNA/NL ALT) → HBeAg-Neg CHB (HBeAg-/Anti-HBe+/DNA>2k/↑ALT=Tx)**  
> **T**reatment HBV: **NUCs 1st Line — TAF 25mg (Prefs), TDF 245mg, ETV 0.5mg; High Barrier; Indications: Immune Active, HBeAg-Neg CHB, Cirrhosis**  
> **E**ndpoints HBV: **DNA Undetect → HBeAg Seroconv (Finite Tx Possible) → HBsAg Loss (Func Cure, Rare)**  
> **H**CV: **RNA Virus, GT1-8, Quasispecies, High Mutation, No Vaccine**  
> **C** Diagnosis HCV: **Anti-HCV → RNA PCR (+) = Current Infection; RNA (-) = Past Clearance**  
> **V** DAA: **Pan-GT 1st Line — SOF/VEL 12w, GLE/PIB 8w (12w GT3 Cirr), SOF/DCV 12w; SVR12 = Cure**  
> **S**exual: **HBV HIGH (100x HIV); HCV LOW (Except MSM/HIV/Trauma)**  
> **P**revention: **HBV Vacc (3-dose 0,1,6m / Heplisav 2-dose 0,1m); PEP: HBIG+Vacc; HCV: Harm Red, TasP, No Vacc**  
> **R** HIV Coinfection: **TDF/TAF in ART = HBV Tx; DAA+ART Check DDIs; SOF/VEL/GLE/PIB OK**  
> **E** Pregnancy: **HBV DNA>200k → TAF/TDF 28w-12w PP; Infant HBIG+Vacc <12h; HCV Defer DAA**  
> **A** Renal: **HBV: ETV (Dose Adj); HCV: GLE/PIB/GZR/EBR (No Adj) Avoid SOF**  
> **C** Reactivation HBV: **Screen HBsAg/Anti-HBc/Anti-HBs Pre-Immunosupp; Anti-HBc+ = Risk; High (Anti-CD20/SCT/High Steroid) → NUC Prophyl 12m Post**  
> **T** Vertical HBV: **Mom DNA>200k→TAF/TDF; Infant HBIG+Vacc<12h**  
> **H**CC Surveillance: **HBV Cirrhosis (or High Risk): US ± AFP q6m; HCV Post-SVR Cirrhosis: US q6m**  
> **I**terferon: **PegIFN Finite (48w HBeAg+, 48w HBeAg-); HBeAg Seroconv ~30%; SE High; Contra Decomp Cirr**  
> **E**liminate: **WHO 2030: 90% Dx, 80% Tx, 65% ↓ Mortality (HBV/HCV)**  
> **R**einfection HCV: **SVR = Cure Current; Re-infection Possible (No Immunity); Harm Red Critical**  
> **D**ecompensated: **HBV: TAF/TDF/ETV Safe; HCV: SOF/VEL+RBV 12-24w / Refer Transplant**  

---

## 6. 🗺️ Mind Map

```mermaid
mindmap
  root((Hepatitis B & C))
    HBV
      Virology: DNA, cccDNA, Genotypes A-J
      Serology: HBsAg, Anti-HBs, Anti-HBc IgM/IgG, HBeAg, Anti-HBe, DNA
      Phases: Immune Tolerant → Immune Active → Inactive Carrier → HBeAg-Neg CHB
      Treatment: NUCs (TAF/TDF/ETV) — High Barrier
      Indications: Immune Active, HBeAg-Neg CHB, Cirrhosis
      Endpoints: DNA Undetect → HBeAg Seroconv → HBsAg Loss (Func Cure)
      Prevention: Vaccine (3-dose/Heplisav 2-dose), PEP (HBIG+Vacc)
    HCV
      Virology: RNA, GT1-8, Quasispecies
      Diagnosis: Anti-HCV → RNA PCR (+) = Current; (-) = Past
      Treatment: Pan-GT DAAs (SOF/VEL 12w, GLE/PIB 8w, SOF/DCV 12w)
      SVR12 = Cure (>95%)
      Prevention: Harm Reduction, TasP, No Vaccine
    Sexual Transmission
      HBV: HIGH (100x HIV) — Semen, Vaginal, Blood
      HCV: LOW (MSM/HIV/Trauma Exception)
    Special Pops
      HIV: TDF/TAF in ART = HBV Tx; DAA+ART Check DDIs
      Pregnancy: HBV DNA>200k→TAF/TDF 28w; Infant HBIG+Vacc; HCV Defer
      Renal: HBV: ETV (Adj); HCV: GLE/PIB/GZR/EBR (No Adj)
      Reactivation: Screen Anti-HBc Pre-Immunosupp; High Risk→NUC Prophyl
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
| HBV Virology & Serology | 4 | | |
| HBV Phases & Treatment | 4 | | |
| HCV Virology & Diagnosis | 3 | | |
| HCV DAA Regimens | 4 | | |
| Sexual Transmission Comparison | 2 | | |
| Prevention (Vaccine, PEP) | 2 | | |
| Special Populations (HIV, Preg, Renal, Reactivation) | 3 | | |
| **Total** | **20** | | |

---

## 9. 💬 Exam Answer Modes

| Format | Prompt | Key Points |
|--------|--------|------------|
| **Long Essay** | "Compare and contrast Hepatitis B and C — Virology, Transmission, Diagnosis, Treatment, and Prevention." | **HBV: DNA Virus, cccDNA Persistence, Genotypes A-J; Serology: HBsAg (Infection), Anti-HBs (Immune), Anti-HBc IgM (Acute), HBeAg (Replication); Phases: Immune Tolerant → Active → Inactive → HBeAg-Neg CHB; Treatment: NUCs TAF 25mg (1st), TDF 245mg, ETV 0.5mg; Indications: Immune Active (ALT>2xULN+DNA>20k), HBeAg-Neg CHB (ALT>ULN+DNA>2k), Cirrhosis; Endpoints: DNA Undetect → HBeAg Seroconv → HBsAg Loss; Prevention: Vaccine 0,1,6m / Heplisav 0,1m; PEP: HBIG+Vacc**; **HCV: RNA Virus, GT1-8, Quasispecies; Diagnosis: Anti-HCV→RNA PCR (+=Current, -=Past); Treatment: Pan-GT DAAs SOF/VEL 12w, GLE/PIB 8w (12w GT3 Cirr), SOF/DCV 12w; SVR12=Cure; Prevention: Harm Red, TasP, No Vacc**; **Sexual: HBV HIGH (100x HIV); HCV LOW (Except MSM/HIV/Trauma)**; **HIV: TDF/TAF Covers HBV; DAA+ART Check DDIs**; **Preg: HBV DNA>200k→TAF/TDF 28w+Infant HBIG+Vacc; HCV Defer**; **Reactivation: Screen Anti-HBc Pre-Immunosupp; High Risk→NUC Prophyl 12m Post** |
| **Short Note** | "HBV Serology Interpretation — Patterns and Clinical Significance." | **HBsAg+/Anti-HBc IgM+/HBeAg+/High DNA/↑ALT = Acute Hepatitis B**; **HBsAg+/HBeAg+/High DNA/NL ALT = Immune Tolerant (Children/Perinatal)**; **HBsAg+/HBeAg+/High DNA/↑ALT = Immune Active (TREAT)**; **HBsAg+/HBeAg-/Anti-HBe+/Low DNA (<2000)/NL ALT = Inactive Carrier (Monitor)**; **HBsAg+/HBeAg-/Anti-HBe+/DNA>2000/↑ALT = HBeAg-Negative CHB (TREAT)**; **HBsAg-/Anti-HBs+/Anti-HBc+ = Resolved Natural Infection (Immune)**; **Anti-HBs+ Only (Anti-HBc-) = Vaccinated**; **HBsAg-/Anti-HBc+ Only = Occult HBV / False Positive / Window Period** |
| **Viva** | "HCV Treatment — Pan-Genotypic DAA Regimens and SVR12." | **1st Line: SOF/VEL 12 Weeks (All GT 1-6, CrCl≥30); GLE/PIB 8 Weeks (All GT, Shortest, Contra Decompensated Cirrhosis); SOF/DCV 12 Weeks (Low Cost, Renal Safe)**; **Retreatment: SOF/VEL/VOX 12 Weeks**; **CKD/ESRD: GLE/PIB or GZR/EBR (No Renal Adjust); Avoid SOF**; **Goal: SVR12 = HCV RNA Undetectable at 12 Weeks Post-Tx = CURE (>95%)**; **Monitoring: RNA at 4w (Rapid VR), EOT, 12w Post (SVR12)** |
| **Ward Round** | "HIV+ MSM on TDF/FTC/DTG, New Diagnosis HCV GT1a. Management?" | **HCV GT1a: Treat with Pan-Genotypic DAA (SOF/VEL 12w or GLE/PIB 8w)**; **Check DDIs: DTG — No Significant Interaction with SOF/VEL or GLE/PIB**; **TDF in ART = HBV Prophylaxis Also**; **Fibrosis Assessment (FibroScan/APRI) Before Tx**; **SVR12 = Cure; Re-infection Risk Counselling (Condoms, Harm Reduction)** |
| **Last-Night** | "HBV: DNA, cccDNA, GT A-J. Serol: HBsAg Inf, Anti-HBs Imm, Anti-HBc IgM Acute, HBeAg Replic. Phases: Tolerant(HBeAg+HiDNA NLidALT)→Active(HBeAg+HiDNA↑ALT=Tx)→Carrier(HBeAg-AntiHBe+LoDNA NLid)→HBeAgNegCHB(HBeAg-AntiHBe+DNA>2k↑ALT=Tx). Tx: TAF25(1st)/TDF245/ETV0.5. HCV: RNA, GT1-8. Dx: Anti-HCV→RNA(+)=Curr, (-)=Past. DAA: SOF/VEL12w/GLE/PIB8w/SOF/DCV12w→SVR12=Cure. Sex: HBV HIGH(100xHIV), HCV LOW(MSM/HIV/Trauma↑). Vacc: 0,1,6m/Heplisav 0,1m. PEP: HBIG+Vacc. HIV: TDF/TAF=HBVtx, DAA+ART DDIs. Preg: HBV DNA>200k→TAF/TDF28w+Infant HBIG+Vacc<12h. React: Screen Anti-HBc pre-Immuno; Anti-CD20/SCT/High Steroid→NUC Prophyl 12m post." | Compressed. |

---

## 10. 📌 Summary
- **HBV**: **DNA Virus, cccDNA Persistence**; **Serology: HBsAg=Infection, Anti-HBs=Immune, Anti-HBc IgM=Acute, HBeAg=High Replication**; **Phases: Immune Tolerant → Active (Treat) → Inactive Carrier → HBeAg-Neg CHB (Treat)**; **Treatment: NUCs — TAF 25mg (1st Line), TDF 245mg, ETV 0.5mg**; **Indications: Immune Active (ALT>2xULN+DNA>20k), HBeAg-Neg CHB (ALT>ULN+DNA>2k), Cirrhosis**; **Endpoints: DNA Undetect → HBeAg Seroconversion → HBsAg Loss (Functional Cure)**; **Prevention: Vaccine (0,1,6m / Heplisav-B 0,1m); PEP: HBIG+Vaccine**
- **HCV**: **RNA Virus, GT1-8, Quasispecies**; **Diagnosis: Anti-HCV → HCV RNA PCR (+=Current, -=Past Clearance)**; **Treatment: Pan-Genotypic DAAs — SOF/VEL 12w, GLE/PIB 8w (12w GT3 Cirrhosis), SOF/DCV 12w**; **SVR12 = Cure (>95%)**; **No Vaccine; Prevention: Harm Reduction, Treat Partners (TasP)**
- **Sexual Transmission**: **HBV HIGH (100x HIV — Semen, Vaginal Fluids, Blood)**; **HCV LOW (~1-3%) — Exception: MSM with HIV/PrEP/Trauma/STIs**
- **Special Populations**: **HIV: TDF/TAF in ART covers HBV; DAAs + ART Check DDIs (SOF/VEL/GLE/PIB OK)**; **Pregnancy: HBV DNA>200,000 → TAF/TDF from 28w; Infant HBIG+Vaccine <12h; HCV: Defer DAAs**; **Renal: HBV→ETV (Dose Adj); HCV→GLE/PIB/GZR/EBR (No Adj), Avoid SOF**; **HBV Reactivation: Screen Anti-HBc Pre-Immunosuppression; High Risk (Anti-CD20, SCT, High-Dose Steroids) → NUC Prophylaxis 12m Post**

---

## 11. ❓ MCQs (10)

1. **HBV Serology Pattern for Resolved Natural Infection (Immunity)?**  
   A. HBsAg+, Anti-HBs+, Anti-HBc+  B. **HBsAg-, Anti-HBs+, Anti-HBc+**  C. Anti-HBs+ Only  D. HBsAg+, Anti-HBc IgM+  
   *Answer: B. HBsAg Negative, Anti-HBs Positive, Anti-HBc Positive = Resolved Infection with Immunity.*

2. **1st Line Nucleos(t)ide Analogue for Chronic HBV (Preferred for Renal/Bone Safety)?**  
   A. Lamivudine  B. Adefovir  C. **Tenofovir Alafenamide (TAF) 25mg OD**  D. Entecavir 0.5mg OD  
   *Answer: C. TAF 25mg OD — High Barrier, Better Renal/Bone Safety Profile than TDF.*

3. **HCV Diagnosis — Anti-HCV Positive, HCV RNA Negative. Interpretation?**  
   A. Acute HCV  B. **Past Infection (Spontaneous Clearance or Treated)**  C. Chronic HCV  D. False Positive Anti-HCV  
   *Answer: B. Anti-HCV+ / HCV RNA- = Past Exposure with Clearance (Spontaneous or Post-Treatment).*

4. **Pan-Genotypic DAA Regimen with Shortest Duration (Non-Cirrhotic)?**  
   A. SOF/VEL 12 Weeks  B. **GLE/PIB 8 Weeks**  C. SOF/DCV 12 Weeks  D. GZR/EBR 12 Weeks  
   *Answer: B. GLE/PIB 8 Weeks for Non-Cirrhotic (All Genotypes); Contraindicated in Decompensated Cirrhosis.*

5. **HBV Vertical Transmission Prevention — Maternal HBV DNA Threshold for Antiviral Prophylaxis?**  
   A. >2,000 IU/mL  B. >20,000 IU/mL  C. **>200,000 IU/mL**  D. >2,000,000 IU/mL  
   *Answer: C. Maternal HBV DNA >200,000 IU/mL at 28 Weeks → TAF/TDF Until 12 Weeks Postpartum.*

6. **HBV Reactivation Highest Risk — Which Immunosuppressive Therapy?**  
   A. Methotrexate  B. **Rituximab (Anti-CD20)**  C. Hydroxychloroquine  D. Intra-articular Steroids  
   *Answer: B. Anti-CD20 (Rituximab) / Stem Cell Transplant / High-Dose Steroids = Highest Risk (≥10%).*

7. **HCV Sexual Transmission — Highest Risk Group?**  
   A. Heterosexual Monogamous Couples  B. **MSM with HIV / PrEP / Trauma / STIs**  C. Lesbian Couples  D. Oral Sex Only  
   *Answer: B. MSM with HIV, PrEP Use, Traumatic Practices (Fisting, Toys), Multiple Partners, Concurrent STIs.*

7. **Preferred DAA in ESRD (CrCl <15) for HCV?**  
   A. SOF/VEL  B. **GLE/PIB (No Renal Adjustment)**  C. SOF/DCV  D. SOF/VEL/VOX  
   *Answer: B. GLE/PIB (or GZR/EBR) — No Renal Dose Adjustment; Sofosbuvir Contraindicated (Accumulation).*

8. **HBV Vaccine Schedule — Standard Adult?**  
   A. 0, 1 Month  B. 0, 1, 2 Months  C. **0, 1, 6 Months**  D. 0, 6, 12 Months  
   *Answer: C. Standard 3-Dose: 0, 1, 6 Months; Heplisav-B = 2-Dose (0, 1 Month).*

9. **HBeAg-Negative Chronic Hepatitis B — Treatment Indication?**  
   A. ALT Normal, HBV DNA 500  B. **ALT >ULN, HBV DNA >2,000 IU/mL**  C. ALT >2xULN, HBV DNA >20,000  D. Any Detectable DNA  
   *Answer: B. HBeAg-Neg CHB: ALT >ULN AND HBV DNA >2,000 IU/mL (EASL/APASL).*

---

## 12. 📋 SBAs (5)

1. **35-year-old man, HIV+ on TDF/FTC/DTG, diagnosed with Chronic HBV (HBsAg+, HBeAg-, Anti-HBe+, HBV DNA 5,000 IU/mL, ALT 85 U/L). Best Management?**  
   A. Add Entecavir  B. **Continue Current ART (TDF Covers HBV) — Monitor HBV DNA q3-6m**  C. Switch to TAF/FTC/DTG  D. Start PegIFN  
   *Answer: B. TDF in ART Provides Effective HBV Suppression; Monitor HBV DNA q3-6m; No Additional HBV-Specific NUC Needed.*

2. **28-week Primigravida, HBsAg+, HBV DNA 500,000 IU/mL. Vertical Transmission Prevention?**  
   A. No Intervention  B. **TDF/TAF from 28 Weeks to 12 Weeks Postpartum + Infant HBIG + Vaccine <12h Birth**  C. Elective C-Section  D. Infant Vaccine Only  
   *Answer: B. Maternal HBV DNA >200,000 → TAF/TDF from 28w; Infant HBIG 0.06mL/kg + Vaccine (Separate Sites) <12h Birth.*

---

## 13. 🔑 Answer Keys
| MCQs | SBAs |
|------|------|
| 1-B, 2-C, 3-B, 4-B, 5-C, 6-B, 7-B, 8-B, 9-C, 10-B | 1-B, 2-B |

---

## 14. 🔗 Cross-Links
- [[3.4 Hepatitis B & C.md]] — Main Detailed Hepatitis Note (New Format)
- [[6. HIV-AIDS Cross-Reference.md]] — HBV/HCV in HIV
- [[Contact Tracing and Partner Notification.md]] — PN (HBV: Long-term Partners; HCV: MSM/HIV Partners)
- [[Sexually Transmitted Infections MOC.md]] — Master Index

---

**Last Updated:** 2026-06-15  
**Version:** Full FCPS/MRCP Template Upgrade