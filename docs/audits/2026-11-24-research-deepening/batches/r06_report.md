# Research-deepening batch 6 (2026-11-24)

**Plants:** borage, boswellia, calendula, tea, peach-leaved bellflower.

**Sources searched:**
- PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex.
- A targeted PubMed search for boswellia drug interactions.
- MSKCC About Herbs pages for borage, boswellia, calendula and green tea.
- The EU calendula monograph PDF (extracted with pypdf).

**Outcome:**
- **Search volume:** about 4,900 PubMed hits (tea alone: about 4,400; for tea only reviews, meta-analyses and safety were read in depth) and about 80 abstracts or pages read.
- **New references:** 26 (REF-5205..5230).
- **Symptom-tool pairs:** 1,422 -> 1,428.
- **Checks:** validate passes, with refs cited 4,005 / declared 4,005. The species audit raised one false positive ("Calendula promotes").
- **Files:** change log `r06_changes.tsv`; fixer `../fix_r06.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Borage | arthritis | 5 | 8 | Cochrane 2011: moderate evidence that oils containing gamma-linolenic acid (GLA), borage oil among them, relieve rheumatoid-arthritis symptoms |
| Borage | high blood pressure | new | 5 | 2021 double-blind RCT: borage oil + vitamin E vs vitamin E alone in postmenopausal women with hypertension |
| Borage | metabolic support | new | 6 | Weight-regain RCT (J Nutr 2007) + waist-to-hip ratio in the 2021 trial; one metabolic-rate trial is recorded as no-effect |
| Boswellia | oral health | new | 5 | Placebo RCT of frankincense tablets for mouth ulcers |
| Calendula | oral health | new | 5 | Placebo RCT of a calendula mouthwash for radiation mucositis; EU monograph traditional use |
| Calendula | wounds | 9 | 10 | Episiotomy and caesarean-wound RCTs |
| Tea | acne | new | 7 | 2021 meta-analysis: extract applied to the skin works; taken by mouth, little effect |
| Tea | cold | new | 7 | 2021 meta-analysis: catechins lowered the risk of influenza |
| Tea | blood sugar | 7 | 9 | 2024 meta-analysis in type 2 diabetes (positive) and a 2020 meta-analysis (fasting glucose only) |
| Tea | cognitive function | 5 | 8 | 2025 meta-analysis of tea / L-theanine ± caffeine (labelled as compound evidence) |

**No-effect studies recorded:**
- **Borage, eczema:** two placebo RCTs, the multicentre trial from 1999 and a children's trial from 1997.
- **Calendula, skin irritation:** a 2013 trial comparing calendula with a plain aqueous cream.

## Safety and other tool data

**Calendula:**
- **What was wrong:** the main caution rested on Hoffmann (an unreadable source) and a rat study. It also said internal use is "safe", called calendula a "uterine stimulant" and called it "safe in breastfeeding", none of which a readable source states.
- **Rewritten** from the EU monograph, MSKCC, the CIR 2010 safety report and patch-test data. It now states:
  - do not use with an allergy to the daisy family (Asteraceae);
  - skin sensitisation has been reported;
  - not recommended in pregnancy or breastfeeding;
  - not for children under 6 on the skin or under 12 in the mouth.

**Tea:**
- The extract liver-injury sentence cited only a benefits review and an L-theanine trial.
- It is now a separate **warning**, sourced to a 2018 systematic review (338 mg EGCG a day proposed as a safe intake), the 2008 USP review and MSKCC.
- The L-theanine trial is removed from both safety notes.

**Boswellia:**
- The drug-enzyme caution had no source. It is now verified from a laboratory CYP study and MSKCC.
- The pregnancy line still has no source and stays `needs-review`.
- New caution on a case at high dose (1,000 mg a day): a seizure caused by very low blood sodium.

**Borage:**
- New caution on a case of continuous seizures (status epilepticus) after borage oil.
- MSKCC is added as a source to the pyrrolizidine-alkaloid warning.

**Draft herb-drug interactions (need owner sign-off):** 7 in this batch.

| Plant | Drug class | Severity | Basis |
| --- | --- | --- | --- |
| Tea | chemotherapy (bortezomib) | caution | MSKCC: EGCG blocks bortezomib |
| Tea | statins | caution | MSKCC: rosuvastatin levels fell in healthy volunteers |
| Tea | anticoagulants | insufficient | MSKCC (vitamin K at very high intake) and a 2014 warfarin review |
| Tea | CYP3A4 substrates | insufficient | MSKCC |
| Boswellia | anticoagulants | caution | MSKCC (platelet inhibition) and the 2014 warfarin review |
| Boswellia | CYP3A4 substrates | insufficient | Laboratory CYP study |
| Borage | anticoagulants | insufficient | MSKCC, extrapolated from evening primrose GLA |

## For the owner

1. **The 7 drafts above,** plus the 6 still pending from earlier batches, need sign-off.
2. **Pairs left out because they conflict with the plant's own cautions** (invariant 12d):
   - tea for insomnia, stress and anxiety: the L-theanine reviews are positive, but tea's caffeine causes insomnia and anxiety;
   - tea for liver support: a meta-analysis found better liver enzymes, but tea extracts can cause liver injury.

   Say if you want compound evidence like this handled differently.
3. **Tea cognitive function (8) rests mostly on L-theanine trials.** The note says so.

## Rejected or not added (main reasons)

**Borage:**
- The 2012 Cochrane review of eczema supplements excludes borage.
- A GLA prophylaxis trial showed only a trend.
- An acne RCT gives no comparison with its control group in the abstract.
- A skin study reports only within-group changes.
- Combinations.

**Boswellia:**
- Gingivitis trial: frankincense alone was no better than scaling alone.
- Memowell and Inflawell (formulations).
- Collagenous colitis (a near-miss for IBD).
- *B. carteri* trials (a different species).
- Mixtures.

**Calendula:**
- Active-comparator-only trials: metronidazole, lycopene, bentonite, olive oil, Bao Yuan Gao.
- Combinations.
- A superseded wound review from 2008.
- A 1974 anaphylaxis letter (no abstract).

**Tea:**
- Periodontitis meta-analyses (very low certainty).
- A halitosis review (two before-after studies).
- An inflammatory-marker meta-analysis (TNF-alpha only).
- Observational cancer, stroke and depression meta-analyses (associations, not treatment).

**Peach-leaved bellflower:** no medicinal study of the species exists. Settled.

**Batch 5 Europe PMC check:** nothing new beyond preprints and items already appraised.
