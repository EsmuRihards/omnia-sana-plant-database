# NEXT SESSION — Build the "Dangerous Lookalikes" interactive tool

**Paste the block below into a new chat.** It is self-contained and encodes the
data model, quality bar, deploy path, and known gotchas so the session doesn't
have to rediscover them. The companion spec is
`plant-database/DANGEROUS_LOOKALIKES_SCHEMA.md` (read it first).

State anchored to: DB audited clean at 179 plants / 91 interactions / 88 pairings,
bibliography ends **REF-2598** (verify current max before appending).

---

```
TASK: Add a "Dangerous Lookalikes" feature to the Omnia Sana plant database AND build the
interactive tool that serves it on omniasana.bio. For each medicinal plant, record the
dangerous plant(s)/fungi it can be mistaken for and exactly how to tell them apart. The
tool takes a medicinal plant as input and outputs its dangerous lookalikes + rock-solid
distinguishing features. Where a plant has NO dangerous lookalike, that must be stated
explicitly (not left blank).

READ FIRST (in the canonical repo C:\Users\rsera\Desktop\Omnia Sana\plant-database):
- DANGEROUS_LOOKALIKES_SCHEMA.md  — the full data model + exact schema + pipeline touch-points.
- scripts/build.py, scripts/validate.py, schema/plant.schema.json, schema/drug_class.schema.json,
  vocabularies/drug_classes.yaml — the drug_class_interactions feature is your working template.
- README.md (provenance + syncing) and NEXT_SESSION.md (the safety-campaign deploy workflow).

DATA MODEL (see the spec for exact JSON/YAML — do not deviate):
- NEW vocab vocabularies/dangerous_plants.yaml (+ schema/dangerous_plant.schema.json): one
  entry per toxic plant/fungus (canonical toxicology, DRY). e.g. conium-maculatum, cicuta-virosa,
  oenanthe-crocata, aethusa-cynapium, veratrum-album, digitalis-purpurea, convallaria-majalis,
  colchicum-autumnale, heracleum-mantegazzianum, galerina-marginata, omphalotus-olearius, ...
- NEW dangerous_lookalikes[] array on each medicinal-plant YAML: the PAIRWISE datum
  (dangerous_plant id, severity, confused_part, confusion_context, distinguishing_features[],
  key_test, reference_ids, status, reviewed_by, reviewed_date). ONE-DIRECTIONAL — do NOT mirror
  like pairings; model it like drug_class_interactions.
- NEW lookalikes_review object (outcome: none-known | has-lookalikes) so "researched, none known"
  is DISTINCT from "not yet researched" (absent). A safety feature must never show "not checked"
  as "safe".
- NEW $def lookalike_severity: fatal | dangerous | irritant | caution. Add the matching constant
  set to validate.py so bad values hard-fail CI.

THE QUALITY BAR (this is a life-safety feature — the whole task hinges on this):
1. Every dangerous lookalike must be a REAL, REALISTIC confusion — the two plants co-occur and
   resemble each other at the part/growth-stage people actually use. No fabricated or far-fetched
   pairs.
2. Every distinguishing_feature must be TRUE, RELIABLE and OBSERVABLE — reliable enough to bet a
   life on. Reject anything subtle, reversible, or ambiguous (e.g. never rely on a single vague
   trait). Prefer the single most decisive key_test (stem colour/blotching, crush-and-smell,
   spore print for fungi, etc.). If the honest answer is "don't forage this without an expert,"
   say exactly that.
3. Every claim SOURCED to authoritative references: botanical floras, university extension
   services, national poison-control / toxicology literature, peer-reviewed foraging-poisoning
   case reports. Add each source to bibliography.bibtex as a proper @article (or @misc/@book with
   study_type: traditional) with note = {REF-XXXX} and a study_type. Use PubMed MCP for tox case
   reports; WebSearch/WebFetch for floras + extension sources. Verify DOIs/PMIDs resolve.
4. ADVERSARIAL VERIFICATION before anything is marked approved: for each drafted record, actively
   try to REFUTE the distinguishing claims against an independent source. Anything that could get
   a forager killed if they relied on it must be caught and fixed. Draft first (status: draft),
   promote to approved: true only after this pass + owner sign-off (reviewed_by: 'Omnia Sana
   (owner-authorized)', reviewed_date: today). Public tools serve approved ONLY.
5. STATE WHEN NONE. If a plant has no dangerous lookalike in normal use (many cultivated/spice/
   commercially-bought species, e.g. turmeric powder), set lookalikes_review.outcome: none-known
   with a brief sourced justification — do NOT pad with trivial benign lookalikes dressed up as
   hazards.

SCOPE / SEQUENCING (futureproof, incremental — batches, like the safety campaign):
- Prioritise the HIGH-RISK taxa first, where mistakes are lethal:
  * The 11 Apiaceae (aegopodium-podagraria, angelica-archangelica, foeniculum-vulgare, carum-carvi,
    petroselinum-crispum, pimpinella-anisum, anethum-graveolens, coriandrum-sativum, cuminum-cyminum,
    centella-asiatica, trachyspermum-ammi) vs poison hemlock / water-dropwort / fool's parsley /
    hemlock (and giant hogweed for the tall ones).
  * gentiana-lutea vs Veratrum album (classic fatal European mix-up).
  * Foraged Allium (garlic/ramsons) vs lily-of-the-valley / autumn crocus / Arum.
  * symphytum-officinale + verbascum-thapsus (rosettes) vs foxglove.
  * The foraged fungi (psilocybe-cubensis vs Galerina; pleurotus-ostreatus vs Omphalotus /
    Pleurocybella; trametes-versicolor vs Stereum; inonotus-obliquus / ganoderma / etc.).
  * stellaria-media vs scarlet pimpernel / petty spurge; sambucus-nigra vs dwarf elder.
- Then work through the remaining plants, marking each lookalikes_review outcome as you go so the
  three-state model stays honest and the tool always knows a plant's review status.
- FUTUREPROOF: the model auto-covers new medicinal plants (add a lookalikes_review + optional
  dangerous_lookalikes[] when you add the plant) and new dangerous plants (add one vocab entry;
  reference it from as many medicinal plants as apply). No schema change needed to grow.

PIPELINE + DEPLOY (data):
1. Create schema/dangerous_plant.schema.json + vocabularies/dangerous_plants.yaml; extend
   plant.schema.json (dangerous_lookalikes[] + lookalikes_review + lookalike_severity $def).
2. Wire validate.py (vocab-id + severity + status checks; require reviewed_by/date on approved).
3. Wire build.py: load the vocab, build public-safe dp_public (strip editor_notes), approved_only()
   the dangerous_lookalikes in plants.json, add a one-directional lookalike_rows() emitter →
   build/lookalikes.v1.json (approved-only, embeds dp_public) + build/lookalikes.v1.draft.json (all).
   REGISTER lookalikes.v1.json in the manifest filename list (the .draft twin is NOT manifested).
4. Add data in batches. FILE-WRITE GOTCHA: read with .replace('\r\n','\n') and write open(f,'w',
   newline='\n') — LF is enforced by .gitattributes; CRLF breaks manifest hashes. bibtex dedup via
   re.sub removes ALL key matches → grep the DOI first to avoid nuking good entries.
5. python scripts/validate.py (must print OK) then python scripts/build.py (lookalikes count rises;
   drafts excluded from the public feed).
6. git add -A && git commit && git push osdb main — the dedicated omnia-sana-plant-database repo
   main branch ONLY (what the live WP tools pull from; CI rebuilds build/*.json). NEVER push to
   origin (the monorepo); never force-push. (The auto-mode classifier may block `git push osdb main`
   by conflating it with the monorepo "never push to main" rule — if so, ask the owner to run it.)

BUILD THE TOOL (WordPress, via the Novamira MCP — the site is WP, read/writable there):
Mirror the established tool pattern (os-knowledge-finder.php for the sync, os-monograph.php /
os-symptom-index.php for the virtual pages):
- os_lookalikes_do_sync($force): SHA-gated hourly pull of build/lookalikes.v1.json from
  raw.githubusercontent.com/EsmuRihards/omnia-sana-plant-database/main/build/lookalikes.v1.json,
  cached in an option (+ uploads/omniasana/lookalikes.json), lazy-build on first REST hit.
- REST GET /wp-json/omniasana/v1/lookalikes (+ ?herb=<id> filter), gzip emitter like os_kf.
- Virtual pages /dangerous-lookalikes/ (index + plant selector) and /dangerous-lookalikes/{plant}/
  via add_rewrite_rule + template_include, transient-cached bodies (12h), purge on sync.
- Front-end JS: input = medicinal-plant selector (from plants.json / vocab). Output = the three
  states: (a) not-reviewed → "Identification data not yet available — verify your ID
  independently"; (b) none-known → "No dangerous lookalikes on record for X"; (c) has-lookalikes →
  one card per lookalike with a prominent FATAL/DANGEROUS severity badge, the toxic plant's name +
  toxic principle + what it does, confused_part, the distinguishing_features list, the key_test
  called out, and "View Sources". A STANDING disclaimer is always visible: "This tool aids
  identification but does not replace an expert. When in doubt, throw it out."
- SEO: fold the new pages into os-seo-core (JSON-LD + sitemap) like the other tools.
- Go live: run os_lookalikes_do_sync(true); verify GET /wp-json/omniasana/v1/lookalikes?herb=<id>
  returns the expected records and count. GOTCHA: GitHub-raw is CDN-cached ~5 min, so a fresh push
  can read stale briefly — re-sync after ~5 min or trust the built_sha.

DELIVERABLE
Batches pushed live with a running tally: new vocab entries, new refs (REF-2599..), plants covered
(has-lookalikes vs none-known), and the tool live at /dangerous-lookalikes/. End with a
live-verification (REST spot-check for a lethal case like ground elder→poison hemlock, and a
none-known case). If a distinguishing claim can't be made rock-solid from authoritative sources,
leave the record draft and say so rather than shipping a shaky one.

OPTIONAL DB-hygiene fixes surfaced by the pre-build audit (safe, low-risk, do if time allows):
- Deduplicate REF-0559 == REF-2489 (identical Voroneanu 2016 silymarin meta; grep the DOI first).
- Retag REF-0483 study_type rct → systematic-review (it is a narrative review, currently inflates score).
- Fix REF-2437 year 2002 → 2001 (cosmetic).
- Normalize the 9 St John's wort drug_class_interaction reviewed_by 'Omnia Sana (owner)' →
  '(owner-authorized)' to match the other 126 records.
- Consider damping the evidence score for inferred/needs-review indications (133 currently score ≥7
  despite being mechanistic guesses) — front-end must keep the "inferred" qualifier dominant.
```
