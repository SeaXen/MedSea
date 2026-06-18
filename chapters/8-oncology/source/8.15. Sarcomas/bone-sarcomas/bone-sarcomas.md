# Bone Sarcomas: Osteosarcoma, Ewing Sarcoma, Chondrosarcoma

> [!tip] **FCPS/MRCP Priority: HIGH**
> **Bone Sarcomas**: **Osteosarcoma (35%)**, **Ewing Sarcoma (30%)**, **Chondrosarcoma (25%)**; **Osteosarcoma**: Teenagers, Metaphysis Long Bones, **MAP Protocol (High-Dose MTX, Doxo, Cisplatin) → Surgery → Adjuvant MAP**; **Ewing Sarcoma**: **t(11;22) EWSR1-FLI1**, Children/Young Adults, **VAC/IE Alternating → Surgery/RT → Adjuvant**; **Chondrosarcoma**: Adults, **IDH1/2 Mut**, **Surgery Mainstay**, **RT/Chemo Resistant**; **Limb Salvage Standard**; **Metastatic: Lung Most Common**; **Surveillance**

---

## 1. Learning Objectives
By the end of this note you should be able to:
- [ ] Distinguish **Osteosarcoma, Ewing Sarcoma, Chondrosarcoma** by Age, Site, Histology, Genetics
- [ ] Apply **MAP Protocol** for Osteosarcoma (Neoadjuvant MAP → Surgery → Adjuvant MAP)
- [ ] Apply **VAC/IE Alternating** for Ewing Sarcoma (Neoadjuvant → Local Control → Adjuvant)
- [ ] Recognise **Chondrosarcoma** relies on **Surgery**; **RT/Chemo Resistant**; **IDH1/2 Mutation**
- [ ] Plan **Limb Salvage Surgery** (R0, Endoprosthesis, Allograft, Rotationplasty)
- [ ] Know **Metastatic Patterns**: Lung Most Common, Skip Mets (Osteosarcoma)
- [ ] Indicate **Rotationplasty** for Distal Femur/Proximal Tibia in Young Children

---

## 2. Osteosarcoma

### Epidemiology & Clinical Features

| Feature | Detail |
|---------|--------|
| **Incidence** | **Most Common Primary Bone Sarcoma (35%)**; ~500/year UK |
| **Peak Age** | **10-25 years** (Teenagers); **Second Peak >60** (Secondary: Paget's, RT, Paget's) |
| **Sex Ratio** | M:F = 1.5:1 |
| **Common Sites** | **Distal Femur (40%)**, **Proximal Tibia (20%)**, **Proximal Humerus (10%)** — **Metaphysis Long Bones** |
| **Presentation** | **Pain (Months)**, **Swelling**, **Pathological Fracture (5-10%)** |
| **Metastases** | **Lung (80%)**, **Skip Mets (Same Bone, Non-Contiguous)**, **Bone** |

### Histology & Molecular

| Feature | Detail |
|---------|--------|
| **Histology** | **Osteoblastic (50%)**, **Chondroblastic (25%)**, **Fibroblastic (15%)**, **Telangiectatic, Small Cell, High-Grade Surface** |
| **Molecular** | **Complex Karyotype**, **TP53 Mut (30%)**, **RB1 Loss**, **MYC Amp**, **No Recurrent Translocation** |
| **Genetic Syndromes** | **Li-Fraumeni (TP53)**, **Hereditary Retinoblastoma (RB1)**, **Rothmund-Thomson (RECQL4)**, **Bloom (BLM)**, **Werner (WRN)** |

### MAP Protocol (Standard of Care)

```mermaid
flowchart TD
    A[Localised High-Grade Osteosarcoma] --> B[**Neoadjuvant MAP ×2-3 Cycles**]
    B --> B1[**M**ethotrexate **High-Dose 12g/m²** (Day 1, Leucovorin Rescue)]
    B --> B2[**A**driamycin (Doxorubicin) **37.5mg/m²** (Day 1-2)]
    B --> B3[**P**latinum (Cisplatin) **120mg/m²** (Day 1-2, Hydration)]
    B --> B4[**Cycle Every 21 Days**]
    B1 --> C[**Surgery: Wide Resection + Limb Salvage (Endoprosthesis/Allograft)**<br/>**Rotationplasty (Distal Femur/Prox Tibia, Young Child)**]
    B2 --> C
    B3 --> C
    C --> D[**Pathological Response Assessment**]
    D -->|**Good Response (≥90% Necrosis)**| E[**Adjuvant MAP ×4-6 Cycles (Same)**]
    D -->|**Poor Response (<90% Necrosis)**| F[**Adjuvant MAP ± Addition (Ifosfamide/Etoposide — EURAMOS-1 Failed)**]
    E --> G[**Surveillance: CT Chest q3mo×2yr, q6mo×3yr; MRI Local q6mo×2yr**]
    F --> G
```

### Surgical Options

| Procedure | Indication |
|-----------|------------|
| **Limb Salvage (Endoprosthesis)** | **Standard (>90%)**; **Megaprosthesis** |
| **Allograft/Autograft** | **Biological Reconstruction** (Young, Growth) |
| **Vascularised Fibular Graft** | **Growing Children** |
| **Rotationplasty** | **Distal Femur/Prox Tibia**, **Young Child (<10)**, **Preserves Nerve Function**, **Functional Ankle = Knee** |
| **Amputation** | **Neurovascular Bundle Involvement**, **Pathological Fracture**, **Infection**, **Failed Salvage** |

---

## 3. Ewing Sarcoma

### Epidemiology & Clinical Features

| Feature | Detail |
|---------|--------|
| **Incidence** | **Second Most Common (30%)**; ~300/year UK |
| **Peak Age** | **10-20 years** (Children/Young Adults) |
| **Sex Ratio** | M:F = 1.5:1 |
| **Sites** | **Long Bones (50%)** (Femur, Tibia, Humerus), **Flat Bones (30%)** (Pelvis, Ribs, Scapula), **Vertebrae** |
| **Soft Tissue Ewing** | **Extra-skeletal (15-20%)** |
| **Presentation** | **Pain, Swelling**, **Fever (Systemic)**, **Pathological Fracture** |

### Molecular Pathogenesis

```mermaid
flowchart LR
    A[Ewing Sarcoma] --> B[**t(11;22)(q24;q12) — 85%**]
    B --> C[**EWSR1-FLI1 Fusion** (Type 1 = Exon 7-Exon 6, Best Prognosis)]
    A --> D[**t(21;22) EWSR1-ERG — 10%**]
    A --> E[**Other EWSR1-ETS Fusions — 5%**]
    C --> F[**FLI1/ERG → Transcriptional Dysregulation**]
    F --> G[**Target Genes: NKX2.2, CAV1, CCND1, IGF1R, VEGF**]
```

### Diagnostic IHC / Molecular

| Marker | Result |
|--------|--------|
| **CD99 (MIC2)** | **Membranous, Strong, Diffuse (+)** — **Sensitive but Not Specific** |
| **FLI1** | **Nuclear (+)** — **Specific** |
| **NKX2.2** | **Nuclear (+)** — **Highly Specific** |
| **FISH / RT-PCR** | **EWSR1-FLI1 / EWSR1-ERG** — **Definitive** |

### VAC/IE Alternating Protocol (Standard)

```mermaid
flowchart TD
    A[Localised Ewing Sarcoma] --> B[**Neoadjuvant VAC/IE Alternating ×6-9 Cycles**]
    B --> B1[**VAC**: Vincristine 1.5mg/m² d1 + Actinomycin D 1.25mg/m² d1 + Cyclophosphamide 1.2g/m² d1 **q3w**]
    B --> B2[**IE**: Ifosfamide 1.8g/m² d1-5 (Mesna) + Etoposide 100mg/m² d1-5 **q3w**]
    B1 --> C[**Local Control (Week 10-12)**]
    B2 --> C
    C --> C1[**Surgery (Wide Resection) +/− RT**<br/>**If Surgery Feasible: Surgery + Post-op RT (if Margins+ / Poor Response)**]
    C --> C2[**Definitive RT (55-60Gy)**<br/>**If Unresectable / Poor Surgical Candidate / Pelvis/Spine**]
    C1 --> D[**Adjuvant VAC/IE Alternating ×6-9 Cycles (Total ~14-17 Cycles)**]
    C2 --> D
    D --> E[**Surveillance: CT Chest q3mo×2yr, q6mo×3yr; MRI Local q6mo×2yr**]
```

### Ewing Sarcoma Risk Stratification

| Group | Criteria | Treatment Intensity |
|-------|----------|---------------------|
| **Low** | **Primary <8cm, Distal Extremity, No Mets, Good Response** | **Standard VAC/IE** |
| **Intermediate** | **Primary ≥8cm, Proximal/Pelvis, Good Response** | **Standard + RT Boost** |
| **High** | **Metastatic at Diagnosis, Poor Response** | **Intensified (High-Dose Chemo + ASCT)** |

---

## 4. Chondrosarcoma

### Epidemiology & Clinical Features

| Feature | Detail |
|---------|--------|
| **Incidence** | **Most Common in Adults (>40yr)**; **25% of Bone Sarcomas** |
| **Peak Age** | **40-70 years** |
| **Sites** | **Pelvis (30%)**, **Femur (25%)**, **Humerus (15%)**, **Ribs, Scapula** |
| **Presentation** | **Slow-Growing Pain**, **Mass**, **Neurological (Pelvis/Sacrum)** |

### Histological Grades & Molecular

| Grade | Histology | Molecular | Behaviour |
|-------|-----------|-----------|-----------|
| **Grade 1 (Atypical Chondrogenic Tumour)** | **Low Cellularity**, **Mild Atypia** | **IDH1/2 Mut (50%)**, **COL2A1** | **Locally Aggressive, Rarely Metastasises** |
| **Grade 2** | **Increased Cellularity**, **Mitoses** | **IDH1/2 Mut (60-70%)**, **COL2A1**, **TP53 (Late)** | **Metastatic Potential (Lung)** |
| **Grade 3 (Dedifferentiated)** | **High-Grade Spindle + Chondroid** | **IDH1/2 + TP53 + RB1 + CDKN2A** | **Highly Aggressive, Early Mets** |
| **Mesenchymal** | **Young Adults**, **Spindle + Cartilage** | **HEY1-NCOA2 Fusion** | **Aggressive** |
| **Clear Cell** | **Clear Cells**, **Glycogen** | **Unknown** | **Intermediate** |

### Key Molecular Feature: **IDH1/2 Mutation (50-70%)**
- **Diagnostic** (vs Chondroblastic Osteosarcoma — IDH WT)
- **Prognostic** (IDH Mut = Better Prognosis in Low-Grade)
- **Therapeutic Target** (Ivosidenib/Enasidenib — Trials)

---

## 5. Management

### Chondrosarcoma — Surgery Mainstay

```mermaid
flowchart TD
    A[Chondrosarcoma] --> B{Grade}
    B -->|**Grade 1 (Intralesional/Marginal Acceptable)**| C[**Wide/Marginal Resection**<br/>**Curettage + Adjuvant (Phenol/Cryo/Cement)** for Small Peripheral<br/>**NO RT, NO Chemo**]
    B -->|**Grade 2-3 (Wide/Radical Resection)**| D[**Wide/Radical Resection + Reconstruction**<br/>**Endoprosthesis / Allograft / Arthrodesis**<br/>**Pelvis: Internal Hemipelvectomy / Extended**<br/>**NO Adjuvant Chemo (Resistant)**<br/>**RT: Consider for Close/Positive Margins / Unresectable (66-70Gy)**]
    D --> E[**Surveillance: CT Chest q6mo×3yr, q12mo×2yr; MRI Local q6-12mo**]
```

### Dedifferentiated Chondrosarcoma

| Component | Treatment |
|-----------|-----------|
| **Low-Grade Cartilaginous** | **Surgery (Wide)** |
| **High-Grade Non-Cartilaginous (UPS-like)** | **Surgery + Consider Doxorubicin-based Chemo** (Anthracycline Sensitive) |
| **RT** | **Adjuvant for Margins+ / Unresectable (66-70Gy)** |

---

## 6. Metastatic Disease

| Sarcoma | Metastatic Pattern | 1L Systemic Therapy |
|---------|-------------------|---------------------|
| **Osteosarcoma** | **Lung (80%)**, Skip Mets, Bone | **MAP Continued**, **Gem/Doc**, **High-Dose Ifosfamide/Etoposide**, **Clinical Trials** |
| **Ewing Sarcoma** | **Lung, Bone, Bone Marrow** | **VAC/IE Continuation**, **High-Dose Chemo + ASCT**, **TKIs (IGF1R — Failed)**, **Topo Inhibitors** |
| **Chondrosarcoma** | **Lung (Most Common)** | **Chemo Resistant**; **Dedifferentiated: Doxorubicin**; **IDH Inhibitors (Ivosidenib — Trials)** |

---

## 7. Limb Salvage Reconstruction Options

| Method | Indication | Pros / Cons |
|--------|------------|-------------|
| **Megaprosthesis (Endoprosthesis)** | **Standard (>90%)** | **Immediate Function**, **Revision Risk (Loosening, Infection, Fracture)** |
| **Allograft + Prosthetic Composite** | **Young, Large Defect** | **Biological**, **Non-Union, Infection, Fracture Risk** |
| **Vascularised Fibular Graft** | **Growing Children** | **Living Bone, Hypertrophy**, **Donor Morbidity, Technical** |
| **Rotationplasty** | **Distal Femur/Prox Tibia, Young Child (<10)** | **Preserves Nerve, Ankle = Knee**, **Cosmesis Concerns** |
| **Amputation** | **Neurovascular Involvement, Infection, Failed Salvage** | **Definitive Oncologic**, **Prosthetic Fitting** |

---

## 8. Surveillance

| Tumour | Imaging Schedule |
|--------|------------------|
| **Osteosarcoma** | **CT Chest q3mo ×2yr, q6mo ×3yr**; **MRI Local q6mo ×2yr** |
| **Ewing Sarcoma** | **CT Chest q3mo ×2yr, q6mo ×3yr**; **MRI Local q6mo ×2yr**; **Bone Marrow (if Initial Mets)** |
| **Chondrosarcoma** | **CT Chest q6mo ×3yr, q12mo ×2yr**; **MRI Local q6-12mo** |

---

## 9. FCPS/MRCP High-Yield Summary

| Topic | Key Points |
|-------|------------|
| **Osteosarcoma** | **Teenagers**, Metaphysis Long Bones, **MAP (High-Dose MTX, Doxo, Cisplatin)**, Surgery (Limb Salvage), **Good Response = ≥90% Necrosis** |
| **Ewing Sarcoma** | **t(11;22) EWSR1-FLI1**, Children/Young Adults, **VAC/IE Alternating**, Surgery/RT Local Control |
| **Chondrosarcoma** | **Adults >40**, **IDH1/2 Mut**, **Surgery Mainstay**, **RT/Chemo Resistant** |
| **MAP Protocol** | **Pre-op: MTX 12g + Doxo 37.5 + Cis 120 q3w ×2-3** → Surgery → **Post-op MAP ×4-6** (Adjust by Necrosis) |
| **VAC/IE** | **Alternating q3w**: VAC (Vinca/Act-D/Cyclo) ↔ IE (Ifos/Etopo) ×14-17 Cycles Total |
| **Limb Salvage** | **Endoprosthesis >90%**, Rotationplasty (Young, Distal Femur/Tibia) |
| **Metastases** | **Lung (All)**, Skip Mets (Osteo), Bone Marrow (Ewing) |
| **Chondrosarcoma** | **IDH1/2 Mut (50-70%)**, **Grade 1: Marginal**, **Gr2-3: Wide**, **Dediff: Surgery + Doxo** |
| **Dedifferentiated Chondrosarcoma** | **High-Grade Spindle + Cartilage**, **Surgery + Doxorubicin** |

---

## 10. Viva Questions (MRCP PACES / FCPS)

| Question | Expected Answer |
|----------|-----------------|
| **Osteosarcoma — Peak Age, Common Sites?** | **10-25 years**, **Metaphysis Long Bones (Distal Femur 40%, Prox Tibia 20%, Prox Humerus 10%)**. |
| **Ewing Sarcoma — Translocation, IHC?** | **t(11;22) EWSR1-FLI1 (85%)**; **CD99 Membranous Diffuse (+)**, **FLI1 Nuclear (+)**, **NKX2.2 Nuclear (+)**. |
| **Ewing Sarcoma Chemotherapy Regimen?** | **VAC/IE Alternating**: **VAC (Vincristine, Actinomycin D, Cyclophosphamide) q3w** alternating with **IE (Ifosfamide+Etoposide) q3w** ×14-17 Total Cycles. |
| **Osteosarcoma — Good vs Poor Histological Response?** | **Good: ≥90% Necrosis** → **Continue Same MAP Adjuvant**; **Poor: <90% Necrosis** → **Consider Addition (EURAMOS-1: Ifo/Etopo Failed to Improve OS)**. |
| **Rotationplasty — Indication?** | **Distal Femur / Proximal Tibia**, **Young Child (<10)**, **Preserves Sciatic Nerve**, **Ankle Functions as Knee**. |
| **Chondrosarcoma — Molecular Marker, Treatment?** | **IDH1/2 Mutation (50-70%)** — **Diagnostic/Prognostic**; **Grade 1: Marginal/Curettage**; **Grade 2-3: Wide Resection**; **NO Chemo/RT for Conventional**. |
| **Dedifferentiated Chondrosarcoma — Management?** | **Wide Resection + Doxorubicin-based Chemo** (For High-Grade Component). |
| **Ewing Sarcoma — Skip Mets?** | **Not Typical**; **Osteosarcoma: Skip Mets (Same Bone, Non-Contiguous)**; **Ewing: Bone Marrow Mets Common**. |
| **Chondrosarcoma — Why No Chemo/RT for Low-Grade?** | **Chemoresistant (Low Proliferation, IDH Mut)**, **Radioresistant**; **Surgery Curative if Adequate Margins**. |
| **Osteosarcoma Metastatic — 1L Systemic?** | **Continue MAP**, **Gemcitabine/Docetaxel**, **High-Dose Ifosfamide/Etoposide**, **Clinical Trials**. |

---

## 11. Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| **Osteosarcoma vs Ewing — Age** | **Osteosarcoma: 10-25 (Teenagers)**; **Ewing: 10-20 (Children/Young Adults)** — **Overlap, But Osteo Older Peak** |
| **Osteosarcoma vs Ewing — Site** | **Osteo: Metaphysis Long Bones (Distal Femur)**; **Ewing: Diaphysis Long Bones + Flat Bones (Pelvis, Ribs)** |
| **MAP vs VAC/IE** | **MAP: Osteosarcoma (MTX, Doxo, Cisplatin)**; **VAC/IE: Ewing (Alternating VAC/IE)** |
| **Chondrosarcoma vs Chondroblastic Osteosarcoma** | **Chondrosarcoma: IDH1/2 Mut, Adults >40**; **Chondroblastic Osteosarcoma: IDH WT, Teenagers, Osteoid Production** |
| **Dedifferentiated Chondrosarcoma** | **Low-Grade Cartilaginous + High-Grade Non-Cartilaginous (UPS-like)** — **Treat High-Grade Component with Chemo** |
| **Rotationplasty vs Amputation** | **Rotationplasty: Preserves Nerve, Ankle=Knee, Functional Superior**; **Amputation: Neurovascular Involvement, Infection, Failed Salvage** |
| **Chemo for Chondrosarcoma** | **Conventional Chemo INEFFECTIVE** (Low Proliferation, IDH Mut); **Dedifferentiated: Doxorubicin Works** |

**Mnemonic: BONE-SARCOMA**
- **B**one Sarcomas: **Osteo (35%)**, **Ewing (30%)**, **Chondro (25%)**
- **O**steosarcoma: **Teenagers**, **Metaphysis**, **MAP (MTX/Doxo/Cis)**, **Limb Salvage**
- **S**unburst Periosteal Reaction, **Codman's Triangle**
- **T**ranslocation Ewing: **t(11;22) EWSR1-FLI1**, **CD99/FLI1/NKX2.2**
- **E**wing Chemo: **VAC/IE Alternating** (Vinca/Act-D/Cyclo ↔ Ifos/Etopo)
- **O**steosarcoma Response: **≥90% Necrosis = Good** → Continue MAP
- **S**kip Mets: **Osteo (Same Bone)**, Ewing (Bone Marrow)
- **A**rthroplasty: **Endoprosthesis (>90%)**, **Rotationplasty (Young, Distal Femur/Tibia)**
- **R**esistance: **Chondrosarcoma = Chemo/RT Resistant** (Except Dedifferentiated)
- **C**chondrosarcoma: **IDH1/2 Mut (50-70%)**, **Adults >40**, **Surgery Only**
- **O**steoid Production: **Osteosarcoma Diagnostic** (Not Chondrosarcoma)
- **M**etastases: **Lung (All)**, **Skip (Osteo)**, **Bone Marrow (Ewing)**

---

## 12. Mind Map

```mermaid
mindmap
  root((Bone Sarcomas))
    Osteosarcoma (35%)
      Teenagers, Metaphysis Long Bones
      MAP: MTX 12g + Doxo 37.5 + Cis 120 q3w
      Surgery: Limb Salvage (Endoprosthesis)
      Response: ≥90% Necrosis Good
      Skip Mets
      Rotationplasty (Young)
    Ewing Sarcoma (30%)
      Children/Young Adults
      t(11;22) EWSR1-FLI1
      CD99/FLI1/NKX2.2
      VAC/IE Alternating q3w
      Surgery/RT Local Control
      Diaphysis + Flat Bones
    Chondrosarcoma (25%)
      Adults >40
      IDH1/2 Mut (50-70%)
      Gr1: Marginal/Curettage
      Gr2-3: Wide Resection
      Dedifferentiated: Surgery + Doxo
    Limb Salvage
      Endoprosthesis >90%
      Rotationplasty (Young, Distal Femur/Tibia)
      Allograft, Vascularised Fibula
    Metastases
      Lung (All)
      Skip Mets (Osteo)
      Bone Marrow (Ewing)
    Chondro Grades
      Gr1: Marginal
      Gr2-3: Wide
      Dediff: Surgery + Doxo
```

---

## 13. One-Page Revision Card

| Domain | Key Points |
|--------|------------|
| **Osteosarcoma** | Teenagers, Metaphysis, MAP (MTX/Doxo/Cis), ≥90% Necrosis Good |
| **Ewing Sarcoma** | t(11;22) EWSR1-FLI1, CD99/FLI1, VAC/IE Alternating |
| **Chondrosarcoma** | Adults >40, IDH1/2 Mut, Surgery Only (Gr1 Marginal, Gr2-3 Wide) |
| **MAP** | Neoadj MTX 12g + Doxo 37.5 + Cis 120 ×2-3 → Surgery → Adj MAP ×4-6 |
| **VAC/IE** | Alternating q3w: VAC (Vinca/Act-D/Cyclo) ↔ IE (Ifos/Etopo) ×14-17 |
| **Limb Salvage** | Endoprosthesis >90%, Rotationplasty (Young, Distal Femur/Tibia) |
| **Metastases** | Lung (All), Skip (Osteo), Bone Marrow (Ewing) |
| **Chondro Grades** | Gr1: Marginal; Gr2-3: Wide; Dediff: Surgery + Doxo |

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
| Osteosarcoma MAP Protocol | | |
| Ewing VAC/IE Regimen | | |
| Chondrosarcoma IDH/Grades | | |
| Limb Salvage Options | | |
| Histological Response Criteria | | |
| Rotationplasty Indication | | |
| Dedifferentiated Chondrosarcoma | | |
| Metastatic Patterns | | |

---

## 16. Local Navigation
- **Parent Heading**: [[../Oncology|Oncology]]
- **Chapter Map": [[../Davidson Chapter 7 - Oncology Hierarchy|Oncology Hierarchy]]
- **Chapter MOC": [[../Oncology MOC|Oncology MOC]]
- **Drug Reference": [[../../Clinical Therapeutics and Good Prescribing|Drugs]]
- **Related": [[Soft Tissue Sarcoma]], [[MAP Protocol]], [[VAC/IE]], [[EWSR1-FLI1]], [[IDH1/2 Mutation]], [[Limb Salvage]], [[Rotationplasty]], [[EURAMOS-1]]

---

# FCPS/MRCP Exam Extras

## 17. MCQs (10)


**1.** Regarding Bone Sarcomas: Osteosarcoma, Ewing Sarcoma, Chondrosarcoma (Osteosarcoma), which statement is correct?
   A. **Teenagers**, Metaphysis Long Bones, **MAP (High-Dose MTX, Doxo, Cisplatin)**, Surgery (Limb Salvag
   B. **Teenagers**, - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **Teenagers**, Metaphysis Long Bones, **MAP (High-Dose MTX, Doxo, Cisplatin)**, Surgery (Limb Salvage), **Good Response ...


**2.** Regarding Bone Sarcomas: Osteosarcoma, Ewing Sarcoma, Chondrosarcoma (Ewing Sarcoma), which statement is correct?
   A. **t(11
   B. **t(11 - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **t(11;22) EWSR1-FLI1**, Children/Young Adults, **VAC/IE Alternating**, Surgery/RT Local Control


**3.** Regarding Bone Sarcomas: Osteosarcoma, Ewing Sarcoma, Chondrosarcoma (Chondrosarcoma), which statement is correct?
   A. **Adults >40**, **IDH1/2 Mut**, **Surgery Mainstay**, **RT/Chemo Resistant**
   B. **Adults - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **Adults >40**, **IDH1/2 Mut**, **Surgery Mainstay**, **RT/Chemo Resistant**


**4.** Regarding Bone Sarcomas: Osteosarcoma, Ewing Sarcoma, Chondrosarcoma (MAP Protocol), which statement is correct?
   A. **Pre-op: MTX 12g + Doxo 37.5 + Cis 120 q3w ×2-3** → Surgery → **Post-op MAP ×4-6** (Adjust by Necro
   B. **Pre-op: - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **Pre-op: MTX 12g + Doxo 37.5 + Cis 120 q3w ×2-3** → Surgery → **Post-op MAP ×4-6** (Adjust by Necrosis)


**5.** Regarding Bone Sarcomas: Osteosarcoma, Ewing Sarcoma, Chondrosarcoma (VAC/IE), which statement is correct?
   A. **Alternating q3w**: VAC (Vinca/Act-D/Cyclo) ↔ IE (Ifos/Etopo) ×14-17 Cycles Total
   B. **Alternating - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **Alternating q3w**: VAC (Vinca/Act-D/Cyclo) ↔ IE (Ifos/Etopo) ×14-17 Cycles Total


**6.** Regarding Bone Sarcomas: Osteosarcoma, Ewing Sarcoma, Chondrosarcoma (Limb Salvage), which statement is correct?
   A. **Endoprosthesis >90%**, Rotationplasty (Young, Distal Femur/Tibia)
   B. **Endoprosthesis - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **Endoprosthesis >90%**, Rotationplasty (Young, Distal Femur/Tibia)


**7.** Regarding Bone Sarcomas: Osteosarcoma, Ewing Sarcoma, Chondrosarcoma (Metastases), which statement is correct?
   A. **Lung (All)**, Skip Mets (Osteo), Bone Marrow (Ewing)
   B. **Lung - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **Lung (All)**, Skip Mets (Osteo), Bone Marrow (Ewing)


**8.** Regarding Bone Sarcomas: Osteosarcoma, Ewing Sarcoma, Chondrosarcoma (Chondrosarcoma), which statement is correct?
   A. **IDH1/2 Mut (50-70%)**, **Grade 1: Marginal**, **Gr2-3: Wide**, **Dediff: Surgery + Doxo**
   B. **IDH1/2 - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **IDH1/2 Mut (50-70%)**, **Grade 1: Marginal**, **Gr2-3: Wide**, **Dediff: Surgery + Doxo**


**9.** Regarding Bone Sarcomas: Osteosarcoma, Ewing Sarcoma, Chondrosarcoma (Dedifferentiated Chondrosarcoma), which statement is correct?
   A. **High-Grade Spindle + Cartilage**, **Surgery + Doxorubicin**
   B. **High-Grade - alternative approach
   C. Empirical management only
   D. Watch and wait
   - **Answer: A** — **High-Grade Spindle + Cartilage**, **Surgery + Doxorubicin**


**10.** Regarding Bone Sarcomas: Osteosarcoma, Ewing Sarcoma, Chondrosarcoma (FCPS/MRCP High Yield - Bone Sarcomas), which statement is correct?
   - A. FCPS/MRCP High Yield - Bone Sarcomas: Osteosarcoma (35%), Ewing Sarcoma (30%), Chondrosarcoma (25%)
   - B. Empirical approach without specific indication
   - C. Used only in research protocols
   - D. Not relevant in current practice
   - **Answer: A** — FCPS/MRCP High Yield - Bone Sarcomas: Osteosarcoma (35%), Ewing Sarcoma (30%), Chondrosarcoma (25%)

## 18. SBA Questions (10)


**1.** A 55-year-old presents with classic features. MDT discussion recommends:
   - A. **Teenagers**, Metaphysis Long Bones, **MAP (High-Dose MTX, Doxo, Cisplatin)**, Surgery (Limb Salvag
   - B. **Teenagers**, (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — first-line: **Teenagers**, Metaphysis Long Bones, **MAP (High-Dose MTX, Doxo, Cisplatin)**, Surgery (Limb Salvage), **Good Response ...


**2.** On staging workup, the patient is found to be [Stage X]. Best management is:
   - A. **t(11
   - B. **t(11 (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — stage-specific: **t(11;22) EWSR1-FLI1**, Children/Young Adults, **VAC/IE Alternating**, Surgery/RT Local Control


**3.** Following first-line treatment, the patient develops [complication]. Best next step:
   - A. **Adults >40**, **IDH1/2 Mut**, **Surgery Mainstay**, **RT/Chemo Resistant**
   - B. **Adults (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — complication: **Adults >40**, **IDH1/2 Mut**, **Surgery Mainstay**, **RT/Chemo Resistant**


**4.** The patient asks about prognosis. Most appropriate response based on:
   - A. **Pre-op: MTX 12g + Doxo 37.5 + Cis 120 q3w ×2-3** → Surgery → **Post-op MAP ×4-6** (Adjust by Necro
   - B. **Pre-op: (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — prognosis: **Pre-op: MTX 12g + Doxo 37.5 + Cis 120 q3w ×2-3** → Surgery → **Post-op MAP ×4-6** (Adjust by Necrosis)


**5.** A 65-year-old with relevant risk factors should be screened with:
   - A. **Alternating q3w**: VAC (Vinca/Act-D/Cyclo) ↔ IE (Ifos/Etopo) ×14-17 Cycles Total
   - B. **Alternating (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — screening: **Alternating q3w**: VAC (Vinca/Act-D/Cyclo) ↔ IE (Ifos/Etopo) ×14-17 Cycles Total


**6.** The most clinically important biomarker/molecular test is:
   - A. **Endoprosthesis >90%**, Rotationplasty (Young, Distal Femur/Tibia)
   - B. **Endoprosthesis (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — biomarker: **Endoprosthesis >90%**, Rotationplasty (Young, Distal Femur/Tibia)


**7.** The standard chemotherapy/regimen of choice is:
   - A. **Lung (All)**, Skip Mets (Osteo), Bone Marrow (Ewing)
   - B. **Lung (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — chemo: **Lung (All)**, Skip Mets (Osteo), Bone Marrow (Ewing)


**8.** The role of surgery in this case is:
   - A. **IDH1/2 Mut (50-70%)**, **Grade 1: Marginal**, **Gr2-3: Wide**, **Dediff: Surgery + Doxo**
   - B. **IDH1/2 (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — surgery: **IDH1/2 Mut (50-70%)**, **Grade 1: Marginal**, **Gr2-3: Wide**, **Dediff: Surgery + Doxo**


**9.** The recommended surveillance/follow-up protocol is:
   - A. **High-Grade Spindle + Cartilage**, **Surgery + Doxorubicin**
   - B. **High-Grade (less specific)
   - C. Empirical broad approach
   - D. No intervention required
   - **Answer: A** — follow-up: **High-Grade Spindle + Cartilage**, **Surgery + Doxorubicin**


**10.** A clinician encounters this presentation. Best approach:
   - A. FCPS/MRCP High Yield - Bone Sarcomas: Osteosarcoma (35%), Ewing Sarcoma (30%), Chondrosarcoma (25%)
   - B. Watch and wait approach
   - C. Empirical broad treatment
   - D. No intervention required
   - **Answer: A** — FCPS/MRCP High Yield - Bone Sarcomas: Osteosarcoma (35%), Ewing Sarcoma (30%), Chondrosarcoma (25%)

## 19. Flashcards

**Q1:** Osteosarcoma?
**A1:** Teenagers, Metaphysis Long Bones, MAP (High-Dose MTX, Doxo, Cisplatin), Surgery (Limb Salvage), Good Response = ≥90% Necrosis

**Q2:** Ewing Sarcoma?
**A2:** t(11;22) EWSR1-FLI1, Children/Young Adults, VAC/IE Alternating, Surgery/RT Local Control

**Q3:** Chondrosarcoma?
**A3:** Adults >40, IDH1/2 Mut, Surgery Mainstay, RT/Chemo Resistant

**Q4:** MAP Protocol?
**A4:** Pre-op: MTX 12g + Doxo 37.5 + Cis 120 q3w ×2-3 → Surgery → Post-op MAP ×4-6 (Adjust by Necrosis)

**Q5:** VAC/IE?
**A5:** Alternating q3w: VAC (Vinca/Act-D/Cyclo) ↔ IE (Ifos/Etopo) ×14-17 Cycles Total

**Q6:** Limb Salvage?
**A6:** Endoprosthesis >90%, Rotationplasty (Young, Distal Femur/Tibia)

**Q7:** Metastases?
**A7:** Lung (All), Skip Mets (Osteo), Bone Marrow (Ewing)

**Q8:** Chondrosarcoma?
**A8:** IDH1/2 Mut (50-70%), Grade 1: Marginal, Gr2-3: Wide, Dediff: Surgery + Doxo

## 20. Answer Key with Explanations

| # | MCQ | Topic | Explanation |
|---|-----|-------|-------------|
| 1 | A | Osteosarcoma | Teenagers, Metaphysis Long Bones, MAP (High-Dose MTX, Doxo, Cisplatin), Surgery (Limb Salvage), Good Response = ≥90% Nec |
| 2 | A | Ewing Sarcoma | t(11;22) EWSR1-FLI1, Children/Young Adults, VAC/IE Alternating, Surgery/RT Local Control |
| 3 | A | Chondrosarcoma | Adults >40, IDH1/2 Mut, Surgery Mainstay, RT/Chemo Resistant |
| 4 | A | MAP Protocol | Pre-op: MTX 12g + Doxo 37.5 + Cis 120 q3w ×2-3 → Surgery → Post-op MAP ×4-6 (Adjust by Necrosis) |
| 5 | A | VAC/IE | Alternating q3w: VAC (Vinca/Act-D/Cyclo) ↔ IE (Ifos/Etopo) ×14-17 Cycles Total |
| 6 | A | Limb Salvage | Endoprosthesis >90%, Rotationplasty (Young, Distal Femur/Tibia) |
| 7 | A | Metastases | Lung (All), Skip Mets (Osteo), Bone Marrow (Ewing) |
| 8 | A | Chondrosarcoma | IDH1/2 Mut (50-70%), Grade 1: Marginal, Gr2-3: Wide, Dediff: Surgery + Doxo |
| 9 | A | Dedifferentiated Chondrosarcoma | High-Grade Spindle + Cartilage, Surgery + Doxorubicin |
| 10 | A | FCPS/MRCP High Yield - Bone Sarcomas | FCPS/MRCP High Yield - Bone Sarcomas: Osteosarcoma (35%), Ewing Sarcoma (30%), Chondrosarcoma (25%) |

| # | SBA | Topic | Explanation |
|---|-----|-------|-------------|
| 1 | A | Osteosarcoma | Teenagers, Metaphysis Long Bones, MAP (High-Dose MTX, Doxo, Cisplatin), Surgery (Limb Salvage), Good Response = ≥90% Nec |
| 2 | A | Ewing Sarcoma | t(11;22) EWSR1-FLI1, Children/Young Adults, VAC/IE Alternating, Surgery/RT Local Control |
| 3 | A | Chondrosarcoma | Adults >40, IDH1/2 Mut, Surgery Mainstay, RT/Chemo Resistant |
| 4 | A | MAP Protocol | Pre-op: MTX 12g + Doxo 37.5 + Cis 120 q3w ×2-3 → Surgery → Post-op MAP ×4-6 (Adjust by Necrosis) |
| 5 | A | VAC/IE | Alternating q3w: VAC (Vinca/Act-D/Cyclo) ↔ IE (Ifos/Etopo) ×14-17 Cycles Total |
| 6 | A | Limb Salvage | Endoprosthesis >90%, Rotationplasty (Young, Distal Femur/Tibia) |
| 7 | A | Metastases | Lung (All), Skip Mets (Osteo), Bone Marrow (Ewing) |
| 8 | A | Chondrosarcoma | IDH1/2 Mut (50-70%), Grade 1: Marginal, Gr2-3: Wide, Dediff: Surgery + Doxo |
| 9 | A | Dedifferentiated Chondrosarcoma | High-Grade Spindle + Cartilage, Surgery + Doxorubicin |

| 11 | A | FCPS/MRCP High Yield - Bone Sarcomas | FCPS/MRCP High Yield - Bone Sarcomas: Osteosarcoma (35%), Ewing Sarcoma (30%), Chondrosarcoma (25%) |
## 21. Local Navigation


- **Parent Heading Hub**: [[../../Sarcomas|Sarcomas]]
- **Chapter Map**: [[../../Davidson Chapter 7 - Oncology Hierarchy|Oncology Hierarchy]]
- **Chapter MOC**: [[../../Oncology MOC|Oncology MOC]]
- **Drug Reference**: [[../../../Clinical Therapeutics and Good Prescribing|Drugs]]

