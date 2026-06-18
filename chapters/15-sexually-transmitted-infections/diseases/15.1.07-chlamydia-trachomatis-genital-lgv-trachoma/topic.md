**Parent Topic:** [STI MOC](../Sexually%20Transmitted%20Infections%20MOC.md) → [STI Hierarchy](../Davidson%20Chapter%2013%20-%20STI%20Hierarchy.md)  
**Status:** `full-fcps-mrcp-note`  
**Priority:** ⭐⭐⭐ HIGHEST (FCPS/MRCP — Most Common Bacterial STI, LGV, Neonatal, Screening)  
**Source:** Davidson 24th Ed Ch 13; WHO/BASHH/CDC Guidelines; FCPS/MRCP Syllabus; NICE CG110

---

## 1. 🎯 Learning Objectives
- [ ] Recognise **Chlamydia trachomatis** clinical manifestations (Genital, LGV, Extra-genital, Neonatal)
- [ ] Apply **diagnostic algorithms** (NAAT, Culture, POC) and interpret results
- [ ] Apply **evidence-based treatment** (Doxycycline, Azithromycin, Amoxicillin in Pregnancy)
- [ ] Manage **LGV** (L1/L2/L3 Serovars) and **Extra-genital** infections (Pharyngeal, Rectal, Conjunctival)
- [ ] Manage **Neonatal** Chlamydia (Ophthalmia Neonatorum, Pneumonia)
- [ ] Implement **Screening, Partner Notification, Test of Cure** strategies
- [ ] Answer viva: "Chlamydia screening in pregnancy" and "LGV vs Classic Chlamydia" and "Test of Cure timing"

---

## 2. 🧠 Core Concept: Chlamydia trachomatis Biology & Pathogenesis

```mermaid
flowchart TD
    A[Chlamydia trachomatis] --> B[Obligate Intracellular Bacterium]
    B --> C[Developmental Cycle]
    C --> C1[Elementary Body (EB) — Infectious, Metabolically Inert]
    C --> C2[Reticulate Body (RB) — Replicative, Metabolically Active]
    C1 --> C2[Entry → Endosome → RB]
    C2 --> C1[Replication → EB Release → Cell Lysis]
    B --> D[Serovars]
    D --> D1[A-K: Genital (D-K), Trachoma (A-C)]
    D --> D2[L1/L2/L3: Lymphogranuloma Venereum (LGV)]
    B --> E[Pathogenesis]
    E --> E1[Intracellular Replication → Cell Death → Inflammation]
    E --> E2[Heat Shock Protein 60 → Autoimmunity (Reactive Arthritis, Tubal Damage)]
```

---

## 1️⃣ Serovars & Disease Spectrum

| Serovar Group | Disease | Target Population |
|---------------|---------|-------------------|
| **A, B, Ba, C** | **Trachoma** (Conjunctivitis → Scarring → Blindness) | **Endemic areas (Africa, Middle East, Asia)**; Children → Adults |
| **D to K** | **Genital Infection** (Urethritis, Cervicitis, PID, Proctitis, Pharyngitis) | **Sexually active worldwide**; Most common bacterial STI |
| **L1, L2, L3** | **Lymphogranuloma Venereum (LGV)** | **MSM (Proctitis outbreaks)**, Heterosexual in tropics |

> **Key**: **D-K = Genital STI**; **L1-L3 = LGV (Invasive, Systemic)**; **A-C = Trachoma (Ocular)**

---

## 2️⃣ Clinical Manifestations

### Genital Infection (Serovars D-K)

| Population | Asymptomatic | Symptomatic Presentation |
|------------|--------------|-------------------------|
| **Women** | **70-80%** | **Cervicitis**: Mucopurulent discharge, cervical friability, contact bleeding; **Urethritis**: Dysuria, frequency; **PID**: Lower abdominal pain, adnexal tenderness, cervical motion tenderness |
| **Men** | **50%** | **Urethritis**: Mucopurulent discharge, dysuria, urethral itch; **Epididymo-orchitis**: Unilateral testicular pain, swelling; **Proctitis**: Rectal pain, discharge, tenesmus (MSM) |
| **Both** | — | **Pharyngitis**: Usually asymptomatic; **Conjunctivitis**: Adult inclusion conjunctivitis |

### Lymphogranuloma Venereum (LGV) — Serovars L1/L2/L3

```mermaid
flowchart TD
    A[LGV Infection] --> B[Stage 1: Primary<br/>Transient painless papule/ulcer at inoculation site<br/>Often missed, heals spontaneously<br/>3-12 days post-exposure]
    B --> C[Stage 2: Secondary<br/>Regional lymphadenopathy (Buboes)<br/>Inguinal/femoral (Unilateral/Bilateral)<br/>Groove sign (Inguinal + Femoral separation)<br/>Systemic: Fever, malaise, arthralgia<br/>2-6 weeks post-primary]
    C --> D[Stage 3: Tertiary<br/>Chronic inflammation → Fibrosis/Strictures<br/>Anorectal strictures, fistulas, rectal stenosis<br/>Genital elephantiasis (Esthiomene)<br/>Months to years]
```

| LGV Syndrome | Population | Key Features |
|--------------|------------|--------------|
| **Anorectal LGV (L2b)** | **MSM (Outbreaks 2003+)** | Proctitis: Rectal pain, bloody discharge, tenesmus, fever; **Groove sign** (Inguinal + Femoral nodes); **Systemic symptoms common** |
| **Inguinal LGV** | Heterosexual (Tropics) | Unilateral tender inguinal buboes; Groove sign; Genital ulcer (often healed) |
| **Pharyngeal LGV** | Rare | Sore throat, cervical lymphadenopathy |

### Neonatal Chlamydia

| Condition | Timing | Presentation | Complications |
|-----------|--------|--------------|---------------|
| **Ophthalmia Neonatorum** | **5-14 Days** | Purulent conjunctivitis, eyelid swelling | Corneal scarring, blindness (**if untreated**) |
| **Pneumonia** | **3-12 Weeks** | Staccato cough, tachypnoea, hypoxemia, **no fever**; Bilateral diffuse infiltrates | Chronic lung disease |

---

## 3️⃣ Diagnostic Algorithms

### Testing Hierarchy

```mermaid
flowchart TD
    A[Clinical Suspicion] --> B{Test Available?}
    B -->|Yes| C[NAAT — Gold Standard]
    C --> C1[Urine (M/F): First-catch 20mL]
    C --> C2[Vaginal Swab (F): Self- or clinician-collected]
    C --> C3[Urethral Swab (M): Dacron/rayon]
    C --> C4[Rectal/Pharyngeal Swab: If exposure]
    C --> C5[Conjunctival Swab: Neonatal/Eye]
    B -->|No| D[Empirical Tx + Partner Notification]
    C --> E[Positive NAAT → Treat + PN + TOC if Pregnant/Rectal/Pharyngeal]
    C --> F[Negative NAAT → Consider other causes / Repeat if high suspicion]
```

| Test | Specimen | Sensitivity | Specificity | Turnaround | Notes |
|------|----------|-------------|-------------|------------|-------|
| **NAAT (PCR, TMA, SDA)** | Urine (M/F), Vaginal, Urethral, Rectal, Pharyngeal, Conjunctival | **95-99%** | **>99%** | **1-24h** | **Gold Standard**; Self-collected vaginal = best for women |
| **Culture** | Urethral, Cervical, Rectal, Conjunctival | 70-85% | 100% | 2-3 days | **LGV typing requires culture**; Legal evidence |
| **POC NAAT** (e.g., GeneXpert) | Urine, Swabs | 90-95% | >98% | **30-90 min** | Point-of-care; More expensive |
| **Antigen Detection (DFA/EIA)** | Conjunctival, Cervical | 70-85% | 90-95% | Hours | **Obsolete**; Lower sensitivity than NAAT |
| **Serology (MIF)** | Serum | Variable | Variable | Days | **LGV diagnosis (L1/L2/L3 specific IgG >1:64)**; Not for genital |

---

## 4️⃣ Treatment Regimens

### Genital Infection (D-K Serovars)

| Population | 1st Line | Alternative | Duration | Notes |
|------------|----------|-------------|----------|-------|
| **Non-Pregnant Adults/Adolescents** | **Doxycycline 100mg PO BD** | **Azithromycin 1g PO Stat** | **7 Days** | Doxy preferred (higher rectal efficacy); Avoid dairy/antacids with doxy |
| **Pregnant** | **Azithromycin 1g PO Stat** | **Amoxicillin 500mg PO TDS × 7d** | Single / 7d | Doxy contraindicated; Erythromycin less effective + GI side effects |
| **Immunocompromised / HIV** | **Doxycycline 100mg PO BD × 7d** | **Azithromycin 1g PO Stat** | 7d / 1d | Same as non-pregnant; Monitor TOC |
| **Rectal/Pharyngeal (All)** | **Doxycycline 100mg PO BD × 7d** | — | **7d** | Azithro less effective for rectal; **7d doxy preferred for rectal** |
| **PID (with GC coverage)** | **Ceftriaxone 500mg IM + Doxycycline 100mg BD × 14d (+ Metronidazole)** | — | **14d** | See PID syndrome management |

### LGV (L1/L2/L3 Serovars)

| Stage | Regimen | Duration |
|-------|--------|----------|
| **All Stages** | **Doxycycline 100mg PO BD** | **21 Days** (3 Weeks) |
| **Alternative** | **Azithromycin 1g PO Weekly × 3 Weeks** | 3 Weeks |
| **Pregnant** | **Azithromycin 1g PO Weekly × 3 Weeks** | 3 Weeks |
| **Severe/Systemic** | Add **IV Ceftriaxone** if sepsis suspected | — |

> **Critical**: **LGV = 21 Days Doxycycline (not 7d)**; **Rectal LGV requires 21d**; **Azithro weekly × 3 if pregnant**

### Neonatal

| Condition | Regimen | Duration |
|-----------|---------|----------|
| **Ophthalmia Neonatorum** | **Azithromycin 20mg/kg PO OD** | **3 Days** (or Erythromycin 50mg/kg/d ÷4 × 14d) |
| **Pneumonia** | **Azithromycin 20mg/kg PO OD** | **3-5 Days** (or Erythromycin 50mg/kg/d ÷4 × 14d) |
| **Prophylaxis (Born to Chlamydia+ Mother)** | **Not Routine** (Treat only if confirmed) | — |

---

## 5️⃣ Test of Cure (TOC) & Follow-Up

| Scenario | TOC Recommended? | Timing | Test |
|----------|------------------|--------|------|
| **Pregnancy** | **YES (Mandatory)** | **3-4 Weeks post-treatment** | NAAT |
| **Rectal / Pharyngeal Infection** | **YES** | **3-4 Weeks** | NAAT |
| **LGV** | **YES** | **3-4 Weeks** | NAAT |
| **Symptoms Persist** | **YES** | **1-2 Weeks** | NAAT |
| **Re-infection Risk High** | **YES** | **3 Months** | NAAT |
| **Uncomplicated Genital (Low Risk)** | **NO** (Routine TOC not needed) | — | — |

> **Rule**: **TOC if Pregnant, Rectal, Pharyngeal, LGV, Persistent Symptoms, or High Re-infection Risk**; **3 Month Re-screen for All**

---

## 6️⃣ Partner Notification & Screening

### Lookback Period
- **Symptomatic**: **60 Days** before symptom onset
- **Asymptomatic**: **60 Days** before diagnosis
- **Current Partners**: **All within last 60 days**

### Strategies
| Method | Description |
|--------|-------------|
| **Patient Referral** | Patient tells partners (Low completion) |
| **Provider Referral** | Health dept notifies (High completion) |
| **EPT (Expedited Partner Therapy)** | **Doxycycline 100mg BD × 7d** or **Azithromycin 1g Stat** given to patient for partners (Legal in many jurisdictions) |

### Screening Recommendations
| Population | Frequency |
|------------|-----------|
| **Sexually Active Women <25y** | **Annually** (or on partner change) |
| **Pregnant Women** | **Booking Visit** (Repeat 3rd Trimester if Risk) |
| **MSM** | **Annually** (3-Site: Urethral, Pharyngeal, Rectal) |
| **HIV+** | **Annually** (3-Site if MSM) |
| **Correctional/Detention** | **Entry + Periodic** |

---

## 7️⃣ Complications & Sequelae

| Complication | Population | Mechanism | Long-term Impact |
|--------------|------------|-----------|------------------|
| **PID** | Women | Ascending infection → Tubal inflammation | **Infertility (10-20%), Ectopic Pregnancy (↑ 6-10x), Chronic Pelvic Pain** |
| **Epididymo-orchitis** | Men | Ascending urethral infection | Subfertility (rare), Chronic pain |
| **Reactive Arthritis (Reiter's)** | Men > Women | HLA-B27 + Chlamydia HSP60 cross-reactivity | Arthritis, Conjunctivitis, Urethritis triad |
| **Perihepatitis (Fitz-Hugh-Curtis)** | Women | Spread to liver capsule | RUQ pain, Violin-string adhesions |
| **Neonatal Pneumonia/Conjunctivitis** | Neonates | Vertical transmission at delivery | Blindness (conjunctivitis), Chronic lung disease (pneumonia) |
| **Trachoma Blindness** | Endemic areas | Repeated A-C serovar infection → Conjunctival scarring → Trichiasis → Corneal opacity | **Leading infectious cause of blindness globally** |

---

## 3. ⚡ FCPS/MRCP High-Yield Summary

| Topic | Key Points |
|-------|------------|
| **Serovars** | **D-K = Genital**; **L1-L3 = LGV**; **A-C = Trachoma** |
| **Most Common Bacterial STI** | **Asymptomatic 70% women, 50% men** |
| **Diagnosis** | **NAAT = Gold Standard**; Urine (M/F), Vaginal swab (F), Rectal/Pharyngeal if exposure |
| **Treatment (Genital)** | **Doxycycline 100mg BD × 7d (1st line)**; **Azithromycin 1g Stat (Alt, Pregnant)** |
| **LGV Treatment** | **Doxycycline 100mg BD × 21d (3 Weeks)**; Azithro 1g weekly × 3 if pregnant |
| **Neonatal** | **Ophthalmia (5-14d): Azi 20mg/kg OD × 3d**; **Pneumonia (3-12w): Azi 20mg/kg OD × 3-5d** |
| **Test of Cure** | **Pregnant, Rectal, Pharyngeal, LGV, Persistent Sx → 3-4 weeks post-Tx**; Routine genital = No |
| **Screening** | **Women <25y Annual**; **Pregnant at Booking**; **MSM 3-Site Annual**; **HIV+ Annual** |
| **Partner Notification** | **60-day Lookback**; **EPT: Doxy BD×7d or Azi 1g Stat** |
| **Complications** | **PID → Infertility/Ectopic/Chronic Pain**; **Reactive Arthritis (HLA-B27)**; **Fitz-Hugh-Curtis**; **Trachoma Blindness** |

---

## 4. 🎤 Viva Questions (Expected Answers)

| # | Question | Expected Answer |
|---|----------|-----------------|
| 1 | Chlamydia serovars and associated diseases? | **D-K = Genital STI (Urethritis, Cervicitis, PID)**; **L1/L2/L3 = LGV (Invasive, Systemic, Anorectal in MSM)**; **A, B, Ba, C = Trachoma (Ocular, Endemic Blindness)** |
| 2 | Diagnostic test of choice for genital chlamydia? | **NAAT (PCR/TMA/SDA)** — **Urine (first-catch) for men, Vaginal swab (self/clinician) for women**; Sensitivity >95%, Specificity >99% |
| 3 | First-line treatment for uncomplicated genital chlamydia in non-pregnant adult? | **Doxycycline 100mg PO BD × 7 days** (Preferred over azithromycin due to higher rectal efficacy, lower resistance risk) |
| 4. Treatment for LGV? | **Doxycycline 100mg PO BD × 21 days (3 weeks)** — Longer than genital (7d); **Azithromycin 1g weekly × 3 weeks** alternative (esp. pregnancy) |
| 5. When is Test of Cure required? | **Pregnancy, Rectal/Pharyngeal infection, LGV, Persistent symptoms, High re-infection risk** — **3-4 weeks post-treatment**; Routine genital = not required |
| 6. Neonatal chlamydia — ophthalmia vs pneumonia timing and treatment? | **Ophthalmia: 5-14 days, Azi 20mg/kg OD × 3d**; **Pneumonia: 3-12 weeks, Staccato cough/afebrile, Azi 20mg/kg OD × 3-5d** |
| 7. Screening recommendations for chlamydia? | **Women <25y: Annual**; **Pregnant: Booking**; **MSM: 3-Site (Urethral, Pharyngeal, Rectal) Annual**; **HIV+: Annual** |
| 8. Partner notification lookback period? | **60 days** before symptom onset or diagnosis (symptomatic/asymptomatic); **EPT: Doxy BD×7d or Azi 1g Stat** |
| 9. Complications of untreated chlamydia in women? | **PID (10-30%) → Tubal factor infertility (10-20%), Ectopic pregnancy (↑6-10x), Chronic pelvic pain**; **Fitz-Hugh-Curtis (Perihepatitis)**; **Reactive arthritis (HLA-B27+)** |
| 10. LGV in MSM — clinical presentation? | **Anorectal proctitis: Rectal pain, bloody mucopurulent discharge, tenesmus, fever**; **Inguinal/femoral lymphadenopathy (Groove sign)**; **Systemic symptoms common**; **L2b serovar dominant in outbreaks** |

---

## 5. 🧩 Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **"Azithromycin = 1st line for everything"** | **NO.** **Doxycycline 7d = 1st line (Better rectal efficacy, less resistance)**; **Azithro = Pregnant/Alternative** |
| **"LGV = Just longer doxy"** | **YES, but 21d vs 7d**; **Also: Anorectal LGV needs 21d doxy; Azithro weekly × 3** |
| **"TOC needed for everyone"** | **NO.** **Only: Pregnant, Rectal, Pharyngeal, LGV, Persistent Sx, High Re-infection Risk** |
| **"Neonatal prophylaxis routine"** | **NO.** **Treat only if confirmed (NAAT+)**; No routine prophylaxis for exposed neonates |
| **"Trachoma = Same as genital chlamydia"** | **NO.** **Serovars A-C (Ocular)**; **Endemic blindness**; **SAFE Strategy (Surgery, Antibiotics, Facial cleanliness, Environment)** |
| **"Chlamydia can be cultured easily"** | **NO.** **Obligate intracellular**; **Culture only for LGV typing/legal**; **NAAT is standard** |
| **"M. genitalium = Chlamydia"** | **NO.** **Different organism**; **M. genitalium = NGU, Macrolide resistance common**; **Treat with Moxifloxacin if resistant** |

> **Mnemonic: CHLAMYDIA MASTER**  
> **C**hlamydia = **Obligate Intracellular**; **D**evelopmental Cycle **EB→RB→EB**  
> **H**igh Prevalence: **Most Common Bacterial STI**, **70%♀/50%♂ Asymptomatic**  
> **L**GV Serovars: **L1/L2/L3 (Invasive, Anorectal MSM, 21d Doxy)**; **Not 7d!**  
> **A**NAAT = **Gold Standard**; **Urine♂, Vaginal Swab♀, Rectal/Pharyngeal if Exposure**  
> **M**ost Common Tx: **Doxy 100mg BD × 7d (1st Line)**; **Azi 1g Stat (Alt/Pregnant)**  
> **Y**es TOC: **Pregnant, Rectal, Pharyngeal, LGV, Persistent Sx → 3-4 Weeks**  
> **D**oxy 7d Genital vs **21d LGV** — **Don't Confuse Duration!**  
> **I**n Pregnancy: **Azi 1g Stat (Genital)**; **Azi 1g Weekly × 3 (LGV)**; **No Doxy!**  
> **A**s Neonates: **Ophthalmia 5-14d (Azi 20mg/kg OD×3d)**; **Pneumonia 3-12w (Staccato Cough, Azi×3-5d)**  
> **D** Screening: **♀<25y Annual, Pregnant Booking, MSM 3-Site Annual, HIV+ Annual**  
> **P**artner Notification: **60-Day Lookback**; **EPT: Doxy BD×7d / Azi 1g**  
> **S**equelae: **PID→Infertility/Ectopic/Chronic Pain; Reactive Arthritis (HLA-B27); Fitz-Hugh-Curtis; Trachoma Blindness**

---

## 6. 🗺️ Mind Map

```mermaid
mindmap
  root((Chlamydia trachomatis))
    Biology
      Obligate Intracellular
      Developmental Cycle: EB ↔ RB
      Serovars: D-K (Genital), L1-L3 (LGV), A-C (Trachoma)
    Clinical
      Genital: Urethritis, Cervicitis, PID, Epididymitis, Proctitis
      LGV: 3 Stages (Ulcer → Buboes/Groove Sign → Fibrosis/Strictures)
      Neonatal: Ophthalmia (5-14d), Pneumonia (3-12w, Staccato Cough)
    Diagnosis
      NAAT (Gold Standard): Urine, Vaginal, Rectal, Pharyngeal
      Culture: LGV Typing, Legal
      POC NAAT: Rapid
    Treatment
      Genital: Doxy 100mg BD×7d (1st), Azi 1g Stat (Alt/Preg)
      LGV: Doxy 100mg BD×21d (3 Wks), Azi 1g Wkly×3
      Neonatal: Azi 20mg/kg OD×3-5d
      PID: Ceftriaxone + Doxy 14d + Metronidazole
    Follow-Up
      TOC: Pregnant, Rectal, Pharyngeal, LGV, Persistent Sx (3-4 Wks)
      Re-screen: 3 Months All
    Partner Notification
      60-Day Lookback
      EPT: Doxy BD×7d / Azi 1g
    Screening
      ♀<25y Annual, Pregnant Booking, MSM 3-Site Annual, HIV+ Annual
    Complications
      PID → Infertility, Ectopic, Chronic Pain
      Reactive Arthritis (HLA-B27)
      Fitz-Hugh-Curtis (Perihepatitis)
      Trachoma Blindness (SAFE Strategy)
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
| Biology & Serovars | 2 | | |
| Clinical Manifestations (Genital, LGV, Neonatal) | 4 | | |
| Diagnosis (NAAT, Culture, Specimens) | 2 | | |
| Treatment (Genital, LGV, Neonatal, Pregnancy) | 4 | | |
| TOC & Follow-Up | 2 | | |
| Partner Notification & Screening | 2 | | |
| Complications & Sequelae | 2 | | |
| Viva Readiness | 2 | | |
| **Total** | **20** | | |

---

## 9. 💬 Exam Answer Modes

| Format | Prompt | Key Points |
|--------|--------|------------|
| **Long Essay** | "Describe the clinical manifestations, diagnosis, and management of Chlamydia trachomatis infections including LGV and neonatal disease." | **Serovars (D-K Genital, L1-L3 LGV, A-C Trachoma)**; **Genital: Asymptomatic majority, Urethritis/Cervicitis/PID**; **LGV: 3 Stages (Ulcer, Buboes/Groove sign, Fibrosis); Anorectal in MSM**; **Neonatal: Ophthalmia 5-14d, Pneumonia 3-12w (Staccato cough)**; **Dx: NAAT Gold Standard (Urine♂, Vaginal Swab♀, Rectal/Pharyngeal if exposure)**; **Tx: Doxy 100mg BD×7d (1st), Azi 1g Stat (Preg/Alt); LGV Doxy×21d; Neonatal Azi 20mg/kg OD×3-5d**; **TOC: Pregnant, Rectal, Pharyngeal, LGV, Persistent Sx (3-4w)**; **Screening: ♀<25y Annual, Pregnant Booking, MSM 3-Site Annual**; **PN: 60d Lookback, EPT Doxy/Azi**; **Complications: PID→Infertility/Ectopic, Reactive Arthritis (HLA-B27), Fitz-Hugh-Curtis, Trachoma Blindness** |
| **Short Note** | "LGV — clinical stages and treatment." | **Serovars L1/L2/L3**; **Stage 1: Transient painless genital ulcer (missed)**; **Stage 2: Regional lymphadenopathy (Inguinal/Femoral → Groove sign), Systemic symptoms**; **Stage 3: Chronic fibrosis → Anorectal strictures, Fistulas, Elephantiasis**; **MSM: Anorectal proctitis (Rectal pain, bloody discharge, tenesmus, fever), L2b dominant**; **Tx: Doxycycline 100mg BD × 21 DAYS (not 7d); Azi 1g weekly × 3 if pregnant** |
| **Viva** | "Pregnant woman at 28 weeks tests positive for chlamydia on NAAT. Management?" | **Treat: Azithromycin 1g PO Stat (Doxy Contraindicated)**; **Partner Notification: 60-day Lookback, EPT (Azi 1g Stat for Partner)**; **Test of Cure: Mandatory at 3-4 Weeks Post-Tx (NAAT)**; **Re-screen: 3rd Trimester if Risk Factors**; **Neonatal: Assess at Delivery, Treat if Neonatal NAAT+** |
| **Ward Round** | "MSM with rectal pain, bloody discharge, tenesmus, fever. Inguinal lymphadenopathy. Diagnosis & Management?" | **Anorectal LGV (L2b)** — **NAAT (Chlamydia+) + LGV PCR/Serology**; **Dx Supported by Groove Sign (Inguinal+Femoral Nodes), Systemic Sx**; **Tx: Doxycycline 100mg BD × 21 DAYS**; **PN: 60-day Lookback, Test for HIV/Syphilis/GC/HSV**; **TOC at 3-4 Weeks** |
| **Last-Night** | "C. trachomatis: Serovars D-K Genital, L1-L3 LGV, A-C Trachoma. Dx: NAAT (Urine♂, Vaginal♀, Rectal/Pharyngeal). Tx: Doxy 100mg BD×7d (1st), Azi 1g Stat (Preg). LGV: Doxy×21d! Neonatal: Ophthalmia 5-14d Azi×3d, Pneumonia 3-12w Staccato Cough Azi×3-5d. TOC: Preg/Rectal/Phar/LGV/Persist→3-4w. Screen: ♀<25y Annual, Preg Booking, MSM 3-Site Annual, HIV+ Annual. PN: 60d Lookback, EPT Doxy/Azi. Complications: PID→Infertility/Ectopic, Reactive Arthritis HLA-B27, Fitz-Hugh-Curtis, Trachoma Blindness." | Compressed. |

---

## 10. 📌 Summary
- **Serovars**: **D-K = Genital STI**; **L1/L2/L3 = LGV (Invasive, Anorectal in MSM)**; **A-C = Trachoma (Ocular Blindness)**
- **Epidemiology**: **Most Common Bacterial STI**; **Asymptomatic 70% women, 50% men**
- **Diagnosis**: **NAAT = Gold Standard** (Urine ♂, Vaginal Swab ♀, Rectal/Pharyngeal if exposure)
- **Treatment (Genital)**: **Doxycycline 100mg BD × 7d (1st Line)**; **Azithromycin 1g Stat (Pregnant/Alternative)**
- **LGV Treatment**: **Doxycycline 100mg BD × 21 DAYS (3 Weeks)** — **NOT 7 days!**; **Azi 1g Weekly × 3 if Pregnant**
- **Neonatal**: **Ophthalmia (5-14d): Azi 20mg/kg OD × 3d**; **Pneumonia (3-12w, Staccato Cough): Azi 20mg/kg OD × 3-5d**
- **Test of Cure**: **Mandatory if Pregnant, Rectal, Pharyngeal, LGV, Persistent Symptoms → 3-4 Weeks Post-Tx**
- **Screening**: **Women <25y Annual; Pregnant at Booking; MSM 3-Site Annual; HIV+ Annual**
- **Partner Notification**: **60-Day Lookback; EPT: Doxy BD×7d or Azi 1g Stat**
- **Complications**: **PID → Infertility (10-20%), Ectopic (↑6-10x), Chronic Pain**; **Reactive Arthritis (HLA-B27)**; **Fitz-Hugh-Curtis**; **Trachoma Blindness (SAFE Strategy)**

---

## 11. ❓ MCQs (10)

1. **Chlamydia trachomatis serovars causing genital infection?**  
   A. A, B, C  B. **D to K**  C. L1, L2, L3  D. All serovars  
   *Answer: B. Serovars D-K cause genital infection; L1-L3 = LGV; A-C = Trachoma.*

2. **Gold standard diagnostic test for genital chlamydia?**  
   A. Culture  B. Serology  C. **NAAT (PCR/TMA/SDA)**  D. Gram Stain  
   *Answer: C. NAAT — Sensitivity >95%, Specificity >99%.*

3. **First-line treatment for uncomplicated genital chlamydia in non-pregnant adult?**  
   A. Azithromycin 1g Stat  B. **Doxycycline 100mg BD × 7 Days**  C. Ceftriaxone 500mg IM  D. Amoxicillin 500mg TDS × 7d  
   *Answer: B. Doxycycline 7 days is 1st line (better rectal efficacy, lower resistance); Azithro alternative.*

4. **LGV treatment duration with doxycycline?**  
   A. 7 Days  B. 14 Days  C. **21 Days (3 Weeks)**  D. 28 Days  
   *Answer: C. LGV requires 21 days doxycycline (vs 7d for genital); Azithro 1g weekly × 3 alternative.*

5. **When is Test of Cure mandatory after chlamydia treatment?**  
   A. All cases  B. **Pregnancy, Rectal/Pharyngeal infection, LGV, Persistent symptoms**  C. Only if symptoms persist  D. Never  
   *Answer: B. TOC mandatory for Pregnant, Rectal, Pharyngeal, LGV, Persistent Sx at 3-4 weeks; Routine genital = no.*

6. **Neonatal chlamydial pneumonia — typical age and presentation?**  
   A. 5-14 days, purulent conjunctivitis  B. **3-12 weeks, staccato cough, afebrile, bilateral infiltrates**  C. Birth, respiratory distress  D. 6 months, wheeze  
   *Answer: B. Pneumonia: 3-12 weeks, staccato cough, afebrile, tachypnoea, bilateral diffuse infiltrates.*

7. **Chlamydia screening — which group does NOT need annual screening?**  
   A. Sexually active women <25y  B. Pregnant women at booking  C. **Asymptomatic men >25y with no risk factors**  D. MSM  
   *Answer: C. Asymptomatic men >25y without risk factors not routinely screened; Women <25y, Pregnant, MSM (3-site) = Annual.*

8. **Partner notification lookback period for chlamydia?**  
   A. 30 Days  B. **60 Days**  C. 90 Days  D. 1 Year  
   *Answer: B. 60 days before symptom onset or diagnosis.*

8. **Complication of chlamydia PID — most characteristic triad for Reactive Arthritis?**  
   A. Arthritis, Rash, Fever  B. **Arthritis, Conjunctivitis, Urethritis**  C. Arthritis, Nephritis, Neuropathy  D. Arthritis, Carditis, Pleuritis  
   *Answer: B. Reactive Arthritis (Reiter's) = Arthritis + Conjunctivitis + Urethritis (HLA-B27 associated).*

9. **LGV in MSM — most common clinical presentation?**  
   A. Painless genital ulcer  B. **Anorectal proctitis (Rectal pain, bloody discharge, tenesmus, fever)**  C. Inguinal buboes only  D. Pharyngitis  
   *Answer: B. Anorectal LGV (L2b) = Proctitis with rectal pain, bloody mucopurulent discharge, tenesmus, fever, systemic symptoms.*

---

## 12. 📋 SBAs (5)

1. **24-year-old pregnant woman at 30 weeks: NAAT+ for Chlamydia. Best management?**  
   A. Doxycycline 100mg BD × 7d  B. **Azithromycin 1g PO Stat + TOC at 3-4 weeks + Partner EPT with Azithro 1g**  C. Ceftriaxone 500mg IM  D. No treatment until delivery  
   *Answer: B. Azithromycin 1g Stat (Doxy Contraindicated); TOC Mandatory 3-4w; PN with EPT (Azi 1g for Partner).*

2. **MSM with 2-week history rectal pain, bloody mucopurulent discharge, tenesmus, fever. Exam: Tender inguinal & femoral nodes (Groove sign). NAAT+ for Chlamydia. Next step?**  
   A. Azithromycin 1g Stat  B. **Doxycycline 100mg BD × 21 Days (LGV Regimen)**  C. Ceftriaxone 500mg IM + Doxy 7d  D. Doxycycline 100mg BD × 7d  
   *Answer: B. Clinical picture = Anorectal LGV → Doxycycline 21 days (not 7d).*

---

## 13. 🔑 Answer Keys
| MCQs | SBAs |
|------|------|
| 1-B, 2-C, 3-B, 4-C, 5-B, 6-B, 7-C, 8-B, 9-B, 10-B | 1-B, 2-B |

---

## 14. 🔗 Cross-Links
- [[2.1 Chlamydia.md]] — Main detailed Chlamydia note
- [[Urethritis Syndrome (Mucopurulent vs Non-Gonococcal).md]] — Syndromic approach
- [[Pelvic Inflammatory Disease (PID).md]] — Complication management
- [[Genital Ulcer Disease Syndrome (GUD).md]] — LGV differential
- [[Pelvic Inflammatory Disease (PID).md]] — Chlamydia PID treatment
- [[Contact Tracing and Partner Notification.md]] — PN strategies
- [[6. HIV-AIDS Cross-Reference.md]] — Chlamydia in HIV
- [[5.1-5.8 Syndromic Management.md]] — WHO Algorithms
- [[4.1-4.4 Parasitic & Fungal STIs.md]] — Co-infections

---

**Last Updated:** 2026-06-15  
**Version:** Full FCPS/MRCP Template Upgrade