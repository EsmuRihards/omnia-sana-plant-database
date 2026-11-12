# Symptom-tool audit - batch 13 of 19 (2026-11-12) - FIXED (deep pass)

Plants 121-130: pimpinella-anisum, pinus-sylvestris, piper-methysticum, plantago-lanceolata,
plantago-major, pleurotus-ostreatus, potentilla-erecta, primula-veris, prunella-vulgaris,
prunus-africana. 81 pairs.

The owner asked for a deeper pass this time. On top of "does the source name the symptom", each
pair was checked for:
- mechanistic plausibility;
- safety versus claims;
- species and plant-part confusion;
- missing landmark and null trials;
- claim-note accuracy.

**New owner policy (DATA_PRINCIPLES inv. 11).** A mechanistic-only pair is dropped when:
- the plant's own evidence contradicts the mechanism; or
- the action evidence concerns an unrelated target.

Generic anti-inflammatory or antioxidant inferences stay, labelled.

**Result:**
- 155 changes; batch pairs 81 -> 68; site-wide 1,340 -> 1,327.
- 6 refs added (REF-3397..3402); 9 deleted or merged.
- Logs: `batch13_changes.tsv`, `batch13_followup_changes.tsv`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| Pygeum / prostate, urinary | Keehn & Lowe 2015 ("no evidence that phytotherapy significantly improves symptoms of BPH against placebo"; names Pygeum) was **cited as support** | Recorded as no-effect on both. The Cochrane 2002 review (still current) remains |
| Oyster mushroom / blood sugar, metabolic, heart | The only source was an edible-mushroom review that never names a species | Purged. The Dicks 2020 systematic review of 8 *P. ostreatus* trials (lower glucose and lipids; low-quality evidence) added |
| Oyster mushroom / cold, immunity | Rested on one narrative review; the two placebo-controlled pleuran RCTs were missing | Added Bergendiova 2011 (athletes) and Jesenak 2013 (children; both arms got vitamin C, so the effect is pleuran's) |
| Kava / anxiety | The largest trial (Sarris 2020, 16 weeks, 171 patients) was missing: **no benefit** in GAD, and more liver-test abnormalities on kava. The earlier positive GAD trial (Sarris 2013) was also missing. The 2000 meta-analysis was superseded by the same authors' Cochrane review. REF-2463 was the trial *protocol*, not the results | Both trials added; 2020 recorded as no-effect. 2000 MA merged into Cochrane. REF-2463 repointed to the KADSS results paper. Claim note now states the mixed result |
| Greater plantain / 7 pairs | "WHO Monographs" 2002 (vol. 2) has **no Plantago major monograph**: its table of contents goes from kava (p.231) to pygeum (p.246) | Purged |
| Self-heal | "Yang 2007" antiviral paper and cowslip's "Wicke 2007" can't be found in PubMed, OpenAlex or Crossref. PV-1 is a multi-herb mixture | All three purged |
| Self-heal / immune support | Four of 8 sources show immune **suppression** (colitis, thyroiditis Th1/Th17, TLR blocking) | Removed; one innate-immunity study remains |
| Scots pine | A general essential-oil review naming no pine was cited on 12 pairs. The one pine wound/anti-inflammatory study found **no effect** for *P. sylvestris* oil. An inhalation study found the oil *raised* inflammatory markers | Review purged; null recorded for inflammation; the pro-inflammatory study hidden from inflammation. Bronchitis, cough, UTI, swelling and wounds dropped |

## Deeper checks

**Mechanistic plausibility (new policy).** Three inferred pairs were dropped:

| Plant / symptom | Why the inference fails |
|---|---|
| Tormentil / arthritis | Contradicted: the UC trial found its tannins are not absorbed into the blood |
| Self-heal / cold | Off-target: its antiviral evidence is herpes and HIV lab work |
| Scots pine / wounds | Off-target: oil tested against gonorrhoea bacteria and a yeast |

These inferred pairs stay (generic anti-inflammatory evidence): anise, oyster mushroom, pygeum,
greater plantain arthritis, self-heal skin, ribwort bruising, tormentil wounds, kava stress.

**Species and plant-part confusion.**
- Ribwort: an aucubin review naming *P. asiatica* was purged, as was a Balkan review that never
  names ribwort.
- Herbal Reality: one page covers both plantains and gives sore throat to ribwort only. It was
  removed from greater plantain's sore throat and added to ribwort's.
- Constipation: no psyllium (*P. ovata*) confusion. The pair now rests on a Persian-medicine
  review that names *P. major*.
- Greater plantain cardiovascular: rests on plantamajoside (its signature compound), labelled.
  One of the two papers attributes the compound to *P. asiatica*.

**Null trials found.** Greater plantain's oral-mucositis RCT (no better than bicarbonate) was
being used as evidence for its "demulcent" action. It is now recorded as no-effect for
inflammation.

**Measured outcome ≠ claimed outcome.**
- Tormentil: a mouse study where only a four-ingredient mix eased diarrhoea.
- Tormentil: two dental-biofilm studies cited for sore throat.
- Oyster mushroom: an immune-profile study cited for cancer.
- Kava: anxiety trials cited for stress, tension and insomnia; insomnia dropped.

**Commentary replaced by its trial.** Tormentil/IBD cited a commentary. It now cites the trial
itself: Huber 2007, open-label, 16 patients, disease activity fell.

**Safety versus claims.**
- No plant is listed for the organ its own warning covers.
- Kava's liver warning is reinforced by the 2020 trial; the warning itself is unchanged.

**Claim notes.** 37 notes rewritten:
- Many pairs with direct sources said "inferred from X action". They now describe their real
  evidence.
- Pine notes now credit Grieve's traditional uses.
- The pygeum inflammation note was fixed in a follow-up.

## Evidence gaps (owner follow-ups, not new claims)

- **Anise:** the EU monograph uses (bloating, flatulence, cough with colds) have no pairs.
- **Cowslip:** no cough pair and no expectorant action, though EMA and ESCOP 2021 both name
  "cough associated with cold".
  - Its plant-page traditional-uses text cites the ivy/primrose/thyme SR. That SR says "studies
    on primrose were lacking".
- **Scots pine:** Commission E-type uses of pine-needle oil (catarrh, rheumatic pain) are
  unsourced here, so bronchitis and cough were dropped.
- **Kava, pygeum:** WHO vol. 2 does have monographs on both. Neither plant cites them (WHO
  bot-blocks).
- **REF-3010** (greater plantain): the journal's own published abstract reads like a copy of
  earlier reviews, not its in-vitro title. Left as a mechanistic card.

## For your spot-check (EMA returns 429)

- Tormentil EU monograph REF-0520: diarrhoea, minor oral-mucosa inflammation, sore throat.
- Ribwort EU monograph REF-0499: oral/pharyngeal irritation, dry cough.
- Cowslip EU monograph REF-0075: cough with colds.

Validate 0 errors; refs 3196/3196.
