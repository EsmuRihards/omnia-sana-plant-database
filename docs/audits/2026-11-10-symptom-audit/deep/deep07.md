# Deep re-sweep - batch 7 (2026-11-12)

Plants 61-70: California poppy, eucalyptus, eyebright, meadowsweet, dropwort, fennel, white
bedstraw, cleavers, reishi, gentian. 64 pairs before, 70 after.

Method as in `deep01.md`. Result:
- 64 changes.
- 11 refs added (REF-3552..3562); 2 deleted.
- Log: `d07_changes.tsv`. Fixer: `fix_deep07.py`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Reishi / blood sugar, metabolic | The Cochrane review (2015: trials "do not support" reishi for CV risk factors in type 2 diabetes) was missing | Recorded as no-effect on both. Notes say so |
| Reishi | A polysaccharide-structure chemistry paper was filed as evidence under seven actions | Kept for immunomodulator only |
| White bedstraw | Two of its three studies are of *Galium mollugo*, a separate species (POWO). A third names only *G. mollugo* | Purged (two deleted). No species-level evidence remains |
| Meadowsweet | A macrophage anti-inflammatory study was filed under eight actions (analgesic, diuretic, antimicrobial...) | Removed from the five it does not support |
| Fennel / muscle spasm | Inferred from gut/uterine smooth-muscle antispasmodic activity | Dropped (off-target) |

## Added under the owner rule

| Plant | New pair | Source |
|---|---|---|
| Eucalyptus | asthma | Two 1,8-cineole RCTs (signature compound, labelled) |
| Eucalyptus | sinusitis | Cineole RCT |
| Fennel | menopause | Held MA + RCT |
| Fennel | anxiety, depression | RCT in postmenopausal women. The MA's "unclear" psychological results recorded as no-effect |
| Reishi | fatigue | Neurasthenia RCT + cancer-fatigue pilot |
| Reishi | stress | RCT |

Also added:
- Eucalyptus: cineole COPD RCT (respiratory support).
- Fennel: dysmenorrhoea MA.

## Gaps and negative findings (not added)

- **Eucalyptus cough.** A 2022 MA found efficacy "minimal and of uncertain clinical importance".
  There is no cough pair, so it was not recorded.
- **Meadowsweet.** The EU monograph names the common cold. There is no SR/RCT, so no pair.
- **Fennel.** The EU monograph names bloating and flatulence. There is no SR/RCT, so no pair. An
  infantile-colic RCT exists, but colic is not bloating.
- **Gentian.** The PubMed "gentian" trials are gentian violet, a synthetic dye.

Validate 0 errors; refs 3344/3344. Claim notes: 36 rewritten.
