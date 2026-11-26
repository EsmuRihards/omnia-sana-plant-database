# Research-deepening batch 18 (2026-11-26)

**Plants:** chaga, elecampane, juniper, field scabious, wild lettuce.

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex. Name overrides were added for all five plants, for example *Fuscoporia obliqua* for chaga and lactucarium for wild lettuce.

**Outcome:**
- **Search volume:** about 220 PubMed hits, many of them noise (Chagas disease; the Juniper Gardens project) and about 15 abstracts read.
- **New references:** 5 (REF-5421..5425).
- **Symptom-tool pairs:** 1,472 -> 1,472 (no new pair).
- **Checks:** validate passes, with refs cited 4,200 / declared 4,200. The species audit raised no flags.
- **Files:** change log `r18_changes.tsv`; fixer `../fix_r18.py`.

## Safety and other tool data

**Chaga:** a new kidney **warning** (the strongest batch addition).
- Chaga is extremely high in oxalate. Three case reports describe oxalate kidney damage after months of daily chaga powder, including dialysis and end-stage kidney disease.
- One report measured 14.2 g of oxalate per 100 g of the product.

**Wild lettuce:** new caution "never inject". Three drug users who injected a home-made extract became acutely ill. None had the opiate-like effect that online sources claim for "opium lettuce".

**Elecampane:** the skin-allergy note now cites a 2017 review of systemic allergic dermatitis from Compositae sesquiterpene lactones.

**Draft interactions:** none new. Three from batch 16 are pending: hibiscus × statins, hibiscus × anticoagulants and devil's claw × anticoagulants.

## Gaps and settled plants

- **Chaga gap:** a 2008 study in type 2 diabetes found a single prior dose lowered the post-meal glucose peak. The abstract does not state randomisation or a placebo, so no blood-sugar pair was created.
- **Elecampane:** no human trial of the herb alone (cough syrups are combinations).
- **Juniper:** nothing new.
  - A hyponatraemia case followed a multi-herb "detox" with very high fluid intake, so it can't be attributed to juniper.
  - The cosmetic safety review found the data insufficient.
  - Cade oil poisonings involve another species.
- **Field scabious:** zero human studies in every source. Settled.
- **Wild lettuce:** still no human trial.

## For the owner

1. **The chaga kidney note uses severity "warning"**, matching the strength of three independent case reports with dialysis and kidney failure. Tell me if you'd prefer "caution".
