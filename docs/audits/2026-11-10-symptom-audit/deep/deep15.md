# Deep audit - batch 15 (2026-11-13)

Plants 141-150: raspberry, sorrel, butcher's broom, white willow, chia, sage, rosemary,
elder, soapwort, schisandra. 71 pairs before, 73 after.

Same two-part pass as batch 14: the strict `!NAME` check (does each direct source name the
symptom?) plus the deep checks from `deep01.md`.

Result:
- 153 changes.
- 29 refs added (REF-3735..3763); 1 deleted (REF-1260).
- Log: `d15_changes.tsv`. Fixer: `fix_deep15.py`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Elder / safety note | The main safety note was pasted Wikipedia text full of link fragments. It cited Kew's taxonomy database and a flu trial, and neither says anything about toxicity | Rewritten from the NIH (NCCIH) elderberry page and the EU flower monograph. NCCIH says little is known about pregnancy, so the old "should not be consumed in pregnancy" line now reads "not recommended because safety has not been established" |
| Elder / second safety note | Said use for colds, bronchitis and fever "is well-supported". A larger 2020 flu trial found no benefit, and a 2021 systematic review rated the evidence uncertain | Sentence removed. The cold note now presents both sides |
| Soapwort / safety note | Begins "SERIOUS: ... can cause haemolysis" but was filed with severity `info` | Severity changed to `serious` |
| Sorrel | Chevallier and Grieve were cited on all 10 pairs. Grieve's sorrel entry covers diuretic, fever, scurvy, ringworm and kidney gravel. It says nothing on rheumatism, bloating, indigestion, UTI or wounds | Removed. Arthritis, bloating, UTI and wounds dropped |
| Sorrel / urinary support | Grieve's "gravel and stone" use contradicts the plant's own oxalate warning (avoid if prone to kidney stones) | Dropped (organ-of-own-warning rule) |
| Butcher's broom | The meta-analysis and two reviews are on Cyclo 3 Fort (Ruscus + hesperidin + vitamin C), and another study tested a four-ingredient product | Removed as combinations. The Ruscus-only placebo RCT (Vanscheidt 2002) now carries varicose veins and swelling. Pain dropped |
| White willow | The 2006 Cochrane review was cited, but the 2014 update supersedes it | Purged and deleted (the 2014 update is kept) |
| Raspberry / menstrual cramps | A guinea-pig gut study and a rat endometriosis study. Neither names cramps | Dropped |
| Raspberry / pregnancy | A labour RCT (no shorter labour) and a 2021 systematic review ("evidence base weak") were missing or treated as support | Both recorded as no-effect. The note now says the evidence is weak |
| Chia / heart health | A meta-analysis and an SR finding no significant effect on CV risk factors were cited as support | Recorded as no-effect. Two blood-pressure meta-analyses added |
| Rosemary / muscle spasm | Smooth-muscle (gut) antispasmodic, off-target for muscle spasm | Dropped |
| Sage / memory | A mouse study of a two-species sage mixture | Removed. Three human RCTs added (Alzheimer's, older adults, mood and attention) |

## Added under the owner rule

| Plant | New pair | Source |
|---|---|---|
| Raspberry | arthritis | RCT (knee osteoarthritis pain) |
| Chia | high blood pressure | 2 meta-analyses, 2 RCTs |
| Sage | PMS | RCT |
| Sage | high cholesterol | 2 RCTs |
| Sage | blood sugar | RCT (type 2 diabetes) |
| Sage | skin irritation | RCT (UV redness, matched hydrocortisone) |
| Rosemary | anxiety | 3 RCTs (students; depression add-on; before surgery) |
| Rosemary | depression | 2 RCTs |
| Rosemary | insomnia | RCT (student sleep quality) |
| Rosemary | oral health | RCT (toothpaste: gum bleeding, plaque) |

Also added:
- White willow: osteoarthritis RCT (moderate benefit), plus a second OA/RA RCT as no-effect. A low back pain RCT that matched rofecoxib.
- Sage: a hot-flash meta-analysis and a pharyngitis spray RCT.
- Rosemary: COPD cognition RCT and an episiotomy-healing RCT.
- Elder: the air-traveller cold RCT, and as no-effect, the Macknin 2020 flu RCT and the Wieland 2021 SR.
- Soapwort: detox re-sourced to Grieve ("alterative"). The old note described skin cleansing, not detox.

## Other fixes

- 19 study_type retags (mostly reviews tagged as RCTs, and a pregnancy cohort tagged as an RCT).
- Schisandra: an antioxidant review was cited on five symptoms it never names; removed.
- Chia: the `digestive` action lost its only source (a blood-sugar RCT) and is now needs-review.

## Gaps (not added)

- **Sorrel:** Chevallier could not be checked. A periodontal mouth-rinse RCT found no benefit (not wired as a pair).
- **Soapwort:** Drugs.com refused automated access. Cough and bronchitis stay traditional-only ("no scientific studies", per MedicineNet).
- **Sage:** a palliative mouth-rinse RCT found no difference vs saline. There is no mouth-ulcer pair to record it on.
- **Schisandra:** muscle-strength RCTs measure strength, not soreness, so they were not used.

Validate 0 errors; refs 3528/3528.
