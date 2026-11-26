# Research-deepening campaign (started 2026-11-24)

Owner request (2026-11-24): work through the plants in batches of 5, find further scientific research on each
plant (medicinal properties and everything else the interactive tools use), read the papers properly so that a
source is only wired where it really supports the claim, add them to the database and make sure they reach the
tools. "Never force information - if there is none, there isn't."

Batch N = plants sorted by id, slice `[(N-1)*5, N*5)`; 189 plants = 38 batches.

## Method (per batch)

1. `rd_profile.py N` - what each record already holds, field by field, with the study_type of every ref.
2. `rd_search.py N` - multi-seam search; every hit marked HELD / SEEN / new.
   - PubMed families: human trials incl. untagged ones (HT), SR/MA (SR), safety and interactions (SAFE),
     observational (OBS), narrative reviews (REV).
   - ClinicalTrials.gov registrations with result PMIDs.
   - OpenAlex trial-worded works with no PMID (journals PubMed does not index; this is where most Iranian and
     Indian trials are).
   - `rd_epmc.py N` reruns Europe PMC separately (it returns 503 under load): non-MEDLINE records + full text.
   - Name clauses come from `batches/names_override.json` when the binomial alone misses the literature
     (black cohosh is mostly published as *Cimicifuga racemosa*; sweet flag as Vacha).
3. Read: `../2026-11-10-symptom-audit/deep_efetch.py PMID...` (verbatim PubMed abstracts) and `rd_doi.py DOI...`
   (Crossref / OpenAlex abstract for non-PubMed papers); blocked pages via the web-fetch agent; PDFs via pypdf.
4. Judge every candidate on the osdb-source-citations sequence (held? species? single herb? claim? direction?
   identity?), the DATA_PRINCIPLES invariants and the owner rules:
   - a new symptom pair needs an SR/MA or RCT of the species that names the symptom and finds benefit (12a);
   - lab-only evidence never makes a pair (owner direction 2026-11-16: pairs need human evidence); it goes to
     actions, constituents or safety;
   - no-effect studies go to `null_result_ids` (7); superseded review versions are not cited (11);
   - a pair the plant's own safety note forbids is not added (12d); signature compounds count, labelled (10);
   - duplicate publications of one trial are cited once;
   - new herb-drug interactions are always `draft` (owner sign-off).
5. `fix_rNN.py` (fixlib ops for indications/actions/bucket + `rd_fix.py` ops for constituents, safety, dosage,
   preparations, interactions, monograph blocks), all-or-nothing; then validate, `audit_species.py`, build,
   compare scores, commit, push, sync the site, verify live.

REF ids for this campaign come from a reserved block starting at **REF-5001** (a parallel session allocates
4029+, 4201+, 4301+). Work happens in the worktree `wt/osdb-research-deepening` (branch `research-deepening`),
rebased onto `osdb/main` before each push, because another session edits the main checkout.

## Batch log

| Batch | Plants | New refs | Pairs | Report |
| --- | --- | --- | --- | --- |
| 1 | yarrow, sweet flag, black cohosh, ground elder, horse chestnut | REF-5001..5082 (82; 1 retracted ref deleted) | 1,405 -> 1,409 | `batches/r01_report.md` |
| 2 | agrimony, lady's mantle, garlic, aloe, lemon verbena | REF-5083..5131 (49) | 1,409 -> 1,415 | `batches/r02_report.md` |
| 3 | marshmallow, andrographis, dill, angelica, burdock | REF-5132..5168 (37) | 1,415 -> 1,417 | `batches/r03_report.md` |
| 4 | lesser burdock, bearberry, arnica, wormwood, mugwort (+ andrographis follow-up) | REF-5169..5186 (18) | 1,417 -> 1,420 | `batches/r04_report.md` |
| 5 | pleurisy root, astragalus, bacopa, birch, bistort | REF-5187..5204 (18) | 1,420 -> 1,422 | `batches/r05_report.md` |
| 6 | borage, boswellia, calendula, tea, peach-leaved bellflower | REF-5205..5230 (26) | 1,422 -> 1,428 | `batches/r06_report.md` |
| 7 | hemp, shepherd's purse, chili pepper, caraway, centaury | REF-5231..5249 (19) | 1,428 -> 1,434 | `batches/r07_report.md` |
| 8 | gotu kola, fireweed, greater celandine, cassia, true cinnamon | REF-5250..5269 (20) | 1,434 -> 1,439 | `batches/r08_report.md` |
| 9 | blessed thistle, coffee, cordyceps, coriander, midland hawthorn | REF-5270..5286 (17) | 1,439 -> 1,441 | `batches/r09_report.md` |
| 10 | common hawthorn, saffron, cumin, turmeric, artichoke | REF-5287..5314 (28) | 1,441 -> 1,453 | `batches/r10_report.md` |
| 11 | wild carrot, wild yam, echinacea, cardamom, eleuthero | REF-5315..5341 (27) | 1,453 -> 1,455 | `batches/r11_report.md` |
| 12 | couch grass, small-flowered willowherb, field, shady and wood horsetail | REF-5342..5345 (4) | 1,455 -> 1,455 | `batches/r12_report.md` |
| 13 | California poppy, eucalyptus, eyebright, meadowsweet, dropwort | REF-5346..5355 (10) | 1,455 -> 1,459 | `batches/r13_report.md` |
| 14 | fennel, birch polypore, white bedstraw, cleavers, lingzhi | REF-5356..5373 (18) | 1,459 -> 1,463 | `batches/r14_report.md` |
| 15 | gentian, water avens, ginkgo, licorice, gymnema | REF-5374..5390 (17) | 1,463 -> 1,467 | `batches/r15_report.md` |
| 16 | witch hazel, devil's claw, ivy leaf, lion's mane, hibiscus | REF-5391..5403 (13) | 1,467 -> 1,468 | `batches/r16_report.md` |
| 17 | sea buckthorn, hops, goldenseal, St John's wort, hyssop | REF-5404..5420 (17) | 1,468 -> 1,472 | `batches/r17_report.md` |
