# Symptom-tool audit - batch 10 of 19 (2026-11-12) - FIXED

Plants 91-100: laurus-nobilis, lavandula-angustifolia, lentinula-edodes, leonurus-cardiaca,
linum-usitatissimum, lysimachia-vulgaris, mahonia-aquifolium, malva-sylvestris, marrubium-vulgare,
matricaria-chamomilla. 90 pairs.

Owner decision this batch (added to DATA_PRINCIPLES invariant 11): **a product registered as
homeopathic but made at mother-tincture strength (Reliéva, a 10% Mahonia cream) counts as plant
evidence**, labelled in the note. Serial dilutions still don't count.

Result: 144 changes; site-wide pairs 1,381 -> 1,367; 1 ref added (REF-3395). Logs:
`batch10_changes.tsv`, `batch10_followup_changes.tsv`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Mallow / pain, wounds (5) | The episiotomy RCT (REF-1190) found **no difference** in healing (P = 0.89) or pain (P = 0.56) | Moved to null_result_ids. Scores 5 -> 2; reviews that name analgesic and wound-healing activity remain |
| Chamomile / 15 pairs | Hoffmann (unverifiable since batch 2) and "Chamomile: industrial profiles" (Padula, not locatable) | Removed. The Srivastava review is kept where it names the use; the EU monograph is no longer cited for eczema or infection. Back pain, bruising, eczema and headache dropped |
| Flaxseed / heart, metabolism | Its "RCT" REF-0039 and "clinical" REF-0001 are reviews. The RCT REF-0190 had a DOI that points to a nucleosome paper (it is Pan 2007). A Natural Standard review (REF-2217) says the literature "does not support recommendation for any condition" | Retagged and metadata fixed. REF-2217 recorded as no-effect. FLAX-PAD RCT added (REF-3395: 30 g flaxseed/day, SBP about 10 mmHg lower). Heart 6 -> 5, metabolic 6 -> 8 |
| Lavender / 9 pairs | A genus-level oil review, a genus-level book, and a mechanism study tagged as an RCT | Removed. Insomnia now rests on the EU flower monograph (5 -> 1); eczema, menstrual cramps and muscle spasm dropped |
| Motherwort / 7 pairs | A generic Indian handbook and a genus-level Leonurus review (mostly *L. japonicus*) | Removed. *L. cardiaca* reviews now cover heart, menstrual cramps, sleep, inflammation and skin |
| Shiitake / 5 pairs | Two sources can't be located (lentinan 1996, eritadenine 1989) | Removed; heart and metabolic dropped |

## Medium

- **Horehound.** EU and ESCOP monographs name cough with colds, catarrh, dyspepsia, bloating and
  appetite, not bronchitis. ESCOP was added to its digestive pairs.
- **Yellow loosestrife.** A fatty-liver study was moved from cholesterol and metabolic to liver
  support. The Turkish study (folk use for wounds; anti-inflammatory) was added to wounds and inflammation.
- **Oregon grape.** Psoriasis kept per your decision; its note now says the cream is a 10% extract
  registered as homeopathic. Herbal Reality names arthritis.
- **Retags:** 11 refs (several reviews tagged RCT or clinical).

## For your spot-check (EMA returns 429)

- Lavender flower REF-3071 (sleep); mallow REF-0480 (throat, dry cough; removed from skin);
  horehound REF-0468; chamomile REF-0079.

Validate 0 errors; refs 3200/3200.
