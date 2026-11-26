# Research-deepening batch 23 (2026-11-26)

**Plants:** field restharrow, marjoram, oregano, yellow woodsorrel, European cranberry.

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex.
- **Name overrides:** added for all five plants.
- **European cranberry:** searched only by its own names (*Oxycoccus palustris*, *Vaccinium oxycoccos*, small, bog or European cranberry). Nearly all cranberry trials use American cranberry (*V. macrocarpon*), which has its own record.

**Outcome:**
- **Search volume:** about 450 PubMed hits (oregano about 460 before de-duplication, marjoram about 125) and about 15 abstracts read.
- **New references:** 3 (REF-5545..5547).
- **Symptom-tool pairs:** 1,498 -> 1,499.
- **Checks:** validate passes, with refs cited 4,322 / declared 4,322. The species audit raised no flags on the new references.
- **Files:** change log `r23_changes.tsv`; fixer `../fix_r23.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Oregano | sinusitis | new | 7 | 2023 network meta-analysis of 47 herbal RCTs: *O. vulgare* ranked best for chronic rhinosinusitis without polyps (low certainty) |

## Safety and other tool data

- **Oregano:** new allergy caution. Eating oregano and thyme caused three systemic allergic reactions in one person, and mint-family herbs can cross-react.
- **Marjoram:** new info note. A leaf extract caused DNA damage in cell tests at higher concentrations, but showed no acute toxicity in rats.

**Draft interactions:** none new. Six are still pending.

## For the owner

1. **The oregano sinusitis score (7) comes from a single network meta-analysis graded low certainty.** It is computed as a meta-analysis. Tell me if you would like such low-certainty network meta-analyses weighted lower.

## Gaps and settled plants

- **Field restharrow:** settled. The only trial used Aqualibra, a combination with Java tea and goldenrod.
- **Yellow woodsorrel:** settled. There are no human studies in any source.
- **European cranberry:** settled for human evidence specific to this species. A microbiome-only pilot was not added.
- **Marjoram stress/anxiety:** gap. In a 2023 inhalation RCT, scores fell only within the marjoram group, with no difference from control.
- **Marjoram Parkinson's:** the motor score was unchanged, and the non-motor and depression gains are within-group only.

## Rejected or not added (main reasons)

**Oregano:**
- Blood-marker studies in soldiers and athletes (surrogates).
- Spice blends and oregano + lemon balm tablets (combinations).
- *O. onites* and *O. dubium* (other species).
- Carvacrol-only studies.

**Marjoram:**
- Aromatherapy blends.
- Marjoram + cinnamon PCOS tea (combination).
