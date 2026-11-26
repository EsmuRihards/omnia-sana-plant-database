# Research-deepening batch 19 (2026-11-26)

**Plants:** white dead-nettle, bay laurel, lavender, shiitake, motherwort.

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex.
- **Name overrides:** added for all five plants (for example Silexan for lavender, lentinan and *Lentinus edodes* for shiitake).
- **Europe PMC re-run:** two shiitake and motherwort queries timed out and were re-run; nothing new.
- **Full text read:** the 2009 bay leaf diabetes trial in PubMed Central, to confirm randomisation that its abstract does not state.

**Outcome:**
- **Search volume:** about 1,500 PubMed hits (lavender about 710, shiitake about 620) and about 90 abstracts read.
- **New references:** 41 (REF-5426..5466), 3 of them DOI-only records with no PubMed ID.
- **Symptom-tool pairs:** 1,472 -> 1,482.
- **Checks:** validate passes, with refs cited 4,241 / declared 4,241. The species audit raised no flags on the new references.
- **Files:** change log `r19_changes.tsv`; fixer `../fix_r19.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Lavender | fatigue | new | 9 | 2024 meta-analysis in haemodialysis patients, plus RCTs in multiple sclerosis (flower capsules) and chemotherapy (inhaled oil) |
| Lavender | menopause | new | 9 | 2020 meta-analysis plus two inhaled-lavender RCTs; a 2024 oral-oil RCT that did not beat placebo is recorded as a no-effect study |
| Lavender | hot flushes | new | 8 | 2016 randomized crossover trial (fewer hot flushes) plus the meta-analysis |
| Bay laurel | high cholesterol | new | 6 | 2009 randomized placebo trial in type 2 diabetes, plus a 2024 randomized double-blind tea pilot |
| Lavender | arthritis | 1 | 6 | Two knee osteoarthritis RCTs (massage with lavender oil; lavender oil vs piroxicam gel) |
| Shiitake | immune support | 5 | 6 | 2011 randomized crossover trial of a shiitake beta-glucan (more B cells) |
| Bay laurel | blood sugar | new | 5 | 2009 randomized placebo trial in type 2 diabetes |
| Bay laurel | stress | new | 5 | 2026 randomized double-blind tea pilot in healthy adults |
| Bay laurel | anxiety | new | 5 | The same 2026 pilot (anxiety scores) |
| Lavender | menstrual cramps | new | 5 | 2014 placebo RCT of inhaled lavender in primary dysmenorrhoea |
| Lavender | mouth ulcers (oral health) | new | 5 | 2012 double-blind placebo RCT of topical lavender oil |
| Lavender | PMS | new | 5 | 2013 small randomized crossover trial (one inhalation) |
| Shiitake | infection | 1 | 5 | 2022 randomized placebo trial: AHCC (a shiitake mycelium extract) helped clear persistent HPV |

## Safety and other tool data

**Bay laurel:**
- New liver caution: two women who regularly drank bay leaf tea had liver injury. One case was rated probable and she recovered after stopping; the other died of liver failure.
- New caution about swallowing the leaves: whole leaves have blocked the oesophagus (two cases).
- New allergy caution: laurel oil contact dermatitis, and occupational asthma from herb dust.
- New **warning**: an 84-year-old got complete heart block from oleander leaves mistaken for bay.
- The unsourced caution lost "not toxic to people and safe to cook with", which the liver cases contradict. Its leaf and dermatitis sentences moved into the sourced cautions above.

**Lavender:**
- New caution: breast growth in prepubertal children using lavender products (case reports). It sits alongside the review, survey and lab tests that question causality.
- New skin-allergy caution: 2.2% of patients patch-tested at an Australian clinic reacted, and oxidised oil is a stronger allergen.
- Two info notes on Silexan: no relevant effect on CYP1A2, 2C9, 2D6 or 3A4, or on a contraceptive pill. It also did not impair simulated driving, showed no abuse potential and caused no withdrawal.

**Shiitake:**
- New bowel-blockage caution: two surgical cases in people without teeth who ate uncut shiitake, plus one other case.
- The dermatitis caution now cites the French poison-centre series (59 cases, 2014-2019).
- New info note: a shiitake-rich diet slightly raised gabapentin clearance without changing blood levels.

**Draft interactions:** none new. Three from batch 16 are pending: hibiscus × statins, hibiscus × anticoagulants and devil's claw × anticoagulants.

## Research-integrity hold

No new reference is first- or last-authored by the flagged Tehran psychopharmacology group. The 2003 lavender tincture vs imipramine trial is from that group and was not added; lavender depression is already at 9.

## For the owner

1. **Lavender fatigue (9) and menopause (9) are high scores from small, mostly Iranian nursing trials.** The meta-analyses behind them have very high heterogeneity (I² 76-92%), and the menopause one also pools lavender combinations and non-randomized studies. The score is computed, not hand-set, but you may want to know that these are softer than the Silexan anxiety evidence.
2. **Bay laurel liver note uses severity "caution", although one of the two cases was fatal.** Chaga's kidney note in batch 18 is a "warning". Tell me if you'd like bay raised to match.
3. **Bay laurel stress, anxiety and cholesterol rest on one research group's two 10-day pilots in the same 55 people,** registered as two separate trials. Each paper is cited only for its own outcome.
4. **Possible follow-up:** oleander could become a formal Dangerous Lookalikes entry for bay. It would need a sourced toxicology and distinguishing-features write-up, so for now it is a warning note.

## Gaps and settled plants

- **White dead-nettle:** settled. The only human trial was a three-herb combination.
- **Motherwort:** settled. Almost all trials are Chinese motherwort injection (another species and route). A 2011 oil-extract study in hypertension with anxiety had no control group.
- **Lavender headache:** no pair. The post-dural-puncture trial differed only immediately after inhalation, and the 2012 migraine trial does not state randomisation.
- **Bay laurel cookie trial:** glucose was lower at 30-45 minutes, but the overall glucose response did not differ, so it was not added.
- **Shiitake cholesterol:** a double-blind RCT lowered only triglycerides, not cholesterol, so no pair was created.

## Rejected or not added (main reasons)

**Bay laurel:**
- A 2011 diabetes study whose wording copies the 2009 paper, with randomisation not stated.
- A 24-oil inhalation study and a 13-spice meal trial (combinations).
- Impaction, bleeding and perforation letters with no abstract.

**Lavender:**
- Combinations with other oils.
- *L. stoechas* studies (another species).
- Two retracted reviews.
- A serotonin-toxicity letter with sertraline (no abstract; worth re-checking if the full text becomes available).
- Restless legs and dementia agitation (no vocabulary condition).

**Shiitake:**
- Lentinan injections and pleural infusions.
- Lentinan nasal drops in COVID-19 (no symptom benefit).
- Plaque-only dental studies (a surrogate).
- Taste and neuropathy trials (no vocabulary condition; the neuropathy result was null).
- Fermented rice bran and mushroom blends.
