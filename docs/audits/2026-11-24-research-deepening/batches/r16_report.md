# Research-deepening batch 16 (2026-11-26)

**Plants:** witch hazel, devil's claw, ivy leaf, lion's mane, hibiscus (roselle).

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex. Name overrides were added for all five plants; ivy also searched the Prospan and EA 575 product names.

**Outcome:**
- **Search volume:** about 750 PubMed hits (hibiscus about 280, ivy about 160) and about 40 abstracts read.
- **New references:** 13 (REF-5391..5403).
- **Symptom-tool pairs:** 1,467 -> 1,468.
- **Checks:** validate passes, with refs cited 4,178 / declared 4,178. The species audit flagged prose ("Hibiscus intake, tea"); "intake" and "tea" were added to its stop list.
- **Files:** change log `r16_changes.tsv`; fixer `../fix_r16.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Hibiscus | liver support | new | 5 | 2014 randomized trial vs control in obese adults: less weight and body fat, and improved fatty liver |

**Ivy cough and bronchitis stay at 7.** I added the 2019 EA 575 placebo RCT as an independent replication of the 2016 trial already cited. The 2022 meta-analysis was **not** added: it pools exactly those two trials, so citing it as well would count the same evidence twice. It would have pushed ivy bronchitis to 10.

**No-effect study recorded:** a 2022 single-blind placebo study found that lion's mane (10 g a day for 4 weeks) did not change cognition.

## Safety and other tool data

**Devil's claw:**
- New info note: in a 2008 review of 28 trials, minor side effects (mainly digestive) affected about 3% of patients, and no double-blind trial found more than with placebo.
- New caution: low blood sodium (SIADH) twice in one patient, the second time after restarting the herb.
- The ulcer caution now cites a Prescrire review of gastrointestinal bleeding cases.
- The warfarin caution now cites a 2000 review.

**Ivy:** the allergy note now cites two anaphylaxis cases after ivy syrup and a falcarinol contact-dermatitis review.

**Lion's mane:** new lung caution from a case of acute respiratory distress syndrome after a lion's mane extract.

**Hibiscus:** the medicines caution now cites a volunteer study in which hibiscus drink sped up paracetamol elimination.

**Draft herb-drug interactions (need owner sign-off):**

| Plant | Drug class | Severity | Basis |
| --- | --- | --- | --- |
| Hibiscus | statins | caution | In a randomized crossover study in volunteers, hibiscus tea cut simvastatin exposure by about a third (AUC ratio 0.65). The authors advise against combining them. |
| Hibiscus | anticoagulants and antiplatelets | caution | A woman on long-term warfarin had a markedly raised INR after starting hibiscus tea; it normalised after stopping (2026 case report). |
| Devil's claw | anticoagulants and antiplatelets | insufficient | Reviews list devil's claw as possibly strengthening warfarin, based on case reports; no clinical study. The record's caution already warned of this, but the checker had no entry. |

## For the owner

1. **The three drafts above** need sign-off.
2. **Ivy double-counting avoided:** the meta-analysis was left out because it re-pools trials already cited. Tell me if you'd prefer a different rule, such as citing the meta-analysis instead of its trials.

## Settled or no change

- **Witch hazel:** dead end. A 1995 double-blind RCT in eczema found the cream no better than its vehicle (no eczema pair exists).

## Rejected or not added (main reasons)

**Devil's claw:**
- Arthritis, back pain and pain are already at 8, so they were not padded.
- A hypertension case with no abstract.
- The 2016 *Spine* republication of the Cochrane review (the 2014 version is already cited).

**Ivy:** combinations (with thyme, primula or coptis), ivy-vs-ivy trials, observational studies and an in-vitro CYP study.

**Lion's mane:**
- A mood and sleep study with no control group.
- A liver case attributed to *Agaricus* in a mixed mushroom powder.

**Hibiscus:**
- Its strong pairs (8-10) were not padded.
- Active-comparator and combination trials.
- An amlodipine interaction study (rats).
- Letters with no abstract.
