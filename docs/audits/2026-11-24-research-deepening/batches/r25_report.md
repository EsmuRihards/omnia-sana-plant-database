# Research-deepening batch 25 (2026-11-27)

**Plants:** parsley, anise, Scots pine, kava, ribwort plantain.

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex.
- **Name overrides:** added for all five plants (for example *Petroselinum sativum*, aniseed, Scotch pine, kavalactones and WS 1490, English plantain).
- **Europe PMC:** no failures. It added nothing single-herb: the anise hits were multi-herb formulas, and the ribwort cough trials were combinations.

**Outcome:**
- **Search volume:** about 1,700 PubMed hits (kava about 780, anise about 370) and about 55 abstracts read, plus two full texts (hot flushes, COVID-19); the migraine trial's record was also checked in three databases.
- **New references:** 28 (REF-5570..5597).
- **Symptom-tool pairs:** 1,503 -> 1,511.
- **Checks:** validate passes, with refs cited 4,372 / declared 4,372. The species audit raised no flags on the new references (110 suspects, unchanged).
- **Files:** change log `r25_changes.tsv`; fixer `../fix_r25.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Anise | IBS | new | 5 | 2016 double-blind RCT: enteric-coated anise oil left 75% symptom-free, versus 35% on placebo |
| Anise | depression | new | 5 | The same trial's report on mild to moderate depression in people with IBS |
| Anise | indigestion | new | 5 | 2015 double-blind RCT in functional dyspepsia versus a cornstarch placebo |
| Anise | PMS | new | 5 | 2020 double-blind placebo RCT |
| Anise | hot flushes | new | 5 | 2012 double-blind placebo RCT: fewer hot flushes (severity results mixed) |
| Anise | diarrhoea | new | 5 | 2024 double-blind add-on RCT in adults with COVID-19 |
| Anise | loss of appetite | new | 5 | The same COVID-19 trial |
| Kava | insomnia | new | 5 | 2004 double-blind RCT in anxiety-related sleep problems; a 2015 meta-analysis found no herb better than placebo, and it stays alongside |

**No-effect study recorded:** a 2011 crossover found parsley leaf tea did not change urine volume or composition, so it is recorded on parsley urinary support.

## Safety and other tool data

- **Kava:**
  - New skin caution: kava dermopathy (a dry, scaly skin condition) after heavy use, and acute skin reactions after starting kava products, some resembling a severe drug reaction (DRESS). It includes a newborn with a similar rash after exposure in pregnancy.
  - New dependence and withdrawal caution: severe withdrawal after heavy use, treated in hospital with phenobarbital.
  - New info notes:
    - **Driving:** one medicinal dose did not impair simulated driving, unlike oxazepam, but driving was impaired with alcohol.
    - **Trial safety data:** liver tests, withdrawal and addiction measures did not differ from placebo over 6 weeks.
  - The serious liver caution is unchanged.
- **Anise:**
  - New allergy caution: tongue swelling, asthma, rhinoconjunctivitis, and food allergy confirmed by a blinded challenge. It notes cross-reactivity with birch and mugwort pollen and with parsley-family spices.
  - New infant caution: liver failure in a 4-month-old given a homemade star anise + anise tea.
- **Parsley:** new allergy caution (near-fatal anaphylaxis after "over-use" as a home remedy).
- **Scots pine:**
  - New liver caution (the first reported case of liver injury, in a person using it for asthma).
  - New info note: needle oil caused chromosome damage in lab tests.

**Draft interactions:** one new, **parsley × immunosuppressants** (caution). A kidney transplant recipient had a sirolimus level above target after eating excessive parsley. It is draft and needs your approval. Seven drafts are now pending:
- hibiscus × statins
- hibiscus × anticoagulants
- devil's claw × anticoagulants
- flax × anticoagulants
- noni × anticonvulsants
- bitter melon × chemotherapy agents
- parsley × immunosuppressants

## Research-integrity hold

None of the new anise trials is first- or last-authored by the flagged Tehran psychopharmacology group (author lists checked). Kava had no Iranian trials.

## For the owner

1. **Anise gains seven pairs, all from single trials (score 5).** All seven come from Iranian university trials (Shiraz, Isfahan and Tehran groups), none from the flagged group. One Shiraz traditional-medicine team ran both the IBS trial (which also gives the depression pair) and the COVID-19 trial.
2. **Anise for breastfeeding: no pair (inv. 12d).** A 2023 RCT found more pumped milk with anise tea in mothers of preterm infants. However, the record cautions against medicinal use in breastfeeding (the same pattern as evening primrose and labour). Tell me if you would like that caution reviewed instead.
3. **The COVID-19 anise trial reports its risk ratios in a confusing direction** (below 1 while describing more improvement). The pair follows the authors' stated conclusion.

## Gaps and settled plants

- **Anise migraine:** PubMed, Europe PMC and OpenAlex show the author-contribution statement in place of the published abstract of the 2019 topical-oil pilot RCT, and the full text is closed, so its result could not be checked.
- **Anise menopause:** the Kupperman-index gains in a 2026 RCT were only within the anise group.
- **Kava menopause and depression:** the climacteric results lacked between-group comparisons, and the depression trials were design-only or combinations.
- **Scots pine blood pressure:** in a 2023 inhalation study, pine oil had no blood-pressure effect.
- **Ribwort plantain:** settled. The cough trials used combinations or *Plantago major*.
- **Scots pine and parsley:** settled for human efficacy evidence.

## Rejected or not added (main reasons)

- **Strong pairs were not padded:** kava anxiety (10) and nervous tension.
- **Combinations:** Apiaceae dysmenorrhoea meta-analysis (anise with fennel and dill), six-herb dyspepsia formula, Thai multi-herb remedies, Menstrugole, St John's wort + kava, kava + HRT, SEDIFLÙ and Grintuss.
- **Not duplicated:** the second report of the dyspepsia trial (quality of life) and IBS meta-analyses that hold only the one anise trial.
- **Other species:** star anise (*Illicium*) poisonings, *Plantago major*.
- **Not caused by the plant:** aniseed-aperitif pseudohyperaldosteronism (caused by liquorice in the drink).
- **Active comparator only:** parsley melasma cream versus hydroquinone.
- **Surrogate outcomes:** parsley-seed bread kidney biomarkers.
- **No abstract:** a 1995 kava dopamine letter.
- **Single suspected case:** a kava serotonin-syndrome case (the CYP caution already covers raised drug levels).
