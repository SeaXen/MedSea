## 1. Learning Objectives
- [ ] Stratify reactivation risk by HBsAg status and immunosuppression type
- [ ] Prescribe prophylactic antivirals appropriately
- [ ] Implement monitoring protocol during and after immunosuppression
- [ ] Manage reactivation if it occurs
- [ ] Identify FCPS/MRCP high-yield risk groups and prophylaxis indications

---

## 2. Definition

> **HBV Reactivation** = **Reappearance of HBV DNA** or **HBsAg seroreversion** in a patient with **previous or current HBV infection** triggered by immunosuppression

| Scenario | Reactivation Definition |
|----------|------------------------|
| **HBsAg+ (Chronic)** | HBV DNA ↑ >1 log10 IU/mL from baseline (or reappearance if undetectable) |
| **HBsAg-, Anti-HBc+ (Resolved)** | **HBsAg Seroreversion** (HBsAg becomes positive) OR HBV DNA becomes detectable |

---

## 3. Risk Stratification

### By HBsAg Status and Immunosuppression

```mermaid
flowchart TD
    A[Patient Needing Immunosuppression] --> B{HBsAg Status}
    B -->|HBsAg+ (Chronic HBV)| C[HIGH RISK for ALL Immunosuppression]
    B -->|HBsAg-, Anti-HBc+ (Resolved)| D{Risk by Immunosuppression Type}
    D -->|High Risk (Rituximab, Stem Cell Tx, High-Dose Steroids)| E[HIGH RISK]
    D -->|Moderate (Anti-TNF, Chemo, Low-Dose Steroids)| F[MODERATE RISK]
    D -->|Low (Methotrexate, Azathioprine, Low-Dose Steroids <10mg)| G[LOW RISK]
    B -->|HBsAg-, Anti-HBc- (Susceptible)| H[No Reactivation Risk - Vaccinate]
```

### High-Risk Immunosuppression (>10% Reactivation)
| Agent / Setting | Examples |
|----------------|----------|
| **Anti-CD20** | **Rituximab, Ofatumumab, Obinutuzumab** |
| **Stem Cell Transplant** | Autologous / Allogeneic |
| **High-Dose Corticosteroids** | **≥20mg Prednisolone/day ≥4 weeks** |
| **Anthracycline Chemotherapy** | Doxorubicin, Epirubicin |
| **Combination Immunosuppression** | Multi-agent Regimens |

### Moderate-Risk (1-10% Reactivation)
| Agent / Setting | Examples |
|----------------|----------|
| **Anti-TNF** | Infliximab, Adalimumab, Etanercept, Certolizumab, Golimumab |
| **TYK2/JAK Inhibitors** | Tofacitinib, Upadacitinib, Baricitinib |
| **Chemotherapy (Non-Anthracycline)** | Methotrexate, Cyclophosphamide, 5-FU |
| **Solid Organ Transplant** | Kidney, Heart, Lung (non-liver) |

### Low-Risk (<1% Reactivation)
| Agent / Setting | Examples |
|----------------|----------|
| **Traditional DMARDs** | Methotrexate ≤25mg/week, Azathioprine, Leflunomide, Hydroxychloroquine, Sulfasalazine |
| **Low-Dose Steroids** | **<10mg Prednisolone/day** |
| **Anti-IL6/IL12/IL23/IL17** | Tocilizumab, Ustekinumab, Secukinumab (Data Limited) |

---

## 4. Prophylaxis Strategy

### HBsAg+ (Chronic HBV) — **PROPHYLAXIS FOR ALL**
| Immunosuppression | Prophylaxis | Duration |
|-------------------|-------------|----------|
| **Any** | **Entecavir 0.5mg/day** OR **Tenofovir 245mg/day** | **Start BEFORE/With Immunosuppression** → Continue **≥12 months AFTER STOPPING** Immunosuppression |

### HBsAg-, Anti-HBc+ (Resolved) — **Risk-Adapted**
| Risk Level | Prophylaxis | Monitoring (If No Prophylaxis) |
|------------|-------------|--------------------------------|
| **High** | **Entecavir/Tenofovir** (Same as HBsAg+) | — |
| **Moderate** | **Consider Prophylaxis** (Guideline-Dependent) | **ALT q1-3mo**; If ALT↑ → Check HBV DNA → Start NUC if Detectable |
| **Low** | **No Prophylaxis** | **ALT q3-6mo**; If ALT↑ → Check HBV DNA |

> **EULAR/ACR**: **Prophylaxis for Moderate/High Risk** in Resolved HBV

---

## 5. Prophylactic Antiviral Choice

| Drug | Dose | Advantages |
|------|------|------------|
| **Entecavir (ETV)** | 0.5mg daily (0.25mg if eGFR<50) | High Barrier, Minimal Side Effects, Safe in Renal Impairment (adjust) |
| **Tenofovir DF (TDF)** | 245mg daily (adjust if eGFR<50) | High Barrier, Cheap (Generic), HBV+HIV |
| **Tenofovir AF (TAF)** | 25mg daily | Less Renal/Bone Toxicity, Preferred if CKD/Osteoporosis |

> **Lamivudine**: **NOT Recommended** — Low Barrier (Resistance)

---

## 6. Monitoring Protocol

### On Prophylaxis
| Test | Frequency | Action |
|------|-----------|--------|
| **HBV DNA** | Every 3 months | Detect Breakthrough Early |
| **ALT** | Every 1-3 months | Surrogate for Reactivation |
| **HBsAg / Anti-HBs** | Every 6 months | Seroconversion / Clearance |
| **Renal Function** | Every 6 months (TDF) | Dose Adjust if eGFR Decline |

### Off Prophylaxis (Resolved HBV, Low/Moderate Risk)
| Test | Frequency | Action if Abnormal |
|------|-----------|-------------------|
| **ALT** | q1-3mo (Moderate) / q3-6mo (Low) | If ALT ↑ >2×ULN → **Check HBV DNA** |
| **HBV DNA** | Only if ALT ↑ | If Detectable → **Start Prophylaxis** |

---

## 7. Management of Reactivation

```mermaid
flowchart TD
    A[HBV Reactivation Detected] --> B{On Prophylaxis?}
    B -->|Yes| C[Assess Adherence / Resistance]
    C --> D{Resistant?}
    D -->|Yes| E[Switch to High-Barrier (TDF/TAF)]
    D -->|No| F[Continue Current / Optimise Adherence]
    B -->|No (Monitoring Only)| G[START ETV/TDF IMMEDIATELY]
    G --> H[Continue ≥12mo After Immunosuppression Stops]
    E --> H
    F --> H
    H --> I[Monitor HBV DNA Monthly Until Undetectable ×3mo]
```

### Definition of Reactivation (Action Threshold)
| Population | Threshold |
|------------|-----------|
| **HBsAg+ (Chronic)** | HBV DNA ↑ >1 log10 IU/mL from baseline OR Reappearance if Undetectable |
| **Resolved (Anti-HBc+)** | **HBsAg Seroreversion** (HBsAg becomes +) OR HBV DNA Detectable |

---

## 8. Special Situations

### Rituximab Therapy
- **Highest Risk** — **Prophylaxis Mandatory** for both HBsAg+ and Resolved HBV
- **Duration**: Continue **≥12 months AFTER LAST RITUXIMAB DOSE** (B-cell depletion persists)

### Stem Cell Transplant
- **Prophylaxis Throughout Conditioning + Transplant + ≥12mo Post-Engraftment**
- **Monitor**: HBV DNA Weekly during Neutropenia

### Anti-TNF Therapy
- **Moderate Risk** — **Prophylaxis Recommended** by EULAR/ACR for Resolved HBV
- **Duration**: Continue **≥6 months AFTER STOPPING Anti-TNF**

### Corticosteroids
- **≥20mg Prednisolone ≥4 weeks** = High Risk
- **<10mg Prednisolone** = Low Risk

---

## 9. FCPS/MRCP High-Yield Summary

| Concept | Key Points |
|---------|------------|
| **HBsAg+** | **Prophylaxis ALWAYS** (Entecavir/Tenofovir) → ≥12mo after immunosuppression stops |
| **Resolved (Anti-HBc+)** | Risk by Immunosuppression: High (Rituximab, SCT, High-Dose Steroids) → Prophylaxis; Moderate (Anti-TNF, Chemo) → Prophylaxis/Monitor; Low (MTX, AZA, Low Steroids) → Monitor |
| **Drug of Choice** | **Entecavir 0.5mg** or **Tenofovir 245mg** (High Barrier) |
| **Prophylaxis Duration** | **≥12 months AFTER stopping immunosuppression** |
| **Rituximab** | **Always Prophylaxis** (High Risk); ≥12mo after last dose |
| **Monitoring** | HBV DNA q3mo on prophylaxis; ALT q1-3mo off prophylaxis |
| **Reactivation Definition** | HBsAg+ → HBV DNA ↑1 log; Resolved → HBsAg Seroreversion |

---

## 10. Viva Questions

1. **What is the reactivation risk for HBsAg+ patients on Rituximab?**
2. **Do you give prophylaxis to Anti-HBc+ patients on Methotrexate?**
3. **What is the duration of prophylaxis after stopping immunosuppression?**
4. **What is the drug of choice for HBV prophylaxis?**
5. **How do you monitor a patient on HBV prophylaxis?**
6. **Define HBV reactivation in Resolved HBV.**
7. **What is the reactivation risk for Anti-TNF therapy?**
8. **How does prophylaxis duration differ for Rituximab vs Anti-TNF?**
9. **What if HBV DNA rises despite prophylaxis?**
10. **Do you need prophylaxis for Vaccinated patients (Anti-HBs+ only)?**

---

## 11. Confusions & Mnemonics

| Confusion | Clarification |
|-----------|---------------|
| HBsAg+ vs Resolved Prophylaxis | HBsAg+ = **Always Prophylaxis**; Resolved = **Risk-Based** |
| Duration After Stopping | **≥12 months after LAST DOSE** (especially Rituximab) |
| Rituximab Duration | **B-cell depletion lasts months** → Prophylaxis ≥12mo after LAST RITUXIMAB |
| Anti-TNF Risk | **Moderate** — Guidelines vary; EULAR/ACR recommends prophylaxis for Resolved HBV |
| Low-Dose Steroids | **<10mg Prednisolone = Low Risk** — No Prophylaxis Needed for Resolved HBV |
| HBsAg+ on NUC Already | **Continue Same NUC** — Optimize Adherence; Monitor HBV DNA |
| Breakthrough on Prophylaxis | Check Adherence → Switch to Tenofovir (Highest Barrier) |
| Vaccinated Only (Anti-HBs+) | **No Reactivation Risk** — No Prophylaxis, No Monitoring |

---

## 12. Mind Map

```mermaid
mindmap
  root((HBV Reactivation))
    HBsAg+ (Chronic)
      Prophylaxis ALWAYS
      ETV/TDF
      Duration: ≥12mo After Immunosuppression Stops
    Resolved (Anti-HBc+)
      High Risk: Rituximab, SCT, High-Dose Steroids → Prophylaxis
      Moderate: Anti-TNF, Chemo → Prophylaxis (EULAR) / Monitor
      Low: MTX, AZA, Low Steroids → Monitor ALT q3-6mo
    Drug of Choice
      ETV 0.5mg / TDF 245mg / TAF 25mg
      High Barrier
    Monitoring
      On Prophylaxis: HBV DNA q3mo, ALT q1-3mo
      Off Prophylaxis: ALT q1-3mo → DNA if ALT↑
    Definitions
      HBsAg+: DNA ↑1 log
      Resolved: HBsAg Seroreversion
    Special
      Rituximab: Mandatory Prophylaxis → 12mo After LAST DOSE
      SCT: During + 12mo Post-Engraftment
```

---

## 13. One-Page Revision Card

| **Patient Group** | **Risk** | **Action** |
|-------------------|----------|------------|
| **HBsAg+** | High (All) | **Prophylaxis ALWAYS** (ETV/TDF) |
| **Resolved + Rituximab/SCT/High Steroids** | High | **Prophylaxis** |
| **Resolved + Anti-TNF/Chemo** | Moderate | **Prophylaxis (EULAR) / Monitor** |
| **Resolved + MTX/AZA/Low Steroids** | Low | **Monitor ALT q3-6mo** |

| **Drug of Choice** | |
|--------------------|--|
| **ETV 0.5mg** | Renal adjust if eGFR<50 |
| **TDF 245mg** | Renal/Bone monitoring |
| **TAF 25mg** | Less Renal/Bone Toxicity |

| **Prophylaxis Duration** | |
|--------------------------|--|
| **Standard** | ≥12 months AFTER Immunosuppression Stops |
| **Rituximab** | ≥12 months AFTER LAST DOSE |
| **Anti-TNF** | ≥6 months AFTER STOPPING |

| **Reactivation Definition** | |
|-----------------------------|--|
| HBsAg+ | HBV DNA ↑1 log from baseline |
| Resolved | HBsAg Seroreversion (HBsAg becomes +) |

---

## 14. Spaced Repetition Tracker

| Day | 1 | 3 | 7 | 15 | 30 |
|-----|---|---|---|----|----|
| Risk Stratification Table | ☐ | ☐ | ☐ | ☐ | ☐ |
| Prophylaxis Indications | ☐ | ☐ | ☐ | ☐ | ☐ |
| Duration After Stop | ☐ | ☐ | ☐ | ☐ | ☐ |
| Rituximab Special Rule | ☐ | ☐ | ☐ | ☐ | ☐ |
| Reactivation Definitions | ☐ | ☐ | ☐ | ☐ | ☐ |

---

## 15. Self-Test Scorecard

| Question | My Answer | Correct? |
|----------|-----------|----------|
| Rituximab prophylaxis duration |  |  |
| Resolved HBV on MTX |  |  |
| Drug of choice |  |  |
| Reactivation definition |  |  |
| Anti-TNF prophylaxis |  |  |

---

## 16. Local Navigation

- [[Viral Hepatitis/Hepatitis B|HBV Overview]]
- [[Viral Hepatitis/Hepatitis B phases of chronic infection|HBV Phases]]
- [[Viral Hepatitis/Hepatitis B treatment indications|HBV Treatment]]
- [[Viral Hepatitis/Hepatitis B pregnancy and vertical transmission|HBV Pregnancy]]
- [[Viral Hepatitis/Hepatitis B serology interpretation|HBV Serology]]