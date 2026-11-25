# Research-deepening batch 12 (2026-11-25)

**Plants:** couch grass, small-flowered willowherb, field horsetail, shady (meadow) horsetail, wood horsetail.

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex. Name overrides were added for all five plants (for example *Agropyron repens* and *Elytrigia repens* for couch grass).

**Outcome:**
- **Search volume:** about 120 PubMed hits. Field horsetail had 82 hits; shady and wood horsetail had none in any query family. About 15 abstracts were read.
- **New references:** 4 (REF-5342..5345).
- **Symptom-tool pairs:** 1,455 -> 1,455 (no new pair).
- **Checks:** validate passes, with refs cited 4,120 / declared 4,120. The species audit raised no flag on the new references.
- **Files:** change log `r12_changes.tsv`; fixer `../fix_r12.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Field horsetail | wounds | 1 | 5 | 2015 placebo RCT: horsetail ointment improved episiotomy healing and reduced pain (until now this pair rested on the EU monograph alone) |

## Safety and other tool data

**Field horsetail:**
- New caution: repeated mild acute pancreatitis that stopped when the patient gave up horsetail infusions (case report).
- New info note: the 2026 Cosmetic Ingredient Review found five horsetail-derived ingredients safe as used in cosmetics.

**Draft herb-drug interaction (needs owner sign-off):**

| Plant | Drug class | Severity | Basis |
| --- | --- | --- | --- |
| Field horsetail | antiretrovirals | caution | Two people on long-standing efavirenz-based HIV treatment had virological breakthrough after taking a supplement containing horsetail (2017 case reports). The authors advise avoiding the combination. |

## For the owner

1. **The horsetail antiretroviral draft above** needs sign-off. It rests on two case reports; the supplement contained horsetail, but the abstract doesn't say whether it held other herbs.
2. **Hyponatraemia with horsetail.** There are a 2018 *Annals of Internal Medicine* letter (severe hyponatraemia after drinking horsetail juice) and a 2021 case.
   - Neither has an abstract, so neither was added (house rule).
   - Given horsetail's diuretic use, they are worth a manual read.
3. **Pre-existing species-audit flags on willowherb (not from this batch).**
   - REF-2297 and REF-2299 describe oenothein B isolated from *E. angustifolium* (fireweed), but they are cited on small-flowered willowherb's constituents.
   - They belong in the species-audit triage; fireweed already took REF-2301 the same way.

## Settled (no usable human study)

- **Couch grass:** all kidney-stone trials and registered studies use multi-ingredient products (potassium citrate + Agropyrum, Renalof, Neorenal Forte).
- **Small-flowered willowherb:** the prostate products are combinations, often with *E. angustifolium*. The rest is a canine case and lab work.
- **Shady and wood horsetail:** zero PubMed hits in every query family. Field horsetail evidence is not inherited.

## Rejected or not added (main reasons)

**Field horsetail:**
- Dead end: the 2022 antihypertensive RCT compared horsetail only with hydrochlorothiazide (no placebo), so there is no blood-pressure pair.
- A liver-injury case involving garcinia, horsetail and ketoprofen together (horsetail not singled out).
- Silicon-absorption and urinary-protein studies (no clinical outcome).
- Combinations (Urox, Viviscal, CELcomplex, PEA + horsetail, nail lacquers).
- Perineal-trauma and PROM vaginal-cream trials (no vocabulary condition).
- Other *Equisetum* species.
