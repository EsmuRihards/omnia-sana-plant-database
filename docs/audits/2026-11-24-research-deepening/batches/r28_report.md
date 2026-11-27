# Research-deepening batch 28 (2026-11-27)

**Plants:** rhodiola, marsh Labrador tea, blackcurrant, dog rose, Japanese rose.

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex.
- **Name overrides:** added for all five plants.
- **Species traps avoided:**
  - Bare "rhodiola" was not searched (Chinese products are often *R. crenulata*).
  - Bog Labrador tea (*R. groenlandicum*) is a different species.
  - "Rosehip" papers were species-checked in the full text.
- **Rhodiola:** stress and anxiety RCTs were also searched directly.

**Outcome:**
- **Search volume:** about 1,090 PubMed hits (rhodiola about 465, blackcurrant about 400) and about 55 abstracts read, plus three full texts (species checks).
- **New references:** 9 (REF-5627..5635).
- **Symptom-tool pairs:** 1,516 -> 1,519.
- **Checks:** validate passes, with refs cited 4,410 / declared 4,410. The species audit raised no flags on the new references (110 suspects, unchanged).
- **Files:** change log `r28_changes.tsv`; fixer `../fix_r28.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Blackcurrant | cardiovascular support | 3 | 6 | 2023 six-month placebo RCT in menopausal women (lower triglycerides and inflammatory markers) |
| Blackcurrant | muscle soreness | new | 5 | 2021 double-blind RCT (less soreness at 24/48 h); two null RCTs stay alongside |
| Dog rose | metabolic support | 7 | 8 | 2015 double-blind RCT: less visceral fat and lower BMI (before: animal studies and reviews only) |
| Dog rose | high cholesterol | new | 5 | 2012 double-blind crossover in obese adults (LDL -6%; *Rosa canina* confirmed in the full text) |
| Dog rose | high blood pressure | new | 5 | The same trial (systolic -3.4%) |

## Safety and other tool data

- **Rhodiola:**
  - New medicines caution: in a randomised crossover, rhodiola reduced CYP2C9 activity by about 21% (other CYP enzymes unchanged).
  - New info note: US supplements varied widely in active content, one appeared spiked with synthetic salidroside, and all capsules had trace arsenic, cobalt and lead.

**Draft interactions:** one new, **marsh Labrador tea × CYP3A4 substrates** (insufficient; lab study only). Ten drafts are now pending.

## For the owner (queued for the end-of-campaign review)

1. **Blackcurrant for infant eczema: no pair (inv. 12d).** A 2010 RCT gave the seed oil to mothers from early pregnancy and found less eczema at 12 months (not 24). The record's caution says maternal trials do not mean pregnancy use is recommended. This is the same pattern as anise and breastfeeding, and evening primrose and labour induction.
2. **Rhodiola stress: no pair.** The only randomised stress trial compared rhodiola with no treatment (not placebo), and its authors say causality cannot be determined. The other stress and burnout studies were open-label.
3. **Glaucoma has no vocabulary condition.** A two-year blackcurrant RCT slowed visual-field loss.
4. **The new Labrador tea draft needs your approval.**

## Gaps and settled plants

- **Blackcurrant blood pressure:** a 2023 meta-analysis of four RCTs was null.
- **Rhodiola:** fatigue (7), cognitive function (6) and depression (5) were not padded.
- **Dog rose:** arthritis (10) and inflammation (8) were not padded.
- **Marsh Labrador tea:** settled for efficacy (homeopathic Ledum only).
- **Japanese rose:** settled.

## Rejected or not added (main reasons)

- **Combinations:**
  - Rhodiola: with caffeine, saffron or Cimicifuga; ADAPT-232.
  - Blackcurrant: mixed-berry and anthocyanin-blend drinks.
  - Dog rose: Lady Prelox; cartilage + rosehip.
- **Other species:** *Rhodiola crenulata*, Chinese "rhodiola" injections, *Rosa mosqueta* oil, bog Labrador tea.
- **No vocabulary condition:** sport-performance trials (rhodiola, blackcurrant), rosehip for orthostatic intolerance.
- **Not randomised or open-label:** rhodiola burnout and life-stress studies, a Chinese blackcurrant-oil capsule study, rosehip-oil skin studies.
- **No abstract:** a false-positive digoxin assay letter (hibiscus + rose hip tea).
