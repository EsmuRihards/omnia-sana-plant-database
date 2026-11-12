# Symptom-tool audit - batch 8 of 19 (2026-11-12) - FIXED

Plants 71-80: geum-rivale, ginkgo-biloba, glycyrrhiza-glabra, gymnema-sylvestre,
hamamelis-virginiana, harpagophytum-procumbens, hedera-helix, hericium-erinaceus,
hibiscus-sabdariffa, hippophae-rhamnoides. 77 pairs.

No new owner policy this batch; standing rules applied.

Result: 136 changes; site-wide pairs 1,411 -> 1,400; 4 refs deleted (one a duplicate). Logs:
`batch08_changes.tsv`, `batch08_followup_changes.tsv`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Ginkgo / cognitive function, memory | The GEM trial (REF-0056, 3,069 people) was cited as support. It found ginkgo "was not effective" in preventing dementia | Moved to null_result_ids. Two positive dementia meta-analyses (REF-2186, REF-2185), already in the DB as mechanistic cards, now cited directly. Score 6 -> 9 |
| Lion's mane / cognition, memory | An acute RCT (REF-0641) found no overall effect; its main source REF-0179 was **a PubMed search-results URL** | Null recorded; REF-0179 deleted. The mild-Alzheimer's pilot RCT REF-2419 now cited directly |
| Hibiscus / blood pressure, cholesterol | REF-0465 pooled hibiscus **combined with other plants**. A lipid meta-analysis (REF-1843) "does not support" a lipid effect | REF-0465 deleted; REF-1843 recorded as no-effect. Metabolic support 7 -> 1 (inferred only) |
| Devil's claw / 6 pairs | The Natural Standard SR (REF-0443) abstract names no condition. The 2006 OA review (REF-1834) "cannot provide a definitive answer" | Removed; null recorded. The OA/low-back-pain SR (REF-0561) is now also cited for arthritis. Back pain and pain 9 -> 7 |
| Ivy / cough, bronchitis | The 2021 updated SR (REF-0833): effects "minimal at best and of uncertain clinical importance" | Recorded as no-effect; the 3 trials stay |
| Licorice / 14 pairs | One source is a genus-level "Glycyrrhiza sp." review; another (REF-0089) has an abstract that names no condition | Removed. WHO vol. 1 kept on its known uses. EU monograph (dyspepsia, heartburn, cough with colds) added. Immune support, menstrual cramps, muscle spasm and wounds dropped |
| Water avens / inflammation | REF-2777 tested *Geum urbanum*, not *G. rivale* | Deleted (wrong species) |

## Medium

- **Sea buckthorn.** Its two sources for 11 pairs (Chodak 2014, Zuniga-Lopez 2021) can't be
  found. They were replaced where verified reviews name the use: a dermatology review for wounds,
  eczema, skin and inflammation; others for immunity, heart and blood sugar. Metabolic support and
  bruising dropped.
- **Witch hazel.** REF-0532 is a 2025 review that was tagged as an RCT; it was retagged, so the
  inflammation and skin scores dropped from 5 to 2. The EU monograph names skin, oral mucosa and
  haemorrhoids, so it was removed from bruises and wounds. Herbal Reality names no arthritis.
- **Ginkgo.** WHO vol. 1 kept for cognition, memory and circulation; removed from arthritis,
  inflammation and skin.
- **Gymnema.** A sugar-cravings trial measured no blood glucose.
- **Water avens.** A tannin screen named no diarrhoea and an antimicrobial assay named no sore
  throat; both were removed.
- **Duplicate:** REF-0305 and REF-0308 were both WHO vol. 1. They were merged, which also touched
  turmeric.
- **Retags:** 9 refs (e.g. an open-label ivy study tagged RCT).

## For your spot-check (bot-blocked, kept per your batch-5 decision)

- **WHO vol. 1:** Folium Ginkgo (cognition, memory, circulation); Radix Glycyrrhizae (cough,
  bronchitis, respiratory, dyspepsia, arthritis, inflammation, tuberculosis/infection).
- **EU monographs (EMA 429):** licorice REF-3081; witch hazel REF-0531.

Validate 0 errors; refs 3204/3204.
