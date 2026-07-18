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

Scores are computed from each indication's own `reference_ids`. Two symptoms of a
broken record:

- **Every indication scores the same** → the plant's whole bibliography is pinned
  to every claim. Re-wire claim-by-claim.
- **A score above 5 with no human studies cited** → check `study_type` values; a
  mislabelled `preclinical` as `rct` inflates the base.

Spot-check by recomputing from the cited tiers: base from the strongest source
(review 7 / rct 5 / clinical 3 / preclinical 2 / traditional 1) plus a volume
bonus that only human sources earn.

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
