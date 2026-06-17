# Update MOC with: section checkboxes, progress tracker, high-yield tables, viva topics

## 1. Purpose
Enhance the Cardiology MOC with interactive learning features: progress tracking, high-yield tables, and viva-style questions to support active recall and FCPS/MRCP exam preparation.

## 2. Section Checkboxes
Add `- [ ]` markdown checkboxes for each subtopic. Use `[x]` to mark completed.

```markdown
## 16. Cardiac Emergencies
- [x] STEMI management
- [x] NSTEMI/UA
- [ ] Cardiogenic shock
- [ ] Cardiac tamponade
- [ ] Aortic dissection
- [ ] Life-threatening arrhythmias (VF/VT/TdP)
- [ ] Bradyarrhythmias
- [ ] Post-cardiac arrest care
- [ ] TTM
- [ ] Neuroprognostication
```

## 3. Progress Tracker
Add a summary table at the top of MOC:

| Section | Topics | Completed | % |
|---------|--------|-----------|---|
| Anatomy & Physiology | 12 | 8 | 67% |
| Investigations | 18 | 18 | 100% |
| Ischemic Heart Disease | 25 | 15 | 60% |
| Heart Failure | 22 | 20 | 91% |
| **Overall** | **183** | **122** | **67%** |

## 4. High-Yield Tables
Add comparison tables for high-yield differentials:

### ACS vs. Aortic Dissection vs. PE
| Feature | ACS | Dissection | PE |
|---------|-----|------------|-----|
| Pain | Pressure, gradual | Tearing, sudden | Pleuritic |
| ECG | ST changes | Non-specific | S1Q3T3 |
| CXR | Often normal | Widened mediastinum | Often normal |
| Troponin | Elevated | Often elevated | May elevate |
| D-dimer | Often normal | Elevated | Elevated |

## 5. Viva Topics
Add sample MRCP/FCPS viva questions:

### Sample Viva
**Q1: A 60-year-old man collapses at home with VF. ROSC achieved after 20 min. ECG post-arrest shows ST elevation in V1-V4. Next steps?**
- A1: Immediate coronary angiography ± PCI, TTM, post-arrest care bundle

**Q2: Differentiate cardiac tamponade from constrictive pericarditis.**
- A2: Tamponade = acute compression by fluid (pericardiocentesis Rx); Constriction = chronic scarring (pericardiectomy Rx). Tamponade: pulsus paradoxus, equalization of pressures; Constriction: Kussmaul sign, pericardial knock, dip-plateau.

**Q3: How would you manage a patient with Torsades de Pointes?**
- A3: IV magnesium 2 g, correct K⁺/Mg²⁺, withdraw QT-prolonging drugs, overdrive pacing, defibrillation if pulseless.

## 6. Update Workflow
1. Add new section checkbox list at top of MOC
2. Add progress tracker table
3. Embed high-yield tables in relevant sections
4. Append viva questions at end
5. Cross-link to source files
6. Add tag system (#high-yield, #viva, #revision)

> **Pearls**
> - **Checkboxes** drive completion psychology
> - **Viva questions** test application, not just recall
> - **High-yield tables** consolidate differentials
> - **Progress %** motivates continued study
> - Update MOC **monthly** with new evidence
