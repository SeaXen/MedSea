## 1. Learning Objectives
- [ ] Apply DAA regimens in HCV-HIV coinfection (Same efficacy, Same duration)
- [ ] Manage drug-drug interactions (DAAs with ART)
- [ ] Prioritise treatment (CD4, HIV VL, Fibrosis)
- [ ] Monitor for immune reconstitution inflammatory syndrome (IRIS)
- [ ] Identify FCPS/MRCP high-yield interaction pearls

---

## 2. Epidemiology & Natural History

| Feature | HCV Monoinfection | HCV-HIV Coinfection |
|---------|-------------------|---------------------|
| **Global Prevalence** | ~58M | ~2.3M (Co-infected) |
| **Transmission** | Blood, Unsafe Medical | **Shared Routes** (IVDU, Sexual-MSMS, Blood) |
| **Fibrosis Progression** | Slow (Decades) | **Accelerated 2-3x** (Even on ART) |
| **Cirrhosis Risk** | ~20% at 20y | **Higher, Earlier** |
| **Liver-Related Mortality** | Lower | **Leading Cause** in Treated HIV |
| **Spontaneous Clearance** | 15-25% | **Reduced** (5-15%) |

> **FCPS/MRCP**: **HIV Accelerates HCV Fibrosis** — Even with Suppressed HIV VL

---

## 3. Treatment Principles

| Principle | Detail |
|---------|--------|
| **Same Efficacy** | **DAA SVR Rates >95%** in Coinfection (Same as Mono) |
| **Same Duration** | **No Extension Needed** for Coinfection |
| **Same Regimens** | **Pan-Genotypic Preferred** (SOF/VEL, GLE/PIB, SOF/VEL/VOX) |
| **Priority** | **Treat ALL Coinfection** — Regardless of CD4, Fibrosis Stage |
| **ART Continuation** | **Do NOT Stop ART** for HCV Treatment |

---

## 4. Recommended Regimens (Pan-Genotypic)

### 1. Sofosbuvir/Velpatasvir (SOF/VEL) — **PREFERRED First-Line**
| Aspect | Detail |
|-------|--------|
| **Regimen** | SOF 400mg / VEL 100mg Once Daily |
| **Duration** | 12 Weeks (All Genotypes, All Fibrosis) |
| **Key Advantage** | **Minimal ART Interactions** — Fewest Drug Interactions |
| **ART Compatibility** | Compatible with Most ART (Integrase Inhibitors, NNRTIs, Some PIs) |
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

## 5. Critical Drug Interactions (DAAs with ART)

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
| **SOF/VEL** | **INSTI (DTG, BIC, RAL, CAB)** | **None** | Preferred |
| **SOF/VEL** | **NNRTI (EFV, RPV, DOR, ETV)** | **None/Minimal** | OK |
| **SOF/VEL** | **Boosted PI (DRV/r, ATV/r, LPV/r, TPV/r)** | ↑ VEL Levels (CYP3A4/P-gp Inhibition) | **Monitor VEL Toxicity**; Consider Dose Adjust or Alternate DAA |
| **GLE/PIB** | **Boosted PI (DRV/r, ATV/r, LPV/r, TPV/r)** | **↑↑ GLE/PIB Levels** (Strong CYP3A4/P-gp Inhib) | **CONTRAINDICATED / AVOID** |
| **GLE/PIB** | **INSTI / NNRTI** | Minimal | Safe |
| **SOF/VEL/VOX** | **Boosted PI** | ↑ VOX Levels | **Avoid** |

---

## 6. IRIS (Immune Reconstitution Inflammatory Syndrome)

| Feature | Detail |
|--------|--------|
| **Definition** | **Paradoxical Worsening** of Liver Inflammation After Starting ART (or HCV Treatment) |
| **Timing** | **4-12 Weeks** After ART Initiation (or HCV DAA Start) |
| **Clinical** | ALT Flares, Jaundice, Hepatic Decompensation |
| **Mechanism** | Immune Recovery → Enhanced HCV-Specific Response |
| **Risk Factors** | Low CD4 (<200), High HIV VL, Advanced Fibrosis, Recent ART Start |
| **Management** | **Continue Both ART + DAA** (Usually Self-Limited); **Corticosteroids if Severe** (Pred 0.5-1mg/kg) |

> **IRIS vs DILI vs Reactivation** — Timing from ART/DAA Start, Pattern of LFTs, Histology if Biopsy

---

## 7. Monitoring in Coinfection

| Parameter | Frequency |
|-----------|-----------|
| **HCV RNA** | Baseline, Week 4 (Optional), EOT, SVR12 |
| **HIV VL** | Every 3-6 Months (Per HIV Guidelines) |
| **CD4 Count** | Every 3-6 Months |
| **LFTs (ALT, AST, Bilirubin, ALP)** | Baseline, Week 4, EOT, SVR12 |
| **Renal Function** | Baseline, Week 4, EOT (If TDF/ART) |
| **ART Levels** | If Boosted PI + VEL/VOX (Therapeutic Drug Monitoring) |

---

## 8. Special Situations

### Decompensated Cirrhosis (Child B/C) + HIV
| Regimen | Duration |
|---------|----------|
| **SOF/VEL + RBV** | 12 Weeks |
| **GLE/PIB** | **CONTRAINDICATED** |
| **SOF/VEL/VOX** | **CONTRAINDICATED** |

### Renal Impairment (eGFR <30) + HIV
| Regimen | Notes |
|---------|--------|
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

## 9. FCPS/MRCP High-Yield Summary

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

## 10. Viva Questions

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

## 11. Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| SOF/VEL vs GLE/PIB in HIV | **SOF/VEL = Minimal Interactions (Preferred)**; GLE/PIB = Avoid Boosted PI |
| SVR in Coinfection | **Same >95%** — No Duration Extension |
| Boosted PI + DAA | **DRV/r, ATV/r, LPV/r, TPV/r** increase PI/DAA levels — Monitor or Avoid |
| INSTI/NNRTI + DAA | **Compatible** — DTG, BIC, RAL, EFV, RPV, DOR |
| Decompensated + HIV | **SOF/VEL + RBV ONLY** — GLE/PIB, VOX Contraindicated |
| CKD + HIV + HCV | **GLE/PIB Preferred** (Safe All eGFR) |
| IRIS Timing | **4-12 Weeks** After ART/DAA Start — Self-Limited, Steroids if Severe |
| TDF in HIV | Part of ART (TDF/FTC or TAF/FTC) — Also Covers HBV |

---

## 12. Mind Map

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
      Triple HBV: HIV Art (TDF/FTC) + HCV DAA
    IRIS
      4-12w Post ART/DAA
      ALT Flare → Continue Both, Steroids if Severe
```

---

## 13. One-Page Revision Card

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

---

## 14. Spaced Repetition Tracker

| Day | 1 | 3 | 7 | 15 | 30 |
|-----|---|---|---|----|----|
| Preferred Regimen | ☐ | ☐ | ☐ | ☐ | ☐ |
| Interaction Table | ☐ | ☐ | ☐ | ☐ | ☐ |
| Boosted PI Avoidance | ☐ | ☐ | ☐ | ☐ | ☐ |
| IRIS Management | ☐ | ☐ | ☐ | ☐ | ☐ |
| Special Situations | ☐ | ☐ | ☐ | ☐ | ☐ |

---

## 15. Self-Test Scorecard

| Question | My Answer | Correct? |
|----------|-----------|----------|
| Preferred Regimen Coinfection |  |  |
| BOOSTED PI + GLE/PIB |  |  |
| IRIS Timing |  |  |
| CKD + HIV + HCV |  |  |
| Decompensated + HIV |  |  |

---

## 16. Local Navigation

- [[Viral Hepatitis/Hepatitis C|HCV Overview]]
- [[Viral Hepatitis/Hepatitis C genotype-based treatment|HCV Genotype Treatment]]
- [[Viral Hepatitis/HCV DAA Regimens by Genotype & Cirrhosis|HCV DAA Regimens]]
- [[Viral Hepatitis/Hepatitis C decompensated cirrhosis management|HCV Decompensated]]
- [[Viral Hepatitis/Hepatitis C renal impairment|HCV Renal]]