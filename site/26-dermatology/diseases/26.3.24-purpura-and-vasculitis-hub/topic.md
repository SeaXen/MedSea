# Purpura and Vasculitis Hub

---
tags: [medicine, dermatology, topic-group-hub, scaffold-hub]
davidson_part: Part 3: Clinical Medicine
davidson_chapter: Chapter 29: Dermatology
heading: Urticaria, Erythema & Purpura
topic_group: Purpura & Vasculitis
topic:
status: full-fcps-mrcp-hub
priority: critical
created: 2026-06-15
modified: 2026-06-15
exam_relevance: [FCPS, MRCP Part 1, MRCP Part 2, PACES]
see_also:
  - "[[Urticaria Erythema Purpura Hub]]"
  - "[[Dermatology MOC]]"
---

# Purpura & Vasculitis Hub

> [!info]
> **Topic Group 3.4** | **8 Disease Topics** | **Priority: CRITICAL**

---

## Disease Topics in this Group

| # | Topic | Status | Priority |
|---|-------|--------|----------|
| 1 | Palpable purpura approach | 🔴 scaffold | Critical |
| 2 | IgA vasculitis (Henoch-Schönlein purpura) | 🔴 scaffold | Critical |
| 3 | ANCA-associated vasculitis (cutaneous) | 🔴 scaffold | Critical |
| 4 | Cryoglobulinaemic vasculitis | 🔴 scaffold | High |
| 5 | Urticarial vasculitis | 🔴 scaffold | High |
| 6 | Cutaneous polyarteritis nodosa | 🔴 scaffold | High |
| 7 | Livedoid vasculopathy | 🔴 scaffold | Medium |
| 8 | Purpura fulminans | 🔴 scaffold | Critical |

---

## High-Yield Summary

| Vasculitis | Key Clinical | Histology/DIF | Serology | 1st Line |
|------------|--------------|---------------|----------|----------|
| **IgA Vasculitis (HSP)** | Palpable purpura (legs/buttocks), abdominal pain, arthritis, renal | Leukocytoclastic + **IgA dominant vessel deposits** | IgA ↑, ANA -ve, ANCA -ve | Supportive, steroids if renal/GI |
| **ANCA Vasculitis (Cutaneous)** | Purpura + systemic (renal, lung, ENT, nerves) | LCV + IgG/IgM/C3 vessels | **c-ANCA/PR3 = GPA**, **p-ANCA/MPO = MPA/EGPA** | Induction: CYC/RTX + steroids |
| **Cryoglobulinaemic** | Purpura (cold-induced), arthralgia, weakness, renal, neuropathy | LCV + IgM/IgG/C3, **intravascular thrombi** | **Cryoglobulins +ve, Rheumatoid factor +ve, Low C4** | Treat cause (HCV), Rituximab + steroids |
| **Urticarial Vasculitis** | Wheals >24h, purpuric, burning, hypocomplementaemic | LCV + C1q deposits | **Low C3/C4, Anti-C1q +ve**, ANA +ve (lupus) | H1 → HCQ → Dapsone → Immunosuppress |
| **Cutaneous PAN** | Nodular lesions, livedo, ulcers, peripheral neuropathy, **no systemic** | Medium vessel NEC, necrotising inflammation | ANCA -ve, Hep B -ve | Steroids + immunosuppressant (AZA/MMF) |
| **Livedoid Vasculopathy** | Painful ulcers (ankles), atrophie blanche, livedo racemosa, summer worse | Fibrin deposition, minimal inflammation | Hypercoagulable workup (APS, Factor V Leiden) | Anticoagulation, pentoxifylline, danazol |
| **Purpura Fulminans** | Rapid necrosis, DIC, adrenal haemorrhage (Waterhouse-Friderichsen), meningococcaemia | Vascular thrombosis, necrosis, DIC | **Meningococcus, Sepsis, DIC screen** | **EMERGENCY: Antibiotics, Fluids, Vasopressors, FFP, Protein C** |

---

## Key Algorithms

### Palpable Purpura Diagnostic Approach
```mermaid
flowchart TD
    A[Palpable Purpura] --> B[Urgent: FBC, U&E, LFT, CRP, Urine ACR, Coagulation, Blood cultures]
    B --> C{Systemic Features?}
    C -->|Yes (Renal, Lung, ENT, Neuro)| D[ANCA, Cryoglobulins, C3/C4, ANA, Hep B/C, HIV, Biopsy]
    C -->|No (Cutaneous Only)| E[Biopsy: LCV + DIF]
    D & E --> F{DIF/Serology}
    F -->|IgA dominant vessels| G[IgA Vasculitis HSP]
    F -->|c-ANCA/PR3 +ve| H[GPA]
    F -->|p-ANCA/MPO +ve| I[MPA/EGPA]
    F -->|Cryoglobulins +ve, Low C4| J[Cryoglobulinaemic Vasculitis]
    F -->|Low C3/C4, Anti-C1q| K[Urticarial Vasculitis / Lupus]
    F -->|Medium vessel, ANCA -ve| L[Cutaneous PAN]
```

### IgA Vasculitis (HSP) Tetrad
```mermaid
flowchart TD
    A[IgA Vasculitis HSP] --> B1[Palpable Purpura: Legs/Buttocks, symmetric]
    A --> B2[Abdominal Pain: Colicky, intussusception risk]
    A --> B3[Arthritis: Knees/Ankles, migratory, non-erosive]
    A --> B4[Renal: Haematuria/Proteinuria, IgA nephropathy]
    B1 & B2 & B3 & B4 --> C[Biopsy: LCV + IgA vessel deposits]
    C --> D[Urine ACR monitoring 6-12m]
    D --> E{Renal Involvement}
    E -->|Yes| F[Steroids ± Immunosuppressant (AZA/MMF)]
    E -->|No| G[Supportive, NSAIDs for arthritis]
```

---

## FCPS/MRCP Viva Topics

1. **Palpable purpura approach** - urgent bloods (FBC, U&E, urine ACR, coagulation), biopsy (LCV + DIF), ANCA, cryoglobulins, complement
2. **IgA Vasculitis (HSP)** - tetrad (purpura, abdominal pain, arthritis, renal), IgA deposits, children > adults, urine monitoring 6-12m
3. **ANCA vasculitis** - c-ANCA/PR3 = GPA; p-ANCA/MPO = MPA/EGPA; cutaneous = LCV, systemic = CYC/RTX + steroids
4. **Cryoglobulinaemic vasculitis** - HCV association, cold-induced purpura, RF +ve, low C4, treat HCV + Rituximab
5. **Urticarial vasculitis** - wheals >24h, burning, purpuric, low C3/C4, anti-C1q, SLE association, HCQ/dapsone
6. **Cutaneous PAN** - nodular lesions, livedo, ulcers, neuropathy, **medium vessel**, ANCA -ve, Hep B -ve
7. **Livedoid vasculopathy** - painful ankle ulcers, atrophie blanche, livedo racemosa, hypercoagulable state, anticoagulation
8. **Purpura fulminans** - meningococcaemia, DIC, adrenal haemorrhage, **EMERGENCY**: ceftriaxone, fluids, FFP, protein C concentrate
9. **Differential of purpura** - palpable (vasculitis), non-palpable (thrombocytopenia, coagulation, senile), pressure-induced
10. **LCV histology** - neutrophilic infiltrate, nuclear dust (leukocytoclasis), fibrin, vessel damage, DIF for immunoglobulin typing

---

## Mnemonics

- **HSP Tetrad:** `PARK` = **P**urpura (palpable, legs), **A**bdominal pain, **R**enal (haematuria), **K**nees/ankles arthritis
- **ANCA patterns:** `CANCA` = **C**-ANCA = **P**R3 = **G**PA; **P-ANCA** = **MPO** = **M**PA/**E**GPA
- **Cryoglobulins:** `CRYOGLOB` = **C**old-induced purpura, **R**F +ve, **Y**... **O**HCV, **G**lomerulonephritis, **L**ow C4, **O**intravascular thrombi, **B**iopsy = LCV
- **Urticarial vasculitis:** `UV WHEAL` = **U**rticarial **V**asculitis = **W**heals >24h, **H**ypocomplementaemic, **E**xtravascular? No - **B**urning not itch, **A**nti-C1q, **L**upus association

---

## Linkage

- **Parent Hub:** [[Urticaria Erythema Purpura Hub]]
- **MOC:** [[Dermatology MOC]]
- **Disease Topics:** See individual files in `03_Urticaria_Erythema_Purpura/`

---

## Progress
- [ ] Palpable purpura approach (scaffold → full)
- [ ] IgA vasculitis (scaffold → full)
- [ ] ANCA-associated vasculitis (scaffold → full)
- [ ] Cryoglobulinaemic vasculitis (scaffold → full)
- [ ] Urticarial vasculitis (scaffold → full)
- [ ] Cutaneous polyarteritis nodosa (scaffold → full)
- [ ] Livedoid vasculopathy (scaffold → full)
- [ ] Purpura fulminans (scaffold → full)