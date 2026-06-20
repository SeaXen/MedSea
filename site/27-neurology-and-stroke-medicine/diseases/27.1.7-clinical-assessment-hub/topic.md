# Clinical Assessment Hub

---
tags: [medicine, neurology, hub, fcps, mrcp]
chapter: Neurology
davidson_part: Part 3: Clinical Medicine
davidson_chapter: Chapter 25: Neurology
topic: Clinical Assessment Hub
exam: [FCPS, MRCP Part 1, MRCP Part 2, PACES]
references:
  anatomy: []
  physiology: []
  clinical: ['Davidson 24th Ed Ch25', 'Neurology: A Clinician\'s Approach', 'Adams and Victor\'s Principles of Neurology', 'PasTest', 'MRCP Part 1/2 Notes', 'Personal notes']
related: []
status: scaffold-hub
---

# Clinical Assessment Hub

**Topic-Group:** Clinical Assessment  
**Section:** 01_Fundamentals_Examination  
**Chapter:** Davidson 24th Ed Chapter 25: Neurology  
**Parent:** [[Fundamentals & Examination Hub]] | **Children:** [[Neurological History Taking]], [[Neurological Examination]], [[Anatomical Localisation Principles]], [[Higher Cortical Function Assessment]], [[Cranial Nerve Examination]], [[Motor System Examination]], [[Sensory System Examination]], [[Coordination & Gait Examination]], [[Autonomic Nervous System Assessment]]

> [!tip] Hub Overview
> Core clinical skills for neurological assessment: history taking, systematic examination, and anatomical localisation principles.

---

## Disease-Level Topics in This Hub

| # | Topic | Status | Key Focus |
|---|-------|--------|-----------|
| 1 | [[Neurological History Taking]] | scaffold | PACES framework, red flags, symptom descriptors |
| 2 | [[Neurological Examination]] | scaffold | Systematic CN, motor, sensory, coordination, gait |
| 3 | [[Anatomical Localisation Principles]] | scaffold | Lesion mapping: cortex, brainstem, cord, PNS, NMJ, muscle |
| 4 | [[Higher Cortical Function Assessment]] | scaffold | Cognition, language, praxis, neglect, frontal lobe |
| 5 | [[Cranial Nerve Examination]] | scaffold | II-XII systematic, brainstem localisation |
| 6 | [[Motor System Examination]] | scaffold | Tone, power, reflexes, UMN vs LMN, involuntary movements |
| 7 | [[Sensory System Examination]] | scaffold | Modalities, distributions, dermatomes, sensory level |
| 8 | [[Coordination & Gait Examination]] | scaffold | Cerebellar vs sensory ataxia, gait patterns |
| 9 | [[Autonomic Nervous System Assessment]] | scaffold | Valsalva, tilt, sudomotor, cardiac autonomic |

---

## Key Clinical Pearls

### History → Localisation Mapping
| Symptom | Localisation Clue |
|---------|------------------|
| **Unilateral weakness + UMN signs** | Contralateral corticospinal tract (corona radiata, internal capsule, brainstem) |
| **Hemianopia** | Contralateral optic tract/radiation/occipital cortex |
| **Aphasia** | Dominant hemisphere (Broca's, Wernicke's, conduction, global) |
| **Neglect** | Non-dominant parietal lobe |
| **Cranial nerve palsy + contralateral weakness** | Brainstem (crossed signs) |
| **Sensory level** | Spinal cord (dermatomal level) |
| **Dissociated sensory loss** | Syrinx (cape), cord hemisection (Brown-Séquard) |
| **Stocking-glove sensory loss** | Peripheral neuropathy (length-dependent) |
| **Proximal weakness + fatigue** | NMJ (myasthenia) |
| **Distal weakness + wasting + fasciculations** | LMN (MND, radiculopathy, plexopathy) |

### Examination Efficiency Tips
- **Order:** Higher centres → CNs → Motor → Sensory → Coordination → Gait
- **Time:** 5-7 minutes for focused exam in PACES
- **Localise as you go:** Don't just document, interpret
- **Compare sides:** Asymmetry is key

---

## High-Yield FCPS/MRCP Exam Topics

### Must Know
- [ ] PACES history structure (onset, progression, distribution, associated, triggers, functional)
- [ ] Full neurological examination sequence
- [ ] UMN vs LMN lesion signs table
- [ ] Sensory modalities and pathways (dorsal column vs spinothalamic)
- [ ] Dermatome/myotome map (C5-T1, L2-S1 key)
- [ ] Cerebellar signs (ataxia, dysmetria, dysdiadochokinesia, nystagmus)
- [ ] Gait patterns: spastic, ataxic, parkinsonian, waddling, steppage, festinating
- [ ] Red flags requiring urgent imaging/referral

### Should Know
- [ ] Higher cortical testing: MMSE/MoCA, frontal lobe tests (Luria, go/no-go, trail making)
- [ ] Language assessment: fluency, comprehension, repetition, naming, reading, writing
- [ ] Visual field testing: confrontation, mapping defects
- [ ] Pupillary examination: direct/consensual, RAPD, near response
- [ ] Autonomic testing: Valsalva manoeuvre, tilt table, sudomotor

### Nice to Know
- [ ] Primitive reflexes (grasp, snout, palmomental, glabellar)
- [ ] Alien limb syndrome, cortical sensory loss (graphaesthesia, stereognosis)
- [ ] Subtle parkinsonian signs (micrographia, reduced blink, hypomimia)
- [ ] Functional neurological disorder positive signs

---

## Cross-Section Links
| Section | Relevance |
|---------|-----------|
| **02_Headache** | Fundoscopy for papilloedema, CN examination |
| **03_Epilepsy** | Seizure semiology localisation, post-ictal signs |
| **04_Demyelinating** | Optic neuritis (RAPD, colour vision), INO, cerebellar signs |
| **05_Movement** | Parkinsonism examination, tremor classification |
| **06_Dementia** | Cognitive assessment, frontal vs temporal vs parietal |
| **07_MND** | Combined UMN+LMN signs, split hand syndrome |
| **08_Neuropathy** | Sensory level vs stocking-glove, NCS/EMG correlation |
| **09_NMJ** | Fatigability tests (ptosis, proximal weakness), ice pack test |
| **11_Spinal_Cord** | Sensory level, ASIA scale, cord vs root vs plexus |
| **12_Infections** | Meningism (Kernig, Brudzinski), encephalopathy grading |
| **13_Tumours** | Raised ICP signs, false localising signs (VI, III) |
| **14_Coma** | GCS/FOUR score, brainstem reflexes, respiratory patterns |
| **15_FND** | Positive signs: Hoover's, entrainment, give-way weakness |

---

## Verification Commands
```bash
# Check all 9 topics exist
ls /mnt/tb/Medicine/Neurology/01_Fundamentals_Examination/*.md | grep -E "(History|Examination|Localisation|Higher|Cranial|Motor|Sensory|Coordination|Autonomic)"

# Count scaffolds
grep -l "status: scaffold" /mnt/tb/Medicine/Neurology/01_Fundamentals_Examination/*.md | wc -l
```

---

## Revision Log
- **2026-06-16**: Hub scaffold created with 9 disease-level topics
- **Next:** Convert topics to full-fcps-mrcp-note format