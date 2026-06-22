## 1. Learning Objectives
- [ ] Manage HBV/HIV and HCV/HIV coinfection
- [ ] Select ART with minimal hepatotoxicity
- [ ] Monitor for ART-induced liver injury
- [ ] Manage immune reconstitution inflammatory syndrome (IRIS)
- [ ] Identify FCPS/MRCP high-yield HIV-hepatology intersections

---

## 2. HIV and Liver Disease: Overview

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

## 3. HBV/HIV Coinfection

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

## 4. HCV/HIV Coinfection

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

## 5. Recommended Regimens (Pan-Genotypic)

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

## 6. Critical Drug Interactions (DAAs with ART)

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

## 7. IRIS (Immune Reconstitution Inflammatory Syndrome)

| Feature | Detail |
|--------|--------|
| **Definition** | **Paradoxical Worsening** of Liver Inflammation After Starting ART (or HCV Treatment) |
| **Timing** | **4-12 Weeks** After ART Initiation (or HCV DAA Start) |
| **Clinical** | ALT Flares, Jaundice, Hepatic Decompensation |

*...continued (truncated for renderer performance)*
---

> Auto-generated study sections for "Hepatology in Special Situations" — Ch 23: Hepatology.

## Flashcards (35 generated)

- Q: What is Global Coinfection of Hepatology in Special Situations?
  A: ~2.7 Million (7-10% of PLHIV)
- Q: What is High-Risk of Hepatology in Special Situations?
  A: Sub-Saharan Africa, Asia, PWID, MSM
- Q: What is Impact of Hepatology in Special Situations?
  A: Accelerated Fibrosis, ↓ Spontaneous Clearance, ↑ HCC Risk
- Q: What is TDF of Hepatology in Special Situations?
  A: ↑ Tenofovir Levels with Boosted PI; Monitor Renal
- Q: What is TAF of Hepatology in Special Situations?
  A: ↑ Levels with Strong CYP3A4 Inhibitors (Boosted PI)
- Q: What is ETV of Hepatology in Special Situations?
  A: No Significant HIV Drug Interactions
- Q: What is Regimen of Hepatology in Special Situations?
  A: SOF 400mg / VEL 100mg Once Daily
- Q: What is Duration of Hepatology in Special Situations?
  A: 12 Weeks (All Genotypes, All Fibrosis)
- Q: What is Key Advantage of Hepatology in Special Situations?
  A: Minimal ART Interactions — Fewest Drug Interactions
- Q: What is ART Compatibility of Hepatology in Special Situations?
  A: Compatible with Most ART (INSTI, NNRTI, Some PIs)
- Q: What is eGFR <30 of Hepatology in Special Situations?
  A: Avoid (Sofosbuvir Accumulation)
- Q: What is Regimen of Hepatology in Special Situations?
  A: 3 Tablets (300/120mg) Once Daily
- Q: What is Duration of Hepatology in Special Situations?
  A: 8 Weeks (Naive, Non-Cirrhotic); 12 Weeks (Cirrhotic/Experienced)
- Q: What is Key Caveat of Hepatology in Special Situations?
  A: Drug Interactions with Boosted PIs (Ritonavir/Cobicistat-Boosted) — ↑ GLE/PIB Levels
- Q: What is eGFR <30 of Hepatology in Special Situations?
  A: Safe (Preferred in Renal Impairment)
- Q: What is ART Compatibility of Hepatology in Special Situations?
  A: Check Interactions (Avoid with Boosted DRV/ATV/LPV/r)
- Q: What is the definition of Hepatology in Special Situations?
  A: Paradoxical Worsening of Liver Inflammation After Starting ART (or HCV Treatment)
- Q: What is Timing of Hepatology in Special Situations?
  A: 4-12 Weeks After ART Initiation (or HCV DAA Start)
- Q: What is Clinical of Hepatology in Special Situations?
  A: ALT Flares, Jaundice, Hepatic Decompensation
- Q: What is Global Coinfection of Hepatology in Special Situations?
  A: ~2.7 Million (7-10% of PLHIV)
- Q: What is High-Risk of Hepatology in Special Situations?
  A: Sub-Saharan Africa, Asia, PWID, MSM
- Q: What is TDF of Hepatology in Special Situations?
  A: ↑ Tenofovir Levels with Boosted PI; Monitor Renal
- Q: What is TAF of Hepatology in Special Situations?
  A: ↑ Levels with Strong CYP3A4 Inhibitors (Boosted PI)
- Q: What is ETV of Hepatology in Special Situations?
  A: No Significant HIV Drug Interactions
- Q: What is Regimen of Hepatology in Special Situations?
  A: SOF 400mg / VEL 100mg Once Daily
- Q: What is Duration of Hepatology in Special Situations?
  A: 12 Weeks (All Genotypes, All Fibrosis)
- Q: What is Key Advantage of Hepatology in Special Situations?
  A: Minimal ART Interactions — Fewest Drug Interactions
- Q: What is ART Compatibility of Hepatology in Special Situations?
  A: Compatible with Most ART (INSTI, NNRTI, Some PIs)
- Q: What is Regimen of Hepatology in Special Situations?
  A: 3 Tablets (300/120mg) Once Daily
- Q: What is Duration of Hepatology in Special Situations?
  A: 8 Weeks (Naive, Non-Cirrhotic); 12 Weeks (Cirrhotic/Experienced)
- Q: What is Key Caveat of Hepatology in Special Situations?
  A: Drug Interactions with Boosted PIs (Ritonavir/Cobicistat-Boosted) — ↑ GLE/PIB Levels
- Q: What is eGFR <30 of Hepatology in Special Situations?
  A: Safe (Preferred in Renal Impairment)
- Q: What is the definition of Hepatology in Special Situations?
  A: Paradoxical Worsening of Liver Inflammation After Starting ART (or HCV Treatment)
- Q: What is Timing of Hepatology in Special Situations?
  A: 4-12 Weeks After ART Initiation (or HCV DAA Start)
- Q: What is Clinical of Hepatology in Special Situations?
  A: ALT Flares, Jaundice, Hepatic Decompensation

## MCQs (1 generated)

1. **Which of the following best describes Hepatology in Special Situations?**
   A. **| Global Coinfection | ~2.7 Million (7-10% of PLHIV) |**
   B. An unrelated condition not matching the clinical picture of Hepatology in Special Situations
   C. A complication seen late in the disease course of Hepatology in Special Situations
   D. A condition that mimics Hepatology in Special Situations but has a different underlying cause

## SBA Questions (1 generated)

1. A patient with suspected Hepatology in Special Situations presents with: TDF — ↑ Tenofovir Levels with Boosted PI; Monitor Renal; TAF — ↑ Levels with Strong CYP3A4 Inhibitors (Boosted PI); ETV — No Significant HIV Drug Interactions. What is the most likely diagnosis?
   A. **Hepatology in Special Situations**
   B. A condition that mimics Hepatology in Special Situations but is not the same entity
   C. A complication of Hepatology in Special Situations rather than the primary diagnosis
   D. An unrelated condition in the same clinical category as Hepatology in Special Situations

