# Symptom-tool audit - batch 12 of 19 (2026-11-12) - FIXED

Plants 111-120: origanum-majorana, origanum-vulgare, oxalis-stricta (no indications),
oxycoccus-palustris, panax-ginseng, passiflora-incarnata, paullinia-cupana, pelargonium-sidoides,
petasites-hybridus, petroselinum-crispum. 65 pairs.

No new owner policy this batch; standing rules applied.

Result: 98 changes; site-wide pairs 1,349 -> 1,340; 2 refs deleted. Logs: `batch12_changes.tsv`,
`batch12_followup_changes.tsv`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Ginseng / cognition (8) | Cochrane "Ginseng for cognition" ("a lack of convincing evidence") was **cited as support**. Two of its general sources (a 1999 commentary and a review tagged RCT) name no condition | Null recorded; both removed from all 12 pairs. The AFP review is kept for immunity, diabetes and inflammation. Cognition 8 -> 2; heart and muscle soreness dropped |
| Guarana / fatigue (9) | The cancer-fatigue meta-analysis ("did not reduce cancer-related fatigue", p = 0.98) was **cited as support**. The two RCTs measured memory/alertness and cycling, not fatigue | Null recorded; RCTs removed; pair dropped |
| Cranberry / urinary | The Cochrane cranberry-UTI review covers **American** cranberry (*V. macrocarpon*), not the European small cranberry | Deleted (wrong species); the *V. oxycoccos* review remains |
| Pelargonium / cold, sinusitis, bronchitis | Cochrane 2008 is superseded by its 2013 update. The 2013 version ("may be effective", low-quality evidence) wasn't cited directly | 2008 merged into 2013; the 2013 review is now direct support per your may-be-effective rule. Cold 2 -> 7 |
| Butterbur / 8 pairs | Pediatrics in Review column with no abstract or retrievable text. Its fever pair was really **hay fever** | Removed; fever dropped. Migraine (2 RCTs), allergy (SR) and asthma keep their sources |
| Parsley / 9 pairs | Its main review was tagged RCT. Diuretic studies were cited for swelling and UTI | Retagged; bad breath, swelling and UTI dropped; scores 5 -> 1-2 |

## Medium

- **Passionflower.** The anxiety SR was removed from insomnia and nervous tension. The EU monograph
  (mental stress, sleep) was removed from anxiety and nervous tension. Insomnia 9 -> 6; it still has
  2 RCTs.
- **Marjoram.** Hoffmann was removed from 10 pairs.
- **Oregano.** The carvacrol review is kept for infection only (compound evidence). Arthritis and
  inflammation dropped.
- **Retags:** 12 refs.

## For your spot-check (EMA returns 429)

- Passionflower monograph REF-0491 (stress, sleep).

Validate 0 errors; refs 3199/3199.
