# Research-deepening batch 13 (2026-11-25)

**Plants:** California poppy, eucalyptus (blue gum), eyebright, meadowsweet, dropwort.

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex.
- **Name overrides:** added for all five plants; eucalyptus also searched 1,8-cineole / eucalyptol in titles (its signature compound).
- **Europe PMC:** four queries timed out; the rest completed.

**Outcome:**
- **Search volume:** about 340 PubMed hits (eucalyptus: about 260) and about 30 abstracts read.
- **New references:** 10 (REF-5346..5355).
- **Symptom-tool pairs:** 1,455 -> 1,459.
- **Checks:** validate passes, with refs cited 4,130 / declared 4,130. The species audit flagged prose ("Eucalyptus than", "Eucalyptus aromatherapy"); those words were added to its stop list.
- **Files:** change log `r13_changes.tsv`; fixer `../fix_r13.py`.

## Score changes

Unnamed "eucalyptus oil" is assigned to *E. globulus* (invariant 10), as the record already does.

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Eucalyptus | allergy | new | 7 | 2025 systematic review of three trials: rhinitis quality of life improved vs placebo; nasal symptom score not significant |
| Eucalyptus | bronchitis | new | 5 | 2013 placebo RCT of 1,8-cineole capsules (compound evidence, labelled): symptoms and coughing fits fell within 4 days |
| Eucalyptus | pain | new | 5 | 2013 RCT: inhaled eucalyptus oil vs almond oil after knee replacement |
| Eucalyptus | headache | new | 5 | 2026 small RCT vs usual care: inhaled eucalyptus oil eased dialysis headache |

## Safety and other tool data

**Eucalyptus:**
- New poisoning caution:
  - Melbourne series of 109 children who swallowed the oil: 59% had symptoms, and 3 were unconscious after 5-10 mL; all recovered.
  - A Queensland series found most children symptom-free.
  - A review of 110 seizure cases: seizures followed swallowing, inhaling or skin application.
  - A fatal adult case after 15 mL.
- New info note: the 2023 Cosmetic Ingredient Review found six *E. globulus*-derived ingredients safe in cosmetics when formulated to be non-sensitising.

**Draft interactions:** none in this batch. Pending from earlier batches: saffron × anticoagulants and field horsetail × antiretrovirals.

## For the owner

1. **The eucalyptus headache (5) and pain (5) pairs rest on single small aromatherapy trials.** The headache trial had 11 patients per group and was compared with usual care, not a placebo. Both meet the new-pair rule (a randomized trial that finds benefit) but are thin.
2. **California poppy gap.** A. Vogel's placebo-controlled RCT of Eschscholzia tablets for insomnia (NCT06795776) finished in November 2025 but has no results or publication yet. It's worth rechecking.

## Settled or no change

- **California poppy:** no published single-herb human trial (only combinations with valerian, or with hawthorn and magnesium).
- **Eyebright:** both "new" studies are the Weleda homeopathic eye-drop products already purged as REF-2173 and REF-0613.
- **Meadowsweet:** no single-herb trial.
  - A child's severe gastrointestinal bleed came from a multi-herb syrup (meadowsweet + willow), so it was not attributed.
  - A 2024 Russian cognition study has no retrievable abstract.
- **Dropwort:** every human hit was water dropwort (*Oenanthe*), a different and often deadly genus.

## Rejected or not added (main reasons)

**Eucalyptus:**
- A 2014 pre-operative anxiety RCT: the cineole arm worked, but the eucalyptus-oil arm did not clearly beat control, so there is no anxiety pair.
- A eucalyptol nursing-home pilot (not randomised; dementia scores unchanged).
- A leaf-extract liver-fat pilot (difference only after unblinding).
- An active-comparator toothpaste trial.
- Many combinations (eucalyptol-limonene-pinene capsules, turpentine ointment, nasal sprays, peppermint + eucalyptus headache products).
- A mouse diazepam study.
