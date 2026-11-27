# Research-deepening batch 30 (2026-11-27)

**Plants:** chia, sage, rosemary, elder, soapwort.

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex.
- **Name overrides:** added for all five plants.
- **Bare words not searched:**
  - "Sage" (matches the SAGE publisher and acronyms).
  - "Elder" (matches older people).
  - "Chia" outside titles (mastic, *Pistacia lentiscus* var. Chia, and the CHIA gene).
- **Research-integrity hold:** applied to sage and rosemary.

**Outcome:**
- **Search volume:** about 1,900 PubMed hits (rosemary about 1,000) and about 50 abstracts read.
- **New references:** 11 (REF-5644..5654).
- **Symptom-tool pairs:** 1,519 -> 1,522.
- **Checks:** validate passes, with refs cited 4,429 / declared 4,429. The species audit raised no flags on the new references (110 suspects, unchanged).
- **Files:** change log `r30_changes.tsv`; fixer `../fix_r30.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Sage | high cholesterol | 6 | 9 | 2023 meta-analysis of three diabetes RCTs (lower total and LDL cholesterol), adding to two RCTs already cited |
| Sage | blood sugar | 5 | 8 | The same meta-analysis (lower fasting glucose and HbA1c) |
| Sage | menopause | 7 | 8 | 2021 double-blind Menosan RCT (overall menopause score -39% versus placebo) |
| Sage | low libido | new | 5 | 2023 randomised aromatherapy trial in postmenopausal women (sexual function) |
| Rosemary | fatigue | new | 5 | 2021 randomised trial: rosemary oil inhalation reduced night-shift sleepiness in nurses |
| Rosemary | sore throat | new | 5 | 2025 randomised trial: rosemary extract reduced post-intubation sore throat versus water |

**No-effect study recorded:** a 2024 meta-analysis of eight chia RCTs found no effect on fasting glucose, HbA1c or insulin, so it is recorded on metabolic support. Rosemary anxiety also gained a 2025 double-blind crossover; its score stays 7.

## Safety and other tool data

- **Chia:** new allergy caution (IgE reactions including anaphylaxis; possible cross-reactivity with sesame).
- **Elder:**
  - New pancreas caution: a possible case of pancreatitis with daily black elderberry extract.
  - New liver caution: autoimmune hepatitis with long-term elderberry-containing supplements.

**Draft interactions:** one new, **elder × chemotherapy agents** (insufficient). It is based on a grade 3 liver-injury case on pazopanib with long-term elderberry flower supplements. Eleven drafts are now pending.

## Research-integrity hold

Sage and rosemary: author lists were checked, and no new reference is from the flagged Tehran psychopharmacology group. The existing sage cognitive and memory pairs were left as they are.

## For the owner (queued for the end-of-campaign review)

1. **Sage cholesterol now scores 9 and blood sugar 8.** Both come from a small 2023 meta-analysis (three trials, all Iranian diabetes RCTs, largely from one research group) plus RCTs from the same group. Tell me if you would like such geographically concentrated evidence weighted lower.
2. **The new elder × chemotherapy-agents draft needs your approval.**

## Gaps and settled plants

- **Chia:** blood sugar gets no pair (three null meta-analyses), and cholesterol gets no pair (conflicting meta-analyses). Blood pressure and cardiovascular support (9) were not padded.
- **Rosemary:** a fatty-liver RCT was null versus placebo (there is no liver pair).
- **Sage:** hot flushes were not raised, because the cited meta-analysis likely includes Menosan.
- **Elder:** cold (9) and respiratory support (8) were not padded.
- **Soapwort:** settled. The only trial used a three-herb cream, and most hits concern saporin, a research toxin.

## Rejected or not added (main reasons)

- **Active comparators:**
  - Sage versus benzydamine, clotrimazole or triamcinolone.
  - Rosemary versus minoxidil, mefenamic acid, ketoconazole or menthol.
- **Within-group or single-arm studies:** Iranian sage menopause studies, the sage periodontitis trial, the rosemary diabetes tea study.
- **Combinations:** sage + rosemary + melissa, aromatherapy blends, chia + fennel, and elder blends (lutein, violet + calendula, Sinupret-type products).
- **Other species:** American elderberry (*S. canadensis*), Spanish sage, a "clary sage" study.
- **Surrogate outcomes:** elderberry juice metabolism, chia CRP, sage PCOS markers.
- **No abstract:** a sage-oil child seizure letter, a 2020 elderberry pancreatitis case.
