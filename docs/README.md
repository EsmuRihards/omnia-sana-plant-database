# docs/ — data-architecture documentation

Human-facing documentation of how this database is structured and how it flows to
the public site. These files are **documentation, not data** — no build step reads
them and `validate.py` ignores them.

| File | What it is |
| --- | --- |
| `schema.html` | Interactive data-lineage map. Open in any browser. Three views: **Pipeline** (source YAML → `validate.py`/`build.py` → the nine `build/*.json` feeds → the WordPress tools), **Entity map** (how source records cross-reference each other by `id`), and **Evidence & gating** (the clinical 1–10 score, the inverted practice-band ladder, and the three publish gates). Every node, count and edge is traced from `schema/`, `scripts/build.py`, and the `novamira-sandbox` PHP handlers. |
| `omnia-sana.chartdb.sql` | The entity layer as a normalized PostgreSQL DDL, for opening in [ChartDB](https://chartdb.io) or any SQL ER tool. Import via **Import database → Query/DDL**. The real store is YAML/BibTeX; this is a relational *projection* so the tables + foreign keys render as a classic ER diagram. |

## Keeping it accurate

Both files are hand-authored snapshots. When the data model changes (a new entity
folder, a new `build/*.json` feed, a new tool consuming one), update:

- **Counts** — from `build/manifest.json` and `ls plants/ | wc -l` etc.
- **`schema.html`** — the `N` node object and the `FLOW` / `ENTITY` edge lists near
  the top of the inline `<script>`.
- **`omnia-sana.chartdb.sql`** — add the table + its foreign keys.

If a file here disagrees with `schema/*.json` or `scripts/build.py`, **the code wins** —
fix the doc.
