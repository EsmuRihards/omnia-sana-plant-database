-- ============================================================================
--  Omnia Sana plant database — ENTITY-RELATIONSHIP MODEL (ChartDB import)
-- ============================================================================
--  This is a RELATIONAL PROJECTION of a file-based YAML/BibTeX database, written
--  so ChartDB (or any SQL ER tool) renders the entity layer as tables + keys.
--
--  The real store is NOT SQL. Each "table" below is a folder of YAML files or an
--  array inside a plant record:
--     plant              -> plants/<id>.yaml            (188 files)
--     compound           -> compounds/<id>.yaml         (75 files)
--     reference          -> bibliography.bibtex         (3,170 entries)
--     action/condition/… -> vocabularies/*.yaml
--     practice_record    -> practice/<id>.yaml
--     vernacular_name    -> names/<id>.yaml             (verified, machine-managed)
--  Arrays on a plant (indications[], actions[], pairings[]…) are modelled here as
--  child tables with foreign keys — that is the whole point of the diagram.
--
--  Dialect: PostgreSQL.  Import in ChartDB via "Import database → Query/DDL".
--  Field notes are trimmed from schema/*.json — see those files for the full contract.
-- ============================================================================

-- ─────────────────────────────  CORE ENTITIES  ─────────────────────────────

CREATE TABLE plant (
    id              TEXT PRIMARY KEY,          -- slug, e.g. 'taraxacum-officinale'
    scientific_name TEXT NOT NULL,
    family          TEXT NOT NULL,
    common_slug     TEXT,                      -- public /plants/<slug>/ (derived if absent)
    wp_post_id      INTEGER,                   -- WordPress Materia Medica post id
    provenance      TEXT,                      -- book | website | pubmed | combos
    status          TEXT NOT NULL,             -- verified | draft | needs-review
    last_updated    DATE NOT NULL
);

CREATE TABLE reference (                       -- the single bibliography (BibTeX)
    ref_id      TEXT PRIMARY KEY,              -- 'REF-0042' (== BibTeX cite key)
    type        TEXT NOT NULL,                 -- article | book | incollection | misc …
    title       TEXT,
    authors     TEXT,
    journal     TEXT,
    year        TEXT,
    doi         TEXT,
    url         TEXT,
    kind        TEXT DEFAULT 'publication',    -- publication | standard (pharmacopoeial)
    study_type  TEXT,                          -- systematic-review|rct|clinical|preclinical|traditional …
    abstract    TEXT                           -- REAL published abstract only
);

CREATE TABLE compound (
    id              TEXT PRIMARY KEY,          -- 'berberine', 'flavonoid'
    name            TEXT NOT NULL,
    class           TEXT,                      -- biosynthetic class (NOT extractive)
    resolution      TEXT DEFAULT 'unresolvable', -- exact | ambiguous | unresolvable (practice join)
    toxicity_flag   TEXT DEFAULT 'avoid-internal', -- none|dose-limited|topical-only|avoid-internal (fail-closed)
    regulatory_limit TEXT
);

CREATE TABLE action (                          -- vocabularies/actions.yaml (52)
    id       TEXT PRIMARY KEY,                 -- 'anti-inflammatory'
    label    TEXT NOT NULL,
    category TEXT
);

CREATE TABLE condition (                       -- vocabularies/conditions.yaml (70)
    id          TEXT PRIMARY KEY,              -- 'menstrual-cramps'
    label       TEXT NOT NULL,
    body_system TEXT NOT NULL,                 -- digestive | nervous | cardiovascular …
    icd10       TEXT,
    snomed      TEXT
);

CREATE TABLE drug_class (                      -- vocabularies/drug_classes.yaml (17)
    id       TEXT PRIMARY KEY,                 -- 'anticoagulants-antiplatelets'
    label    TEXT NOT NULL,
    category TEXT
);

CREATE TABLE dangerous_plant (                 -- vocabularies/dangerous_plants.yaml (80)
    id               TEXT PRIMARY KEY,          -- 'conium-maculatum'
    label            TEXT NOT NULL,
    scientific_name  TEXT NOT NULL,
    kingdom          TEXT,                      -- plant | fungus
    toxic_principle  TEXT NOT NULL,
    default_severity TEXT NOT NULL              -- fatal | dangerous | irritant | caution
);

CREATE TABLE solvent            ( id TEXT PRIMARY KEY, label TEXT ); -- solvents.yaml (18)
CREATE TABLE extraction_class   ( id TEXT PRIMARY KEY, label TEXT ); -- extraction_classes.yaml (26)
CREATE TABLE extraction_method  ( id TEXT PRIMARY KEY, label TEXT ); -- extraction_methods.yaml (20)

CREATE TABLE language (                         -- vocabularies/languages.yaml (34)
    code    TEXT PRIMARY KEY,                    -- ISO 639-1, e.g. 'lv'
    name_en TEXT NOT NULL,
    script  TEXT,
    tier    TEXT                                 -- eu-official | non-eu-major
);

-- ───────────────────────  PLANT CLAIM CHILD TABLES  ─────────────────────────
--  Each array on a plant record. Every claim carries reference_ids + a status.

CREATE TABLE plant_action (
    id         SERIAL PRIMARY KEY,
    plant_id   TEXT NOT NULL REFERENCES plant(id),
    action_id  TEXT NOT NULL REFERENCES action(id),
    note       TEXT,
    status     TEXT NOT NULL                     -- verified | draft | needs-review
);

CREATE TABLE plant_indication (                  -- powers the Symptom-to-Plant Lookup
    id                SERIAL PRIMARY KEY,
    plant_id          TEXT NOT NULL REFERENCES plant(id),
    condition_id      TEXT NOT NULL REFERENCES condition(id),
    evidence_override INTEGER,                    -- optional 1..10; else COMPUTED at build
    status            TEXT NOT NULL               -- needs-review => 'inferred' in symptoms.json
);

CREATE TABLE plant_constituent (
    id       SERIAL PRIMARY KEY,
    plant_id TEXT NOT NULL REFERENCES plant(id),
    name     TEXT NOT NULL                        -- verbatim free-text constituent name
);

CREATE TABLE plant_constituent_compound (        -- constituent -> compound entity (M:N)
    constituent_id INTEGER NOT NULL REFERENCES plant_constituent(id),
    compound_id    TEXT    NOT NULL REFERENCES compound(id),
    PRIMARY KEY (constituent_id, compound_id)
);

CREATE TABLE plant_contraindication (
    id       SERIAL PRIMARY KEY,
    plant_id TEXT NOT NULL REFERENCES plant(id),
    severity TEXT,                                -- info | caution | warning | serious
    note     TEXT NOT NULL,
    status   TEXT NOT NULL
);

CREATE TABLE plant_preparation (                 -- withheld from plants.json if unsourced (D8)
    id       SERIAL PRIMARY KEY,
    plant_id TEXT NOT NULL REFERENCES plant(id),
    name     TEXT NOT NULL,
    text     TEXT,
    status   TEXT
);

CREATE TABLE plant_dosage (                      -- withheld from plants.json if unsourced (D8)
    id       SERIAL PRIMARY KEY,
    plant_id TEXT NOT NULL REFERENCES plant(id),
    name     TEXT NOT NULL,
    text     TEXT,
    status   TEXT
);

-- ─────────────────────  SAFETY LISTS (approved-only)  ───────────────────────
--  These use a SEPARATE lifecycle: status draft | approved. Public tools serve
--  'approved' only.

CREATE TABLE plant_drug_interaction (            -- Herb-Drug Interaction Checker
    id            SERIAL PRIMARY KEY,
    plant_id      TEXT NOT NULL REFERENCES plant(id),
    drug_class_id TEXT NOT NULL REFERENCES drug_class(id),
    severity      TEXT NOT NULL,                  -- avoid|caution|likely-safe|insufficient
    mechanism     TEXT,
    status        TEXT NOT NULL DEFAULT 'draft'   -- draft | approved
);

CREATE TABLE plant_pairing (                     -- Herb-Herb Combinations (self-referencing, mirrored)
    id               SERIAL PRIMARY KEY,
    plant_id         TEXT NOT NULL REFERENCES plant(id),
    partner_plant_id TEXT NOT NULL REFERENCES plant(id),
    type             TEXT NOT NULL,               -- synergy|neutral|caution|avoid
    note             TEXT,
    status           TEXT NOT NULL DEFAULT 'draft'
);

CREATE TABLE plant_dangerous_lookalike (         -- Dangerous Lookalikes (one-directional)
    id                 SERIAL PRIMARY KEY,
    plant_id           TEXT NOT NULL REFERENCES plant(id),
    dangerous_plant_id TEXT NOT NULL REFERENCES dangerous_plant(id),
    severity           TEXT NOT NULL,             -- fatal|dangerous|irritant|caution
    confused_part      TEXT,
    key_test           TEXT,
    status             TEXT NOT NULL DEFAULT 'draft'
);

-- ─────────────────────────  CLAIM → REFERENCE links  ────────────────────────
--  Every claim's reference_ids[]. Modelled per claim table so the ER shows how
--  the single bibliography is cited from all over. (build.py's find_refs walks
--  these; validate.py checks each REF resolves.)

CREATE TABLE indication_reference (
    indication_id INTEGER NOT NULL REFERENCES plant_indication(id),
    ref_id        TEXT    NOT NULL REFERENCES reference(ref_id),
    PRIMARY KEY (indication_id, ref_id)
);
CREATE TABLE action_reference (
    plant_action_id INTEGER NOT NULL REFERENCES plant_action(id),
    ref_id          TEXT    NOT NULL REFERENCES reference(ref_id),
    PRIMARY KEY (plant_action_id, ref_id)
);
CREATE TABLE constituent_reference (
    constituent_id INTEGER NOT NULL REFERENCES plant_constituent(id),
    ref_id         TEXT    NOT NULL REFERENCES reference(ref_id),
    PRIMARY KEY (constituent_id, ref_id)
);
CREATE TABLE plant_reference (                   -- plant-level background refs[]
    plant_id TEXT NOT NULL REFERENCES plant(id),
    ref_id   TEXT NOT NULL REFERENCES reference(ref_id),
    PRIMARY KEY (plant_id, ref_id)
);
CREATE TABLE compound_reference (
    compound_id TEXT NOT NULL REFERENCES compound(id),
    ref_id      TEXT NOT NULL REFERENCES reference(ref_id),
    PRIMARY KEY (compound_id, ref_id)
);

CREATE TABLE compound_action (                   -- compound credited with a mechanism
    compound_id TEXT NOT NULL REFERENCES compound(id),
    action_id   TEXT NOT NULL REFERENCES action(id),
    PRIMARY KEY (compound_id, action_id)
);

CREATE TABLE action_related_condition (          -- action -> indication bridge
    action_id    TEXT NOT NULL REFERENCES action(id),
    condition_id TEXT NOT NULL REFERENCES condition(id),
    PRIMARY KEY (action_id, condition_id)
);

-- ───────────────────────────  VERNACULAR NAMES  ─────────────────────────────
--  names/<id>.yaml — machine-managed by verify_names.py; feeds the Name Dictionary.

CREATE TABLE vernacular_name (
    id            SERIAL PRIMARY KEY,
    plant_id      TEXT NOT NULL REFERENCES plant(id),
    language_code TEXT NOT NULL REFERENCES language(code),
    name          TEXT NOT NULL,
    preferred     BOOLEAN DEFAULT FALSE,
    status        TEXT NOT NULL                    -- verified (served) | needs-review (held)
);

-- ─────────────────────  PRACTICE CORPUS (extraction)  ───────────────────────
--  practice/<id>.yaml — the inverted evidence ladder; feeds the Tincture Calculator.

CREATE TABLE practice_record (
    id                 TEXT PRIMARY KEY,           -- 'curcumin--ethanol-water--maceration'
    record_type        TEXT NOT NULL,              -- extraction|stability|dose-form-conversion (live)
    parameter_kind     TEXT NOT NULL,              -- empirical | normative
    species_scope      TEXT NOT NULL,              -- class-general | species-specific
    species            TEXT,                       -- binomial (species-specific only)
    key_compound_id    TEXT NOT NULL REFERENCES compound(id),
    key_extraction_class TEXT REFERENCES extraction_class(id),
    key_solvent        TEXT NOT NULL REFERENCES solvent(id),
    key_method         TEXT NOT NULL REFERENCES extraction_method(id),
    status             TEXT NOT NULL DEFAULT 'draft', -- draft (never ships) | approved
    reviewed_by        TEXT,
    verified_by        TEXT,                       -- MUST differ from reviewed_by (two-person rule)
    last_updated       DATE NOT NULL
);

CREATE TABLE practice_finding (                    -- one paper, one condition set, one number
    id             TEXT PRIMARY KEY,               -- record-local 'F1'… (global here for FK)
    practice_id    TEXT NOT NULL REFERENCES practice_record(id),
    ref_id         TEXT NOT NULL REFERENCES reference(ref_id),
    method_type    TEXT NOT NULL,                  -- optimisation|comparative-bench|characterisation|pharmacopoeial…
    design         TEXT,                           -- rsm-ccd|factorial|single-condition|normative …
    material_species TEXT,                         -- AS PRINTED in the paper
    varied_factor  TEXT,                           -- solvent_pct|temperature_c|time_min|solid_liquid_ratio …
    analyte        TEXT,
    value          NUMERIC,
    unit           TEXT
);

CREATE TABLE practice_recommendation (             -- what the calculator may say
    id            SERIAL PRIMARY KEY,
    practice_id   TEXT NOT NULL REFERENCES practice_record(id),
    parameter     TEXT NOT NULL,                   -- solvent_pct|temperature_c|solid_liquid_ratio|drug_extract_ratio …
    solvent       TEXT REFERENCES solvent(id),
    method        TEXT REFERENCES extraction_method(id),
    route         TEXT NOT NULL,                   -- internal | topical
    statement     TEXT
);

CREATE TABLE practice_plant_link (                 -- species_overrides[].plant_id
    practice_id TEXT NOT NULL REFERENCES practice_record(id),
    plant_id    TEXT NOT NULL REFERENCES plant(id),
    PRIMARY KEY (practice_id, plant_id)
);

-- ============================================================================
--  READING THE DIAGRAM
--  • plant is the primary hub: 9 child tables hang off it.
--  • reference is the second hub: every *_reference table + practice_finding cite it.
--  • compound bridges plant chemistry to the practice corpus (join key).
--  • plant_pairing is self-referential (plant ↔ plant).
--  • Safety tables (plant_drug_interaction, plant_pairing, plant_dangerous_lookalike)
--    carry status draft|approved — only 'approved' rows reach the public build feeds.
--  • plant_indication.evidence_override is the ONLY hand-set score; every other
--    evidence number is computed in scripts/build.py from reference.study_type.
-- ============================================================================
