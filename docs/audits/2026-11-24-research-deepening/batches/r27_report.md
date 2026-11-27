# Research-deepening batch 27 (2026-11-27)

**Plants:** pygeum, wild cherry, psilocybin mushroom, lungwort, Japanese knotweed.

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex.
- **Name overrides:** added for all five plants.
- **Psilocybin mushroom:** searched with "psilocybin" in titles. The record already relies on purified psilocybin, labelled as compound evidence. The trial listing was capped at 200 of 445 hits, so headache trials were searched directly.
- **Japanese knotweed:** searched by its synonyms (*Polygonum cuspidatum*, *Fallopia japonica*, Hu Zhang) but not "resveratrol", which mostly comes from other sources.
- **Lungwort:** tree lungwort (a lichen) is a different organism.

**Outcome:**
- **Search volume:** about 1,600 PubMed hits (psilocybin about 1,250) and about 50 abstracts read, plus the migraine trial's registry record.
- **New references:** 15 (REF-5612..5626).
- **Symptom-tool pairs:** 1,516 (unchanged; one score raised).
- **Checks:** validate passes, with refs cited 4,401 / declared 4,401. The species audit raised no flags on the new references (110 suspects, unchanged).
- **Files:** change log `r27_changes.tsv`; fixer `../fix_r27.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Psilocybin mushroom | anxiety | 5 | 8 | 2020 meta-analysis of psilocybin trials in life-threatening illness (lower anxiety scores than control). Before, it rested on one RCT and rodent studies. Compound evidence. |

## Safety and other tool data

- **Psilocybin mushroom:**
  - New kidney caution: acute kidney injury after eating confirmed *P. cubensis*.
  - New heart and blood pressure caution: about +19/9 mmHg for a few hours in supervised studies, plus a ventricular fibrillation case in a man on a stimulant.
  - New mental-health caution: six months of catatonia after a first dose in a man with no psychiatric history.
  - The existing caution (lithium seizures, triggering latent psychiatric illness) now cites an analysis of 62 lithium reports (47% involved seizures) and two mania/psychosis cases.
  - New info note: about 10% of people worsened in depression trials (similar to escitalopram), and in Oregon's regulated services 1.2% needed medical attention.
- **Japanese knotweed:** new liver caution (probable liver injury after 14 days of a Huzhang formula; the authors point to emodin).
- **Pygeum:** new lab-safety info note (rat studies: no harm at up to 1,000 mg/kg daily; organ damage only at very high doses).

**Draft interactions:** two new.
- **Psilocybin mushroom × serotonergic antidepressants** (caution): SSRIs and SNRIs weakened mushroom effects in about half of 611 reports.
- **Japanese knotweed × immunosuppressants** (insufficient): in rats, knotweed root changed methotrexate blood levels through a drug transporter.

Nine drafts are now pending.

## For the owner (queued for the end-of-campaign review)

1. **Psilocybin anxiety now scores 8 on compound evidence.** It rests on small trials of purified psilocybin in people with life-threatening illness, not on the mushroom itself (the same basis as the depression score of 10).
2. **The old psilocybin caution says "physiologically non-toxic".** That sits awkwardly beside the new kidney and heart cautions. The text predates this campaign; tell me if you would like it reworded.
3. **The two draft interactions above need your approval.**

## Gaps and settled plants

- **Psilocybin migraine:** a 2021 crossover (10 people) was positive, but the randomisation is stated only in the trial registry. A 2026 RCT (18 people) missed its primary outcome, so there is no pair.
- **Psilocybin cluster headache:** the 2022 RCT was not significant.
- **Psilocybin, other conditions:** alcohol, smoking, OCD, anorexia, PTSD and bipolar depression have no vocabulary condition or only open pilots. Chronic pain evidence is open pilots only.
- **Pygeum:** prostate and urinary pairs (9) were not padded.
- **Wild cherry:** settled. A black cherry concentrate kidney case was not attached because the fruit species was not stated, and the record covers the bark.
- **Lungwort:** settled. The only other hit was a different *Pulmonaria* species.

## Rejected or not added (main reasons)

- **Combinations:**
  - Pygeum + nettle, pygeum hair-loss blend, Prostaquil.
  - Huzhang and Tongfeng gout formulas, knotweed + hawthorn, two multi-extract supplements.
- **Surrogate outcomes:** knotweed inflammatory-marker trials.
- **Not randomised:** pseudo-randomised Gulf War illness trial; a 1991 pygeum series with no control group.
- **Other species:** Makore wood "African cherry" asthma (*Tieghemella*); takotsubo after *Psilocybe semilanceata*.
- **Pooled with other drugs:** the Cochrane psychedelics review (psilocybin + LSD); a microdosing review.
- **No abstract:** serotonin-syndrome cases, a prolonged mania case, a JAMA Netw Open outcomes letter.
