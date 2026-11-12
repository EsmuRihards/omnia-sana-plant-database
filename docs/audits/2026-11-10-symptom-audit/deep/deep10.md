# Deep re-sweep - batch 10 (2026-11-12)

Plants 91-100: bay laurel, lavender, shiitake, motherwort, flaxseed, yellow loosestrife, Oregon
grape, mallow, horehound, chamomile. 85 pairs before, 100 after (plus one St John's wort pair
dropped, cross-batch).

Method as in `deep01.md`. Result:
- 112 changes.
- 39 refs added (REF-3609..3647); 2 deleted; 1 title corrected.
- Log: `d10_changes.tsv`. Fixer: `fix_deep10.py`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Lavender | Held Silexan anxiety MA and a herb network MA were never wired to any pair. Lavender had no anxiety pair | Anxiety, depression, stress and pain pairs added from MAs and RCTs |
| Flaxseed | Large MA literature on blood pressure, cholesterol, blood sugar and constipation, none wired | Four new pairs. The 2016 CRP MA (no overall effect) recorded as no-effect |
| Chamomile / muscle spasm | The EU monograph's "minor spasms" are gut spasms. Off-target | Dropped |
| Chamomile / anxiety | Herb network MA found chamomile not significant vs placebo | Recorded as no-effect |
| Bay, St John's wort / bruising | Only support was wound-healing evidence. A wound is not a bruise | Dropped |
| Shiitake | A 1989 anti-obesity observation was filed under six actions | Removed from all six |
| Flaxseed | A stearidonic-acid paper (not flax) supported three actions | Deleted |
| Yellow loosestrife | One study is of a different *Lysimachia* species | Deleted |
| Motherwort | A bibliography title did not match its DOI | Corrected |

## Added under the owner rule

| Plant | New pair | Source |
|---|---|---|
| Lavender | anxiety | 2 held MAs + 2 MAs |
| Lavender | depression | MA + RCT (an inconclusive SR recorded as no-effect) |
| Lavender | stress | MA |
| Lavender | pain | 2 SRs (postoperative, episiotomy) |
| Flaxseed | high blood pressure | 2 MAs + held RCT |
| Flaxseed | high cholesterol | 2 MAs |
| Flaxseed | blood sugar | 3 MAs |
| Flaxseed | constipation | 2 RCTs |
| Chamomile | menopause, hot flashes | 2 RCTs |
| Chamomile | PMS | RCT vs mefenamic acid |
| Chamomile | migraine | RCT |
| Chamomile | oral health | 2 RCTs + SR |
| Chamomile | back pain | RCT |
| Mallow | eczema | RCT |
| Mallow | oral health | 2 RCTs + EU monograph |

Also added:
- Lavender: 2 sleep MAs.
- Shiitake: an immunity RCT; a cancer MA and SR (add-on; no survival benefit).
- Oregon grape: a psoriasis MA; an atopic dermatitis trial.
- Chamomile: anxiety/sleep MA, anti-inflammatory MA, a tea RCT for blood sugar. The 2013 UV-erythema RCT is no-effect for skin.

## Web source checked

- Herbal Reality Oregon grape page: names arthritis, skin, mouth and gut infections, infected
  wounds, psoriasis, eczema and digestion. It lists references.

## Gaps (not added)

- **Mallow constipation.** A placebo-controlled trial, but randomisation is not stated.
- **Flaxseed hot flashes.** Two null RCTs. There is no hot-flash pair.
- **Oregon grape digestion.** Traditional only.

Validate 0 errors; refs 3422/3422.
