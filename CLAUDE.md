# Omnia Sana plant database — working rules

This repo is the **backbone of omniasana.bio**. Every interactive tool, every plant
page, the Knowledge Finder, the sitemaps and the schema.org markup are generated
from the data here. Nothing on the public site is authored by hand downstream — if
a fact is wrong here, it is wrong everywhere, on a site people consult about what
to put in their bodies.

Read that sentence again before any edit. It is the reason for every rule below.

## The five invariants

**1. Truthful or absent.** Never write a claim the cited source does not state.
Not a stronger verb, not a rounder number, not an extrapolation from a related
species. If the source does not support it, the field stays empty. An empty field
is a correct database; a plausible-sounding one is a broken database that looks fine.

**2. A source must fit the specific claim.** "Relevant to the plant" is not the
bar. The bar is: *this reference states this fact about this species.* Wrong-species
citations are the single most common failure mode here — genus-level literature
searches return congeners constantly. Confirm the binomial in the abstract before
citing. See `.claude/skills/osdb-source-citations/`.

**3. Documented dead ends are successes.** Searching hard and finding nothing is a
real result. Record what you searched and why it failed, in `internal_notes`. That
stops the next session re-running the same dead search, and it is honest about
coverage. Never pad a gap with a weak or wrong-species source to make a number
look better.

**4. Decide for the schema you will have, not the one you have.** Any new field
needs: a `schema/` entry, a `scripts/validate.py` rule, `scripts/build.py`
handling, at least one downstream consumer, and a defined behaviour when the field
is *absent* on the other 186 plants. Renderers stay field-agnostic so a data
addition never requires a front-end change. Additive changes only.

**5. Never commit what you have not validated.** `python scripts/validate.py`
must exit 0. It is the last gate before data reaches the public site.

## Before you commit

```bash
python scripts/validate.py     # exit 0 required — hard gate
python scripts/build.py        # regenerate build/*.json; commit them too
```

CI (`build-and-publish.yml`) re-validates and rebuilds on push, and commits
outputs back. Commit your `build/` outputs anyway — CI skips when they already
match, which keeps the diff clean and the push single.

## Where the procedure lives

| Task | Skill |
| --- | --- |
| Add a plant, add a field, extend a record | `osdb-add-plant` |
| Find and wire references; assign `study_type` | `osdb-source-citations` |
| Audit citations, hunt phantoms and orphans | `osdb-verify-integrity` |
| Push and get it live on the website | `osdb-deploy` |

`README.md` documents the mechanics — schema fields, evidence scoring, the
`REF-XXXX` convention. The skills document the *judgment*. When they disagree
about a mechanical detail, the README and the actual schema file win; report the
drift so the skill gets fixed.

## Hard-won facts that are easy to get wrong

- `abstract` in the bibliography means **the real published abstract, only**.
  Editorial one-liners go in `summary`. The site shows `abstract` *as* the
  paper's abstract, so a paraphrase there is a fabricated quotation.
- Orphaned bibliography entries (declared, never cited) still ship to the public
  Knowledge Finder feed. Deleting a citation from a plant is not enough — remove
  the bibliography entry too, or it stays visible on the site.
- `validate.py` skips `internal_notes` when collecting cited refs, on purpose.
  Notes discuss removed refs; scanning them would resurrect ghosts.
- Never `textwrap.fill` an existing `internal_notes` — it reflows history into an
  unreadable diff.
- Evidence scores are computed, not hand-set. Pinning a plant's whole
  bibliography to every indication gives every indication the maximum score and
  makes the number meaningless. Wire references claim-by-claim.
  An `evidence_override: N` field does exist and the build honours it verbatim,
  but **0 of 187 records use one** — that is the de-facto policy. Fix the
  references before reaching for an override, and if you genuinely need one, write
  the justification into `internal_notes` in the same edit.
- `validate.py` is the only real gate, and it is narrower than it looks. It does
  **not** check the JSON schema, `study_type`, or per-claim `status`. A green run
  means references and vocabulary ids resolve and records are well-formed — not
  that the data is correct.
