---
name: osdb-add-plant
description: "Add a new plant record to the Omnia Sana database, extend an existing one, or add a new schema field. Use whenever writing to plants/*.yaml, adding a species, filling monograph fields (botanical_description/habitat/harvesting/traditional_uses/preparations/dosage), wiring actions/indications/constituents, or changing schema/*.json. Covers the future-proofing checklist any new field must pass."
---

# Adding to the plant database

`README.md` has the mechanics — schema fields, evidence scoring, `REF-XXXX`
convention. Read it for *what a field is*. This skill is *how to decide what goes
in it*, and it assumes you have read `CLAUDE.md` (the five invariants).

## Before you write anything

1. **Does the record already exist?** `ls plants/ | grep <genus>`. Extending beats
   creating — a duplicate species under a synonym is very hard to unpick later.
2. **Confirm the accepted binomial.** Check the synonym isn't the accepted name
   (or vice versa). Put taxonomic synonyms in `synonyms[]` so future searches and
   the EMA/WHO register cross-matches find the record.
3. **Get `external_ids` first** (`wikidata`, `gbif`, `powo`). These anchor
   botanical identity, and CI's name-verification step needs them to harvest
   vernacular names for a new plant. A record without them is a record whose
   identity you cannot later prove.

## Writing the record

Required, always: `id`, `scientific_name`, `common_names`, `family`, `status`,
`last_updated`. `family` must be a real botanical family — validate.py warns on
`Unknown`, and a warning here means the record shipped unidentified.

**`id`** is the lowercase scientific name, spaces → hyphens. It is permanent —
every downstream artifact, URL and cross-reference keys off it. Renaming one is a
migration, not an edit.

### Claim-bearing fields

`actions[]`, `indications[]`, `constituents[]`, `contraindications[]`,
`preparations[]`, `dosage[]` and the monograph prose blocks each carry their own
`reference_ids` and `status`. That per-claim sourcing is the whole point of the
schema — it is what makes an evidence score mean something.

**Wire references claim-by-claim.** The temptation is to paste the plant's whole
bibliography onto every indication. Don't. Evidence scores are computed from the
references *on that indication*; a blanket paste gives every condition the
strongest source's score and silently destroys the signal. If a reference supports
the diuretic claim and not the anti-inflammatory one, it belongs on one of them.

Sources that back the plant generally — identification, distribution, an overview
— go in the top-level `references[]` bucket, not on a claim.

**`note` preserves the source's own phrasing.** Keep it verbatim where you can. It
is the audit trail for what the source actually said, and the thing that lets a
later reviewer catch a drifted paraphrase.

**`status` per claim:** `verified` (sourced and checked, publishable) / `draft`
(written, not source-checked, do not publish) / `needs-review` (conflicting or
weak). Record-level `status` is governed by the lowest-confidence claim.

Safety-bearing arrays (`drug_class_interactions`, `pairings`,
`dangerous_lookalikes`) use a **separate** enum — `draft` | `approved` — and the
public tools serve `approved` only. `approved` additionally requires `reviewed_by`
and a `YYYY-MM-DD` `reviewed_date`. That gate is a medical sign-off, not a
formality; do not set it to clear a validation error.

### Vocabulary-bound fields

`actions[].action` → `vocabularies/actions.yaml`
`indications[].condition` → `vocabularies/conditions.yaml`
`constituents[].compounds[]` → `compounds/<id>.yaml`
`drug_class_interactions[].drug_class` → `vocabularies/drug_classes.yaml`
`dangerous_lookalikes[].dangerous_plant` → `vocabularies/dangerous_plants.yaml`

validate.py hard-errors on an unknown id. If the concept genuinely doesn't exist
yet, add it to the vocabulary deliberately — with a definition — rather than
bending the claim to fit an existing term. A forced fit is a quiet mistranslation
of the source. (Known trap: `triterpene` is not a valid compound id.)

### Absence is a value

`lookalikes_review` exists because "researched, none known" and "not yet
researched" are different facts, and the tool must not render the second as safe.
When you finish researching something and find nothing, **say so explicitly** —
outcome `none-known` with the sources that support it. Silence is not a finding.

Apply that pattern generally: a documented dead end in `internal_notes` beats an
empty field with no explanation.

## Adding a new schema field

Any new field must pass all five before it is committed:

1. **`schema/*.json` entry** with a real `description`. `additionalProperties` is
   `false` — an undeclared field is a hard validation failure, by design.
2. **`scripts/validate.py` rule** if the field has any constraint beyond its type
   (enum, id-resolves-to-vocabulary, range, cross-record reference).
3. **`scripts/build.py` handling** — decide which `build/*.json` it flows into, or
   deliberately none.
4. **At least one downstream consumer**, or an explicit note saying it is
   deliberately internal. A field nothing reads is a field that will silently rot.
5. **Defined behaviour when absent** on the other 186 plants. This is the one that
   gets skipped. Renderers must degrade to "not shown", never to "empty section"
   or a crash — the Monograph generator is field-agnostic precisely so a data
   addition never forces a front-end change. Preserve that property.

Additive only. Removing or renaming a field breaks live pages, cached tool JSON,
and any external consumer of `build/*.json`.

## Finishing

```bash
python scripts/validate.py     # must exit 0
python scripts/build.py
```

Set `last_updated` to today. Add an `internal_notes` line recording what you did
and what you deliberately left out — that note is what makes the next session
cheap. Append; never reflow existing notes.

Then `osdb-deploy` to get it live.
