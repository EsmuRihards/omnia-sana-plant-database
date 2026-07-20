# The applied practice corpus

The second corpus. `plants/` answers *what does this species do in people*;
`practice/` answers *what actually comes out of this material under these
conditions, and how do we know*. It exists because the site's tincture and
formula calculators currently hardcode `PART_RATIOS`, `DEFAULT_RATIO 1:5`,
`GLYCERITE_MIX 75/25` and the `shelfLife` bands in JavaScript with zero
provenance, and an unsourced default is honest only for as long as nobody
pretends otherwise.

One file per record: `practice/<id>.yaml`. Validated against
`../schema/practice.schema.json` — which is a **documentation contract only**.
Nothing in this repo loads JSON Schema. Every rule that actually runs is
imperative Python in `../scripts/validate.py`. If the two disagree, the schema
is the bug.

## The ladder is upside down here

Do not carry clinical instincts across.

| clinical (`TIER_BASE`) | practice (`method_type`) |
| --- | --- |
| review / meta-analysis = 7 | **method-review = 0, and inadmissible in `findings[]`** |
| RCT = 5 | no tier — irrelevant to extraction |
| preclinical bench = 2 | **optimisation = 7** |
| volume of human evidence = bonus | **independent replication = bonus** |
| null results bucketed out | **discordant results stay in and cost points** |

A review of extraction methods scores zero. That is arithmetic, not a slight: it
cannot report a single (solvent, temperature, time, ratio, measured yield)
tuple, because it did not run the experiment. `validate.py` rejects
`method-review` and `traditional-text` inside `findings[]` as a hard error. Put
them in `context_reference_ids[]`, where they inform your prose and contribute
nothing, and go find the primary papers they cite.

`method_type` lives on the **finding**, not on the bibtex entry. One paper can be
`optimisation` for the solvent axis and `characterisation` for temperature, and
reusing an existing clinical `REF-XXXX` in a practice finding requires no edit to
`bibliography.bibtex` at all.

## Anti-skim: what it does and does not do

Every required field was chosen against one test — *could this be fabricated
plausibly by someone who read only the abstract?* `locator.table`,
`comparator_levels` (the **full** level set, not just the winner),
`solid_liquid_ratio`, `quantification`, `unit_basis` and `reference_standard`
are all Methods-and-Results data.

Be honest about what that buys. These fields are checked **against each other**,
so a determined fabricator satisfies them all from one imagined number. What the
design actually delivers is **auditability**: a wrong `Table 3` is checkable by a
second reader in thirty seconds. Two fields make that real, and they are
required at `approved`:

- `fulltext_source` — where the PDF came from. There is no value meaning
  "abstract only", because an abstract cannot produce a finding.
- `verified_by` + `verified_date`, which **must differ from `reviewed_by`**. A
  second person opened the papers.

Do not describe this corpus as making fabrication impossible. It makes it
auditable, and it makes carelessness detectable.

## The three hard gates

1. **Solvent.** `recommendation.solvent` is required. The extrapolation envelope
   is built only from findings in the **same solvent** varying the **same
   parameter**. A methanol sweep of 20/40/60/80 does not legitimise an ethanol
   band of 60-75. Findings in lab solvents are welcome — they are good evidence
   about polarity — but `consumer_safe: false` in `../vocabularies/solvents.yaml`
   is a hard error on a recommendation, as is `consumer_reproducible: false` in
   `extraction_methods.yaml`.
2. **Toxicity.** A recommendation is a preparation that is safe and
   traditionally correct. It is **never the argmax of a yield table**. Any record
   whose `key.compound_id` carries a non-`none` `toxicity_flag` needs a
   `limit_rationale` and a second reviewer. This is not theoretical: `alkaloid`
   sits on 17 plants including comfrey, butterbur, coltsfoot, borage,
   greater celandine and arnica, where the alkaloid fraction *is* the toxicity.
   `coumarin` sits on 19. `recommendation.route` (`internal` | `topical`) is
   required, and arnica is the reason.
3. **Copyright.** Pharmacopoeial monographs are paywalled normative texts. Cite
   `locator.edition` + `locator.monograph`, paraphrase the requirement in one
   sentence in `statement_summary` (≤300 chars, enforced), and never populate
   `abstract` on a `kind: standard` bibliography entry — the Knowledge Finder
   renders `abstract` *as the source's own words*.

## What v1 does not do

- **`key.part` is frozen to `null`.** `plants[].parts_used` is 58 distinct
  free-text strings with no enum and no validation rule, and `constituents[]`
  carries no part attribution at all, so the part axis cannot be populated from
  plant data. `validate.py` rejects any non-null value. `PART_RATIOS` stays
  hardcoded and labelled unsourced. There is no `vocabularies/parts.yaml`.
- **The calculator never emits a single menstruum.** Chamomile flower carries
  mucilage (cold water; ethanol above ~30% precipitates it) *and* bisabolol
  (70-96% ethanol). Both records are correct and they disagree. The output is a
  **per-constituent table** plus the standing line *"a tincture captures the
  volatile fraction and loses the mucilage"* — never one number. Thirteen plants
  have this collision today.
- **A plant gets a recommendation only when it opts in by resolving.** The
  constituent must resolve unambiguously to one `extraction_class`, and the
  keyed compound's `toxicity_flag` must be `none`. Absent, ambiguous or
  unresolvable → nothing. `flavonoid` (132 plants), `tannin` (42),
  `polysaccharide` (36), `glycoside`, `phenolic-compound` and `terpene` are all
  ambiguous until disambiguated on the compound record or on
  `plants[].constituents[].extraction_class`.
- **Eight plant records will be excluded outright** by `PRACTICE_PLANT_EXCLUSIONS`
  in `build.py`, declared and consumed when the plant→practice join lands (D5) —
  it does not exist today, and nothing joins to a plant yet. Their own data would
  make the join wrong: the seven fungal records that declare `Whole Plant`
  (`trametes-versicolor`, `psilocybe-cubensis`, `pleurotus-ostreatus`,
  `lentinula-edodes`, `inonotus-obliquus`, `ganoderma-lingzhi`,
  `cordyceps-militaris` — fruiting body, mycelium and sclerotium are different
  materials with different beta-glucan content) and `allium-sativum`, which lacks
  `Bulb` entirely while carrying `allicin`. Ids are hyphenated: that is the `id:`
  field, not the filename.

## Species scope

`species-specific` — invariant 2 unchanged. Every finding's binomial must match
the record's. A *Silybum eburneum* paper on a *Silybum marianum* record is the
same error it has always been.

`class-general` — the claim is about a class of molecule in a kind of matrix, so
a *Taraxacum* flavonoid solvent curve is legitimate evidence. Rejecting
off-species data here would reject the corpus wholesale. But generalising is
never silent: `generalisation.basis`, a `rationale` a chemist could disagree
with (≥80 chars, enforced), and ≥2 genera before `approved`. `source_taxa` is
**derived** from `findings[].material.species` in `build.py` — do not author it.
`excluded_taxa` *is* authored, and these are the species that break their class
and are invisible in an abstract: *Allium sativum* (process-limited,
alliinase-dependent), *Berberis*/*Mahonia* (berberine is quaternary and
water-soluble regardless of pH), *Hericium erinaceus* (its part reads `Fruit`,
meaning fruiting body), *Hypericum perforatum* (hyperforin degrades on a
maceration timescale), anything mucilaginous.

## Discordance is data

A paper measuring the optimum at 85% when your band says 60-75 is not a null; it
is a measurement of your parameter that disagrees with you. It stays in
`findings[]`, it lowers the score, and at `approved` it needs a
`discordance_note`. Deleting it to lift a score is falsifying the grade. Do not
widen a band to swallow an outlier either — a widened band is a one-line diff a
reviewer will ask about, and there is no tolerance parameter.

## Draft → approved

Same shape as `drug_class_interactions`. Only `approved` reaches
`build/practice.v1.json`; drafts go to `build/practice.v1.draft.json`, which is
gitignored by `build/*.draft.json` and therefore never reaches `osdb/main` or the
site. `approved` requires:

- method-confidence index ≥ 5;
- ≥ 2 **independent** groups (first-author surname, or issuing authority for
  pharmacopoeias) — **except** for `parameter_kind: normative`, where one
  authority suffices provided `recommendation.jurisdiction` is set and the
  statement is jurisdiction-scoped. A definition needs no replication;
  disagreement between Ph. Eur. and USP is expressed as two scoped records, not
  one contested one;
- for `empirical`, ≥1 `optimisation` or `comparative-bench` finding **in the
  recommended solvent, varying the recommended parameter**;
- a finding whose conditions are `unspecified` may not be the sole support;
- `reviewed_by` + `reviewed_date`, and `verified_by` + `verified_date` by a
  different person;
- `discordance_note` if any admissible finding falls outside the band;
- `limit_rationale` if the keyed compound is toxicity-flagged;
- for `class-general`, ≥2 genera and a reviewed `generalisation` block.

A record with a non-empty `avoid[]` may be approved with **no recommendation at
all**. A precaution should be cheaper to assert than an instruction: the cost of
a wrong precaution is a suboptimal extract, and the cost of a wrong instruction
is somebody drinking it for two years.

## Presentation

Rendered as a **word plus a four-segment bar** under the heading *Method
confidence*: `established` / `supported` / `provisional` / `insufficient`. Never
the clinical ten dots, never "N/10", never the word "evidence". The emitted
object carries `"scale": "omnia-sana/method-confidence@1"` and **never a key
named `evidence`**, so a renderer written against the clinical contract finds
nothing and renders nothing rather than the wrong thing.

The reason is worth internalising rather than obeying. A user who has learned
that ten dots means *strong human evidence this plant works* will read ten dots
on an extraction record as exactly that — when it means *three labs agree about
a solvent percentage* and says nothing whatever about whether the plant works.
The two can sit a few hundred pixels apart on the same page. This project has
already shipped one two-scale confusion: 918 of 1,696 live claims displayed an
inflated evidence label for four weeks while every sync reported success.

## Finishing

    python scripts/validate.py
    python scripts/build.py

Then `osdb-verify-integrity` after a large batch, and `osdb-deploy` to publish.
One standing warning for integrity passes: **never delete a bibliography entry
whose derived `corpus` includes `practice`** on the strength of an orphan
warning.
