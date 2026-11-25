# Research-deepening batch 9 (2026-11-25)

**Plants:** blessed thistle, coffee, cordyceps (*C. militaris*), coriander, midland hawthorn.

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex. Two targeted PubMed searches covered coffee with levothyroxine and caffeine with quinolone antibiotics.

**Outcome:**
- **Search volume:** about 5,500 PubMed hits (coffee alone: about 4,600; reviews, meta-analyses and safety were read in depth) and about 55 abstracts read.
- **New references:** 17 (REF-5270..5286).
- **Symptom-tool pairs:** 1,439 -> 1,441.
- **Checks:** validate passes, with refs cited 4,061 / declared 4,061. The species audit flagged *Crataegus oxyacantha*, which is now recorded as a synonym on midland hawthorn; the flag is cleared.
- **Files:** change log `r09_changes.tsv`; fixer `../fix_r09.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Coffee | depression | new | 7 | 2016 meta-analysis of observational studies (lower risk; an association) |
| Coffee | metabolic support | 2 | 8 | Green coffee meta-analyses of RCTs: weight (2023) and cardiometabolic markers (2020) |
| Coffee | cognitive function | 1 | 7 | 2024 dose-response meta-analysis (lower Alzheimer's and cognitive-disorder risk; observational) |
| Coriander | migraine | new | 5 | Triple-blind placebo RCT of coriander fruit syrup |
| Hawthorn | high blood pressure | 5 | 8 | 2025 meta-analysis of placebo RCTs (systolic -6.7 mmHg); a 2002 pilot is recorded as no-effect |
| Hawthorn | cardiovascular support | 7 | 8 | 2003 placebo RCT of a fresh-berry extract in heart failure |

## Safety and other tool data

**Coffee:**
- New info note from the BMJ 2017 umbrella review: generally safe at usual intakes, but not in pregnancy, and women at higher risk of fracture may need to limit it.
- The caffeine-and-sleep systematic review is added to the caution.

**Coriander:**
- New caution: lead poisoning linked to adulterated imported coriander powder (case report, 2025).
- The existing caution gains two sources: an anaphylaxis case (coriander as a hidden allergen in beer) and the 2025 diabetes trial (it already mentioned possible blood-sugar effects).

**Hawthorn:** the safety note now cites a systematic review of adverse events (well tolerated, no reported interactions) and a placebo ECG trial (no QT change).

**Draft herb-drug interactions (need owner sign-off):**

| Plant | Drug class | Severity | Basis |
| --- | --- | --- | --- |
| Coffee | thyroid medicines | caution | Coffee cut levothyroxine absorption by roughly a quarter to a third; waiting 60 minutes avoided it (2008 study) |
| Coffee | antibiotics | caution | Quinolones such as enoxacin block caffeine clearance (2000 review) |
| Coffee | serotonergic antidepressants | caution | Fluvoxamine blocks caffeine clearance (same review) |

## For the owner

1. **The 3 draft interactions above** need sign-off.
2. **Two new coffee pairs rest on observational evidence:** depression and cognitive function (7 each). This follows the precedent of coffee's existing liver and diabetes pairs, and each note says "association".
3. **Coffee and blood pressure were left out.** A green coffee extract meta-analysis and an observational meta-analysis both found benefit, but the record's caution says caffeine raises blood pressure (invariant 12d).

## Rejected or not added (main reasons)

**Cordyceps:**
- An insomnia add-on RCT: placebo did better.
- A kidney trial: placebo-controlled, but randomisation is not stated, so it doesn't meet the new-pair bar (recorded as a gap).
- Exercise trials: no vocabulary condition.
- Other *Cordyceps* species.

**Coriander:**
- A sensitive-skin trial: no placebo comparison in the abstract.
- Combinations.
- An insulin autoimmune case (attributed to omeprazole).

**Hawthorn:**
- A 2011 statin add-on RCT: no significant difference from placebo, and no cholesterol pair exists.
- The 2003 Pittler meta-analysis: superseded by the Cochrane review.
- *C. pinnatifida* and *C. mexicana* (different species).
- Mixtures and homeopathic preparations.

**Blessed thistle:** no human study exists. Settled.
