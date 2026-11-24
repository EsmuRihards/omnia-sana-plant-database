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
