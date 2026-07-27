# Practice Corpus — Continuation Handoff

**Date saved:** 2026-07-27 | **Git:** `osdb/main` = `fce6b4c` | **Next REF id:** REF-3137

## Mission

Continue and finish the PRACTICE CORPUS — the second, applied research corpus in `plant-database/` that sources the tincture and formula calculators on omniasana.bio. Those two calculators are the only public tools with no cited data behind them: `uploads/omniasana/js/os-formulation.js` hardcodes PART_RATIOS 0.15–0.45, DEFAULT_RATIO 1:5, GLYCERITE_MIX 75/25 and shelfLife() ABV bands with ZERO provenance, on a site whose whole proposition is that it cites things. Scope is a full per-plant, per-constituent recommendation at `approved` — the calculator says "use 60–70% ethanol for this plant" WITH a citation. Do it properly: factual, future-proof, no logical fallacies, no entity-model chaos. Correctness is the constraint, not speed. The infrastructure is built and deployed; what remains is research + the entity-model work.

## State (verified end of session 2026-07-27)

Git: `osdb/main` = `fce6b4c`, working tree clean, validate.py exits 0. Next REF id: REF-3137 (always re-check: `grep -o "REF-[0-9]\{4\}" bibliography.bibtex | sort -u | tail -3`).

75 compounds, 187 plants. Public practice.v1.json = 0 records; draft twin = 3 (gitignored).

## Done — do not redo

- Infrastructure (D0), D8 (nothing unsourced publishes), Knowledge Finder corpus filter (?v=kf8, live). D3 toxicity triage (16 compounds flagged; rest fail-closed avoid-internal).
- THREE gate/emitter fixes (all proven surgical, no-op on existing data):
  * (A) validate.py: RSM optimum → envelope-containment for optimisation tier, strict membership kept for comparative-bench.
  * (B) validate.py: finding solid:liquid band widened 1:2→1:2000 (analytical extractions are dilute).
  * (C) build.py: R1-7 practice→plant linkage + clinically_linked snapshot so practice refs aren't unlinked KF cards.
- kind==standard harvard()/best_link() branches (pharmacopoeial citations render correctly).
- conversion-block emitter (Gap 2): dose-form-conversion records now reach the calculator.
- THREE verified draft practice records (crocin, salicin class-general, parthenolide avoid-only). Read them as worked examples of the record shapes.
- D6 CORE: all 75 compounds carry extraction_class + resolution. 160/187 plants now resolve to a class; broad/ambiguous ids degrade to no-recommendation by design.

## Work Queue — Priority Order

### 1. THE RESEARCH (the main event)

~120–140 primary papers + pharmacopoeial. Method that works: fan-out FIND agents + adversarial VERIFY agents, then author ONLY what survives verification. Verification has already caught a wrong temperature (Tong 2018) and an unreachable full text (Zheng 2024) — trust it. Author at status: draft. Key on a triaged dose-limited compound + a plant with a clean part. Start from the compounds that now resolve exact (160 plants) so a class-default recommendation has a home.

### 2. NORMATIVE record (sources DEFAULT_RATIO 1:5)

Code prerequisites ALL shipped. Two constraints:
- (a) Pharmacopoeial findings REQUIRE a species binomial, so the GENERAL Ph. Eur. 0765 "a tincture is 1:5" definition can't be a finding — use a SPECIES monograph (WHO Radix Valerianae etc.), record_type dose-form-conversion, parameter_kind normative, species-specific, jurisdiction set.
- (b) Needs a READABLE primary — WebFetch could not reach WHO/Ph.Eur PDFs (403/binary/DSpace); an interactive browser session or institutional access is required. Content is well-corroborated (Ph.Eur 0765: 1:10 or 1:5; valerian 1:5 in 70% EtOH) but was HELD unauthored to honour the same "full text unreachable" bar that dropped Zheng. AUTHORITIES set = {ph-eur,usp-nf,bhp,ahp,bp,who-monographs,escop}; EMA HMPC is NOT in it (best free readable seam if you add it, invariant 4).

### 3. 229 preparations + 46 dosages still withheld (D8)

Best seams: the ~61 preparations whose monograph ref has no stored summary (fetch PDF, read); then ESCOP; then Commission E (Blumenthal 1998) — the tier never opened, best fit for traditional 1:5 tinctures.

### 4. D6 TAIL: 85 empty constituent compounds-lists across 63 plants

Continue the absent-entity audit — CREATE the missing compound entity (kavalactones/piper-methysticum, gymnemic-acids/gymnema-sylvestre, arbutin/uva-ursi, andrographolide/andrographis, the equisetum & galium constituents…), assign its extraction_class + resolution, wire it. Cheapest wins first.

### 5. D5 conflict arbiter

13 plants have a water-vs-ethanol collision; the calculator's output is a per-constituent table, never one menstruum; PRACTICE_PLANT_EXCLUSIONS for 7 fungi + allium-sativum lands with the plant→practice join. D7 parts cleanup LAST.

## Read First, In Order

1. `plant-database/CLAUDE.md` — the five invariants. Binding. (Truthful-or-absent; source fits the specific claim; documented dead ends are successes; decide for the schema you will have; never commit unvalidated.)
2. `plant-database/practice/README.md` — the corpus's front door (the ladder is inverted: optimisation=7, review=0; the three hard gates; presentation as method-confidence, never the clinical dots).
3. `plant-database/PRACTICE_CORPUS_SPEC.md` §0, then APPENDIX B, then §1–3 as needed.
4. The three existing records in `practice/*.yaml` as worked examples.
5. Auto-memory `omniasana-practice-corpus-campaign.md` (top addenda are the live state).

## How to Work

`python scripts/validate.py` must exit 0 before any commit, then `python scripts/build.py`, commit build/ too. Green means refs+vocab resolve, NOT that data is correct. Verify DB changes on `/plant-monograph/{id-or-slug}/`, NOT `/plants/{slug}/` (a stale legacy CPT post). Ask before committing, pushing, or deploying.

## Traps (hard-won; do not re-derive)

- schema/*.json is loaded by NOTHING; validate.py is the only gate.
- `str(None)` is 'None' (truthy) — every text gate goes through `_s()`; never `str(x.get(k,"")).strip()`.
- Quote ratios in YAML: unquoted `1:10` loads as the integer 70 (YAML 1.1 sexagesimal).
- Analytical vs preparative solvents: findings may cite methanol/UAE; recommendations may not.
- Congeners and unverifiable papers → internal_notes prose ONLY, never cited (orphan + the build linkage mislinks a cited ref to the record's species).
- Fetch real bibtex via pubmed get_article_metadata (real abstracts + full author lists).
- Never trust a memory's "next REF id" — always grep bibliography.bibtex.
- Never re-read a YAML inside a per-entry edit loop; group edits, read/write each file once.
- If using workflows: keep StructuredOutput schemas MINIMAL (long field descriptions trip a safety classifier and the whole run returns empty); no backticks inside JS template literals; the workflow journal can record a completed agent's result as empty even when it succeeded — recover the payload from the agent-*.jsonl StructuredOutput tool_use input. Cap concurrent agents at 2. This session hit weekly usage limits — expect long research to span sessions.
