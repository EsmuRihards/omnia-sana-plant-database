# Deep re-sweep - batch 6 (2026-11-12)

Plants 51-60: wild carrot, wild yam, echinacea, cardamom, eleuthero, couch grass, small-flowered
willowherb, field / meadow / wood horsetail. 56 pairs before, 60 after.

Method as in `deep01.md`. Result:
- 85 changes.
- 16 refs added (REF-3536..3551).
- Log: `d06_changes.tsv`. Fixer: `fix_deep06.py`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Echinacea / cold | Only one positive trial and the Cochrane null were shown. Four *E. purpurea* trials found **no benefit**: Taylor 2003 JAMA (children; more rashes), Yale 2004, Sperber 2004 (rhinovirus), O'Neil 2008 | All four recorded as no-effect. Added 3 positive trials (incl. children prevention) and a 2025 MA in children. The note now says "results are mixed" |
| Eleuthero / fatigue | A chronic-fatigue RCT (Hartz 2004: "overall efficacy was not demonstrated") was missing. A review concluding *no* endurance benefit was filed as ergogenic evidence | Both recorded as no-effect. The review was removed from the action |
| Echinacea | A pilot whose authors say effectiveness "could not be accurately assessed" was filed as antimicrobial evidence | Removed from the action |
| Field horsetail | Its diuretic RCT and EU monograph were filed under anti-inflammatory, anti-rheumatic and antimicrobial actions | Removed from those actions |
| Willowherb | A fireweed (*E. angustifolium*) review was filed under *E. parviflorum* | Moved to fireweed. Genus reviews hidden from its mechanistic cards |

## Medium

- **Cardamom.** A small uncontrolled BP study was filed under three unrelated actions. Removed.
- **Wild yam.** A pain/inflammation rodent study was filed as antispasmodic evidence. Removed.
- **Horsetails (meadow, wood).** A study of silver nanoparticles made *with* horsetail extract was
  filed as the plant's own antioxidant evidence. Removed.
- **Claim notes:** 34 rewritten.

## Added under the owner rule

| Plant | New pair | Source |
|---|---|---|
| Echinacea | eczema | Alkylamide cream RCT |
| Cardamom | high-blood-pressure | MA |
| Cardamom | high-cholesterol | 2 MAs (triglycerides only, labelled) |
| Cardamom | nausea | Aromatherapy RCT |

Also wired:
- Cardamom: CV MA; inflammation MA and RCT.
- Echinacea: immune RCT; its held RCT made direct.

## For you to decide

- **Wild carrot / fertility.** A carrot-seed RCT improved low libido (hypoactive sexual desire).
  But the record's own evidence reports estrogenic, pregnancy-interceptive effects of the seeds. I
  did not add a "fertility" pair.

Validate 0 errors; refs 3335/3335.
