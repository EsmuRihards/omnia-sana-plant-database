# Research-deepening batch 10 (2026-11-25)

**Plants:** common hawthorn, saffron, cumin, turmeric, artichoke.

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex. Six Europe PMC queries timed out; the rest completed, and about 210 Europe PMC-only hits were screened by title, with 19 read in full abstract.

**Outcome:**
- **Search volume:** about 10,600 PubMed hits (turmeric alone: about 8,200; reviews, meta-analyses and safety were read in depth) and about 80 abstracts read, plus one full text (the data-integrity analysis below).
- **New references:** 28 (REF-5287..5314).
- **Symptom-tool pairs:** 1,441 -> 1,453.
- **Checks:** validate passes, with refs cited 4,089 / declared 4,089. The species audit raised no new flags.
- **Files:** change log `r10_changes.tsv`; fixer `../fix_r10.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Common hawthorn | high blood pressure | new | 7 | 2025 meta-analysis of placebo RCTs of *Crataegus* extracts (same evidence as midland hawthorn, batch 9) |
| Saffron | insomnia | 5 | 8 | 2022 meta-analysis of RCTs (sleep quality and duration) |
| Saffron | high cholesterol | new | 7 | 2022 dose-response meta-analysis of RCTs (triglycerides, total and LDL cholesterol) |
| Saffron | high blood pressure | new | 7 | Same meta-analysis (systolic pressure) |
| Saffron | low libido | new | 5 | 2024 triple-blind RCT: saffron + vitamin E vs vitamin E alone; the libido domain improved |
| Saffron | menopause | new | 5 | 2021 placebo RCT (affron): psychological symptoms of perimenopause improved; hot flushes did not |
| Cumin | cognitive function | new | 5 | 2026 double-blind placebo RCT of cumin essential oil in healthy older adults |
| Turmeric | oral health | new | 9 | 2024 meta-analysis and two systematic reviews: turmeric/curcumin gel or mouthwash for radiotherapy mouth sores (oral mucositis) |
| Turmeric | indigestion | 1 | 5 | 2022 Thai RCT in functional dyspepsia: better than placebo, similar to omeprazole (until now it rested on the WHO monograph alone) |
| Turmeric | prostate support | new | 7 | 2026 meta-analysis: curcumin added to prostate medicines improved symptom scores vs placebo |
| Turmeric | hot flushes | new | 5 | 2026 pilot placebo RCT of curcuminoids; a 2025 review found the evidence conflicting (recorded as no-effect) |
| Turmeric | PMS | new | 5 | 2025 double-blind placebo RCT of curcumin |
| Turmeric | menstrual cramps | new | 5 | Same trial (pain scores in cycles 2 and 3) |
| Turmeric | fatigue | new | 5 | 2025 double-blind placebo RCT of curcumin in postmenopausal women |
| Artichoke | high blood pressure | 7 | 9 | 2022 dose-response meta-analysis and a 2020 placebo RCT in hypertension |
| Artichoke | blood sugar | 7 | 8 | 2020 placebo RCT of a standardised extract in impaired fasting glucose |

Artichoke liver support also gained a 2022 liver-enzyme meta-analysis (score unchanged). The curcumin-only turmeric pairs say "curcumin, turmeric's signature compound" (invariant 10).

## Safety and other tool data

**Turmeric:**
- New caution: lead-chromate adulteration of turmeric powder in South Asia (2024 study), a likely lead source for children in rural Bangladesh (2014 study).
- New caution: kidney failure from oxalate nephropathy in a long-term supplement user (case report, 2024).
- The approved anticoagulant interaction gains its first human source: a probable INR rise with fluindione, a vitamin K antagonist (case report). Until now it cited only a rat study; the text is unchanged.

**Saffron:**
- The pregnancy caution now cites a 2026 integrative review (low doses studied for labour; excessive intake risky).
- New info note: saffron infusion modestly reduced CYP1A2 activity (about 14%, mainly in men); the authors judged meaningful interactions unlikely.
- New info note: 200-400 mg saffron tablets for a week were well tolerated in placebo-controlled safety studies, with no effect on clotting.

**Cumin:** the allergy note now cites a 2026 paediatric anaphylaxis case with a literature review.

**Common hawthorn:** the safety note now cites the 2006 systematic review of adverse events.

**Draft herb-drug interaction (needs owner sign-off):**

| Plant | Drug class | Severity | Basis |
| --- | --- | --- | --- |
| Saffron | anticoagulants and antiplatelets | caution | A man on rivaroxaban had nosebleeds and bleeding gums after starting a saffron supplement (2022 case report). The text also states that a 2014 placebo-controlled study found no effect on clotting factors. |

## For the owner

1. **Research-integrity flag (decision needed).** A 2026 analysis in *Research Integrity and Peer Review* (PMID 42288935) examined 223 RCTs from one psychopharmacology research group.
   - **Findings:** the trials show implausible baseline balance and dropout patterns, so they are unlikely to have been truly randomised. The authors caution against using their data.
   - **Reach into saffron:** by the authors' estimate, the group produced about a third of saffron-vs-placebo trials and two thirds of saffron-vs-active trials.
   - **Held this batch:** three new saffron candidate trials share that group's senior author and were **not added**: hot flushes, and two female sexual-function trials. The 2019 sexual-dysfunction meta-analysis that pools such trials was also held.
   - **Already in the database:** 8 references from the group.
     - Saffron cognitive function (5) and memory (5) each rest on one of these trials alone.
     - Saffron depression (2 of 6 refs) and PMS (1 of 2) cite them too.
     - So do passionflower anxiety (1 of 5) and sage cognition and memory (1 of 6 and 1 of 5).
   - **Not touched:** existing pairs are unchanged until you decide.
2. **The saffron draft interaction above** needs sign-off.
3. **Common hawthorn's blood-pressure pair** rests on a genus-level *Crataegus* meta-analysis, the same attribution the record already uses for cardiovascular support (the EU monograph covers both hawthorns). No *C. monogyna*-specific trial was found.
4. **Turmeric liver support was not added.** Meta-analyses in fatty liver disease found benefit, but the record carries a serious liver-injury warning (invariant 12d). This is the same rule applied to cassia in batch 8.

## Rejected or not added (main reasons)

**Saffron:**
- An erectile-dysfunction meta-analysis: not the same condition as low libido (near-miss).
- A 2025 crocin lipid meta-analysis: inconclusive.
- Saffron + fenugreek and other combinations.
- More depression umbrella reviews (the pair is already at 10).
- Preprints (menopause and PMS RCTs, a glycaemic meta-analysis).
- The trials held under item 1 above.

**Cumin:**
- Dead end: a 2015 double-blind RCT in NASH found no difference from placebo (no liver pair exists).
- An IBS case series (uncontrolled), combinations, a 1997 anaphylaxis letter (no abstract).
- Black cumin (*Nigella sativa*) and *Bunium persicum* (other species).

**Turmeric:**
- A 2026 cognition RCT (2 of 35 endpoints significant).
- Chemotherapy-neuropathy RCTs (sensory symptoms, not pain; near-miss).
- Periodontitis adjunct meta-analyses (local delivery, mixed photodynamic designs).
- Oral lichen planus vs corticosteroids, and mouth ulcers vs triamcinolone (active comparators only).
- Further liver-injury case reports (the serious warning already cites three case series).

**Artichoke:**
- A 2021 anthropometric meta-analysis (waist circumference only).
- Combinations with bergamot, red yeast rice or ginger.
- Network meta-analyses in fatty liver disease (artichoke not separable).
- Jerusalem artichoke (a different plant).
