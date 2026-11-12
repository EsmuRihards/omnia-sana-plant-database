# Deep re-sweep - batch 8 (2026-11-12)

Plants 71-80: water avens, ginkgo, licorice, gymnema, witch hazel, devil's claw, ivy, lion's
mane, hibiscus, sea buckthorn. 67 pairs before, 73 after.

Method as in `deep01.md`. Result:
- 132 changes.
- 31 refs added (REF-3563..3593); 4 deleted.
- Log: `d08_changes.tsv`. Fixer: `fix_deep08.py`.

## Ginkgo name fix (owner decision)

The primary common name was misspelt "Ginko", so every URL used `/ginko/`. It is now "Ginkgo"
(`/plants/ginkgo/`). A new optional plant field, `former_slugs`, records the retired slug. The
site module `os-slug-redirects.php` 301s any plant route that still carries it: plant page,
symptom sources, lookalikes, name dictionary, tincture and compare. A future rename only needs a
`former_slugs` line. `validate.py` blocks a former slug that is any plant's live slug or id.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Ginkgo / cardiovascular support | Only support was the WHO monograph (claudication). The Cochrane review found no clinically significant benefit | Recorded as no-effect. Note says so |
| Ginkgo / cognition, memory | The 2026 Cochrane review was missing: small-moderate benefit in dementia, probably none in MCI | Added. Notes give both halves |
| Sea buckthorn / cold | Inferred from immune action, but an RCT found the berries did not prevent colds | Dropped |
| Ivy / muscle spasm | Inferred from airway and gut smooth-muscle studies. One of them showed the extract contracted stomach muscle | Pair dropped; study removed from the antispasmodic action |
| Hibiscus / blood pressure | The 2021 Cochrane review (evidence vs placebo insufficient, very low certainty) was missing | Recorded as no-effect. Note says so |
| Lion's mane, sea buckthorn | Three references with no identifier, not on PubMed or Crossref | Deleted |

## Added under the owner rule

| Plant | New pair | Source |
|---|---|---|
| Ginkgo | anxiety | RCT (EGb 761) + network MA |
| Ginkgo | depression | MA of 21 trials |
| Licorice | sore throat | MA + RCT (postoperative sore throat) |
| Licorice | oral health | SR (mouth ulcers) |
| Licorice | wounds | RCT (second-degree burns) |
| Sea buckthorn | high cholesterol | MA of 15 trials (a healthy-adult RCT recorded as no-effect) |
| Sea buckthorn | constipation | RCT |
| Sea buckthorn | menopause | RCT (vaginal atrophy) |

Also added:
- Ginkgo: inflammatory-marker MA.
- Licorice: GutGard RCTs for reflux and indigestion.
- Witch hazel: a UV-erythema RCT that beat its vehicle; the 2013 one that did not is no-effect.
- Devil's claw: the 2014 Cochrane low-back-pain review; an OA trial vs diacerhein.
- Ivy: a review of asthma RCTs; an add-on trial with null main outcomes is no-effect.
- Lion's mane: an RCT and SR for cognition. The RCT's memory tests were null, so it is no-effect for memory.
- Hibiscus: overview of reviews and two MAs. A lipid MA and an obesity MA are no-effect.
- Sea buckthorn: a burn RCT, and three trials recorded as no-effect.

## Owner decision (not added)

- **Licorice / liver support.** Two NAFLD RCTs lowered liver enzymes. But the record's own
  contraindication lists liver disease, so it was not added.

## Gaps and negative findings (not added)

- **Lion's mane.** Stress: only a trend (p=0.051). Depression and anxiety: the RCT shows a
  within-group change only, and the SR's mood claim rests on animal data.
- **Licorice eczema.** The gel trial compares 2% with 1% only, not with base gel.
- **Ginkgo cholesterol.** One MA vs Western medicine only. A diabetes MA found no lipid or glucose effect.
- **Sea buckthorn.** Psoriasis trial was single-blind with randomisation not stated. Bloating was
  only a secondary outcome.

Validate 0 errors; refs 3371/3371. Structure fingerprint reconciled (`former_slugs`).
