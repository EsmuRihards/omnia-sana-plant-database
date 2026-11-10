# Symptom-tool audit - batch 2 of 19 (2026-11-10) - FIXED

Plants 11-20: althaea-officinalis, andrographis-paniculata, anethum-graveolens,
angelica-archangelica, arctium-lappa, arctium-minus, arctostaphylos-uva-ursi, arnica-montana,
artemisia-absinthium, artemisia-vulgaris.

Scope: 110 pairs, 104 articles, each read against its symptom. Rules: DATA_PRINCIPLES v1.4
invariants 7-9, plus two owner decisions from this batch: **homeopathic preparations are not
evidence for the plant**, and **sources that lump Arctium species describe A. lappa only**.
Result: 173 claim-level changes; 110 pairs reduced to 77; 10 refs deleted. Log: `batch02_changes.tsv`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Bearberry / UTI, infection, urinary support (6) | Both RCTs are negative: ATAFUTI REF-0701 found "no evidence of an effect", and REF-0700 had a higher symptom burden than fosfomycin | Moved to null_result_ids. ESCOP added. Score 6 -> 1 |
| Arnica / bruising, pain, swelling, inflammation (7) | REF-0399 is a **homeopathic** meta-analysis, non-significant vs placebo (p = 0.059). REF-2103 used homeopathic pellets (p = 0.097 and 0.074 reported as "significant"). REF-2098 is a homeopathy review | All 3 purged. EU-monograph review REF-0726 is now the source for bruising/inflammation/arthritis. Pain and swelling dropped |
| Andrographis / 5 pairs (5) | REF-0393 is a narrative review **tagged as an RCT** | Retagged. Kept only where it names the use |
| Lesser burdock / 10 pairs | Its only sources (Herbal Reality, Drugs.com) describe *A. lappa* | Purged (wrong species). 7 pairs dropped |
| Dill / inflammation (5) | The trial measured hs-CRP and found no change | Moved to null_result_ids |

## Medium - article does not match the symptom

- **Marshmallow.** The EU and ESCOP monographs cover cough, throat and gastric irritation only. They
  were cited for acid reflux, eczema and skin, which they don't cover. REF-1370 (rat wound healing)
  was cited for skin irritation.
- **Dill.** The WHO monograph was cited for 12 pairs. Its text supports only dyspepsia, flatulence,
  dysuria and experimental anti-inflammatory activity.
- **Angelica.** One narrative review (REF-0695) backed 18 pairs but names only 4 uses. REF-0696
  (fibromyalgia model) was cited for arthritis.
- **Greater burdock.**
  - REF-0309 is a "WHO monograph" that doesn't exist for burdock.
  - REF-0313 (Xu 2008) can't be found anywhere.
  - REF-0709 names contact dermatitis only as a *side effect*, but was cited for eczema and skin.
- **Arnica.** The review REF-0398 was cited for 11 pairs but names none of them except infection and
  inflammation.
- **Wormwood and mugwort.**
  - Hoffmann (REF-0112) is unverifiable.
  - Kung & Ko 2002 (REF-0149) can't be found.
  - Grieve supports only digestion, flatulence and antiseptic use for wormwood, and stomach,
    rheumatism and tonsil swelling for mugwort.
- **Compound papers with no species named** (arctigenin REF-2858/2860, arbutin REF-2862) were
  purged.

## Data defects found

- **Duplicates.**
  - REF-0103 duplicates REF-1391 (the same dill trial; REF-0103's DOI doesn't resolve).
  - REF-0310 duplicates REF-3094 (the same WHO monograph).
  - Both pairs were merged.
- **Systemic (not fixed): at least 115 stored abstracts are cut at a "<" sign** (e.g. "P < 0.05"),
  so whole results sections are missing. Example: REF-1391's hs-CRP result. Truncated abstracts can
  hide null results. Needs a re-fetch from PubMed.

Validate 0 errors; refs 3226/3226.
