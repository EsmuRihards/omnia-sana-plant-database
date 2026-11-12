# Symptom-tool audit - batch 11 of 19 (2026-11-12) - FIXED

Plants 101-110: melissa-officinalis, mentha-piperita, momordica-charantia, morinda-citrifolia,
nepeta-cataria, nigella-sativa, ocimum-tenuiflorum, oenothera-biennis, olea-europaea,
ononis-arvensis. 100 pairs.

No new owner policy this batch; standing rules applied. 1 ref added (REF-3396).

Result: 111 changes; site-wide pairs 1,367 -> 1,349. Logs: `batch11_changes.tsv`,
`batch11_followup_changes.tsv`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Evening primrose / eczema (8) | The Cochrane review (REF-0447), the BMJ editorial (REF-1458) and the EAACI meta-analysis were **cited as support**. All three say oral EPO doesn't work, and the claim note said so too | All moved to null_result_ids. Now inferred only (1); note rewritten |
| Evening primrose / PMS | Its 2024 review found EPO "did not demonstrate effectiveness" in PMS | Recorded as no-effect; the mastalgia RCT stays. 8 -> 5 |
| Bitter melon / blood sugar | The Cochrane review (no difference vs placebo; "insufficient evidence") was missing | Added (REF-3396) and recorded as no-effect. 6 -> 5 |
| Holy basil / anxiety (8) | Neither source names anxiety: the SR names stress and the RCT measured stress, mood and sleep | Removed; anxiety dropped. Stress keeps both |
| Noni / 12 pairs | The main review (REF-0197) names no condition ("clinical data are essentially lacking") | Removed. Pain, back pain, headache, blood sugar, metabolic and cold dropped |
| Lemon balm, catnip, restharrow | Hoffmann, BHP 1983, a rosmarinic-acid compound paper, and a 1978 Czech study with no text | Removed. Catnip dropped 5 pairs, restharrow 5; the EU lemon balm monograph (sleep, bloating, indigestion) added |
| Lemon balm / insomnia (5) | REF-0134 is an RCT of mood and cognition, not sleep | Removed: an RCT counts only for what it measured |

## Medium

- **Peppermint.** The IBS trial review (REF-0100) names IBS and abdominal pain, so it was removed
  from bloating, indigestion and muscle spasm; pain 5 -> 7. **Peppermint has no IBS pair,** though IBS
  is its best-evidenced use; adding one would be a new claim (your call). Two mint-genus assays were
  removed from cognition.
- **Olive.** The olive-leaf diabetes RCT names no heart outcome; heart 5 -> 2. The oil review was
  removed from 6 pairs. A leaf-polyphenol RCT was added to metabolic support.
- **Restharrow.** Its heart note described a study it doesn't cite; corrected.
- **Leak check:** two unverifiable sources were still visible as mechanistic cards on other pairs
  (restharrow UTI and swelling, shiitake cancer); they are now hidden. New tool: `mech_leak_check.py`.
- **Retags:** 9 refs (e.g. a multi-plant diabetes review tagged RCT).

## For your spot-check (EMA returns 429)

- Lemon balm leaf monograph REF-3078 (sleep, bloating, indigestion).

Validate 0 errors; refs 3201/3201.
