# Research-deepening batch 7 (2026-11-25)

**Plants:** hemp (*Cannabis sativa*), shepherd's purse, chili pepper, caraway, centaury.

**Sources searched:**
- PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex.
- For hemp and chili, the signature compounds were searched as title terms: cannabinoids / CBD / nabiximols, and capsaicin.
- For those two plants, only systematic reviews, meta-analyses and safety reviews were read in depth.

**Outcome:**
- **Search volume:** about 20,000 PubMed hits (hemp alone: about 17,000) and about 60 abstracts read.
- **New references:** 19 (REF-5231..5249).
- **Symptom-tool pairs:** 1,428 -> 1,434.
- **Checks:** validate passes, with refs cited 4,024 / declared 4,024. The species audit raised only false positives ("Cannabis use").
- **Files:** change log `r07_changes.tsv`; fixer `../fix_r07.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Hemp | pain | 6 | 9 | Whiting 2015 JAMA meta-analysis (moderate-quality evidence for chronic pain) and a 2023 trial-sequential meta-analysis. The benefit is modest, with more side effects; the cancer-pain meta-analysis is recorded as no-effect |
| Hemp | muscle spasm | new | 8 | Nabiximols (THC:CBD extract spray) for MS spasticity, meta-analysis 2023; plus Whiting 2015 |
| Hemp | insomnia | new | 8 | Whiting 2015 and the 2023 meta-analysis (low-quality evidence, mostly in chronic pain) |
| Hemp | appetite loss | new | 8 | Cancer-cachexia meta-analysis 2019 (more appetite, lower quality of life); Whiting 2015 (HIV weight gain) |
| Hemp | anxiety | new | 7 | CBD meta-analysis 2024 in anxiety disorders (compound evidence) |
| Chili | pain | 7 | 8 | 2026 meta-analysis of 8% capsaicin patches for HIV nerve pain |
| Chili | metabolic support | new | 7 | 2023 capsaicin weight-loss meta-analysis (modest); the capsinoid meta-analysis (no effect) is recorded as no-effect |
| Caraway | metabolic support | new | 5 | Triple-blind placebo RCT of a caraway extract in overweight women |

## Safety and other tool data

**Hemp:**
- **New warning:** cannabis use was linked to more heart attacks, strokes and other major cardiovascular events (2025 meta-analysis).
- **New warning:** psychosis is more common in cannabis users, the risk rises with dose, onset comes earlier, and people with psychosis relapse more (review of reviews).
- **New caution:** cannabinoid hyperemesis syndrome (cyclic vomiting with regular use).
- **New caution:** CBD side effects (diarrhoea; liver enzymes and sedation in childhood-epilepsy trials).
- **Existing caution:** its CYP450 and anticoagulant wording now has sources (2024 drug-interaction and CYP reviews), plus a 2025 review of birth outcomes.

**Caraway:** the 12-week placebo-controlled safety trial (no adverse changes) is added to its caution.

**Draft herb-drug interactions (need owner sign-off):**

| Plant | Drug class | Severity | Basis |
| --- | --- | --- | --- |
| Hemp | anticoagulants (warfarin) | caution | 2024 drug-interaction systematic review |
| Hemp | immunosuppressants (tacrolimus, sirolimus) | caution | Same review |
| Hemp | CYP3A4 substrates | caution | 2024 reviews of CYP450 effects |
| Caraway | antibiotics (tuberculosis drugs) | caution | Healthy-volunteer study: caraway extract raised rifampicin, isoniazid and pyrazinamide levels by about 30% |

## For the owner

1. **The 4 draft interactions above** need sign-off.
2. **Hemp nausea was left out.** There is low-quality evidence for chemotherapy nausea, but regular use itself causes cyclic vomiting. This is the same rule as tea and insomnia; say if you want it handled differently.
3. **The new hemp pairs (8) rest on cannabinoid medicines,** including THC-containing nabiximols. Industrial hemp foods contain little THC. Each note names the product type.
4. **Hemp pain is now 9,** but both meta-analyses say the benefit is modest and the harms may outweigh it. The note says so.

## Rejected or not added (main reasons)

**Hemp:**
- Cochrane 2018 neuropathic pain: benefit may be outweighed by harms; this is not a no-effect result.
- Nabilone fibromyalgia: a synthetic analogue.
- Dementia.
- Epilepsy: no vocabulary condition. CBD-clobazam is already covered by the approved anticonvulsant interaction.
- Use-disorder, driving and adolescent literature.

**Chili:**
- Glucose, blood-pressure and IBS meta-analyses: all found no effect, and no pair exists.
- Mouth (burning mouth, orofacial) and nasal (rhinitis) capsaicin: these conflict with the record's mucous-membrane warning (invariant 12d).
- Cannabinoid hyperemesis (single-arm data only).

**Caraway:**
- Menthacarin and caraway oil + menthol: combinations.
- *Bunium persicum* "black caraway": a different species.
- Persian formulas.

**Shepherd's purse and centaury:**
- No usable new human study. Centaury's trials all use Canephron N (a three-herb combination). Both are settled.

**Batch 6 Europe PMC follow-up:**
- An olibanum chewing-gum trial in Alzheimer's found no effect. It is not added: the abstract names no *Boswellia* species.
- A 2018 nadolol-EGCG pharmacokinetic study: the tea-nadolol interaction is already approved.
