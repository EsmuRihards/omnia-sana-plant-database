# Deep audit - batch 17 (2026-11-13)

Plants 161-170: feverfew, tansy, dandelion, cacao, wild thyme, garden thyme, linden, ajwain,
turkey tail, red clover. 85 pairs before, 82 after.

Same two-part pass as batches 14-16: the strict `!NAME` check plus the deep checks.

Result:
- 246 changes.
- 26 refs added (REF-3791..3816); 5 deleted.
- Log: `d17_changes.tsv`. Fixer: `fix_deep17.py`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Red clover / hot flashes, menopause | The superseded 2007 Cochrane was cited. The 2013 Cochrane update ("no conclusive evidence" for phytoestrogens) and two large US placebo trials (ICE 2003; Geller 2009) were missing | 2007 version purged and deleted. The three nulls added. Two positive meta-analyses (2026 GRADE review; Promensil 80 mg) also added. The note now gives both sides |
| Red clover | A bone-density RCT was cited for anti-inflammatory, antioxidant, antispasmodic and expectorant actions and for heart support. A broiler-chicken study was also on heart support. Menstrual cramps rested only on two unverifiable books | Removed. Cramps and muscle spasm dropped. The books are kept only where Grieve agrees (cough, bronchitis) |
| Tansy | "The 1879 Beal seed viability experiment" was cited for 5 actions. Grieve was pinned to all 9 pairs. Bloating and indigestion contradict the record's own warning ("not recommended for internal use", thujone) | Seed paper purged and deleted. Bloating and indigestion dropped (own-warning rule). Cramps and muscle spasm also dropped (an emmenagogue). The tansy-specific Grieve entry kept only where it fits |
| Dandelion | A 2024 review was pinned to 13 pairs, 6 of which it never names. Two other reviews were in the same position. A 1993 diuretic screen ("no significant increase in urine volume") was cited as diuretic support. A genus-level review was used | Moved to mechanistic where unnamed. Grieve and Herbal Reality (has references; says clinical evidence is minimal) now carry the traditional uses. Diuretic screen recorded as no-effect. Genus review removed; wounds dropped |
| Feverfew / migraine | The 2000 Cochrane was cited (superseded by 2015). A failed dose-finding RCT and a "mixed" 2020 SR were cited as support. The positive MIG-99 RCT and a null RA trial were missing | Superseded review purged and deleted. Failed RCT and mixed SR moved to no-effect. MIG-99 (2005) added. The 1989 RA RCT recorded as no-effect for arthritis |
| Cacao / heart support | A cell study, a 2021 SR finding no effect in healthy people, and the COSMOS trial (primary endpoint null) were all cited as support. A confectionery technology book was cited for 4 actions | Cell study removed. SR and COSMOS moved to no-effect. Cochrane BP review added. Book purged and deleted |
| Garden thyme / cough, cold, bronchitis | The notes cited a thyme-ivy combination trial (not referenced, and a combination) | Rewritten to the EU monograph and Grieve. A thyme-only asthma-cough placebo RCT added |
| Turkey tail / cold | Its only card (a 2002 review) never names colds | Dropped |
| Ajwain | A review with a dead DOI was on 5 pairs. Two reviews were on cramps, oral health and indigestion, which they never name | Review purged and deleted. Menstrual cramps dropped. Oral health is now lab-only (needs-review) |

## Added under the owner rule

| Plant | New pair | Source |
|---|---|---|
| Cacao | high blood pressure | Cochrane + 2026 MA |
| Wild thyme | indigestion | 2026 multicentre placebo RCT |
| Garden thyme | anxiety, depression, insomnia, memory | RCT in university students |
| Garden thyme | oral health | RCT (halitosis, gingivitis) |
| Ajwain | pain | placebo RCT (neuropathic burning feet) + dental-injection RCT; a chemotherapy-neuropathy pilot recorded as no-effect |

Also added:
- Garden thyme: a thyme vs ibuprofen vs placebo dysmenorrhoea RCT. Menstrual cramps is now verified.
- Cacao: a chocolate-cognition MA (cognitive function, memory).
- Red clover: a lipid MA. The Howes 2004 cognition RCT added as no-effect.
- Turkey tail: Yun Zhi survival MA (cancer).
- Ajwain: an asthma bronchodilator study.
- Grieve entries: tansy, dandelion, garden thyme, wild thyme, lime, red clover.
- Linden: a safety note (Grieve) about narcotic effects of stale flowers.

## Other fixes

- Linden: the EU monograph covers cold symptoms and mild mental stress, so anxiety is now mechanistic. The stress note no longer cites *T. americana* animal data.
- Red clover: blood sugar is lab-only, so verified was changed to needs-review.
- 16 study_type retags.

## Gaps (not added)

- Feverfew: none new.
- Red clover: a glucose RCT whose primary outcome was not different.
- Linden: the only RCT is a four-ingredient sleep combination.
- Ajwain: the dyspepsia RCT used an Apium + ajwain combination.
- Turkey tail: the HPV trials used mushroom combinations.
- Thyme: honey-based RCTs (combination); Shirazi thyme is a different species.
- Dandelion: a jaw-surgery RCT combined it with borneol.
- The British Herbal Pharmacopoeia and Hoffmann's Medical Herbalism could not be checked online.

Validate 0 errors; refs 3572/3572.
