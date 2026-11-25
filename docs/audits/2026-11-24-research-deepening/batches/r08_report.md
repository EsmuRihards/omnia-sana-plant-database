# Research-deepening batch 8 (2026-11-25)

**Plants:** gotu kola, fireweed, greater celandine, cassia cinnamon, true cinnamon.

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex.

**Outcome:**
- **Search volume:** about 1,900 PubMed hits and about 55 abstracts read.
- **New references:** 20 (REF-5250..5269).
- **Symptom-tool pairs:** 1,434 -> 1,439.
- **Checks:** validate passes, with refs cited 4,044 / declared 4,044. The species audit flagged *Cinnamomum zeylanicum*, which is now a recorded synonym on true cinnamon; the flag is cleared.
- **Files:** change log `r08_changes.tsv`; fixer `../fix_r08.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Gotu kola | swelling | 7 | 9 | Two triterpene-fraction RCTs: ankle swelling in venous hypertension, and swelling on long flights |
| Gotu kola | pain | new | 6 | Placebo RCTs: diabetic-neuropathy symptoms (triterpenes) and jaw pain (ECa 233 extract) |
| Gotu kola | anxiety | 5 | 6 | Clinical study in generalized anxiety disorder |
| Cassia | high blood pressure | new | 9 | Two 2020 meta-analyses and a 2024 umbrella review |
| Cassia | menstrual cramps | new | 6 | Two double-blind placebo RCTs (cinnamon capsules) |
| Cassia | wounds | new | 5 | Placebo RCT of a cinnamon ointment on episiotomy wounds |
| True cinnamon | allergy | new | 5 | Placebo RCT of a Ceylon cinnamon bark nasal spray for hay fever |

**No-effect study recorded:** a gotu kola + exercise trial found no extra cognitive benefit over exercise alone.

**Species rule:** trials that say only "cinnamon" are assigned to cassia (invariant 10). The notes say the species was not stated.

## Safety and other tool data

**Greater celandine:**
- The serious liver warning now also cites:
  - formal causality reanalyses of 22 German spontaneous reports (2011) and of 21 published European cases (2012);
  - a 2017 review;
  - the first US case (2024) and a 2026 case.
- New caution: a case of severe haemolytic anaemia after an oral extract.

**Cassia:** new allergy caution. In reported cases, people first sensitised by inhaling heated cinnamon-flavoured vapour later had severe reactions, including anaphylaxis, to spiced food.

**Draft interactions:** none in this batch.

## For the owner

1. **Cassia high blood pressure (9)** rests on meta-analyses of "cinnamon" trials, mostly without a named species. It follows your cinnamon rule; it is flagged in case you want BP evidence kept off species-level pairs.
2. **Liver support for cassia was not added.** Two meta-analyses found better liver enzymes, but the record warns that cassia coumarin can damage the liver (invariant 12d).

## Rejected or not added (main reasons)

**Gotu kola:**
- Dead end: a 2025 Thai placebo RCT in type 2 diabetes found no effect on glucose or lipids (no pair exists).
- Combination creams and cosmetics.
- Active-comparator trials (vs flavonoids).
- A scar-cream RCT (pigmentation only).
- Skin-ageing, eye and strength trials (no vocabulary condition).

**Fireweed:** no usable human study. The only single-extract nocturia study is in a SCIRP journal (Beall's list); the BPH products are combinations. Settled.

**Greater celandine:**
- Ukrain (a semisynthetic alkaloid derivative, not the herb).
- Chelidonium + turmeric (combination).
- Letters with no abstract.

**Cassia:**
- Heavy bleeding (a near-miss: the women had period pain, not heavy bleeding).
- Active-comparator trials (ibuprofen, chlorhexidine).
- PCOS hormone trials (surrogate outcomes).
- Combinations with berberine, sumac, chromium, probiotics or marjoram.

**True cinnamon:**
- A 2025 Sri Lankan diabetes report: the same trial as REF-2413, and its abstract reports only within-group changes.
- An essential oil vs nystatin trial (active comparator only).
