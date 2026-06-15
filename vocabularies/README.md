# Controlled vocabularies

The canonical lists that plant records reference by id. Keeping these closed and
curated is what prevents the free-text sprawl the old `medicinal_actions` field had
(338 distinct strings for ~860 entries).

- **`actions.yaml`** — pharmacological actions / mechanisms (e.g. `anti-inflammatory`,
  `antimicrobial`, `vulnerary`). Validated against `../schema/action.schema.json`.
- **`conditions.yaml`** — symptoms / conditions / indications, consumer-facing, with
  the free-text synonyms a user might search. Validated against
  `../schema/condition.schema.json`. This is the source of truth for the
  Symptom-to-Plant Lookup (replaces the in-page `META` map).

Populated in migration **Phase 2**.
