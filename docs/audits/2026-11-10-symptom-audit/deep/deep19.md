# Deep audit - batch 19 (2026-11-13)

Plants 181-188: speedwell, cramp bark, sweet violet, heartsease, chasteberry, ashwagandha,
corn silk, ginger. 68 pairs before, 68 after. This is the last batch: all 188 plants have now
had the second-pass and deep audit.

Same two-part pass as batches 14-18: the strict `!NAME` check plus the deep checks.

Result:
- 200 changes.
- 28 refs added (REF-3850..3877); 1 deleted.
- Log: `d19_changes.tsv`. Fixer: `fix_deep19.py`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Ashwagandha | Every pair was mechanistic-only, although held MAs and RCTs named sleep, memory and cognition. Safety note #1 has no source and does not mention the liver | Sleep MA and the MCI RCT wired. New stress, anxiety and depression pairs (below). New safety note on idiosyncratic, often cholestatic liver injury (2026 scoping review) |
| Ginger | A 2008 review was pinned to 12 pairs. A warfarin-bleeding study and a T2D MA were cited for 5 actions. Pregnancy and chemotherapy nausea studies were filed under indigestion. The null CINV RCT was cited as support | Review moved to mechanistic where unnamed. Respiratory support and muscle spasm dropped. Actions cleaned. Nausea studies moved off indigestion. CINV RCT recorded as no-effect for nausea |
| Ginger / migraine, arthritis | A migraine-prophylaxis placebo RCT (no benefit) and a 2020 knee-OA MA ("insufficient evidence") were missing | Both recorded as no-effect, beside a positive acute-migraine MA and a 2015 OA MA |
| Chasteberry | A genus-level *Vitex* review was on 4 pairs. A cohort study of VAC products (one a homeopathic combination) was on 3. A 2019 MA ("most trials cannot be used as evidence") was cited as support | Genus review and cohort removed; acne dropped. MA moved to no-effect. Four placebo RCTs added (Schellenberg 2001 BMJ, two Chinese BNO 1095 trials, Ze 440) |
| Corn silk | A review was on 7 pairs it never names. Cough, sore throat and infection had no other source | Moved to mechanistic. Cough, sore throat and infection dropped. Grieve's corn silk entry (cystitis, bladder irritation, gravel) now carries UTI and urinary support |
| Cramp bark | A ScienceDirect Topics page (403) was cited. Headache was not named by Herbal Reality. A rat endometriosis study was filed under cramps | Topics page purged and deleted. Headache dropped. Cramps are now traditional-only (verified changed to needs-review) |
| Heartsease | A case report on multi-herb products and a multi-herb anti-cytokine preparation were cited | Removed. Grieve and Herbal Reality (covers *V. tricolor*) now source eczema, psoriasis, arthritis and skin irritation |
| Speedwell | A DNA-barcoding adulteration study and 1970s phytochemistry papers were cited for actions. Bloating and bronchitis were not named by HerbaZest | Removed. Bloating dropped. Grieve added |

## Added under the owner rule

| Plant | New pair | Source |
|---|---|---|
| Sweet violet | fever | triple-blind placebo RCT |
| Ashwagandha | stress | 2 MAs + 2 RCTs; a cortisol-only MA recorded as no-effect for perceived stress |
| Ashwagandha | anxiety | 3 MAs |
| Ashwagandha | depression | 2026 MA |
| Ginger | blood sugar | 2 MAs |
| Ginger | high blood pressure | 2026 MA |
| Ginger | migraine | MA; prophylaxis RCT recorded as no-effect |
| Ginger | muscle soreness | 2 placebo RCTs |

Also added:
- Sweet violet: an insomnia MA, a menopausal sleep RCT, and a COVID RCT (cough, headache).
- Ashwagandha: a 2026 cognition MA.
- Ginger:
  - dysmenorrhoea MA (menstrual cramps now verified);
  - CINV MA;
  - inflammation-marker MA.
- Grieve entries: speedwell, guelder rose, sweet violet, heartsease, ginger, corn silk.

## Gaps (not added)

- **Sweet violet:** allergic-rhinitis RCT (no abstract available).
- **Heartsease:** the only RCT is a three-herb ointment.
- **Chasteberry:** a menstrual-bleeding MA found no effect, but there is no heavy-bleeding pair to record it on.
- **Ashwagandha:** a glucose MA (very low certainty). Safety note #1 is still unsourced.
- **Corn silk:** lipid MA of Chinese modified decoctions (unblinded).
- **Ashwagandha:** the LiverTox chapter had no abstract to import, so the scoping review was used instead.

Validate 0 errors; refs 3632/3632.
