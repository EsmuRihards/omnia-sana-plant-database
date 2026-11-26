# Research-deepening batch 24 (2026-11-26)

**Plants:** Asian ginseng, passionflower, guarana, pelargonium, butterbur.

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex.
- **Name overrides:** added for all five plants (for example Korean red ginseng, EPs 7630 and Umckaloabo for pelargonium, Petadolex and Ze 339 for butterbur).
- **Europe PMC:** re-run after the session was interrupted. It added three ginseng trials: cancer-survivor fatigue, white-ginseng stress, and a null diabetes add-on.

**Outcome:**
- **Search volume:** about 3,300 PubMed hits (ginseng about 2,100) and about 65 abstracts read.
- **New references:** 22 (REF-5548..5569).
- **Symptom-tool pairs:** 1,499 -> 1,503.
- **Checks:** validate passes, with refs cited 4,344 / declared 4,344. The species audit raised no flags on the new references.
- **Files:** change log `r24_changes.tsv`; fixer `../fix_r24.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Ginseng | high blood pressure | new | 9 | 2017 meta-analysis of double-blind RCTs (Korean red ginseng; American ginseng did not work), a 2026 Rg3-ginseng RCT and a 2022 metabolic meta-analysis |
| Ginseng | menopause | new | 7 | 2022 meta-analysis of placebo RCTs (most at risk of bias) |
| Ginseng | hot flushes | new | 7 | The same meta-analysis (small effect) |
| Ginseng | fatigue | 7 | 8 | 2026 double-blind RCT in gastrointestinal cancer survivors |
| Ginseng | stress | new | 6 | Two double-blind RCTs (2025 red ginseng; 2025 white ginseng) |
| Ginseng | arthritis | 1 | 5 | 2021 double-blind RCT in hand osteoarthritis |

**No-effect study recorded:** a 2026 Korean red ginseng add-on trial in type 2 diabetes did not change fasting glucose or HbA1c, so it is recorded on blood sugar.

## Safety and other tool data

- **Butterbur:** new liver **warning**. Even the PA-free extract Petadolex has rare liver-injury reports; nine were severe and two needed a transplant. The record previously had only the raw-plant PA caution.
- **Guarana:** new heart-rhythm **warning**, from two case reports:
  - Ventricular fibrillation after a guarana energy drink.
  - Atrial fibrillation after guarana tablets containing 1.6 g of caffeine.
- **Passionflower:**
  - New heart caution: a case of prolonged QT and runs of ventricular tachycardia at usual doses.
  - The pregnancy caution now cites a series of five exposed pregnancies with neonatal complications.
  - The approved sedatives interaction now cites a valerian + passionflower + lorazepam case.
- **Pelargonium:**
  - New allergy caution: 34 WHO pharmacovigilance reports, two with circulatory collapse.
  - New liver info note: causality analysis found no probable cases, and safety studies in adults and young children raised no concerns.
- **Ginseng:** info notes on a fibroid-safety RCT (no growth versus placebo) and a pregnancy review.

**Draft interactions:** none new. Six are still pending.

## Research-integrity hold

The hold applies to passionflower: nothing new was added from the flagged group, and its pairs are unchanged.

## For the owner

1. **Ginseng high blood pressure scores 9 from two meta-analyses plus an RCT.** The benefit is for Korean red ginseng; American ginseng trials were negative, and the note says so.
2. **Butterbur and guarana warnings.** Both use severity "warning" for life-threatening events: liver transplant and ventricular fibrillation.

## Gaps and settled plants

- **Ginseng COPD:** a 2019 *Thorax* 12-month RCT found no difference from placebo. There is no respiratory pair to attach it to.
- **Guarana anorexia and hot flushes:** single-arm pilots only.
- **Butterbur in children with migraine:** better than placebo only at follow-up.

## Rejected or not added (main reasons)

- **Strong pairs were not padded:** passionflower anxiety (10), stress and insomnia; pelargonium respiratory pairs (7-9); guarana fatigue and cognition; butterbur allergy and migraine; ginseng libido, fatigue and cholesterol.
- **Combinations:** Ze 185, Euphytose, honey/propolis/zinc, Saengmaeksan, Ma Huang + guarana.
- **Biomarker-only studies:** ginseng NK cells, butterbur airway challenge.
- **Other species:** American ginseng, notoginseng, *Petasites japonicus*, passion fruit.
