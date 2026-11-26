# Research-deepening batch 22 (2026-11-26)

**Plants:** catnip, black seed, holy basil, evening primrose, olive.

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex.
- **Name overrides:** added for all five plants (for example thymoquinone for black seed, *Ocimum sanctum* for holy basil, olive leaf and oleuropein for olive).
- **Europe PMC:** no failures. It added three trials: a black seed PMS trial, a black seed episiotomy trial and an olive blood-pressure trial.

**Outcome:**
- **Search volume:** about 3,900 PubMed hits (black seed about 1,800, olive about 2,460 before de-duplication) and about 75 abstracts read.
- **New references:** 24 (REF-5521..5544).
- **Symptom-tool pairs:** 1,489 -> 1,498.
- **Checks:** validate passes, with refs cited 4,319 / declared 4,319.
- **Species audit:** suspects fell from 118 to 110, because *Ocimum sanctum* L. (an accepted synonym) was added to the holy basil record. Ten older and new tulsi papers that use that name had been flagged as wrong-species.
- **Files:** change log `r22_changes.tsv`; fixer `../fix_r22.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Black seed | arthritis | 1 | 8 | 2022 double-blind knee OA RCT and a 2024 OA systematic review; a null processed-seed RCT stays alongside |
| Olive | high blood pressure | new | 8 | 2022 olive-leaf meta-analysis of 12 RCTs and the 2021 meta-analysis; a null 2026 RCT stays alongside |
| Black seed | insomnia | new | 6 | Two 2023 double-blind RCTs of the BlaQmax extract |
| Holy basil | oral health | new | 6 | 2020 placebo-toothpaste and 2014 saline-controlled mouthwash RCTs (gingivitis) |
| Black seed | acne | new | 5 | 2020 double-blind hydrogel RCT |
| Black seed | sinusitis | new | 5 | 2021 double-blind nasal-drop RCT |
| Black seed | kidney support | new | 5 | 2019 triple-blind kidney-stone RCT |
| Black seed | stress | new | 5 | 2023 BlaQmax RCT |
| Black seed | PMS | new | 5 | 2025 double-blind RCT |
| Black seed | wounds | 1 | 5 | 2025 triple-blind episiotomy emulgel RCT |
| Black seed | pain | 1 | 5 | The same episiotomy RCT (lower pain) |
| Evening primrose | fatigue | new | 5 | 2018 double-blind RCT in multiple sclerosis |

**No-effect studies recorded:**
- A 2017 processed black seed formula for knee OA.
- A 2025 olive leaf pilot trial for blood sugar.
- A 2026 olive extract trial for blood pressure.

## Safety and other tool data

**Black seed:**
- New **warning**: black seed oil on the skin caused severe, Stevens-Johnson-like blistering dermatitis in three women, with more than 15% of skin detaching (2018 JAMA Dermatology case series).
- New caution: rhabdomyolysis, acute kidney injury and liver injury after drinking the oil.
- New info note: a meta-analysis of liver and kidney tests (ALP and urea lower; high doses may raise urea).
- New info note: a case of severe low platelets, with evening primrose oil also taken.

**Evening primrose:**
- New info note: a 2007 review judged the epilepsy warning spurious.
- New caution: lipoid pneumonia after long-term use.
- New info note: the same low-platelet case.

**Catnip:** new caution after a toddler became drowsy and unresponsive after eating a large amount.

**Olive:** new info note. In patch tests, olive oil was a weak skin irritant, mostly under occlusion.

**Draft interactions:** none new. Six are pending:
- hibiscus × statins
- hibiscus × anticoagulants
- devil's claw × anticoagulants
- flax × anticoagulants
- noni × anticonvulsants
- bitter melon × chemotherapy agents

## Research-integrity hold

No new black seed reference is from the flagged Tehran psychopharmacology group.

## For the owner

1. **Black seed skin reaction uses severity "warning",** because the three cases resembled Stevens-Johnson syndrome and needed hospital care.
2. **Evening primrose for labour induction: no pair (inv. 12d).** Two meta-analyses report cervical ripening, but the record cautions against medicinal use in pregnancy.
3. **Black seed insomnia and stress rest on one company product (BlaQmax).**

## Gaps and settled plants

- **Catnip:** no human trial. Settled.
- **Black seed male infertility:** only a multi-herb review was found.
- **Black seed depression:** the adjunct trial does not state randomisation.
- **Olive cholesterol:** no pair. Olive leaf lowered triglycerides overall but cholesterol only in subgroups, and olive oil trials compare it with other oils.

## Rejected or not added (main reasons)

**Black seed:**
- A honey-based dyspepsia formula and an olive + black seed oil episiotomy oil (combinations).
- A navel-oil incontinence trial (topical abdominal route, mixed result).
- An H. pylori trial with an appetite outcome only.

**Evening primrose:**
- Pain (9), hot flushes (9) and menopause (8) were not padded.
- Combinations with hemp seed or fish oil.

**Holy basil:**
- Stress (8) and blood sugar (8) were not padded.
- Mouthwash trials compared only with chlorhexidine.

**Olive:**
- Cohort mortality meta-analyses (observational).
- A pre-post-only blood-pressure meta-analysis.
- An accidental leaf-swallowing case.
- Olive pollen allergy (not related to use).
