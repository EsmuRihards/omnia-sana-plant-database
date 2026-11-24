# Research-deepening batch 2 (2026-11-24)

**Plants:** agrimony, lady's mantle, garlic, aloe, lemon verbena.

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov, OpenAlex and the NCCIH fact sheets.

**Outcome:**
- **Search volume:** about 3,300 hits, and about 110 abstracts or pages read.
- **New references:** 49 (REF-5083..5131).
- **Symptom-tool pairs:** 1,409 -> 1,415.
- **Checks:** validate reports 0 errors, with refs cited 3,906 / declared 3,906. The species audit raised only expected flags: *Aloe barbadensis* is a synonym (now recorded on the aloe record) and "Allium data" is a false positive.
- **Files:** change log `r02_changes.tsv`; fixer `../fix_r02.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Garlic | liver support | new | 8 | MAs of RCTs in chronic liver disease and in NAFLD (ALT, AST, steatosis) |
| Garlic | PMS | new | 5 | Double-blind placebo RCT, 3 cycles |
| Garlic | fatigue | new | 5 | Placebo RCT in multiple sclerosis |
| Garlic | blood pressure, blood sugar, inflammation, metabolic | 8-9 | 9-10 | 2026 CV-risk MA, aged-garlic GRADE MA, 2024 glucose/lipid MA, MetS MA |
| Aloe | IBD (ulcerative colitis) | new | 5 | Langmead 2004 double-blind RCT (clinical response 47% vs 14%) |
| Aloe | bruising | new | 5 | 2026 RCT, vein-harvest-site bruising (found via Europe PMC) |
| Aloe | wounds, oral health, skin irritation, blood sugar | 7-9 | 8-10 | Diabetic-foot RCT, burn SR, aphthous placebo RCT, gingival MA, 2022 radiation-dermatitis SR, glucose MA |
| Lemon verbena | stress | new | 6 | Two placebo RCTs (adults 2022; adolescents 2025, not in PubMed) |
| Lemon verbena | anxiety | 2 | 6 | Anxiolytic RCT + pre-caesarean aromatherapy RCT |
| Lemon verbena | insomnia | 6 | 7 | Same two RCTs |

**No-effect studies recorded:**
- **Garlic:** the 2009 SR found blood-pressure trials too poor to confirm an effect; the 2021 MA of inflammatory markers was not significant overall.
- **Aloe:** two IBS RCTs (2006, 2020); a 2017 radiation-dermatitis RCT.
- **Lemon verbena:** a single dose before coronary angiography did not reduce anxiety.

## Safety and other tool data

**Aloe:**
- The oral-latex caution **had no source at all**. It is now sourced to:
  - the NCCIH fact sheet (2025);
  - the EFSA 2018 hydroxyanthracene opinion;
  - a review of aloe-gel food products;
  - a review of aloe-emodin;
  - a case of acute liver injury;
  - a 60-day study of gel juice and liver function;
  - a bezoar case report.
- The caution is raised to `warning`.
- The latex preparation is now sourced.

**Garlic:**
- The caution named NCCIH but cited taxonomy pages instead. It now cites the NCCIH fact sheet, the garlic-burn SR (39 cases) and the platelet-aggregation SR.
- The POWO taxon page now sits only in the plant's general reference list.

**Lady's mantle:**
- Description, habitat, harvesting, traditional uses, infusion and a historical dose are now sourced to Grieve.
- POWO is no longer cited for safety or description.
- The safety caution now rests only on Hoffmann (unreadable), so it is set to `needs-review`.
- Two small human studies (a skin-barrier study and an open aphthous-ulcer study) are added to the vulnerary action.

**Lemon verbena:** mouse teratogenicity studies showing no harm are added to the pregnancy caution.

**Draft herb-drug interaction (needs owner sign-off):** aloe latex with cardiac glycosides such as digoxin, severity caution, source NCCIH.

**Link fix:** the 10 campaign entries with a PMID but no DOI now carry their PubMed URL, so their source cards link correctly.

## Rejected or not added (main reasons)

- **Wrong species:** the "Lemon Verbena (*Cymbopogon citratus*)" oral-candidiasis SR is about lemongrass.
- **Retracted:** an aged-garlic blood-pressure MA (2024) and a garlic pregnancy trial.
- **Active comparator only (no placebo):**
  - garlic vs podophyllin for genital warts;
  - lady's mantle vs dexamethasone for post-intubation sore throat;
  - aloe vs omeprazole/ranitidine for GERD;
  - aloe vs oestrogen for atrophic vaginitis.
- **Combinations:** hibiscus + lemon verbena; lemon verbena + omega-3; many aloe and garlic polyherbal products.
- **Not attributable to one herb:** the 2026 lemon verbena cardiometabolic MA, whose benefit was larger with combination products.
- **Near-miss condition:** garlic for endometriosis pain is not ordinary period pain (inv. 12c).
- **Conflicts with a safety warning:** garlic mouthwash (raw garlic on mucosa vs the burn warning).
- **Agrimony:** no new human study exists; settled.
