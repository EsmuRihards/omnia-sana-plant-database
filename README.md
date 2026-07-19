# Omnia Sana — Plant Fact Database

A canonical, version-controlled database of medicinal-plant facts and the
scientific sources that back them. This repository is the **single source of
truth** for plant content across the book, blog, Materia Medica, and any
interactive tools. Anything published anywhere should trace back to a record
here.

---

## Why this exists

Plant facts were previously scattered across drafts, posts, and notes, each with
its own (often missing) citations. This database fixes that:

- **One fact, one place.** Each plant has exactly one record.
- **Every claim is sourced.** Claims point to references by id; references live
  in one bibliography.
- **Claims carry a status.** `verified`, `draft`, or `needs-review`, so it is
  always clear what is safe to publish.
- **It is diffable.** Plain-text YAML + BibTeX under Git — every change is
  reviewable.

---

## Folder structure

```
plant-database/
├── .gitignore
├── README.md
├── bibliography.bibtex         # every scientific reference, one BibTeX entry each
├── schema/                     # JSON Schemas — the data contract for each entity
│   ├── plant.schema.json   compound.schema.json   source.schema.json
│   └── action.schema.json  condition.schema.json
├── plants/                     # one YAML per species (the human editing unit)
├── compounds/                  # one YAML per active compound / class entity
├── vocabularies/               # controlled vocab: actions.yaml, conditions.yaml
├── build/                      # generated JSON the website consumes (built in CI)
│   └── citations.json  symptoms.json  plants.json  vocab.json
├── scripts/
│   ├── validate.py             # integrity checker (refs + vocab + schema)
│   └── build.py                # builds all build/*.json from the canonical data
├── ingest/
│   └── archive/                # one-shot ingestion/migration scripts + raw sources
└── .github/workflows/
    ├── validate.yml            # CI: scripts/validate.py on every push/PR
    └── build-and-publish.yml   # CI: rebuild + commit build/*.json on data change
```

### File-naming convention

Each plant is one file in `plants/`, named after its **lowercase scientific
name with the space replaced by an underscore**:

| Scientific name        | File name                    |
| ---------------------- | ---------------------------- |
| *Taraxacum officinale* | `taraxacum_officinale.yaml`  |
| *Zingiber officinale*  | `zingiber_officinale.yaml`   |

Use only `[a-z0-9_]`. Drop authorship abbreviations (e.g. `L.`, `Mill.`).

---

## The plant record schema

```yaml
common_names:
  - Name 1
  - Name 2

scientific_name: Genus species

family: Plant Family

parts_used:
  - name: "Leaf"
    medicinal_actions:
      - action: "Diuretic"
        reference_ids: ["REF-0001", "REF-0002"]
        status: "verified"
      - action: "Anti-inflammatory"
        reference_ids: ["REF-0003"]
        status: "draft"
  - name: "Root"
    medicinal_actions:
      - action: "Bitter tonic"
        reference_ids: ["REF-0004"]
        status: "verified"

constituents:
  - name: "Flavonoids"
    note: "Including luteolin and apigenin"
    reference_ids: ["REF-0005"]

contraindications:
  - note: "May interact with diuretic medications"
    reference_ids: ["REF-0007"]
    status: "verified"

internal_notes: "Any editorial notes or flags"
last_updated: "2026-06-12"
status: "verified"   # verified | draft | needs-review
```

### Field notes

- **`parts_used[].name`** — the plant part(s) the actions are attributed to.
  When a source maps a specific action to a specific part (e.g. Dandelion leaf =
  diuretic, root = bitter tonic), use one entry per part. When a source lists
  parts and actions as **flat, unmapped lists** (as much of the book manuscript
  does), the actions are grouped under a single `parts_used` entry whose name
  joins the parts with `/` (e.g. `"Flower / Leaf / Root"`). This is an honest
  signal that the part↔action split was not specified by the source.
- **`reference_ids`** — a list of `REF-XXXX` ids. Each must resolve to a BibTeX
  entry (see below).
- **`status`** — per-claim status. The top-level `status` is the record-level
  status (the lowest-confidence claim usually governs it).

---

## Evidence scoring (1–10, computed)

Each indication's strength is **not stored by hand** — it is computed
deterministically at build time (`scripts/build.py`) from the **study types of the
references that back it**. There is no AI and no opaque "publication count": the
same data always yields the same score, and every score is auditable from its
`reference_ids`.

The rule (Option B):

```
base  = score of the STRONGEST single cited source (best tier)
bonus = reward for a BODY of HUMAN evidence (number of review/rct/clinical sources)
score = clamp(base + bonus, 1, 10)
```

| Strongest source tier | base | Human-source count | bonus |
| --------------------- | ---- | ------------------ | ----- |
| systematic-review     | 7    | ≥ 5                | +3    |
| rct                   | 5    | 3–4                | +2    |
| clinical (other human)| 3    | 2                  | +1    |
| preclinical           | 2    | < 2                | +0    |
| traditional           | 1    |                    |       |

Worked examples: one RCT = **5**; three RCTs = **7**; a meta-analysis backed by
≥5 human trials = **10**; any number of in-vitro/animal sources only = **2**;
traditional sources only = **1**. Preclinical and traditional **volume never
raises the score** — ten in-vitro studies are still not clinical evidence.

> ⚠️ A score is only as specific as the indication's `reference_ids`. Where a
> record pins its whole strong bibliography to *every* indication, each indication
> inherits the maximum. Tightening which references back which condition (claim-
> level sourcing) is what makes individual scores meaningful.

**Editorial override.** Add `evidence_override: N` (1–10) to an indication to force
a value; the build uses it verbatim instead of computing.

---

## Reference id convention

References are identified by ids of the form **`REF-XXXX`**, zero-padded to at
least four digits (`REF-0001`, `REF-0042`, `REF-1234`).

Each id maps to one entry in `bibliography.bibtex`. The link is stored in the
BibTeX entry's `note` field:

```bibtex
@article{clare2009dandelion,
  author  = {Clare, B. A. and Conroy, R. S. and Spelman, K.},
  title   = {The diuretic effect in human subjects of an extract of {Taraxacum officinale}},
  journal = {Journal of Alternative and Complementary Medicine},
  year    = {2009},
  volume  = {15},
  number  = {8},
  pages   = {929--934},
  doi     = {10.1089/acm.2008.0152},
  note    = {REF-0042}
}
```

So a plant YAML cites `REF-0042`, and `scripts/validate.py` confirms that a
BibTeX entry carries `note = {REF-0042}`.

### Abstracts (optional)

Scientific-publication entries (`@article`) may carry an optional **`abstract`**
field holding the publication's official abstract:

```bibtex
@article{clare2009dandelion,
  ...
  note     = {REF-0042},
  abstract = {Dandelion (Taraxacum officinale) has a long history of use ...}
}
```

- Stored on a **single line** with braces removed and whitespace collapsed, so
  the lightweight regex parsers in the builders (`build_citations_json.py` and
  the live PHP port) read it without brace-depth or terminator surprises.
- Populated reproducibly by `tools/add_abstracts_2026_06_14.py` (Europe PMC by
  DOI, then by title with a similarity guard, then Crossref). Re-running is
  idempotent — entries that already have an `abstract` are skipped.
- Surfaced by the Knowledge Finder's **"View Abstract"** button. Entries with no
  publicly available abstract simply omit the field (the button is hidden).

### Study type (evidence tier)

Every entry carries an explicit **`study_type`** field — the keyword-free signal
that drives both the source-card ordering and the 1–10 evidence scoring above:

```bibtex
@article{abdelmonem2022hibiscus,
  ...
  note       = {REF-0566},
  study_type = {systematic-review},
  abstract   = {We aimed to assess the efficacy of Hibiscus sabdariffa ...}
}
```

- Allowed values (strongest → weakest): **`systematic-review`**, **`rct`**,
  **`clinical`** (other human studies — cohort, open-label, case report),
  **`preclinical`** (in vitro / animal), **`traditional`** (books, monographs,
  websites, ethnobotany).
- When you add a reference, **set `study_type` by hand** — it is the one field the
  scoring depends on. `scripts/build.py` falls back to a title/abstract keyword
  heuristic only for an entry that is missing it, so the build never breaks, but
  an explicit value is always preferred.
- The existing values were seeded once from that heuristic by
  `ingest/archive/backfill_study_type_2026_06_19.py`; spot-check and correct as
  needed (the `@misc` web sources default to `traditional`, journal articles
  without trial wording default to `preclinical`).

---

## How to add a new plant

1. Create `plants/<lowercase_scientific_name>.yaml` following the schema above.
2. For every claim, add or reuse references in `bibliography.bibtex` and cite
   them by `REF-XXXX` id.
3. Set each claim's `status` (`verified` / `draft` / `needs-review`).
4. Set `last_updated` to today and the top-level `status`.
5. Run the validator:
   ```bash
   python scripts/validate.py
   ```
6. Commit (see syncing below).

## How to add or update a source in the bibliography

1. Pick the next free `REF-XXXX` id. To see the highest id in use:
   ```bash
   grep -ho "REF-[0-9]\+" bibliography.bibtex | sort -u -V | tail -1
   ```
   The `-V` matters: a plain `sort` is lexicographic and is only correct while
   every id has four digits. From `REF-10000` on it silently returns a lower id
   than the true maximum, handing you an id that is already taken.
2. Add a BibTeX entry. Choose a citation key of the form
   `lastnameYEARkeyword` (e.g. `clare2009dandelion`). Put the `REF-XXXX` id in
   the `note` field.
3. Keep entries **sorted alphabetically by citation key**.
4. Reference the new id from the relevant plant YAML.
5. Run `python scripts/validate.py`.

## How to mark a claim's status

Use the `status` field on each action / contraindication, and the top-level
record `status`:

- **`verified`** — sourced and checked; safe to publish.
- **`draft`** — written but not yet source-checked; do not publish.
- **`needs-review`** — flagged for a second look (conflicting sources, weak
  evidence, possible error).

---

## Validating

```bash
python scripts/validate.py
```

- **Exit 0** — every cited `REF-XXXX` resolves to a BibTeX entry.
- **Exit 1** — there are missing or malformed references (a hard error).
- Orphaned references (in the bibliography but never cited) are printed as
  warnings and do **not** fail the check.

CI runs this automatically on every push and pull request
(`.github/workflows/validate.yml`).

---

## Data provenance

Records come from three ingestion passes, all reproducible from `ingest/archive/`
(the one-shot scripts were moved there during the architecture migration):

1. **Book manuscript** (`ingest_book.py`) — 96 species from the Omnia Sana book,
   `status: verified`. Parts and actions are flat/unmapped (see the note above),
   with plant-level references.
2. **omniasana.bio Materia Medica pages** (`add_dandelion.py`,
   `ingest_website.py`) — fully part-mapped, well-cited records:
   Dandelion, White Dead Nettle (new), and enrichment of the existing Greater
   Plantain and Yarrow records with site-sourced constituents, actions and
   cautions. `status: verified`.
3. **Symptom-to-Plant Lookup tool** (`ingest_website.py`, from
   `ingest/archive/sources/symptom_lookup.json`) — 77 plants imported as **skeletal
   records**: a single `Whole plant` part whose actions are the symptoms the
   tool associates with the plant, each tagged with the tool's evidence score
   (`evidence N/4`) and citing the tool itself. These are
   `status: needs-review` (associations to be confirmed against primary
   literature, not independently verified). They are the obvious next target
   for enrichment.

Re-running an ingestion script regenerates its records; the scripts are additive
and the bibliography re-sorts alphabetically while preserving `REF-XXXX` ids.

## Syncing with GitHub

> ⚠️ **Never `git push` this repo to `origin/main`, and never force-push.** This
> local repo has a **separate, unrelated history** from the GitHub copy, and `main`
> on the `EsmuRihards/OmniaSana` repo is the **live WordPress site export** —
> pushing the database onto it would overwrite the website.

The GitHub master copy of this database lives in the **`EsmuRihards/OmniaSana`**
monorepo on the **`add-plant-database`** branch, inside a **`plant-database/`**
subdirectory that mirrors this repo's root. **That branch — not `main`** — is what
the website's Knowledge Finder pulls from. This local repo has **no `origin`
remote**; it is a standalone history.

Day-to-day:

```bash
# 1. Work locally; ALWAYS validate before committing.
python scripts/validate.py
git add .
git commit -m "Describe what changed"

# 2. Deploy: port the new commit into the remote add-plant-database branch's
#    plant-database/ subdir (fast-forward, non-destructive). Export the patch:
git diff HEAD~1 HEAD > ../batch.patch
#    then, in a checkout of EsmuRihards/OmniaSana on the add-plant-database branch:
#      git apply --directory=plant-database /path/to/batch.patch
#      git commit -am "plant-database: describe what changed"
#      git push origin add-plant-database
```

CI runs `scripts/validate.py` on every push/PR (`.github/workflows/validate.yml`).

> **Planned improvement:** move this database into its own dedicated repository so
> syncing becomes a normal `git push` (no worktree-patch step). See the architecture
> audit (`../plant-database-architecture-audit.md`) for the full migration plan.
