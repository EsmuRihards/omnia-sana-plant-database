# Research-deepening batch 26 (2026-11-27)

**Plants:** greater plantain, oyster mushroom, tormentil, cowslip, selfheal.

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex.
- **Name overrides:** added for all five plants. Three species traps were avoided:
  - Bare "plantain" was not searched, because it also matches banana plantains and psyllium.
  - Marsh cowslip (*Caltha*) is a different plant.
  - "Bloodroot" in tormentil's names is also *Sanguinaria*.
- **Europe PMC:** two temporary failures that it retried successfully. It added nothing new, only a null pleuran gastroenteritis trial and an uncontrolled 1982 plantain series.

**Outcome:**
- **Search volume:** about 690 PubMed hits (oyster mushroom about 330, selfheal about 230) and about 45 abstracts read, plus one full text (the selfheal breast-cancer trial).
- **New references:** 14 (REF-5598..5611).
- **Symptom-tool pairs:** 1,511 -> 1,516.
- **Checks:** validate passes, with refs cited 4,386 / declared 4,386. The species audit raised no flags on the new references (110 suspects, unchanged).
- **Files:** change log `r26_changes.tsv`; fixer `../fix_r26.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Greater plantain | bronchitis | 1 | 5 | 2024 double-blind RCT in acute bronchitis (previously traditional sources only) |
| Greater plantain | cough | 2 | 5 | The same trial (fewer coughs than placebo) |
| Greater plantain | oral health | new | 5 | 2020 double-blind RCT: fewer mouth sores during radiotherapy |
| Greater plantain | liver support | new | 5 | 2021 double-blind RCT in fatty liver disease (enzymes and ultrasound grade) |
| Oyster mushroom | cold | 6 | 7 | 2025 double-blind pleuran RCT in 249 children versus an active placebo |
| Oyster mushroom | asthma | new | 5 | 2025 double-blind pleuran + vitamin C versus vitamin C RCT in 230 children (benefit partly by age group) |
| Oyster mushroom | memory | new | 5 | 2026 RCT: eating the mushroom 4 times a week improved word recall in older adults |
| Selfheal | prostate support | new | 5 | 2026 double-blind RCT in men with urinary symptoms (IPSS) |

**No-effect study recorded:** in a 2026 double-blind RCT, oyster mushroom powder did not lower LDL cholesterol, so it is recorded on cardiovascular support.

## Safety and other tool data

- **Selfheal:** new caution. Long-term use of Chinese herbal medicines, mainly selfheal, was linked to mesenteric phlebosclerosis (calcified bowel veins) in a case report. The record's old note says there is no known toxicity.
- **Oyster mushroom:**
  - The occupational-allergy caution now cites an anaphylaxis case at a mushroom farm.
  - New food-allergy caution: one case confirmed by an oral challenge.
- **Cowslip:** new info note. In a German market survey, cowslip combination products were often contaminated with liver-toxic pyrrolizidine alkaloids from ragwort-type plants, above EU limits.
- **Greater plantain:** new info note. A water extract was genotoxic in fruit flies; another extract was not mutagenic.

**Draft interactions:** none new. Seven are still pending.

## For the owner

1. **Selfheal and thyroid: no vocabulary condition.** Two meta-analyses (2025, 2027) report that selfheal preparations added to antithyroid drugs improved thyroid hormones and antibodies in Graves' disease and hyperthyroidism. The tool has no thyroid condition, so the evidence cannot be shown. Adding one would be a schema decision for you.
2. **Selfheal breast-cancer trial not added.** A 2018 trial in 424 patients reported better response and survival with selfheal plus chemotherapy. However, neither the abstract nor the full text says the groups were randomised or blinded, there is no trial registration, and the drug regimen is described inconsistently. Given the size of the claim, I left it out.

## Gaps and settled plants

- **Greater plantain:**
  - Heavy periods: the oral trial compared only with mefenamic acid, and the review mixes routes.
  - Ulcerative colitis: blood in stool did not differ from placebo.
  - Kidney: open-label, proteinuria only.
  - Diuretic: a 1992 double-blind crossover found no effect.
- **Oyster mushroom:** the gastroenteritis trial was null. Herpes (no condition) and eczema (no randomisation stated) were not added.
- **Tormentil:** settled. Nothing new beyond the rotavirus RCT and the ulcerative colitis study already held.
- **Cowslip:** settled for human efficacy. Every trial used a combination (Sinupret, Cardiodoron, ivy combinations).

## Rejected or not added (main reasons)

- **Combinations:**
  - Plantain: Aloe vera + plantain gel, plantain + mallow + honey cream, KalobaTUSS, Butirprost.
  - Selfheal: SKI 306X / SKCPT, Chinese patent formulas.
- **Surrogate outcomes:** plantain leptin/VEGF; pleuran eosinophil/IgE; athletes' immune cells; single-meal GLP-1.
- **Other species:** psyllium (*Plantago ovata*), Tamogitake (*Pleurotus cornucopiae*).
- **No randomisation, or within-group results only:** the COPD pleuran study, the Mexican diet study, the HIV lipid study.
- **No abstract:** a plantain dermatitis letter and an oyster mushroom occupational-allergy letter.
