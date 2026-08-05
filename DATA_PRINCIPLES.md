<!-- structure-fingerprint: e75f00f7d2ed -->
<!-- doc-version: 1.1  ·  last-updated: 2026-08-05 -->

# Omnia Sana — Data Principles (canonical, model-agnostic)

**This file is the single source of truth for _how_ the Omnia Sana plant database is
edited and kept trustworthy.** It is written for **any** editor — Claude, ChatGPT,
Gemini, a future model nobody has shipped yet, or a human. `CLAUDE.md`, `AGENTS.md`,
`README.md`, and every `.claude/skills/*` defer to this document. When any of them
disagrees with this file on a _principle_, this file wins; when this file disagrees
with the actual `schema/*.json` or `scripts/*.py` on a _mechanical fact_, the code
wins — and this file is the bug (see §9).

> The site this feeds is a place people consult about **what to put in their bodies.**
> A wrong fact here is wrong everywhere it renders. That single sentence is the reason
> for every rule below. Read it again before any edit.

---

## 0. How to load this document (do this first, every session)

Instructions only work if the editing model actually reads them. This doc is inert if
it isn't loaded, so **the first action of any session that touches this repo is to read
this file.** How that happens per tool:

| Editor | How it gets loaded |
| --- | --- |
| **Claude Code** | `CLAUDE.md` points here and is auto-loaded. Still open this file explicitly before data work. |
| **Codex / Cursor / Aider / Cline / Windsurf / Gemini-CLI** | They auto-read **`AGENTS.md`** at the repo root, which points here. |
| **ChatGPT / Claude web / any chat with no repo access** | Paste this file into the conversation (or the Project's custom instructions) **before** editing anything. |
| **Human** | You're reading it. |

If you are an AI model and you were not given this file, **stop and ask for it** before
writing to `plants/`, `compounds/`, `practice/`, `bibliography.bibtex`, or `schema/`.

---

## 1. The prime directive and the invariants

**Truthful or absent.** Never write a claim the cited source does not state — not a
stronger verb, not a rounder number, not an extrapolation from a related species. If
the source doesn't support it, the field stays empty. *An empty field is a correct
database; a plausible-sounding one is a broken database that looks fine.*

The five invariants (full rationale in `README.md`; they are canonical **here**):

1. **Truthful or absent.** Above.
2. **A source must fit the _specific_ claim.** Not "relevant to the plant" — *this
   reference states this fact about this species.* Wrong-species citations are the
   **single most common failure**: genus-level literature searches return congeners
   constantly. Confirm the binomial in the abstract before citing.
3. **Documented dead ends are successes.** Searching hard and finding nothing is a real
   result — record it in `internal_notes`. Never pad a gap with a weak or wrong-species
   source to make a number look better.
4. **Decide for the schema you will have, not the one you have.** Additive changes only;
   every new field needs the §6 checklist. Renderers stay field-agnostic so a data
   addition never forces a front-end change.
5. **Never commit what you have not validated.** `python scripts/validate.py` must exit
   0. It is the last gate before data reaches the public site.

---

## 2. The one distinction that organizes everything

Not all edits carry the same risk. **Sort every edit into one of two lanes** and apply
the matching ceremony. This is the resolution of "simple vs. future-proof": keep the
_schema_ simple and let cheap edits flow; concentrate all the rigor on _claims_.

### Cheap edits — low ceremony (any model, freely)
Additive, reversible, non-claim-bearing. **Adding a field, a new vocabulary id, a new
entity type, a new build feed, a monograph prose block, fixing a typo, refactoring a
renderer.** Requirements: pass the §6 checklist (for new structure) and `validate.py`.
Do not agonize — these are safe by construction because renderers are field-agnostic and
changes are additive.

### Expensive edits — high ceremony (this is where trust is won or lost)
**Any claim about a plant**: an `indication`, `action`, `contraindication`,
`drug_class_interaction`, `dangerous_lookalike`, `dosage`, `preparation`, a `study_type`
tag, or a practice `finding`. Requirements:

- **Per-claim provenance.** The claim cites `reference_ids`, and the cited source
  *actually states this fact about this exact species* (invariant 2). Confirm the
  binomial in the title/abstract.
- **Second-model verification (use your multi-provider setup).** Because a model that
  misreads a source cannot detect its own error, a claim-bearing edit made by one model
  should be re-derived from the raw source by a **different** model before it is treated
  as verified. Disagreement between providers is *signal*, not noise — it is the cheapest
  real safeguard you have. Until re-verified, mark the claim `needs-review` /`draft`.
- **Safety claims** (`drug_class_interactions`, `pairings`, `dangerous_lookalikes`) use
  the `draft → approved` lifecycle and require human medical sign-off. Public tools serve
  `approved` only. A model **never** promotes a safety claim to `approved` on its own.

> Why this line matters more than schema flexibility: `validate.py` proves a claim is
> *well-formed*, never that it is *true*. A wrong-species citation is perfectly valid
> YAML with a resolving ref id — the gate will pass it, and every downstream model then
> treats it as ground truth for its next ten edits. The lane you put an edit in decides
> how hard you look before that happens.

---

## 3. How the system is structured (the map)

One version-controlled database compiles to JSON feeds that a WordPress site consumes.
**Nothing on the public site is authored downstream** — every public fact traces to a
record here.

```
plants/ compounds/ practice/ names/     ← canonical YAML (the human/AI editing unit)
bibliography.bibtex                      ← every scientific source, one entry each
vocabularies/*.yaml                      ← controlled ids (actions, conditions, …)
        │
        ▼  scripts/validate.py  (hard gate: refs+ids resolve, records well-formed)
        ▼  scripts/build.py     (computes scores, applies publish gates)
        ▼
build/*.json  (9 feeds + manifest)       ← citations, symptoms, plants, vocab, names,
        │                                   interactions, pairings, lookalikes, practice
        ▼
omniasana.bio  (WordPress: os-*.php)     ← Knowledge Finder, Symptom→Plant, monograph,
                                            comparison, tincture calc, herb-drug &
                                            herb-herb safety, lookalikes, name dictionary
```

**The full, current, interactive map lives in [`docs/schema.html`](docs/schema.html)**
(open in a browser — pipeline view, entity view, and evidence-scoring view) with the
entity layer also as SQL in [`docs/omnia-sana.chartdb.sql`](docs/omnia-sana.chartdb.sql).
When you need to know exactly what feeds which tool, read those — do not guess.

Entity relationships (by `id`): a `plant` references `compounds`, `actions`,
`conditions`, `drug_classes`, `dangerous_plants`, other `plants` (pairings), and
`references`; a `practice` record references a `compound`, `solvent`/`method` vocab, and
`references`; a `names` record references a `plant` and a `language`. The `Plant Sighting
Map` is the one tool that does **not** read a build feed — it writes its own WordPress
table.

---

## 4. Evidence & grading invariants (survive any redesign)

The evidence score is **about to be redesigned.** These invariants constrain *any* new
design — honor them and the redesign is safe; break one and it isn't:

1. **Computed, never hand-set.** A score is derived deterministically at build time from
   structured inputs (today: the `study_type` of each cited reference). Same data → same
   number, always. The lone exception, `evidence_override`, is used by **0** records —
   that is the de-facto policy; fix the references instead.
2. **Auditable from its inputs.** Every score must be reconstructable from the claim's
   own `reference_ids`. A score pinned to a whole bibliography instead of the specific
   claim is meaningless — tighten sourcing claim-by-claim.
3. **Weak evidence and volume never raise the floor.** Ten in-vitro studies are still
   preclinical; traditional-only stays lowest. Volume of *human* evidence may add a
   bounded bonus — nothing else does.
4. **The score is only as trustworthy as its input tags.** `study_type` is *hand/AI
   assigned* and `validate.py` does **not** check it. The redesign's real job is auditing
   those inputs, not just re-shaping the formula — a prettier number on unaudited tags
   reproduces the [SSR-twin inflation](../) that once hit 54% of live labels. **Any
   grading redesign must ship a tag-audit, not only a new formula.**
5. **Don't cross the two ladders.** The clinical 1–10 score ("does it work in a body?")
   and the practice bands ("does this extraction reproduce on a bench?") **invert** and
   must never share a scale or a renderer. The practice feed deliberately never emits a
   key named `evidence`.

A precise "8/10" shown to a consumer implies more rigor than AI-assigned tags carry —
treat the number as a claim that itself must be earned (see §10).

---

## 5. Future-proofing: simple *and* extensible

The database must stay **as simple as possible** and absorb data nobody has designed yet.
Both at once, via one rule: **extend by adding, never by rewriting; keep renderers
field-agnostic.** Before adding structure, find your case:

| You are adding… | Do this | Ceremony |
| --- | --- | --- |
| A new **value** in an existing field (a new action id, a new plant) | Just add it; cite it. | Cheap |
| A new **field** on an existing entity | §6 checklist. Renderer must ignore it when absent. | Cheap-ish |
| A new **entity type** (a new top-level dir + `schema/*.json`) | §6 checklist + a `validate.py` loader + at least one consumer. Prefer reusing an existing entity first. | Deliberate |
| A new **build feed** (`build/*.json`) | Add to `build.py`, register in `manifest.json`, name one tool that reads it. | Deliberate |
| A new **tool/page** | Reads existing feeds; needs no schema change if the data already exists. | Cheap |

**Do NOT over-engineer** (these are the tempting-but-wrong moves): a generic
entity-attribute-value "flexible" schema, speculative fields "for later," or a bespoke
process for a change the §6 checklist already covers. Additive fields are cheap and
reversible — you do not need to predict the future, only to avoid painting it into a
corner. Simplicity *is* the future-proofing.

### §6 — the new-structure checklist (invariant 4, operationalized)
A new field or entity ships only when **all** are true:

1. A `schema/*.json` entry defines it (the documentation contract).
2. `scripts/validate.py` has a rule for it (the enforced contract — schema files are
   *not* auto-loaded; the imperative check in `validate.py` is what actually runs).
3. `scripts/build.py` handles it (or deliberately ignores it).
4. At least one downstream consumer uses it (else it's dead weight).
5. Its behavior when **absent** on the other ~187 records is defined (renderers must not
   break on a field that isn't there).
6. This document is updated if the change is structural (see §9), and the fingerprint bumped.

---

## 6. What the machine checks vs. what only judgment checks

Be honest about the boundary — over-trusting the gate is how bad data ships green.

**`validate.py` (the hard gate) checks:** every cited `REF-XXXX` resolves to a bibliography
entry; every vocab/compound id resolves; required fields, slug format, id uniqueness,
status enums, date/range formats; the full practice-corpus contract; and (warning-only)
that this doc is in sync (§9). **Exit 0 required to commit.**

**`validate.py` does NOT check** — and no current script does — the three things that
actually determine trust:
- whether the cited source is the **right species**;
- whether the source **actually states the claim**;
- whether a `study_type` tag is **correct**.

Those are **judgment**, and they are the whole job (§2, high-ceremony lane). One guard now
moves the frontier outward, and more should follow:
- **Species-diff audit (BUILT): `python scripts/audit_species.py`.** For every
  claim-bearing citation it reads the reference's title+abstract and flags the wrong-species
  smoking gun — a same-genus *congener* named while the record's own species is absent
  (invariant 2's failure mode). Precision-first and **non-blocking** (a flag is a prompt to
  check the source, not a verdict); `--strict` makes a flag exit nonzero for CI. Run it after
  any sourcing batch and clear the congener flags. It is a heuristic, not a truth-checker —
  it cannot confirm a source *supports* a claim, only that it is plausibly the right species.
- **Edit provenance (see §7).**

---

## 7. Provenance — stamp every edit with the model that made it

When trust erodes months from now, you need `git blame` to name the culprit, not memory.
**Every commit records which model/provider made it**, as a trailer line in the commit
message:

```
data: add three RCT sources to Achillea anti-inflammatory indication

Model: openai/gpt-5.1            ← provider/model that authored the change
Verified-by: anthropic/claude-…  ← the DIFFERENT model that re-derived the claim (§2), if any
```

Humans use `Model: human`. This costs one line and is the only thing that makes
multi-model drift debuggable.

---

## 8. The self-update rule (this document maintains itself)

**When the internal structure changes, this document changes in the same edit — but only
for _meaningful, structural_ changes.**

**Update this doc when:** a schema field or entity type is added/removed/redefined; a new
`build/*.json` feed appears; the evidence-scoring model changes; a new tool consumes a new
feed; or a core principle/process changes.

**Do NOT update this doc for:** adding a plant, a reference, or a vocabulary value; routine
sourcing; a wording tweak in an unrelated file. Data growth is not a structural change —
churning this doc on every data edit is its own failure mode.

**How the rule is enforced across models (not just trusted):** `validate.py` computes a
`structure_fingerprint()` over the schema/entity/vocab surface and compares it to the
`<!-- structure-fingerprint: … -->` line at the top of this file. If the structure moved
and this doc wasn't reconciled, **every** editor — Claude, ChatGPT, CI — sees a loud
`doc-sync ⚠` warning on the next validate run. To reconcile after a structural change:

1. Update the relevant section(s) above.
2. Add a line to the changelog (§11).
3. Run `python scripts/validate.py --fingerprint` and paste the value into the
   fingerprint line at the very top of this file.
4. Bump `doc-version` and `last-updated`.

> Scope note: the fingerprint watches `schema/*.json`, the entity directories, and the
> vocabulary file set — a clean "shape changed" signal. It intentionally does **not**
> watch `build.py` line-by-line (scoring/refactors are too noisy); keeping the doc honest
> about scoring and tools relies on this rule, not the hash. That is a deliberate
> simple-over-complete choice.

---

## 9. Honest limits (the things tooling will not save you from)

Name these plainly so no one mistakes green checks for safety:

- **No tool replaces reading the source.** Every guard here still assumes a human or model
  actually opened the paper. The fastest way to destroy this database is to rubber-stamp
  AI-authored claims at volume. More editors raises that temptation, not lowers it.
  Throughput is in permanent tension with truth; when they conflict, truth wins or the
  site's whole premise is gone.
- **The real adversary is growth pressure, not model disobedience.** SEO/indexing,
  "more indications," "more products," "higher scores" — the incentives that grow a site
  are exactly the ones that corrupt a health database. "Truthful or absent" is a cap on
  content, on purpose. Expect the pressure; keep the cap.
- **A precise score implies rigor it may not have.** The 1–10 is only as good as its
  unaudited input tags (§4). Until a tag-audit exists, treat every displayed score as a
  claim that can be wrong, and prefer under-claiming.

---

## 10. Changelog

- **v1.1 — 2026-08-05.** Built the §6 species-diff audit (`scripts/audit_species.py`) —
  the wrong-species guard moved from planned to shipped (non-blocking, precision-first).
  No structural change, so the fingerprint is unchanged.
- **v1 — 2026-08-05.** Created. Establishes the model-agnostic principles, the
  cheap/expensive edit lanes, the structure map, the grading invariants, the
  future-proofing checklist, provenance stamping, and the `validate.py` doc-sync guard
  (`structure_fingerprint()` + this file's fingerprint line). Distilled from a council +
  pre-mortem review; supersedes nothing but is now canonical for principles.
