---
name: osdb-verify-integrity
description: "Audit the Omnia Sana database for citation-integrity failures — phantom references, orphaned bibliography entries, wrong-species citations, paraphrased abstracts, over-claimed evidence. Use after a large sourcing batch, when validate.py reports warnings, when a citation looks suspect, or when running a periodic integrity pass."
---

# Citation integrity audit

The database is the backbone of a site people consult about what to put in their
bodies. A wrong citation here is not a broken link — it is a fabricated evidence
claim, published. This audit is how that gets caught.

Read `CLAUDE.md` first.

## Start with the validator

```bash
python scripts/validate.py
```

**Errors (exit 1)** are hard failures: a cited `REF-` with no bibliography entry, an
unknown vocabulary id, a malformed record, a pairing pointing at a nonexistent
plant, a verified vernacular name failing the multi-source rule. Fix before
anything else.

**Warnings do not fail the build, and two of them matter:**

- **Orphan reference** (declared in the bibliography, never cited). Not cosmetic.
  **Orphaned entries still ship to the public Knowledge Finder feed** — they are
  visible on the site with nothing pointing to them. Removing a citation from a
  plant is only half the job; the bibliography entry has to go too.

  **PRECONDITION — check this before deleting anything.** The baseline is
  0 orphans against 3110 declared, so an orphan block that suddenly appears is
  suspicious by default. `cited` is assembled by `find_refs()` calls inside each
  entity loop in `validate.py`. If the call inside the `practice/**` loop is
  missing, every reference cited only by a practice record — extraction-chemistry
  papers and every pharmacopoeial monograph, i.e. most of that corpus — is
  reported here as an orphan. Deleting those on this instruction destroys the
  data, and the next run turns the warnings into exit-1 errors.

  Two checks, both cheap:
  1. `grep -n "cited.update" scripts/validate.py` — expect **one call per entity
     loop**, plants and practice at minimum. One call total means the accounting
     is broken; fix that first and re-run.
  2. `grep -rn "<REF-ID>" practice/` before removing any entry. A hit means it is
     cited and the orphan report is wrong.

  Only orphans that survive both checks are real.
- **`family` is 'Unknown'** — a record published without a confirmed identity.

Note that validate.py deliberately skips `internal_notes` when collecting cited
refs. Notes discuss deliberately-removed references; scanning them would resurrect
ghosts and mask a genuine missing-reference error. Don't "fix" that.

## Phantom references

A phantom is a `REF-` whose bibliography entry describes a paper that does not
exist, or does not say what the entry claims — usually a hallucinated title,
author, or DOI that resolves to nothing or to something unrelated.

The validator **cannot** catch these. It checks that a citation resolves to an
entry, not that the entry describes a real paper. Only fetching does.

To audit a batch:

1. Pull every entry added in the batch (by `REF-` range or citekey).
2. Resolve each DOI/PMID against Europe PMC or PubMed.
3. Compare the *fetched* title and authors to the entry. A near-miss title with
   different authors is a phantom, not a typo.
4. For each phantom: re-source the claim properly, or remove the claim. Then
   **delete the bibliography entry** — see the orphan rule above.

**Before declaring a phantom drop clean, check what the entry's co-citations
actually are.** A dropped reference often leaves a claim cited only by something
that cannot support it — a POWO or GBIF taxonomic record cannot support a
therapeutic claim. The claim is then unsourced even though validate.py is green.

## Wrong-species sweep

The highest-yield precision pass. For a batch, confirm the accepted binomial
appears in each source's abstract as the material studied. Congeners are the
recurring offenders — see `osdb-source-citations` for the documented near-miss
list.

Two failure shapes:

- **Wrong species** — remove the citation outright.
- **Over-claim** — right species, but the source is weaker than the claim implies
  (a cell-line result cited for a clinical indication). Demote: relabel the claim,
  correct `study_type`, or move the reference to the general `references[]` bucket.

## Abstract integrity

`abstract` in the bibliography means **the real published abstract, verbatim**. The
Knowledge Finder renders it *as* the paper's abstract, so a hand-written blurb
there is a fabricated quotation attributed to the authors.

- Fetch by exact DOI/PMID, never by title alone (title matching needs a similarity
  guard and still drifts).
- Editorial one-liners belong in `summary`, which is not surfaced that way.
- Store single-line, braces stripped, whitespace collapsed — the lightweight regex
  parsers in the builders and the live PHP port depend on it.
- Entries with no publicly available abstract simply omit the field; the button
  hides itself. An absent abstract is fine. An invented one is not.

## Evidence-score sanity

Scores are computed from each indication's own `reference_ids`. The computed value
is emitted into `build/plants.json` as **`evidence`**. The hand-set input field in
the YAML is **`evidence_override`**. There is no field called `evidence_score`
anywhere — reading for that name returns `None` and looks exactly like a broken
build; it isn't.

Two symptoms of a genuinely broken record:

- **Every indication scores the same** → the plant's whole bibliography is pinned
  to every claim. Re-wire claim-by-claim.
- **A score above 5 with no human studies cited** → check `study_type` values. The
  usual culprit is a narrative review labelled `systematic-review`, which moves the
  base from 2 to 7 in one step.

Spot-check by recomputing from the cited tiers: base from the strongest source
(review 7 / rct 5 / clinical 3 / preclinical 2 / traditional 1) plus a volume
bonus that only human sources earn.

Sanity anchors: a single RCT scores **5**; any number of in-vitro or animal
sources alone scores **2**; traditional sources alone score **1**. An animal study
that scores above 2 is a labelling bug, not a strong claim.

## Does the citation match what the note claims?

When a claim's `note` names its source — "Duke (2002) rates…", "the EMA monograph
states…", "per WHO vol. 2" — that named source must appear in the same claim's
`reference_ids`. Otherwise the record asserts what a specific authority says while
citing something else entirely.

This is not hypothetical: a bulk ingestion left **96 contraindication claims
across 95 plants** attributing content to Duke (2002) while citing unrelated
papers, with the actual Duke handbook sitting orphaned in the bibliography. Sweep
for it directly:

```bash
grep -l "Duke\|EMA monograph\|WHO monograph" plants/*.yaml
```

then confirm each hit cites the entry it names.

## Blanket-paste detection

Check **every** claim array, not just `indications` — `actions`,
`contraindications`, `constituents`, `preparations` and `dosage` all carry
`reference_ids` too. An audit that only walks `indications` will report clean on a
record whose actions are all pinned to the same bibliography.

## Null results in the wrong place

A reference reporting that the plant did *not* work must never sit in a claim's
`reference_ids` — the build reads everything there as support and scores it. Null
results belong in the top-level `references[]` bucket with the finding stated in
`internal_notes`. Grep new batches for negative-result language ("no significant
effect", "did not differ", "failed to") and confirm none of those refs are wired
to a claim.

## Dosage figures

Roughly 35 pre-existing dose figures in this database were found to be **wrong** —
not unsourced, wrong (lavender 4× high, astragalus 3× high, burdock 3× low). When
you touch a `dosage[]` entry, verify the number against the source rather than
assuming an existing figure was ever checked. The source must state a dose *for
that species*.

## Closing an audit

Record in `internal_notes` what you checked, what you removed and why. A phantom
that was removed and documented will not be re-added; a phantom silently deleted
will. Append — never reflow.

```bash
python scripts/validate.py
python scripts/build.py
```

Then `osdb-deploy`. Removals must reach the live site — an orphan left in the
bibliography stays publicly visible until it is pushed away.
