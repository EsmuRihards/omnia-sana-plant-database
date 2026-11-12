# Deep re-sweep - batch 1 (2026-11-12)

Plants 1-10: yarrow, sweet flag, black cohosh, ground elder, horse chestnut, agrimony, lady's mantle,
garlic, aloe vera, lemon verbena. 77 pairs before, 81 after.

The owner asked for batches 1-12 to be re-checked at batch-13 depth. Each pair was checked for:
- mechanistic plausibility;
- safety versus claims;
- species and plant-part confusion;
- missing landmark and null trials;
- claim-note accuracy.

Each ref was also checked for title match, retraction, dead DOIs and tag mismatches, against
PubMed and Crossref (`deep_verify.py`). Each plant was searched on PubMed for SRs, MAs and RCTs
(`deep_landmark.py`).

**New owner rule (2026-11-12).** A new pair is added only when a systematic review or RCT of the
species names the symptom and finds benefit.

**Result:**
- 98 changes.
- 23 refs added (REF-3403..3425); 3 deleted.
- Log: `d01_changes.tsv`. Fixer: `fix_deep01.py`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Black cohosh / hot flashes, menopause | The Cochrane review (2012, 16 RCTs: no difference from placebo) was missing. So were the NIH HALT trial (2006) and Geller 2009, which were also null | All three recorded as no-effect. Added the 2023 positive MA and the Osmers 2005 RCT (304 women). Notes now state the mixed result |
| Garlic / cold | Cochrane 2014 ("insufficient evidence"; only one trial) was missing | Recorded as no-effect. The single trial stays as support |
| Garlic / cancer | Two cohort meta-analyses found **no lower** cancer risk with garlic supplements (one found a possible higher colorectal risk) | Recorded as no-effect |
| Garlic / skin irritation, wounds | The record's own safety note says raw garlic causes chemical burns on skin | Both mechanistic-only pairs dropped (contradicted, inv. 11) |
| Sweet flag / cancer | Its own serious warning: beta-asarone is carcinogenic. The anticancer evidence was beta-asarone itself | Pair dropped (organ or system of its own serious warning) |
| Aloe / wounds | The Cochrane review (2012: "absence of high quality evidence") was missing | Recorded as no-effect. The burns MA (2024, positive) added |
| Aloe / skin irritation | An SR found "no evidence" that aloe prevents radiation skin reactions | Recorded as no-effect |

## Medium

- **Lemon verbena / anxiety.** The claim note cited a trial of *Aloysia polystachya*, another
  species. The sentence was removed.
- **Horse chestnut.**
  - The 2006 Cochrane review was merged into its 2012 update.
  - The arthritis source credits a five-ingredient product, so it is now a mechanistic card only.
- **Lady's mantle.** Studies of *A. caucasica* and *A. acutiloba* were purged as wrong species.
- **Yarrow / muscle spasm.** The only evidence was gut smooth-muscle antispasmodic work. That is
  off-target for muscle cramps (inv. 11), so the pair was dropped.
- **Retags:** 5 refs.
  - Black cohosh REF-2401: a structured review, not a reproducible SR.
  - Ajoene editorial.
  - Goutweed review.
  - Two lab studies tagged traditional.
- **Claim notes:** 38 rewritten. Many said "inferred from X" although the pair had direct
  sources.

## Added under the new owner rule (SR/RCT names the symptom and finds benefit)

| Plant | New pair | Source |
|---|---|---|
| Garlic | high-cholesterol, high-blood-pressure | Meta-analyses already held (Ried 2016, REF-2536), plus a 2024 MA |
| Aloe | oral-health | MAs on mouth ulcers (2022) and mucositis (2025) |
| Aloe | blood-sugar | Held MA REF-2456 ("some potential benefit") |
| Aloe | ibs | Hong 2018 MA (3 RCTs) |
| Black cohosh | insomnia | Jiang 2015 RCT |
| Agrimony | liver-support | 2018 RCT (ALT fell vs placebo) |
| Yarrow | oral-health | 2015 RCT (chemotherapy mouth sores) |

Also wired to existing pairs:
- Yarrow: the held dysmenorrhoea RCT; an episiotomy-wound RCT; an RCT on irritated skin.
- Garlic: an SR on RA/OA; glucose MAs.
- Lemon verbena: a muscle-soreness RCT.

## Checked, not changed

- The Sacred Plant Co yarrow page has a 10-item reference list, so it stays.
- These were not added:
  - Yarrow candidiasis RCT: inferior to clotrimazole.
  - Sweet flag "SR" on cognition: preclinical work only.
  - Black cohosh PCOS SR: "lack of high-quality evidence".
  - Aloe gingivitis SR and prediabetes MA: both "inconclusive".

Validate 0 errors; refs 3216/3216; mechanistic-leak check unchanged.
