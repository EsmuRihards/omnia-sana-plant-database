# Practice corpus — implementation specification

Design output for the second (applied) corpus that will source the tincture and
formula calculators. Produced 2026-07-20 by an 8-agent review: 2 survey, 2 design,
2 adversarial refutation, 2 synthesis. **Not yet implemented.** Nothing in this
document has been written to the repo.

Owner decisions it is built on (fixed): broad `practice/` namespace with a type
discriminator; hybrid class key (existing compound ids + optional
`extraction_class` disambiguator); pharmacopoeias in scope; one public library
filterable by corpus; calculator may recommend, gated draft->approved, from actual
Methods/Results; species dose ranges stay in plant `dosage[]`.

Read section 1 first — it records which refutation findings are binding and why.
Section 4 (day-one green check) is the acceptance test.

Provenance note: sections were written by subagents and spot-verified against the
live tree, but line numbers and quoted code should be re-checked before applying.
The refutations (not included here) found 4 blocking issues in the first drafts;
section 1 lists the resolutions.

---

# 1. DECISIONS RESOLVED

Verified against the live repo: `vocab_ids()` at `validate.py:77` returns `{x["id"] for x in yaml.safe_load(...)}` — every vocabulary file below is a top-level **list of mappings with `id`**, loadable by that helper unchanged. `K` (compound ids) at `validate.py:86`. `constituents[]` confirmed to have `additionalProperties: false` and keys `{name, compounds, note, reference_ids}` only — no `part`. 17 plants carry compound id `alkaloid`, 19 `coumarin`, 11 `sesquiterpene-lactone`, 1 `asarone`, 3 `berberine` (measured).

| # | Finding | RESOLUTION (binding) |
|---|---|---|
| **R2-1** | Solvent identity unchecked; analytical solvent can surface as an ethanol instruction | `recommendation.solvent` and `recommendation.method` are **REQUIRED**. `validate.py` loads `vocabularies/solvents.yaml` + `extraction_methods.yaml` and **hard-errors** when `consumer_safe: false` / `consumer_reproducible: false`. The extrapolation envelope is built **only from findings whose `conditions.solvent` == `recommendation.solvent`** AND whose `varied_factor` == `recommendation.parameter`. A methanol sweep can never legitimise an ethanol band. Findings in non-recommended solvents are legal, contribute to `rationale` only, and are excluded from base, bonus, penalty and envelope. |
| **R2-2** | Yield-optimal ≠ use-optimal; the key compound ids are the toxic ones | Three new gates. (a) `compound.schema.json` gains `toxicity_flag: {none, dose-limited, topical-only, avoid-internal}` + `regulatory_note`; populated **before** any practice record is authorable for: `alkaloid, berberine, coumarin, asarone, sesquiterpene-lactone, parthenolide, anthraquinone, hypericin, allicin, organosulfur, thujone-bearing` — this covers the 17 alkaloid plants (`arnica-montana, borago-officinalis, chelidonium-majus, petasites-hybridus, symphytum-officinale, tussilago-farfara, hydrastis-canadensis, mahonia-aquifolium, …`), the 19 coumarin plants, `acorus-calamus`, and the 11 sesquiterpene-lactone plants. Absent → treated as `avoid-internal` (fail-closed). (b) `recommendation.route: {internal, topical}` REQUIRED; a record keyed on a `topical-only` compound may only be `topical`. (c) A record whose `key.compound_id` has any non-`none` flag is a **hard error unless** it carries `limit_rationale` (≥120 chars) AND `status: draft`, or `limit_rationale` + `reviewed_by` + `verified_by` at approved. Yield-maximising phrasing is barred by rule, stated in the skill. |
| **R2-3** | Two disjoint vocabularies; the binding copy has no safety flags | **One vocabulary.** `PCT_SOLVENTS`, `NOPCT_SOLVENTS`, `EXTRACTION_METHODS` are **deleted** from `validate.py` and replaced by `vocab_ids()` loads of the two YAML files below, plus a second load that reads `consumer_safe` / `consumer_reproducible` / `takes_concentration`. Naming convention = **the literature's** (`ethanol-water`, not `hydroethanol`), because findings transcribe Methods sections. |
| **R1-2** | No conflict-resolution rule for multi-class plants (13+ plants, e.g. `matricaria-chamomilla`) | Option (b): **the calculator's unit of output is a per-constituent table, never a single menstruum.** No `primary_constituent` field is added to plants (no new plant field, no backfill). `recommendation.statement` is defined as a per-class statement. The calculator renders one row per resolvable constituent and a standing line: *"a tincture captures X and loses Y."* Emitting a single number is a front-end bug, specified as such. |
| **R1-3 / R1-12** | `constituents[]` has no part attribution; `parts_used` still 58 dirty strings | **`key.part` is FROZEN to `null` in v1.** `validate.py` hard-errors on any non-null `part`. `vocabularies/parts.yaml` is **not created**. No `parts_used` enum, no migration, no `constituents[].parts` backfill is a prerequisite. `PART_RATIOS` **stays hardcoded** in the JS and is labelled unsourced. Part keying is a v2 item gated on the parts cleanup. |
| **R1-1 / R2-11** | The two drafts define incompatible finding shapes | **Canonical shape = Draft B's field names** (`locator`, `species`, `time_min`, `solvent_pct`, `method`, `quantification`, `comparator_levels`, `varied_factor`) **plus Draft A's `findings[].id` handles + `derived_from` + `avoid[]`**. `evidence_grade` is **deleted**. Record-level discriminator is `record_type` (Draft B). Ratio regex is `^\d+(\.\d+)?:\d+(\.\d+)?$` or the literal `unspecified`. |
| **R1-14** | `method_type` on the bibtex entry contradicts "grading lives on the finding" | **`method_type` moves onto the finding.** No bibtex edit is required to reuse an existing clinical REF in a practice finding. This also deletes the "unset method_type" double-error for the normal case. `bibliography.bibtex` gains **no new fields at all**. |
| **R1-5** | `_in_band` / envelope compare across physical dimensions | Both filtered to `varied_factor == recommendation.parameter` **and** `conditions.solvent == recommendation.solvent`. Hard error if no finding varies the recommended parameter in the recommended solvent. |
| **R1-6 / R2-6** | Orphan accounting incomplete (`normative_citations`, `references`, `species_overrides` uncollected) | Do **not** hand-enumerate. Call the existing generic `find_refs(rec)` on the whole practice record — it already skips `PROSE_KEYS` and walks arbitrary depth. `cited.update(find_refs(rec))`. Lands in the **same commit as the `practice/` directory**, not the first record. `osdb-verify-integrity` gains: *never delete a bibliography entry whose derived `corpus` includes `practice`.* |
| **R1-7 / R2-8** | `corpus` declared vs derived | **Derived only.** `build.py` sets it from actual linkage (`["clinical"]` when absent/unlinked, so all 3,110 entries are correct with zero backfill). The `validate.py` corpus check is **deleted**. `build.py`'s `add()` linkage inversion is extended over `practice/**` so practice REFs carry plant/class linkage into `citations.json` and do not render as unlinked orphan cards. |
| **R1-8** | Anti-skim is internally-consistent free text, not detection | Reframed and **sold as auditability**, not enforcement. Three additions make the audit real: (a) `findings[].fulltext_source` REQUIRED (`doi-pdf`, `pmc`, `publisher-html`, `institutional`, `author-copy`, `print`) — no full text, no finding; (b) `verified_by` + `verified_date` REQUIRED at approved and **must differ from `reviewed_by`** — a second person opened the paper; (c) `outcome.value` stored to the printed precision so a 10% spot-check script can diff. Documentation must say "auditable", never "impossible to fabricate". |
| **R1-9** | Over-strict required fields manufacture fabrication; 3 methods unauthorable | `solid_liquid_ratio`, `temperature_c`, `time_min`, `particle_size_mm` accept the literal `unspecified`/`null`. Absent-but-declared **caps** the finding: `condition_complete: false` (derived), and such a finding **may not be the sole support for approval**. `expression`, `crush-and-rest`, `steam-distillation`, `hydrodistillation` are exempt from the ratio/solvent-pct requirement via `takes_concentration: false` / `requires_menstruum: false` on the method and solvent vocabularies. `outcome.unit` is **opened**: `{value, unit, unit_basis, reference_standard}` — `unit_basis: {dry-weight, fresh-weight, extract, volume}`, `reference_standard` free text (`rutin`, `gallic acid`). |
| **R1-10 / R2** | Every "structurally impossible" claim resting on JSON Schema is false | Confirmed: no `jsonschema` import anywhere. **Every rule below is imperative `validate.py`.** The schema file is a documentation contract and says so in its own `description`. Highest priority: the two **copyright** checks — `statement_summary` length ≤ 300 chars, and a hard error when a bibtex entry with `kind = standard` carries an `abstract`. |
| **R1-11** | `extraction_exceptions[]` fails open on the already-broken records | **Inverted, and the field is deleted.** A plant receives a class recommendation only when its constituent resolves unambiguously to a single `extraction_class` **and** the keyed compound's `toxicity_flag` is `none`. Absent → no recommendation. Additionally `build.py` carries `PRACTICE_PLANT_EXCLUSIONS` = the 8 known-broken records (`trametes_versicolor, psilocybe_cubensis, pleurotus_ostreatus, lentinula_edodes, inonotus_obliquus, ganoderma_lingzhi, cordyceps_militaris, allium_sativum`), which emit nothing regardless. |
| **R2-4** | `approved_only()` covers 3 keys; new plant fields would leak | Resolved by **adding no statused plant field**. The only plant-record addition is `constituents[].extraction_class` — a vocabulary id, not a claim, no `status`. `approved_only()` is untouched. (Separate pre-existing issue: 280 draft preparations + 84 draft dosages are already public. Flagged, out of scope, must not be worsened by practice records contradicting them.) |
| **R2-5** | CI does not fire on `practice/**` | Add `- 'practice/**'` to `build-and-publish.yml` trigger paths **in the commit that creates the directory**. |
| **R2-7** | KF content leak; deploy order is forced | Order is mandatory and non-negotiable: (1) ship `corpus` derivation + `harvard()`/`best_link()` `kind == "standard"` branches, provably no-op on all 3,110 entries; (2) ship the KF corpus filter and **bump `?v=kfN` on page 208**, verify live; (3) only then add the first practice bibtex entry. |
| **R2-9** | Malformed YAML crashes the gate | `check_practice_recommendation` shape-validates and returns early **before** any scoring; the whole per-record body is wrapped `try/except Exception as e: errors.append(f"{nm}: crashed during validation: {e}")`. One bad record = one error line. |
| **R2-10** | Warnings gated harder than instructions | `avoid[]` entries may be backed by `references[]` with `method_type: method-review`. `recommendation` is **not** required for approval when `avoid[]` is non-empty. A record may be approved for saying only *don't*. |
| **R1-13** | `DEFAULT_RATIO 1:5` permanently unapprovable | **Refutation overruled in part** (stated explicitly): the ≥2-independent-source rule was designed for empirical concordance and does not apply to definitions. A `parameter_kind: normative` record may be approved on **one** authority provided `recommendation.jurisdiction` is set and `statement` is jurisdiction-scoped ("Ph. Eur. defines a tincture as 1:5 in 70% ethanol"). Disagreement between authorities is expressed as **two approved jurisdiction-scoped records**, not one contested record. |
| **R1-15** | `source_taxa` is required but computable | Derived in `build.py`; **removed from the authored record**. `excluded_taxa` is retained (authored judgement). |
| **R1-16 / R2-13** | Regex + drift | New anchored `PRACTICE_REF_RE = re.compile(r"^REF-\d{4,}$")`; existing `REF_RE` untouched. `evidence_type` → `study_type` in `source.schema.json` lands as its **own solo commit** (it is a CI trigger path). |
| **R1-4** | A large share of plant×compound slots need disambiguation; some plants emit nothing | Accepted and **scoped as phase 0**, sized in entries not papers. **Re-measured at `88221f9`: 861 slots, 324 needing a decision (37.6%), 92 constituent entries with empty `compounds`, and 20 of 187 plants resolving nothing** — the 842 / 394 / 46.8% / 27 figures that appeared in the drafts were wrong. The 324 depends on the ambiguity set (`{flavonoid, tannin, polysaccharide, terpene}` ambiguous, `{glycoside, phenolic-compound}` unresolvable); state your set when reporting. Coverage is stated honestly in the roadmap and the build print line reports plants-covered. A green build with 20 silent plants is **not** success. |
| **R2-12** | Disambiguator has no consumer | `build.py` adds `extraction_class` to the `vocab.json` compound projection in the same commit, and the `resolution` field (`exact`/`ambiguous`/`unresolvable`) is authored on the compound record with the degradation rule implemented in the calculator's join. |
| **R2-14** | Redundancy | `extraction_classes.yaml` is retained as a **value space only**; `key.extraction_class` is optional and never the primary key. `extraction_methods.yaml` ids are the normalisation target for the 549 existing `preparations[].name` strings (v2). |

---

# 2. FILES TO CREATE

## `schema/practice.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://omniasana.bio/schema/practice.schema.json",
  "title": "Practice record (applied corpus)",
  "description": "One record in the APPLIED corpus: practice/<id>.yaml. NOTE FIRST: nothing in this repo loads JSON Schema — there is no jsonschema import in scripts/. This file is a DOCUMENTATION CONTRACT. Every constraint expressed here as required/minItems/enum is enforced imperatively in scripts/validate.py, and that is the copy that runs. If the two disagree, validate.py wins and this file is the bug. A plant record answers 'what does this species do in people'; a practice record answers 'what comes out of this material under these conditions, and how do we know'. The evidence ladders invert: a designed bench experiment is the gold standard here and a review cannot carry a record at all. Do NOT reuse TIER_BASE / score_from_tiers from scripts/build.py — they feed indication_score, plants.json and symptoms.json, and touching them silently rescores the whole site.",
  "type": "object",
  "required": ["id", "record_type", "parameter_kind", "species_scope", "key", "status", "last_updated"],
  "additionalProperties": false,
  "properties": {
    "id": {"type": "string", "pattern": "^[a-z0-9-]+(--[a-z0-9-]+)*$", "description": "Stable slug and filename stem. Compose from the key: flavonoid--ethanol-water--maceration."},
    "record_type": {
      "type": "string",
      "enum": ["extraction", "stability", "dose-form-conversion", "harvest-timing", "identification", "cultivation", "post-harvest"],
      "description": "Q1 type discriminator, so practice/ can grow beyond extraction without a rename. LIVE: extraction, stability, dose-form-conversion. RESERVED and rejected by validate.py's PRACTICE_TYPES_LIVE: harvest-timing, identification, cultivation, post-harvest."
    },
    "parameter_kind": {
      "type": "string",
      "enum": ["empirical", "normative"],
      "description": "empirical = an optimum, kinetic, half-life or yield; only experimental findings are admissible. normative = a definition, ratio convention, identity criterion or dose-form equivalence; only pharmacopoeial findings are admissible. A standard mandating 70% ethanol is a committee decision, not a measured optimum, and contributes nothing to an empirical record."
    },
    "label": {"type": "string", "description": "Display label for the Knowledge Finder and the calculator provenance panel."},
    "status": {"type": "string", "enum": ["draft", "approved"], "description": "draft is written ONLY to build/practice.v1.draft.json, which is gitignored by build/*.draft.json and therefore never reaches osdb/main or the site."},
    "species_scope": {"type": "string", "enum": ["class-general", "species-specific"]},
    "species": {"type": "string", "pattern": "^[A-Z][a-z]+ [a-z][a-z-]+$", "description": "Required when species_scope is species-specific. Invariant 2 applies in full: every finding's binomial must match."},
    "off_corpus": {"type": "boolean", "description": "True when a species-specific record deliberately concerns a species with no plants/ record."},
    "key": {
      "type": "object",
      "required": ["compound_id", "part", "solvent", "method"],
      "additionalProperties": false,
      "description": "The join key. Keyed on an EXISTING compound id (validate.py's K set), not on a new class vocabulary. extraction_class is an optional disambiguator drawn from vocabularies/extraction_classes.yaml, used only where the compound id spans classes with different optima (flavonoid, tannin, polysaccharide, terpene, glycoside, phenolic-compound). An unresolved ambiguous id degrades to NO RECOMMENDATION.",
      "properties": {
        "compound_id": {"type": "string", "pattern": "^[a-z0-9-]+$", "description": "Must resolve to compounds/<id>.yaml."},
        "extraction_class": {"type": ["string", "null"], "pattern": "^[a-z0-9-]+$", "description": "Optional disambiguator -> vocabularies/extraction_classes.yaml."},
        "part": {"type": "null", "description": "FROZEN in v1. plants[].parts_used is 58 distinct dirty free-text strings with no enum and no rule, and constituents[] carries no part attribution at all, so the part axis cannot be populated from plant data. validate.py hard-errors on any non-null value. PART_RATIOS stays hardcoded and labelled unsourced until the parts cleanup lands."},
        "solvent": {"type": "string", "pattern": "^[a-z0-9-]+$", "description": "-> vocabularies/solvents.yaml. Concentration is never part of the id."},
        "method": {"type": "string", "pattern": "^[a-z0-9-]+$", "description": "-> vocabularies/extraction_methods.yaml."},
        "target_analyte": {"type": "string", "description": "Optional narrowing. Does not participate in the join."}
      }
    },
    "findings": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/finding"}},
    "recommendation": {"$ref": "#/$defs/recommendation"},
    "avoid": {
      "type": "array",
      "description": "Negative results. A precaution is CHEAPER to assert than an instruction: an avoid[] entry may be backed by references[] carrying method_type review-context, and a record with a non-empty avoid[] may be approved with no recommendation at all.",
      "items": {
        "type": "object",
        "required": ["solvent", "reason"],
        "additionalProperties": false,
        "properties": {
          "solvent": {"type": "string", "pattern": "^[a-z0-9-]+$"},
          "method": {"type": ["string", "null"], "pattern": "^[a-z0-9-]+$"},
          "above_concentration_pct": {"type": ["number", "null"], "minimum": 0, "maximum": 100},
          "reason": {"type": "string", "maxLength": 400},
          "derived_from": {"type": "array", "uniqueItems": true, "items": {"type": "string", "pattern": "^F\\d+$"}},
          "context_reference_ids": {"type": "array", "items": {"type": "string", "pattern": "^REF-\\d{4,}$"}}
        }
      }
    },
    "conversion": {"$ref": "#/$defs/conversion"},
    "generalisation": {
      "type": "object",
      "required": ["basis", "rationale"],
      "additionalProperties": false,
      "description": "Required when species_scope is class-general. Generalising is never implicit. source_taxa is DERIVED in build.py from findings[].material.species and must not be authored.",
      "properties": {
        "basis": {"type": "string", "enum": ["physicochemical", "matrix-analogous"]},
        "rationale": {"type": "string", "minLength": 80, "maxLength": 1200, "description": "WHY the chemistry carries across species. 'Similar compounds' is not a rationale and fails on length."},
        "excluded_taxa": {"type": "array", "items": {"type": "string", "pattern": "^[A-Z][a-z]+ [a-z][a-z-]+$"}},
        "reviewed_by": {"type": "string"},
        "reviewed_date": {"type": "string", "pattern": "^\\d{4}-\\d{2}-\\d{2}$"}
      }
    },
    "limit_rationale": {"type": "string", "minLength": 120, "maxLength": 1200, "description": "REQUIRED when the keyed compound carries a non-none toxicity_flag in compounds/<id>.yaml. States the dose or route limit and why the recommendation does not maximise recovery. A recommendation is a preparation that is safe and traditionally correct; it is never the argmax of a yield table."},
    "discordance_note": {"type": "string", "maxLength": 800, "description": "REQUIRED at approved when any admissible finding's optimum falls outside the recommended band. Deleting the inconvenient finding to lift a score is falsifying the grade."},
    "references": {"type": "array", "items": {"type": "string", "pattern": "^REF-\\d{4,}$"}, "description": "Background sources. May back an avoid[] entry; may never back a recommendation."},
    "context_reference_ids": {"type": "array", "items": {"type": "string", "pattern": "^REF-\\d{4,}$"}, "description": "Reviews and orientation. Contribute nothing to the score."},
    "reviewed_by": {"type": "string"},
    "reviewed_date": {"type": "string", "pattern": "^\\d{4}-\\d{2}-\\d{2}$"},
    "verified_by": {"type": "string", "description": "REQUIRED at approved and MUST differ from reviewed_by. Means a second person opened the cited PDFs and checked the locators. This is the only externally-real half of the anti-skim design."},
    "verified_date": {"type": "string", "pattern": "^\\d{4}-\\d{2}-\\d{2}$"},
    "internal_notes": {"type": "string", "description": "NEVER published. The field name is load-bearing: validate.py PROSE_KEYS and build.py's public filter both key on this literal string. Any other name and every REF mentioned in a dead-end note counts as cited."},
    "last_updated": {"type": "string", "pattern": "^\\d{4}-\\d{2}-\\d{2}$"}
  },
  "$defs": {
    "finding": {
      "type": "object",
      "required": ["id", "ref_id", "method_type", "fulltext_source", "locator", "material", "varied_factor", "conditions", "outcome"],
      "additionalProperties": false,
      "description": "One paper, one condition set, one measured number. Six solvent levels in one paper is six findings sharing a ref_id.",
      "properties": {
        "id": {"type": "string", "pattern": "^F\\d+$", "description": "Record-local handle. recommendation.derived_from points here."},
        "ref_id": {"type": "string", "pattern": "^REF-\\d{4,}$"},
        "method_type": {
          "type": "string",
          "enum": ["optimisation", "comparative-bench", "characterisation", "pharmacopoeial", "method-review", "traditional-text"],
          "description": "The practice tier, held on the FINDING and not on the bibtex entry: one paper can be optimisation for the solvent axis and characterisation for temperature, and a per-source grade would be wrong half the time. It also means reusing an existing clinical REF needs no bibliography edit. Bases: optimisation 7, pharmacopoeial 6, comparative-bench 5, characterisation 3, method-review 0, traditional-text 0. method-review and traditional-text MAY NOT appear in findings[] at all — validate.py rejects them; they belong in context_reference_ids[]."
        },
        "design": {"type": "string", "enum": ["rsm-ccd", "rsm-bbd", "factorial", "taguchi", "mixture", "multi-level-sweep", "two-level", "single-condition", "normative"]},
        "authority": {"type": "string", "enum": ["ph-eur", "usp-nf", "bhp", "ahp", "bp", "who-monographs", "escop"], "description": "Pharmacopoeial findings only. Doubles as the independence key: two editions of one body are one voice."},
        "fulltext_source": {"type": "string", "enum": ["doi-pdf", "pmc", "publisher-html", "institutional", "author-copy", "print", "pharmacopoeia-subscription"], "description": "Where the full text was actually read. There is no value meaning 'abstract only', because an abstract cannot produce a finding."},
        "locator": {
          "type": "object",
          "required": ["section"],
          "additionalProperties": false,
          "properties": {
            "section": {"type": "string", "enum": ["methods", "results", "table", "figure", "supplementary", "monograph"]},
            "table": {"type": "string"},
            "figure": {"type": "string"},
            "page": {"type": "integer", "minimum": 1},
            "monograph": {"type": "string", "description": "Pharmacopoeial only, e.g. '1559'."},
            "edition": {"type": "string", "description": "Pharmacopoeial only, e.g. 'Ph. Eur. 11.5'. Monograph numbers persist across editions while their requirements change."}
          }
        },
        "statement_summary": {"type": "string", "maxLength": 300, "description": "Pharmacopoeial findings only. ONE-SENTENCE PARAPHRASE of the requirement, in your own words. NEVER a quotation and never a transcription: these are copyrighted paywalled normative texts. validate.py enforces the length; it is one of the two copyright gates and the highest-consequence check in the file."},
        "material": {
          "type": "object",
          "required": ["species", "part", "state"],
          "additionalProperties": false,
          "properties": {
            "species": {"type": "string", "pattern": "^[A-Z][a-z]+ [a-z][a-z-]+", "description": "As PRINTED in the paper, including when it is a food crop. Writing our species because the congener is close enough is the failure invariant 2 exists to stop."},
            "part": {"type": "string", "description": "Free text as the paper reports it. NOT a controlled id — the part vocabulary is frozen in v1."},
            "state": {"type": "string", "enum": ["fresh", "dried", "freeze-dried", "frozen", "unspecified"]},
            "particle_size_mm": {"type": ["number", "string", "null"], "description": "Number in mm, or the literal 'unspecified'. Declaring it unspecified is honest and caps the finding."},
            "origin": {"type": "string"}
          }
        },
        "varied_factor": {"type": "string", "enum": ["solvent_pct", "temperature_c", "time_min", "solid_liquid_ratio", "ph", "particle_size_mm", "cycles", "method", "none"]},
        "conditions": {
          "type": "object",
          "required": ["solvent", "temperature_c", "time_min", "solid_liquid_ratio", "method"],
          "additionalProperties": false,
          "description": "The Methods tuple. Every required field accepts the literal 'unspecified' where the paper genuinely omits it; validate.py then sets condition_complete false, and an incomplete finding may not be the sole support for approval. Rejecting such papers outright is what makes a tired editor invent 1:10.",
          "properties": {
            "solvent": {"type": "string", "pattern": "^[a-z0-9-]+$"},
            "solvent_pct": {"type": ["number", "null"], "minimum": 0, "maximum": 100, "description": "REQUIRED when the solvent has takes_concentration true; MUST be null otherwise. Record the number the paper used (63), never a band."},
            "temperature_c": {"type": ["number", "string"], "description": "Number in C, or 'unspecified'."},
            "time_min": {"type": ["number", "string"], "description": "Number in minutes, or 'unspecified'."},
            "solid_liquid_ratio": {"type": "string", "pattern": "^(\\d+(\\.\\d+)?:\\d+(\\.\\d+)?|unspecified|n-a)$", "description": "'1:20', or 'unspecified', or 'n-a' for methods with requires_menstruum false (expression, crush-and-rest, distillation)."},
            "ph": {"type": ["number", "null"], "minimum": 0, "maximum": 14},
            "cycles": {"type": ["integer", "null"], "minimum": 1},
            "method": {"type": "string", "pattern": "^[a-z0-9-]+$"},
            "agitation": {"type": "string"},
            "power_w": {"type": ["number", "null"], "minimum": 0},
            "frequency_khz": {"type": ["number", "null"], "minimum": 0},
            "pressure_bar": {"type": ["number", "null"], "minimum": 0}
          }
        },
        "outcome": {
          "type": "object",
          "required": ["analyte", "quantification", "value", "unit", "unit_basis"],
          "additionalProperties": false,
          "properties": {
            "analyte": {"type": "string", "minLength": 3},
            "quantification": {"type": "string", "enum": ["hplc-dad", "hplc-uv", "hplc-ms", "uplc-ms", "gc-ms", "gc-fid", "lc-nmr", "uv-vis", "gravimetric", "titrimetric", "folin-ciocalteu", "aluminium-chloride", "vanillin-hcl", "dpph", "frap", "volumetric-distillation"], "description": "Colorimetric totals and chromatographic quantitation are not the same measurement and must never be compared across findings as if they were."},
            "value": {"type": "number", "exclusiveMinimum": 0, "description": "To the precision printed, so a spot-check can diff it."},
            "unit": {"type": "string", "minLength": 1, "description": "Open, e.g. 'mg/g', 'mL/100 g', '% v/w', 'mg RE/g'. A closed 9-value enum silently destroyed the reference standard."},
            "unit_basis": {"type": "string", "enum": ["dry-weight", "fresh-weight", "extract", "volume", "unspecified"]},
            "reference_standard": {"type": "string", "description": "Rutin, gallic acid, quercetin. An equivalence unit without its standard is not a unit."},
            "dispersion": {"type": "string"},
            "comparator_levels": {"type": "array", "items": {"type": ["number", "string"]}, "description": "EVERY level the Methods say was tested, not just the winner. Abstracts report the winner; only Methods report the set."},
            "optimum_level": {"type": ["number", "null"]},
            "optimum_value": {"type": ["string", "null"]},
            "is_optimum_stated": {"type": "boolean", "description": "True only when the authors themselves name this the optimum. Never assert it by picking the largest number in a table."}
          }
        },
        "note": {"type": "string", "maxLength": 600}
      }
    },
    "recommendation": {
      "type": "object",
      "required": ["parameter", "solvent", "method", "route", "statement", "derived_from"],
      "additionalProperties": false,
      "description": "What the calculator is permitted to say. Enforced in validate.py: solvent must be consumer_safe, method must be consumer_reproducible, every derived_from handle must resolve, the recommended band must lie inside the envelope swept BY FINDINGS IN THE SAME SOLVENT VARYING THE SAME PARAMETER, and at least one such finding must be optimisation or comparative-bench.",
      "properties": {
        "parameter": {"type": "string", "enum": ["solvent_pct", "temperature_c", "time_min", "solid_liquid_ratio", "ph", "cycles", "shelf_life_months", "drug_extract_ratio"]},
        "solvent": {"type": "string", "pattern": "^[a-z0-9-]+$", "description": "REQUIRED. Without it a bare band renders in an ethanol calculator as an ethanol instruction, even when every finding was a methanol sweep."},
        "method": {"type": "string", "pattern": "^[a-z0-9-]+$"},
        "route": {"type": "string", "enum": ["internal", "topical"], "description": "REQUIRED. A record keyed on a compound flagged topical-only may only be topical."},
        "range": {"type": "array", "minItems": 2, "maxItems": 2, "items": {"type": "number"}},
        "value": {"type": "string"},
        "unit": {"type": "string"},
        "jurisdiction": {"type": "string", "description": "REQUIRED when parameter_kind is normative. A definitional claim needs no replication but must be scoped: 'Ph. Eur. defines a tincture as 1:5 in 70% ethanol.'"},
        "statement": {"type": "string", "maxLength": 400},
        "rationale": {"type": "string", "maxLength": 800},
        "derived_from": {"type": "array", "minItems": 1, "uniqueItems": true, "items": {"type": "string", "pattern": "^F\\d+$"}}
      }
    },
    "conversion": {
      "type": "object",
      "required": ["input_form", "output_form", "drug_extract_ratio", "equivalence"],
      "additionalProperties": false,
      "description": "Dose-FORM arithmetic ONLY. Species-specific traditional and pharmacopoeial dose RANGES stay in plants[].dosage[]. Putting a dose here would let a class-general record imply a species-specific dose.",
      "properties": {
        "input_form": {"type": "string", "enum": ["dried-herb", "fresh-herb", "powdered-drug"]},
        "output_form": {"type": "string", "enum": ["tincture", "fluid-extract", "soft-extract", "dry-extract", "glycerite", "acetous-tincture", "infusion", "decoction", "infused-oil"]},
        "drug_extract_ratio": {"type": "string", "pattern": "^1:\\d+(\\.\\d+)?$"},
        "menstruum_ethanol_pct": {"type": ["number", "null"], "minimum": 0, "maximum": 100},
        "menstruum_glycerol_pct": {"type": ["number", "null"], "minimum": 0, "maximum": 100, "description": "Backs GLYCERITE_MIX 75/25. Glycerol's co-solvent role and its preservation threshold are two different numbers; cite findings for each."},
        "equivalence": {
          "type": "object",
          "required": ["preparation_ml", "dried_herb_g"],
          "additionalProperties": false,
          "properties": {
            "preparation_ml": {"type": "number", "exclusiveMinimum": 0},
            "dried_herb_g": {"type": "number", "exclusiveMinimum": 0},
            "basis": {"type": "string", "enum": ["nominal-ratio", "gravimetric-solids"]}
          }
        },
        "marc_retention_ml_per_g": {"type": ["number", "null"], "minimum": 0}
      }
    }
  }
}
```

## `vocabularies/extraction_classes.yaml`

```yaml
# Omnia Sana — controlled vocabulary: EXTRACTION CLASSES
# Schema: ../schema/practice.schema.json ($defs -> key.extraction_class)
#
# VALUE SPACE ONLY. This is NOT the join key. Practice records are keyed on the
# existing compound ids in ../compounds/, which validate.py already validates as
# the K set. An extraction class is an OPTIONAL disambiguator, authored in two
# places and used only where one compound id spans classes whose solvent optima
# differ: `compounds/<id>.yaml -> extraction_classes[]` and
# `plants/<id>.yaml -> constituents[].extraction_class` (the plant wins).
#
# An extraction class groups constituents that behave the same way in a
# menstruum — same polarity band, same heat and pH tolerance, same volatility.
# It is deliberately not the biosynthetic `class` field: biosynthesis groups
# quercetin with rutin; extraction chemistry splits them, because their optima
# are opposite (70-96% vs 40-60% ethanol).
#
# Degradation rule, and it is the whole reason this file exists:
#   resolution exact        -> join and recommend
#   resolution ambiguous    -> no recommendation, and may never reach approved
#   resolution unresolvable -> do not join at all
# Shipping "no recommendation" for flavonoid is correct. Shipping 70% ethanol
# for a mucilage is not.
#
# `optimal_ethanol_pct` is orientation for the editor choosing what to research,
# [min, max] %v/v in water, or null where the class is not hydroethanol-
# extractable. The number a calculator reads ALWAYS comes from a practice
# record's findings, never from this file.
# `solvents` and `methods` reference ./solvents.yaml and ./extraction_methods.yaml.

- id: volatile-terpenoid
  label: Volatile terpenoids
  category: terpenoid
  optimal_ethanol_pct: [70, 96]
  solvents: [steam, ethanol-water, ethanol-absolute, fixed-oil, supercritical-co2]
  heat_stability: labile
  volatility: high
  glycosidic: false
  compounds: [bisabolol, camphor, chamazulene, cineole, citral, linalool, menthol, sesquiterpene, terpene]
  note: Recovery is governed by vapour pressure, not solvent affinity; water solubility 0.01-1 g/L.

- id: volatile-phenol
  label: Volatile phenols
  category: terpenoid
  optimal_ethanol_pct: [45, 70]
  solvents: [water, ethanol-water, steam]
  heat_stability: moderate
  volatility: moderate
  glycosidic: false
  compounds: [asarone, carvacrol, eugenol, thymol]
  note: A phenolic OH (pKa ~10) gives ~1 g/L water solubility, ~70x the hydrocarbons. Why thyme infusions work and lavender infusions largely do not.

- id: volatile-oil-complex
  label: Essential oil (whole distillable fraction)
  category: terpenoid
  optimal_ethanol_pct: [90, 96]
  solvents: [steam, ethanol-absolute, supercritical-co2]
  heat_stability: labile
  volatility: high
  glycosidic: false
  compounds: [essential-oil]
  note: The distillable fraction as one unit, because that is how the literature reports it — yield against distillation time, not against component.

- id: lipophilic-terpenoid
  label: Lipophilic terpenoids (non-volatile)
  category: terpenoid
  optimal_ethanol_pct: [85, 96]
  solvents: [ethanol-water, ethanol-absolute, fixed-oil, supercritical-co2]
  heat_stability: stable
  volatility: none
  glycosidic: false
  compounds: [boswellic-acid, valerenic-acid, withanolide, sesquiterpene, terpene]
  note: Water-insoluble at any temperature. The class most often silently absent from an aqueous product a user believes contains it.

- id: sesquiterpene-lactone
  label: Sesquiterpene lactones
  category: terpenoid
  optimal_ethanol_pct: [60, 80]
  solvents: [ethanol-water]
  heat_stability: labile
  volatility: none
  glycosidic: false
  compounds: [parthenolide, sesquiterpene-lactone]
  note: The alpha-methylene-gamma-lactone ring opens above ~pH 8 and is a Michael acceptor. Heat and pH limit, not solvent. Several carrying plants (arnica, tanacetum, artemisia) are dose-limited or topical-only.

- id: nonpolar-lipid
  label: Fixed oils and nonpolar lipids
  category: lipid
  optimal_ethanol_pct: null
  solvents: [fixed-oil, supercritical-co2, hexane]
  heat_stability: moderate
  volatility: none
  glycosidic: false
  compounds: [carotenoid, gla, phytosterol]
  note: Not hydroethanol-extractable at any practical concentration. The calculator must be able to state that this constituent is not in the tincture at all.

- id: saponin-glycoside
  label: Saponin glycosides
  category: glycoside
  optimal_ethanol_pct: [50, 70]
  solvents: [water, ethanol-water]
  heat_stability: stable
  volatility: none
  glycosidic: true
  compounds: [escin, ginsenoside, glycyrrhizin, saponin, triterpene-saponin]
  note: Amphiphilic surfactants. They foam, which is a mechanical constraint on percolation, not only a yield number.

- id: flavonoid-glycoside
  label: Flavonoid glycosides
  category: glycoside
  optimal_ethanol_pct: [40, 60]
  solvents: [water, ethanol-water]
  heat_stability: stable
  volatility: none
  glycosidic: true
  compounds: [flavonoid, rutin, apigenin, kaempferol, luteolin, quercetin]
  note: The sugar moiety raises water solubility 10-100x. Slow drying lets endogenous beta-glucosidase convert this class into flavonoid-aglycone.

- id: flavonoid-aglycone
  label: Flavonoid aglycones
  category: glycoside
  optimal_ethanol_pct: [70, 96]
  solvents: [ethanol-water, ethanol-absolute]
  heat_stability: stable
  volatility: none
  glycosidic: false
  compounds: [apigenin, kaempferol, luteolin, quercetin, silymarin, flavonoid]
  note: Same skeleton, opposite optimum. `flavonoid` sits on 132 plants and resolves to either class, so it is ambiguous and unresolved plants get nothing rather than a coin-flip.

- id: anthocyanin
  label: Anthocyanins
  category: glycoside
  optimal_ethanol_pct: [40, 60]
  solvents: [acidified-water, acidified-ethanol-water]
  heat_stability: labile
  volatility: none
  glycosidic: true
  compounds: [anthocyanin]
  note: The flavylium cation is stable only below ~pH 3; half-life is hours at 80 C. The only class whose recommendation must include an acidulant.

- id: anthraquinone-glycoside
  label: Anthraquinone glycosides
  category: glycoside
  optimal_ethanol_pct: [30, 60]
  solvents: [water, ethanol-water]
  heat_stability: stable
  volatility: none
  glycosidic: true
  compounds: [anthraquinone]
  note: Deglycosylate slowly in storage, which is why cascara is aged. Stimulant laxative — the carrying compound is dose-limited and a yield-maximising recommendation is barred.

- id: iridoid-glycoside
  label: Iridoid glycosides
  category: glycoside
  optimal_ethanol_pct: [30, 50]
  solvents: [water, ethanol-water]
  heat_stability: labile
  volatility: none
  glycosidic: true
  compounds: [harpagoside, iridoid-glycoside]
  note: The ring opens to a reactive dialdehyde and polymerises to black pigment. The recommendation is a prohibition — do not acidify, do not decoct.

- id: proanthocyanidin
  label: Proanthocyanidins and flavan-3-ols
  category: phenolic
  optimal_ethanol_pct: [50, 70]
  solvents: [water, ethanol-water, acetone-water]
  heat_stability: moderate
  volatility: none
  glycosidic: false
  compounds: [catechin, proanthocyanidin, tannin]
  note: Heat and acid polymerise to insoluble phlobaphenes; protein binding depresses apparent yield, so a yield without the matrix stated is not comparable.

- id: hydrolysable-tannin
  label: Hydrolysable tannins
  category: phenolic
  optimal_ethanol_pct: [50, 70]
  solvents: [water, ethanol-water]
  heat_stability: labile
  volatility: none
  glycosidic: true
  compounds: [tannin]
  note: Hydrolyse in hot water to gallic and ellagic acid, which then precipitates, so measured yield FALLS with decoction time — the exact opposite of proanthocyanidin. This is why `tannin` (42 plants) cannot join undisambiguated.

- id: phenolic-acid-free
  label: Free phenolic acids
  category: phenolic
  optimal_ethanol_pct: [50, 70]
  solvents: [water, ethanol-water]
  heat_stability: stable
  volatility: none
  glycosidic: false
  compounds: [caffeic-acid, ellagic-acid, ferulic-acid, gallic-acid, phenolic-acid]
  note: Chemically robust; ellagic acid is solubility-limited, which shows as a plateau rather than an optimum.

- id: phenolic-ester-labile
  label: Labile phenolic esters
  category: phenolic
  optimal_ethanol_pct: [50, 70]
  solvents: [ethanol-water]
  heat_stability: moderate
  volatility: none
  glycosidic: true
  compounds: [chlorogenic-acid, rosmarinic-acid, verbascoside, phenolic-acid]
  note: Hydrolysed by endogenous esterase and polyphenol oxidase during wilting. The recommendation is about drying speed and alcohol stabilisation, not solvent.

- id: lipophilic-phenolic-labile
  label: Lipophilic labile phenolics
  category: phenolic
  optimal_ethanol_pct: [80, 96]
  solvents: [ethanol-water, ethanol-absolute, fixed-oil]
  heat_stability: labile
  volatility: none
  glycosidic: false
  compounds: [curcumin, gingerol, hyperforin, hypericin]
  note: Light-, oxygen- and heat-labile. Gingerol-to-shogaol is a measurable heat marker. Hypericin/hyperforin carry photosensitivity and CYP3A4 induction — dose-limited.

- id: coumarin
  label: Coumarins
  category: phenolic
  optimal_ethanol_pct: [60, 80]
  solvents: [ethanol-water]
  heat_stability: moderate
  volatility: slight
  glycosidic: true
  compounds: [coumarin]
  note: Lactone; glycoside-to-aglycone conversion on wilting is the new-mown-hay smell. Hepatotoxic with an EFSA TDI, and furanocoumarins are photoreactive — dose-limited on all 19 carrying plants.

- id: lignan
  label: Lignans
  category: phenolic
  optimal_ethanol_pct: [60, 80]
  solvents: [ethanol-water]
  heat_stability: stable
  volatility: none
  glycosidic: true
  compounds: [arctigenin, lignan]
  note: Moderately lipophilic dimeric phenylpropanoids; the glycosidic forms (arctiin, SDG) sit nearer the flavonoid-glycoside band.

- id: mucilage
  label: Mucilage
  category: polysaccharide
  optimal_ethanol_pct: null
  solvents: [water]
  heat_stability: labile
  volatility: none
  glycosidic: false
  compounds: [mucilage, polysaccharide]
  note: The hardest constraint on a tincture calculator — above ~25-30% ethanol this class is PRECIPITATED, not extracted, and leaves in the marc. Cold water only.

- id: storage-polysaccharide
  label: Storage polysaccharides
  category: polysaccharide
  optimal_ethanol_pct: null
  solvents: [water]
  heat_stability: requires-heat
  volatility: none
  glycosidic: false
  compounds: [inulin, pectin, starch, polysaccharide]
  note: Need the hot water that destroys mucilage, and are recovered by alcohol precipitation rather than alcohol extraction. Inulin is acid-labile.

- id: fungal-beta-glucan
  label: Fungal beta-glucans
  category: polysaccharide
  optimal_ethanol_pct: null
  solvents: [water, alkaline-water]
  heat_stability: requires-heat
  volatility: none
  glycosidic: false
  compounds: [polysaccharide]
  note: Must be liberated from the chitin wall by heat and sometimes alkali; alcohol-insoluble. Justifies dual-extraction. NOTE all seven fungal plant records are currently excluded from recommendations — see practice/README.md.

- id: alkaloid
  label: Alkaloids
  category: alkaloid
  optimal_ethanol_pct: [45, 70]
  solvents: [acidified-ethanol-water, ethanol-water, water]
  heat_stability: moderate
  volatility: slight
  glycosidic: true
  compounds: [alkaloid, berberine]
  note: >-
    Ionisation, not polarity, is the governing variable. CRITICAL: the compound id
    `alkaloid` sits on 17 plants including symphytum, petasites, tussilago,
    borago, chelidonium and arnica, where the alkaloid fraction IS the toxicity
    (pyrrolizidines, chelidonine). A yield-maximising record here instructs a user
    to maximise hepatotoxin recovery. `alkaloid` is flagged avoid-internal in
    compounds/, and no recommendation may be authored on it without a
    limit_rationale and a second reviewer. Berberine is quaternary, permanently
    charged and water-soluble regardless of pH, so the acidified-menstruum logic
    does not apply to it at all.

- id: organosulfur-thiosulfinate
  label: Thiosulfinates (organosulfur)
  category: organosulfur
  optimal_ethanol_pct: null
  solvents: [water, ethanol-water]
  heat_stability: destroyed
  volatility: high
  glycosidic: false
  compounds: [allicin, organosulfur]
  methods: [crush-and-rest, expression]
  note: Allicin does not exist in the intact bulb; alliinase forms it on crushing and it decays in hours, and above ~60 C nothing forms. Process is everything. allium_sativum is excluded from recommendations until its parts_used gains Bulb.

- id: mineral-inert
  label: Inert mineral constituents
  category: mineral
  optimal_ethanol_pct: null
  solvents: [water]
  heat_stability: stable
  volatility: none
  glycosidic: false
  compounds: [silica]
  note: Even long decoction yields only trace soluble silicic acid. Present so the calculator can say "essentially not extracted" rather than say nothing.

- id: polar-small-metabolite
  label: Polar small metabolites
  category: other
  optimal_ethanol_pct: [0, 40]
  solvents: [water, ethanol-water]
  heat_stability: moderate
  volatility: none
  glycosidic: false
  compounds: [allantoin]
  note: Freely water-soluble, no strong solvent preference, labile only at pH extremes.
```

## `vocabularies/solvents.yaml`

```yaml
# Omnia Sana — controlled vocabulary: SOLVENT SYSTEMS
# Schema: ../schema/practice.schema.json ($defs -> key.solvent, conditions.solvent,
# recommendation.solvent). Loaded by scripts/validate.py via vocab_ids() — this is
# the ONLY solvent list. There is no hardcoded copy in validate.py; an earlier
# draft had one with disjoint ids and no safety annotation, and it was deleted.
#
# Ids follow the LITERATURE's naming (ethanol-water), not the herbalist's
# (hydroethanol), because findings transcribe Methods sections verbatim.
#
# A solvent id names a SYSTEM, not a strength. Concentration is a separate
# numeric field: conditions.solvent_pct on a finding, and a [min, max] band on a
# recommendation. A paper reports 63%; a band is a derived editorial judgement
# that must be traceable to several findings.
#
# consumer_safe: false is a HARD GATE in scripts/validate.py, not a label.
# Most published optimisation work uses methanol, acetone or ethyl acetate, and
# it is perfectly good evidence about where a class sits on the polarity scale —
# so findings may cite it freely. A recommendation may not. A bench optimum in
# 80% methanol is a fact about chemistry; it is not something a person puts in a
# jar. Additionally, the extrapolation envelope is partitioned by solvent: a
# methanol sweep can never legitimise an ethanol band.
#
# takes_concentration  — conditions.solvent_pct is REQUIRED (true) or must be
#                        null (false).
# requires_menstruum   — false means solid_liquid_ratio may be 'n-a'.

- id: water
  label: Water
  polarity: high
  consumer_safe: true
  takes_concentration: false
  requires_menstruum: true
  synonyms: ["aqueous", "aqua", "distilled water"]
  note: Cold and hot aqueous extraction alike; temperature is a condition, not a different solvent.

- id: ethanol-water
  label: Ethanol / water (hydroethanol)
  polarity: variable
  consumer_safe: true
  takes_concentration: true
  requires_menstruum: true
  synonyms: ["hydroethanol", "EtOH", "aqueous ethanol", "spirit", "menstruum"]
  note: The workhorse, and the reason concentration is a separate field — the same system spans 20% to 90% and the answer changes completely across that range.

- id: ethanol-absolute
  label: Absolute / near-absolute ethanol
  polarity: low
  consumer_safe: true
  takes_concentration: false
  requires_menstruum: true
  synonyms: ["96% ethanol", "absolute alcohol", "rectified spirit"]
  note: Held separate because at this end any water-dependent class is not merely reduced but excluded.

- id: glycerol-water
  label: Glycerol / water
  polarity: high
  consumer_safe: true
  takes_concentration: true
  requires_menstruum: true
  synonyms: ["glycerite", "glycerin", "hydroglycerol"]
  note: Backs GLYCERITE_MIX 75/25. Glycerol's co-solvent role and its preservation threshold are two distinct numbers; a record conflating them is right for neither.

- id: acidified-water
  label: Acidified water
  polarity: high
  consumer_safe: true
  takes_concentration: false
  requires_menstruum: true
  synonyms: ["citric acid solution", "pH-adjusted water"]
  note: Required for anthocyanins, where flavylium stability below pH 3 governs everything. Record the acidulant and pH in conditions.

- id: acidified-ethanol-water
  label: Acidified ethanol / water
  polarity: variable
  consumer_safe: true
  takes_concentration: true
  requires_menstruum: true
  synonyms: ["acidulated menstruum", "acidified alcohol"]
  note: The classical alkaloid menstruum. Never for iridoid glycosides, which the same acid destroys. Subject to the toxicity gate on every alkaloid-keyed record.

- id: acetic-acid-water
  label: Acetic (vinegar) menstruum
  polarity: high
  consumer_safe: true
  takes_concentration: true
  requires_menstruum: true
  synonyms: ["vinegar", "acetum", "acetous tincture", "oxymel base"]

- id: fixed-oil
  label: Fixed oil
  polarity: low
  consumer_safe: true
  takes_concentration: false
  requires_menstruum: true
  synonyms: ["olive oil", "carrier oil", "infused oil", "oleum"]
  note: The only consumer-accessible route to the nonpolar-lipid class.

- id: steam
  label: Steam / water vapour
  polarity: high
  consumer_safe: true
  takes_concentration: false
  requires_menstruum: false
  synonyms: ["hydrodistillation medium", "steam"]
  note: Strictly a carrier rather than a solvent, but it occupies the solvent slot so the volatile classes have a coherent key row instead of a null.

- id: alkaline-water
  label: Alkaline water
  polarity: high
  consumer_safe: false
  takes_concentration: false
  requires_menstruum: true
  synonyms: ["sodium carbonate solution", "alkali extraction"]
  note: Liberates fungal beta-glucans from chitin and drives alkaloid free bases out of aqueous phase. Not a domestic technique.

- id: supercritical-co2
  label: Supercritical CO2
  polarity: low
  consumer_safe: false
  takes_concentration: false
  requires_menstruum: false
  synonyms: ["scCO2", "SFE"]
  note: Industrial only. Excellent comparative evidence about lipophilic classes; never a recommendation, since no reader can reproduce it.

- id: methanol-water
  label: Methanol / water
  polarity: variable
  consumer_safe: false
  takes_concentration: true
  requires_menstruum: true
  synonyms: ["MeOH", "aqueous methanol"]
  note: Toxic, and the single most common solvent in published phytochemical optimisation. It will appear constantly in findings and must never appear in a recommendation. This is the specific case the gate was written for.

- id: acetone-water
  label: Acetone / water
  polarity: variable
  consumer_safe: false
  takes_concentration: true
  requires_menstruum: true
  synonyms: ["acetone", "70% acetone"]
  note: Standard for proanthocyanidin work; laboratory only.

- id: ethyl-acetate
  label: Ethyl acetate
  polarity: low
  consumer_safe: false
  takes_concentration: false
  requires_menstruum: true
  synonyms: ["EtOAc"]
  note: Fractionation solvent; appears in partition schemes, never in a preparation.

- id: hexane
  label: Hexane
  polarity: nonpolar
  consumer_safe: false
  takes_concentration: false
  requires_menstruum: true
  synonyms: ["n-hexane", "petroleum ether"]
  note: Lipid and carotenoid work. Laboratory only.

- id: chloroform
  label: Chloroform
  polarity: low
  consumer_safe: false
  takes_concentration: false
  requires_menstruum: true
  synonyms: ["trichloromethane"]

- id: dichloromethane
  label: Dichloromethane
  polarity: low
  consumer_safe: false
  takes_concentration: false
  requires_menstruum: true
  synonyms: ["DCM", "methylene chloride"]

- id: none
  label: No solvent
  polarity: n-a
  consumer_safe: true
  takes_concentration: false
  requires_menstruum: false
  synonyms: ["solventless", "neat"]
  note: For process-limited records — expression and crush-and-rest — where the constituent is created or released mechanically and no menstruum is involved. Without this id the allicin record, the design's own headline example, would be unauthorable.
```

## `vocabularies/extraction_methods.yaml`

```yaml
# Omnia Sana — controlled vocabulary: EXTRACTION METHODS
# Schema: ../schema/practice.schema.json ($defs -> key.method, conditions.method,
# recommendation.method). Loaded by scripts/validate.py via vocab_ids() — the ONLY
# method list. The earlier hardcoded copy in validate.py (uae, mae,
# oil-infusion) is deleted.
#
# consumer_reproducible: false is a HARD GATE, matching consumer_safe in
# solvents.yaml. Soxhlet, UAE and MAE produce most of the good comparative yield
# data, so findings cite them freely; a recommendation may not use them. Telling
# a reader that 20 minutes of 40 kHz sonication is optimal is true and useless,
# and putting it on a page next to a jar and a bottle of vodka is worse.
#
# requires_menstruum: false exempts the method from solid_liquid_ratio and from
# conditions.solvent_pct — expression, crush-and-rest and the distillations do
# not have a drug-to-menstruum ratio in any comparable sense.
#
# These ids are also the eventual normalisation target for the 549 existing
# plants[].preparations[].name strings (Infusion, Decoction, Tincture, Poultice).
# That migration is v2; until it runs, the two taxonomies coexist and the plant
# page and the calculator must not be made to look like they disagree.

- id: infusion
  label: Infusion (hot steep)
  category: traditional-domestic
  heat_profile: hot-off-boil
  consumer_reproducible: true
  requires_menstruum: true
  synonyms: ["tea", "tisane", "hot infusion"]
  note: Standard for leaf and flower. The volatile fraction is partly lost unless the vessel is covered — itself a documented, measurable effect.

- id: cold-infusion
  label: Cold infusion (cold macerate)
  category: traditional-domestic
  heat_profile: ambient
  consumer_reproducible: true
  requires_menstruum: true
  synonyms: ["cold macerate", "overnight steep", "cold water extract"]
  note: The only correct method for mucilage, which heat degrades and ethanol precipitates.

- id: decoction
  label: Decoction (simmer)
  category: traditional-domestic
  heat_profile: boiling
  consumer_reproducible: true
  requires_menstruum: true
  synonyms: ["simmer", "decoct"]
  note: Required for storage polysaccharides and fungal beta-glucans; actively harmful for hydrolysable tannins, where yield falls as simmer time rises, and for iridoids, which polymerise.

- id: dual-extraction
  label: Dual extraction (decoction plus tincture, combined)
  category: traditional-domestic
  heat_profile: mixed
  consumer_reproducible: true
  requires_menstruum: true
  synonyms: ["double extraction"]
  note: The standard answer for fungal material, where beta-glucans need hot water and triterpenes need alcohol and neither menstruum alone gets both.

- id: maceration
  label: Maceration
  category: traditional-domestic
  heat_profile: ambient
  consumer_reproducible: true
  requires_menstruum: true
  synonyms: ["steeping", "cold maceration", "jar method", "folk method"]
  note: The default tincture method and the one the site's calculator actually models.

- id: percolation
  label: Percolation
  category: traditional-domestic
  heat_profile: ambient
  consumer_reproducible: true
  requires_menstruum: true
  synonyms: ["cone percolation"]
  note: Higher recovery per unit menstruum than maceration, but saponins foam and mucilage blocks the cone — mechanical constraints that belong in the record, not just yield numbers.

- id: oil-infusion-cold
  label: Cold oil infusion
  category: traditional-domestic
  heat_profile: ambient
  consumer_reproducible: true
  requires_menstruum: true
  synonyms: ["solar infusion", "cold-infused oil"]

- id: oil-infusion-heated
  label: Heated oil infusion
  category: traditional-domestic
  heat_profile: warm
  consumer_reproducible: true
  requires_menstruum: true
  synonyms: ["double-boiler infusion", "warm oil maceration"]

- id: expression
  label: Expression (pressing)
  category: traditional-domestic
  heat_profile: ambient
  consumer_reproducible: true
  requires_menstruum: false
  synonyms: ["cold press", "juicing", "pressing"]
  note: Fresh juice and cold-pressed seed oils. No solvent, no ratio.

- id: crush-and-rest
  label: Crush and rest (enzymatic conversion)
  category: traditional-domestic
  heat_profile: ambient
  consumer_reproducible: true
  requires_menstruum: false
  synonyms: ["chop and wait", "enzymatic activation"]
  note: Not an extraction but the step that creates the constituent — alliinase forms allicin after crushing, and it does not exist in the intact bulb. Without this method id and solvent 'none', the thiosulfinate record has nowhere to put the only variable that matters.

- id: steam-distillation
  label: Steam distillation
  category: industrial
  heat_profile: boiling
  consumer_reproducible: false
  requires_menstruum: false
  synonyms: ["SD", "distillation"]
  note: The reference method for essential-oil yield and the source of most volatile-class comparative data. Home stills exist, but the published yield curves do not reproduce at that scale.

- id: hydrodistillation
  label: Hydrodistillation (Clevenger)
  category: industrial
  heat_profile: boiling
  consumer_reproducible: false
  requires_menstruum: false
  synonyms: ["Clevenger", "HD", "water distillation"]

- id: reflux
  label: Heated reflux
  category: industrial
  heat_profile: boiling
  consumer_reproducible: false
  requires_menstruum: true
  synonyms: ["HRE", "heat-reflux extraction"]

- id: spray-drying
  label: Spray drying
  category: industrial
  heat_profile: hot
  consumer_reproducible: false
  requires_menstruum: false
  synonyms: ["dry extract production"]
  note: Relevant to standardised-extract records and pharmacopoeial drug-extract ratios, not to anything a reader makes.

- id: uae
  label: Ultrasound-assisted extraction
  category: laboratory
  heat_profile: warm
  consumer_reproducible: false
  requires_menstruum: true
  synonyms: ["ultrasound-assisted", "sonication", "ultrasonic bath"]
  note: Produces a large share of the best controlled-comparative solvent data because it makes a full factorial cheap. Cite it; never recommend it. A solvent optimum found under UAE does not automatically transfer to static maceration, and a record assuming it does must say so in the rationale.

- id: mae
  label: Microwave-assisted extraction
  category: laboratory
  heat_profile: hot
  consumer_reproducible: false
  requires_menstruum: true
  synonyms: ["microwave-assisted", "microwave extraction"]

- id: soxhlet
  label: Soxhlet extraction
  category: laboratory
  heat_profile: boiling
  consumer_reproducible: false
  requires_menstruum: true
  synonyms: ["continuous solvent extraction"]
  note: Exhaustive extraction; the usual benchmark other methods are measured against, and thermally brutal to every labile class.

- id: sfe
  label: Supercritical fluid extraction
  category: laboratory
  heat_profile: warm
  consumer_reproducible: false
  requires_menstruum: false
  synonyms: ["scCO2 extraction"]

- id: ple
  label: Pressurised liquid extraction
  category: laboratory
  heat_profile: hot
  consumer_reproducible: false
  requires_menstruum: true
  synonyms: ["PLE", "ASE", "accelerated solvent extraction"]

- id: none
  label: No extraction step
  category: normative
  heat_profile: n-a
  consumer_reproducible: true
  requires_menstruum: false
  synonyms: ["not applicable"]
  note: For dose-form-conversion and normative records, where the fact is arithmetic or definitional and no technique is being asserted.
```

## `practice/README.md`

```markdown
# The applied practice corpus

The second corpus. `plants/` answers *what does this species do in people*;
`practice/` answers *what actually comes out of this material under these
conditions, and how do we know*. It exists because the site's tincture and
formula calculators currently hardcode `PART_RATIOS`, `DEFAULT_RATIO 1:5`,
`GLYCERITE_MIX 75/25` and the `shelfLife` bands in JavaScript with zero
provenance, and an unsourced default is honest only for as long as nobody
pretends otherwise.

One file per record: `practice/<id>.yaml`. Validated against
`../schema/practice.schema.json` — which is a **documentation contract only**.
Nothing in this repo loads JSON Schema. Every rule that actually runs is
imperative Python in `../scripts/validate.py`. If the two disagree, the schema
is the bug.

## The ladder is upside down here

Do not carry clinical instincts across.

| clinical (`TIER_BASE`) | practice (`method_type`) |
| --- | --- |
| review / meta-analysis = 7 | **method-review = 0, and inadmissible in `findings[]`** |
| RCT = 5 | no tier — irrelevant to extraction |
| preclinical bench = 2 | **optimisation = 7** |
| volume of human evidence = bonus | **independent replication = bonus** |
| null results bucketed out | **discordant results stay in and cost points** |

A review of extraction methods scores zero. That is arithmetic, not a slight: it
cannot report a single (solvent, temperature, time, ratio, measured yield)
tuple, because it did not run the experiment. `validate.py` rejects
`method-review` and `traditional-text` inside `findings[]` as a hard error. Put
them in `context_reference_ids[]`, where they inform your prose and contribute
nothing, and go find the primary papers they cite.

`method_type` lives on the **finding**, not on the bibtex entry. One paper can be
`optimisation` for the solvent axis and `characterisation` for temperature, and
reusing an existing clinical `REF-XXXX` in a practice finding requires no edit to
`bibliography.bibtex` at all.

## Anti-skim: what it does and does not do

Every required field was chosen against one test — *could this be fabricated
plausibly by someone who read only the abstract?* `locator.table`,
`comparator_levels` (the **full** level set, not just the winner),
`solid_liquid_ratio`, `quantification`, `unit_basis` and `reference_standard`
are all Methods-and-Results data.

Be honest about what that buys. These fields are checked **against each other**,
so a determined fabricator satisfies them all from one imagined number. What the
design actually delivers is **auditability**: a wrong `Table 3` is checkable by a
second reader in thirty seconds. Two fields make that real, and they are
required at `approved`:

- `fulltext_source` — where the PDF came from. There is no value meaning
  "abstract only", because an abstract cannot produce a finding.
- `verified_by` + `verified_date`, which **must differ from `reviewed_by`**. A
  second person opened the papers.

Do not describe this corpus as making fabrication impossible. It makes it
auditable, and it makes carelessness detectable.

## The three hard gates

1. **Solvent.** `recommendation.solvent` is required. The extrapolation envelope
   is built only from findings in the **same solvent** varying the **same
   parameter**. A methanol sweep of 20/40/60/80 does not legitimise an ethanol
   band of 60-75. Findings in lab solvents are welcome — they are good evidence
   about polarity — but `consumer_safe: false` in `../vocabularies/solvents.yaml`
   is a hard error on a recommendation, as is `consumer_reproducible: false` in
   `extraction_methods.yaml`.
2. **Toxicity.** A recommendation is a preparation that is safe and
   traditionally correct. It is **never the argmax of a yield table**. Any record
   whose `key.compound_id` carries a non-`none` `toxicity_flag` needs a
   `limit_rationale` and a second reviewer. This is not theoretical: `alkaloid`
   sits on 17 plants including comfrey, butterbur, coltsfoot, borage,
   greater celandine and arnica, where the alkaloid fraction *is* the toxicity.
   `coumarin` sits on 19. `recommendation.route` (`internal` | `topical`) is
   required, and arnica is the reason.
3. **Copyright.** Pharmacopoeial monographs are paywalled normative texts. Cite
   `locator.edition` + `locator.monograph`, paraphrase the requirement in one
   sentence in `statement_summary` (≤300 chars, enforced), and never populate
   `abstract` on a `kind: standard` bibliography entry — the Knowledge Finder
   renders `abstract` *as the source's own words*.

## What v1 does not do

- **`key.part` is frozen to `null`.** `plants[].parts_used` is 58 distinct
  free-text strings with no enum and no validation rule, and `constituents[]`
  carries no part attribution at all, so the part axis cannot be populated from
  plant data. `validate.py` rejects any non-null value. `PART_RATIOS` stays
  hardcoded and labelled unsourced. There is no `vocabularies/parts.yaml`.
- **The calculator never emits a single menstruum.** Chamomile flower carries
  mucilage (cold water; ethanol above ~30% precipitates it) *and* bisabolol
  (70-96% ethanol). Both records are correct and they disagree. The output is a
  **per-constituent table** plus the standing line *"a tincture captures the
  volatile fraction and loses the mucilage"* — never one number. Thirteen plants
  have this collision today.
- **A plant gets a recommendation only when it opts in by resolving.** The
  constituent must resolve unambiguously to one `extraction_class`, and the
  keyed compound's `toxicity_flag` must be `none`. Absent, ambiguous or
  unresolvable → nothing. `flavonoid` (132 plants), `tannin` (42),
  `polysaccharide` (36), `glycoside`, `phenolic-compound` and `terpene` are all
  ambiguous until disambiguated on the compound record or on
  `plants[].constituents[].extraction_class`.
- **Eight plant records are excluded outright** by `PRACTICE_PLANT_EXCLUSIONS`
  in `build.py`, because their data would join wrongly: the seven fungal records
  that declare `Whole Plant` (`trametes_versicolor`, `psilocybe_cubensis`,
  `pleurotus_ostreatus`, `lentinula_edodes`, `inonotus_obliquus`,
  `ganoderma_lingzhi`, `cordyceps_militaris`) and `allium_sativum`, which lacks
  `Bulb` entirely while carrying `allicin`.

## Species scope

`species-specific` — invariant 2 unchanged. Every finding's binomial must match
the record's. A *Silybum eburneum* paper on a *Silybum marianum* record is the
same error it has always been.

`class-general` — the claim is about a class of molecule in a kind of matrix, so
a *Taraxacum* flavonoid solvent curve is legitimate evidence. Rejecting
off-species data here would reject the corpus wholesale. But generalising is
never silent: `generalisation.basis`, a `rationale` a chemist could disagree
with (≥80 chars, enforced), and ≥2 genera before `approved`. `source_taxa` is
**derived** from `findings[].material.species` in `build.py` — do not author it.
`excluded_taxa` *is* authored, and these are the species that break their class
and are invisible in an abstract: *Allium sativum* (process-limited,
alliinase-dependent), *Berberis*/*Mahonia* (berberine is quaternary and
water-soluble regardless of pH), *Hericium erinaceus* (its part reads `Fruit`,
meaning fruiting body), *Hypericum perforatum* (hyperforin degrades on a
maceration timescale), anything mucilaginous.

## Discordance is data

A paper measuring the optimum at 85% when your band says 60-75 is not a null; it
is a measurement of your parameter that disagrees with you. It stays in
`findings[]`, it lowers the score, and at `approved` it needs a
`discordance_note`. Deleting it to lift a score is falsifying the grade. Do not
widen a band to swallow an outlier either — a widened band is a one-line diff a
reviewer will ask about, and there is no tolerance parameter.

## Draft → approved

Same shape as `drug_class_interactions`. Only `approved` reaches
`build/practice.v1.json`; drafts go to `build/practice.v1.draft.json`, which is
gitignored by `build/*.draft.json` and therefore never reaches `osdb/main` or the
site. `approved` requires:

- method-confidence index ≥ 5;
- ≥ 2 **independent** groups (first-author surname, or issuing authority for
  pharmacopoeias) — **except** for `parameter_kind: normative`, where one
  authority suffices provided `recommendation.jurisdiction` is set and the
  statement is jurisdiction-scoped. A definition needs no replication;
  disagreement between Ph. Eur. and USP is expressed as two scoped records, not
  one contested one;
- for `empirical`, ≥1 `optimisation` or `comparative-bench` finding **in the
  recommended solvent, varying the recommended parameter**;
- a finding whose conditions are `unspecified` may not be the sole support;
- `reviewed_by` + `reviewed_date`, and `verified_by` + `verified_date` by a
  different person;
- `discordance_note` if any admissible finding falls outside the band;
- `limit_rationale` if the keyed compound is toxicity-flagged;
- for `class-general`, ≥2 genera and a reviewed `generalisation` block.

A record with a non-empty `avoid[]` may be approved with **no recommendation at
all**. A precaution should be cheaper to assert than an instruction: the cost of
a wrong precaution is a suboptimal extract, and the cost of a wrong instruction
is somebody drinking it for two years.

## Presentation

Rendered as a **word plus a four-segment bar** under the heading *Method
confidence*: `established` / `supported` / `provisional` / `insufficient`. Never
the clinical ten dots, never "N/10", never the word "evidence". The emitted
object carries `"scale": "omnia-sana/method-confidence@1"` and **never a key
named `evidence`**, so a renderer written against the clinical contract finds
nothing and renders nothing rather than the wrong thing.

The reason is worth internalising rather than obeying. A user who has learned
that ten dots means *strong human evidence this plant works* will read ten dots
on an extraction record as exactly that — when it means *three labs agree about
a solvent percentage* and says nothing whatever about whether the plant works.
The two can sit a few hundred pixels apart on the same page. This project has
already shipped one two-scale confusion: 918 of 1,696 live claims displayed an
inflated evidence label for four weeks while every sync reported success.

## Finishing

    python scripts/validate.py
    python scripts/build.py

Then `osdb-verify-integrity` after a large batch, and `osdb-deploy` to publish.
One standing warning for integrity passes: **never delete a bibliography entry
whose derived `corpus` includes `practice`** on the strength of an orphan
warning.
```

---

# 3. FILES TO MODIFY — exact old/new pairs

Verified against the live tree. All line references re-checked; where the drafts quoted line numbers I quote text instead so the edits apply regardless of drift.

**Canonical record shape decision (required before any of this applies).** The two upstream drafts define incompatible finding shapes. These edits implement **Draft B's shape** (`record_type`, `parameter_kind`, `key`, `species_scope`, `findings[].{locator,material,conditions,outcome}`, `recommendation`), with three corrections forced by the refutations:
- `method_type` lives **on the finding**, not on the bibtex entry (refutation #14 — it is per-axis by definition, and putting it on the entry hard-errors every reuse of an existing clinical REF).
- `recommendation.solvent` and `recommendation.method` are **required**, and gated against `consumer_safe` / `consumer_reproducible` (refutation-2 #1).
- `corpus` is **derived** in build.py and **not** validated (refutation-2 #8).

---

## 3.1 `scripts/validate.py`

### Edit A — module constants

OLD (verbatim, lines 22–37):
```python
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLANTS = os.path.join(ROOT, "plants")
VOCAB = os.path.join(ROOT, "vocabularies")
COMPDIR = os.path.join(ROOT, "compounds")
NAMESDIR = os.path.join(ROOT, "names")
BIB = os.path.join(ROOT, "bibliography.bibtex")

REF_RE = re.compile(r"REF-\d{4,}")
SLUG = re.compile(r"^[a-z0-9-]+$")
STATUSES = {"verified", "draft", "needs-review"}
SAFETY_STATUSES = {"draft", "approved"}
SEVERITIES = {"avoid", "caution", "likely-safe", "insufficient"}
PAIR_TYPES = {"synergy", "neutral", "caution", "avoid"}
LOOKALIKE_SEVERITIES = {"fatal", "dangerous", "irritant", "caution"}
LOOKALIKE_OUTCOMES = {"none-known", "has-lookalikes"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
```

NEW — append after the block (do not alter existing lines):
```python
PRACTICEDIR = os.path.join(ROOT, "practice")

# REF_RE above is UNANCHORED and is used with .findall() on prose. Do not reuse it
# with .match() — "REF-0481-typo" would pass. This is the anchored twin.
REF_EXACT_RE = re.compile(r"^REF-\d{4,}$")

# ---- practice corpus (practice/**/*.yaml) -----------------------------------
# The record-shape enums. The SOLVENT and METHOD vocabularies are NOT here: they
# are loaded from vocabularies/solvents.yaml and vocabularies/extraction_methods.yaml
# so that consumer_safe / consumer_reproducible travel with the id. A second
# hardcoded copy is how the safety flags get silently lost.
PRACTICE_RECORD_TYPES = {"extraction", "dose-form-conversion", "harvest-timing",
                         "identification", "cultivation", "post-harvest"}
PRACTICE_TYPES_LIVE = {"extraction", "dose-form-conversion"}
PARAMETER_KINDS = {"empirical", "normative"}
SPECIES_SCOPES = {"class-general", "species-specific"}
GENERALISATION_BASES = {"physicochemical", "matrix-analogous"}
LOCATOR_SECTIONS = {"methods", "results", "table", "figure", "supplementary"}
MATERIAL_STATES = {"fresh", "dried", "freeze-dried", "frozen", "unspecified"}
VARIED_FACTORS = {"solvent_pct", "temperature_c", "time_min", "solid_liquid_ratio",
                  "ph", "particle_size_mm", "method", "none"}
DOE_DESIGNS = {"rsm-ccd", "rsm-bbd", "factorial", "taguchi", "mixture", "multi-level-sweep"}
QUANTIFICATION = {"hplc-dad", "hplc-ms", "uplc-ms", "gc-ms", "gc-fid", "lc-nmr",
                  "uv-vis-spectrophotometry", "gravimetric", "titrimetric",
                  "folin-ciocalteu", "aluminium-chloride", "dpph", "frap", "none-declared"}
OUTCOME_UNITS = {"mg-per-g-dw", "mg-gae-per-g-dw", "mg-qe-per-g-dw", "mg-re-per-g-dw",
                 "mg-per-g-fw", "pct-wv", "pct-ww", "pct-yield", "ml-per-100g",
                 "g-per-100g", "mg-per-ml", "ug-per-ml", "mg-per-100g"}
AUTHORITIES = {"ph-eur", "usp", "bhp", "ahp", "bp", "who-monographs", "escop"}
RATIO_RE = re.compile(r"^1:\d+(\.\d+)?$")
BINOMIAL_RE = re.compile(r"^[A-Z][a-z]+ [a-z][a-z-]+$")
# Wide, generous magnitude bands. Job is to catch a fabricated order of magnitude,
# not to referee analytical chemistry.
UNIT_RANGE = {"mg-per-g-dw": (1e-4, 900), "mg-gae-per-g-dw": (1e-4, 900),
              "mg-qe-per-g-dw": (1e-4, 900), "mg-re-per-g-dw": (1e-4, 900),
              "mg-per-g-fw": (1e-4, 900), "pct-wv": (1e-4, 100), "pct-ww": (1e-4, 100),
              "pct-yield": (1e-4, 100), "ml-per-100g": (1e-4, 100),
              "g-per-100g": (1e-4, 100), "mg-per-ml": (1e-4, 1000),
              "ug-per-ml": (1e-3, 1e6), "mg-per-100g": (1e-3, 90000)}
# Methods with no menstruum: the condition tuple does not apply and requiring it
# would make the thiosulfinate and expression records unauthorable.
NO_MENSTRUUM_METHODS = {"expression", "crush-and-rest", "steam-distillation",
                        "hydrodistillation"}
```

### Edit B — a vocabulary loader that keeps the whole record

OLD:
```python
def vocab_ids(path):
    return {x["id"] for x in yaml.safe_load(open(path, encoding="utf-8"))}
```
NEW:
```python
def vocab_ids(path):
    return {x["id"] for x in yaml.safe_load(open(path, encoding="utf-8"))}


def vocab_map(path):
    """id -> whole record. vocab_ids() discards every field but the id, which is
    fine for actions/conditions but not for solvents and methods, where the
    consumer_safe / consumer_reproducible flags ARE the gate."""
    return {x["id"]: x for x in yaml.safe_load(open(path, encoding="utf-8"))}
```

### Edit C — load the practice vocabularies + the practice ladder

OLD:
```python
    D = vocab_ids(os.path.join(VOCAB, "drug_classes.yaml"))
    X = vocab_ids(os.path.join(VOCAB, "dangerous_plants.yaml"))
```
NEW:
```python
    D = vocab_ids(os.path.join(VOCAB, "drug_classes.yaml"))
    X = vocab_ids(os.path.join(VOCAB, "dangerous_plants.yaml"))
    # Practice-corpus vocabularies. Loaded unconditionally, exactly like the five
    # above — a missing file is an unhandled FileNotFoundError that kills the gate,
    # so these YAML files and this line must land in the SAME commit.
    SOLV = vocab_map(os.path.join(VOCAB, "solvents.yaml"))
    METH = vocab_map(os.path.join(VOCAB, "extraction_methods.yaml"))
    XCLS = vocab_ids(os.path.join(VOCAB, "extraction_classes.yaml"))
    PARTS = vocab_ids(os.path.join(VOCAB, "parts.yaml"))
```

Immediately above `def main():` (i.e. after `vocab_map`), add the ladder import:
```python
# The practice evidence ladder is DEFINED ONCE, in scripts/build.py, and imported
# here so the gate and the published score can never drift. build.py guards main()
# behind __main__, so this import has no side effects.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import (PRACTICE_METHOD_TYPES, PRACTICE_FINDING_TIERS, PRACTICE_TIER_BASE,
                   ADMISSIBLE_TIERS, practice_finding_rows, practice_score_from_rows,
                   practice_band, practice_n_independent)  # noqa: E402
```

### Edit D — the practice loop, the crash guard, and the orphan fix

OLD (verbatim — this is the accounting block; the loop goes immediately **above** it):
```python
    missing = sorted(cited - declared)
    orphan = sorted(declared - cited)
```
NEW:
```python
    # ---- practice corpus (practice/**/*.yaml) ----------------------------------
    # Must run AFTER the plants loop (needs seen_ids) and BEFORE the missing/orphan
    # arithmetic below.
    bib_fields = {}
    try:
        from build import parse_bibtex as _pb
        bib_fields = {e["ref_id"]: e["fields"] for e in _pb(open(BIB, encoding="utf-8").read()) if e["ref_id"]}
    except Exception as exc:                      # never let the practice layer kill the plants gate
        warnings.append(f"practice: could not parse bibliography for method_type checks ({exc})")

    practice_files = sorted(glob.glob(os.path.join(PRACTICEDIR, "**", "*.yaml"), recursive=True))
    seen_practice_ids, practice_plant_refs = {}, []
    for path in practice_files:
        nm = "practice/" + os.path.relpath(path, PRACTICEDIR).replace("\\", "/")
        try:
            rec = yaml.safe_load(open(path, encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{nm}: YAML parse failed: {exc}")
            continue
        if not isinstance(rec, dict):
            errors.append(f"{nm}: not a mapping")
            continue

        # THE ORPHAN FIX. cited.update(find_refs(d)) is called exactly once today,
        # inside the plants loop. Without the mirror below, every REF cited only by a
        # practice record reports as "orphan reference (never cited)" — a WARNING, so
        # the build stays green — and osdb-verify-integrity's documented remediation
        # is to delete the bibliography entry. find_refs() walks the whole record and
        # already skips internal_notes via PROSE_KEYS, so it catches findings[],
        # context_reference_ids[], references[], normative_citations[] and the whole
        # species-override subtree. Do NOT hand-enumerate ref fields — hand
        # enumeration is what broke this in the first place.
        cited.update(find_refs(rec))

        rid = rec.get("id")
        if rid:
            if not re.match(r"^[a-z0-9-]+(--[a-z0-9-]+)*$", str(rid)):
                errors.append(f"{nm}: bad practice id '{rid}'")
            if rid in seen_practice_ids:
                errors.append(f"{nm}: duplicate practice id '{rid}' (also {seen_practice_ids[rid]})")
            seen_practice_ids[rid] = nm

        # CRASH GUARD. One malformed record must be one error line, not a dead gate.
        # A traceback here takes down the hard gate for the whole repo, and the
        # editor's fastest way out is to delete the record — which, for a DISCORDANT
        # finding, is exactly the deletion the corpus exists to prevent.
        try:
            check_practice_record(nm, rec, seen_ids, SOLV, METH, XCLS, PARTS,
                                  bib_fields, practice_plant_refs, errors, warnings)
        except Exception as exc:
            errors.append(f"{nm}: crashed during validation ({type(exc).__name__}: {exc}) "
                          f"— fix the record shape; do not delete findings to make it pass")

    for (nm, pid) in practice_plant_refs:
        if pid not in seen_ids:
            errors.append(f"{nm}: species override plant_id '{pid}' has no plant record")

    missing = sorted(cited - declared)
    orphan = sorted(declared - cited)
```

### Edit D2 — the checker (new module-level function, place after `vocab_map`)

```python
def _num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def check_practice_record(nm, rec, plant_ids, SOLV, METH, XCLS, PARTS,
                          bib_fields, plant_refs, errors, warnings):
    """Every rule the JSON Schema *documents* but cannot enforce.

    schema/*.json is loaded by NOTHING — there is no `import jsonschema` anywhere
    in scripts/. Every "required", "minItems", "false" and "const" in
    practice.schema.json is inert documentation. This function is the enforcement.
    """
    for k in ("id", "record_type", "parameter_kind", "species_scope",
              "recommendation", "status", "last_updated"):
        if k not in rec:
            errors.append(f"{nm}: missing required field '{k}'")
    rt = rec.get("record_type")
    if rt not in PRACTICE_RECORD_TYPES:
        errors.append(f"{nm}: record_type '{rt}' invalid (want {sorted(PRACTICE_RECORD_TYPES)})")
    elif rt not in PRACTICE_TYPES_LIVE:
        errors.append(f"{nm}: record_type '{rt}' is RESERVED — no record may be authored "
                      f"under it until its schema branch and rules exist")
    kind = rec.get("parameter_kind")
    if kind not in PARAMETER_KINDS:
        errors.append(f"{nm}: parameter_kind '{kind}' invalid (want {sorted(PARAMETER_KINDS)})")
    if not DATE_RE.match(str(rec.get("last_updated", ""))):
        errors.append(f"{nm}: bad last_updated '{rec.get('last_updated')}'")
    if rec.get("status") not in SAFETY_STATUSES:
        errors.append(f"{nm}: status '{rec.get('status')}' invalid (want draft|approved)")

    key = rec.get("key")
    if rt == "extraction":
        if not isinstance(key, dict):
            errors.append(f"{nm}: extraction record needs a key{{}} block")
            key = {}
        if key.get("extraction_class") not in XCLS:
            errors.append(f"{nm}: key.extraction_class '{key.get('extraction_class')}' "
                          f"not in vocabularies/extraction_classes.yaml")
        part = key.get("part")
        if part is not None and part not in PARTS:
            errors.append(f"{nm}: key.part '{part}' not in vocabularies/parts.yaml "
                          f"(use null for the class-level default)")
        if key.get("solvent") not in SOLV:
            errors.append(f"{nm}: key.solvent '{key.get('solvent')}' not in vocabularies/solvents.yaml")
        if key.get("method") not in METH:
            errors.append(f"{nm}: key.method '{key.get('method')}' not in vocabularies/extraction_methods.yaml")

    findings = rec.get("findings")
    if findings is None:
        findings = []
    if not isinstance(findings, list):
        errors.append(f"{nm}: findings must be a list")
        findings = []
    for i, fi in enumerate(findings):
        if isinstance(fi, dict):
            _check_finding(nm, fi, i, SOLV, METH, PARTS, errors, warnings)
        else:
            errors.append(f"{nm}: findings[{i}] is not a mapping")
    for ov in (rec.get("species_overrides") or []):
        if isinstance(ov, dict):
            plant_refs.append((nm, ov.get("plant_id")))

    _check_recommendation(nm, rec, findings, SOLV, METH, errors, warnings)
    _check_scope(nm, rec, findings, plant_ids, errors, warnings)
    _check_copyright(nm, rec, errors)
    if rec.get("status") == "approved":
        _check_approval(nm, rec, findings, bib_fields, errors)


def _check_finding(nm, fi, i, SOLV, METH, PARTS, errors, warnings):
    tag = f"{nm}: findings[{i}] ({fi.get('ref_id', 'no-ref')})"
    if not REF_EXACT_RE.match(str(fi.get("ref_id", ""))):
        errors.append(f"{tag}: bad or missing ref_id")
    mt = (fi.get("method_type") or "").strip().lower()
    if mt not in PRACTICE_METHOD_TYPES:
        errors.append(f"{tag}: method_type '{mt}' invalid (want {sorted(PRACTICE_METHOD_TYPES)}). "
                      f"It lives on the FINDING, not on the bibtex entry: the same paper is "
                      f"'optimisation' for the solvent axis and 'characterisation' for temperature.")
        return
    tier = PRACTICE_METHOD_TYPES[mt]
    if tier not in PRACTICE_FINDING_TIERS:
        errors.append(f"{tag}: tier '{tier}' may not carry a finding — a review or textbook "
                      f"reports no single (solvent, temperature, time, ratio, yield) tuple. "
                      f"Move it to context_reference_ids[].")
        return

    loc = fi.get("locator") or {}
    if loc.get("section") not in LOCATOR_SECTIONS:
        errors.append(f"{tag}: locator.section '{loc.get('section')}' invalid")
    if tier == "pharmacopoeial":
        for k in ("monograph", "edition"):
            if not str(loc.get(k, "")).strip():
                errors.append(f"{tag}: pharmacopoeial finding needs locator.{k} "
                              f"(cite the coordinates; NEVER reproduce the text)")
        if fi.get("authority") not in AUTHORITIES:
            errors.append(f"{tag}: pharmacopoeial finding needs authority (want {sorted(AUTHORITIES)})")
    else:
        if not (str(loc.get("table", "")).strip() or str(loc.get("figure", "")).strip()):
            errors.append(f"{tag}: needs locator.table or locator.figure — an abstract has no "
                          f"tables, so this is the field a second reader can check in 30 seconds")
        if loc.get("section") not in ("results", "table", "figure", "supplementary"):
            errors.append(f"{tag}: a measured value must be located in results/table/figure/supplementary")
        if not isinstance(loc.get("page"), int):
            warnings.append(f"{tag}: no locator.page — makes audit slower")

    mat = fi.get("material") or {}
    sp = str(mat.get("species", "")).strip()
    if not BINOMIAL_RE.match(sp):
        errors.append(f"{tag}: material.species '{sp}' is not 'Genus species' — record the "
                      f"binomial the paper actually printed, not the one you wanted")
    if mat.get("part") not in PARTS:
        errors.append(f"{tag}: material.part '{mat.get('part')}' not in vocabularies/parts.yaml")
    if mat.get("state") not in MATERIAL_STATES:
        errors.append(f"{tag}: material.state '{mat.get('state')}' invalid")
    if tier == "pharmacopoeial":
        return                                     # a norm has no experimental conditions

    co = fi.get("conditions") or {}
    meth = co.get("method")
    if meth not in METH:
        errors.append(f"{tag}: conditions.method '{meth}' not in vocabularies/extraction_methods.yaml")
    solv = co.get("solvent")
    needs_menstruum = meth not in NO_MENSTRUUM_METHODS
    if needs_menstruum:
        if solv not in SOLV:
            errors.append(f"{tag}: conditions.solvent '{solv}' not in vocabularies/solvents.yaml")
        else:
            declared_pct = SOLV[solv].get("ethanol_pct", "absent")
            pct = co.get("solvent_pct")
            if declared_pct is None and not _num(pct):
                errors.append(f"{tag}: solvent '{solv}' is a variable-strength system and "
                              f"requires a numeric solvent_pct")
            if _num(pct) and not (0 <= pct <= 100):
                errors.append(f"{tag}: solvent_pct {pct} out of range 0-100")
    for k in ("temperature_c", "time_min", "solid_liquid_ratio"):
        v = co.get(k, "__absent__")
        if v == "__absent__":
            errors.append(f"{tag}: conditions.{k} is required (use null and accept the grade cap "
                          f"if the paper genuinely omits it) — silent absence is the signature "
                          f"of an abstract-only read")
        elif v is None:
            warnings.append(f"{tag}: conditions.{k} is null — this finding cannot be the sole "
                            f"support for an approved recommendation")
    t, tm = co.get("temperature_c"), co.get("time_min")
    if _num(t) and not (-80 <= t <= 250):
        errors.append(f"{tag}: temperature_c {t} out of range -80..250")
    if _num(tm) and not (0.5 <= tm <= 20160):
        errors.append(f"{tag}: time_min {tm} out of range 0.5-20160")
    slr = co.get("solid_liquid_ratio")
    if slr is not None and needs_menstruum:
        if not RATIO_RE.match(str(slr)):
            errors.append(f"{tag}: solid_liquid_ratio '{slr}' must be written '1:N' (g:mL)")
        else:
            n = float(str(slr).split(":")[1])
            if not (2 <= n <= 200):
                errors.append(f"{tag}: solid:liquid 1:{n:g} outside the plausible 1:2-1:200 band")
    ph = co.get("ph")
    if ph is not None and not (_num(ph) and 0 <= ph <= 14):
        errors.append(f"{tag}: conditions.ph {ph} out of range 0-14")

    out = fi.get("outcome") or {}
    if len(str(out.get("analyte", "")).strip()) < 3:
        errors.append(f"{tag}: outcome.analyte is required — 'significantly higher' is an "
                      f"abstract; a named analyte is a Results table")
    q = out.get("quantification")
    if q not in QUANTIFICATION:
        errors.append(f"{tag}: outcome.quantification '{q}' invalid")
    elif q == "none-declared":
        errors.append(f"{tag}: quantification 'none-declared' cannot back a recommendation")
    v, u = out.get("value"), out.get("unit")
    if not (_num(v) and v > 0):
        errors.append(f"{tag}: outcome.value must be a positive number (got {v!r})")
    if u not in OUTCOME_UNITS:
        errors.append(f"{tag}: outcome.unit '{u}' invalid — an equivalence unit without its "
                      f"reference standard is not a unit")
    elif _num(v):
        lo, hi = UNIT_RANGE[u]
        if not (lo <= v <= hi):
            errors.append(f"{tag}: outcome.value {v} implausible for '{u}' (expect {lo}-{hi})")

    vf = fi.get("varied_factor")
    if vf not in VARIED_FACTORS:
        errors.append(f"{tag}: varied_factor '{vf}' invalid")
    levels = [x for x in (out.get("comparator_levels") or []) if _num(x)]
    need = 3 if tier == "optimisation" else 2 if tier == "comparative-bench" else 0
    if tier == "optimisation" and fi.get("design") not in DOE_DESIGNS:
        errors.append(f"{tag}: method_type 'optimisation' requires design in {sorted(DOE_DESIGNS)}")
    opt = out.get("optimum_level")
    if need:
        if vf == "none":
            errors.append(f"{tag}: tier '{tier}' asserts a factor was varied but varied_factor is 'none'")
        if len(levels) < need:
            errors.append(f"{tag}: tier '{tier}' requires >={need} comparator_levels (the FULL set "
                          f"the Methods say was tested); got {len(levels)}")
        if opt is None and not str(out.get("optimum_value", "")).strip():
            errors.append(f"{tag}: a comparative finding must record which level won")
        if _num(opt) and levels and opt not in levels:
            errors.append(f"{tag}: optimum_level {opt} is not a member of comparator_levels "
                          f"{levels} — that is what a guessed level set looks like")
        if _num(opt) and vf in ("solvent_pct", "temperature_c", "time_min", "ph"):
            here = co.get(vf)
            if _num(here) and here != opt:
                errors.append(f"{tag}: varied_factor '{vf}' optimum is {opt} but conditions "
                              f"record {here} — best condition and run condition disagree")
    elif tier == "characterisation" and (opt is not None or out.get("optimum_value")):
        errors.append(f"{tag}: a single-condition characterisation cannot report an optimum")
```

### Edit D3 — recommendation gate (the safety-critical half)

```python
def _check_recommendation(nm, rec, findings, SOLV, METH, errors, warnings):
    """Two things the drafts left out and that are the difference between
    'use 60-70% ethanol' and 'use 80% methanol'.

    1. recommendation.solvent is REQUIRED and gated on consumer_safe. A bare band
       {parameter: solvent_pct, range: [60,75]} derived entirely from methanol
       sweeps renders in an ethanol calculator as 'use 60-75% ethanol'.
    2. The swept envelope is partitioned BY SOLVENT and BY PARAMETER. Pooling all
       comparator_levels lets a temperature sweep of 40-80 C legitimise a solvent
       band of 60-75%, which defeats the one check advertised as stopping
       extrapolation.
    """
    r = rec.get("recommendation")
    if not isinstance(r, dict) or not r:
        errors.append(f"{nm}: recommendation is required and must be a mapping")
        return
    param = r.get("parameter")
    if not param:
        errors.append(f"{nm}: recommendation.parameter is required")

    if rec.get("record_type") == "extraction":
        rs, rm = r.get("solvent"), r.get("method")
        if rs not in SOLV:
            errors.append(f"{nm}: recommendation.solvent '{rs}' missing or not in "
                          f"vocabularies/solvents.yaml — a band with no named solvent is "
                          f"rendered by the calculator as an ETHANOL band whatever was tested")
        elif SOLV[rs].get("consumer_safe") is not True:
            errors.append(f"{nm}: recommendation.solvent '{rs}' is consumer_safe: false. "
                          f"Findings may cite methanol/acetone/scCO2 freely; a recommendation "
                          f"may not. A bench optimum is a fact about chemistry, not something "
                          f"a person should put in a jar.")
        if rm not in METH:
            errors.append(f"{nm}: recommendation.method '{rm}' missing or not in "
                          f"vocabularies/extraction_methods.yaml")
        elif METH[rm].get("consumer_reproducible") is not True:
            errors.append(f"{nm}: recommendation.method '{rm}' is consumer_reproducible: false "
                          f"— telling a reader 20 min of 40 kHz sonication is optimal is true "
                          f"and useless")

    rng = r.get("range")
    if rng is None and r.get("value") is None:
        errors.append(f"{nm}: recommendation needs range[lo,hi] or a categorical value")
        return
    if rng is None:
        return
    # SHAPE FIRST, then arithmetic. range: ['a','b'] or [60] must be one error line,
    # not a TypeError/ValueError that kills the gate for the whole repo.
    if not (isinstance(rng, list) and len(rng) == 2 and all(_num(x) for x in rng)):
        errors.append(f"{nm}: recommendation.range must be [lo, hi], two numbers (got {rng!r})")
        return
    lo, hi = rng
    if lo > hi:
        errors.append(f"{nm}: recommendation.range {rng} has lo > hi")
        return
    if param == "solvent_pct" and not (0 <= lo and hi <= 100):
        errors.append(f"{nm}: recommendation.range {rng} outside 0-100 for solvent_pct")

    rs = r.get("solvent")
    swept, optima = [], []
    for fi in findings:
        if not isinstance(fi, dict) or fi.get("varied_factor") != param:
            continue                            # a temperature sweep says nothing about a % band
        if param == "solvent_pct" and (fi.get("conditions") or {}).get("solvent") != rs:
            continue                            # methanol optima do not transfer to ethanol
        out = fi.get("outcome") or {}
        swept += [x for x in (out.get("comparator_levels") or []) if _num(x)]
        if _num(out.get("optimum_level")):
            optima.append(out["optimum_level"])
    if not swept:
        errors.append(f"{nm}: no finding varies '{param}' in solvent '{rs}' — nothing was swept "
                      f"on the recommended axis, so nothing supports a band")
        return
    if not (min(swept) <= lo and hi <= max(swept)):
        errors.append(f"{nm}: recommendation.range {rng} extrapolates beyond the tested envelope "
                      f"[{min(swept)}, {max(swept)}] on this axis and solvent")
    if optima and not any(lo <= x <= hi for x in optima):
        errors.append(f"{nm}: no cited optimum falls inside {rng}. Widen the band in a visible "
                      f"one-line diff or fix the band — there is no tolerance parameter")
```

### Edit D4 — scope, copyright, approval

```python
def _check_scope(nm, rec, findings, plant_ids, errors, warnings):
    scope = rec.get("species_scope")
    if scope not in SPECIES_SCOPES:
        errors.append(f"{nm}: species_scope '{scope}' invalid (want {sorted(SPECIES_SCOPES)})")
        return
    found = sorted({str((fi.get("material") or {}).get("species", "")).strip()
                    for fi in findings if isinstance(fi, dict)
                    and str((fi.get("material") or {}).get("species", "")).strip()})
    if scope == "species-specific":
        sp = str(rec.get("species", "")).strip()
        if not BINOMIAL_RE.match(sp):
            errors.append(f"{nm}: species-specific record needs a valid `species` binomial")
            return
        if rec.get("generalisation"):
            errors.append(f"{nm}: species-specific record must not carry a generalisation block")
        wrong = [s for s in found if s != sp]
        if wrong:
            errors.append(f"{nm}: species-specific record for '{sp}' cites findings on {wrong} "
                          f"— invariant 2. Drop them or re-scope to class-general and DECLARE it.")
        pid = sp.lower().replace(" ", "-")
        if pid not in plant_ids and not rec.get("off_corpus"):
            warnings.append(f"{nm}: species '{sp}' has no plant record; set off_corpus: true "
                            f"if deliberate")
        return
    g = rec.get("generalisation") or {}
    if not g:
        errors.append(f"{nm}: class-general record requires a generalisation block — "
                      f"generalising must be explicit and reviewable, never silent")
        return
    if g.get("basis") not in GENERALISATION_BASES:
        errors.append(f"{nm}: generalisation.basis '{g.get('basis')}' invalid")
    if len(str(g.get("rationale", "")).strip()) < 80:
        errors.append(f"{nm}: generalisation.rationale must say WHY the physicochemistry carries "
                      f"across species, in >=80 chars. 'Similar compounds' is not a rationale.")
    for s in (g.get("excluded_taxa") or []):
        if not BINOMIAL_RE.match(str(s).strip()):
            errors.append(f"{nm}: excluded_taxa '{s}' is not a valid binomial")
        if str(s).strip() in found:
            errors.append(f"{nm}: '{s}' is both an excluded taxon and a source taxon")
    if len({s.split()[0] for s in found}) < 2:
        warnings.append(f"{nm}: class-general record rests on a single genus — it is a species "
                        f"result wearing a class label and cannot be approved")


def _check_copyright(nm, rec, errors):
    """Pharmacopoeias are paywalled, copyrighted normative texts. The schema's
    maxLength:300 and `abstract: false` are inert (nothing loads schema/*.json).
    These four lines are the only thing that runs."""
    for i, nc in enumerate(rec.get("normative_citations") or []):
        if not isinstance(nc, dict):
            errors.append(f"{nm}: normative_citations[{i}] is not a mapping")
            continue
        s = str(nc.get("statement_summary", ""))
        if len(s) > 300:
            errors.append(f"{nm}: normative_citations[{i}].statement_summary is {len(s)} chars "
                          f"(max 300). Paraphrase the requirement in one sentence; a summary "
                          f"long enough to substitute for buying the monograph is too long.")
        if nc.get("abstract") or nc.get("monograph_text") or nc.get("quote"):
            errors.append(f"{nm}: normative_citations[{i}] carries reproduced monograph text — "
                          f"cite coordinates only, never the text")
        for k in ("pharmacopoeia", "edition", "monograph_number"):
            if not str(nc.get(k, "")).strip():
                errors.append(f"{nm}: normative_citations[{i}] missing '{k}'")


def _check_approval(nm, rec, findings, bib_fields, errors):
    rows = practice_finding_rows(rec, findings)
    idx = practice_score_from_rows(rows)
    adm = [r for r in rows if r["admissible"]]
    if idx < 5:
        errors.append(f"{nm}: approved but method-confidence index is {idx} "
                      f"(band '{practice_band(idx)}'); approval requires >=5")
    n_ind = practice_n_independent(adm)
    if n_ind < 2:
        errors.append(f"{nm}: approved on {n_ind} independent source(s); approval requires >=2 "
                      f"independent research groups")
    if rec.get("parameter_kind") == "empirical" and not any(
            r["tier"] in ("optimisation", "comparative-bench") for r in adm):
        errors.append(f"{nm}: approved with no optimisation or comparative-bench finding — no "
                      f"cited paper actually varied the factor being recommended")
    if not rec.get("reviewed_by"):
        errors.append(f"{nm}: approved record missing reviewed_by")
    if not DATE_RE.match(str(rec.get("reviewed_date", ""))):
        errors.append(f"{nm}: approved record bad reviewed_date '{rec.get('reviewed_date')}'")
    disc = practice_n_independent([r for r in adm if r["in_band"] is False])
    if disc and not str(rec.get("discordance_note", "")).strip():
        errors.append(f"{nm}: {disc} independent finding(s) fall outside the band; an approved "
                      f"record must carry a discordance_note. Deleting the inconvenient finding "
                      f"to lift the score is falsifying the grade.")
```

**Deliberate omissions, and why.** No `corpus` bibtex check (it is derived — refutation-2 #8; validating a derived field guarantees a false failure). No `generalisation.source_taxa` equality check (refutation #15 — the field is computed from data already in the record; derive it in build.py, do not author it).

### Edit E — summary print

OLD:
```python
    print(f"Scanned {len(files)} plants | {len(name_files)} names files | "
          f"refs cited {len(cited)} / declared {len(declared)} | "
```
NEW:
```python
    print(f"Scanned {len(files)} plants | {len(name_files)} names files | "
          f"{len(practice_files)} practice records | "
          f"refs cited {len(cited)} / declared {len(declared)} | "
```
`refs cited N` is the only visible confirmation the orphan fix is live.

---

## 3.2 `scripts/build.py`

### Edit A — the practice ladder (insert between `score_from_tiers` and `load_plants`)

OLD:
```python
    bonus = 3 if human >= 5 else 2 if human >= 3 else 1 if human >= 2 else 0
    return max(1, min(10, base + bonus))


def load_plants():
```
NEW:
```python
    bonus = 3 if human >= 5 else 2 if human >= 3 else 1 if human >= 2 else 0
    return max(1, min(10, base + bonus))


# ---- PRACTICE CORPUS: the inverted evidence ladder ---------------------------
# TIER_BASE above answers "does this happen in a human body?". This one answers
# "does this number reproduce on a bench?". They INVERT and must never be
# interchanged. Do NOT touch TIER_BASE/score_from_tiers to accommodate practice:
# they feed indication_score -> plants.json and symptoms.json, and editing them
# silently moves every evidence number on the site.
#
#   * A REVIEW is the top clinical tier and scores ZERO here — it reports no
#     single (solvent, temperature, time, ratio, yield) tuple, so under the rule
#     that recommendations come from Methods and Results it cannot carry a record.
#   * A designed, quantified bench experiment is the BOTTOM clinical tier and the
#     TOP tier here.
#   * An RCT has no tier here at all. It is not evidence about extraction.
#
# method_type lives on the FINDING, not on the bibtex entry: one paper is
# 'optimisation' for the solvent axis and 'characterisation' for temperature, and
# a per-source grade would have to pick one and be wrong half the time. It also
# means reusing an existing clinical REF needs no bibliography edit.
PRACTICE_METHOD_TYPES = {
    "optimisation": "optimisation", "rsm": "optimisation", "factorial": "optimisation",
    "comparative-bench": "comparative-bench",
    "characterisation": "characterisation",
    "pharmacopoeial": "pharmacopoeial",
    "method-review": "method-review", "traditional-text": "traditional-text",
}
PRACTICE_TIER_BASE = {"optimisation": 7, "pharmacopoeial": 6, "comparative-bench": 5,
                      "characterisation": 3, "method-review": 0, "traditional-text": 0}
PRACTICE_FINDING_TIERS = {"optimisation", "comparative-bench", "characterisation",
                          "pharmacopoeial"}
# A normative standard is not a measurement of the world; it is a definition of it.
# Ph. Eur. 1559 does not report that 1:5 is optimal — it defines what may be CALLED
# a tincture. So it is authoritative for its own question and inadmissible for the
# other, in BOTH directions.
ADMISSIBLE_TIERS = {"empirical": {"optimisation", "comparative-bench", "characterisation"},
                    "normative": {"pharmacopoeial"}}
# Presentation. DELIBERATELY NOT the clinical 1-10 dots and NOT os-scoring.php: a
# user who has learned ten dots means "strong human evidence this plant works"
# will read ten dots on an extraction record as exactly that, when it means "three
# labs agree about a solvent percentage". The two can sit a few hundred pixels
# apart on one page. This artifact NEVER emits a key named `evidence`, so a
# renderer written against the clinical contract renders nothing rather than the
# wrong thing.
PRACTICE_BANDS = ((8, "established"), (5, "supported"), (2, "provisional"), (1, "insufficient"))


def practice_band(idx):
    for floor, name in PRACTICE_BANDS:
        if idx >= floor:
            return name
    return "insufficient"


def practice_independence_key(fi):
    """Identity of the RESEARCH GROUP. Concordance counts independent replication,
    not one lab's serial papers. Two editions of Ph. Eur. are one voice. Surname
    collisions merge two unrelated authors — a deliberate conservative bias: the
    error can only LOWER a score, never raise one."""
    auth = (fi.get("authority") or "").strip().lower()
    if auth:
        return "authority:" + auth
    grp = (fi.get("research_group") or "").strip().lower()
    if grp:
        return "group:" + re.sub(r"[^a-z]", "", grp)
    return "ref:" + str(fi.get("ref_id") or "")


def practice_in_band(fi, rec):
    """True / False / None. None = reports no optimum, so counts neither way.
    Compares ONLY on the recommended axis and (for solvent_pct) the recommended
    solvent: a temperature optimum of 70 C is not concordance with a 60-75%
    ethanol band. No tolerance — widening a band is a visible one-line diff."""
    r = rec.get("recommendation") or {}
    out = fi.get("outcome") or {}
    param = r.get("parameter")
    if fi.get("varied_factor") != param:
        return None
    if param == "solvent_pct" and (fi.get("conditions") or {}).get("solvent") != r.get("solvent"):
        return None
    rng = r.get("range")
    x = out.get("optimum_level")
    if isinstance(rng, list) and len(rng) == 2 and all(isinstance(y, (int, float)) for y in rng) \
       and isinstance(x, (int, float)) and not isinstance(x, bool):
        return rng[0] <= x <= rng[1]
    val, want = out.get("optimum_value"), r.get("value")
    if isinstance(val, str) and isinstance(want, str):
        return val.strip().casefold() == want.strip().casefold()
    return None


def practice_finding_rows(rec, findings=None):
    kind = rec.get("parameter_kind", "empirical")
    rows = []
    for fi in (findings if findings is not None else rec.get("findings") or []):
        if not isinstance(fi, dict):
            continue
        tier = PRACTICE_METHOD_TYPES.get((fi.get("method_type") or "").strip().lower(),
                                         "traditional-text")
        rows.append({"ref_id": fi.get("ref_id", ""), "tier": tier,
                     "indep": practice_independence_key(fi),
                     "admissible": tier in ADMISSIBLE_TIERS.get(kind, set()),
                     "in_band": practice_in_band(fi, rec)})
    return rows


def practice_n_independent(rows):
    return len({r["indep"] for r in rows if r["indep"]})


def practice_score_from_rows(rows):
    """base = strongest ADMISSIBLE tier; bonus = independent CONCORDANT findings;
    penalty = independent DISCORDANT ones. The penalty has no clinical analogue and
    is the point: a result outside your band is information ABOUT the band, not a
    null to be bucketed away, and a contested parameter must not score high."""
    adm = [r for r in rows if r["admissible"]]
    if not adm:
        return 1
    base = max(PRACTICE_TIER_BASE[r["tier"]] for r in adm)
    conc = practice_n_independent([r for r in adm if r["in_band"] is True])
    disc = practice_n_independent([r for r in adm if r["in_band"] is False])
    bonus = 3 if conc >= 4 else 2 if conc == 3 else 1 if conc == 2 else 0
    penalty = 2 if (disc and disc >= conc) else 1 if disc else 0
    return max(1, min(10, base + bonus - penalty))


def load_practice():
    """practice/**/*.yaml. A missing directory yields [] — glob on a nonexistent
    path returns [], so an empty or absent corpus builds green."""
    out = []
    for fn in sorted(glob.glob(os.path.join(PRACTICE, "**", "*.yaml"), recursive=True)):
        d = yaml.safe_load(open(fn, encoding="utf-8"))
        if isinstance(d, dict):
            out.append(d)
    return out


def load_plants():
```

Also add the path constant. OLD: `COMPDIR = os.path.join(ROOT, "compounds")` → NEW: same line plus `PRACTICE = os.path.join(ROOT, "practice")`.

### Edit B — load practice + derive `corpus` BEFORE citations.json

OLD:
```python
    plants = load_plants()
    slugs = resolve_common_slugs(plants)
```
NEW:
```python
    plants = load_plants()
    slugs = resolve_common_slugs(plants)
    # Loaded here, before citations.json, because the corpus dimension and the
    # practice linkage both feed the citation rows below.
    practice = load_practice()
    practice_refs = set()
    for _pr in practice:
        for _fi in (_pr.get("findings") or []):
            if isinstance(_fi, dict) and _fi.get("ref_id"):
                practice_refs.add(_fi["ref_id"])
        for _nc in (_pr.get("normative_citations") or []):
            if isinstance(_nc, dict) and _nc.get("ref_id"):
                practice_refs.add(_nc["ref_id"])
        for _r in (_pr.get("context_reference_ids") or []) + (_pr.get("references") or []):
            practice_refs.add(_r)
        for _ov in (_pr.get("species_overrides") or []):
            for _fi in ((_ov or {}).get("findings") or []):
                if isinstance(_fi, dict) and _fi.get("ref_id"):
                    practice_refs.add(_fi["ref_id"])
```

### Edit C — the corpus key on every citation row

OLD:
```python
            "tier": classify_tier(f, e["type"]),
            "display": display_title(f, e["key"]),
```
NEW:
```python
            "tier": classify_tier(f, e["type"]),
            # DERIVED, never declared. A derived value cannot drift from reality,
            # and a paper measuring both extraction yield and bioactivity legitimately
            # belongs to both — which is why it is an ARRAY. Behaviour when a REF is
            # cited by neither: ["clinical"], so all 3110 existing entries are
            # correctly labelled with zero backfill.
            "corpus": (["clinical"] if e["ref_id"] not in practice_refs
                       else (["clinical", "practice"] if e["ref_id"] in inv else ["practice"])),
            "display": display_title(f, e["key"]),
```
The sort is unchanged (`display` then `_year`), so no existing row re-orders.

### Edit D — the practice emitter + draft twin

OLD:
```python
    # ---- manifest.json (versioning + integrity; no timestamp -> clean diffs) ------
    artifacts = {}
```
NEW:
```python
    # ---- practice.v1.json (tincture / formula calculator provenance feed) --------
    # PUBLIC file carries approved records ONLY. The twin MUST be named
    # practice.v1.draft.json: that inherits the existing `build/*.draft.json` line in
    # .gitignore, so it never reaches osdb/main and therefore never reaches the
    # WordPress sync. Any other name publishes unreviewed extraction recommendations
    # straight to the live site. This is the highest-consequence name in the change.
    def practice_rows(status):
        rows = []
        for pr in practice:
            if status and pr.get("status") != status:
                continue
            rws = practice_finding_rows(pr)
            idx = practice_score_from_rows(rws)
            adm = [r for r in rws if r["admissible"]]
            k = pr.get("key") or {}
            rows.append({
                "id": pr.get("id", ""), "record_type": pr.get("record_type", ""),
                "parameter_kind": pr.get("parameter_kind", ""),
                "species_scope": pr.get("species_scope", ""),
                "extraction_class": k.get("extraction_class"), "part": k.get("part"),
                "solvent": k.get("solvent"), "method": k.get("method"),
                "recommendation": pr.get("recommendation") or {},
                "avoid": pr.get("avoid") or [],
                "source_taxa": sorted({str((f.get("material") or {}).get("species", "")).strip()
                                       for f in (pr.get("findings") or []) if isinstance(f, dict)
                                       and (f.get("material") or {}).get("species")}),
                "excluded_taxa": sorted((pr.get("generalisation") or {}).get("excluded_taxa") or []),
                "discordance_note": pr.get("discordance_note", ""),
                "references": sorted({f["ref_id"] for f in (pr.get("findings") or [])
                                      if isinstance(f, dict) and f.get("ref_id")}),
                # Method confidence. NOT the clinical evidence scale. `scale` is a hard
                # assertion a front end can test; there is deliberately no key named
                # `evidence` anywhere in this row.
                "confidence_band": practice_band(idx), "confidence_index": idx,
                "basis_tier": max(adm, key=lambda r: PRACTICE_TIER_BASE[r["tier"]])["tier"] if adm else "",
                "concordant_sources": practice_n_independent([r for r in adm if r["in_band"] is True]),
                "discordant_sources": practice_n_independent([r for r in adm if r["in_band"] is False]),
                "scale": "omnia-sana/method-confidence@1",
                "status": pr.get("status", ""),
            })
        rows.sort(key=lambda r: (str(r["extraction_class"] or ""), str(r["part"] or ""),
                                 str(r["solvent"] or ""), str(r["method"] or ""), r["id"]))
        return rows

    approved_pr, draft_pr = practice_rows("approved"), practice_rows(None)
    solvents_pub, methods_pub, xclasses_pub = [], [], []
    for _fn, _sink in ((os.path.join(VOCAB, "solvents.yaml"), solvents_pub),
                       (os.path.join(VOCAB, "extraction_methods.yaml"), methods_pub),
                       (os.path.join(VOCAB, "extraction_classes.yaml"), xclasses_pub)):
        for _v in yaml.safe_load(open(_fn, encoding="utf-8")):
            _sink.append({k: v for k, v in _v.items() if k != "note"})
    write(os.path.join(OUT, "practice.v1.json"),
          {"schema": "omnia-sana/practice@1", "count": len(approved_pr),
           "solvents": solvents_pub, "methods": methods_pub, "classes": xclasses_pub,
           "records": approved_pr})
    write(os.path.join(OUT, "practice.v1.draft.json"),
          {"schema": "omnia-sana/practice@1", "count": len(draft_pr),
           "solvents": solvents_pub, "methods": methods_pub, "classes": xclasses_pub,
           "records": draft_pr})

    # ---- manifest.json (versioning + integrity; no timestamp -> clean diffs) ------
    artifacts = {}
```

Note the twin filter follows the existing idiom exactly: `if status and pr.get("status") != status` — the truthiness guard means `status=None` disables filtering, so the draft twin is the **review superset** (draft + approved), matching `interaction_rows`.

### Edit E — manifest list

OLD:
```python
    for fn in ["citations.json", "symptoms.json", "plants.json", "vocab.json", "names.json",
               "interactions.v1.json", "pairings.v1.json", "lookalikes.v1.json"]:
```
NEW:
```python
    for fn in ["citations.json", "symptoms.json", "plants.json", "vocab.json", "names.json",
               "interactions.v1.json", "pairings.v1.json", "lookalikes.v1.json",
               "practice.v1.json"]:
```
Appended, not inserted — `artifacts` is a dict built in list order, so inserting mid-list shifts every manifest key. The `.draft` twin stays **out**: it is gitignored, and hashing an untracked file would make `manifest.json` depend on local state.

### Edit F — print block

OLD:
```python
    print("  manifest.json  : %d artifacts hashed" % len(artifacts))
```
NEW:
```python
    print("  practice       : %d approved (%d incl. draft) [.v1.json + .draft twin]" % (len(approved_pr), len(draft_pr)))
    print("  manifest.json  : %d artifacts hashed" % len(artifacts))
```

---

## 3.3 `schema/source.schema.json` — full replacement

Measured before editing: `grep -c evidence_type bibliography.bibtex` = **0**; `study_type` = **3110** across 3110 entries. The schema field name is dead; the code is right. Fix the schema, not the code.

OLD (the two properties, verbatim):
```json
    "url": {"type": "string"},
    "evidence_type": {
      "type": "string",
      "enum": ["rct", "meta-analysis", "systematic-review", "review", "observational", "in-vivo", "in-vitro", "traditional", "monograph", "web"],
      "description": "Study/source type, used to weight claim evidence and support validation."
    },
    "abstract": {"type": "string", "description": "Optional single-line abstract (braces stripped, whitespace collapsed)."}
  }
}
```
NEW:
```json
    "url": {"type": "string", "description": "Required on kind: standard. build.py's best_link() falls back to a Google Scholar SEARCH url when there is no doi and no url, which on a paywalled monograph presents a junk search as the source. Point this at the publisher's monograph landing page."},
    "publisher": {"type": "string"},
    "kind": {
      "type": "string",
      "enum": ["publication", "standard"],
      "default": "publication",
      "description": "Source shape. 'publication' is the historical shape and the behaviour when this field is ABSENT, so none of the 3110 existing entries need backfilling. 'standard' is a normative pharmacopoeial monograph: paywalled, copyrighted, prescriptive rather than descriptive. There is ONE bibliography and ONE REF sequence — a second schema file would describe a record class with no store, and splitting `declared` would manufacture the orphan false-positive class whose documented remediation is destructive."
    },
    "pharmacopoeia": {"type": "string", "enum": ["ph-eur", "usp", "bhp", "ahp", "bp", "who-monographs", "escop"], "description": "Issuing body. kind: standard only."},
    "edition": {"type": "string", "description": "Edition and supplement, e.g. '11th Ed., Supplement 11.5 (2024)'. Part of the IDENTITY of a standard: monograph numbers persist across editions while their requirements change, so an uncited edition is unverifiable. kind: standard only."},
    "monograph_number": {"type": "string", "description": "e.g. '1559', '0765', '<565>'. kind: standard only."},
    "monograph_title": {"type": "string", "description": "e.g. 'Tinctures'. Note display_title() needs >=6 alphabetic characters in `title` or it falls back to the url host, so `title` should read e.g. 'Tinctures (Ph. Eur. monograph 1559)'."},
    "study_type": {
      "type": "string",
      "enum": ["systematic-review", "meta-analysis", "review", "rct", "clinical", "preclinical", "traditional"],
      "description": "Evidence tier for CLINICAL claims, hand-set on every entry. THIS enum is the one scripts/build.py actually reads (STUDY_TYPE_TIER) and the one README.md documents. It replaces the former `evidence_type`, which was declared here, written to 0 of 3110 entries, and read by no script — the schema was wrong, not the code. A pharmacopoeial standard is correctly `traditional` here: it is authoritative about PRACTICE, not evidence that a plant treats a condition. Its normative weight is carried by the practice record's method_type: pharmacopoeial, NOT by a new value in this enum. Do not introduce a third source-typing vocabulary."
    },
    "corpus": {
      "type": "array",
      "items": {"type": "string", "enum": ["clinical", "practice"]},
      "description": "Which public corpus this source belongs to, for the Knowledge Finder's corpus filter. DERIVED by scripts/build.py from actual linkage — never authored, and scripts/validate.py deliberately does NOT check it. An array because a study measuring both extraction yield and bioactivity belongs to both. Behaviour when a REF is cited by neither: ['clinical']."
    },
    "abstract": {"type": "string", "description": "The REAL published abstract, single line, braces stripped, whitespace collapsed. The site renders this AS the source's own words, so a paraphrase is a fabricated quotation. FORBIDDEN on kind: standard — a monograph has no abstract, and anything written there is either invented or a reproduction of paywalled normative text."}
  },
  "allOf": [
    {
      "if": {"properties": {"kind": {"const": "standard"}}, "required": ["kind"]},
      "then": {
        "required": ["pharmacopoeia", "edition", "monograph_number", "url", "publisher"],
        "properties": {"abstract": false, "doi": false, "journal": false, "study_type": {"const": "traditional"}}
      },
      "$comment": "INERT. No script imports jsonschema; schema/*.json is loaded by nothing. This branch is the documentation contract only — the abstract-forbidden rule that actually runs is _check_copyright() in scripts/validate.py."
    }
  ]
}
```
Also widen the existing `"type"` enum (currently `["article", "book", "misc"]`) to `["article", "book", "incollection", "inbook", "booklet", "misc"]` — `classify_tier` already branches on all six.

`harvard()` reads only `author, year, title, journal, volume, number, pages, doi, url`, so `edition` and `monograph_number` are silently dropped from the generated citation. That needs a `kind == "standard"` branch in `harvard()`, provably no-op for the 3110 entries with no `kind` — **deferred to step D4 below**, not part of the day-one landing.

---

## 3.4 `schema/compound.schema.json`

OLD:
```json
    "class": {"type": "string", "description": "Chemical / biosynthetic class, e.g. flavonoid, organosulfur, sesquiterpene-lactone, alkaloid."},
```
NEW:
```json
    "class": {"type": "string", "description": "Chemical / biosynthetic class, e.g. flavonoid, organosulfur, sesquiterpene-lactone, alkaloid. Biosynthetic, NOT extractive: it groups quercetin with rutin, whose solvent optima are opposite (70-96% vs 40-60% ethanol). Never key an extraction record on it."},
    "extraction_class": {
      "type": "array",
      "items": {"type": "string", "pattern": "^[a-z0-9-]+$"},
      "description": "OPTIONAL disambiguator -> vocabularies/extraction_classes.yaml. The practice corpus keys on the existing compound ids (already validated against compounds/ by validate.py); this is the secondary layer that resolves the class-like ids. `flavonoid` sits on 132 plants and resolves to either flavonoid-glycoside or flavonoid-aglycone, whose optima are opposite. Behaviour when ABSENT or when this lists >1 class: `resolution` governs — see below. It is never a coin flip."
    },
    "resolution": {
      "type": "string",
      "enum": ["exact", "ambiguous", "unresolvable"],
      "default": "unresolvable",
      "description": "How this compound id joins to the practice corpus. exact -> join and recommend. ambiguous (flavonoid, tannin, polysaccharide, terpene) -> emit the conservative intersection only, and NEVER reach approved. unresolvable (glycoside, phenolic-compound) -> do not join at all. Behaviour when ABSENT is 'unresolvable', i.e. NO recommendation — the fail-closed default. 324 of the 861 plant x compound slots need this; shipping silence for them is correct, shipping a confident 70% ethanol figure for a mucilage is not."
    },
    "toxicity_flag": {
      "type": "string",
      "enum": ["none", "dose-limited", "topical-only", "avoid-internal"],
      "default": "avoid-internal",
      "description": "Whether a YIELD-MAXIMISING recommendation is safe for this constituent. A recommendation states a preparation that is safe and traditionally correct; it is NOT the argmax of a yield table, and the two diverge violently. `alkaloid` sits on symphytum_officinale, petasites_hybridus, tussilago_farfara, chelidonium_majus and arnica_montana, where it means hepatotoxic PYRROLIZIDINE alkaloids — an approved 'acidified menstruum extracts the salt' record joined on that id instructs a user to maximise PA recovery from comfrey root. Same for `coumarin` (cinnamomum_cassia, arnica_montana; EFSA TDI 0.1 mg/kg bw), `asarone` (acorus_calamus, genotoxic), `sesquiterpene-lactone` (arnica_montana, topical only). Behaviour when ABSENT is 'avoid-internal' — FAIL CLOSED. An unflagged compound cannot carry an approved recommendation, which forces the ~12 known ids to be triaged before any record joins them."
    },
    "regulatory_limit": {"type": "string", "description": "Free text, e.g. 'EFSA TDI 0.1 mg/kg bw'. Shown alongside any recommendation whose key compound is dose-limited."},
```
The matching validate.py rule (fail-closed: an approved extraction record whose key compound's `toxicity_flag` is anything but `none` errors unless it carries `limit_rationale` + `route`) is part of the same edit, **but it depends on the practice→compound join, which is deferred** — see step D3.

`vocab.json` currently projects compounds as `{id, name, class}` only, so none of these fields reach the front end and invariant 4's "downstream consumer" is unmet until the projection is widened. Do that in the same commit as the join.

---

## 3.5 `.github/workflows/build-and-publish.yml`

OLD:
```yaml
      - 'compounds/**'
      - 'bibliography.bibtex'
      - 'schema/**'
      - 'scripts/**'
```
NEW:
```yaml
      - 'compounds/**'
      - 'practice/**'
      - 'bibliography.bibtex'
      - 'schema/**'
      - 'scripts/**'
```
Without this, a practice-only commit skips validate **and** rebuild: the record lands in the repo, `build/practice.v1.json` is never regenerated, the manifest sha still describes the old data, and the hourly WordPress sync serves stale content while every check is green. One line, and it must land with the directory. (`build/` stays out — that is loop prevention.) The commit step (`git add build/ names/ plants/`) is correct unchanged: `practice/` is hand-authored, nothing machine-mutates it.

`.github/workflows/validate.yml` has no path filter, so the hard gate already runs on every push — the validate.py changes must be correct on their first push.

---

## 3.6 `CLAUDE.md`

OLD:
```markdown
- Orphaned bibliography entries (declared, never cited) still ship to the public
  Knowledge Finder feed. Deleting a citation from a plant is not enough — remove
  the bibliography entry too, or it stays visible on the site.
```
NEW:
```markdown
- Orphaned bibliography entries (declared, never cited) still ship to the public
  Knowledge Finder feed. Deleting a citation from a plant is not enough — remove
  the bibliography entry too, or it stays visible on the site.
  **Before acting on ANY orphan, confirm the practice loop is wired.** `cited` is
  populated by `cited.update(find_refs(d))`, which for years existed only inside
  the plants loop. If the mirror inside the `practice/` loop is missing or has
  regressed, every REF cited only by a practice record reports as an orphan — a
  warning, so the build stays green — and following the deletion rule destroys the
  bibliography the calculator depends on, after which the same refs flip to hard
  errors with the data already gone. The tell: `refs cited N / declared M` in the
  validate.py summary, where N is far below M and the orphan list is all recent
  REF ids. Never delete an entry whose only citer is a practice record.
```

## 3.7 `.claude/skills/osdb-verify-integrity/SKILL.md`

OLD:
```markdown
- **Orphan reference** (declared in the bibliography, never cited). Not cosmetic.
  **Orphaned entries still ship to the public Knowledge Finder feed** — they are
  visible on the site with nothing pointing to them. Removing a citation from a
  plant is only half the job; the bibliography entry has to go too.
```
NEW:
```markdown
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
```

---

# 4. DAY-ONE GREEN CHECK

**Landing set:** empty `practice/` directory (plus `.gitkeep`), the four new `vocabularies/*.yaml` files, `schema/practice.schema.json`, all of §3.1–3.7 above. No practice records, no bibtex changes.

**`validate.py` path, traced:**
1. Edit A constants — pure module-level regex/set construction, no I/O. Safe.
2. `sys.path.insert` + `from build import ...` — `scripts/build.py` guards `main()` behind `if __name__ == "__main__":` (confirmed, last two lines of the file), so importing executes only module-level defs and the `ROOT/BIB/PLANTS/...` path constants. `os.path.join` on a nonexistent `practice/` does not touch the filesystem. **No side effects. Safe.** Circular-import risk is nil: build.py does not import validate.
3. Edit C vocab loads — `vocab_map`/`vocab_ids` open four files with no `try`, exactly like the existing five. **This is the only thing that can break green:** if any of `solvents.yaml`, `extraction_methods.yaml`, `extraction_classes.yaml`, `parts.yaml` is missing, it is an unhandled `FileNotFoundError` that kills the gate. **Land the four YAML files in the same commit as Edit C.** Each must parse as a list of mappings each carrying `id` — a mapping or a `None` raises `TypeError`/`AttributeError` inside the comprehension.
4. Plants loop — untouched. 187 files, `cited` populated as before.
5. Practice loop — `glob.glob(os.path.join(ROOT, "practice", "**", "*.yaml"), recursive=True)` on an empty (or absent) directory returns `[]`. Loop body never executes. `bib_fields` parses fine (and is wrapped in try/except anyway). `practice_plant_refs` is empty, so its resolution loop is a no-op.
6. `missing`/`orphan` — `cited` is byte-identical to today's, `declared` unchanged. Baseline is **3110 cited / 3110 declared, zero orphans**; that holds exactly.
7. Summary print gains `0 practice records`. Exit 0. ✅

**`build.py` path:**
1. Ladder constants + five new functions — module-level, no I/O. `PRACTICE` path constant added.
2. `load_practice()` → `[]`. `practice_refs` → `set()`.
3. Citations: every `e["ref_id"] not in practice_refs` is True for all 3110, so every row gets `"corpus": ["clinical"]`. Sort keys (`display`, `_year`) untouched → **row order identical**; the only diff in `citations.json` is one added key per row. Expected: file grows, sha changes, manifest count unchanged at 3110.
4. Practice emitter: `practice_rows("approved")` and `practice_rows(None)` both return `[]`. `solvents_pub`/`methods_pub`/`xclasses_pub` load the three vocabularies — **same missing-file crash surface as validate.py**; same mitigation. `write()` emits `practice.v1.json` with `count: 0` and `records: []`, and `practice.v1.draft.json` likewise.
5. Manifest: the loop re-reads `practice.v1.json` off disk in binary. The emitter runs **before** the artifact list (verified: the insertion point is immediately above `artifacts = {}`), so the file exists. **Naming a file in that list with no emitter is a hard `FileNotFoundError` — list and emitter must be one commit.** Manifest gains a 9th key, appended last, so the existing 8 keys keep their positions and their shas (except `citations.json`, which legitimately changed).
6. Print block gains `practice : 0 approved (0 incl. draft)`. ✅

**Things that break green if you get them wrong — all four verified:**
- Missing any of the four new vocabulary YAML files → unhandled crash in both scripts. *(Same commit.)*
- A vocabulary file that is not a list of `{id: ...}` mappings → `TypeError` in the comprehension.
- Adding `"practice.v1.json"` to the manifest list without the emitter → `FileNotFoundError`, and `build/` is left half-updated with a manifest describing the previous run.
- Naming the twin anything but `practice.v1.draft.json` → it is **not** matched by `.gitignore`'s `build/*.draft.json`, gets committed, reaches `osdb/main`, and the WordPress sync serves unreviewed recommendations.

**Not required for green, confirmed:** the `parts_used` cleanup (58 distinct dirty values, composites like `'Root (and bark, wood)'` still live), the seven fungal `Whole Plant` records, the missing garlic `Bulb`, the 69 compound `extraction_class`/`toxicity_flag` assignments, the 92 constituent entries with no `compounds` list. Nothing on day one joins `parts_used` to `parts.yaml`.

**One expected new warning class:** none. Zero practice records means zero new refs, so the orphan list stays empty.

---

# 5. DEFERRED — order and blockers

**D0 (day one, one commit).** §3.1 A–E + D2–D4, §3.2 A–F, §3.3, §3.5, §3.6, §3.7, `schema/practice.schema.json`, the four vocabularies, empty `practice/`. *Blocked on:* nothing. The three one-liners the refutations flagged as must-not-slip — CI trigger path, `cited.update`, and the `corpus` contradiction (resolved by deriving, not validating) — are all inside this commit.

**D1 — reconcile the record shape, in writing, before anyone authors.** The two upstream drafts specify disjoint field names for every anti-skim field; a schema-A-shaped record hard-errors on every field of the schema-B validator. Delete the losing document so nobody authors against it. *Blocked on:* nothing. *Blocks:* everything below.

**D2 — the Knowledge Finder deploy order. This one is forced and must not be reordered.** `build.py` iterates **every** bibtex entry into `citations.json` regardless of linkage or status, and `bibliography.bibtex` **is** a CI trigger path, so the moment the first practice REF exists it is public — via hourly WP-cron, the lazy-on-request path, and the push webhook. There is no window in which you control the timing.
  1. Ship `corpus` derivation (in D0). All 3110 entries derive to `["clinical"]` — a provably no-op content change.
  2. Ship the Knowledge Finder corpus filter in the JS **and bump `?v=kfN` in page 208**, run `os_kf_do_sync(true)`, and verify the filter renders — while the field is still uniformly `["clinical"]`. A no-op deploy is the only safe way to test a filter.
  3. *Only then* add the first practice bibtex entry.
  Reversing 2 and 3 dumps 120–160 extraction-methodology papers and pharmacopoeial monographs into a clinical-evidence library with no filter to exclude them and heuristic tier labels (`classify_tier` routes `@book`/`@misc` monographs to `traditional`). Consider bumping the envelope to `knowledge-finder@3` if the WP consumer branches on it.

**D3 — the toxicity gate, before the first approved extraction record.** Populate `toxicity_flag` + `regulatory_limit` on the ~12 ids (`alkaloid`, `coumarin`, `asarone`, `sesquiterpene-lactone`, `hypericin`, `berberine`, `allicin`, …), widen the `vocab.json` compound projection, and add the fail-closed validate rule plus a required `route: internal|topical` on the recommendation. *Blocked on:* D1. *Blocks:* any `status: approved` extraction record. Absent `toxicity_flag` defaults to `avoid-internal`, so this is enforced by construction, not by discipline.

**D4 — pharmacopoeial rendering.** `harvard()` branch for `kind == "standard"` (it currently drops `edition` and `monograph_number` — the entire citation identity), a `link_type: "normative"` branch so `best_link()` stops emitting a Google Scholar **search** URL as the source, and a `title` convention satisfying `display_title()`'s ≥6-alphabetic-character rule. Each must be provably no-op for the 3110 entries with no `kind`. *Blocked on:* D2 step 3.

**D5 — the conflict arbiter.** 13 plants have a measured water-vs-ethanol collision on a single part (`matricaria_chamomilla` is the clean case: one `parts_used: [Flower]`, mucilage + polysaccharide *and* bisabolol + chamazulene + essential-oil). The calculator must emit one answer and nothing says how N correct class records collapse to one. Recommended resolution: make the calculator's output a **per-constituent table**, never a single number — no new plant field, and it is the honest answer. *Blocked on:* D1. *Blocks:* the calculator wiring, i.e. invariant 4's downstream consumer.

**D6 — the disambiguation backfill (phase 0 of the real project).** Re-measured at `88221f9`: **324 of 861** plant×compound slots need a `resolution`/`extraction_class` decision; **92** constituent entries carry no `compounds` list at all; **20 of 187 plants have no cleanly-resolving compound id** and will emit zero recommendations even with a complete corpus. (The drafts said 394 / 842 / 27; those were wrong.) The 20: `andrographis-paniculata, asclepias-tuberosa, capsella-bursa-pastoris, cordyceps-militaris, crocus-sativus, equisetum-pratense, equisetum-sylvaticum, galium-album, gentiana-lutea, gymnema-sylvestre, hericium-erinaceus, inonotus-obliquus, lentinula-edodes, piper-methysticum, pleurotus-ostreatus, psilocybe-cubensis, rhodiola-rosea, salix-alba, scutellaria-lateriflora, trametes-versicolor`.

Two patterns, and both mean this is an **entity-model gap, not a sourcing gap**:
**(a) 7 of the 20 are the same 7 fungi** that carry the `Whole Plant` `parts_used` debt — they fail on both axes at once, so fix them as one workstream.
**(b) The defining constituent is frequently missing from `compounds/` altogether.** `salix_alba`'s "Salicin and related salicylates" has `compounds: None` and **there is no `salicin` entity** — salicin being the one thing anyone looks willow bark up for. `crocus_sativus` is identical in shape: crocin, crocetin, safranal and picrocrocin are all named in its constituents and none is an entity. **Audit `compounds/` for absences before disambiguating what exists** — adding the missing entities may resolve several of the 20 outright, and is cheaper than any of the alternatives.

This is sized in **entries, not papers**, and is invisible in the 120–200 paper estimate. State the coverage target honestly; a green build with 20 silently-empty plants must not read as success. *Blocked on:* D3.

**D7 — `parts_used` cleanup, and it goes LAST.** Split composites to atomic ids, move the 12 product qualifiers into `preparations[]`, apply the 8 factual corrections (7 fungal `Whole Plant` → `fruiting-body`/`mycelium`/`sclerotium`; `allium_sativum` gains `Bulb`), then add `constituents[].parts` (540 entries), then add the enum to `plant.schema.json` and the validate rule. Until all of that lands, the practice `key.part` axis must be **`null`-only**. *Blocked on:* D6. Also add `parts_used[].reference_ids` so the corrections are citable in-record.

**D8 — the already-public draft leak, and it is not caused by this work.** `build.py`'s public-plant projection is `q = {k: v for k, v in p.items() if k != "internal_notes"}`, and `approved_only()` is applied to exactly three keys (`drug_class_interactions`, `pairings`, `dangerous_lookalikes`). Everything else ships status-ignored. Measured in the live build: **280 `draft` preparations and 84 `draft` dosages are already public on the plant pages.** That matters here for two reasons: (a) it is the leak path for any future plant-record extension — an `extraction_exceptions[]` entry is a *safety* statement and would go live unreviewed, so **extend `approved_only()` coverage before adding any such field**; (b) the practice corpus is about to start contradicting those 280 unreviewed preparation instructions on the same pages. *Blocked on:* nothing — do it independently, ideally before D5.

**D9 — the audit loop that makes anti-skim real.** None of the anti-skim fields is externally verifiable; the three internal-consistency checks compare fabricated fields against each other, so they catch careless transcription by an honest editor and not deliberate fabrication. What the design actually buys is **auditability**, and that should be sold as such. Add: `fulltext_source` naming where the PDF came from; a `verified_by`/`verified_date` distinct from `reviewed_by`, meaning a second person opened the paper; and a sampling script that pulls 10% of findings for PDF spot-check and records the pass rate.

---

# 6. RISK REGISTER

| # | Risk | Mitigation |
|---|---|---|
| 1 | **A recommendation derived from lab-solvent findings renders as an ethanol instruction.** `recommendation` had no solvent field at all in the drafts, and the extrapolation check pooled comparator levels across solvents and across parameters — so a methanol sweep of 20–90% legitimises "60–75% ethanol", and a temperature sweep of 40–80 °C legitimises it too. | `recommendation.solvent` and `.method` required and gated on `consumer_safe`/`consumer_reproducible` loaded from the vocabulary (§3.1 D3); envelope and concordance partitioned by both `varied_factor` and solvent (§3.1 D3, §3.2 `practice_in_band`). |
| 2 | **A yield-maximising recommendation joined on `alkaloid` or `coumarin` tells a user to maximise a hepatotoxin** — the ids are shared by comfrey, butterbur, coltsfoot, celandine, arnica and cassia, and `compounds/*.yaml` has no toxicity field to gate on. | `toxicity_flag` defaults to `avoid-internal` (fail-closed), so an untriaged compound cannot carry an approved record; D3 is a hard prerequisite to the first approval; required `route` cross-checked against `parts_used`. |
| 3 | **False orphans get the practice bibliography deleted.** Baseline is 0 orphans / 3110 declared, so the first practice batch produces an orphan block that is entirely practice REFs, in a repo where that list has never had anything in it — and the skill says to delete them. | `cited.update(find_refs(rec))` in the practice loop, landing in the **same commit as the directory** (§3.1 D); the precondition block added to both CLAUDE.md and osdb-verify-integrity (§3.6, §3.7); `refs cited N` in the summary as the live tell. |
| 4 | **Unreviewed recommendations reach the live site.** Two independent paths: a draft twin named anything but `practice.v1.draft.json` misses the `build/*.draft.json` gitignore and gets committed to `osdb/main`; and any practice data denormalised onto the plant record ships status-ignored, exactly as 280 draft preparations and 84 draft dosages already do. | Twin name fixed and commented at the emitter (§3.2 D); no plant-record extension until `approved_only()` coverage is widened (D8). |
| 5 | **The method-confidence score is read as an efficacy score.** A second numeric confidence scale now exists on the same site — and 918 of 1,696 live claims displayed an inflated evidence label for four weeks the last time two scales coexisted, while every sync reported success. | The artifact emits **no key named `evidence`**, so a clinical renderer pointed at a practice record renders nothing rather than the wrong thing; a `scale: "omnia-sana/method-confidence@1"` marker the front end can assert on; word + 4-segment bar under "Method confidence", never dots, never "N/10"; spot-check the extremes on the live page — a bench-only record must not render as strong. |