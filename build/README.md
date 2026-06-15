# Build outputs

Generated JSON consumed by the website tools. **Do not hand-edit** — these are
produced by `scripts/build.py` from the canonical data (plants, vocabularies,
bibliography) and rebuilt in CI.

- **`citations.json`** — Knowledge Finder (bibliographic metadata + plant/action linkage).
- **`symptoms.json`** — Symptom-to-Plant Lookup (plant↔condition with evidence).
- **`plants.json`** — plant pages and future tools (full public-safe index).
- **`vocab.json`** — UI filters (action/condition labels + synonyms).

Wired up in migration **Phase 6**.
