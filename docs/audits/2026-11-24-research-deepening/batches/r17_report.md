# Research-deepening batch 17 (2026-11-26)

**Plants:** sea buckthorn, hops, goldenseal, St John's wort, hyssop.

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex.
- **Name overrides:** added for all five plants.
- **Goldenseal:** berberine-only trials were not counted as goldenseal evidence, because berberine also comes from barberry and *Coptis*.

**Outcome:**
- **Search volume:** about 2,500 PubMed hits (St John's wort about 1,940; its depression pair and approved interactions were not padded) and about 45 abstracts read.
- **New references:** 17 (REF-5404..5420).
- **Symptom-tool pairs:** 1,468 -> 1,472.
- **Checks:** validate passes, with refs cited 4,195 / declared 4,195. The species audit raised no flags on the new references.
- **Files:** change log `r17_changes.tsv`; fixer `../fix_r17.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Hops | bad breath | new | 7 | 2026 pooled analysis of seven randomized company studies: hops beta-acid toothpastes cut morning-breath sulphur compounds, dose-dependently |
| Sea buckthorn | eye strain / eye health | new | 6 | 2010 double-blind placebo RCT of oral oil in dry eye, plus a 2019 eyelid-spray study |
| Sea buckthorn | blood sugar | 2 | 5 | 2021 randomized crossover trial (small fall in fasting glucose); the null meta-analysis stays alongside, and the note says "mixed" |
| Sea buckthorn | liver support | new | 5 | 2003 randomized trial in cirrhosis vs a vitamin B control (lower fibrosis markers) |
| Hops | metabolic support | new | 5 | 2016 double-blind placebo RCT of matured hop extract (visceral and body fat fell) |

## Safety and other tool data

**Goldenseal:**
- New info note: human studies found no meaningful change in indinavir, digoxin or, overall, metformin levels. (The approved CYP3A4 / CYP2D6 interaction stands.)
- New caution: a child's high blood sodium appeared to be worsened by goldenseal (case report).
- New caution: in two-year US National Toxicology Program studies, goldenseal root powder increased liver tumours in rats and mice.

**Hops:**
- New info note: no clinically relevant effect on four drug-metabolising enzymes (2020 phase I study).
- New allergy caution.

**St John's wort:** the approved contraceptive interaction now cites a 2016 systematic review (breakthrough bleeding, lower hormone levels, possible ovulation).

**Hyssop:** new caution. In a 2024 randomized asthma trial, a post-hoc analysis found benefit only with productive cough; lung function got worse in people with a dry cough.

**Sea buckthorn:** new info note: heavy intake can turn the skin yellow (harmless).

**Draft interactions:** none new this batch. Three from batch 16 are pending: hibiscus × statins, hibiscus × anticoagulants and devil's claw × anticoagulants.

## For the owner

1. **Hops bad breath (7) rests on company-run studies.** They are randomized, but the toothpaste maker ran all of them; the note says "company studies".
2. **Hyssop asthma:** no pair was created, because benefit appeared only in a post-hoc subgroup. The harm signal in the dry-cough subgroup is shown as a caution instead.

## Settled or no change

**St John's wort:** only the contraceptive review was added. The 2012 dental pain meta-analysis was homeopathic (*Hypericum* with *Arnica*), and the OCD, neuropathic pain and smoking reviews found no benefit or have no vocabulary condition.

## Rejected or not added (main reasons)

**Sea buckthorn:**
- A nephrotic syndrome add-on study (randomisation not stated).
- A postprandial trial that found no glucose effect.
- Compound suppositories and other combinations.

**Hops:**
- A sexual-function trial vs oestradiol (active comparator).
- Hop + valerian and soy + hop combinations.
- Xanthohumol-only trials (single compound).
- Plaque studies (a surrogate).

**Goldenseal:** berberine-only studies, a multi-ingredient photosensitivity case, and lab work.
