# Figurate Erythemas Hub

---
tags: [medicine, dermatology, topic-group-hub, scaffold-hub]
davidson_part: Part 3: Clinical Medicine
davidson_chapter: Chapter 29: Dermatology
heading: Urticaria, Erythema & Purpura
topic_group: Figurate Erythemas
topic:
status: full-fcps-mrcp-hub
priority: high
created: 2026-06-15
modified: 2026-06-15
exam_relevance: [FCPS, MRCP Part 1, MRCP Part 2, PACES]
see_also:
  - "[[Urticaria Erythema Purpura Hub]]"
  - "[[Dermatology MOC]]"
---

# Figurate Erythemas Hub

> [!info]
> **Topic Group 3.3** | **4 Disease Topics** | **Priority: HIGH**

---

## Disease Topics in this Group

| # | Topic | Status | Priority |
|---|-------|--------|----------|
| 1 | Erythema annulare centrifugum | 🔴 scaffold | High |
| 2 | Erythema marginatum | 🔴 scaffold | High |
| 3 | Erythema gyratum repens | 🔴 scaffold | Medium |
| 4 | Subacute cutaneous lupus erythematosus | 🔴 scaffold | High |

---

## High-Yield Summary

| Condition | Key Clinical | Association | Histology | Management |
|-----------|--------------|-------------|-----------|------------|
| **Erythema Annulare Centrifugum (EAC)** | Expanding annular erythema, trailing scale inside border, asymptomatic/pruritic | Idiopathic, drugs, infections, malignancy (rare) | Superficial/deep perivascular lymphocytic, no interface change | Treat cause, topical TCS, antihistamines, dapsone |
| **Erythema Marginatum** | Transient pink rings, non-pruritic, truncal, evanescent (hours), **RF/ARF** | **Acute Rheumatic Fever** (Jones criteria major), also SLE, drugs | Superficial perivascular, oedema, minimal inflammation | Treat underlying (penicillin for ARF), NSAIDs |
| **Erythema Gyratum Repens (EGR)** | Rapidly moving concentric waves/gyrations, "wood grain", strongly associated with **malignancy** | **Lung, breast, GI, GU cancers** (80%); paraneoplastic | Superficial perivascular lymphocytic | **Treat underlying malignancy**; topical TCS |
| **Subacute Cutaneous Lupus (SCLE)** | Annular or psoriasiform plaques, photo-distributed, non-scarring, **Anti-Ro/SSA +ve (70-90%)** | SLE (50% develop), Sjögren, drug-induced (hydrochlorothiazide, PPI, TNFα) | Interface dermatitis, vacuolar basal degeneration, mucin | **Sun protection**, Hydroxychloroquine, TCS, avoid triggers |

---

## Key Algorithms

### Figurate Erythema Differential
```mermaid
flowchart TD
    A[Figurate Erythema] --> B{Scale inside border (trailing)?}
    B -->|Yes| C[Erythema Annulare Centrifugum]
    B -->|No| D{Transient, evanescent, non-pruritic?}
    D -->|Yes| E[Erythema Marginatum: Think ARF!]
    D -->|No| F{Rapidly moving concentric waves?}
    F -->|Yes| G[Erythema Gyratum Repens: SCREEN FOR CANCER]
    F -->|No| H{Photo-distributed, Anti-Ro+?}
    H -->|Yes| I[Subacute Cutaneous Lupus]
    H -->|No| J[Other: Erythema migrans (Lyme), Figurate drug eruption, Granuloma annulare]
```

### SCLE Diagnostic Criteria
```mermaid
flowchart TD
    A[Suspected SCLE] --> B[Clinical: Annular/psoriasiform, photo-distributed, non-scarring]
    B --> C[Serology: ANA +, **Anti-Ro/SSA + (70-90%)**, Anti-La/SSB + (30-50%)]
    C --> D[Biopsy: Interface dermatitis, vacuolar change, mucin]
    D --> E[Drug Review: HCTZ, PPI, TNFα, Ca-channel blockers, terbinafine]
    E --> F[Screen for SLE/Sjögren: dsDNA, complement, Schirmer, salivary flow]
```

---

## FCPS/MRCP Viva Topics

1. **Erythema Annulare Centrifugum** - trailing scale (inside border), expanding rings, idiopathic/drug/malignancy, dapsone for persistent
2. **Erythema Marginatum** - evanescent (hours), non-pruritic, truncal, **ARF major criterion**, also SLE/drugs
3. **Erythema Gyratum Repens** - "wood grain" concentric waves, **MALIGNANCY 80%** (lung, breast, GI), paraneoplastic
4. **Subacute Cutaneous Lupus** - annular/psoriasiform, photo-distributed, **Anti-Ro/SSA 70-90%**, drug-induced (HCTZ, PPI, TNFα), HCQ 1st line
5. **Figurate erythema DDx** - EAC (trailing scale), E. marginatum (evanescent, ARF), E. migrans (Lyme, target), E. gyratum (cancer), SCLE (photo, Anti-Ro), Granuloma annulare (dermal, no scale)
6. **Drug-induced SCLE** - hydrochlorothiazide, PPIs, TNFα inhibitors, calcium channel blockers, terbinafine, anti-TNF paradoxical
7. **Erythema Migrans (Lyme)** - expanding erythema from tick bite, central clearing, Borrelia, doxycycline
8. **Granuloma Annulare** - dermal nodules/rings, no scale, necrobiotic granulomas, self-limiting, TCS/Injection

---

## Mnemonics

- **Figurate types:** `EAC MARGIN GYRATUM SCLE` = **EAC** = traling sc**ALE**; **MARGIN**atum = e**VAN**escent, **ARF**; **GYRATUM** = **GYR**ating waves = **C**ancer; **SCLE** = **S**ubacute **C**utaneous **L**upus = **A**nti-**Ro**, **P**hoto
- **EAC trailing scale:** `INSIDE` = Scale on **INSIDE** of advancing border (trailing)
- **E. marginatum:** `EVANESCENT` = Lasts **HOURS**, non-pruritic, **ARF**
- **EGR cancer:** `EGR CANCER` = **E**rythema **G**yrata **R**epens → **C**ancer (Lung, Breast, GI, GU)

---

## Linkage

- **Parent Hub:** [[Urticaria Erythema Purpura Hub]]
- **MOC:** [[Dermatology MOC]]
- **Disease Topics:** See individual files in `03_Urticaria_Erythema_Purpura/`

---

## Progress
- [ ] Erythema annulare centrifugum (scaffold → full)
- [ ] Erythema marginatum (scaffold → full)
- [ ] Erythema gyratum repens (scaffold → full)
- [ ] Subacute cutaneous lupus erythematosus (scaffold → full)