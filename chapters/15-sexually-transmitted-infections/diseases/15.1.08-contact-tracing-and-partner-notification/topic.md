**Parent Topic:** [STI MOC](../Sexually%20Transmitted%20Infections%20MOC.md) → [STI Hierarchy](../Davidson%20Chapter%2013%20-%20STI%20Hierarchy.md)  
**Status:** `full-fcps-mrcp-note`  
**Priority:** ⭐⭐⭐ HIGHEST (FCPS/MRCP — Core Public Health Skill, EPT, Lookback Periods, Cluster Management)  
**Source:** Davidson 24th Ed Ch 13; WHO/BASHH/CDC Guidelines; FCPS/MRCP Syllabus; NICE NG162

---

## 1. 🎯 Learning Objectives
- [ ] Define **Contact Tracing (Partner Notification)** and its role in STI control
- [ ] Apply **Lookback Periods** by STI type
- [ ] Differentiate **Partner Notification Methods** (Patient Referral, Provider Referral, Contract Referral)
- [ ] Apply **Expedited Partner Therapy (EPT)** principles, regimens, and legal framework
- [ ] Manage **Special Situations** (Anonymous partners, Clusters, Outbreaks, HIV Co-infection)
- [ ] Answer viva: "Partner notification methods" and "EPT indications" and "Lookback period for Syphilis" and "Cluster management"

---

## 2. 🧠 Core Concept: Partner Notification Framework

```mermaid
flowchart TD
    A[Index Patient Diagnosed with STI] --> B[Risk Assessment & Counselling]
    B --> C[Determine Lookback Period by STI]
    C --> D[Choose Notification Method]
    D --> D1[Patient Referral (Self)]
    D --> D2[Provider Referral (Health Dept)]
    D --> D3[Contract Referral (Hybrid)]
    D --> D4[EPT (Expedited Partner Therapy)]
    D1 & D2 & D3 & D4 --> E[Partners Tested & Treated]
    E --> F[Test of Cure / Follow-Up]
    F --> G[Re-infection Prevention & Re-screening]
    G --> H[Surveillance Data Entry]
```

---

## 1️⃣ Principles of Contact Tracing

| Principle | Description |
|-----------|-------------|
| **Confidentiality** | Index patient identity **never disclosed** to partners |
| **Timeliness** | Initiate **within 24-48h** of diagnosis |
| **Comprehensiveness** | **All partners** within lookback period |
| **Empathy/Non-judgemental** | Supportive counselling, reduce stigma |
| **Partner-Centred** | Offer testing/treatment **on-site or via EPT** |
| **Documentation** | Record **method, outcomes, partner count** for surveillance |
| **Integration** | **HIV/Syphilis co-testing** for all STI diagnoses |

---

## 2️⃣ Lookback Periods by STI

| STI | Symptomatic | Asymptomatic | Rationale |
|-----|-------------|--------------|-----------|
| **Gonorrhoea / Chlamydia / Trichomonas / Mycoplasma genitalium** | **60 Days** before symptom onset | **60 Days** before diagnosis | Short incubation, high infectivity |
| **Syphilis (Primary)** | **3 Months** + duration of symptoms | **3 Months** | Chancre incubation 3w-90d |
| **Syphilis (Secondary)** | **6 Months** + duration of symptoms | **6 Months** | Systemic dissemination period |
| **Syphilis (Early Latent <1 Year)** | — | **1 Year** | Seroconversion window |
| **Syphilis (Late Latent / Unknown Duration)** | — | **Long-term partners** (No fixed limit) | Potential long latency |
| **HSV (Symptomatic Episode)** | **60 Days** before episode | **60 Days** | Recurrence shedding period |
| **HPV (New Warts/Dysplasia)** | **6 Months** before detection | **6 Months** | Subclinical infection window |
| **Hepatitis B** | **6 Months** before symptoms | **6 Months** | Long incubation (60-150d) |
| **Hepatitis C** | **6 Months** before symptoms | **6 Months** (If sexual transmission suspected) | Variable incubation |
| **Mpox** | **21 Days** before symptom onset | **21 Days** | Incubation 5-21d |
| **HIV** | **Since last negative test** or **Indefinite** | **Since last negative test** or **Indefinite** | All sexual/needle-sharing partners |

> **Rule**: **Partner notification is MANDATORY for all notifiable STIs**; **Lookback based on incubation + infectivity window**

---

## 3️⃣ Partner Notification Methods

### Comparison

| Method | Description | Partner Treatment Rate | Resources Required | Best For |
|--------|-------------|------------------------|-------------------|----------|
| **Patient Referral (Self-Referral)** | Index patient informs partners themselves | **30-50%** | Low | Motivated patients, Low stigma, Few partners |
| **Provider Referral (Health Dept Notification)** | Trained staff notify partners confidentially | **70-90%** | High (Staff, Database) | **Syphilis, HIV, Clusters**, Anonymous partners |
| **Contract Referral (Conditional)** | Patient agrees to notify within 1-2 weeks; If not done, Provider does it | **50-70%** | Moderate | **Balanced approach**, Empowers patient with safety net |
| **EPT (Expedited Partner Therapy)** | **Patient delivers medication/prescription** to partners without clinical assessment | **70-90%** (Where legal) | Moderate (Med supply) | **Chlamydia, Gonorrhoea (where injection feasible), Trichomonas** |

> **Evidence**: **Provider Referral + EPT = Highest Partner Treatment Rates**; **Combination Approaches Optimal**

### Method Selection Algorithm

```mermaid
flowchart TD
    A[Index Patient] --> B{STI Type}
    B -->|Syphilis/HIV/Late Latent Syphilis/Clusters| C[Provider Referral (Mandatory)]
    B -->|GC/CT/TV/MG| D{Patient Preference & Capacity}
    D -->|Motivated, Few Partners| E[Patient Referral + EPT Offer]
    D -->|Anonymous/Cluster/Unmotivated| F[Provider Referral]
    D -->|Wants to Try Self First| G[Contract Referral (1-2 Week Deadline)]
    C & E & F & G --> H[Document Method & Outcomes]
```

---

## 4️⃣ Expedited Partner Therapy (EPT)

### EPT Regimens by STI

| STI | EPT Regimen | Feasibility | Notes |
|-----|-------------|-------------|-------|
| **Chlamydia** | **Doxycycline 100mg PO BD × 7d** or **Azithromycin 1g PO Stat** | **High (Oral, Simple)** | **Preferred EPT**; Azithro if Pregnant |
| **Gonorrhoea** | **Ceftriaxone 500mg IM + Azithromycin 1g PO** | **Low (Requires Injection)** | **Not Practical for EPT**; Provider Referral Preferred |
| **Trichomonas** | **Metronidazole 2g PO Stat** or **Tinidazole 2g PO Stat** | **High (Oral, Single Dose)** | Effective EPT |
| **M. genitalium** | **Moxifloxacin 400mg OD × 7-14d** | **Moderate (Resistance Testing Needed)** | **Not Standard EPT** (Resistance-guided) |
| **Syphilis** | **Not Suitable** | **None** | **Injection, Staging, CSF, Follow-Up Required** |
| **HSV / HPV** | **Not Suitable** | **None** | **Chronic/Recurrent, Not Curable by Single Course** |

### EPT Implementation Checklist

| Step | Action |
|------|--------|
| 1 | **Confirm Index Diagnosis** (Lab confirmed) |
| 2 | **Counsel Index** on partner notification importance |
| 3 | **Assess Partner Number/Accessibility** |
| 4 | **Provide EPT Pack** (Medication + Info Sheet + Allergy Warning + STI Testing Advice) |
| 5 | **Document** (Partner Count, Regimen Given, Lot Numbers) |
| 6 | **Advise Index** to encourage partners to seek full STI screen |
| 7 | **Follow-Up** Index at 2 weeks (Adverse Events, Partner Uptake) |

### EPT Legal Status (Key Jurisdictions)

| Jurisdiction | Chlamydia | Gonorrhoea | Trichomonas | Notes |
|--------------|-----------|------------|-------------|-------|
| **UK (England)** | **Legal** (PGD/PGD) | **Not Routine** (Injection) | Legal | BASHH Guidelines Support |
| **US (Most States)** | **Legal** (Varies by State) | **Legal in Some** (IM) | Legal | CDC Recommends for GC/CT |
| **Canada** | **Legal** (Provincial) | **Not Routine** | Legal | Provincial Variation |
| **Australia** | **Legal** (State-Based) | **Not Routine** | Legal | RACGP Supports |
| **WHO** | **Recommended** | **Conditional** (If Feasible) | Recommended | Global Strategy 2016-2021 |

---

## 5️⃣ Special Situations

### Anonymous Partners / Digital Contacts
| Scenario | Management |
|----------|------------|
| **Apps/Websites (Grindr, Tinder, etc.)** | Use **in-app notification features** (Anonymous); **Provider Referral** via health dept if platform cooperates |
| **One-night Stands / No Contact Info** | **EPT** if chlamydia; **Document** "Anonymous Partner — Unable to Notify" |
| **Sex Venues (Saunas, Clubs)** | **Venue-Based Notification** (Posters, Staff Alerts); **Outreach Testing** |

### Clusters & Outbreaks
| Trigger | Definition | Response |
|---------|------------|----------|
| **Cluster** | **≥3 Cases** linked epidemiologically (Time, Place, Person) | **Enhanced Surveillance**, **Contact Tracing Expansion**, **Molecular Typing (WGS/MLST)**, **Public Health Alert** |
| **Outbreak** | **Unexpected Increase** above baseline | **Incident Management Team**, **Media Communication**, **Mass Screening**, **Policy Review** |

### HIV Co-infection
- **All STI Diagnoses → Offer HIV Test** (Opt-out)
- **HIV+ Index → Enhanced PN** (Provider Referral Preferred)
- **PrEP Users → 3-Monthly STI Screen + PN for Each Positive**

### Pregnancy
- **Syphilis/GC/CT/HIV/HBV → Mandatory PN** (Provider Referral)
- **Congenital Prevention → Partner Treatment Critical**
- **EPT Azithromycin for CT** (Doxy Contraindicated)

---

## 6️⃣ Outcomes & Quality Indicators

### PN Outcome Categories
| Category | Definition |
|----------|------------|
| **Notified & Treated** | Partner informed, tested, treated |
| **Notified, Not Treated** | Partner informed, declined/testing pending |
| **Not Notifiable** | Outside lookback, already treated, partner deceased |
| **Unable to Notify** | No contact info, anonymous, refused |
| **Index Refused** | Patient declines all notification methods |

### Quality Indicators (BASHH/WHO)
| Indicator | Target |
|-----------|--------|
| **PN Initiated within 48h** | **>90%** |
| **Partners Treated per Index** | **>0.8 (GC), >0.6 (CT)** |
| **EPT Utilisation (where legal)** | **>50% of Eligible CT Cases** |
| **Re-infection Rate at 3 Months** | **<10%** |
| **Cluster Detection Time** | **<2 Weeks** |

---

## 3. ⚡ FCPS/MRCP High-Yield Summary

| Topic | Key Points |
|-------|------------|
| **Definition** | Contact Tracing = Identifying, informing, testing, treating sexual partners of index STI patient |
| **Lookback Periods** | **GC/CT/TV/MG: 60d**; **Syphilis: 1°3m, 2°6m, Early Latent 1y, Late Latent Long-term**; **HSV/HPV: 60d/6m**; **Mpox: 21d**; **HIV: Since Last Negative/Indefinite** |
| **Notification Methods** | **Patient Referral (30-50%)**, **Provider Referral (70-90%)**, **Contract Referral (50-70%)**, **EPT (70-90%)** |
| **EPT Regimens** | **CT: Doxy BD×7d / Azi 1g**; **TV: Metro/Tini 2g Stat**; **GC: Not Practical (IM); Syphilis: No EPT** |
| **EPT Legal** | **Legal for CT/TV in UK/US/Canada/Aus**; **GC = Injection Barrier** |
| **Special Situations** | Anonymous Partners → Apps/EPT/Document; Clusters → WGS/Enhanced Surveillance; HIV+ → Provider Referral |
| **Quality Indicators** | PN <48h >90%; Partner Tx/Index >0.8(GC)/0.6(CT); Re-infection <10% at 3mo |
| **Viva** | "Syphilis lookback by stage", "EPT regimens & legal status", "Provider vs Patient referral", "Cluster management" |

---

## 4. 🎤 Viva Questions (Expected Answers)

| # | Question | Expected Answer |
|---|----------|-----------------|
| 1 | What are the lookback periods for partner notification for common STIs? | **GC/CT/TV/MG: 60 days**; **Syphilis 1°: 3m+Sx, 2°: 6m+Sx, Early Latent: 1y, Late Latent: Long-term**; **HSV: 60d; HPV: 6m; Mpox: 21d; HIV: Since last negative/Indefinite** |
| 2 | Compare partner notification methods — which has highest partner treatment rate? | **Provider Referral (70-90%) > EPT (70-90%) > Contract (50-70%) > Patient Referral (30-50%)**; **Combination approaches optimal** |
| 3 | What is Expedited Partner Therapy (EPT) and for which STIs is it recommended? | **Patient delivers medication to partners without clinical assessment**; **CT: Doxy BD×7d/Azi 1g; TV: Metro/Tini 2g**; **GC: Impractical (IM); Syphilis: Not suitable**; **Legal in UK/US/Can/Aus for CT/TV** |
| 4 | How do you manage partner notification for anonymous partners met on dating apps? | **In-app anonymous notification features**; **Provider Referral via Health Dept if platform cooperates**; **EPT for Chlamydia**; **Document "Anonymous Partner — Unable to Notify"** |
| 5 | What defines an STI cluster and how is it managed? | **≥3 Cases linked (Time/Place/Person)** → **Enhanced Surveillance, Contact Tracing Expansion, Molecular Typing (WGS/MLST), Public Health Alert**; **Outbreak = Unexpected Increase Above Baseline → Incident Management Team** |
| 6 | Syphilis partner notification — lookback by stage? | **Primary: 3 months + symptom duration**; **Secondary: 6 months + symptom duration**; **Early Latent (<1y): 1 year**; **Late Latent/Unknown: Long-term partners (No fixed limit)** |
| 7 | What are the key quality indicators for partner notification programmes? | **PN Initiated <48h (>90%)**; **Partners Treated/Index >0.8(GC)/>0.6(CT)**; **EPT Utilisation >50% (CT)**; **Re-infection Rate <10% at 3 Months**; **Cluster Detection <2 Weeks** |
| 8 | When is Provider Referral mandatory over Patient Referral? | **Syphilis (All Stages), HIV, Late Latent Syphilis, Clusters/Outbreaks, Anonymous Partners, Index Patient Refuses/Unable** |
| 9 | EPT for Gonorrhoea — why is it not routinely recommended? | **Requires Ceftriaxone IM Injection** — Not feasible for patient-delivered; **Safety (Allergy, Needle Injury)**; **Provider Referral Preferred**; **Dual Therapy Complexity** |
| 10 | Pregnant woman with Chlamydia — partner notification approach? | **Mandatory PN (Provider Referral Preferred)**; **EPT: Azithromycin 1g Stat (Doxy Contraindicated)**; **Congenital Prevention Critical**; **Partner Tested for Full STI Screen Including HIV/Syphilis** |

---

## 5. 🧩 Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **"EPT = For All STIs"** | **NO.** **CT/TV Oral Only (Legal)**; **GC = Injection (Impractical)**; **Syphilis = No EPT (Staging/CSF/Follow-Up)** |
| **"Lookback = Same for All STIs"** | **NO.** **Varies by Incubation/Infectivity**: **GC/CT 60d, Syphilis 3m-1y+, HIV Indefinite** |
| **"Patient Referral = Always Best"** | **NO.** **Lowest Completion (30-50%)**; **Provider Referral = Highest (70-90%)**; **Use Combination** |
| **"EPT = Legal Everywhere"** | **NO.** **Jurisdiction Dependent**; **Check Local Laws**; **UK/US/Can/Aus Legal for CT/TV** |
| **"Syphilis = 6 Months Lookback Always"** | **NO.** **Stage-Dependent: 1°3m, 2°6m, Early Latent 1y, Late Latent Long-Term** |
| **"Anonymous Partners = No PN Needed"** | **NO.** **Use App Features, EPT, Document Attempt**; **Cluster Risk if Multiple Anonymous** |
| **"Cluster = Just More Cases"** | **NO.** **Epidemiologically Linked (Time/Place/Person)**; **Requires Molecular Typing (WGS/MLST)** |
| **"Re-infection = Treatment Failure"** | **Often Re-infection from Untreated Partner**; **TOC + PN + Re-screen at 3mo Critical** |
| **"HIV PN = Same as Other STIs"** | **NO.** **Enhanced (Provider Referral Mandatory), All Sexual/Needle Partners Since Last Negative** |
| **"EPT = Replaces Partner Testing"** | **NO.** **EPT = Treatment Only**; **Partners Still Need Full STI Screen (HIV, Syphilis, etc.)** |

> **Mnemonic: PARTNER NOTICE MASTER**  
> **P**artner Notification = **Identify, Inform, Test, Treat** Sexual Partners of Index STI Patient  
> **A**ll Notifiable STIs = **Mandatory PN** (Legal Duty) → **Surveillance Integration**  
> **R** Lookback: **GC/CT/TV/MG 60d**; **Syph 1°3m/2°6m/EarlyLat1y/LateLat LT**; **HIV Indefinite**  
> **T** Methods: **Patient (30-50%) < Contract (50-70%) < Provider (70-90%) ≈ EPT (70-90%)**  
> **N** EPT Regimens: **CT Doxy BD×7d/Azi 1g; TV Metro/Tini 2g**; **GC No (IM); Syph No**  
> **E** EPT Legal: **UK/US/Can/Aus for CT/TV**; **Check Local Law**  
> **R** Provider Referral Mandatory: **Syph/HIV/Late Latent/Clusters/Anonymous/Refusal**  
> **A**nonymous Partners: **App Features, EPT (CT), Document "Unable to Notify"**  
> **C**lusters: **≥3 Linked (Time/Place/Person) → WGS/MLST + Enhanced PN + Public Alert**  
> **E** HIV Co-infection: **All STI Dx → HIV Test (Opt-Out); HIV+ → Enhanced PN (Provider)**  
> **Q**uality Indicators: **PN <48h >90%; Partner Tx/Idx >0.8(GC)/>0.6(CT); Re-inf <10%@3mo; Cluster <2wk**  
> **U** Pregnancy: **Mandatory PN (Syph/GC/CT/HIV/HBV); EPT Azi for CT; Congenital Prevention**  
> **I**ntegration: **STI/HIV/SRH Services One-Stop → Better PN Outcomes**  
> **R**e-screening: **3 Months Post-Tx All → Detects Re-infection (Partner Failure)**  
> **D**ocumentation: **Method, Partners Count, Outcomes, Lot Numbers → Surveillance/Legal**  
> **S**tructural: **Decriminalisation, Stigma Reduction → ↑ PN Completion, ↑ Access**  
> **T**echnology: **Digital PN Apps, In-App Notifications, Automated Reminders**  
> **O**utbreak Management: **IMT + Media + Mass Screen + Policy Review**  
> **W**HO Targets: **90% PN Coverage Key Pops; Integrated STI/HIV Services**  
> **H**arm Reduction: **PWID → PN Includes Needle-Sharing Partners**  

---

## 6. 🗺️ Mind Map

```mermaid
mindmap
  root((Partner Notification))
    Principles
      Confidentiality (Index Identity Protected)
      Timeliness (<48h)
      Comprehensiveness (All Partners in Lookback)
      Empathy/Non-judgemental
    Lookback Periods
      GC/CT/TV/MG: 60 Days
      Syphilis: 1°3m, 2°6m, EarlyLat1y, LateLat LT
      HSV: 60d, HPV: 6m, Mpox: 21d
      HIV: Since Last Negative/Indefinite
    Methods
      Patient Referral (Self) - 30-50%
      Provider Referral (Health Dept) - 70-90%
      Contract Referral (Hybrid) - 50-70%
      EPT (Expedited) - 70-90%
    EPT
      CT: Doxy BD×7d / Azi 1g
      TV: Metro/Tini 2g
      GC: Impractical (IM)
      Syphilis: Not Suitable
      Legal: UK/US/Can/Aus (CT/TV)
    Special Situations
      Anonymous/Apps: In-App Alerts, EPT, Document
      Clusters: ≥3 Linked → WGS + Enhanced PN
      HIV+: Provider Referral Mandatory
      Pregnancy: Mandatory PN, EPT Azi for CT
    Quality Indicators
      PN <48h >90%
      Partner Tx/Idx >0.8/>0.6
      Re-infection <10%@3mo
      Cluster Detection <2wk
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
| Lookback Periods by STI | 4 | | |
| Notification Methods (Comparison) | 3 | | |
| EPT (Regimens, Legal, Limitations) | 4 | | |
| Special Situations (Anonymous, Clusters, HIV, Pregnancy) | 4 | | |
| Quality Indicators & Outcomes | 2 | | |
| Viva Readiness | 3 | | |
| **Total** | **20** | | |

---

## 9. 💬 Exam Answer Modes

| Format | Prompt | Key Points |
|--------|--------|------------|
| **Long Essay** | "Describe the principles, methods, and quality indicators of partner notification for STIs." | **Principles: Confidentiality, Timeliness (<48h), Comprehensiveness**; **Lookback: GC/CT/TV 60d, Syphilis Stage-Dependent (1°3m/2°6m/EarlyLat1y/LateLat LT), HIV Indefinite**; **Methods: Patient (30-50%), Provider (70-90%), Contract (50-70%), EPT (70-90%)**; **EPT: CT Doxy BD×7d/Azi 1g, TV Metro/Tini 2g, GC Impractical (IM), Syphilis Not Suitable**; **Legal: UK/US/Can/Aus for CT/TV**; **Special: Anonymous/Apps (In-App/EPT/Document), Clusters (≥3 Linked→WGS/Enhanced PN), HIV+ (Provider Mandatory), Pregnancy (Mandatory PN, EPT Azi for CT)**; **Quality: PN<48h>90%, Partner Tx/Idx>0.8/0.6, Re-inf<10%@3mo, Cluster<2wk** |
| **Short Note** | "Expedited Partner Therapy (EPT) — indications, regimens, and limitations." | **Definition: Patient-Delivered Medication to Partners Without Clinical Assessment**; **Indications: CT, TV (Oral, Simple)**; **Regimens: CT Doxy 100mg BD×7d / Azi 1g Stat; TV Metro 2g/Tini 2g Stat**; **Not For: GC (IM Injection), Syphilis (Staging/CSF/Follow-Up), HSV/HPV (Chronic)**; **Legal: Permitted UK/US/Can/Aus for CT/TV**; **Limitations: No Partner Testing (HIV/Syphilis Missed), Allergy Risk, Adherence Unknown, Legal Barriers (Some Jurisdictions)** |
| **Viva** | "Syphilis partner notification — lookback periods by stage." | **Primary: 3 Months + Duration of Symptoms (Chancre Incubation 3w-90d)**; **Secondary: 6 Months + Duration of Symptoms (Systemic Dissemination)**; **Early Latent (<1 Year): 1 Year (Seroconversion Window)**; **Late Latent/Unknown Duration: Long-Term Partners (No Fixed Limit) — Assess Risk Individually** |
| **Ward Round** | "MSM diagnosed with gonorrhoea. 5 Grindr contacts — no names, only profiles. Management?" | **EPT Not Feasible for GC (Requires Ceftriaxone IM)**; **Use Grindr In-App Anonymous Notification Feature**; **Provider Referral via Health Dept if Platform Cooperates**; **Document "Anonymous Partners — Unable to Notify Individually"**; **Index: Full STI Screen (HIV, Syphilis, CT, HCV), TOC if Pharyngeal/Rectal**; **Cluster Assessment: If ≥3 Linked → Molecular Typing (WGS), Public Health Alert** |
| **Last-Night** | "PN: Principles (Confid, <48h, All Partners). Lookback: GC/CT/TV 60d, Syph 1°3m/2°6m/EarlyLat1y/LateLat LT, HIV Indef. Methods: Pt Ref 30-50% < Contr 50-70% < Prov Ref 70-90% ≈ EPT 70-90%. EPT: CT Doxy BD×7d/Azi 1g, TV Metro/Tini 2g, GC No (IM), Syph No. Legal: UK/US/Can/Aus CT/TV. Special: Anonymous→App/EPT/Document, Cluster≥3→WGS/Enhanced PN, HIV+→Provider Mandatory, Preg→Mandatory+EPT Azi. Quality: PN<48h>90%, Partner Tx/Idx>0.8/0.6, Re-inf<10%@3mo." | Compressed. |

---

## 10. 📌 Summary
- **Contact Tracing** = **Identify, Inform, Test, Treat** sexual partners; **Mandatory for All Notifiable STIs**
- **Lookback Periods**: **GC/CT/TV/MG 60d**; **Syphilis: 1°3m+Sx, 2°6m+Sx, Early Latent 1y, Late Latent Long-term**; **HSV 60d, HPV 6m, Mpox 21d, HIV Indefinite**
- **Notification Methods**: **Patient Referral (30-50%) < Contract Referral (50-70%) < Provider Referral (70-90%) ≈ EPT (70-90%)**
- **EPT Regimens**: **CT: Doxy 100mg BD×7d / Azi 1g Stat**; **TV: Metronidazole/Tinidazole 2g Stat**; **GC: Impractical (IM); Syphilis: Not Suitable**
- **EPT Legal**: **UK/US/Canada/Australia for CT/TV**; **Check Local Laws**
- **Provider Referral Mandatory**: **Syphilis (All Stages), HIV, Clusters, Anonymous Partners, Index Refusal**
- **Special**: **Anonymous/Apps → In-App Alerts + EPT + Document**; **Clusters (≥3 Linked) → WGS/MLST + Enhanced PN + Alert**; **HIV+ → Provider Referral + All Sexual/Needle Partners**
- **Quality Indicators**: **PN <48h >90%; Partners Treated/Index >0.8(GC)/0.6(CT); Re-infection <10% at 3mo; Cluster Detection <2 Weeks**
- **Pregnancy**: **Mandatory PN (Syph/GC/CT/HIV/HBV); EPT Azithromycin for CT; Congenital Prevention Critical**

---

## 11. ❓ MCQs (10)

1. **Standard lookback period for Chlamydia partner notification?**  
   A. 30 Days  B. **60 Days**  C. 90 Days  D. 1 Year  
   *Answer: B. 60 Days before symptom onset or diagnosis.*

2. **Partner notification method with HIGHEST partner treatment rate?**  
   A. Patient Referral  B. Contract Referral  C. **Provider Referral**  D. All Equal  
   *Answer: C. Provider Referral (70-90%) — Confidential, Professional, Systematic.*

3. **EPT regimen for Chlamydia in non-pregnant adult?**  
   A. Ceftriaxone 500mg IM  B. **Doxycycline 100mg BD × 7 Days**  C. Metronidazole 2g Stat  D. Azithromycin 1g Weekly × 3  
   *Answer: B. Doxycycline 100mg BD × 7d (or Azithromycin 1g Stat).*

4. **EPT for Gonorrhoea — why NOT routinely recommended?**  
   A. Illegal Everywhere  B. **Requires Ceftriaxone IM Injection (Not Feasible for Patient-Delivered)**  C. Ineffective  D. Resistance  
   *Answer: B. Ceftriaxone IM Required — Injection Barrier, Safety, Legal Complexity; Provider Referral Preferred.*

5. **Syphilis (Secondary) — partner notification lookback?**  
   A. 3 Months  B. **6 Months + Duration of Symptoms**  C. 1 Year  D. Indefinite  
   *Answer: B. 6 Months + Duration of Symptoms (Systemic Dissemination Period).*

6. **Anonymous partners met on dating apps — best notification approach?**  
   A. Ignore  B. **In-App Anonymous Notification + EPT if CT + Document**  C. Police Report  D. Provider Referral Only  
   *Answer: B. Use App Features (Grindr/Tinder Anonymous Notify), EPT for CT, Document "Unable to Notify Individually".*

7. **What defines an STI cluster requiring enhanced response?**  
   A. >10 Cases in a Month  B. **≥3 Cases Epidemiologically Linked (Time, Place, Person)**  C. >50% Increase Yearly  D. Any Drug-Resistant Case  
   *Answer: B. ≥3 Cases Linked by Time/Place/Person → Enhanced Surveillance, WGS/MLST, Public Health Alert.*

8. **Quality indicator — Target for PN initiated within 48 hours?**  
   A. >70%  B. **>90%**  C. >50%  D. 100%  
   *Answer: B. >90% of Index Cases Should Have PN Initiated Within 48 Hours.*

8. **HIV+ patient diagnosed with Gonorrhoea — partner notification method?**  
   A. Patient Referral Only  B. **Provider Referral (Mandatory for HIV Co-infection)**  C. EPT Only  D. No PN Needed  
   *Answer: B. HIV Co-infection → Enhanced PN with Provider Referral Mandatory; All Sexual/Needle Partners Since Last Negative.*

9. **Recommended EPT regimen for Trichomonas?**  
   A. Doxycycline 100mg BD × 7d  B. **Metronidazole 2g Stat or Tinidazole 2g Stat**  C. Azithromycin 1g Stat  D. Ceftriaxone 500mg IM  
   *Answer: B. Metronidazole 2g Single Dose or Tinidazole 2g Single Dose (Oral, Simple, Effective).*

---

## 12. 📋 SBAs (5)

1. **25-year-old woman with Chlamydia. 3 partners in 60 days — 1 regular (contactable), 2 anonymous (app only). Best PN approach?**  
   A. Patient Referral for All  B. **Provider Referral for Regular + EPT (Doxy BD×7d) for Regular; In-App Notify + EPT Pack for Anonymous**  C. EPT Only for All  D. No PN for Anonymous  
   *Answer: B. Regular Partner: Provider Referral (Best) or Patient Referral + EPT; Anonymous: In-App Notify + EPT Pack + Document.*

2. **Syphilis (Early Latent <1 year) diagnosed. Lookback period for PN?**  
   A. 3 Months  B. 6 Months  C. **1 Year**  D. Since Last Negative Test  
   *Answer: C. Early Latent Syphilis (<1 Year) → 1 Year Lookback.*

---

## 13. 🔑 Answer Keys
| MCQs | SBAs |
|------|------|
| 1-B, 2-C, 3-B, 4-B, 5-B, 6-B, 7-B, 8-B, 9-B, 10-B | 1-B, 2-B |

---

## 14. 🔗 Cross-Links
- [[7.1-7.4 Public Health & Control.md]] — Public Health Dashboard
- [[2.1 Chlamydia.md]] — Chlamydia PN & EPT
- [[2.2 Gonorrhoea.md]] — Gonorrhoea PN (No EPT)
- [[2.3 Syphilis.md]] — Syphilis PN (Stage-Specific Lookback)
- [[5.1-5.8 Syndromic Management.md]] — Syndrome PN Protocols
- [[6. HIV-AIDS Cross-Reference.md]] — HIV Enhanced PN
- [[Sexually Transmitted Infections MOC.md]] — Master Index

---

**Last Updated:** 2026-06-15  
**Version:** Full FCPS/MRCP Template Upgrade