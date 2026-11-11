# Symptom-tool audit - batch 6 of 19 (2026-11-11) - FIXED

Plants 51-60: daucus-carota, dioscorea-villosa, echinacea-purpurea, elettaria-cardamomum,
eleutherococcus-senticosus, elymus-repens, epilobium-parviflorum, equisetum-arvense,
equisetum-pratense, equisetum-sylvaticum (no indications). 68 pairs, 34 direct sources.

Owner decisions this batch (now DATA_PRINCIPLES invariant 11):
- A **superseded review version is not cited**; the current version is, as written.
- **Landmark trials missing from the DB may be added**, positive or null.

Result: 87 changes; site-wide pairs 1,445 -> 1,433; 2 refs deleted, 2 added. Log: `batch06_changes.tsv`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Wild yam / menopause (5) | The only source, RCT REF-0614, found no difference from placebo ("little effect on menopausal symptoms") | Moved to null_result_ids; pair dropped |
| Echinacea / cold | Cochrane 2006 (REF-0153) was superseded by the 2014 update (REF-0797, already in the DB): products "have not here been shown to provide benefits for treating colds" | 2006 deleted. 2014 recorded as no-effect. Jawad 2012 RCT (REF-3392, 755 people, fewer colds vs placebo) added. Score 1 -> 5 |
| Echinacea / 4 pairs | REF-0271 is a **phantom**: its title, volume and pages match no paper by these authors in PubMed, Crossref or OpenAlex | Purged |
| Siberian ginseng / fatigue, stress | The strongest negative RCT, Schaffler 2013 (adding E. senticosus to stress training: "negligible"), was missing | Added as REF-3393; recorded as no-effect |
| Horsetail / swelling, UTI (5) | A diuretic RCT in healthy men and the EU "urinary flushing" monograph were cited for swelling and UTI | Removed (birch precedent); both pairs dropped |
| Willowherb / prostate | Its review REF-0618 says BPH studies are "not conclusive or too preliminary" | Moved to null_result_ids. EU monograph (names E. parviflorum, BPH urinary symptoms) added |

## Medium

- **Unverifiable, removed from all pairs (kept in the record):**
  - Cardamom: Korikanthimath 2002 (an agronomy book chapter) and Bhilave 2013 (no journal). Neither can be found in PubMed, Crossref or OpenAlex. 9 and 2 pairs.
  - Horsetail: Sandhu 2010 (Asian J Pharm Clin Res). No abstract or text is retrievable. 10 pairs; bruising and infection dropped.
- **Siberian ginseng.** Full texts read: no review names colds or muscle soreness. REF-2295 names
  cold prophylaxis ("promising"), fatigue, stress and cognition, so it was added to those pairs.
  Muscle soreness was dropped; its only cards were a null endurance review and an adipocyte study.
- **Couch grass.** The EU and ESCOP monographs name urinary flushing and irritable bladder only.
  They were removed from swelling and UTI. REF-2563, a null rat urolithiasis study, was recorded.
- **Wild yam.** The rodent pain/inflammation study was removed from back pain, headache and skin.
- **Cardamom.** The rat ulcer study was cited for bloating and indigestion, and the hypertension
  trial for inflammation; both were removed. The critical review REF-1668 (names asthma, gum
  infections, cardiac disorders) was added.
- **Wild carrot.** Its review was cited for swelling and indigestion, which it never names.
- **Retags:** 12 refs, e.g. two reviews tagged traditional and the 2005 endurance review tagged clinical.
- **Metadata:** horsetail RCT REF-0041 year 2016 -> 2014, journal added; PubMed ids on 5 refs.

## For your spot-check (bot-blocked, kept per your batch-5 decision)

- **WHO vol. 1, Herba Echinaceae Purpureae** (REF-0308). Kept for cold, infection, immune
  support, wounds and skin irritation; removed from arthritis and inflammation.
- **EU monographs (EMA returns 429):** horsetail REF-0083 (urinary support, minor wounds); couch
  grass REF-0437 (urinary support); willowherb REF-3075 (prostate and urinary support).

Validate 0 errors; refs 3211/3211.
