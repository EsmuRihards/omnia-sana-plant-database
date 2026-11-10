# Symptom-tool audit - batch 1 of 19 (2026-11-10)

Plants 1-10 by id: achillea-millefolium, acorus-calamus, actaea-racemosa, aegopodium-podagraria,
aesculus-hippocastanum, agrimonia-eupatoria, alchemilla-vulgaris, allium-sativum, aloe-vera,
aloysia-citrodora.

Scope: 99 plant-symptom pairs, 126 unique articles (direct + Mechanistic-basis cards), each read
against the symptom it is shown under. Method: `extract_batch.py` mirrors `os-symptom-sources.php`
(direct = `reference_ids`; mech = related-action refs minus direct minus `mechanistic_exclude_ids`).

**Tool parity: OK.** Live `os-sym.js` scores == `build/symptoms.json` for all 10 plants. 5 live
sources pages checked card-for-card == DB (sweet-flag/anxiety, agrimony/arthritis,
ground-elder/headache, black-cohosh/hot-flashes, aloe-vera/wounds).

**Result: about 35 of 126 articles have at least one problem.**

## High - misleading to users

| # | Plant / symptom | Problem | Fix |
|---|---|---|---|
| H1 | Black cohosh / anxiety (8, rank 2 of 17), depression (8) | REF-0674 reports a **non-significant** effect of black cohosh on anxiety. REF-0670 covers only "psychological menopausal symptoms". There is no anxiety or depression evidence outside menopause. | Drop to menopause-context only, or set needs-review with a lower override |
| H2 | Black cohosh / hot-flashes, menopause (10) | REF-0673 is a **null RCT** ("failed to provide any evidence"). REF-0623 calls efficacy "uncertain". Both are shown as support and both raise the score. | Owner decision: label null results and keep them out of the score (needs a field) |
| H3 | Lemon verbena (9 pairs at 7), Sweet flag (all 10 at 7) | One **narrative** pharmacology review (REF-0474; REF-0516/0624) is tiered `review` (base 7) and badged "Meta-analysis / review". Result: lemon verbena is #7 of 127 for arthritis and #13 of 94 for cancer, and sweet flag is #6 of 17 for anxiety, all with **no human data**. | Retag narrative reviews (systemic, see below) |
| H4 | Sweet flag / anxiety, depression, cancer | The DB's own contraindication says beta-asarone is carcinogenic. The tool ranks it at 7 with **no safety cue**: `render()` has no warning field at all. | Add a safety flag to the tool cards |
| H5 | Aloe vera / wounds, bruising, eczema, skin-irritation | **0 direct refs** (score 1). The clinical systematic review on wounds (REF-2241) and REF-2238/2243 appear only under "Mechanistic basis". Real evidence is hidden. | Move REF-2241, 2238, 2243 to direct for wounds (and REF-2243 for eczema) |

## Medium - article does not match the symptom

| # | Plant / symptom | Ref | Problem |
|---|---|---|---|
| M1 | Agrimony / arthritis, bruising | REF-0386 | The EU monograph covers diarrhoea, mouth/throat inflammation, and minor skin inflammation/wounds only (the YAML notes agree) |
| M2 | Agrimony / arthritis, inflammation | REF-0680 | A cisplatin **neuropathic** pain model in rats, not arthritis |
| M3 | Agrimony / bruising; Yarrow / bruising | REF-0682, REF-0372 | Wound-healing studies; a wound is not a bruise |
| M4 | Garlic / wounds | REF-0651 | Allicin vapour against **lung** pathogens |
| M5 | Garlic / inflammation (7) | REF-0648 | A CVD systematic review; inflammation is not an outcome. It alone lifts an inferred pair to 7 |
| M6 | Ground elder / all 9 pairs | REF-0098, REF-0168 | One copied 2-book bucket (its YAML says "plant-level"). Grieve supports joint, gout and sciatic pain and "inflamed parts" only: **no headache, UTI, skin or back pain**. Moerman's entry for this European weed is unverified |
| M7 | Yarrow / 10 pairs incl. uti, muscle-spasm | REF-0011, REF-0098 | Same copied-bucket pattern; not verified per claim |
| M8 | Aloe vera / cancer | REF-2845, REF-2847 | Aloe-emodin sourced from **rhubarb** (Rheum), not aloe |
| M9 | Sweet flag / cancer | REF-2825, REF-2827 | Beta-asarone from *Acorus tatarinowii* (another species) |
| M10 | Yarrow / cancer | REF-2822 | Genus-level paper; its experiments use *A. coarctata* |

## Low - source quality and metadata

- **Consumer websites as sources:** REF-0373 and REF-0387 (herbalreality.com) and REF-0381 (a
  sacredplantco.com blog) back 7-9 pairs each, some of them `verified`.
- **Wrong tier:** REF-0369 is a review but tagged traditional. REF-0372 is an animal study but tagged
  traditional. REF-0647, 0678 and 0679 are clinical reviews but tagged preclinical. REF-0681 and 0683
  are reviews but tagged preclinical. REF-2589 is a review but tagged clinical.
- **Links:** REF-0011, 0098, 0113, 0168 and 0372 link to a Google Scholar *search*, not to the item.
  REF-0011 and 0372 have DOIs.

## Systemic (affects all batches)

1. `study_type: review` covers both meta-analyses and narrative reviews. Both get base 7 and the
   "Meta-analysis / review" badge. This is the biggest score inflator found so far. It is related to,
   but separate from, the deferred inferred-badge issue.
2. Null or negative trials count as support. The schema has no field for result direction.
3. The tool shows no safety cue next to ranked plants.

No data changed. Nothing committed.
