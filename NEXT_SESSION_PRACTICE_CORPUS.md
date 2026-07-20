# Next session — the practice corpus, full per-plant scope

Paste the block below into a new conversation. Everything it references is on disk.

---

## MISSION

Build the **practice corpus** — a second, applied research corpus in
`plant-database/` that sources the tincture and formula calculators on
omniasana.bio. Those two calculators are the only public tools with no data
backing: `uploads/omniasana/js/os-formulation.js` asserts `PART_RATIOS` 0.15–0.45,
`DEFAULT_RATIO` 1:5, `GLYCERITE_MIX` 75/25 and `shelfLife()` ABV bands with **zero
provenance**, on a site whose entire proposition is that it cites things.

Scope is **full per-plant recommendation at `approved`** — the calculator says
"use 60–70% ethanol for this plant" with a citation. The owner has accepted the
cost with eyes open. Do it properly: factual, future-proof, no logical fallacies,
no mismatch or chaos in the entity model. Speed is not the constraint;
correctness is.

## READ FIRST, IN THIS ORDER

1. `plant-database/CLAUDE.md` — the five invariants. Binding.
2. `plant-database/PRACTICE_CORPUS_SPEC.md` — the implementation spec. Literal
   content for the new files, exact old/new edit pairs for the modified ones, a
   traced day-one green check, and the D0–D9 order. Produced by an 8-agent pass
   (2 survey, 2 design, 2 adversarial refutation, 2 synthesis), then audited by a
   further 3-agent pass. **Nothing in it has been applied.**

   **Read §0 (Provenance and Trust) and APPENDIX A before you touch section 3.**
   The audit found 14 blocking and 7 major defects, and **Appendix A is not
   applied to the body — section 3 still contains all of them.** Apply the
   appendix to section 3 first, then follow the §0 pre-flight checklist. The
   three that matter most:
   - `Edit C` loads `vocabularies/parts.yaml`, which §1 explicitly forbids
     creating, with no `try` around the load. Unhandled `FileNotFoundError` in
     the only hard gate in the repo, on the first push, for all 187 plants.
   - The toxicity gate existed in the schema, the README, the decisions table and
     the risk register — and in **zero lines of validator code**. The claim that
     an absent `toxicity_flag` is fail-closed "by construction" was false: JSON
     Schema `default` is inert here. Absent meant unconstrained, on the join key
     shared by comfrey, butterbur, coltsfoot, celandine and arnica.
   - The copyright gate keyed on `normative_citations`, a field left over from
     the losing draft that is not in the schema at any level. It could never fire.

   The seventeen `OLD (verbatim)` anchors in section 3 *do* all match the live
   files byte-for-byte at `22f88ed` — the edits apply cleanly. The risk was never
   that they wouldn't apply; it was that what they apply is wrong.
3. `plant-database/README.md` — schema mechanics, evidence scoring, REF convention.
4. `.claude/skills/osdb-*` — the four procedure skills.

## STATE (verified 2026-07-20, HEAD `88221f9`, tree clean)

187 plants · 3,110 refs cited / 3,110 declared · **zero orphans** · validate and
build both green. That clean baseline matters — see trap 3.

Already committed: the four `parts_used` comma-split repairs, `crocus_sativus`
Flower→Stigma (3 sourced reviews), `hericium_erinaceus` Fruit→Fruiting body,
`Whole Plant`→`Whole plant` on the 3 non-fungal records, plus a docs pass that
corrected several skill claims that misdescribed the code.

## OWNER DECISIONS — FIXED, DO NOT RELITIGATE

- Namespace `practice/`, broad, with a **type discriminator** so it can later
  cover harvest/phenology, morphometrics, cultivation, post-harvest without a rename.
- **Hybrid class key**: key on existing compound ids (already enforced by
  `validate.py`'s `K` set) + an optional `extraction_class` disambiguator on the
  compound record and on `plants[].constituents[]`. Ambiguous or unresolved ids
  must degrade to **no recommendation** — never a guessed one.
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

**First — two fixes the owner has approved, independent of the corpus:**

- **D8. The already-public draft leak.** `build.py`'s public projection is
  `q = {k: v for k, v in p.items() if k != "internal_notes"}`, and `approved_only()`
  is applied to exactly three keys (`drug_class_interactions`, `pairings`,
  `dangerous_lookalikes`). Everything else ships status-ignored. **Measured: 280
  `draft` preparations and 84 `draft` dosages are live on the plant pages now.**
  Decide per field whether draft should publish, then make it explicit rather
  than incidental. This is also the leak path for any future plant-record field.
- **D3. The toxicity gate.** `compounds/*.yaml` carries only
  `{id, name, class, synonyms}` — no toxicity field. Add `toxicity_flag`
  (`none | dose-limited | topical-only | avoid-internal`) + `regulatory_note`,
  **defaulting to `avoid-internal` when absent** so it is fail-closed rather than
  discipline-dependent. Populate for at least `alkaloid`, `berberine`, `coumarin`,
  `asarone`, `sesquiterpene-lactone`, `parthenolide`, `anthraquinone`, `hypericin`,
  `allicin`, `organosulfur`. Widen the `vocab.json` compound projection so the
  field reaches a consumer (invariant 4). Add required
  `recommendation.route: internal | topical`.

**Then D0** — the day-one landing, one commit: `schema/practice.schema.json`, the
three vocabularies, empty `practice/`, and all of spec §3.1–3.7. The green check
in spec §4 is the acceptance test. Three one-liners inside it must not slip: the
CI trigger path, the `cited.update()` orphan fix, and deriving `corpus` rather
than validating it.

**Then D1** — reconcile the record shape in writing before anyone authors, and
delete the losing draft so nobody writes against it.

**Then phase 0 — the entity work, and this is the part the paper estimate hides.**
It is sized in *entries*, not papers. Figures below were re-measured directly
against the tree at `88221f9` (an earlier subagent pass reported 842 / 394 / 27;
those were wrong or used a different ambiguity set — trust these, and re-run the
count yourself, since the disambiguation number depends on which ids you classify
as ambiguous):

- **861** plant×compound slots total.
- **324** need a `resolution` / `extraction_class` decision, treating
  `{flavonoid, tannin, polysaccharide, terpene}` as ambiguous and
  `{glycoside, phenolic-compound}` as unresolvable. Change that set and the
  number moves — state your set explicitly when you report progress.
- **92** constituent entries carry **no `compounds` list at all**.
- **20 of 187 plants resolve nothing** and would emit zero recommendations from a
  complete corpus:
  `andrographis-paniculata, asclepias-tuberosa, capsella-bursa-pastoris,
  cordyceps-militaris, crocus-sativus, equisetum-pratense, equisetum-sylvaticum,
  galium-album, gentiana-lutea, gymnema-sylvestre, hericium-erinaceus,
  inonotus-obliquus, lentinula-edodes, piper-methysticum, pleurotus-ostreatus,
  psilocybe-cubensis, rhodiola-rosea, salix-alba, scutellaria-lateriflora,
  trametes-versicolor`.

Two patterns in that list, and both say the gap is an **entity-model gap, not a
sourcing gap**:

- **7 of the 20 are the same 7 fungi that carry the `Whole Plant` `parts_used`
  debt.** They fail on both axes at once — no usable part *and* no resolvable
  compound. Fix them as one workstream, not two.
- **The defining constituent is often simply missing from `compounds/`.**
  `salix_alba`'s "Salicin and related salicylates" has `compounds: None` and
  **there is no `salicin` entity** — salicin being the one thing anyone looks
  willow bark up for. `crocus_sativus` is the same shape: crocin, crocetin,
  safranal and picrocrocin are all named in its constituents and none is an
  entity. Before disambiguating what exists, **audit `compounds/` for what is
  absent**; adding the missing entities may resolve several of these 20 outright.

Report coverage as a first-class build number. A green build with 20 silent
plants must not read as success.

**Then the research** — ~120–140 primary papers + 15–20 pharmacopoeial, or
180–200 if `approved` requires 2+ independent sources. Reviews **cannot** carry a
record alone: they report no single (solvent, temperature, time, ratio, yield)
tuple, which is exactly what the Methods/Results rule demands. That is the single
biggest cost driver, because reviews are otherwise the cheapest sources.

**D7 — `parts_used` cleanup goes LAST**, and until it lands the practice
`key.part` axis stays **`null`-only**. Outstanding debt: 7 fungal records declare
`Whole Plant` (`trametes_versicolor`, `psilocybe_cubensis`, `pleurotus_ostreatus`,
`lentinula_edodes`, `inonotus_obliquus`, `ganoderma_lingzhi`, `cordyceps_militaris`)
and `allium_sativum` has **no `Bulb`** — garlic's medicinal part is missing
entirely. Both need sourced corrections. Note `parts_used` has no `reference_ids`
field, so add one or record the justification in `internal_notes`; adding a bibtex
entry with nothing to cite it from creates an orphan.

## TRAPS THAT WILL BITE

1. **`schema/*.json` is loaded by nothing.** No `jsonschema` import anywhere.
   JSON Schema here is an inert documentation contract; `validate.py` is the only
   real gate. Any "structurally impossible" rule must be imperative Python.
2. **Analytical vs preparative solvents.** Most published optimisation work uses
   methanol or acetone. Without a `consumer_safe` gate and an extrapolation
   envelope partitioned *by solvent*, a methanol sweep legitimises an "ethanol
   60–75%" band the calculator then prints. Findings may cite lab solvents;
   recommendations may not.
3. **The join key is shared with the hepatotoxins.** Compound id `alkaloid` is
   declared by **17 plants** including `symphytum-officinale`, `borago-officinalis`,
   `chelidonium-majus`, `petasites-hybridus` and `arnica-montana`. A class-level
   "acidified menstruum extracts the salt" recommendation instructs a user to
   maximise **pyrrolizidine-alkaloid** recovery from comfrey root. `arnica_montana`
   is `Flower head (topical preparations)` and nothing in the current schema can
   say "topical only". Same trap on `coumarin` (19 plants),
   `sesquiterpene-lactone` (11), `asarone` (`acorus-calamus`). Yield-optimal is
   not use-optimal.
4. **False orphans destroy the corpus.** `cited.update(find_refs(d))` appears
   once, inside the plants loop. Practice REF ids would report as orphans — and
   `osdb-verify-integrity` instructs deleting orphaned bibliography entries. The
   baseline is zero orphans, so the first practice batch produces a warning block
   that is entirely practice REFs, in a repo where that list has never had
   anything in it. Follow the documented procedure and you delete the corpus's
   bibliography, then the same refs flip to hard errors with the data gone. The
   fix is one line and **must ship in the same commit as the `practice/` directory**.
5. **The `.draft` twin name is load-bearing.** `practice.v1.draft.json` inherits
   the existing `build/*.draft.json` gitignore. Any other name gets committed,
   reaches `osdb/main`, and the WordPress sync serves unreviewed recommendations.
6. **Knowledge Finder deploy order is forced.** `build.py` iterates every bibtex
   entry into `citations.json` regardless of linkage or status, and
   `bibliography.bibtex` is a CI trigger path — so the moment the first practice
   REF exists it is public. Ship `corpus` derivation → ship the KF filter and bump
   `?v=kfN` while every entry still derives to `["clinical"]` (a provably no-op
   deploy) → *only then* add the first practice bibtex entry.
7. **The evidence ladder inverts.** `TIER_BASE` scores `review` 7 and
   `preclinical` 2. For extraction chemistry a controlled bench study is the gold
   standard and a review scores zero. Do **not** edit `TIER_BASE` — it feeds
   `plants.json` and `symptoms.json`, and touching it silently moves every
   evidence number on the site. The practice ladder is separate, and its score
   must never render as the clinical 1–10 dots.

## HOW TO WORK

- `python scripts/validate.py` must exit 0 before any commit; then
  `python scripts/build.py` and commit `build/` too. Green means references and
  vocab ids resolve — not that the data is correct.
- Invariant 1 governs everything: truthful or absent. A documented dead end in
  `internal_notes` is a success; a plausible-sounding gap-filler is a broken
  database that looks fine.
- Invariant 4 for every new field: schema entry, validate rule, build handling, a
  real downstream consumer, and defined behaviour when absent.
- If using ultracode: **never more than 2 agents at a time.**
- Ask before committing or deploying. Don't push to the site without being asked.
