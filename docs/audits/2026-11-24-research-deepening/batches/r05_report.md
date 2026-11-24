# Research-deepening batch 5 (2026-11-24)

**Plants:** pleurisy root, astragalus, bacopa, birch, bistort.

**Sources searched:**
- PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex.
- A targeted PubMed search for birch bark extract (Oleogel-S10 / Filsuvez).
- The EMA Filsuvez product information (PDF, extracted with pypdf).

**Outcome:**
- **Search volume:** about 2,200 PubMed hits (astragalus alone: about 1,600, mostly multi-herb formulas and injections) and about 60 abstracts or pages read.
- **New references:** 18 (REF-5187..5204).
- **Symptom-tool pairs:** 1,420 -> 1,422.
- **Checks:** validate passes, with refs cited 3,979 / declared 3,979. The species audit flagged *Astragalus mongholicus*, the accepted name. It is now recorded as a synonym on the astragalus record, and the flag is cleared.
- **Files:** change log `r05_changes.tsv`; fixer `../fix_r05.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Birch | wounds | new | 7 | Birch bark extract gel (licensed in the EU as Filsuvez): EASE double-blind RCT in epidermolysis bullosa (223 patients), two phase III donor-site RCTs (219 patients) and a phase II RCT |
| Astragalus | kidney support | new | 7 | 2019 meta-analysis in diabetic kidney disease; the oral subgroup (4 RCTs) reduced albumin in the urine; low-quality evidence |
| Astragalus | arthritis | 1 (inferred) | 5 | 2025 placebo RCT of a root extract for knee joint pain |
| Bacopa | depression | 5 | 6 | Citalopram add-on trial in anhedonia |
| Pleurisy root | cold | 1 (inferred) | 2 | Historical review: Eclectic physicians used it for influenza in 1918 (still `needs-review`) |

**Other evidence added (no score change):**
- **Bacopa, memory and cognitive function:** a 2026 network meta-analysis and a 90-day RCT. The meta-analysis found high doses improved working and short-term memory, but not attention or processing speed.
- **Bacopa, no-effect study:** a 12-week RCT found no effect on any cognitive measure and only a non-significant anxiety trend. It is recorded as no-effect for memory, cognitive function and anxiety.
- **Astragalus, fatigue:** a placebo RCT in fatigue after stroke.

## Safety and other tool data

- **Birch:** new info note from the EU product information. The bark gel can cause hypersensitivity reactions, and must be stopped if they occur. Wound infection is a known complication.
- **Bacopa:** new caution from a 2025 review: take care with some medicines and in hyperthyroidism; safety in pregnancy and breastfeeding has not been established.
- **Pleurisy root:**
  - A second corneal-injury case report (2026, a contact-lens wearer after gardening) is added to the cardiac-glycoside caution, whose text now covers both cases.
  - The 2017 case report (REF-0626) was tagged as a lab study; it is retagged `clinical`.
- **Astragalus:** new `vulnerary` action, from a preclinical meta-analysis of wound healing.

**Draft herb-drug interactions (need owner sign-off):**
- **Bacopa × serotonergic antidepressants (caution):** two pharmacovigilance reports, with agomelatine and with moclobemide (a heart attack).
- **Astragalus × CYP3A4 substrates (insufficient):** a 2025 review of effects on CYP2C9, CYP3A4, UGT1A6 and P-gp. Studies disagree on CYP3A4.

## For the owner

1. **Approve or reject the two draft interactions above.**
2. **The birch wounds pair rests on a licensed bark-extract medicine,** not on birch leaf tea. The note says so, and the species is confirmed by the EMA product information (*Betula pendula*, *B. pubescens* and hybrids).
3. **Injected extracts are not counted.** Astragalus injection trials are excluded as support, as were the andrographolide injections in batch 3, because injection is a hospital drug route, not herbal use. As a result, the heart-failure, heart-attack and cancer meta-analyses were left out.

   There is an inconsistency: an earlier audit kept an astragalus-polysaccharide *infusion* trial (REF-3451) as a no-effect study for fatigue.
4. **Bacopa memory (10) and cognitive function (9) are still `needs-review`.** This pass did not change their status.

## Rejected or not added (main reasons)

**Astragalus:**
- The 2016 Cochrane review on preventing respiratory infections in children found no eligible trials. That is an empty review, not a no-effect result.
- Diastolic-function trials in hypertensive women: tiny echocardiography changes, open-label, no symptom outcome.
- Injection-only meta-analyses.
- Products that combine astragalus with other ingredients:
  - Lectranal (herbal-mineral complex);
  - Myelophil;
  - SHPro;
  - AstraGin;
  - Rubus + Astragalus;
  - Huang Qi formulas.

**Bacopa:**
- Ayurvedic formulations: Brahmi vati, Brahmi ghrita, Medhya Rasayana.
- Multi-ingredient products.
- A trial against donepezil (active comparator only).
- Conditions not in the vocabulary: ADHD, schizophrenia, Parkinson's.
- A cevimeline toxicity case (the supplement also contained phosphatidylserine).
- A myopathy letter with no abstract.

**Birch:**
- A single-centre report that is a subset of the donor-site trial.
- The burns RCT (compared only with Octenilin gel).
- The actinic-keratosis placebo RCT (no effect, and not a vocabulary condition).
- The open extension of EASE.
- Pollen and forestry literature.

**Pleurisy root and bistort:**
- No human studies exist. Both are settled.
- Bistort's two info notes and its pregnancy caution carry no reference (open item).
