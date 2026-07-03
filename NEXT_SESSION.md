# NEXT SESSION — Expand the Herb–Drug Interaction Checker

**Paste the block below into a new chat.** It is self-contained and encodes the
established workflow, quality bar, deploy path, and known gotchas so the session
doesn't have to rediscover them.

State is anchored to where the **safety-data campaign** last left off (osdb `9aedf04`),
not to any later cosmetic edits.

---

```
TASK: Expand the scientific backing of the Herb–Drug Interaction Checker on omniasana.bio.

GOAL
Add more cited herb–drug interaction data. Target ~100 additional publications, but
DO NOT force unrelated or weak claims — if the solid evidence isn't there, stop. A
smaller, defensible set beats a padded one. The bar is: every interaction claim is
backed by a real PubMed clinical trial, meta-analysis, or systematic review (RCT >
meta > systematic-review preferred; preclinical/traditional only to support, never as
sole basis for a caution). Default severity to `caution`; reserve `avoid` for strong
contraindications (e.g. enzyme-induction like St John's Wort).

The ~100 articles can come from THREE places (all legitimate, don't force interactions):
  1. NEW herb→drug-class interactions where solid clinical/meta evidence exists.
  2. ADDITIONAL citations strengthening the 84 EXISTING interaction records
     (more publications per claim = more scientific backing, no new claim risk).
  3. Herb–herb PAIRINGS (currently 58) — flagged as having the most remaining room;
     expand with cited synergy/caution pairings.
Reality check: the prior campaign already harvested most high-confidence NEW-interaction
gaps, so expect a large share of the ~100 to come from (2) deepening existing citations
and (3) pairings rather than 100 brand-new interactions. That is the correct shape of
"add more publications, don't force it."

CRITICAL REQUIREMENT (the user's main ask):
Every source you cite MUST be added to the main bibliography (`bibliography.bibtex`)
as a proper @article entry with `note = {REF-XXXX}` and a `study_type`. The build
pipeline compiles bibliography.bibtex → citations.json, which feeds BOTH the Knowledge
Finder AND the Plant Monograph Builder. So adding sources correctly means they
automatically appear in those tools too. Do NOT cite a REF-id that isn't a real
@article in bibliography.bibtex (validate.py will catch orphans/broken refs).

REPO & STATE (last safety-data batch: osdb 9aedf04)
- Canonical repo: C:\Users\rsera\Desktop\Omnia Sana\plant-database  (Python 3.11)
- 179 plants, 84 interactions, 58 pairings — all live.
- Bibliography ends at REF-2502. New entries start at REF-2503 (verify the current max
  before appending).
- Drug-class vocab (vocabularies/drug_classes.yaml, 16 ids): anticoagulants-antiplatelets,
  antihypertensives, cardiac-glycosides, statins, antidiabetics, thyroid-medicines,
  hormonal-therapies, antidepressants-serotonergic, sedatives-cns-depressants,
  anticonvulsants, immunosuppressants, chemotherapy-agents, antiretrovirals,
  antibiotics, nsaids, cyp3a4-substrates. (If you genuinely need a class that doesn't
  exist — e.g. diuretics for licorice/aloe hypokalemia, stimulants for green-tea
  caffeine — add it to the vocab first; several real gaps need classes we don't have.)

WORKFLOW (repeatable, per batch)
1. Use the PubMed MCP (search_articles + get_article_metadata) to find landmark
   citations. Prefer systematic reviews / meta-analyses / RCTs. Capture DOI + PMID.
2. Append @article entries to bibliography.bibtex, matching the existing entry format
   EXACTLY, with note = {REF-XXXX} and study_type = {rct|meta-analysis|systematic-
   review|clinical|preclinical|traditional} (study_type vocab is constrained to those
   six — case reports → clinical; narrative reviews → systematic-review).
3. Insert `drug_class_interactions:` (and/or `pairings:`) into the relevant
   plants/<file>.yaml. Each interaction item: drug_class, severity, mechanism
   (plain-English), reference_ids, status: approved, reviewed_by: 'Omnia Sana
   (owner-authorized)', reviewed_date: '<today, e.g. 2026-07-04>'. Pairings:
   partner_id (the id, not the filename), type (synergy|neutral|caution|avoid), note,
   reference_ids, status, reviewed_by, reviewed_date. Pairings are directionless — the
   build mirrors A↔B automatically. Placement in the YAML: interaction block goes before
   ^pairings: if present, else before ^provenance:; pairings block before ^provenance:.
4. FILE-WRITE GOTCHA: read with .replace('\r\n','\n') and write open(f,'w',
   newline='\n') — LF is enforced by .gitattributes; CRLF breaks manifest hashes.
   (Editing many YAMLs via a Python heredoc through Bash is lighter than the Edit tool,
   which needs a prior Read of each file.)
5. Run: python scripts/validate.py  (must print OK — all refs/vocab resolve) then
   python scripts/build.py  (interaction/pairing counts should rise; drafts excluded).
6. git add -A && git commit && git push osdb main
   — push to the `osdb` remote's main branch ONLY (the documented data-deploy path).
   NEVER push to `origin` (that's the OmniaSana monorepo). Note: the auto-mode classifier
   may block `git push osdb main` by conflating it with the monorepo "never push to main"
   rule — if so, ask the user to authorize/run the push; do not work around it.
7. Go live via Novamira execute-php: run os_safety_sync(true) and os_kf_do_sync(true)
   (and os_pe_sync(true) if plant records changed). Verify with REST:
   GET /wp-json/omniasana/v1/interactions?herb=<id>  and confirm the new count.
   GOTCHA: os_safety_sync fetches the GitHub-raw branch URL, CDN-cached ~5 min, so the
   safety count can read stale right after a push; os_kf_do_sync reads fresh (trust its
   sha). Re-run os_safety_sync(true) after ~5 min or let the hourly cron catch up.

QUALITY GUARDRAILS (from prior sessions — keep the bar)
- Don't cite a null-result meta to support a caution (e.g. ginger+antidiabetics: the
  most recent meta found no significant effect — correctly rejected).
- Don't propagate misconceptions (e.g. cassia cinnamon's coumarin is the hepatotoxic
  parent coumarin, NOT a vitamin-K-antagonist anticoagulant — "potentiates warfarin"
  is wrong; correctly skipped).
- Be honest in mechanism text about evidence strength and any related-species
  extrapolation (e.g. Schisandra sphenanthera → S. chinensis).
- Public tools serve status: approved only. The user has authorized publishing directly
  PROVIDED each claim is PubMed-cited and conservative.

KNOWN REMAINING LEADS (verify evidence before adding — several are weak/preclinical)
- Antidiabetic ACTION but no interaction yet (need a real clinical/meta DOI):
  artemisia-absinthium, betula-pendula, eleutherococcus-senticosus, ganoderma-lingzhi,
  hippophae-rhamnoides, lentinula-edodes, morinda-citrifolia, pleurotus-ostreatus,
  rhodiola-rosea. (camellia-sinensis/green tea shown INEFFECTIVE per Willcox — skip.)
- Needs new drug classes we don't have: diuretics (licorice/aloe hypokalemia),
  stimulants (green-tea caffeine), MAOI-specific cautions.
- Pairings: passiflora/melissa/hops permutations, more adaptogen synergy (needs a
  combination-specific citation, not just two mono-herb refs).

DELIVERABLE
Batches pushed live, with a running tally: new refs (REF-2503..), new interactions,
strengthened existing interactions, new pairings, any new drug classes. End with a
live-verification (REST counts + a spot check that a couple of the new sources appear
in the Knowledge Finder / monograph builder). If remaining candidates are only
weak/preclinical, say so and stop rather than padding.
```
