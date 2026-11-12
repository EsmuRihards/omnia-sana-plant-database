# Deep re-sweep - batch 9 (2026-11-12)

Plants 81-90: hops, goldenseal, St John's wort, hyssop, chaga, elecampane, juniper, field
scabious, wild lettuce, white dead nettle. 73 pairs before, 84 after.

Method as in `deep01.md`. Result:
- 81 changes.
- 15 refs added (REF-3594..3608); 1 deleted.
- Log: `d09_changes.tsv`. Fixer: `fix_deep09.py`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| St John's wort / depression | The two large US null trials (JAMA 2001, 2002) were missing | Recorded as no-effect. Note now says so |
| St John's wort / insomnia | Inferred from the "sedative" action, whose refs are all antidepressant studies. A sleep study showed only longer REM latency | Dropped (off-target) |
| St John's wort | The Cochrane depression review was filed under five unrelated actions (antiviral, emollient...) | Removed from those |
| Hyssop / expectorant | Rested on an immune-cell study and an asthmatic-mouse study; neither tests expectoration | Replaced with Grieve (expectorant, chronic catarrh, lung complaints) |
| Field scabious | Its only study is of Turkish *Scabiosa* species, not *Knautia* | Deleted |
| White dead nettle | A tracheal muscle-relaxation study was filed as expectorant; a chemistry paper as antioxidant | Moved out. The study that states the traditional mucolytic use now supports expectorant |

## Added under the owner rule

| Plant | New pair | Source |
|---|---|---|
| Hops | anxiety, depression, stress | RCT (stress also EU monograph) |
| Hops | menopause, hot flashes | Two RCTs |
| St John's wort | menopause | MA + 2 RCTs |
| St John's wort | hot flashes | RCT (pilot RCT on frequency: no-effect) |
| St John's wort | PMS | RCT |
| St John's wort | eczema | RCT (cream vs base) |
| St John's wort | psoriasis | Small single-blind RCT |
| St John's wort | arthritis | Knee OA RCT |
| Juniper | menstrual cramps | RCT |

Also added:
- Hops: a UV-erythema RCT (cream as good as hydrocortisone), retagged rct, for skin irritation and inflammation.
- St John's wort: episiotomy and caesarean wound RCTs; a pressure-injury RCT as no-effect.
- Juniper: functional dyspepsia RCT.
- Elecampane: a study stating traditional respiratory use, for respiratory support.
- Wild lettuce: an 1815 whooping-cough report.

## Web sources checked

- Herbal Reality wild lettuce and white dead nettle pages: both list references. Notes now
  match what each names.
- RxList wild lettuce: lists cough, insomnia, restlessness and joint pain. It rates the evidence
  insufficient. Its references are five reference books.
- The Grieve elecampane URL returned 404. Bronchitis and cough stay inferred.

## Gaps (not added)

- **White dead nettle:** heavy menstrual bleeding (traditional only).
- **Hyssop:** asthma and bruises (Grieve only).
- **Chaga:** a DOI that does not resolve (preclinical action ref).

Validate 0 errors; refs 3385/3385.
