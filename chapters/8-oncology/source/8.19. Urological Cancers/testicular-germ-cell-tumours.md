# Testicular Germ Cell Tumours (GCT)

> [!tip] **FCPS/MRCP Priority: HIGH**
> **Testicular cancer = most common solid tumour in men 15-45**; **Curable in >95%** (even metastatic). **Seminoma vs Non-seminoma (NSGCT)** = distinct management. **IGCCCG risk groups** (Good/Intermediate/Poor) guide metastatic therapy. **Stage I**: Seminoma → Surveillance/Carboplatin/RT; NSGCT → Surveillance/RPLND/BEP×1. **Metastatic**: **Good/Intermediate: BEP×3 (or EP×4)**; **Poor: BEP×4**. **Salvage**: High-dose chemo + ASCT (TIP/GEP) or Conventional (VeIP/VIP). **Late effects**: CVD, Second cancers, Hypogonadism, Neuropathy, Raynaud's, Fertility.

---

## 1. Learning Objectives
By the end of this note you should be able to:
- [ ] Distinguish **Seminoma** vs **Non-seminoma (NSGCT)** histology, markers, spread, treatment
- [ ] Apply **IGCCCG risk classification** for metastatic disease
- [ ] Manage **Stage I**: Surveillance vs Adjuvant (Carboplatin/RT for Seminoma; RPLND/BEP×1 for NSGCT)
- [ ] Prescribe **BEP chemotherapy** (Bleomycin, Etoposide, Cisplatin) with dose adjustments for bleomycin lung toxicity
- [ ] Know **RPLND** indications: Primary (NSGCT Stage I/IIA), Post-chemo residual mass
- [ ] Manage **Salvage therapy**: High-dose chemo + ASCT (standard) vs Conventional chemo
- [ ] Screen for **Late effects**: CVD, Second malignancies, Hypogonadism, Fertility, Neuropathy, Raynaud's

---

## 2. Definition & Epidemiology

| Feature | Detail |
|---------|--------|
| **Definition** | Malignant germ cell tumour of testis; **Seminoma (50-55%)** vs **Non-seminoma/NSGCT (45-50%)**; Mixed = treated as NSGCT |
| **Incidence** | UK: ~2,400/year; **Most common solid cancer in men 15-45**; Rising incidence |
| **Prevalence** | **>95% cure rate** overall; 5-year OS: Stage I >99%, Metastatic Good risk >90% |
| **Peak Age** | **Seminoma**: 35-45; **NSGCT**: 20-35; **Bimodal** (infants: yolk sac; 15-45: GCT; >60: spermatocytic) |
| **Sex Ratio** | Male only |
| **Risk Factors** | **Cryptorchidism** (↑3-5x, even after orchidopexy), **Prior GCT** (contralateral 2-5%), **Family history**, **GWAS loci** (KITLG, SPRY4, BAK1, DMRT1), **HIV**, **Hypospadias**, **Testicular microlithiasis** |

---

## 3. Aetiology & Pathophysiology

```mermaid
flowchart LR
    A[Primordial Germ Cell] --> B[GCNIS (Germ Cell Neoplasia In Situ)]
    B --> C1[Seminoma]
    B --> C2[Non-Seminoma (NSGCT)]
    C1 --> D1[Uniform cells, clear cytoplasm, central nuclei, LCD117+, PLAP+, OCT3/4+]
    C2 --> D2[Embryonal Carcinoma (EC) — Stem cell<br/>Yolk Sac Tumour (YST) — AFP+<br/>Choriocarcinoma — hCG+ (syncytiotrophoblasts)<br/>Teratoma — Somatic differentiation (mature/immature)<br/>Spermatocytic Tumour — Benign, older men]
    C2 --> E[Trophoblastic differentiation → hCG]
    C2 --> F[YST differentiation → AFP]
    D1 --> G[Lymphatic Spread (Predictable: Para-aortic → Iliac → Mediastinal → Supraclavicular)]
    C2 --> H[Lymphatic + Haematogenous (Lung, Liver, Brain, Bone)]
```

### Tumour Markers

| Marker | Seminoma | NSGCT | Half-life | Clinical Use |
|--------|----------|-------|-----------|--------------|
| **AFP** | **Never elevated** (if ↑ = NSGCT component) | ↑ in **YST** (70%) | 5-7 days | Diagnosis, Staging, Monitoring, Prognosis (IGCCCG) |
| **hCG** | ↑ in 10-15% (syncytiotrophoblasts) | ↑ in **Choriocarcinoma** & **EC** | 24-36 hours | Diagnosis, Staging, Monitoring, Prognosis |
| **LDH** | ↑ in bulky/advanced | ↑ in advanced | — | **IGCCCG Prognostic Factor** (surrogate for tumour burden) |

---

## 4. Clinical Features

| Feature | Description |
|---------|-------------|
| **Painless Testicular Lump** | **Most common (90%)**; Firm, non-tender, intra-testicular |
| **Pain/Discomfort** | 10-20% (haemorrhage, infarction, epididymo-orchitis) |
| **Gynaecomastia** | hCG → ↑ oestrogen (NSGCT with choriocarcinoma) |
| **Back Pain** | Retroperitoneal nodes (ureteric obstruction, IVC compression) |
| **Respiratory Symptoms** | Lung mets (cough, dyspnoea, haemoptysis) |
| **Neurological** | Brain mets (NSGCT, choriocarcinoma) |
| **Acute Scrotum** | Torsion, infection — **Always rule out tumour** |

---

## 5. Staging & Classification

| System | Detail |
|--------|--------|
| **TNM 8th Edition** | pT1: No LVI, tunica albuginea intact; pT2: LVI or tunica vaginalis; pT3: Spermatic cord; pT4: Scrotum |
| **S Stage (Serum Markers)** | S0: Normal; S1: AFP<1000, hCG<5000, LDH<1.5xULN; S2: AFP 1000-10000, hCG 5000-50000, LDH 1.5-10xULN; S3: >S2 |
| **Stage Grouping** | **Stage I**: pT1-4, N0, M0, S0<br/>**Stage II**: Any pT, N1-3, M0, S0-1<br/>**Stage III**: Any pT, Any N, M1, Any S |

### IGCCCG Risk Groups (Metastatic — Post-Orchidectomy Markers)

| Risk Group | Seminoma | Non-Seminoma |
|------------|----------|--------------|
| **Good** | **Any primary, No non-pulmonary visceral mets**, Normal AFP, Any hCG, Any LDH | **Testicular/Retroperitoneal primary, No non-pulmonary visceral mets**, **AFP <1000, hCG <5000, LDH <1.5xULN** |
| **Intermediate** | **Non-pulmonary visceral mets present** | **Testicular/Retroperitoneal primary, No non-pulmonary visceral mets**, **AFP 1000-10000 OR hCG 5000-50000 OR LDH 1.5-10xULN** |
| **Poor** | **Does not exist for Seminoma** | **Mediastinal primary OR Non-pulmonary visceral mets OR AFP >10000 OR hCG >50000 OR LDH >10xULN** |

**Key: Seminoma = ONLY Good or Intermediate (no Poor risk)**

---

## 6. Diagnosis & Investigations

| Investigation | Role | Key Findings |
|---------------|------|--------------|
| **Scrotal Ultrasound** | **First-line** — Confirm intra-testicular mass | Heterogeneous, hypoechoic, vascular; Rule out epididymal cyst |
| **Serum Markers (Pre-Orchidectomy)** | **AFP, hCG (β-hCG), LDH** — **Mandatory before orchidectomy** | Baseline for staging, prognosis (IGCCCG), monitoring |
| **Radical Inguinal Orchidectomy** | **Diagnostic + Therapeutic** — Never transscrotal | **Gold standard**; Histology (Seminoma vs NSGCT), LVI, Rete testis invasion |
| **CT Chest/Abdomen/Pelvis** | **Staging** — Nodal, Pulmonary, Visceral mets | **Lymph nodes >1cm short axis = suspicious** |
| **MRI** | Equivocal CT; Brain mets (NSGCT symptom) | Better soft tissue |
| **PET-CT** | **Not standard**; Residual mass post-chemo (Seminoma: >3cm residual → PET at 6-8wks) | FDG-avid = viable tumour |
| **Chest X-ray** | Baseline if CT not available | Less sensitive |

---

## 7. Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|-------------------------|
| **Epididymal Cyst / Spermatocele** | Cystic, transilluminates, separate from testis, asymptomatic |
| **Hydrocele** | Fluid collection, transilluminates, fluctuant; May obscure testis |
| **Epididymo-orchitis** | Acute pain, fever, tender, swollen epididymis; **Urinalysis + culture +ve** |
| **Testicular Torsion** | **Acute severe pain**, absent cremasteric reflex, high-riding testis; **Surgical emergency** |
| **Varicocele** | "Bag of worms", left-sided, increases with Valsalva |
| **Leydig / Sertoli Cell Tumour** | Rare, sex cord-stromal; May produce androgens/oestrogens; **AFP/hCG negative** |
| **Metastasis to Testis** | Older men; Known primary (Lung, Prostate, Melanoma, RCC); Bilateral common |

---

## 8. Management

### Stage I Seminoma (pT1-4, N0, M0, S0)

```mermaid
flowchart TD
    A[Stage I Seminoma post-Orchidectomy] --> B{Risk Factors for Relapse}
    B -->|**No risk factors**<br/>(pT1-2, no LVI, Tumour <4cm)| C[**Surveillance (Preferred)**<br/>CT Abd/Pelvis q3-6mo×2yr, then q6-12mo×3yr<br/>Chest X-ray annually ×5yr<br/>Markers q3-6mo ×5yr<br/>**Relapse rate ~15-20%**]
    B -->|**Risk factors**<br/>(pT3-4, LVI, Tumour ≥4cm)| D[**Adjuvant Options**]
    D --> D1[**Carboplatin AUC7 ×1 cycle**<br/>(NEAT/SAKK 9401) — **Preferred**<br/>Less toxicity, equivalent to RT]
    D --> D2[**Radiotherapy**<br/>Para-aortic ± Ipsilateral iliac (Dog-leg)<br/>20-30 Gy in 10-15 fractions<br/>**More late toxicity** (CVD, 2nd cancers)]
    D --> D3[**Surveillance** (Patient choice, compliance)]
```

### Stage I Non-Seminoma (pT1-4, N0, M0, S0)

```mermaid
flowchart TD
    A[Stage I NSGCT post-Orchidectomy] --> B{Risk Factors}
    B -->|**No LVI (pT1)**<br/>Relapse rate ~15%| C[**Surveillance (Preferred)**<br/>CT q2mo×1yr, q3mo×2yr, q6mo×2yr<br/>Markers q2mo×1yr, then q3mo<br/>Chest X-ray q6mo×5yr<br/>**High compliance required**]
    B -->|**LVI+ (pT2) or High-risk**<br/>Relapse rate ~50%| D[**Adjuvant Options**]
    D --> D1[**Primary RPLND**<br/>Nerve-sparing (preserve ejaculation)<br/>Pathological staging → guides chemo<br/>**Preferred if expertise available**]
    D --> D2[**BEP ×1 cycle**<br/>(SWENOTECA) — **Non-inferior to RPLND**<br/>Less morbidity, easier logistics]
    D --> D3[**Surveillance** (Selected, compliant)]
```

### Stage II (Nodal Mets)

```mermaid
flowchart TD
    A[Stage II] --> B{Histology}
    B -->|Seminoma| C[IIA/IIB (<3-5cm nodes): **Radiotherapy** (Para-aortic + Iliac) OR **Chemo (BEP×3/EP×4)**<br/>IIC (>5cm): **Chemo (BEP×3/EP×4)**]
    B -->|Non-Seminoma| D[IIA/IIB: **Primary RPLND** (if markers normalised) OR **BEP×3**<br/>IIC: **BEP×3** (or EP×4)]
```

### Metastatic (Stage III) — IGCCCG Risk-Adapted

```mermaid
flowchart TD
    A[Metastatic GCT] --> B{Risk Group (IGCCCG)}
    B -->|**Good Risk**<br/>Seminoma: Any primary, no non-pulm visceral, any markers<br/>NSGCT: Testicular/Retrop primary, no non-pulm visceral, S1 markers| C[**BEP ×3 cycles** (Standard)<br/>Bleomycin 30U d1,8,15 + Etoposide 100 d1-5 + Cisplatin 20 d1-5 q3w<br/>**OR EP ×4 cycles** (omit Bleomycin if >40yr/lung disease)<br/>**Cure rate >90%**]
    B -->|**Intermediate Risk**<br/>Seminoma: Non-pulmonary visceral mets<br/>NSGCT: Testicular/Retrop primary, S2 markers| D[**BEP ×4 cycles**<br/>**OR EP ×4 cycles** (if Bleomycin contraindicated)<br/>Cure rate ~80%]
    B -->|**Poor Risk**<br/>(NSGCT only): Mediastinal primary OR Non-pulm visceral OR S3 markers| E[**BEP ×4 cycles** (Standard)<br/>**Consider Clinical Trial / High-dose 1L**<br/>Cure rate ~50%]
```

### Post-Chemotherapy Residual Mass

| Histology | Size | Management |
|-----------|------|------------|
| **Seminoma** | **<3cm** | Surveillance (PET at 6-8wks if >3cm) |
| **Seminoma** | **>3cm** | **PET-CT at 6-8wks**: FDG+ → **Residual viable tumour** → **Salvage** (Surgery/High-dose chemo); FDG- → **Fibrosis/Necrosis** → Surveillance |
| **NSGCT** | **Any size** | **RPLND** (Post-chemo RPLND — technically difficult) → Pathology: **Necrosis** (80%) → Surveillance; **Teratoma** (10-15%) → Surveillance (chemo-resistant); **Viable NSGCT** (5-10%) → **Adjuvant Chemo** (2 cycles EP or VeIP) |

### Salvage Therapy (Relapsed/Refractory)

| Setting | Standard |
|---------|----------|
| **1st Relapse (Good/Int risk)** | **High-dose Chemo + ASCT** (TIP/GEP conditioning) — **Standard** (Superior to conventional) |
| **1st Relapse (Poor risk)** | **High-dose Chemo + ASCT** |
| **Late Relapse (>2yrs)** | **Surgery** (RPLND/Metastasectomy) if resectable; Teratoma common |
| **Refractory / 2nd+ Relapse** | **Conventional Salvage**: VeIP (Vinblastine/Ifosfamide/Cisplatin), VIP (Etoposide/Ifosfamide/Cisplatin), TIP (Paclitaxel/Ifosfamide/Cisplatin), GEMOX |
| **Brain Mets** | Surgery + RT ± Chemo (poor prognosis) |

---

## 9. FCPS/MRCP High-Yield Summary

| Topic | Key Points |
|-------|------------|
| **Peak Age** | 15-45 years; **Most common solid tumour in young men** |
| **Seminoma vs NSGCT** | Seminoma: **AFP never ↑**; Radiosensitive; Lymphatic spread; **Carboplatin AUC7 adjuvant**<br/>NSGCT: **AFP ↑ (YST), hCG ↑ (Chorio)**; Haematogenous spread; **RPLND / BEP×1 adjuvant** |
| **Markers** | **AFP (YST, t½ 5-7d)**, **hCG (Chorio/EC, t½ 24-36h)**, **LDH (tumour burden)** — **Must check pre-orchidectomy** |
| **IGCCCG** | **Seminoma: Good or Intermediate only** (No Poor); **NSGCT: Good/Intermediate/Poor** |
| **Stage I Seminoma** | **Surveillance** (preferred); **Carboplatin AUC7×1** if risk factors; RT obsolete |
| **Stage I NSGCT** | **Surveillance** (pT1); **RPLND** or **BEP×1** (pT2/LVI+) |
| **Metastatic** | **Good/Int: BEP×3 (EP×4)**: **Poor: BEP×4** |
| **Residual Mass** | Seminoma >3cm → **PET at 6-8wks**; NSGCT any size → **Post-chemo RPLND** |
| **Salvage** | **High-dose chemo + ASCT** (TIP/GEP) — Standard 1st relapse |
| **Late Effects** | **CVD** (Cisplatin, RT), **Second cancers** (RT, Alkylators), **Hypogonadism** (Cisplatin), **Neuropathy** (Cisplatin), **Raynaud's** (Bleomycin), **Infertility** (Cisplatin), **Ototoxicity** (Cisplatin) |
| **Fertility** | **Sperm banking pre-orchidectomy**; **Cisplatin** = main gonadotoxin |

---

## 10. Viva Questions (MRCP PACES / FCPS)

| Question | Expected Answer |
|----------|-----------------|
| **25M, painless testicular lump. Ultrasound: solid intratesticular mass. Markers: AFP 500, hCG normal, LDH normal. Orchidectomy: Mixed GCT (Seminoma + YST). Stage I. Management?** | **Mixed GCT = Treat as NSGCT**. **Stage I NSGCT** → pT stage depends on LVI. If **pT1 (no LVI)**: **Surveillance** (preferred). If **pT2 (LVI+)**: **Primary RPLND** (nerve-sparing) **OR** **BEP ×1 cycle** (SWENOTECA). |
| **35M, pure Seminoma, Stage I, pT2, LVI+, tumour 5cm. Management?** | **Stage I Seminoma with risk factors** → **Carboplatin AUC7 ×1 cycle** (preferred over RT). Surveillance also option if compliant. |
| **IGCCCG Good Risk NSGCT — criteria?** | **Testicular/Retroperitoneal primary** + **No non-pulmonary visceral mets** + **S1 markers (AFP<1000, hCG<5000, LDH<1.5xULN)** |
| **IGCCCG Poor Risk NSGCT — criteria?** | **Mediastinal primary** OR **Non-pulmonary visceral mets** OR **S3 markers (AFP>10000, hCG>50000, LDH>10xULN)** |
| **Metastatic Good Risk Seminoma — chemotherapy?** | **BEP ×3 cycles** (Standard) **OR** **EP ×4 cycles** (if Bleomycin contraindicated) |
| **Post-chemo residual mass 4cm in Seminoma — next?** | **PET-CT at 6-8 weeks**: FDG+ → Salvage (Surgery/High-dose chemo); FDG- → Surveillance |
| **Post-chemo residual mass 2cm in NSGCT — next?** | **Post-chemo RPLND** (any size) → Pathology: Necrosis (surveillance) / Teratoma (surveillance) / Viable NSGCT (Adjuvant chemo 2 cycles EP/VeIP) |
| **Salvage therapy for relapsed GCT — standard?** | **High-dose Chemo (TIP/GEP) + Autologous Stem Cell Transplant** (ASCT) — Superior to conventional chemo |
| **Late effects of cisplatin-based chemo?** | **Neuropathy (peripheral), Ototoxicity (high-freq hearing loss), Nephrotoxicity, Hypogonadism (Leydig cell), Infertility, Raynaud's (Bleomycin), CVD (accelerated atherosclerosis), Second malignancies (Leukaemia - alkylators/etoposide, Solid - RT)** |
| **Fertility preservation — when and how?** | **Sperm banking BEFORE orchidectomy** (and before chemo); **Cisplatin** = main gonadotoxin; Testosterone replacement if hypogonadal |

---

## 11. Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **Seminoma AFP** | **AFP NEVER elevated in pure seminoma** — If AFP ↑ = **NSGCT component** (YST) — Treat as NSGCT |
| **Mixed GCT** | **Always treat as NSGCT** (most aggressive component dictates) |
| **IGCCCG Seminoma Poor Risk** | **Does not exist** — Seminoma = Good or Intermediate only |
| **Carboplatin AUC7 vs RT for Stage I Seminoma** | **Carboplatin preferred**: Single day, less late toxicity (CVD, 2nd cancers), equivalent DFS |
| **RPLND vs BEP×1 for Stage I NSGCT (LVI+)** | **RPLND** = Pathological staging, nerve-sparing; **BEP×1** = Less morbidity, equivalent outcomes (SWENOTECA) |
| **PET-CT in Seminoma residual mass** | **Only for >3cm** at 6-8wks; <3cm = Surveillance; **False +ve if done early** (inflammation) |
| **Bleomycin lung toxicity** | **Cumulative dose >400U** ↑ risk; **Age >40**, **Prior RT**, **Renal impairment** ↑ risk; **Omit if risk factors** (EP×4) |

**Mnemonic: TESTIS**
- **T**umour markers: **AFP (YST)**, **hCG (Chorio)**, **LDH** — Pre-orchidectomy mandatory
- **E**pidemiology: **15-45yr**, Cryptorchidism, FH
- **S**eminoma vs NSGCT: **AFP never ↑ in Seminoma**; Mixed = NSGCT
- **T**reatment Stage I: Seminoma → Surveil/Carbo AUC7; NSGCT → Surveil/RPLND/BEP×1
- **I**GCCCG: Seminoma (Good/Int only); NSGCT (Good/Int/Poor)
- **S**alvage: **High-dose + ASCT** (TIP/GEP) — Standard

---

## 12. Mind Map

```mermaid
mindmap
  root((Testicular GCT))
    Histology
      Seminoma (50-55%)
        AFP never elevated
        Radiosensitive
        Lymphatic spread
      Non-Seminoma (45-50%)
        Embryonal Carcinoma
        Yolk Sac (AFP+)
        Choriocarcinoma (hCG+)
        Teratoma (Chemo-resistant)
      Mixed = NSGCT
    Markers
      AFP (t½ 5-7d) — YST
      hCG (t½ 24-36h) — Chorio/EC
      LDH — Tumour burden
    Staging
      TNM + S (Markers)
      Stage I: N0M0S0
      Stage II: N1-3
      Stage III: M1
    IGCCCG Risk
      Seminoma: Good / Intermediate
      NSGCT: Good / Intermediate / Poor
    Treatment
      Stage I Sem
        Surveillance / Carbo AUC7
      Stage I NSGCT
        pT1: Surveillance
        pT2/LVI+: RPLND / BEP×1
      Metastatic
        Good/Int: BEP×3 / EP×4
        Poor: BEP×4
      Residual Mass
        Sem >3cm: PET at 6-8wk
        NSGCT any: Post-chemo RPLND
      Salvage
        High-dose + ASCT
    Late Effects
      CVD, 2nd Cancers, Hypogonadism
      Neuropathy, Ototoxicity, Raynaud's
      Fertility: Sperm banking pre-tx
```

---

## 13. One-Page Revision Card

| Domain | Key Points |
|--------|------------|
| **Presentation** | Painless testicular lump (90%); Age 15-45; Cryptorchidism risk |
| **Markers** | **AFP** (YST, t½ 5-7d), **hCG** (Chorio/EC, t½ 24-36h), **LDH** (burden) — **Pre-orchidectomy** |
| **Histology** | Seminoma (AFP never ↑); NSGCT (AFP/hCG ↑); Mixed = NSGCT |
| **IGCCCG** | Seminoma: Good/Int only; NSGCT: Good/Int/Poor (Mediastinal primary = Poor) |
| **Stage I Seminoma** | Surveil (pT1-2, no LVI, <4cm); **Carboplatin AUC7×1** if risk factors |
| **Stage I NSGCT** | pT1: Surveil; pT2/LVI+: **RPLND** or **BEP×1** |
| **Metastatic Good/Int** | **BEP×3** (or EP×4); Poor: **BEP×4** |
| **Residual Mass** | Sem >3cm → PET 6-8wk; NSGCT any → Post-chemo RPLND |
| **Salvage** | High-dose chemo (TIP/GEP) + ASCT |
| **Late Effects** | CVD, 2nd cancers, Hypogonadism, Neuropathy, Ototoxicity, Raynaud's, Infertility |
| **Fertility** | **Sperm banking pre-orchidectomy** |

---

## 14. Spaced Repetition Trackers

| Review Interval | Date Completed | Confidence (1-5) | Notes |
|-----------------|----------------|------------------|-------|
| 24 hours | | | |
| 7 days | | | |
| 15 days | | | |
| 30 days | | | |
| 90 days | | | |

---

## 15. Self-Test Scorecard

| Section | Score /5 | Last Attempt |
|---------|----------|--------------|
| Seminoma vs NSGCT markers | | |
| IGCCCG risk groups | | |
| Stage I management (Sem vs NSGCT) | | |
| BEP regimen & cycles | | |
| Residual mass management | | |
| Salvage therapy | | |
| Late effects & fertility | | |
| RPLND indications | | |

---

## 16. Local Navigation
- **Parent Heading**: [[../Oncology|Oncology]]
- **Chapter Map": [[../Davidson Chapter 7 - Oncology Hierarchy|Oncology Hierarchy]]
- **Chapter MOC**: [[../Oncology MOC|Oncology MOC]]
- **Drug Reference**: [[../../Clinical Therapeutics and Good Prescribing|Drugs]]
- **Related**: [[Prostate Cancer]], [[Bladder Cancer]], [[Renal Cell Carcinoma (RCC)]], [[IGCCCG Risk Groups]], [[BEP Chemotherapy]], [[Late Effects Survivorship]]

---

# FCPS/MRCP Exam Extras

## 17. MCQs (10)


**1.** Regarding Testicular Germ Cell Tumours (GCT) (Peak Age), which statement is correct?
   A. 15-45 years
   B. 15-45 - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — 15-45 years; **Most common solid tumour in young men**


**2.** Regarding Testicular Germ Cell Tumours (GCT) (Seminoma vs NSGCT), which statement is correct?
   A. Seminoma: **AFP never ↑**
   B. Seminoma: - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — Seminoma: **AFP never ↑**; Radiosensitive; Lymphatic spread; **Carboplatin AUC7 adjuvant**<br/>NSGCT: **AFP ↑ (YST), hCG...


**3.** Regarding Testicular Germ Cell Tumours (GCT) (Markers), which statement is correct?
   A. **AFP (YST, t½ 5-7d)**, **hCG (Chorio/EC, t½ 24-36h)**, **LDH (tumour burden)**
   B. **AFP - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **AFP (YST, t½ 5-7d)**, **hCG (Chorio/EC, t½ 24-36h)**, **LDH (tumour burden)** — **Must check pre-orchidectomy**


**4.** Regarding Testicular Germ Cell Tumours (GCT) (IGCCCG), which statement is correct?
   A. **Seminoma: Good or Intermediate only** (No Poor)
   B. **Seminoma: - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **Seminoma: Good or Intermediate only** (No Poor); **NSGCT: Good/Intermediate/Poor**


**5.** Regarding Testicular Germ Cell Tumours (GCT) (Stage I Seminoma), which statement is correct?
   A. **Surveillance** (preferred)
   B. **Surveillance** - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **Surveillance** (preferred); **Carboplatin AUC7×1** if risk factors; RT obsolete


**6.** Regarding Testicular Germ Cell Tumours (GCT) (Stage I NSGCT), which statement is correct?
   A. **Surveillance** (pT1)
   B. **Surveillance** - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **Surveillance** (pT1); **RPLND** or **BEP×1** (pT2/LVI+)


**7.** Regarding Testicular Germ Cell Tumours (GCT) (Metastatic), which statement is correct?
   A. **Good/Int: BEP×3 (EP×4)**: **Poor: BEP×4**
   B. **Good/Int: - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **Good/Int: BEP×3 (EP×4)**: **Poor: BEP×4**


**8.** Regarding Testicular Germ Cell Tumours (GCT) (Residual Mass), which statement is correct?
   A. Seminoma >3cm → **PET at 6-8wks**
   B. Seminoma - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — Seminoma >3cm → **PET at 6-8wks**; NSGCT any size → **Post-chemo RPLND**


**9.** Regarding Testicular Germ Cell Tumours (GCT) (Salvage), which statement is correct?
   A. **High-dose chemo + ASCT** (TIP/GEP)
   B. **High-dose - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **High-dose chemo + ASCT** (TIP/GEP) — Standard 1st relapse


**10.** Regarding Testicular Germ Cell Tumours (GCT) (Late Effects), which statement is correct?
   A. **CVD** (Cisplatin, RT), **Second cancers** (RT, Alkylators), **Hypogonadism** (Cisplatin), **Neurop
   B. **CVD** - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **CVD** (Cisplatin, RT), **Second cancers** (RT, Alkylators), **Hypogonadism** (Cisplatin), **Neuropathy** (Cisplatin), ...


## 18. SBA Questions (10)


**1.** A 55-year-old presents with classic features. MDT discussion recommends:
   - A. 15-45 years
   - B. 15-45 (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — first-line: 15-45 years; **Most common solid tumour in young men**


**2.** On staging workup, the patient is found to be [Stage X]. Best management is:
   - A. Seminoma: **AFP never ↑**
   - B. Seminoma: (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — stage-specific: Seminoma: **AFP never ↑**; Radiosensitive; Lymphatic spread; **Carboplatin AUC7 adjuvant**<br/>NSGCT: **AFP ↑ (YST), hCG...


**3.** Following first-line treatment, the patient develops [complication]. Best next step:
   - A. **AFP (YST, t½ 5-7d)**, **hCG (Chorio/EC, t½ 24-36h)**, **LDH (tumour burden)**
   - B. **AFP (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — complication: **AFP (YST, t½ 5-7d)**, **hCG (Chorio/EC, t½ 24-36h)**, **LDH (tumour burden)** — **Must check pre-orchidectomy**


**4.** The patient asks about prognosis. Most appropriate response based on:
   - A. **Seminoma: Good or Intermediate only** (No Poor)
   - B. **Seminoma: (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — prognosis: **Seminoma: Good or Intermediate only** (No Poor); **NSGCT: Good/Intermediate/Poor**


**5.** A 65-year-old with relevant risk factors should be screened with:
   - A. **Surveillance** (preferred)
   - B. **Surveillance** (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — screening: **Surveillance** (preferred); **Carboplatin AUC7×1** if risk factors; RT obsolete


**6.** The most clinically important biomarker/molecular test is:
   - A. **Surveillance** (pT1)
   - B. **Surveillance** (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — biomarker: **Surveillance** (pT1); **RPLND** or **BEP×1** (pT2/LVI+)


**7.** The standard chemotherapy/regimen of choice is:
   - A. **Good/Int: BEP×3 (EP×4)**: **Poor: BEP×4**
   - B. **Good/Int: (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — chemo: **Good/Int: BEP×3 (EP×4)**: **Poor: BEP×4**


**8.** The role of surgery in this case is:
   - A. Seminoma >3cm → **PET at 6-8wks**
   - B. Seminoma (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — surgery: Seminoma >3cm → **PET at 6-8wks**; NSGCT any size → **Post-chemo RPLND**


**9.** The recommended surveillance/follow-up protocol is:
   - A. **High-dose chemo + ASCT** (TIP/GEP)
   - B. **High-dose (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — follow-up: **High-dose chemo + ASCT** (TIP/GEP) — Standard 1st relapse


**10.** Palliative care referral is most appropriate when:
   - A. **CVD** (Cisplatin, RT), **Second cancers** (RT, Alkylators), **Hypogonadism** (Cisplatin), **Neurop
   - B. **CVD** (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — palliative: **CVD** (Cisplatin, RT), **Second cancers** (RT, Alkylators), **Hypogonadism** (Cisplatin), **Neuropathy** (Cisplatin), ...


## 19. Flashcards

**Q1:** Peak Age?
**A1:** 15-45 years; Most common solid tumour in young men

**Q2:** Seminoma vs NSGCT?
**A2:** Seminoma: AFP never ↑; Radiosensitive; Lymphatic spread; Carboplatin AUC7 adjuvant<br/>NSGCT: AFP ↑ (YST), hCG ↑ (Chorio); Haematogenous spread; RPLND / BEP×1 adjuvant

**Q3:** Markers?
**A3:** AFP (YST, t½ 5-7d), hCG (Chorio/EC, t½ 24-36h), LDH (tumour burden) — Must check pre-orchidectomy

**Q4:** IGCCCG?
**A4:** Seminoma: Good or Intermediate only (No Poor); NSGCT: Good/Intermediate/Poor

**Q5:** Stage I Seminoma?
**A5:** Surveillance (preferred); Carboplatin AUC7×1 if risk factors; RT obsolete

**Q6:** Stage I NSGCT?
**A6:** Surveillance (pT1); RPLND or BEP×1 (pT2/LVI+)

**Q7:** Metastatic?
**A7:** Good/Int: BEP×3 (EP×4): Poor: BEP×4

**Q8:** Residual Mass?
**A8:** Seminoma >3cm → PET at 6-8wks; NSGCT any size → Post-chemo RPLND

## 20. Answer Key with Explanations

| # | MCQ | Topic | Explanation |
|---|-----|-------|-------------|
| 1 | A | Peak Age | 15-45 years; Most common solid tumour in young men |
| 2 | A | Seminoma vs NSGCT | Seminoma: AFP never ↑; Radiosensitive; Lymphatic spread; Carboplatin AUC7 adjuvant<br/>NSGCT: AFP ↑ (YST), hCG ↑ (Chorio |
| 3 | A | Markers | AFP (YST, t½ 5-7d), hCG (Chorio/EC, t½ 24-36h), LDH (tumour burden) — Must check pre-orchidectomy |
| 4 | A | IGCCCG | Seminoma: Good or Intermediate only (No Poor); NSGCT: Good/Intermediate/Poor |
| 5 | A | Stage I Seminoma | Surveillance (preferred); Carboplatin AUC7×1 if risk factors; RT obsolete |
| 6 | A | Stage I NSGCT | Surveillance (pT1); RPLND or BEP×1 (pT2/LVI+) |
| 7 | A | Metastatic | Good/Int: BEP×3 (EP×4): Poor: BEP×4 |
| 8 | A | Residual Mass | Seminoma >3cm → PET at 6-8wks; NSGCT any size → Post-chemo RPLND |
| 9 | A | Salvage | High-dose chemo + ASCT (TIP/GEP) — Standard 1st relapse |
| 10 | A | Late Effects | CVD (Cisplatin, RT), Second cancers (RT, Alkylators), Hypogonadism (Cisplatin), Neuropathy (Cisplatin), Raynaud's (Bleom |

| # | SBA | Topic | Explanation |
|---|-----|-------|-------------|
| 1 | A | Peak Age | 15-45 years; Most common solid tumour in young men |
| 2 | A | Seminoma vs NSGCT | Seminoma: AFP never ↑; Radiosensitive; Lymphatic spread; Carboplatin AUC7 adjuvant<br/>NSGCT: AFP ↑ (YST), hCG ↑ (Chorio |
| 3 | A | Markers | AFP (YST, t½ 5-7d), hCG (Chorio/EC, t½ 24-36h), LDH (tumour burden) — Must check pre-orchidectomy |
| 4 | A | IGCCCG | Seminoma: Good or Intermediate only (No Poor); NSGCT: Good/Intermediate/Poor |
| 5 | A | Stage I Seminoma | Surveillance (preferred); Carboplatin AUC7×1 if risk factors; RT obsolete |
| 6 | A | Stage I NSGCT | Surveillance (pT1); RPLND or BEP×1 (pT2/LVI+) |
| 7 | A | Metastatic | Good/Int: BEP×3 (EP×4): Poor: BEP×4 |
| 8 | A | Residual Mass | Seminoma >3cm → PET at 6-8wks; NSGCT any size → Post-chemo RPLND |
| 9 | A | Salvage | High-dose chemo + ASCT (TIP/GEP) — Standard 1st relapse |
| 10 | A | Late Effects | CVD (Cisplatin, RT), Second cancers (RT, Alkylators), Hypogonadism (Cisplatin), Neuropathy (Cisplatin), Raynaud's (Bleom |

## 21. Local Navigation


- **Parent Heading Hub**: [[../../Urological Cancers|Urological Cancers]]
- **Chapter Map**: [[../../Davidson Chapter 7 - Oncology Hierarchy|Oncology Hierarchy]]
- **Chapter MOC**: [[../../Oncology MOC|Oncology MOC]]
- **Drug Reference**: [[../../../Clinical Therapeutics and Good Prescribing|Drugs]]

