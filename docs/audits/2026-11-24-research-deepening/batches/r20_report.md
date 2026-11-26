# Research-deepening batch 20 (2026-11-26)

**Plants:** flaxseed, yellow loosestrife, Oregon grape, mallow, white horehound.

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex.
- **Name overrides:** added for all five plants (for example linseed and secoisolariciresinol for flax, Relieva for Oregon grape).
- **Europe PMC:** the flax queries hit timeouts but completed on retry; a second run gave the same results. It added one flax safety trial.

**Outcome:**
- **Search volume:** about 1,850 PubMed hits (flax about 1,690, the other four about 165) and about 50 abstracts read.
- **New references:** 16 (REF-5467..5482), one of them a DOI-only record with no PubMed ID.
- **Symptom-tool pairs:** 1,482 -> 1,484.
- **Checks:** validate passes, with refs cited 4,257 / declared 4,257. The species audit raised no flags on the new references.
- **Files:** change log `r20_changes.tsv`; fixer `../fix_r20.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Flaxseed | liver support | new | 8 | 2024 meta-analysis in fatty liver disease (lower ALT and triglycerides), plus a 2016 randomized trial (fibrosis and fat scores fell more than with lifestyle advice alone) |
| Flaxseed | arthritis | 1 | 5 | 2019 randomized trial of a warm flaxseed poultice in hand osteoarthritis |
| Flaxseed | menstrual cramps | new | 5 | 2024 placebo RCT in endometriosis (less period, pelvic and intercourse pain) |
| Mallow | pain | 5 | 6 | 2024 triple-blind placebo RCT of mallow ointment for episiotomy pain; the earlier null cream trial stays alongside, and the note says "mixed" |

## Safety and other tool data

**Flaxseed:**
- New allergy caution: anaphylaxis can follow even half a teaspoon of flaxseed flour. The main allergens are seed storage proteins (Lin u 1, 11S globulin), which cross-react with peanut and cashew.
- New hormone info note: a man developed gynaecomastia on flaxseed oil, while a meta-analysis of ten RCTs found no significant change in sex hormones.
- New cyanide info note: a linseed meal raised blood cyanide to about a third of the peak from cassava or apricot kernels at the same dose.
- New info note: 30 g of flaxseed lowered dabigatran exposure in one comparison, but the authors concluded it had no meaningful effect.
- New info note: in a 6-month double-blind RCT in adults aged 49-87, a flax lignan supplement caused no low blood sugar or low blood pressure.

**Oregon grape:** the medicines caution now cites a cell study in which the root extract blocked P-glycoprotein transport of cyclosporine and digoxin.

**Mallow:** new info note. It was among the plants causing irritant dermatitis in a prospective Turkish study.

**Horehound:** new info note. Liver enzymes turn marrubiin into reactive metabolites in lab and rat studies; whether this matters in people is unknown.

**Draft herb-drug interaction (needs owner sign-off):**

| Plant | Drug class | Severity | Basis |
| --- | --- | --- | --- |
| Flaxseed | anticoagulants and antiplatelets | insufficient | A systematic review of RCTs found flaxseed reduced platelet aggregation in healthy people. In a small crossover study it lowered dabigatran exposure in one comparison, judged not meaningful. |

Three drafts from batch 16 are still pending as well: hibiscus × statins, hibiscus × anticoagulants and devil's claw × anticoagulants.

## For the owner

1. **The new flax draft above** needs sign-off.
2. **Flax for menopause and hot flushes: no pair.** A 2013 systematic review found no difference from control and judged flax not indicated for hot flushes, and a 2016 meta-analysis found a non-significant benefit. A 2024 single-blind trial reported very large benefits. I treated this as conflicting and created no pair. Tell me if you would prefer a "mixed" pair instead.

## Gaps and settled plants

- **Yellow loosestrife:** zero human studies in every source. Settled.
- **Horehound:** no trial of the herb alone. A kidney injury case involved a three-plant mixture.
- **Mallow constipation:** still a gap. The 2015 placebo-controlled trial does not state randomisation.
- **Flax carpal tunnel:** a 2014 placebo RCT of topical linseed oil improved symptom and function scores, but the vocabulary has no nerve-entrapment condition.

## Rejected or not added (main reasons)

**Flaxseed:**
- Strong pairs (6-9) were not padded.
- ALA-only and mixed omega-3 studies were not counted as flaxseed.
- A 2025 NAFLD trial that reports only within-group changes.
- A topical knee-oil RCT with no abstract.
- A flaxseed-oil artificial tear that differs from its comparator by two ingredients, with no difference on the primary endpoint.
- PCOS trials (no vocabulary condition; one carries a note of concern).
- A breast cancer review that re-reviews the trial already cited.

**Oregon grape:**
- Psoriasis (9) and eczema (8) were not padded.
- Berberine-only reviews.
- A combination ointment.

**Mallow:**
- A 2014 liver-failure letter with no abstract (worth re-checking if the full text becomes available).
- Combination syrups, mouthwashes and eye drops.
- *Malva parviflora* animal poisonings (another species).
