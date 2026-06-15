# Ingestion (archive)

`archive/` holds the one-shot, dated ingestion and enrichment scripts and the raw
source data they consumed (`archive/sources/`). They are kept for **provenance and
reproducibility** — they document exactly how records entered the database — but are
**not part of the active toolchain**.

The reusable tooling (the validator and the single builder) lives in `../scripts/`.

Large regenerable caches/logs here (`_abstract_cache.json`, `abstracts_log_*.txt`)
are git-ignored.
