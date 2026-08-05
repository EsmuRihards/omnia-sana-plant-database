# AGENTS.md — Omnia Sana plant database

**Any AI agent or tool editing this repo: read [`DATA_PRINCIPLES.md`](DATA_PRINCIPLES.md)
first.** It is the model-agnostic source of truth for how this database is edited and
kept trustworthy. This file is only a pointer to it.

This repo is the backbone of **omniasana.bio**, a site people consult about what to put in
their bodies. Everything public is generated from the data here — a wrong fact here is
wrong everywhere it renders.

Two non-negotiables, in one line each (the full reasoning is in `DATA_PRINCIPLES.md`):

1. **Truthful or absent.** Never write a claim the cited source does not state, and make
   sure the source is about the *exact species* — wrong-species citations are the #1
   failure. If unsure, leave it empty.
2. **`python scripts/validate.py` must exit 0 before any commit.** It is the hard gate.
   Also glance at its `doc-sync` line: if it warns, the structure changed and
   `DATA_PRINCIPLES.md` needs reconciling.

Stamp your commit with which model made it: add a `Model: <provider/model>` trailer line
(see `DATA_PRINCIPLES.md` §7).

Tool-specific operational detail:
- **Claude Code**: also see `CLAUDE.md` and `.claude/skills/osdb-*`.
- **Everyone else**: `DATA_PRINCIPLES.md` is self-contained — start there.
