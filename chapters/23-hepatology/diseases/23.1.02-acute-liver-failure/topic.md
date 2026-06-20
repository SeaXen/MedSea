> [!tip] **FCPS/MRCP Priority: HIGH** — ICU emergency; King's College Criteria, CLIF-C ACLF, transplant referral are core viva topics.

## 1. Scope
This heading covers **Acute Liver Failure (ALF)**, **Acute-on-Chronic Liver Failure (ACLF)**, the distinction between them, aetiology, prognostic scoring, and management including transplant referral.

## 2. Topic Groups & Disease-Level Topics

| Topic Group | Disease-Level Topics | Status |
|-------------|---------------------|--------|
| **Definition and Aetiology** | ALF vs ACLF, Paracetamol-induced hepatotoxicity, Non-paracetamol DILI, Acute viral hepatitis (A, B, E), Idiopathic/seronegative ALF, Wilson disease presenting as ALF, Autoimmune hepatitis presenting as ALF, Acute fatty liver of pregnancy | scaffold |
| **Clinical Assessment and Prognosis** | King's College Criteria, CLIF-C ACLF and ACLF grades, METAVIR and modified METAVIR | scaffold |
| **Management** | ICU supportive care, N-acetylcysteine therapy, Liver transplant referral and timing | scaffold |

## 3. High-Yield Viva Points

| Topic | Must-Know |
|-------|-----------|
| **ALF definition** | **INR ≥1.5 + any degree of encephalopathy** in patient **without pre-existing liver disease**, illness <26 weeks |
| **ACLF definition** | **Acute decompensation of chronic liver disease** with **organ failure(s)** (CLIF-C ACLF score) ± prior compensated cirrhosis |
| **ALF vs ACLF** | **ALF**: no prior liver disease, illness <26 weeks; **ACLF**: chronic liver disease + acute decompensation + organ failure(s) |
| **Common aetiologies** | **Paracetamol** (UK #1), **Idiopathic**, **Drug-induced** (non-paracetamol), **Viral** (A, B, E), **Autoimmune**, **Wilson**, **AFLP** |
| **King's College Criteria (Paracetamol)** | **pH <7.30** (arterial) **OR** **ALL THREE**: PT >100s (INR >6.5) + Cr >300 µmol/L + Grade III/IV HE |
| **King's College Criteria (Non-paracetamol)** | **PT >100s (INR >6.5)** **OR** **ANY THREE**: Age <10 or >40 + Aetiology (non-A, non-B hepatitis, halothane, idiosyncratic drugs) + Jaundice to encephalopathy >7 days + PT >50s (INR >3.5) + Bilirubin >300 µmol/L |
| **CLIF-C ACLF Score** | Organ failures: Liver (bil >12), Kidney (Cr >2 or RRT), Brain (HE grade III/IV), Coagulation (INR >2.5), Circulation (vasopressors), Respiration (PaO2/FiO2 <200 or SpO2/FiO2 <214 or MV) |
| **ACLF Grades** | Grade 1: 1 OF (kidney) or 1 OF (non-kidney) + Cr 1.5-1.9 or HE I-II; Grade 2: 2 OFs; Grade 3: ≥3 OFs |
| **Paracetamol NAC** | **IV 3-bag regimen**: 150mg/kg/1h → 50mg/kg/4h → 100mg/kg/16h (total 300mg/kg/21h); continue if INR improving/hepatic encephalopathy |
| **Transplant referral** | **Discuss early** (King's College met, or CLIF-C ACLF ≥2, or lactic acidosis, or renal failure, or sepsis) |

## 4. Key Algorithms

### ALF/ACLF Triage
```mermaid
flowchart TD
    A[Acute Liver Injury + Encephalopathy] --> B{Pre-existing Liver Disease?}
    B -->|No| C[ALF: Illness <26 weeks]
    B -->|Yes| D[ACLF: Chronic Liver Disease + Acute Decompensation]
    C --> C1[Aetiology?]
    C1 -->|Paracetamol| E1[King's College Criteria (Paracetamol)]
    C1 -->|Non-paracetamol| E2[King's College Criteria (Non-paracetamol)]
    C1 -->|Unknown| E3[Consider transplant early]
    D --> D1[Assess Organ Failures (CLIF-C ACLF)]
    D1 -->|Grade 1-2| F1[ICU Support + Treat Precipitant]
    D1 -->|Grade 2-3| F2[Transplant Assessment]
    E1 -->|Met| G1[Urgent Transplant Referral]
    E2 -->|Met| G1
    E3 --> G1
    E1 -->|Not met| H1[IV NAC + ICU Support]
    E2 -->|Not met| H2[ICU Support + Treat Aetiology]
```

### NAC Regimen (Paracetamol ALF)
| Phase | Dose | Duration |
|-------|------|----------|
| **Loading** | 150 mg/kg in 200ml 5% glucose | 1 hour |
| **Phase 2** | 50 mg/kg in 500ml 5% glucose | 4 hours |
| **Phase 3** | 100 mg/kg in 1000ml 5% glucose | 16 hours |
| **Total** | **300 mg/kg over 21 hours** | |
| **If ongoing risk** | Continue 100 mg/kg/16h | Until INR improving + encephalopathy resolving |

## 5. FCPS/MRCP High-Yield Summary

| Topic | Key Points |
|-------|------------|
| **ALF definition** | INR ≥1.5 + encephalopathy, no prior liver disease, illness <26 weeks |
| **ACLF definition** | Chronic liver disease + acute decompensation + organ failure (CLIF-C ACLF) |
| **Common causes** | Paracetamol (UK #1), Idiopathic, Non-paracetamol DILI, Viral (A, B, E), Autoimmune, Wilson, AFLP |
| **King's College (Paracetamol)** | pH <7.30 **OR** (PT >100s + Cr >300 + Grade III/IV HE) |
| **King's College (Non-paracetamol)** | PT >100s **OR** any 3 of: age <10/>40, non-A non-B aetiology, jaundice-HE >7d, PT >50s, bilirubin >300 |
| **NAC Regimen** | 150mg/kg/1h → 50mg/kg/4h → 100mg/kg/16h = 300mg/kg/21h (continue if INR/HE not improving) |
| **CLIF-C ACLF** | 6 organ systems (liver, kidney, brain, coagulation, circulation, respiration); score predicts 28-day mortality |
| **ACLF Grades** | Grade 1: 1 OF (kidney) or 1 OF + Cr 1.5-1.9/HE I-II; Grade 2: 2 OFs; Grade 3: ≥3 OFs |
| **Transplant referral** | Early if King's College met, CLIF-C ACLF ≥2, lactate >3.5, sepsis, renal failure |

## 6. Quick Reference Card

| Domain | Key Points |
|--------|------------|
| **ALF Definition** | INR ≥1.5 + HE, no prior liver disease, <26 weeks |
| **ACLF Definition** | Chronic liver disease + acute decompensation + organ failure |
| **King's College (Paracetamol)** | pH <7.3 **OR** (PT >100s + Cr >300 + Grade III/IV HE) |
| **King's College (Non-paracetamol)** | PT >100s **OR** 3 of: age<10/>40, non-A non-B, jaundice-HE >7d, PT>50s, bilirubin>300 |
| **NAC Protocol** | 150mg/kg/1h → 50mg/kg/4h → 100mg/kg/16h (continue if INR/HE not improving) |
| **CLIF-C ACLF** | 6 organ systems; score = 28-day mortality prediction |
| **ACLF Grades** | 1 OF (kidney) or 1 OF+Cr 1.5-1.9/HE I-II = Gr1; 2 OFs = Gr2; ≥3 OFs = Gr3 |
| **Transplant Referral** | KCC met, CLIF-C ACLF ≥2, lactate >3.5, renal failure, sepsis |

## 7. Local Navigation
- **Parent Heading**: [[../Hepatology|Hepatology]]
- **Chapter Map**: [[../Davidson Chapter 24 - Hepatology Hierarchy|Hepatology Hierarchy]]
- **Chapter MOC**: [[../Hepatology MOC|Hepatology MOC]]
- **Drug Reference**: [[../../Clinical Therapeutics and Good Prescribing|Drugs]]
- **Related**: [[Jaundice and LFT Interpretation]], [[Drug-Induced Liver Injury]], [[Viral Hepatitis]], [[Autoimmune Liver Disease]], [[Liver Transplantation]], [[Hepatology in Special Situations/Acute fatty liver of pregnancy|Acute fatty liver of pregnancy]], [[Inherited and Metabolic Liver Disease/Wilson disease|Wilson disease]]