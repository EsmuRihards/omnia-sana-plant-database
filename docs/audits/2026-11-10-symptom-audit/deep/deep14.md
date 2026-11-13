# Deep audit - batch 14 (2026-11-13)

Plants 131-140: wild cherry, psilocybin mushroom, lungwort, Japanese knotweed, rhodiola,
Labrador tea, blackcurrant, dog rose, Japanese rose, blackberry. 82 pairs before, 75 after.

Batches 14-19 never had the second-pass audit, so this pass does both:
- the strict "does each direct source name the symptom" check (new `!NAME` dossier screen);
- the deep checks from `deep01.md`.

Result:
- 133 changes.
- 10 refs added (REF-3725..3734); 3 deleted.
- Log: `d14_changes.tsv`. Fixer: `fix_deep14.py`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Rhodiola | Two general reviews were cited on up to 11 symptoms they never name (arthritis, colds, skin...) | Removed from those. Cold and immune support dropped (nothing else named them) |
| Blackcurrant | One review (tagged as an RCT) was on 11 symptoms, 7 never named | Removed. Swelling, urinary support and UTI dropped |
| Labrador tea | Grieve was cited, but its entry is a different species (*Ledum latifolium*). For marsh tea it gives no medicinal use, only "narcotic", used in beer | Removed. Urinary support and UTI dropped |
| Japanese rose | Grieve was cited, but it mentions *R. rugosa* only as a parent of garden hybrids | Removed |
| Wild cherry / sore throat, cramps, muscle spasm | Neither web source names them; airway antispasmodic is off-target | Dropped. Grieve's wild cherry entry added for cough and bronchitis |
| Lungwort / skin | An in vitro COX-2 study was filed as demulcent, expectorant and skin evidence | Removed; skin dropped. Grieve's "Lungwort" is a lichen, so not used |
| Knotweed | "WHO Monographs" 2007 with no volume or page. No knotweed monograph could be found | Deleted as unverifiable. A two-herb mixture study also deleted |
| Blackberry | A review naming only diarrhoea and antimicrobial use was on sore throat, mouth, skin, arthritis. A honey-mixture study was cited | Removed. Grieve's blackberry entry added (diarrhoea; mouth and throat; burns) |
| Rhodiola / fatigue | A systematic review calling the evidence "contradictory" was cited as support; a null RCT was missing | Both recorded as no-effect |

## Added under the owner rule

| Plant | New pair | Source |
|---|---|---|
| Rhodiola | depression | RCT (a sertraline/placebo RCT recorded as no-effect) |
| Rhodiola | PMS | RCT (small) |
| Rhodiola | eye strain | RCT |
| Blackcurrant | blood sugar | held crossover RCT |

Also added:
- Dog rose: a rheumatoid arthritis add-on RCT.
- Rhodiola: an SHR-5 fatigue RCT. A marathon RCT is no-effect for muscle soreness.

## Gaps (not added)

- **Wild cherry:** indigestion and appetite loss (traditional only).
- **Lungwort:** traditional respiratory use has no checkable source.
- **Blackcurrant:** the EMA leaf monograph (joint pain, urinary flushing) could not be fetched (EMA rate limit).

Validate 0 errors; refs 3500/3500.
