# Compounds

One YAML file per active compound / constituent (`<id>.yaml`), validated against
`../schema/compound.schema.json`. Plant records link here via
`constituents[].compound`, which makes plant↔compound and compound↔action
relationships queryable (e.g. "which plants contain apigenin?").

Enriched with external identifiers (PubChem CID, ChEMBL, CAS) where available.

Populated in migration **Phase 4**.
