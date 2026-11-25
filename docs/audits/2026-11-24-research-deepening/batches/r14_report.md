# Research-deepening batch 14 (2026-11-25)

**Plants:** fennel, birch polypore, white bedstraw, cleavers, lingzhi (reishi).

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex. Name overrides were added for all five plants; lingzhi also searched *Ganoderma lucidum* (invariant 11).

**Outcome:**
- **Search volume:** about 1,050 PubMed hits (lingzhi: about 620; fennel: about 420) and about 45 abstracts read.
- **New references:** 18 (REF-5356..5373).
- **Symptom-tool pairs:** 1,459 -> 1,463.
- **Checks:** validate passes, with refs cited 4,148 / declared 4,148.
- **Species audit:** it flags "*Ganoderma lucidum*" on the new lingzhi references. This is expected: the owner decision of 2026-11-11 (invariant 11) counts East Asian *G. lucidum* research for *G. lingzhi*. Adding *G. lucidum* as a synonym would be taxonomically false, so the warning stays.
- **Files:** change log `r14_changes.tsv`; fixer `../fix_r14.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Fennel | PMS | new | 5 | 2011 single-blind placebo RCT |
| Fennel | arthritis | new | 5 | 2020 double-blind placebo RCT in knee osteoarthritis (pain and WOMAC improved) |
| Lingzhi | prostate support | new | 6 | Two 2008 placebo RCTs in men with lower urinary tract symptoms (IPSS improved) |
| Lingzhi | high cholesterol | new | 5 | 2025 spore-oil crossover RCT; a 2016 placebo RCT and the Cochrane review are recorded as no-effect |
| Lingzhi | blood sugar | 2 | 5 | 2025 RCT vs kombucha and control; the 2016 placebo RCT is recorded as no-effect and the note says results are mixed |

**No-effect study recorded:** a 2018 fennel placebo RCT in menopause found no difference, because of a high placebo response.

## Safety and other tool data

**Fennel:**
- **Two unsourced notes rewritten to their sources.** Both had consumer drug-database wording and were showing on the live page.
  - **Pregnancy:** the note said fennel "has been linked to preterm birth". The 2012 Italian cohort linked *almond oil* to preterm birth; the 2015 southern-Italy cohort linked regular fennel use to a *shorter gestational age*. The note now states the 2015 finding.
  - **Allergy:** rewritten to what a 1991 skin-test study and a 2013 mugwort-fennel case state. They support cross-reaction with celery, birch and mugwort; carrot is not named.
- New caution: premature breast development in babies and young girls given fennel tea or preparations; it regressed after stopping (case reports).
- New caution: fennel essential oil is among the plant oils known to provoke seizures (case series and review).

**Lingzhi:**
- New liver caution: acute hepatitis after reishi powder taken with alcohol, and a case of eosinophilic liver nodules that cleared after stopping.
- The safety note now cites a 2007 placebo-controlled safety RCT and a 1990 human platelet study.

**Draft herb-drug interaction (needs owner sign-off):**

| Plant | Drug class | Severity | Basis |
| --- | --- | --- | --- |
| Lingzhi | anticoagulants and antiplatelets | caution | Reishi 1 g three times a day for 2 weeks reduced platelet aggregation by up to about 30% in patients with atherosclerotic disease (1990 clinical study) |

Three drafts are now pending: saffron × anticoagulants (batch 10), field horsetail × antiretrovirals (batch 12) and lingzhi × anticoagulants (this batch).

## For the owner

1. **The lingzhi draft interaction above** needs sign-off.
2. **Fennel still has six unsourced (needs-review) notes showing on its page.** They cover oral and skin safety, breastfeeding, infant colic, bleeding and hormone-sensitive conditions. Two of them are word-for-word duplicates (the skin/sun note appears twice). They belong to the unsourced-claims campaign.
3. **Lingzhi liver support was withheld.** A 2017 crossover RCT in healthy volunteers found lower liver enzymes, but this batch adds liver-injury case reports.
4. **Lingzhi blood sugar is now mixed (5).** One positive 2025 trial sits against a null 2016 placebo trial and a null Cochrane review. The note says so; tell me if you would rather keep it at the review's verdict.

## Settled (no human study)

- **Birch polypore, white bedstraw and cleavers:** no human study (birch polypore was deep-searched on 2026-11-16).

## Rejected or not added (main reasons)

**Fennel:**
- Null trials with no matching pair: sleep, lipids and sexual desire.
- Vaginal-atrophy creams and hirsutism gels (no vocabulary condition).
- Active comparators (dimethicone, mefenamic acid, evening primrose).
- Many combinations.
- A menstrual-bleeding meta-analysis with no abstract.

**Lingzhi:**
- An Alzheimer's spore-powder trial (no difference).
- Immune RCTs (the pair is already 7).
- Fibromyalgia trials (no vocabulary condition).
- Combinations with *Cordyceps* or San Miao San.
- Other *Ganoderma* species.
