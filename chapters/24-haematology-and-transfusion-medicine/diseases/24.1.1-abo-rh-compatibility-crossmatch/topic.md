---
tags: [medicine, haematology, davidson, transfusion-medicine, crossmatch, fcps, mrcp]
davidson_part: Part 3: Clinical Medicine
davidson_chapter: Chapter 25: Haematology and Transfusion Medicine
status: full-fcps-mrcp-note
priority: HIGH
exam_relevance: "FCPS/MRCP High Yield - ABO/Rh compatibility and crossmatching are fundamental to safe transfusion. Key viva: ABO grouping principles, crossmatch techniques (immediate spin, AHG, electronic), antibody screening, and special requirements (irradiated, CMV-, washed)."
see_also: ["Transfusion Reactions", "Red Cell Transfusion", "Platelet Transfusion", "Special Transfusion Situations", "ABO Incompatibility"]
created: 2026-06-15
modified: 2026-06-15
---

# ABO Rh Compatibility & Crossmatch

> [!info]
> **Crossmatch = Final Compatibility Test** between Donor RBCs and Recipient Serum. **Prevents ABO Incompatibility** (Life-Threatening Haemolytic Reaction). **Electronic Crossmatch** (If Antibody Screen Negative) Replaces Serological Crossmatch.

---

## 1. Learning Objectives
By the end of this note you should be able to:
- [ ] Explain ABO and Rh blood group systems and inheritance
- [ ] Apply ABO/Rh compatibility rules for red cell and plasma transfusion
- [ ] Explain antibody screening and identification
- [ ] Differentiate immediate spin vs AHG vs electronic crossmatch
- [ ] Apply special component requirements (irradiated, CMV-, washed)

---

## 2. ABO Blood Group System

| Blood Group | Red Cell Antigens | Plasma Antibodies (Naturally Occurring) | Prevalence (UK) |
|-------------|-------------------|----------------------------------------|-----------------|
| **A** | A | Anti-B | ~42% |
| **B** | B | Anti-A | ~10% |
| **AB** | A, B | **None** | ~4% |
| **O** | **None** | Anti-A, Anti-B | ~44% |

### ABO Compatibility — Red Cell Transfusion
| Recipient | Compatible Donor (Red Cells) |
|-----------|-----------------------------|
| **A** | A, O |
| **B** | B, O |
| **AB** | **A, B, AB, O (Universal Recipient)** |
| **O** | **O Only (Universal Donor)** |

### ABO Compatibility — Plasma/Platelet Transfusion
| Recipient | Compatible Donor (Plasma/Platelets) |
|-----------|------------------------------------|
| **A** | A, AB |
| **B** | B, AB |
| **AB** | **AB Only** |
| **O** | **A, B, AB, O (Universal Plasma Donor)** |

---

## 2. Rh Blood Group System

| Feature | Details |
|---------|---------|
| **Most Immunogenic** | **D Antigen** (RhD) |
| **Rh Positive** | D Antigen Present (~85% UK) |
| **Rh Negative** | D Antigen Absent (~15% UK) |
| **Other Antigens** | C, c, E, e (Clinical Significance in Haemolytic Disease of Fetus/Newborn) |
| **Weak D** | Reduced D Expression → Treat as Rh+ for Donation, Rh- for Recipient |

### Rh Compatibility
| Recipient | Compatible Donor |
|-----------|-----------------|
| **Rh+** | Rh+ or Rh- |
| **Rh-** | **Rh- Only** (Anti-D Formation Risk) |

---

## 3. Crossmatch Techniques

| Method | Principle | Time | Use Case |
|--------|-----------|------|----------|
| **Immediate Spin (IS)** | ABO compatibility only | 2-5 min | Emergency (Type Specific Blood) |
| **Antihuman Globulin (AHG/IAT)** | Detects IgG Antibodies | 30-45 min | **Standard Crossmatch** (If Antibody Screen Positive/Unknown) |
| **Electronic Crossmatch (Computer)** | ABO/Rh Match + **Negative Antibody Screen** | <1 min | **Standard** (If Antibody Screen Negative, Valid Sample) |

### Crossmatch Selection Algorithm
```
PATIENT SAMPLE RECEIVED
         │
         ▼
ABO/Rh TYPING + ANTIBODY SCREEN
         │
         ├── ANTIBODY SCREEN NEGATIVE + VALID SAMPLE (<72h or <7d per policy)
         │       → **ELECTRONIC CROSSMATCH** (Preferred)
         │
         └── ANTIBODY SCREEN POSITIVE / INVALID SAMPLE / EMERGENCY
                 │
                 ├── EMERGENCY (No Time for AHG) → **IMMEDIATE SPIN** (Type-Specific Blood)
                 │
                 └── ROUTINE → **AHG CROSSMATCH** (With Antigen-Negative Units)
```

---

## 3. Antibody Screening & Identification

| Test | Principle | Purpose |
|------|-----------|---------|
| **Antibody Screen** | Patient Serum vs **Screening Cells (2-3 cell panel with known antigens)** | **Detect Unexpected IgG Alloantibodies** |
| **Antibody Identification** | Patient Serum vs **Extended Panel (10-20 cells)** | **Identify Specificity** (Anti-K, Anti-D, Anti-c, Anti-E, Anti-Fya, etc.) |
| **Antibody Titre** | Serial Dilutions | Monitor HDFN, Assess Transfusion Risk |

### Common Clinically Significant Alloantibodies
| Antibody | Blood Group System | Clinical Significance | Crossmatch Requirement |
|----------|-------------------|----------------------|------------------------|
| **Anti-D** | Rh | **HDFN, DHTR** | Antigen-Negative, AHG |
| **Anti-K (Kell)** | Kell | **HDFN (Severe), DHTR** | Antigen-Negative (K-), AHG |
| **Anti-c, Anti-E** | Rh | **HDFN, DHTR** | Antigen-Negative, AHG |
| **Anti-Fyᵃ, Anti-Fyᵇ (Duffy)** | Duffy | **DHTR** | Antigen-Negative, AHG |
| **Anti-Jkᵃ, Anti-Jkᵇ (Kidd)** | Kidd | **DHTR (Delayed, Complement)** | Antigen-Negative, AHG |
| **Anti-M, Anti-N** | MNS | Usually **Not Significant** (IgM, Cold) | IS Only if IgM Only |

---

## 3. Special Component Requirements

| Requirement | Indication | Method |
|-------------|------------|--------|
| **Irradiated (25 Gy)** | **TA-GvHD Prevention** | Gamma/X-ray Irradiation (25 Gy) |
| | Immunocompromised, HSCT, Purine Analogues, Intrauterine, HLA-Matched Relatives, Granulocytes | |
| **CMV-Seronegative** | **CMV Prevention** (Pre-Transplant, Pregnancy, Immunocompromised) | CMV Ab Negative Donor + **Leucodepletion** (UK: Universal Leucodepletion = CMV-Safe) |
| **Washed Red Cells/Platelets** | **IgA Deficiency** (Anti-IgA Anaphylaxis), Recurrent FNHTR, Hyperkalaemia Prevention | Saline Washing (Removes Plasma, Leucocytes, Cytokines) |
| **Frozen/Deglycerolised RBCs** | **Rare Blood Groups**, Long-Term Storage (≥10 Years) | Glycerol Cryopreservation (-80°C/-150°C) |
| **CMV-Negative + Irradiated** | **Intrauterine Transfusion**, Neonatal Exchange | Both Requirements |
| **HEPA Filtration** | **Bacterial Reduction** (Platelets) | Pathogen Reduction Technologies (INTERCEPT, Mirasol) |

---

## 4. Emergency Transfusion (Massive Haemorrhage)

| Phase | Action |
|-------|--------|
| **Immediate (0-10 min)** | **O Negative RBCs (Universal Donor)** — No Crossmatch; **Uncrossmatched**; Group O Rh- (Male) or Rh+ (Female >50) |
| **Urgent (10-30 min)** | **Type-Specific (ABO/Rh Matched)** — Immediate Spin Crossmatch; Group O Rh+ if O Rh- Depleted |
| **Ongoing** | **Fully Crossmatched** (Electronic/AHG) — Switch as Results Available |

### Massive Transfusion Protocol (MTP)
| Component | Ratio (1:1:1 or 1:1:2) | Dose |
|-----------|------------------------|------|
| **RBCs** | 1 | 4-6 Units Initial |
| **FFP** | 1 | 4-6 Units (15 mL/kg) |
| **Platelets** | 1 (or 2) | 1 Adult Dose (1:1:1) or 1:1:2 |
| **Cryoprecipitate** | — | 2 Pools (If Fibrinogen <1.5 g/L) |

---

## 4. Pregnancy & Haemolytic Disease of Fetus/Newborn (HDFN)

| Aspect | Management |
|--------|------------|
| **Routine Antenatal** | ABO/Rh at Booking; **Antibody Screen at 28w** (Anti-D Prophylaxis if Rh-) |
| **Anti-D Prophylaxis** | **500 IU Anti-D Ig IM** at 28w + 34w; Post-Delivery (Within 72h) if Baby Rh+ |
| **Sensitising Events** | **Anti-D Ig** within 72h (Miscarriage, TOP, Amnio, CVS, Trauma, ECV, APH) |
| **Antibody-Positive Mother** | **Serial Antibody Titres** (Monthly <28w, 2-Weekly >28w); Referral if Rising; **Anti-D, Anti-c, Anti-K** = High Risk HDFN |
| **Fetal Monitoring** | MCA Doppler (Peak Systolic Velocity); Intrauterine Transfusion (If Anaemic) |

---

## 4. Platelet & Plasma Compatibility

| Product | ABO Compatibility | Rh Compatibility |
|---------|-------------------|-----------------|
| **Platelets** | **Preferred ABO Identical**; Minor Mismatch OK (ABO Minor) | RhD Match Preferred (If Rh- Recipient, Rh- Preferred) |
| **FFP/Cryoprecipitate** | **ABO Compatible (Major & Minor)** — AB Universal Donor | **Not Required** (No RBCs) |
| **Cryoprecipitate** | ABO Compatible Preferred | Not Required |

---

## 5. Exam Pearls (FCPS/MRCP)

| Topic | Key Point |
|-------|-----------|
| **ABO Universal Donor (RBC)** | **O Negative** |
| **ABO Universal Recipient (RBC)** | **AB Positive** |
| **ABO Universal Donor (Plasma)** | **AB (No Anti-A/B)** |
| **ABO Universal Recipient (Plasma)** | **O Negative** |
| **Crossmatch Types** | **Electronic (Preferred if Antibody Screen Neg)**; AHG (Standard if Pos); IS (Emergency) |
| **Electronic Crossmatch Criteria** | **Antibody Screen Negative + ABO/Rh Match + Valid Sample** |
| **Antibody Screen** | **Detects IgG Alloantibodies** (Anti-K, Anti-D, Anti-c/E, Anti-Fy/Jk) |
| **Clinical Significant Antibodies** | Rh (D, C, c, E, e), Kell (K), Duffy (Fya/Fyb), Kidd (Jka/Jkb) |
| **Non-Significant Antibodies** | Anti-M, Anti-N, Anti-P1, Anti-Lea/Leb (Usually IgM, Cold) |
| **Irradiated Blood (25 Gy)** | **TA-GvHD Prevention**; Immunocompromised, HSCT, Intrauterine, Relatives, Purine Analogues |
| **CMV-Seronegative** | **Leucodepletion = CMV-Safe** (UK Policy); Not Separately Required |
| **Washed Components** | **IgA Deficiency** (Anti-IgA Anaphylaxis); Also Recurrent FNHTR, Hyperkalaemia |
| **Emergency Transfusion** | **O Neg RBCs** (No Crossmatch); Switch to Type-Specific → Fully Crossmatched |
| **MTP Ratio** | **1:1:1 (RBC:FFP:Platelets)** or 1:1:2 |
| **Anti-D Prophylaxis** | **500 IU at 28w + 34w + Post-Delivery** (If Baby Rh+) |
| **HDFN High Risk Antibodies** | **Anti-D, Anti-c, Anti-K** (Severe Anaemia, Hydrops) |
| **Platelet ABO Compatibility** | **Preferred ABO Identical**; Minor Mismatch Acceptable |
| **RhD Matching for Platelets** | Rh- Recipient → Rh- Preferred (If Rh+ Platelets → Anti-D Formation) |
| **Valid Sample for Crossmatch** | **<72h (Electronic) or <7d (Serological) per Hospital Policy** |

---

## 9. Mind Map

```mermaid
mindmap
  root((ABO/Rh Crossmatch))
    ABO System
      A, B, AB, O
      RBC: A→A,O; B→B,O; AB→All; O→O
      Plasma: A→A,AB; B→B,AB; AB→AB; O→All
    Rh System
      D Antigen Most Immunogenic
      Rh+ Recipient: Rh+ or Rh-
      Rh- Recipient: Rh- Only
    Crossmatch
      Electronic: Ab Screen Neg + ABO/Rh Match
      AHG: Ab Screen Pos / Invalid Sample
      Immediate Spin: Emergency (Type-Specific)
    Antibody Screen
      2-3 Cell Panel → Detect IgG Alloantibodies
      If Pos → Antibody ID (10-20 Cell Panel)
    Significant Antibodies
      Rh (D, C, c, E, e), Kell (K), Duffy (Fy), Kidd (Jk)
      HDFN: Anti-D, Anti-c, Anti-K
      DHTR: Anti-Jk, Anti-Fy
    Special Requirements
      Irradiated (25 Gy): TA-GvHD Prevention
      CMV Neg: Leucodepletion = CMV-Safe (UK)
      Washed: IgA Deficiency, Recurrent FNHTR
    Emergency Tx
      O Neg RBCs (No Crossmatch) → Type-Specific → Full Crossmatch
      MTP: 1:1:1 (RBC:FFP:PLT)
    Pregnancy
      Anti-D Prophylaxis 28/34w + Delivery
      Sensitising Events → Anti-D 72h
      HDFN Risk: Anti-D, Anti-c, Anti-K
```

---

## 10. Exam Pearls (FCPS/MRCP)

| Topic | Key Point |
|-------|-----------|
| **RBC Universal Donor** | **O Negative** |
| **RBC Universal Recipient** | **AB Positive** |
| **Plasma Universal Donor** | **AB (No Anti-A/B)** |
| **Crossmatch Preferred** | **Electronic** (Ab Screen Negative) |
| **Antibody Screen** | **Detects IgG Alloantibodies** |
| **Significant Alloantibodies** | Rh (D, c, E), Kell (K), Duffy (Fy), Kidd (Jk) |
| **HDFN High Risk** | Anti-D, Anti-c, Anti-K |
| **Irradiated Blood (25 Gy)** | **TA-GvHD Prevention**; Immunocompromised, Relatives, Intrauterine |
| **CMV-Safe** | **Leucodepletion = CMV-Safe** (UK Universal) |
| **Washed Components** | **IgA Deficiency** (Anti-IgA Anaphylaxis) |
| **Emergency Blood** | **O Neg RBCs** (No Crossmatch) |
| **MTP Ratio** | **1:1:1 (RBC:FFP:PLT)** |
| **Anti-D Prophylaxis** | **500 IU at 28w, 34w, + Delivery** |
| **Rh- Recipient Platelets** | **Rh- Preferred** (Anti-D Prevention) |
| **Ab Screen Positive** | → **AHG Crossmatch + Antigen-Negative Units** |

---

## 10. Local Navigation (for Dashboard UI)

> **Parent**: [[../Transfusion Medicine|Transfusion Medicine]]  
> **Hierarchy**: [[../../Davidson Chapter 25 - Haematology Hierarchy|Haematology Hierarchy]]  
> **Template**: [[../../../Templates/Hematology Topic Template|Hematology Topic Template]]  
> **See also**: [[Transfusion Reactions]], [[Red Cell Transfusion]], [[Platelet Transfusion]], [[Special Transfusion Situations]], [[Massive Transfusion Protocol]]
---

> Auto-generated study sections for "Hematology" — Ch 24: Haematology & Transfusion Medicine.

## Flashcards (20 generated)

- Q: What is the definition of Hematology?
  A: Crossmatch = Final Compatibility Test between Donor RBCs and Recipient Serum.
- Q: What is Most Immunogenic of Hematology?
  A: D Antigen (RhD)
- Q: What is Rh Positive of Hematology?
  A: D Antigen Present (~85% UK)
- Q: What is Rh Negative of Hematology?
  A: D Antigen Absent (~15% UK)
- Q: What is Other Antigens of Hematology?
  A: C, c, E, e (Clinical Significance in Haemolytic Disease of Fetus/Newborn)
- Q: What is Weak D of Hematology?
  A: Reduced D Expression → Treat as Rh+ for Donation, Rh- for Recipient
- Q: What is Routine Antenatal of Hematology?
  A: ABO/Rh at Booking; Antibody Screen at 28w (Anti-D Prophylaxis if Rh-)
- Q: What is Anti-D Prophylaxis of Hematology?
  A: 500 IU Anti-D Ig IM at 28w + 34w; Post-Delivery (Within 72h) if Baby Rh+
- Q: What is Sensitising Events of Hematology?
  A: Anti-D Ig within 72h (Miscarriage, TOP, Amnio, CVS, Trauma, ECV, APH)
- Q: What is Antibody-Positive Mother of Hematology?
  A: Serial Antibody Titres (Monthly <28w, 2-Weekly >28w); Referral if Rising; Anti-D, Anti-c, Anti-K = High Risk HDFN
- Q: How is Hematology monitored?
  A: MCA Doppler (Peak Systolic Velocity); Intrauterine Transfusion (If Anaemic)
- Q: What is Most Immunogenic of Hematology?
  A: D Antigen (RhD)
- Q: What is Rh Positive of Hematology?
  A: D Antigen Present (~85% UK)
- Q: What is Rh Negative of Hematology?
  A: D Antigen Absent (~15% UK)
- Q: What is Other Antigens of Hematology?
  A: C, c, E, e (Clinical Significance in Haemolytic Disease of Fetus/Newborn)
- Q: What is Routine Antenatal of Hematology?
  A: ABO/Rh at Booking; Antibody Screen at 28w (Anti-D Prophylaxis if Rh-)
- Q: What is Anti-D Prophylaxis of Hematology?
  A: 500 IU Anti-D Ig IM at 28w + 34w; Post-Delivery (Within 72h) if Baby Rh+
- Q: What is Sensitising Events of Hematology?
  A: Anti-D Ig within 72h (Miscarriage, TOP, Amnio, CVS, Trauma, ECV, APH)
- Q: What is Antibody-Positive Mother of Hematology?
  A: Serial Antibody Titres (Monthly <28w, 2-Weekly >28w); Referral if Rising; Anti-D, Anti-c, Anti-K = High Risk HDFN
- Q: How is Hematology monitored?
  A: MCA Doppler (Peak Systolic Velocity); Intrauterine Transfusion (If Anaemic)

## MCQs (1 generated)

1. **Which of the following best describes Hematology?**
   A. **Crossmatch = Final Compatibility Test between Donor RBCs and Recipient Serum.**
   B. An unrelated condition not matching the clinical picture of Hematology
   C. A complication seen late in the disease course of Hematology
   D. A condition that mimics Hematology but has a different underlying cause

## SBA Questions (1 generated)

1. A patient with suspected Hematology presents with: Antibody — Blood Group System; Anti-K (Kell) — Kell; Anti-c, Anti-E — Rh. What is the most likely diagnosis?
   A. **Hematology**
   B. A condition that mimics Hematology but is not the same entity
   C. A complication of Hematology rather than the primary diagnosis
   D. An unrelated condition in the same clinical category as Hematology

