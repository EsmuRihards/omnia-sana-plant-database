# Research-deepening batch 33 (2026-11-27)

**Plants:** clove, feverfew, tansy, dandelion, cacao.

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex.
- **Name overrides:** added for all five plants.
- **Terms and traps:**
  - "Cocoa" and "chocolate" were searched in titles only.
  - Eugenol (dental cement) was not searched.
  - "CLOVES syndrome" and garlic cloves were filtered out.
  - Tansy ragwort (*Jacobaea vulgaris*) and the COCOA birth cohort are not this record.

**Outcome:**
- **Search volume:** about 3,000 PubMed hits (cacao about 1,900, clove about 530) and about 40 abstracts read.
- **New references:** 9 (REF-5670..5678).
- **Symptom-tool pairs:** 1,523 -> 1,524.
- **Checks:** validate passes, with refs cited 4,453 / declared 4,453. The species audit raised no flags on the new references (110 suspects, unchanged).
- **Files:** change log `r33_changes.tsv`; fixer `../fix_r33.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Cacao | blood sugar | new | 8 | 2022 meta-analysis of 12 RCTs in type 2 diabetes (long-term cocoa lowered glucose by about 9 mg/dL) and a 2026 metabolic-syndrome meta-analysis |

**No-effect study recorded:** in a 2026 open-label crossover, dandelion root powder did not increase urine output more than water, so it is recorded on urinary support.

## Safety and other tool data

- **Cacao:**
  - New allergy caution: anaphylaxis to chocolate in a person allergic to tree nuts (cross-reactivity).
  - New info notes: about 14% of people with migraine report chocolate as a trigger, and dark chocolate carries more cadmium and lead (highest from Central and South America; children's cadmium intake reaches about 60% of the tolerable limit).
- **Feverfew:**
  - New bleeding caution: vaginal bleeding and abnormal clotting tests after 9 months of high-dose feverfew (causality probable). It is also added to the approved anticoagulants interaction.
  - The allergy note now cites two contact-dermatitis cases from a feverfew moisturiser.

**Draft interactions:** none new. Eleven are still pending.

## For the owner (queued for the end-of-campaign review)

1. **Cacao and mood: no pair.** A 2022 meta-analysis of 9 studies found lower depression and anxiety scores, but 5 studies were single doses and only 2 lasted over a week, mostly in healthy people. A depression or anxiety score near 8 would overstate this. Tell me if you would rather show it.
2. **Cacao blood sugar scores 8 from two meta-analyses,** mostly in type 2 diabetes. Cholesterol got no pair because the meta-analyses conflict (LDL fell in one; another found only triglycerides changed).

## Gaps and settled plants

- **Clove:** oral health and pain stay at 5.
  - Injection-pain trials compared clove only with EMLA, lignocaine or benzocaine.
  - The itch and headache trials were not significant versus control.
  - The radiation mouthwash was a "clove-based herbal" product of unstated composition.
- **Feverfew:** migraine (9) and headache (8) were not padded.
- **Tansy:** settled.
- **Dandelion:** no new efficacy trial. The combinations (with borneol, D-mannose and liver blends) were excluded.
- **Cacao:** blood pressure (8), cardiovascular support, cognitive function and memory (7) were not padded. Observational cohort meta-analyses and surrogate-marker meta-analyses were excluded.

## Rejected or not added (main reasons)

- **Active comparators:** clove versus local anaesthetics.
- **Combinations:** IMOD, Septimeb, dandelion + borneol, BNO 1030.
- **Surrogate outcomes:** cocoa oxidative stress, CRP, vascular function; clove binge-drinking markers.
- **Other species:** tansy ragwort, *Taraxacum kok-saghyz*.
- **No abstract:** a feverfew occupational dermatitis case, a dandelion allergen paper.
