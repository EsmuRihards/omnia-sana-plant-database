# Fomitopsis betulina (birch polypore) - added 2026-11-16

Record: `plants/fomitopsis_betulina.yaml` (public slug `birch-polypore`). Names: `names/fomitopsis-betulina.yaml`
(30 verified names, 21 languages, from `scripts/verify_names.py`). References REF-3881..REF-3946 (66 entries,
map in `ref_map.tsv`). Built by `add_fomitopsis.py` from the PubMed cache
(`docs/audits/2026-11-10-symptom-audit/deep/abstracts.json`) and `nonpubmed_sources.json` (Crossref + OpenAlex).

## What was searched

| Seam | Result |
| --- | --- |
| PubMed, all name variants | 83 records, all abstracts read |
| Europe PMC (full text, patents, preprints, Agricola) | 302 records; no human study |
| OpenAlex title/abstract + Chinese, Russian, Polish, German names | 400 records; non-English searches gave no relevant hits |
| ClinicalTrials.gov | no trial of this species (the two Fomitopsis RCTs used F. officinalis + Trametes versicolor) |
| Full text (PMC / Europe PMC) | about 30 papers |
| Web (identification, harvest stage, lookalikes) | 7 pages, 5 cited |

Not searched: CNKI, eLibrary.ru, WHO ICTRP, EU CTR, Google Scholar.

## Decisions

- **No symptom pairs.** Owner decision 2026-11-16: a symptom pair needs human evidence (a human trial or a
  review of human studies), one rule for all plants. Birch polypore has no human study, so it has no
  `indications[]`; its lab findings are recorded as `actions[]`. The only review-grade source is a PRISMA
  systematic review of five cell-culture studies (REF-3882).
- **Lookalikes:** `none-known`, owner-authorized 2026-11-16 (First Nature, Foraging Course Company, Wild Food UK,
  Practical Self Reliance).
- **Harvest readiness:** fruiting body, gather young (verified: Serbian field survey + independent web source).
- **Dosage:** only a Serbian folk record from one informant; labelled as a folk practice, not a tested dose.
  No regulatory monograph exists, so no tincture practice record.
- **Not used:** Li 2024's anti-malarial claim (abstract only, no data in the body); wound healing (conflicting
  single in vitro results); antihypertensive (in vitro ACE inhibition but no blood-pressure change in rats).
- **Unread, not cited (paywalled):** Papp et al. 2017 (Transylvania), Peintner et al. 1998 (Iceman's fungi),
  Han et al. 2016 (Fungal Diversity), Capasso 1998 (Lancet letter).

Model: anthropic/claude-opus-5-5
