# Symptom-tool audit - batch 5 of 19 (2026-11-11) - FIXED

Plants 41-50: cnicus-benedictus, coffea-arabica, cordyceps-militaris, coriandrum-sativum,
crataegus-laevigata, crataegus-monogyna, crocus-sativus, cuminum-cyminum, curcuma-longa,
cynara-scolymus. 84 pairs, 79 articles.

Owner decision: real sources that block automated reading stay on the uses their known text names,
**flagged for owner spot-check** (below).

Result: 103 changes; site-wide pairs 1,467 -> 1,445. Log: `batch05_changes.tsv`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Cumin / metabolic support (10) | Two cited sources are **null**. MA REF-0654 says the results "do not support" cumin for glycemic markers. RCT REF-0655 found no effect on MetS components | Moved to null_result_ids. Lipid-only MAs removed. Score 8 |
| Cordyceps / fatigue, muscle soreness, respiratory (5) | The only RCT tested a **6-mushroom blend** | Purged; pairs dropped |
| Coffee / cardiovascular | An EFSA caffeine **safety** opinion was cited as heart-benefit evidence | Removed |
| Turmeric / arthritis (1), skin (1) | Positive SR/MAs (REF-0791, REF-0792, REF-2165) sat only in Mechanistic basis | Moved to direct: arthritis 8, skin 7 |
| Saffron / 9 pairs | REF-0115 ("Avicenna") names antidepressant, hypnotic and anti-inflammatory uses only | Kept for insomnia and inflammation. Title, DOI and abstract fixed |

## Medium

- **Coriander.** "WHO Monographs" 1999 (vol. 1) has no coriander monograph, so it was removed.
  The Laribi review names antimicrobial, hypoglycemic and anti-inflammatory activity only; PubMed
  abstract added.
- **Midland hawthorn.** "Hedgerow Medicine" is unverifiable. The EU Crataegus monograph, which
  names *C. laevigata*, was added to cardiovascular and insomnia.
- **Blessed thistle.** The folk-uses review names no specific use; Drugs.com returns 403.
- **Coffee.** Sport-performance and Parkinson-risk papers were removed from cognition.
  MedlinePlus caffeine supports alertness only.
- **Artichoke.** The review names liver and lipid effects only, so it was removed from bloating,
  detox, IBS and indigestion (the EU monograph still covers bloating and indigestion).
- **Cumin.** The post-surgery bowel-motility RCT is not bloating or indigestion evidence.

## For your spot-check (bot-blocked, kept per your decision)

- **WHO Monographs vol. 1, "Rhizoma Curcumae Longae"** (REF-0305). Kept for dyspepsia, rheumatic
  pain/inflammation, skin diseases, ringworm and wounds.
- **NIH LactMed "Blessed Thistle"** (REF-0421). Kept for lactation.

Validate 0 errors; refs 3211/3211.
