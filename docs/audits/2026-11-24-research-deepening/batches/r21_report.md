# Research-deepening batch 21 (2026-11-26)

**Plants:** chamomile, lemon balm, peppermint, bitter melon, noni.

**Sources searched:** PubMed (5 query families), Europe PMC, ClinicalTrials.gov and OpenAlex.
- **Name overrides:** added for all five plants (for example *Matricaria recutita* for chamomile and Cyracos for lemon balm).
- **Europe PMC:** completed without failures and added nothing new beyond PubMed.

**Outcome:**
- **Search volume:** about 3,100 PubMed hits (peppermint about 1,180, chamomile about 575) and about 110 abstracts read.
- **New references:** 38 (REF-5483..5520).
- **Symptom-tool pairs:** 1,484 -> 1,489.
- **Checks:** validate passes, with refs cited 4,295 / declared 4,295. The species audit raised no flags on the new references.
- **Files:** change log `r21_changes.tsv`; fixer `../fix_r21.py`.

## Score changes

| Plant | Symptom | Before | After | Why |
| --- | --- | --- | --- | --- |
| Peppermint | menstrual cramps | 1 | 7 | 2025 systematic review of five randomized trials |
| Peppermint | cognitive function | 2 | 6 | 2018 placebo-controlled crossover study (oil capsules) and a 2025 randomized tea trial |
| Chamomile | bloating | 1 | 5 | 2023 triple-blind RCT: less flatulence after gallbladder surgery |
| Chamomile | headache | new | 5 | 2024 double-blind RCT: fewer post-dural-puncture headaches |
| Chamomile | sinusitis | new | 5 | 2021 double-blind RCT of nasal drops in chronic rhinosinusitis |
| Lemon balm | blood sugar | new | 5 | 2019 double-blind RCT (fasting glucose, HbA1c); a 2019 product trial with no effect stays alongside |
| Lemon balm | menstrual cramps | 1 | 5 | 2017 double-blind dysmenorrhoea RCT |
| Lemon balm | PMS | new | 5 | 2018 placebo RCT in adolescents |
| Lemon balm | low libido | new | 5 | 2018 double-blind RCT (FSFI) |

**No-effect studies recorded:**
- Chamomile radiation-dermatitis gel (skin irritation).
- Peppermint in pregnancy nausea.
- Bitter melon body-weight meta-analysis (metabolic support).

## Safety and other tool data

**Noni:**
- New liver caution. Several hepatitis cases followed noni juice, including a liver transplant and a 14-year-old boy, plus one after a noni skin cream. A 28-day double-blind safety study found no adverse effects.
- New potassium caution: hyperkalaemia in chronic kidney disease.
- New info note: noni extract increased ranitidine absorption.

**Bitter melon:**
- New liver caution: "asowosi" tea, one case rated highly probable.
- New kidney caution: interstitial nephritis from a pure extract.

**Peppermint:**
- New allergy caution: 0.6% of 28,128 patients patch-tested in North America reacted. Some capsules contain peanut oil.
- Info notes: one possible liver case in the Berlin surveillance study, and the effect of peppermint tea on drug enzymes.

**Chamomile:**
- New info note from a 2025 adverse-event review: side effects are uncommon and mild, and case reports describe anaphylaxis.
- New info note: two randomized clotting studies found little or no effect in people not taking warfarin.

**Lemon balm:** info notes on a possible withdrawal case and on guideline toxicology (no harm found in rats).

**Draft herb-drug interactions (need owner sign-off):**

| Plant | Drug class | Severity | Basis |
| --- | --- | --- | --- |
| Noni | anticonvulsants | caution | A man on phenytoin had persistently low levels while drinking noni juice daily; a 2025 systematic review advises avoiding the combination |
| Bitter melon | chemotherapy agents | caution | Acute pancreatitis four days after a patient on long-term pazopanib started bitter melon; no recurrence when pazopanib was restarted alone (case report) |

Four earlier drafts are still pending:
- hibiscus × statins
- hibiscus × anticoagulants
- devil's claw × anticoagulants
- flax × anticoagulants

## Research-integrity hold

None of the new lemon balm or chamomile references is first- or last-authored by the flagged Tehran psychopharmacology group.

## For the owner

1. **The two new drafts above** need sign-off.
2. **Chamomile × anticoagulants (approved) rests on one warfarin case.** Two new randomized studies found little or no effect on clotting tests in healthy people not taking warfarin. I added them as an info note and left the interaction unchanged. Tell me if you want it re-graded.
3. **Noni liver note uses severity "caution".** It covers several cases, including one transplant, so the same question as bay laurel applies: "caution" or "warning".

## Gaps and settled plants

- **Lemon balm cognition:** no pair. The rosmarinic-acid extract RCTs (2020, 2022) found no cognitive difference, and a 2026 acute study missed its primary outcome.
- **Noni dysmenorrhoea:** a double-blind RCT found no effect. There is no pair to attach it to, so it is recorded in the plant notes.
- **Peppermint dyspepsia:** the trials test peppermint plus caraway combinations.

## Rejected or not added (main reasons)

- **Strong pairs were not padded:** chamomile anxiety, oral health, insomnia and pain; lemon balm anxiety, depression and cholesterol; peppermint IBS and pain; bitter melon blood sugar and cholesterol.
- **Combinations:** Iberogast, Menthacarin, Ze 185, Hyponidd and aroma blends.
- **Active-comparator trials:** for example vs citalopram, lidocaine or clotrimazole.
- **No abstract:** letters, including the noni warfarin-resistance and peppermint hepatotoxicity letters.
- **Confounded or disputed noni cases:** one with interferon-beta, one with Herbalife products.
