# Symptom-tool audit - batch 9 of 19 (2026-11-12) - FIXED

Plants 81-90: humulus-lupulus, hydrastis-canadensis, hypericum-perforatum, hyssopus-officinalis,
inonotus-obliquus, inula-helenium, juniperus-communis, knautia-arvensis, lactuca-virosa,
lamium-album. 81 pairs.

Owner decision this batch (added to DATA_PRINCIPLES invariant 11): **a health-content web page
with no checkable references is not a source** (Ask-Ayurveda wiki). Referenced, practitioner-written
pages such as Herbal Reality still count for what they name.

Result: 96 changes; site-wide pairs 1,400 -> 1,381; plants in the tool 184 -> 183; 5 refs deleted.
Logs: `batch09_changes.tsv`, `batch09_followup_changes.tsv`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Field scabious / all 6 pairs | Its only source (REF-2811) tested *Knautia drymeia* and *K. macedonica*, not *K. arvensis* | Deleted. **The plant leaves the Symptom tool** |
| Goldenseal / 9 pairs (5) | REF-0455 is a critical review **tagged as an RCT**. It doesn't name arthritis, bloating, diarrhoea, indigestion or sore throat. REF-0456 is a berberine chemistry review that never names goldenseal | Retagged; removed from 5 pairs; REF-0456 deleted. Infection, inflammation, skin and wounds 5 -> 2. Arthritis, diarrhoea and sore throat dropped |
| Hops / insomnia | The only source (REF-0141) is an overview of the **valerian + hops combination** | Deleted; the EU hop monograph (aid sleep) added |
| St John's wort / 9 pairs | All rested on a Natural Standard page with a truncated title and no URL | Removed. Depression (Cochrane, meta-analyses) is untouched. 5 pairs dropped |
| Chaga / 8 pairs | REF-0272's abstract names no condition. A claim note described a Parkinson's study, but the cited paper is about memory | Removed; note corrected. Infection and wounds dropped |
| Juniper / 7 pairs | The 2010 EU monograph is superseded by the 2021 revision. BHP 1983 is not online | Merged into the 2021 version; BHP removed. Urinary flushing no longer cited for swelling or UTI |
| White deadnettle / bronchitis, respiratory | Ask-Ayurveda wiki (no references) | Deleted per your decision. Herbal Reality (catarrh) and a Planta Medica study naming chronic bronchitis replace it |

## Medium

- **Hyssop.** A genus-level Hyssopus review (7 species) was removed. The asthma-mouse study names
  no bronchitis or cough.
- **Elecampane.** The anti-staphylococcal studies name no wounds and no bronchitis.
- **Wild lettuce.** Herbal Reality, RxList and the lactucin study name pain, sleep, cough, anxiety
  and nervous tension, not headache, back pain or stress. Stress was dropped. RxList was added to
  insomnia and cough.
- **Notes:** 4 claim notes on pairs now resting only on mechanistic evidence were reset to
  "inferred from ... action".

## For your spot-check (EMA returns 429)

- Hop monograph REF-3077 (sleep); juniper monograph REF-3066 (urinary flushing, bloating, indigestion).

Validate 0 errors; refs 3199/3199.
