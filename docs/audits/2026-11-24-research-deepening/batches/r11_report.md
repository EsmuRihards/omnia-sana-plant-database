# Research-deepening batch 11 (2026-11-25)

**Plants:** wild carrot, wild yam, echinacea, cardamom, eleuthero (Siberian ginseng).

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex. Name overrides were added for all five plants (for example *Acanthopanax senticosus* for eleuthero). Europe PMC-only hits were screened and three were read in full abstract.

**Outcome:**
- **Search volume:** about 1,200 PubMed hits (echinacea alone: about 500; most wild carrot hits were crop science) and about 75 abstracts read.
- **New references:** 27 (REF-5315..5341).
- **Symptom-tool pairs:** 1,453 -> 1,455.
- **Checks:** validate passes, with refs cited 4,116 / declared 4,116. The species audit flagged "Echinacea groups" (trial prose); "group" and "groups" were added to its stop-word list and the flag is cleared.
- **Files:** change log `r11_changes.tsv`; fixer `../fix_r11.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Echinacea | infection | 5 | 9 | 2024 ERA-PRIMA meta-analysis (fewer respiratory infections, complications and antibiotics) and a 2022 randomized trial; placebo trials in genital herpes and in otitis-prone children are recorded as no-effect |
| Echinacea | immune support | 6 | 7 | 2005 placebo-controlled study during colds; two pressed-juice crossover trials are recorded as no-effect |
| Cardamom | blood sugar | new | 8 | 2022 meta-analysis (HbA1c and insulin resistance fell; fasting glucose did not) and a 2019 placebo RCT in type 2 diabetes; a pre-diabetes RCT is recorded as no-effect |
| Cardamom | liver support | new | 5 | 2018 placebo RCT in fatty liver disease (less fatty liver, lower ALT) |
| Cardamom | high blood pressure | 7 | 8 | 2024 meta-analysis; the note states the falls were under 1 mmHg |
| Eleuthero | immune support | 7 | 8 | 1987 double-blind study (more T cells and NK cells); a 2001 athlete trial is recorded as no-effect |

**Other no-effect studies recorded:**
- Eleuthero stress: in a 2001 placebo trial in athletes, hormonal markers of stress rose rather than fell.
- Wild carrot high cholesterol: dried purple carrot did not lower cholesterol in a small placebo trial.

## Safety and other tool data

**Echinacea:**
- The safety note now cites a 2026 meta-analysis of 48 trials (adverse events were no more common than with control).
- New caution: allergy. Reactions are rare but can be severe, and *E. purpurea* is among the herbs most often reported for allergy-like reactions in children.
- New caution: pregnancy and breastfeeding (too few data; the safety review advises against use).
- New info note: in human studies, *E. purpurea* did not meaningfully change levels of docetaxel, darunavir-ritonavir or etravirine, and had no significant effect on four CYP enzymes.

**Eleuthero:**
- New info note: no effect on CYP2D6 or CYP3A4 in healthy volunteers.
- New caution: eleuthero (Acanthopanax) injections used in Chinese hospitals have caused anaphylactic shock, sometimes fatal (57 cases reviewed).

**Wild carrot:** new caution for carrot food allergy, linked to birch pollen (a placebo-controlled food-challenge study and a case report).

**Wild yam:** new info note from the 2004 Cosmetic Ingredient Review safety assessment (safe as used in cosmetics; no oestrogen-like activity in rats).

**Draft interactions:** none in this batch. The saffron × anticoagulants draft from batch 10 is still awaiting sign-off.

## For the owner

1. **Echinacea infection went from 5 to 9.** It rests mainly on the ERA-PRIMA meta-analysis, which pools Echinacea products and finds fresh *E. purpurea* extracts the strongest. Two null *E. purpurea* placebo trials are shown alongside it.
2. **Cardamom blood pressure went from 7 to 8** on a second meta-analysis whose effect was statistically significant but tiny (under 1 mmHg). The note says so.
3. **Research-integrity rule applied:** no trial from the flagged research group came up in this batch.

## Rejected or not added (main reasons)

**Echinacea:**
- The cold pair (already 9, with five no-effect trials) was not padded either way; further positive and null trials are logged in the notes.
- Anxiety trials used EP107, which is *E. angustifolia* root (a different species).
- Oral lichen planus, tonsillitis and COVID syrup trials (species not stated).
- Warfarin and digoxin studies (species not stated in the abstract).
- A 2015 recurrent-infection meta-analysis (superseded by ERA-PRIMA).
- Combinations (Kan Jang, Imupret, echinacea + zinc, propolis, ginger or sage).

**Cardamom:**
- A second publication of the fatty-liver trial (the same trial, not counted twice).
- A peppermint vs cardamom ice-cube trial for post-operative nausea (no significant difference from placebo stated).
- Black cardamom (*Amomum subulatum*), PCOS gene-expression trials, combinations.

**Eleuthero:**
- A fruit-extract blood-pressure RCT: the record cautions about uncontrolled high blood pressure (invariant 12d).
- A lipid RCT (within-group changes only).
- Quality-of-life, endurance, hangover and bone trials (no vocabulary condition).
- An active-comparator bipolar trial.
- Acanthopanax stroke injections and multi-herb products.

**Wild carrot:**
- A carrot seed + clomiphene + lifestyle male-infertility RCT: the carrot effect isn't isolated, and the seed is a folk contraceptive.
- Jazar and wild-carrot halva (multi-herb products).
- Letters with no abstract.

**Wild yam:** still no human trial of oral wild yam. The Japanese "yam" cognition RCT does not name the species.
