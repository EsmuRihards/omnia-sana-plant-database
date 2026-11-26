# Research-deepening batch 15 (2026-11-26)

**Plants:** gentian, water avens, ginkgo, licorice, gymnema.

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex. Name overrides were added for all five plants; licorice also searched glycyrrhizin and glycyrrhizic / glycyrrhetinic acid in titles.

**Outcome:**
- **Search volume:** about 4,700 PubMed hits (ginkgo: about 2,250; licorice: about 2,290). For these two, meta-analyses, safety and conditions with no pair yet were read in depth, and pairs already at 8-10 were not padded. About 55 abstracts read.
- **New references:** 17 (REF-5374..5390).
- **Symptom-tool pairs:** 1,463 -> 1,467.
- **Checks:** validate passes, with refs cited 4,165 / declared 4,165. The species audit flagged "Glycyrrhiza exposure" (prose), and "exposure" was added to its stop list.
- **Files:** change log `r15_changes.tsv`; fixer `../fix_r15.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Ginkgo | blood sugar | new | 8 | 2020 meta-analysis in type 2 diabetes (HbA1c; authors call the evidence limited) and a 2018 placebo RCT added to metformin |
| Ginkgo | low libido | new | 8 | 2014 triple-blind RCT in postmenopausal women and a 2021 systematic review; two placebo trials of antidepressant-induced sexual problems recorded as no-effect |
| Ginkgo | cardiovascular support | 1 | 7 | 2026 meta-analysis of 14 placebo RCTs: a modest walking-distance gain in intermittent claudication; the earlier null Cochrane review stays alongside |
| Ginkgo | PMS | new | 5 | 2009 placebo RCT |
| Licorice | oral health | 7 | 8 | 2022 double-blind placebo RCT: a licorice gargle eased mouth-ulcer pain |
| Licorice | depression | new | 5 | 2020 placebo RCT of glycyrrhizic acid added to SSRIs (compound evidence, labelled) |
| Licorice | infection | 1 | 5 | 2016 RCT: licorice added to H. pylori triple therapy raised eradication (83% vs 63%) |

## Safety and other tool data

**Licorice:** the glycyrrhizin warning now also cites:
- a 2018 meta-analysis of 26 trials (diastolic pressure rose by 1.7 mmHg);
- two Finnish cohort studies (2009, 2017): children of mothers with high glycyrrhizin intake in pregnancy had lower IQ and memory scores, more ADHD problems and earlier puberty.

**Ginkgo:** new info note from a 2011 meta-analysis of placebo-controlled trials: standardized extract did not change clotting measures toward a higher bleeding risk. The approved blood-thinner interaction still stands, because of the case reports.

**Gymnema:**
- New liver caution from a 2010 toxic hepatitis case.
- The 2018 EFSA risk assessment now sources the existing caution that gymnema can add to diabetes medicines.

**Draft interactions:** none in this batch. Three remain pending: saffron × anticoagulants, field horsetail × antiretrovirals and lingzhi × anticoagulants.

## For the owner

1. **Ginkgo cardiovascular support went from 1 to 7 on a single 2026 meta-analysis** that found a modest, borderline benefit (p = 0.049). It conflicts with the 2013 Cochrane review, and the note says so. If you want Cochrane to prevail, I can withhold the new meta-analysis.
2. **Ginkgo low libido starts at 8**, but the benefit is confined to postmenopausal women. Antidepressant-induced sexual problems showed no effect, and the note says so.
3. **Licorice depression (5) is compound evidence:** glycyrrhizic acid capsules, not licorice root. The glycyrrhizin warning (blood pressure, potassium) applies to that compound.

## Settled or no change

- **Water avens:** zero hits in every family.
- **Gentian:** no new single-herb trial. The bitter-pudding study measured food intake in healthy people; the rest are combinations or Veratrum poisonings (a gentian lookalike).

## Rejected or not added (main reasons)

**Ginkgo:**
- A hypertension systematic review (no firm conclusion).
- An older claudication meta-analysis (superseded).
- Reviews of tinnitus, dizziness, hearing loss, mountain sickness, ADHD, schizophrenia, glaucoma and vitiligo (no vocabulary condition).
- Chinese ginkgo injections and patent medicines.

**Licorice:**
- Caries reviews (bacterial counts only).
- Active-comparator trials (tetracycline gel, ibuprofen, oestrogen cream).
- Weight loss (it conflicts with the blood-pressure warning).
- Atopic dermatitis (review found insufficient evidence; compound glycyrrhizin products).
- 1970s DGL ulcer trials, glycyrrhizin injections, Kampo and Chinese formulas.

**Gymnema:** sweet-taste trials (no vocabulary condition) and multi-herb Ayurvedic products.
