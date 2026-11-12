# Deep re-sweep - batch 3 (2026-11-12)

Plants 21-30: pleurisy root, astragalus, bacopa, birch, bistort, borage, boswellia, calendula,
tea, peach-leaved bellflower. 59 pairs before, 69 after.

Method as in `deep01.md`. Result:
- 128 changes (incl. 1 follow-up).
- 36 refs added (REF-3449..3484); 3 deleted.
- Logs: `d03_changes.tsv`, `d03_followup_changes.tsv`. Fixer: `fix_deep03.py`.

**Owner answer (this batch).** Systematic reviews that pool only lab or animal studies keep scoring
as systematic reviews. REF-2124 (calendula/cancer) is unchanged.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Pleurisy root (all) | The only source was a web page with no checkable references | Purged. Grieve's Pleurisy Root entry now sources respiratory support. Bronchitis and cold remain inferred only |
| Calendula / skin irritation | Inferred only, although 4 RCTs exist (radiation, diaper, contact dermatitis) | All 4 added. The 2021 radiation trial (no difference vs moisturiser) recorded as no-effect |
| Borage / eczema | Oral borage oil does **not** help eczema (Cochrane; BMJ 2003 trial) | Both recorded as no-effect. Added a topical (undershirt) RCT. The note separates the two |
| Borage / immune support | The only card showed immune **suppression** (inflammasome) | Dropped |
| Borage / inflammation | Its asthma RCT found no fall in airway inflammation, yet it was filed as anti-inflammatory evidence | Moved to no-effect |
| Green tea / weight | The Cochrane review (small, non-significant weight loss) was missing | Recorded as no-effect. A 2020 positive MA added. The note gives both |
| Green tea / blood sugar | A meta-analysis in type 2 diabetes found no effect | Recorded as no-effect. The 17-trial MA (positive) added |
| Astragalus / fatigue | The Astragalus-polysaccharide chemotherapy-fatigue RCT was null overall | Recorded as no-effect. A cancer-fatigue MA and a post-COVID RCT added |
| Birch | Its EMA public summary (urinary flushing only) was filed under 10 actions | Removed from all but diuretic |

## Medium

- **Birch.**
  - The genus review now counts only where it names *B. pendula* (joint disease).
  - Infection and wounds dropped (prose-only genus claims).
  - Back pain dropped: an RA lymphocyte study is off-target.
- **Wrong or empty sources removed.**
  - WHO volume 2 (no monograph) purged from bacopa and borage.
  - The 404 WebMD page purged from bistort.
  - A GC-MS-only study taken out of bistort's antimicrobial action.
  - Bellflower: a *Campanula alliariifolia* study purged; a genus review removed from its actions.
- **Astragalus.** Its Cochrane CKD review ("no definitive conclusions") was removed from the
  nephroprotective action.
- **Boswellia.** The arthritis note claimed rheumatoid arthritis, but there is no RA source. Trimmed.
- **Claim notes:** 40 rewritten.

## Added under the owner rule (SR/RCT names the symptom and finds benefit)

| Plant | New pair | Source |
|---|---|---|
| Tea | high-cholesterol, high-blood-pressure | MAs + Cochrane 2013 |
| Astragalus | blood-sugar | Adjuvant-T2DM MA |
| Bacopa | anxiety, depression | Calabrese 2008 RCT. Anxiety also has a null trial recorded |
| Borage | high-cholesterol | RCT: TG and HDL only |
| Borage | asthma | Phase II RCT |
| Boswellia | blood-sugar | MA |
| Boswellia | ibs, asthma, diarrhea | Casperome RCTs |
| Boswellia | heavy-bleeding | RCT |
| Boswellia | infection | VVC RCT |
| Boswellia | cognitive-function | TBI pilot RCT |

Also wired to existing pairs:
- Bacopa / memory: Pase 2012 SR and two memory RCTs.
- Bacopa / cognition: its held MA made direct.
- Boswellia: the Aflapin RCT and a 2024 MA.
- Borage: the Leventhal 1993 RA RCT.
- Calendula: a hand-wound RCT and the held VVC RCT.
- Astragalus: immune MA, athlete RCT, training RCT.

## Gaps (traditional only, not added)

- Pleurisy root: Grieve's diarrhoea, rheumatism and eczema uses have no pairs.

Validate 0 errors; refs 3270/3270.
