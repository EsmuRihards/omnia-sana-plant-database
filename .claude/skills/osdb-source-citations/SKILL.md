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

0. **Already here?** Grep the DOI **case-insensitively**, and the title, against
   `bibliography.bibtex` before reading anything else. This is the single
   highest-yield filter — in the first real batch run it eliminated 11 of 33
   candidates, more than every other check combined. Run it first and you avoid
   deep-reading papers you already own. A duplicate is not harmless: because the
   evidence bonus counts *human sources*, two REF ids for one paper silently
   inflate a score.
1. **Species.** Is the *accepted binomial* named in the title or abstract as the
   material actually studied? Not the genus. Not a congener. Not "and related
   species". If the abstract says *Angelica sinensis* and your record is *Angelica
   archangelica*, it is not a source — it is a trap you nearly fell into.

   This step has **three** outcomes, not two: confirmed, refuted, and
   **undeterminable**. Treat undeterminable as a rejection, and log it separately
   from a refutation so it can be revisited — the paper may be perfectly good.

   > **The retrieved text may be mutilated.** PubMed/PMC strip *italicised*
   > binomials out of some publishers' abstracts (MDPI especially). You get text
   > like `six different species (,,ssp.,,, and)` or `EO showed the best apoptotic
   > effect` — every per-species result silently unattributed. This is not a
   > formatting nuisance; it removes exactly the evidence step 1 depends on. One
   > cold-start batch lost 7 otherwise-plausible candidates to it.
   >
   > When names are stripped: a `"Binomial"[Title/Abstract]` phrase search can
   > prove the species is *among* those studied, but that is **not** enough to
   > attribute a specific finding to it. Either retrieve the publisher PDF and
   > read it, or reject and record it as needing manual retrieval. Never infer
   > which species a number belongs to from position or ordering.
2. **Single herb?** If the intervention is a multi-herb product, the effect
   **cannot** be attributed to your plant. See the disqualifiers below.
3. **Claim.** Does the paper state the specific thing you are citing it for — this
   action, this condition, this dose, this constituent? A paper that mentions the
   plant while studying something else is not a source for your claim.
4. **Direction.** Does it *support* the claim, or did you skim an abstract that
   reports a null result? Read the conclusion, not the title.
5. **Identity.** Capture DOI or PMID. An entry you cannot re-find is an entry
   nobody can audit.

Only after all six: assign `study_type`, take a `REF-XXXX`, write the entry.

### Disqualifiers that look like good hits

These are real, species-correct, often well-conducted papers. They still cannot
source a claim, and they surface constantly:

- **Multi-herb combination products.** A positive RCT of a 3-herb formulation
  tells you nothing about your plant's individual contribution. Two arrived in the
  first batch (a tinnitus trial of Rosa + Urtica + Tanacetum, a gonarthritis trial
  of Rosa + Urtica + Harpagophytum) and both read as strong evidence until you
  check the intervention. A herb-plus-drug adjunct design has the same problem
  unless the trial isolates the herb arm.
- **Papers with no medicinal claim.** Animal feed and livestock performance,
  poultry/egg science, food processing and shelf-life, extraction engineering,
  irradiation studies, horticultural or breeding work. Six of nine substantive
  rejections in the first batch were this category. The plant is right; the paper
  is about agronomy or food technology, not human use.
- **Reviews that outrun their own method.** A paper titled "systematic review" in
  a low-tier journal, with a loose search description and sweeping conclusions
  ("beneficial in infertility in both men and women"), is not usable evidence.

Log every one of these in `internal_notes` — see *Dead ends are results*.

### Genus-level reviews

A review covering a whole genus is usable **only** where its attribution to your
species is structurally unambiguous — a section heading such as
`2.18. Veronica officinalis`, a species-specific table row — and then **only for
the fact stated in that section**. Structure survives the italics-stripping
described above; running prose often does not.

If the species attribution rests on prose alone, treat it as undeterminable.

Do **not** put a genus review in the `references[]` bucket as "general
background". The bucket is for sources about *this species* that back no
particular claim. A genus paper filed against one species is the
extrapolation-from-a-related-species that `CLAUDE.md` invariant 2 forbids, and it
reads to a later editor as though the species itself was reviewed.

**Wrong-species is the dominant failure mode in this repo.** Genus-level searches
on every engine return congeners constantly, and they look right. Documented
near-misses that were caught in audit — check these patterns, they recur:
*Angelica*, *Trifolium repens* vs *pratense*, *Viburnum opulus*, *Daucus carota*,
*Oxycoccus*/*Vaccinium*, *Ononis natrix*/*vaginalis* vs *arvensis*, and *Veronica*
— a large genus where *V. anagallis-aquatica*, *V. spicata*, *V. polita*,
*V. longifolia* and others all carry their own literature.

**Watch the common name, not just the binomial.** *Pseudolysimachion rotundum*
var. *subintegrum* is sold and published as "Speedwell", the English name of
*Veronica officinalis* — a different genus entirely. A common-name match is never
evidence of species identity.

## Assigning `study_type`

This is the one field the 1–10 evidence score depends on, so set it by hand.
Strongest → weakest: `systematic-review`, `rct`, `clinical` (other human — cohort,
open-label, case report), `preclinical` (in vitro / animal), `traditional` (books,
monographs, websites, ethnobotany).

build.py falls back to a keyword heuristic when the field is missing, so the build
never breaks — but the heuristic is wrong often enough that an unset value is a
silent scoring error. The heuristic's defaults: `@misc` → `traditional`, journal
articles without trial wording → `preclinical`.

**A "review" is not automatically a `systematic-review`.** This is the easiest way
to inflate a score by accident: `systematic-review` carries a base of 7,
`preclinical` a base of 2, so one careless label moves a claim five points. Check
what the paper actually did, not what PubMed's article-type field says:

- A narrative pharmacology review that reports its *own* receptor-binding and
  animal experiments is `preclinical`, whatever it calls itself.
- A mechanism review with no stated search strategy is `preclinical`.
- `systematic-review` means a described, reproducible search and synthesis —
  a real systematic review or meta-analysis.

Do not upgrade a tier to lift a score. Ten in-vitro studies are still not clinical
evidence, and the scoring rule is deliberately built so preclinical volume cannot
raise a score. Working around that is falsifying the evidence grade.

**Spot-check the `study_type` of every existing reference you touch**, not just
the ones you add. Mislabels are already in the data and each one silently moves a
live score. A cold-start batch found REF-0632 — an A549 cell-line and mast-cell
study whose own conclusion asks for animal *then* clinical trials — labelled
`rct`. That single wrong word inflated four published indications from 2 to 5.
If a claim's cited papers don't feel like its score, check the tiers before
assuming the scoring is wrong.

## Wiring the reference

Claim-level, not plant-level. Put the reference on the specific entry it supports.
Blanket-pasting a bibliography across every claim gives each one the top score and
destroys the signal the score exists to carry.

**Every one of these carries `reference_ids`** — check the whole list before
deciding a paper has no home:

| Field | Takes |
| --- | --- |
| `actions[]` | a pharmacological mechanism |
| `indications[]` | a condition the plant is used *for* (this is what gets scored) |
| `constituents[]` | a compound / phytochemical finding |
| `contraindications[]` | a safety signal, adverse event, interaction |
| `preparations[]` | how a form is made |
| `dosage[]` | an amount, for that species |
| `botanical_description` `habitat` `harvesting` `traditional_uses` | monograph prose blocks |

The monograph blocks are easy to forget because they are objects, not arrays, but
they are sourced claims like any other. An ethnobotanical record of *how a plant
was used* belongs in `traditional_uses` — provided the source really describes
use of your species, and provided you do not upgrade "drunk as a tea" into a
therapeutic indication.

General background sources — identification, distribution, an overview that backs
no particular claim — go in the top-level `references[]` bucket.

**Do not force a link.** If the literature genuinely does not demonstrate a
plant↔condition association, leave the indication unwired. A stretched citation is
worse than a gap: the gap is visible, the stretch is not.

### Where a reference goes when it doesn't fit a claim

Three cases come up constantly. All three resolve to the `references[]` bucket
plus an `internal_notes` line — never to a bent claim.

- **No vocabulary entry for what the paper tested.** A solid RCT on skin ageing or
  ADHD, where `conditions.yaml` has neither. Do **not** file skin ageing under
  `skin-irritation` or ADHD under `cognitive-function`; those are different claims
  and the mismatch would misstate what the trial did. Bucket it, and note why.
  Adding the vocabulary entry is the alternative — but do that deliberately, as
  its own decision, not as a side effect of filing a reference.
- **Null and negative results.** A well-conducted trial showing the plant did
  *not* work is valuable and belongs in the database — but it is evidence of
  absence, so it must never sit in a claim's `reference_ids`, where the build
  reads it as support and scores it. Bucket it and state the null finding in
  `internal_notes` explicitly, including **which endpoint** was null: a null for
  menstrual *bleeding volume* does not contradict a claim about menstrual
  *cramping pain*, and conflating the two is its own error.
- **A single isolated-tissue or single-model result.** One rabbit-aorta
  vasorelaxation experiment is not grounds for a cardiovascular indication.
  Bucket it until a body of evidence exists.

### The reference must actually be the source named in the note

If a claim's `note` says "Duke (2002) rates this as…" or "the EMA monograph
states…", then Duke or that monograph must be in that claim's `reference_ids`.
Citing adjacent papers that merely concern the same plant leaves the record
asserting what a named source says while pointing at something else. A bulk
ingestion once put 96 such claims into this database at once, so check the note
text against the citation whenever you touch a claim that names its source.

## Bibliography mechanics

Next free id:

```bash
grep -ho "REF-[0-9]\+" bibliography.bibtex | sort -u -V | tail -1
```

**Use `-V` (or `sort -t- -k2 -n`).** A plain `sort -u` is lexicographic: it is
correct only while every id is four digits, and will silently return the wrong
answer from `REF-10000` onward — handing you an id that is already in use. The
README carries the same command; fix it there too if it still lacks `-V`.

Entries sort alphabetically by citation key; the id lives in `note = {REF-XXXX}`.
Full format in `README.md`.

**Not every paper has a DOI.** Older and regional journals often have only a
PubMed id. Both `pmid` and `url` are established fields here, and `build.py`'s
`best_link()` resolves doi → url → title search, so an entry with no DOI should
carry **both** `pmid = {…}` and `url = {https://pubmed.ncbi.nlm.nih.gov/…/}` or it
will fall through to a Google Scholar guess on the public source card.

Be aware this is a convention, **not an enforced rule** — `validate.py` does not
check it, and older entries violate it. Apply it to what you add; don't assume
what you find already complies.

**If the retrievable abstract is mutilated, omit it.** The `abstract` field means
the real published abstract, and a copy with every species name stripped out (see
step 1) is not that — storing it publishes a corrupted quotation under the
authors' names. Leave the field out and put a plain-language note in `summary`
explaining why. An entry with no abstract is fine; the button simply hides.

Gotchas that have bitten before:

- **Before adding, grep the DOI — case-insensitively.** The same paper sits in the
  bibliography under a different DOI case more often than you would expect
  (`10.1001/JAMA...` vs `10.1001/jama...`). A duplicate entry is two REF ids for
  one paper, which corrupts the human-source *count* the evidence bonus uses.
  Note that a DOI grep alone will not catch a paper filed without one — check the
  title too.
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

**A batch target is a ceiling, not a quota.** If you were asked for ten and only
six survive verification, the answer is six, written down with the reason. A
well-covered plant will often yield fewer new references than a neglected one —
that is the database working, not the search failing. Record which candidates were
already present and which were rejected on substance, so the next session can see
the shape of the remaining gap without repeating the search.

Append to `internal_notes` — never `textwrap.fill` existing content.

## Finishing

```bash
python scripts/validate.py     # every cited REF must resolve — hard gate
python scripts/build.py        # regenerates build/*.json
```

**`build.py` is not optional if you changed data.** `build/*.json` is what the
website actually consumes, so skipping it leaves the build outputs stale relative
to the bibliography and the site serving old numbers. If you are working under an
instruction not to touch `build/`, say so explicitly in your handover — a silently
stale `build/` looks identical to a finished job.

Then `osdb-verify-integrity` if the batch was large, and `osdb-deploy` to publish.
