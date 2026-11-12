# Deep re-sweep - batch 5 (2026-11-12)

Plants 41-50: blessed thistle, coffee, cordyceps, coriander, midland hawthorn, hawthorn, saffron,
cumin, turmeric, artichoke. 62 pairs before, 77 after.

Method as in `deep01.md`. Result:
- 201 changes.
- 29 refs added (REF-3507..3535); 2 deleted; 4 repaired.
- Log: `d05_changes.tsv`. Fixer: `fix_deep05.py`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Artichoke / cholesterol, heart | The Cochrane review cited as support was **withdrawn** by Cochrane in 2016. Its own conclusion was "not convincing" | Purged and deleted. Both pairs still rest on 3 positive MAs and 2 RCTs |
| Hawthorn (both species) / heart | The two large heart-failure trials were missing: SPICE (no effect on primary endpoint) and HERB CHF (no benefit) | Both recorded as no-effect. The note now states the mixed result |
| Coriander / skin irritation | In a placebo-controlled UV-erythema test, coriander was not significantly better than vehicle | Inferred pair dropped (contradicted). Recorded as no-effect for inflammation |
| Cumin | All five actions carried the same ~15-ref bucket: two allergy reviews, EU Official Journal texts, a Latvian dictionary, history pieces, and the **null** glycaemic MA | Cleared. The non-evidence refs are kept in references |
| Saffron | Its depression RCTs were filed under six unrelated actions (anti-inflammatory, anticancer...) | Removed from those actions |
| Coffee | An EFSA caffeine *safety* opinion, a trade report and a sports position stand were filed as antioxidant/neuroprotective evidence | Removed |
| Turmeric | A piperine pharmacokinetics study was filed under all six actions | Removed |

## Medium

- **Coriander.**
  - REF-1702 duplicated REF-0151 (same DOI). Merged.
  - WHO vol. 1 (no coriander monograph) purged.
- **Cumin.**
  - REF-0286's URL pointed to a variational-autoencoder paper. It is Tavakoli-Rouzbehani 2022 (PMID
    34825421) and was repaired.
  - Two DOIs had "/full" appended.
  - Muscle spasm dropped: the antispasmodic evidence was gut smooth muscle (off-target).
- **Hawthorn.** Arrhythmia rat studies were filed under "antispasmodic". One of them found
  hawthorn *aggravated* arrhythmias. Removed.
- **Claim notes:** 45 rewritten.

## Added under the owner rule (SR/MA or RCT names the symptom and finds benefit)

| Plant | New pair | Source |
|---|---|---|
| Turmeric | blood-sugar, high-cholesterol, high-blood-pressure | GRADE MAs + SR (curcumin labelled as signature compound) |
| Turmeric | ibd | MA + held MA |
| Turmeric | psoriasis | Held MA |
| Turmeric | depression | MA |
| Saffron | anxiety | GRADE MA + RCT |
| Saffron | pms | RCT + MA |
| Saffron | menstrual-cramps | MA |
| Saffron | metabolic-support, blood-sugar | MAs |
| Artichoke | high-blood-pressure, blood-sugar | MAs |
| Coffee | liver-support | Cirrhosis MA (observational, labelled) |
| Coffee | blood-sugar | T2D MA (observational, labelled) |
| Cumin | high-cholesterol | 2 MAs |
| Midland hawthorn | high-blood-pressure | Walker 2006 RCT |

Also added to existing pairs:
- Saffron:
  - Sleep RCT.
  - OA RCT.
  - Alzheimer's RCT (cognition, memory).
  - GRADE MA (depression).
- Artichoke:
  - Holtmann 2003 dyspepsia RCT.
  - Liver MA + RCT.
  - Cardiometabolic MA.
  - Cholesterol RCT.
- Cordyceps: immunity RCT.
- Coriander: tinea pedis RCT.
- Cumin: weight-loss RCT.
- Turmeric: inflammation and obesity MAs.

## For you to decide

- **Turmeric / liver support.** A GRADE meta-analysis reports improved liver function. But
  turmeric-associated liver injury is documented (Tuscany phytovigilance SR, PMID 32656820). I did
  not add the pair.

## Carried to later batches

- REF-3527 (UV-erythema RCT) also tested chamomile, lemon balm, witch hazel and tea tree. None was
  significant vs vehicle.

Validate 0 errors; refs 3319/3319.
