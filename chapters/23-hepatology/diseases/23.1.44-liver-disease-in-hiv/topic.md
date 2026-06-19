---
tags: [hepatology, special_situations, hiv, viral_hepatitis, coinfection, fcps, mrcp]
davidson_chapter: Chapter 24
status: full-fcps-mrcp-note
priority: high
exam_relevance: "Liver disease in HIV - HBV/HCV coinfection, ART hepatotoxicity, ART selection, immune reconstitution - FCPS/MRCP HIV-hepatology interface"
see_also: ["Viral Hepatitis/Hepatitis B", "Viral Hepatitis/Hepatitis C", "Viral Hepatitis/Hepatitis B HIV coinfection", "Viral Hepatitis/Hepatitis C HIV coinfection", "Hepatology in Special Situations/Viral Hepatitis in Pregnancy"]
created: 2025-06-13
modified: 2025-06-13
---

# Liver Disease in HIV

## Learning Objectives
- [ ] Manage HBV/HIV and HCV/HIV coinfection
- [ ] Select ART with minimal hepatotoxicity
- [ ] Monitor for ART-induced liver injury
- [ ] Manage immune reconstitution inflammatory syndrome (IRIS)
- [ ] Identify FCPS/MRCP high-yield HIV-hepatology intersections

---

## HIV and Liver Disease: Overview

```mermaid
flowchart TD
    A[HIV + Liver Disease] --> B[Coinfection: HBV, HCV]
    A --> C[ART Hepatotoxicity]
    A --> D[Immune Reconstitution (IRIS)]
    A --> E[Opportunistic Infections]
    A --> F[Drug-Induced Liver Injury]
    A --> G[NAFLD/Metabolic]
    A --> H[Malignancy: Lymphoma, KS, HCC]
```

---

## HBV/HIV Coinfection

### Epidemiology
| Feature | Detail |
|--------|--------|
| **Global Coinfection** | ~2.7 Million (7-10% of PLHIV) |
| **High-Risk** | Sub-Saharan Africa, Asia, PWID, MSM |
| **Impact** | **Accelerated Fibrosis**, ↓ Spontaneous Clearance, ↑ HCC Risk |

### Natural History
| Feature | HBV Mono | HBV/HIV Coinfection |
|--------|----------|---------------------|
| **Progression** | Slow | **Accelerated 2-3x** |
| **HBV DNA** | Variable | **Higher Levels** |
| **HBeAg Seroconversion** | Normal | **Delayed** |
| **Cirrhosis Risk** | 15-20% at 20y | **Higher, Earlier** |
| **HCC Risk** | Increased | **Further Increased** |

### Management Principles
| Principle | Detail |
|----------|--------|
| **Treat ALL** | Regardless of CD4, Fibrosis Stage |
| **ART First** | Start ART with TDF/FTC or TAF/FTC Backbone (Covers HBV) |
| **HBV Therapy** | Continue Lifetime (Even if HBsAg Loss) |
| **Monitor** | HBV DNA, HBsAg, LFTs q3-6mo |

### ART Selection for HBV/HIV
| Preferred | Avoid |
|-----------|-------|
| **TDF/FTC** (or TAF/FTC) + DTG/BIC/RAL | ZDV + 3TC (Less Potent HBV Coverage) |
| **TDF/FTC Preferred** if eGFR >30 | **3TC Monotherapy** (HBV Resistance Risk) |

### Key Interactions
| Drug | Interaction |
|------|-------------|
| **TDF** | ↑ Tenofovir Levels with Boosted PI; Monitor Renal |
| **TAF** | ↑ Levels with Strong CYP3A4 Inhibitors (Boosted PI) |
| **ETV** | No Significant HIV Drug Interactions |

---

## HCV/HIV Coinfection

### Epidemiology
| Feature | Detail |
|--------|--------|
| **Global Coinfection** | ~2.3 Million |
| **Transmission** | Shared Routes (IVDU, Sexual-MSMS, Blood) |
| **Fibrosis Progression** | **2-3x Faster** (Even on ART) |
| **Spontaneous Clearance** | Reduced (5-15% vs 15-25%) |

### Treatment Principles
| Principle | Detail |
|---------|--------|
| **Same Efficacy** | **DAA SVR >95%** (Same as Mono) |
| **Same Duration** | **No Extension** for Coinfection |
| **Same Regimens** | **Pan-Genotypic Preferred** |
| **Priority** | **Treat ALL** — Regardless of CD4, Fibrosis |
| **ART Continuation** | **Do NOT Stop ART** for HCV Treatment |

---

## Recommended Regimens (Pan-Genotypic)

### 1. Sofosbuvir/Velpatasvir (SOF/VEL) — **PREFERRED First-Line**
| Aspect | Detail |
|-------|--------|
| **Regimen** | SOF 400mg / VEL 100mg Once Daily |
| **Duration** | 12 Weeks (All Genotypes, All Fibrosis) |
| **Key Advantage** | **Minimal ART Interactions** — Fewest Drug Interactions |
| **ART Compatibility** | Compatible with Most ART (INSTI, NNRTI, Some PIs) |
| **eGFR <30** | **Avoid** (Sofosbuvir Accumulation) |

### 2. Glecaprevir/Pibrentasvir (GLE/PIB) — **Alternative**
| Aspect | Detail |
|-------|--------|
| **Regimen** | 3 Tablets (300/120mg) Once Daily |
| **Duration** | 8 Weeks (Naive, Non-Cirrhotic); 12 Weeks (Cirrhotic/Experienced) |
| **Key Caveat** | **Drug Interactions with Boosted PIs** (Ritonavir/Cobicistat-Boosted) — ↑ GLE/PIB Levels |
| **eGFR <30** | **Safe** (Preferred in Renal Impairment) |
| **ART Compatibility** | Check Interactions (Avoid with Boosted DRV/ATV/LPV/r) |

### 3. Sofosbuvir/Velpatasvir/Voxilaprevir (SOF/VEL/VOX) — **Retreatment**
| Aspect | Detail |
|-------|--------|
| **Indication** | DAA Failure (NS5A/NS5B Resistance) |
| **Duration** | 12 Weeks |
| **Interactions** | Voxilaprevir + Boosted PIs → ↑ Levels (Avoid) |

---

## Critical Drug Interactions (DAAs with ART)

```mermaid
flowchart TD
    A[DAA + ART Combination] --> B{DAA Class}
    B -->|SOF/VEL| C[Minimal Interactions]
    C --> D[Compatible: INSTI, NNRTI, Unboosted PI]
    C --> E[Monitor: Boosted PI (DRV/r, ATV/r, LPV/r) → ↑ VEL]
    B -->|GLE/PIB| F[Significant with Boosted PI]
    F --> G[AVOID: DRV/r, ATV/r, LPV/r, TPV/r]
    F --> H[OK: INSTI (DTG, BIC, RAL), NNRTI (EFV, RPV, DOR)]
    B -->|SOF/VEL/VOX| I[Voxilaprevir = PI]
    I --> J[Same as GLE/PIB: Avoid Boosted PI]
```

### Key Interaction Table

| DAA | ART Class | Interaction | Management |
|-----|-----------|-------------|------------|
| **SOF/VEL** | **INSTI (DTG, BIC, RAL)** | **None** | Preferred |
| **SOF/VEL** | **NNRTI (EFV, RPV, DOR)** | **None/Minimal** | OK |
| **SOF/VEL** | **Boosted PI (DRV/r, ATV/r, LPV/r)** | ↑ VEL Levels (CYP3A4/P-gp Inhibition) | **Monitor VEL Toxicity**; Consider Dose Adjust or Alternate DAA |
| **GLE/PIB** | **Boosted PI (DRV/r, ATV/r, LPV/r)** | **↑↑ GLE/PIB Levels** (Strong CYP3A4/P-gp Inhib) | **CONTRAINDICATED / AVOID** |
| **GLE/PIB** | **INSTI / NNRTI** | Minimal | Safe |
| **SOF/VEL/VOX** | **Boosted PI** | ↑ VOX Levels | **Avoid** |

---

## IRIS (Immune Reconstitution Inflammatory Syndrome)

| Feature | Detail |
|--------|--------|
| **Definition** | **Paradoxical Worsening** of Liver Inflammation After Starting ART (or HCV Treatment) |
| **Timing** | **4-12 Weeks** After ART Initiation (or HCV DAA Start) |
| **Clinical** | ALT Flares, Jaundice, Hepatic Decompensation |
| **Mechanism** | Immune Recovery → Enhanced HCV/HBV-Specific Response |
| **Risk Factors** | Low CD4 (<200), High HIV VL, Advanced Fibrosis, Recent ART Start |
| **Management** | **Continue Both ART + DAA** (Usually Self-Limited); **Corticosteroids if Severe** (Pred 0.5-1mg/kg) |

> **IRIS vs DILI vs Reactivation** — Timing from ART/DAA Start, Pattern of LFTs, Histology if Biopsy

---

## Special Situations

### Decompensated Cirrhosis (Child B/C) + HIV
| Regimen | Duration |
|---------|----------|
| **SOF/VEL + RBV** | 12 Weeks |
| **GLE/PIB** | **CONTRAINDICATED** |
| **SOF/VEL/VOX** | **CONTRAINDICATED** |

### Renal Impairment (eGFR <30) + HIV
| Regimen | Notes |
|---------|-------|
| **GLE/PIB** | **Preferred** (No Dose Adjustment) |
| **SOF/VEL** | **Avoid** (<30) |
| **ART Interaction** | Monitor CBC (Zidovudine), Renal (TDF) |

### Hepatitis B Triple Coinfection (HIV/HBV/HCV)
| Priority | Action |
|----------|--------|
| **1. HIV** | **ART with TDF/FTC or TAF/FTC** (Cover HBV + HIV) |
| **2. HCV** | **DAA After ART Stable** (Or Concurrent if Indicated) |
| **HBV** | **Covered by TDF/FTC or TAF/FTC in ART** |

---

## Non-ART Drug-Induced Liver Injury in HIV

| Drug Class | Examples | Pattern |
|------------|----------|---------|
| **Antimicrobials** | Cotrimoxazole, Rifampicin, Isoniazid, Fluconazole | Variable |
| **Antiretrovirals** | NVP (Hypersensitivity), EFV (Steatosis), PI (Hyperlipidaemia) | Variable |
| **Anticonvulsants** | Phenytoin, Valproate, Carbamazepine | Hepatocellular |
| **Herbal/OTC** | Green Tea, Kava, Ayurvedic | Variable |

---

## FCPS/MRCP High-Yield Summary

| Concept | Key Points |
|---------|------------|
| **SVR Rates** | **>95%** in Coinfection (Same as Mono) |
| **Regimens** | **Same Duration, Same Regimens** — No Extension for HIV |
| **First-Line** | **SOF/VEL** (Minimal ART Interactions) |
| **Alternative** | **GLE/PIB** (Avoid with Boosted PI) |
| **Retreatment** | **SOF/VEL/VOX** (Avoid Boosted PI) |
| **Decompensated** | **SOF/VEL + RBV ONLY** |
| **Renal Impairment** | **GLE/PIB Preferred** (<30 eGFR) |
| **Boosted PI + VEL/PIB/VOX** | **↑ Levels** — Avoid/Monitor; **INSTI/NNRTI Preferred** |
| **IRIS** | ALT Flare 4-12w Post-ART/DAA — Continue Both, Steroids if Severe |
| **Priority** | **Treat HCV First** (If CD4>500) OR **Concurrent** — Don't Delay |

---

## Viva Questions

1. **What is the preferred DAA regimen for HCV-HIV coinfection?**
2. **Which ART class has minimal interaction with SOF/VEL?**
3. **Why is GLE/PIB avoided with boosted PIs?**
3. **What is IRIS in HCV-HIV coinfection? How to manage?**
4. **Can you use GLE/PIB in eGFR <30 with HIV?**
5. **What is the preferred regimen for decompensated cirrhosis + HIV?**
6. **How do you manage HIV/HBV/HCV triple coinfection?**
7. **What is the SVR rate in HCV-HIV coinfection?**
8. **Why are INSTIs preferred with DAAs?**
9. **Do you need to extend DAA duration in HIV coinfection?**
10. **What is the drug interaction between VEL and DRV/r?**

---

## Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| SOF/VEL vs GLE/PIB in HIV | **SOF/VEL = Minimal Interactions (Preferred)**; GLE/PIB = Avoid Boosted PI |
| SVR in Coinfection | **Same >95%** — No Duration Extension for HIV |
| Boosted PI + DAA | **DRV/r, ATV/r, LPV/r, TPV/r** increase PI/DAA levels — Monitor or Avoid |
| INSTI/NNRTI + DAA | **Compatible** — DTG, BIC, RAL, EFV, RPV, DOR |
| Decompensated + HIV | **SOF/VEL + RBV ONLY** — GLE/PIB, VOX Contraindicated |
| CKD + HIV + HCV | **GLE/PIB Preferred** (Safe All eGFR) |
| IRIS Timing | **4-12 Weeks** After ART/DAA Start — Self-Limited, Steroids if Severe |
| TDF in HIV | Part of ART (TDF/FTC or TAF/FTC) — Also Covers HBV |

---

## Mind Map

```mermaid
mindmap
  root((HCV-HIV Coinfection))
    Principles
      SVR >95% Same as Mono
      Same Regimens / Duration
      Treat All - Priority
    First-Line
      SOF/VEL 12w (Minimal Interactions)
    Alternative
      GLE/PIB 8-12w (Avoid Boosted PI)
    Retreatment
      SOF/VEL/VOX 12w
    Interactions
      SOF/VEL: INSTI/NNRTI OK; Boosted PI ↑ VEL
      GLE/PIB: Avoid Boosted PI (Contraindicated)
      VOX: Same as PIB
      INSTI/NNRTI: Preferred with DAA
    Special
      Decompensated: SOF/VEL+RBV Only
      CKD: GLE/PIB Preferred
      Triple HBV: HIV Art (TDF/FTC) → HCV DAA
    IRIS
      4-12w Post ART/DAA
      ALT Flare → Continue Both, Steroids if Severe
```

---

## One-Page Revision Card

| **Coinfection Principle** | **Detail** |
|---------------------------|------------|
| **SVR Rate** | >95% (Same as Mono) |
| **Duration** | Same (No Extension) |
| **Priority** | Treat All — No CD4 Threshold |

| **Regimen** | **Duration** | **Key Interaction** |
|-------------|--------------|---------------------|
| **SOF/VEL** (1st Line) | 12w | Minimal with INSTI/NNRTI |
| **GLE/PIB** (Alt) | 8-12w | **AVOID Boosted PI** |
| **SOF/VEL/VOX** (Retx) | 12w | Avoid Boosted PI |

| **ART Class** | **SOF/VEL** | **GLE/PIB** | **VOX** |
|---------------|-------------|-------------|---------|
| INSTI (DTG, BIC, RAL) | ✓ | ✓ | ✓ |
| NNRTI (EFV, RPV) | ✓ | ✓ | ✓ |
| Boosted PI (DRV/r) | Monitor VEL | **CONTRAINDICATED** | Avoid |

| **Special** | **Management** |
|-------------|----------------|
| Decompensated + HIV | SOF/VEL + RBV ONLY |
| CKD + HIV | GLE/PIB Preferred |
| Triple HBV/HIV/HCV | ART (TDF/FTC) → HCV DAA |

| **IRIS** | **Management** |
|----------|----------------|
| 4-12w Post ART/DAA | ALT Flare → Continue Both, Steroids if Severe |

---

## Spaced Repetition Tracker

| Day | 1 | 3 | 7 | 15 | 30 |
|-----|---|---|---|----|----|
| Preferred Regimen Coinfection | ☐ | ☐ | ☐ | ☐ | ☐ |
| Interaction Table | ☐ | ☐ | ☐ | ☐ | ☐ |
| Boosted PI Avoidance | ☐ | ☐ | ☐ | ☐ | ☐ |
| IRIS Management | ☐ | ☐ | ☐ | ☐ | ☐ |
| Special Situations | ☐ | ☐ | ☐ | ☐ | ☐ |

---

## Self-Test Scorecard

| Question | My Answer | Correct? |
|----------|-----------|----------|
| Preferred Regimen Coinfection |  |  |
| BOOSTED PI + GLE/PIB |  |  |
| IRIS Timing |  |  |
| CKD + HIV + HCV |  |  |
| Decompensated + HIV |  |  |

---

## Local Navigation

- [[Viral Hepatitis/Hepatitis C|HCV Overview]]
- [[Viral Hepatitis/Hepatitis C genotype-based treatment|HCV Genotype Treatment]]
- [[Viral Hepatitis/HCV DAA Regimens by Genotype & Cirrhosis|HCV DAA Regimens]]
- [[Viral Hepatitis/Hepatitis C decompensated cirrhosis management|HCV Decompensated]]
- [[Viral Hepatitis/Hepatitis C renal impairment|HCV Renal]]