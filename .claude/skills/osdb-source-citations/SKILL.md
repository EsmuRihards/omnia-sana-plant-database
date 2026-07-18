---
name: osdb-source-citations
description: "Find, verify and wire scientific references into the Omnia Sana plant database. Use when sourcing a claim, running a citation campaign, harvesting from PubMed/OpenAlex/Europe PMC/EMA/WHO, adding entries to bibliography.bibtex, assigning study_type, or deciding whether a paper actually supports a claim. Carries the wrong-species traps and the record of which source seams are exhausted."
---

# Sourcing claims

The bar is not "this paper is about this plant". The bar is:

> **This reference states this fact about this species.**

Everything below exists to enforce that one sentence. Read `CLAUDE.md` first.

## The verification sequence

For every candidate reference, in order. Stop at the first failure.

1. **Species.** Is the *accepted binomial* named in the title or abstract as the
   material actually studied? Not the genus. Not a congener. Not "and related
   species". If the abstract says *Angelica sinensis* and your record is *Angelica
   archangelica*, it is not a source — it is a trap you nearly fell into.
2. **Claim.** Does the paper state the specific thing you are citing it for — this
   action, this condition, this dose, this constituent? A paper that mentions the
   plant while studying something else is not a source for your claim.
3. **Direction.** Does it *support* the claim, or did you skim an abstract that
   reports a null result? Read the conclusion, not the title.
4. **Identity.** Capture DOI or PMID. An entry you cannot re-find is an entry
   nobody can audit.

Only after all four: assign `study_type`, take a `REF-XXXX`, write the entry.

**Wrong-species is the dominant failure mode in this repo.** Genus-level searches
on every engine return congeners constantly, and they look right. Documented
near-misses that were caught in audit — check these patterns, they recur:
*Angelica*, *Trifolium repens* vs *pratense*, *Viburnum opulus*, *Daucus carota*,
*Oxycoccus*/*Vaccinium*, *Ononis natrix*/*vaginalis* vs *arvensis*.

## Assigning `study_type`

This is the one field the 1–10 evidence score depends on, so set it by hand.
Strongest → weakest: `systematic-review`, `rct`, `clinical` (other human — cohort,
open-label, case report), `preclinical` (in vitro / animal), `traditional` (books,
monographs, websites, ethnobotany).

build.py falls back to a keyword heuristic when the field is missing, so the build
never breaks — but the heuristic is wrong often enough that an unset value is a
silent scoring error. The heuristic's defaults: `@misc` → `traditional`, journal
articles without trial wording → `preclinical`.

Do not upgrade a tier to lift a score. Ten in-vitro studies are still not clinical
evidence, and the scoring rule is deliberately built so preclinical volume cannot
raise a score. Working around that is falsifying the evidence grade.

## Wiring the reference

Claim-level, not plant-level. Put the reference on the specific `actions[]` /
`indications[]` / `dosage[]` entry it supports. Blanket-pasting a bibliography
across every claim gives each one the top score and destroys the signal the score
exists to carry.

General background sources — identification, distribution, an overview that backs
no particular claim — go in the top-level `references[]` bucket.

**Do not force a link.** If the literature genuinely does not demonstrate a
plant↔condition association, leave the indication unwired. A stretched citation is
worse than a gap: the gap is visible, the stretch is not.

## Bibliography mechanics

Next free id: `grep -ho "REF-[0-9]\+" bibliography.bibtex | sort -u | tail -1`.
Entries sort alphabetically by citation key; the id lives in `note = {REF-XXXX}`.
Full format in `README.md`.

Gotchas that have bitten before:

- **Before adding, grep the DOI — case-insensitively.** The same paper sits in the
  bibliography under a different DOI case more often than you would expect
  (`10.1001/JAMA...` vs `10.1001/jama...`). A duplicate entry is two REF ids for
  one paper, which corrupts the human-source *count* the evidence bonus uses.
- **Never dedupe bibtex with a bare `re.sub` on the citation key** — it removes
  *every* match, including the one you meant to keep. Grep first, edit precisely.
- **An idempotent inserter that skips a duplicate leaves a REF gap.** That is fine
  — ids are identifiers, not a count. Don't renumber to close a gap.
- `abstract` holds the **real published abstract only**. Never a paraphrase — the
  site renders it *as* the paper's abstract. Editorial one-liners go in `summary`.

## Source seams

**PubMed / Europe PMC** — primary. Best abstract and DOI/PMID coverage.

**OpenAlex** — reaches journals PubMed does not index; genuinely finds papers
PubMed misses, especially non-English and smaller journals. Two costs: genus
search returns congeners and other species constantly (verify the active species
in the abstract, every time), and it is slow and flaky in sandbox (~40s/request,
expect retries).

**EMA herbal register** (`medicines-output-herbal_medicines-report_en.xlsx`,
header row 9) — *worked through and exhausted.* Match on synonyms as well as the
accepted name. Check `Status`/`Outcome`: "Draft under discussion" and "Public
statement" are **not** monographs and do not support a claim. The summary web
pages carry no posology — you must fetch the monograph PDF (via `pypdf`) to get a
dose.

**WHO monographs Vols 1–4** — *worked through and exhausted.* Available as
`_djvu.txt` from the Internet Archive; IRIS serves HTML, not PDF. **Never match by
binomial alone** — it yields real false positives. Anchor on WHO's Latin drug
title and read the Definition section to confirm the species and plant part.

**Commission E** — *not yet opened.* The only tier covering traditional tinctures
and infusions; blocked several dosage entries that no other seam could source.
Start here when the regulatory route is needed again.

Both regulatory seams being exhausted means remaining gaps need ESCOP, Commission E,
or per-plant trial mining — and on those, **expect dead ends to outnumber finds.**
That is the normal shape of the work now, not a failure.

## Dead ends are results

When a search fails, write down in `internal_notes` *which seams you searched* and
why each failed. That is a genuine deliverable: it stops the next session
re-running the same expensive dead search, and it is an honest statement of
coverage.

Never pad a gap to improve a number. A species with sparse literature is
**settled-incomplete with a written reason** — not a record quietly filled with
congener papers. Several species in this database are legitimately settled that
way; adding wrong-species citations to "finish" them would be the worst possible
outcome.

Append to `internal_notes` — never `textwrap.fill` existing content.

## Finishing

```bash
python scripts/validate.py     # every cited REF must resolve
python scripts/build.py
```

Then `osdb-verify-integrity` if the batch was large, and `osdb-deploy` to publish.
