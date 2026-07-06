# Dangerous Lookalikes — data-model & schema spec

Design spec for a new **safety-critical** relational entity: for each medicinal
plant, the dangerous plant(s)/fungi it can be mistaken for, and exactly how to
tell them apart. Powers a new interactive tool: input a medicinal plant → output
its dangerous lookalikes + rock-solid distinguishing features.

Status: **SPEC ONLY.** No schema/validate/build changes and no data have been
committed. Implementation + data-gathering happen in the hand-off session
(`NEXT_SESSION_LOOKALIKES.md`). Every example below is *illustrative* and must be
independently fact-checked + human-signed-off before it is marked `approved`.

This spec was written after a full fresh audit of the DB (see the analysis that
accompanies it) and follows the exact conventions the codebase already uses for
`drug_class_interactions` (plant → shared-vocabulary relation) — the closest
existing template.

---

## 1. Data model (and why)

A dangerous plant (e.g. **poison hemlock**) is a lookalike for **many** medicinal
plants (ground elder, wild carrot, sweet cicely, angelica…). Its toxicology is
one fact. *How you distinguish it from a given medicinal plant* is a **different
fact per medicinal plant**. So the model is a **plant → shared-vocabulary
relation**, identical in shape to `drug_class_interactions`:

- **`vocabularies/dangerous_plants.yaml`** — one controlled-vocab entry per toxic
  plant/fungus. Canonical, DRY: hemlock's scientific name + toxic principle +
  toxicity live **once**.
- **`dangerous_lookalikes[]`** array on each medicinal-plant record — the
  **pairwise** datum: which dangerous plant, at which part/stage, and the
  distinguishing features that separate *this* medicinal plant from it.

**Rejected alternatives (and why):**

| Option | Verdict | Reason |
|---|---|---|
| Fully **inline** per plant | ✗ | Duplicates hemlock's toxicology across every plant it resembles → drifts out of sync; violates the README's "one fact, one place". |
| **Mirrored** like `pairings` (A↔B) | ✗ | The relation is **asymmetric**: the toxic plant has no medicinal record and no reciprocal "lookalikes" list. Model it **one-directional**, like `drug_class_interactions` — do **not** mirror in `build.py`. |
| Shared **vocabulary** + pairwise relation | ✓ | DRY, reviewable in one diff, reuses the `drug_class_interactions` template exactly. |

---

## 2. Three states — "no lookalikes" ≠ "not researched"

For a safety feature, *"we haven't checked"* must **never** render as *"safe"*.
An absent array is ambiguous, so add an explicit editorial completeness flag,
`lookalikes_review`, at the plant-record level:

| State | Encoding | Tool renders |
|---|---|---|
| **Not yet researched** | `lookalikes_review` absent | "Identification data not yet available — verify your ID independently." |
| **Researched, none known** | `lookalikes_review.outcome: none-known` (array empty/absent) | "No dangerous lookalikes on record for X." (positive reassurance) |
| **Has lookalikes** | `dangerous_lookalikes[]` non-empty + `outcome: has-lookalikes` | The hazard cards. |

Never overload an empty array to mean "none known" — YAML empty-vs-absent is
brittle and a reviewer can't tell a deliberate "none" from a stub.

---

## 3. Severity enum (new)

Existing enums don't fit lethality (`severity` is herb-drug-specific;
`pairing_type` is synergy/caution; contraindication severity tops out at
"serious"). Add a dedicated `$def` so the UI can loudly badge the killers:

```
lookalike_severity: fatal | dangerous | irritant | caution
```

- **fatal** — ingestion can kill (hemlock, water-dropwort, *Veratrum*, foxglove,
  *Colchicum*, lily-of-the-valley, *Galerina*).
- **dangerous** — serious poisoning / hospitalisation, rarely fatal
  (jack-o'-lantern *Omphalotus*).
- **irritant** — external burns / photodermatitis / GI upset, not lethal by
  normal ingestion (giant hogweed sap, petty spurge).
- **caution** — benign but worth noting so the forager isn't alarmed by a
  harmless confusable.

Mirror it into `validate.py` as a constant set (like `SEVERITIES` / `PAIR_TYPES`)
so malformed values hard-fail CI.

---

## 4. `schema/dangerous_plant.schema.json` (new file)

Modeled on `drug_class.schema.json`. Public-safe fields only are emitted;
`editor_notes` is editor-facing and stripped at build.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://omniasana.bio/schema/dangerous_plant.schema.json",
  "title": "Dangerous-plant vocabulary term",
  "description": "One toxic plant/fungus that a medicinal plant can be confused with. vocabularies/dangerous_plants.yaml is a list of these; each is referenced by id from a medicinal plant's dangerous_lookalikes[]. Canonical toxicology lives here ONCE.",
  "type": "object",
  "required": ["id", "label", "scientific_name", "toxic_principle", "toxicity", "default_severity"],
  "additionalProperties": false,
  "properties": {
    "id": {"type": "string", "pattern": "^[a-z0-9-]+$", "description": "Stable slug, e.g. conium-maculatum, veratrum-album, galerina-marginata."},
    "label": {"type": "string", "description": "Primary common name, e.g. 'Poison hemlock'."},
    "scientific_name": {"type": "string"},
    "family": {"type": "string"},
    "kingdom": {"type": "string", "enum": ["plant", "fungus"], "description": "So the tool can label fungal lookalikes correctly."},
    "synonyms": {"type": "array", "items": {"type": "string"}, "description": "Other common/scientific names, for search."},
    "toxic_principle": {"type": "string", "description": "The toxin(s), e.g. 'coniine and γ-coniceine (piperidine alkaloids)'."},
    "toxicity": {"type": "string", "description": "Plain-English, consumer-safe description of the harm, e.g. 'Ingestion causes ascending paralysis and can be rapidly fatal.'"},
    "toxicity_category": {"type": "string", "description": "Broad grouping: neurotoxic | cardiotoxic | cytotoxic | dermatotoxic | gastrointestinal | mixed."},
    "onset": {"type": "string", "description": "Optional but important for delayed-onset toxins (e.g. amatoxins: '6–24 h delayed; deceptively symptom-free early')."},
    "default_severity": {"$ref": "#/$defs/lookalike_severity", "description": "Worst-case severity if ingested; a relation may narrow it per medicinal plant/part."},
    "external_ids": {
      "type": "object", "additionalProperties": false,
      "description": "Botanical/mycological identity anchors (same idea as plant.external_ids).",
      "properties": {
        "wikidata": {"type": "string"}, "powo": {"type": "string"},
        "gbif": {"type": ["string", "integer"]}, "ncbi_taxon": {"type": ["string", "integer"]}
      }
    },
    "references": {"type": "array", "items": {"type": "string", "pattern": "^REF-\\d{4,}$"}, "description": "Sources for this toxic plant's identity + toxicology."},
    "editor_notes": {"type": "string", "description": "EDITOR-FACING ONLY. Never emitted to public build output."}
  },
  "$defs": {
    "lookalike_severity": {"type": "string", "enum": ["fatal", "dangerous", "irritant", "caution"]}
  }
}
```

### `vocabularies/dangerous_plants.yaml` — shape + illustrative seeds

> ⚠️ Illustrative. Toxicology below is well-established public knowledge, but each
> entry must still be sourced into `bibliography.bibtex` and reviewed before use.

```yaml
# Omnia Sana — controlled vocabulary: DANGEROUS PLANTS / FUNGI
# Schema: ../schema/dangerous_plant.schema.json
# Referenced by id from each medicinal plant's dangerous_lookalikes[].

- id: conium-maculatum
  label: Poison hemlock
  scientific_name: Conium maculatum
  family: Apiaceae
  kingdom: plant
  synonyms: ["hemlock", "poison parsley"]
  toxic_principle: Coniine and γ-coniceine (piperidine alkaloids)
  toxicity: Ingestion causes ascending muscular paralysis and respiratory failure; can be rapidly fatal in small amounts.
  toxicity_category: neurotoxic
  onset: Rapid (30 min–2 h)
  default_severity: fatal
  references: []           # REF-XXXX to be added

- id: veratrum-album
  label: White hellebore
  scientific_name: Veratrum album
  family: Melanthiaceae
  kingdom: plant
  toxic_principle: Steroidal alkaloids (veratrine, protoveratrines)
  toxicity: Causes vomiting, bradycardia and dangerous hypotension; the classic lethal mix-up for foragers seeking yellow gentian.
  toxicity_category: cardiotoxic
  onset: Rapid (30 min–4 h)
  default_severity: fatal
  references: []

- id: galerina-marginata
  label: Funeral bell
  scientific_name: Galerina marginata
  family: Hymenogastraceae
  kingdom: fungus
  toxic_principle: Amatoxins (α-amanitin)
  toxicity: Causes delayed, catastrophic liver failure; a few caps can be lethal. Symptom-free early phase is deceptive.
  toxicity_category: cytotoxic
  onset: Delayed (6–24 h; deceptively symptom-free early)
  default_severity: fatal
  references: []
```

---

## 5. `plant.schema.json` additions

Add two properties to the plant record. `dangerous_lookalikes` mirrors the
`drug_class_interactions` block; `lookalikes_review` carries the three-state flag.

```jsonc
// inside "properties":

"dangerous_lookalikes": {
  "type": "array",
  "description": "Dangerous plants/fungi this medicinal plant is realistically mistaken for. One-directional (NOT mirrored). Public tools serve status: approved ONLY.",
  "items": {
    "type": "object",
    "required": ["dangerous_plant", "severity", "distinguishing_features", "status"],
    "additionalProperties": false,
    "properties": {
      "dangerous_plant": {"type": "string", "pattern": "^[a-z0-9-]+$", "description": "id → vocabularies/dangerous_plants.yaml."},
      "severity": {"$ref": "#/$defs/lookalike_severity"},
      "confused_part": {"type": "string", "description": "Which part/growth stage is confusable, e.g. 'young leaves / basal rosette', 'root', 'whole plant before flowering'."},
      "confusion_context": {"type": "string", "description": "Plain-English why/when the mix-up happens (co-occurrence, foraging scenario, documented poisonings)."},
      "distinguishing_features": {"type": "array", "items": {"type": "string"}, "minItems": 1, "description": "Rock-solid, observable ways to tell the MEDICINAL plant apart from the dangerous one. Each must be reliable enough to bet a life on — omit anything subtle or ambiguous."},
      "key_test": {"type": "string", "description": "The single most reliable field check, e.g. 'Crush a leaf: true fennel smells strongly of aniseed; hemlock smells foul/mousy.'"},
      "reference_ids": {"$ref": "#/$defs/reference_ids"},
      "status": {"$ref": "#/$defs/safety_status"},
      "reviewed_by": {"type": "string"},
      "reviewed_date": {"type": "string"}
    }
  }
},
"lookalikes_review": {
  "type": "object",
  "description": "Record-level completeness flag distinguishing 'researched, none known' from 'not yet researched'. Absent = NOT researched.",
  "required": ["outcome"],
  "additionalProperties": false,
  "properties": {
    "outcome": {"type": "string", "enum": ["none-known", "has-lookalikes"]},
    "reviewed_by": {"type": "string"},
    "reviewed_date": {"type": "string"},
    "reference_ids": {"$ref": "#/$defs/reference_ids", "description": "For a 'none-known' assertion, the source(s) that support it."}
  }
}
```

Add to `$defs`:

```json
"lookalike_severity": {"type": "string", "enum": ["fatal", "dangerous", "irritant", "caution"]}
```

### Worked example — a `dangerous_lookalikes` block (illustrative, `draft`)

```yaml
# plants/aegopodium_podagraria.yaml  (append before `provenance:`)
lookalikes_review:
  outcome: has-lookalikes
  reviewed_by: 'Omnia Sana (owner-authorized)'
  reviewed_date: '2026-07-06'
dangerous_lookalikes:
- dangerous_plant: conium-maculatum
  severity: fatal
  confused_part: Young leaves / non-flowering foliage
  confusion_context: Both are white-umbel Apiaceae of hedgerows and waste ground; foragers gathering young ground-elder leaves have picked poison hemlock growing alongside.
  distinguishing_features:
  - Ground elder stems are plain green and grooved; poison hemlock stems are hairless with distinctive PURPLE/red blotches.
  - Ground elder leaves are once/twice-divided into broad, toothed leaflets; hemlock leaves are finely 3–4× divided, fern-like and lacy.
  - Crushed ground elder smells faintly of carrot/parsley; crushed hemlock smells foul and mousy.
  key_test: 'Check the stem: any purple blotching = do NOT eat (hemlock). Ground elder never has purple-spotted stems.'
  reference_ids: []        # REF-XXXX to be added + verified
  status: draft            # → approved only after human sign-off
  reviewed_by: 'Omnia Sana (owner-authorized)'
  reviewed_date: '2026-07-06'
```

---

## 6. Pipeline touch-points (exact)

Follows the `drug_class_interactions` path end-to-end.

1. **`validate.py`**
   - Load the vocab: `X = vocab_ids(os.path.join(VOCAB, "dangerous_plants.yaml"))`.
   - Add a constant `LOOKALIKE_SEVERITIES = {"fatal","dangerous","irritant","caution"}`.
   - Per plant, loop `d.get("dangerous_lookalikes", [])`: assert `dangerous_plant in X`
     (else `not in dangerous_plants vocab`), `severity in LOOKALIKE_SEVERITIES`,
     `status in SAFETY_STATUSES`. (`find_refs` already recurses the record, so
     `reference_ids` validate automatically.)
   - Optional but recommended (closes an audit gap): if `status == "approved"`,
     require non-empty `reviewed_by` and a `^\d{4}-\d{2}-\d{2}$` `reviewed_date`.

2. **`build.py`**
   - Load `dangerous_plants` vocab alongside `drug_classes` (near line 261) and
     build a public-safe `dp_public` that **strips `editor_notes`** (mirror `dc_public`).
   - In the `plants.json` loop, add
     `if "dangerous_lookalikes" in q: q["dangerous_lookalikes"] = approved_only(q["dangerous_lookalikes"])`
     next to the interactions/pairings `approved_only` calls — so `/plants` pages
     never leak a draft.
   - Add a `lookalike_rows(status)` emitter modeled on `interaction_rows`
     (**one-directional — NOT `pairing_rows`**), joining each row to the
     `dangerous_plants` vocab for label/toxicity, and carrying `lookalikes_review`
     so the front-end can render the three states. Write:
     - `build/lookalikes.v1.json` — approved-only, embeds `dp_public` (public feed).
     - `build/lookalikes.v1.draft.json` — all rows (review twin, **not** deployed).
   - **Register `lookalikes.v1.json` in the `manifest.json` filename list** (the
     `.draft` twin is intentionally excluded, like the interactions/pairings twins).
     *Easy-to-forget: `write()` and the manifest-list entry are two separate edits.*
   - Optionally add `dangerous_plants` to `vocab.json` for UI label lookups.

3. **Schema/vocab files:** add `schema/dangerous_plant.schema.json` +
   `vocabularies/dangerous_plants.yaml`; extend `plant.schema.json` as in §5.
   Note `schema/**` and `vocabularies/**` are CI build triggers.

4. **Deploy (data):** `python scripts/validate.py` → `python scripts/build.py` →
   commit → **`git push osdb main`** (the dedicated `omnia-sana-plant-database`
   repo the live WP tools pull from; CI also rebuilds `build/*.json`). **Never**
   push to `origin`/monorepo `main`; never force-push.

5. **WordPress tool** (lives in the WP monorepo, not this repo): a new
   `os_lookalikes_do_sync` mirrors `os_kf_do_sync` (SHA-gated pull of
   `build/lookalikes.v1.json` from the dedicated repo's `main`), a REST route
   `omniasana/v1/lookalikes` (`?herb=<id>` filter) serves it, and a virtual page
   `/dangerous-lookalikes/` + `/dangerous-lookalikes/{plant}/` renders it — exactly
   the `os-monograph.php` / `os-symptom-index.php` pattern. Public JSON is already
   approved-only, so the REST layer needs no extra gating.

---

## 7. Non-negotiable safety rules

- **Approved-only public.** Draft records never reach `lookalikes.v1.json`. The
  `safety_status` gate + `approved_only()` filter enforce this by default-deny.
- **Rock-solid features only.** A distinguishing feature that is subtle, reversible,
  or ambiguous does not go in — a forager may bet their life on it. If the only
  reliable answer is "don't forage this without an expert," say that.
- **Every claim sourced + human-signed-off** before `approved` (authoritative
  floras, university extension, poison-control/toxicology literature, peer-reviewed
  foraging-poisoning case reports; each added to `bibliography.bibtex` with a
  `study_type`).
- **Three-state honesty.** "Not researched" must never render as "safe".
- **Standing tool disclaimer.** The UI always shows: *this tool aids identification
  but does not replace an expert; when in doubt, throw it out.*
