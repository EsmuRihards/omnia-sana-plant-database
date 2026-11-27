# Research-deepening batch 31 (2026-11-27)

**Plants:** schisandra, figwort, American skullcap, saw palmetto, milk thistle.

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex.
- **Name overrides:** added for all five plants.
- **Species traps avoided:**
  - Bare "skullcap" means Chinese skullcap (*S. baicalensis*).
  - Ningpo figwort and *S. striata* are different species.
  - *Schisandra sphenanthera* is a different species.
- **Milk thistle:** silymarin, silibinin and silybin were searched in titles as compound evidence. Lactation RCTs were also searched directly.

**Outcome:**
- **Search volume:** about 3,400 PubMed hits (milk thistle about 2,200, saw palmetto about 720) and about 45 abstracts read.
- **New references:** 12 (REF-5655..5666).
- **Symptom-tool pairs:** 1,522 -> 1,523.
- **Checks:** validate passes, with refs cited 4,441 / declared 4,441. The species audit raised no flags on the new references (110 suspects, unchanged).
- **Files:** change log `r31_changes.tsv`; fixer `../fix_r31.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Milk thistle | high cholesterol | new | 8 | 2024 dose-response meta-analysis of 33 trials (total and LDL cholesterol and triglycerides down; compound evidence). The 2019 meta-analysis is cited alongside (benefit mainly when combined with other treatments). |

## Safety and other tool data

- **Saw palmetto:**
  - New liver caution: a biopsy-confirmed cholestatic case, plus an FDA adverse-event signal for liver and bile-duct problems.
  - New "post-Serenoa syndrome" caution: persistent sexual and psychiatric symptoms, with causality rated probable in 54%.
  - New caution for rare serious reactions: pancreatitis and rhabdomyolysis.
  - New children caution: hot flushes and early menarche in a 10-year-old girl, which returned on re-challenge.
  - New info note on global reporting data (44% of 1,810 reports were serious).
  - New info note: in a 2003 volunteer study (found via Europe PMC), saw palmetto did not change CYP2D6 or CYP3A4 activity.
  - The bleeding caution and the approved anticoagulants interaction now cite a post-surgical haematoma case and an FDA signal for haemorrhage in older aspirin users.
- **Schisandra:** the drug-interaction note now cites a human study (talinolol exposure +47%, P-glycoprotein inhibition).

**Draft interactions:** none new. Eleven are still pending.

## For the owner (queued for the end-of-campaign review)

1. **Recorded null results do not lower computed scores.** Saw palmetto keeps urinary support 10 and prostate support 9, although the record cites the 2023 Cochrane review and large US trials as no-effect studies and its note says "little to no benefit". The same pattern applies to kava insomnia, blackcurrant soreness and others. This is a scoring-formula question for you: whether recorded null results should reduce a score.
2. **Milk thistle cholesterol scores 8 on compound evidence (silymarin).** It is the same basis as the existing liver and blood-sugar pairs.

## Gaps and settled plants

- **Milk thistle:**
  - Kidney: a 2025 meta-analysis measured creatinine only, with 93% heterogeneity.
  - Lactation: one positive study without stated randomisation, one null RCT in mothers of preterm babies, and one combination product.
  - Blood pressure: diastolic only, -1.25 mmHg.
  - Liver (9) and blood sugar (8) were not padded.
- **Schisandra:** nearly all trials are combinations (ADAPT-232, Saengmaeksan, Shengmai). The single-herb obese-women RCT showed no between-group differences.
- **American skullcap:** settled. All four RCTs are already held.
- **Figwort:** settled. No PubMed hits for *S. nodosa*.

## Rejected or not added (main reasons)

- **Combinations:** schisandra formulas, the silymarin + galega galactagogue, saw palmetto + selenium + lycopene, and a multi-supplement psychosis case.
- **No vocabulary condition:** hair-loss and OCD trials.
- **Letters or no abstract:** a saw palmetto fixed drug eruption, a CP/CPPS meta-analysis letter.
- **Superseded:** older Cochrane saw palmetto versions (the 2023 version is cited).
