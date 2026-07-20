# Next session — the practice corpus, full per-plant scope

Paste everything below the line into a new conversation. Everything it references
is on disk in this repo.

---

## MISSION

Build the **practice corpus** — a second, applied research corpus in
`plant-database/` that sources the tincture and formula calculators on
omniasana.bio. Those two calculators are the only public tools with no data
backing: `uploads/omniasana/js/os-formulation.js` asserts `PART_RATIOS` 0.15–0.45,
`DEFAULT_RATIO` 1:5, `GLYCERITE_MIX` 75/25 and `shelfLife()` ABV bands with **zero
provenance**, on a site whose whole proposition is that it cites things.

Scope is **full per-plant recommendation at `approved`** — the calculator says
"use 60–70% ethanol for this plant" with a citation. The owner has accepted the
cost with eyes open. Do it properly: factual, future-proof, no logical fallacies,
no mismatch or chaos in the entity model. Speed is not the constraint;
correctness is.

The design phase is finished and audited, **and the build phase has now started
and reached a working corpus.** Read the state below before planning anything —
an earlier revision of this file said the build had not started, which was true
when it was written and is no longer.

## STATE (updated 2026-07-20, after the D8 / D0 / D3 session)

Git: HEAD `dcc15f4` on `main`, working tree clean. **8 commits ahead of
`osdb/main`, NOTHING PUSHED.** `python scripts/validate.py` exits 0 — 187 plants,
**3,116** refs cited / 3,116 declared, zero orphans.

**Pushing is a visible content change now, not a docs-only push.** D8 withholds
242 preparations and 46 dosages from the public plant pages until they are
sourced. Get that green-lit deliberately.

### What is DONE

- **APPENDIX A applied** to spec sections 1-6 (14 blocking + 7 major), then
  independently audited. **APPENDIX B** in the same file records what that audit
  found — including one blocking defect that originated in Appendix A's own
  replacement text (`str(None)` is `'None'`, so every `.strip()` emptiness gate
  accepted an explicit YAML null). §0 and the appendix headers now state the
  applied status truthfully.
- **D8 landed.** Owner decision: nothing unsourced publishes, both fields.
  Implemented as `SOURCED_ONLY_KEYS` in `build.py`'s public projection, so any
  future statused list inherits it. NOTE the framing in older notes is wrong:
  extending `approved_only()` would have EMPTIED the editorial lists, because
  they use verified/needs-review/draft and never carry the value `approved`.
- **D0 landed and executed.** schema/practice.schema.json, three vocabularies
  (solvents 18, methods 20, classes 26), `practice/` + README, 8 edits to
  validate.py, 7 + PRACTICE constant to build.py, both schemas, CI trigger path,
  CLAUDE.md and the verify-integrity skill. There is deliberately NO `parts.yaml`.
- **Pre-flight step 7 has RUN, in both directions.** Four malformed records each
  gave error lines and no traceback; every safety gate fired. A valid draft then
  passed, reached the `.draft` twin only, and flipped its ref to
  `corpus: ["clinical","practice"]`.
- **D3 landed.** 10 compound ids triaged. Nothing set to `none`. Verified by
  execution that the flags drive the gate per class, including that a constrained
  arnica TOPICAL record passes while internal use on the same id is blocked.
- **Sourcing:** preparations 244 -> 229 unsourced, dosage 53 -> 46. Health Canada
  NNHPD opened as a new seam (7 dosage entries) and then **measured to exhaustion**
  for the remaining plants — 421 slugs probed, zero further hits, endpoint verified
  live afterwards. Do not re-run that sweep.
- **Integrity:** the database now has ZERO verified-but-unsourced entries in any
  statused field; it had 6 (contraindications, demoted to needs-review).

### What is NOT done — the work queue

1. **D2, and its ordering is FORCED. The window is open RIGHT NOW.** `corpus` is
   derived and live, and all 3,116 citations still derive to `["clinical"]` — a
   provably no-op state. Ship the Knowledge Finder corpus filter and bump
   `?v=kfN` on page 208, verify live, and only THEN add the first practice bibtex
   entry. Reverse that and methodology papers land in a clinical-evidence library
   with no filter to exclude them.
2. **The research** (spec step 7). ~120-140 primary papers + 15-20 pharmacopoeial.
   No practice record has been authored yet beyond throwaway tests.
3. **D5** — the conflict arbiter; the calculator's unit of output is a
   per-constituent table, never a single menstruum.
4. **D6 / phase 0** — 324 of 861 plant x compound slots need a resolution
   decision; 92 constituent entries carry no `compounds` list; 20 of 187 plants
   resolve nothing. Audit `compounds/` for what is ABSENT first (`salix_alba` has
   no `salicin` entity; `crocus_sativus` has no crocin).
5. **229 preparations + 46 dosages still unsourced.** Next best seams: the 61
   preparations whose monograph ref has no stored `summary` (fetch the PDF), then
   ESCOP / Commission E.
6. **D7 — `parts_used` cleanup, LAST.** 7 fungal `Whole Plant` records,
   `allium_sativum` has no `Bulb`. Until it lands `key.part` stays null-only, and
   the validator hard-errors on any non-null value.

## READ FIRST, IN THIS ORDER

1. `plant-database/CLAUDE.md` — the five invariants. Binding.
2. `plant-database/PRACTICE_CORPUS_SPEC.md` — the implementation spec: literal
   content for the new files, exact old/new edit pairs for the modified ones, a
   traced day-one green check, and the D0–D9 order.

   **Read §0 (Provenance and Trust) and APPENDIX A before you touch section 3.**
   The seventeen `OLD (verbatim)` anchors in §3 *do* all match the live files
   byte-for-byte at `22f88ed`, and each is unique in its file — the edits apply
   cleanly. The risk was never that they wouldn't apply; it is that what they
   apply is wrong. The three worst, all of which would otherwise have shipped:
   - `Edit C` loads `vocabularies/parts.yaml`, a file §1 of the same document
     explicitly forbids creating, with no `try` around the load. Unhandled
     `FileNotFoundError` in the only hard gate in the repo, on the first push,
     for all 187 plants.
   - The toxicity gate existed in the schema, the README, the decisions table and
     the risk register — and in **zero lines of validator code**. The claim that
     an absent `toxicity_flag` is fail-closed "by construction" was false: JSON
     Schema `default` is inert in this repo. Absent meant *unconstrained*, on the
     `alkaloid` join key shared by comfrey, butterbur, coltsfoot, celandine and
     arnica.
   - The copyright gate keyed on `normative_citations`, a field left over from
     the losing draft that is not in the schema at any level, on an
     `additionalProperties: false` record. It could never fire.
3. `plant-database/README.md` — schema mechanics, evidence scoring, REF convention.
4. `.claude/skills/osdb-*` — the four procedure skills.

## OWNER DECISIONS — FIXED, DO NOT RELITIGATE

- Namespace `practice/`, broad, with a **type discriminator** so it can later
  cover harvest/phenology, morphometrics, cultivation and post-harvest without a
  rename.
- **Hybrid class key**: key on existing compound ids (already enforced by
  `validate.py`'s `K` set) + an **optional** `extraction_class` disambiguator on
  the compound record and on `plants[].constituents[]`. Ambiguous or unresolved
  ids must degrade to **no recommendation** — never a guessed one.
- Pharmacopoeias in scope (Ph. Eur., USP, BHP, AHP) → second source shape; cite
  edition + monograph number, never reproduce text.
- **One public library** — practice sources appear in the Knowledge Finder,
  filterable by corpus. Needs a `corpus` dimension on `citations.json` and a
  `?v=kfN` bump.
- Calculator may recommend, gated `draft → approved`. Recommendations come from
  **actual Methods and Results** (solvent %, ratio, temperature, duration,
  measured value, assay) — never from titles or abstracts.
- Dosage splits: species dose ranges stay in plant `dosage[]`; only dose-**form**
  conversion maths goes in the new corpus.

## WORK ORDER

**Step 1 — apply APPENDIX A to section 3.** Mechanical, fully specified. Nothing
else starts until this is done, because everything else applies section 3.

**Step 2 — D8, the draft leak.** Decide per field whether `draft` should publish,
then make it explicit rather than incidental. This is also the leak path for any
future plant-record field, so it must precede any such field.

**Step 3 — D3, the toxicity gate.** Add `toxicity_flag`
(`none | dose-limited | topical-only | avoid-internal`) + `regulatory_note` to
`compound.schema.json`, **enforced in `validate.py` treating absent as
`avoid-internal`** — not via the schema `default`, which nothing reads. Populate
for at least `alkaloid`, `berberine`, `coumarin`, `asarone`,
`sesquiterpene-lactone`, `parthenolide`, `anthraquinone`, `hypericin`, `allicin`,
`organosulfur`. Widen the `vocab.json` compound projection so the field reaches a
consumer (invariant 4). Add required `recommendation.route: internal | topical`.

**Step 4 — D0**, the day-one landing, one commit. The green check in spec §4 is
the acceptance test. Then run §0's pre-flight checklist end to end — especially
step 7: author one deliberately malformed throwaway record per live `record_type`
and confirm each produces error lines and **not a traceback**. Until that has run,
no rule in the spec is known to work in either direction.

**Step 5 — D1**, reconcile the record shape in writing, and delete the losing
draft so nobody authors against it.

**Step 6 — phase 0, the entity work.** This is the part the paper estimate hides.
It is sized in *entries*, not papers. Re-measured directly against the tree at
`88221f9` (an earlier subagent pass reported 842 / 394 / 27; those were wrong):

- **861** plant×compound slots total.
- **324** need a `resolution` / `extraction_class` decision, treating
  `{flavonoid, tannin, polysaccharide, terpene}` as ambiguous and
  `{glycoside, phenolic-compound}` as unresolvable. Change that set and the
  number moves — state your set explicitly when you report progress.
- **92** constituent entries carry **no `compounds` list at all**.
- **20 of 187 plants resolve nothing** and would emit zero recommendations from a
  complete corpus: `andrographis-paniculata, asclepias-tuberosa,
  capsella-bursa-pastoris, cordyceps-militaris, crocus-sativus,
  equisetum-pratense, equisetum-sylvaticum, galium-album, gentiana-lutea,
  gymnema-sylvestre, hericium-erinaceus, inonotus-obliquus, lentinula-edodes,
  piper-methysticum, pleurotus-ostreatus, psilocybe-cubensis, rhodiola-rosea,
  salix-alba, scutellaria-lateriflora, trametes-versicolor`.

Two patterns, and both say this is an **entity-model gap, not a sourcing gap**:

- **7 of the 20 are the same 7 fungi** that carry the `Whole Plant` `parts_used`
  debt. They fail on both axes at once — no usable part *and* no resolvable
  compound. Fix them as one workstream, not two.
- **The defining constituent is often simply missing from `compounds/`.**
  `salix_alba`'s "Salicin and related salicylates" has `compounds: None` and
  **there is no `salicin` entity** — salicin being the one thing anyone looks
  willow bark up for. `crocus_sativus` is the same shape: crocin, crocetin,
  safranal and picrocrocin are all named in its constituents and none is an
  entity. **Audit `compounds/` for what is absent before disambiguating what
  exists** — adding the missing entities may resolve several of the 20 outright,
  and is cheaper than every alternative.

Report coverage as a first-class build number. A green build with 20 silent
plants must not read as success.

**Step 7 — the research.** ~120–140 primary papers + 15–20 pharmacopoeial, or
180–200 if `approved` requires 2+ independent sources. Reviews **cannot** carry a
record alone: they report no single (solvent, temperature, time, ratio, yield)
tuple, which is exactly what the Methods/Results rule demands. That is the single
biggest cost driver, because reviews are otherwise the cheapest sources.

**Step 8 — D7, the `parts_used` cleanup, goes LAST**, and until it lands the
practice `key.part` axis stays **`null`-only**. Note `parts_used` has no
`reference_ids` field, so either add one or record the justification in
`internal_notes`; adding a bibtex entry with nothing to cite it from creates an
orphan.

## TRAPS THAT WILL BITE

1. **`schema/*.json` is loaded by nothing.** No `jsonschema` import anywhere.
   JSON Schema here is an inert documentation contract; `validate.py` is the only
   real gate. Any "structurally impossible" rule must be imperative Python. A
   rule that exists only in the schema does not exist.
2. **Analytical vs preparative solvents.** Most published optimisation work uses
   methanol or acetone. Without a `consumer_safe` gate and an extrapolation
   envelope partitioned *by solvent on every axis*, a methanol sweep legitimises
   an "ethanol 60–75%" band the calculator then prints. Findings may cite lab
   solvents; recommendations may not.
3. **The join key is shared with the hepatotoxins.** Compound id `alkaloid` is
   declared by **17 plants** including `symphytum-officinale`,
   `borago-officinalis`, `chelidonium-majus`, `petasites-hybridus` and
   `arnica-montana`. A class-level "acidified menstruum extracts the salt"
   recommendation instructs a user to maximise **pyrrolizidine-alkaloid**
   recovery from comfrey root. `arnica_montana` is
   `Flower head (topical preparations)`. Same trap on `coumarin` (19 plants),
   `sesquiterpene-lactone` (11), `asarone` (`acorus-calamus`). Yield-optimal is
   not use-optimal.
4. **False orphans destroy the corpus.** `cited.update(find_refs(d))` appears
   once, at `validate.py:162`, inside the plants loop. Practice REF ids would
   report as orphans — and `osdb-verify-integrity` instructs deleting orphaned
   bibliography entries. The baseline is **zero** orphans, so the first practice
   batch produces a warning block that is entirely practice REFs, in a repo where
   that list has never had anything in it. Follow the documented procedure and you
   delete the corpus's bibliography, then the same refs flip to hard errors with
   the data already gone. The fix is one line and **must ship in the same commit
   as the `practice/` directory**.
5. **The `.draft` twin name is load-bearing.** `practice.v1.draft.json` inherits
   the existing `build/*.draft.json` gitignore (`.gitignore:16`). Any other name
   gets committed, reaches `osdb/main`, and the WordPress sync serves unreviewed
   recommendations.
6. **Knowledge Finder deploy order is forced.** `build.py` iterates every bibtex
   entry into `citations.json` regardless of linkage or status, and
   `bibliography.bibtex` is a CI trigger path — so the moment the first practice
   REF exists it is public. Ship `corpus` derivation → ship the KF filter and bump
   `?v=kfN` while every entry still derives to `["clinical"]` (a provably no-op
   deploy is the only safe way to test a filter) → *only then* add the first
   practice bibtex entry.
7. **The evidence ladder inverts.** `TIER_BASE` scores `review` 7 and
   `preclinical` 2. For extraction chemistry a controlled bench study is the gold
   standard and a review scores zero. Do **not** edit `TIER_BASE` — it feeds
   `plants.json` and `symptoms.json`, and touching it silently moves every
   evidence number on the site. The practice ladder is separate, and its score
   must never render as the clinical 1–10 dots.

## HOW TO WORK

- `python scripts/validate.py` must exit 0 before any commit; then
  `python scripts/build.py` and commit `build/` too. Green means references and
  vocab ids resolve — **not** that the data is correct.
- Invariant 1 governs everything: truthful or absent. A documented dead end in
  `internal_notes` is a success; a plausible-sounding gap-filler is a broken
  database that looks fine.
- Invariant 4 for every new field: schema entry, validate rule, build handling, a
  real downstream consumer, and defined behaviour when absent.
- If using ultracode: **never more than 2 agents at a time.**
- Ask before committing, pushing or deploying.
