# Truncated abstracts - repair and null-result screen (2026-11-10)

Side task of the symptom-tool audit. The `abstract` field of bibliography entries had been
cut at every literal "<": the July 2026 abstract fetch stripped Europe PMC's HTML with a
regex of the `<[^>]+>` kind, so "P < 0.05)." ate everything up to the `>` of the next
`<h4>` heading. Typical leftovers were "(P Conclusion", "p Discussion", "( P P P".

**Result: 163 abstracts repaired, 51,598 characters of real abstract text restored. No
"<"-truncated abstract was left unrepaired.** Only `abstract` fields were changed (163 lines
of `bibliography.bibtex`); no DOI, PMID, title, study_type or plant data was touched.

## Method

1. Fetched the Europe PMC record (`resultType=core`) for every entry with a DOI or PMID
   (2,535 IDs, 2,496 found), and title-searched the 142 entries with neither. In all,
   2,513 of the 2,612 stored abstracts could be compared against their source text.
2. **Proof of truncation, per entry:** re-ran the buggy regex on the fetched HTML. An entry
   counts as truncated only if that reproduces the stored abstract *exactly* (whitespace
   aside) and a correct tag regex gives a different text. That identity test also proves the
   fetched record is the same paper, which is why the 8 entries matched by title or by a
   corrected ID are safe.
3. Restored text = the same pipeline with a correct tag regex (a tag must start with a
   letter after `<`), HTML entities unescaped, `{`/`}` to `(`/`)`, whitespace collapsed. So
   the new abstract differs from the old one only by the restored spans. "<" is plain text.
4. **PubMed cross-check:** fetched every one of the 163 from PubMed efetch. Every restored
   span appears verbatim in the PubMed abstract, and 162 of 163 abstracts match PubMed word
   for word (the 163rd differs only by PubMed's "UNLABELLED" header, REF-2542).
5. Read the conclusion of all 163 restored abstracts for no-effect results (below).

Coverage: the issue heuristic found 114 entries; all 114 were real. The bug replay found
**49 more** it missed (lost "< 0.001; I²" heterogeneity figures, "< 80 years" inclusion
criteria, "< 133 umol/L" subgroups, a lost "but not for improving Qmax", and so on). 99
abstracts have no Europe PMC source; a broader gap-pattern scan of those found nothing.

## Flag: no-effect conclusions (move to `null_result_ids`, owner to apply)

Per DATA_PRINCIPLES v1.4 invariant 7. Not changed here (this session touched only abstracts).

| Ref | Paper | What the abstract concludes | Pairs that cite it as support | Other citers |
|---|---|---|---|---|
| REF-1895 | Serenoa repens RCT, 12 weeks, BPH | "no significant beneficial effect of this S. repens extract over placebo" | **serenoa-repens / prostate-support, urinary-support** (`reference_ids`) | references |
| REF-0584 | Cochrane: artichoke leaf extract for hypercholesterolaemia | potential to lower cholesterol, "but the evidence is, as yet, not convincing" | **cynara-scolymus / high-cholesterol, cardiovascular-support** (`reference_ids`) | actions |
| REF-0586 | Cochrane: Astragalus for chronic kidney disease | "definitive conclusions could not be made based on available evidence" | **astragalus-membranaceus / kidney-support** (`reference_ids`) | actions |
| REF-1844 | SR: Hibiscus sabdariffa for hypertension | trials "do not provide reliable evidence to support recommending" it | none directly; feeds the `antihypertensive` action, so it reaches **hibiscus-sabdariffa / high-blood-pressure** mechanistically | actions, references |
| REF-0858 | RCT: lavender oil inhalation, postmenopausal insomnia | primary outcome: "no significant differences were observed between groups" | none directly; candidate for **lavandula-angustifolia / insomnia** | references |

Borderline (owner call): **REF-1869 and REF-1870** (Cochrane, Pelargonium sidoides for acute
respiratory infections). Both say it "may be effective" for rhinosinusitis and the common
cold "but doubt exists", with low or very low quality evidence; more positive for acute
bronchitis. No direct pairs; both feed pelargonium-sidoides' `antiviral` action, so they
reach the bronchitis / cold / sinusitis pairs mechanistically.

Already handled in batch 2: REF-0700 (uva-ursi vs fosfomycin) is in `null_result_ids` for
infection, urinary-support and UTI. REF-1391 (dill RCT) is null for inflammation; its
restored results support the metabolic-support and cardiovascular-support pairs it is cited for.

### Mixed results - positive conclusion, but one arm or outcome was null

No move needed unless a pair names the null outcome. Listed so batch audits can check:

| Ref | Plant / cited pairs | Null part |
|---|---|---|
| REF-0295, REF-0635 | zingiber-officinale / nausea, indigestion | no effect on vomiting (nausea positive) |
| REF-1479 | petasites-hybridus / migraine, headache | 50 mg bid not better than placebo (75 mg positive) |
| REF-2002 | crocus-sativus / depression | 22 mg/day no effect (28 mg positive) |
| REF-2584 | psilocybe-cubensis / depression | 10 mg not significant (25 mg positive) |
| REF-1585 | trametes-versicolor / cancer | NSCLC symptoms did not improve (slower deterioration) |
| REF-0666 | cinnamomum-verum / cardiovascular-support | no effect on LDL-C or HDL-C |
| REF-0572 | serenoa-repens / prostate-, urinary-support | combination with tamsulosin not better for Qmax |
| REF-1331, REF-2456, REF-2502 | (no direct pairs) nettle, aloe, saffron | no effect on HbA1c / insulin / HOMA-IR |

## Noticed in passing - not fixed (out of scope)

- **19 hand-abridged abstracts.** Not "<" cuts: sentences were dropped or merged, so the
  stored "abstract" is not the published text. REF-2903, REF-3000, REF-3104 to REF-3120.
  REF-3104 (flax oil, paediatric bipolar) is itself a **null trial** ("no significant
  differences in primary outcome measures") and lost its results section. Same fix
  applies (replace with the Europe PMC/PubMed text), but it was outside this task.
- **Not-a-source rules (batch-2 owner decisions) hit by directly cited refs:**
  REF-0881 is a **homeopathic** retrospective study ("Arnica 50 M ... Ledum 50 M" pads)
  cited for rhododendron-tomentosum / swelling. Multi-herb products cited directly:
  REF-2588 (4-herb nutraceutical) for oenothera-biennis / hot-flashes, menopause;
  REF-0404 (ProstateEZE Max) for epilobium-parviflorum; REF-0593 (thyme + ivy) for
  thymus-vulgaris; REF-1577 (feverfew + willow, Mig-RL) for tanacetum-parthenium.
- **IDs worth backfilling** (left alone; abstract-only scope): REF-0006 has no DOI/PMID
  (PMID 20854384, doi 10.1111/j.1464-5491.2010.03079.x); REF-0158's DOI carries a stray
  `/full` suffix (real doi 10.3389/fnut.2025.1618108, PMID 41608519); title-matched with no
  ID field: REF-0723 (28348972), REF-2348 (22894890), REF-1604 (31182888), REF-1805
  (32523876), REF-1602 (27516984), REF-1180 (18072463).
- REF-0878 now contains PubMed's literal "<or=4.5%" (verbatim). Any renderer that puts
  abstracts into `innerHTML` unescaped would read "<or=..." as a tag; esc_html output is safe.

## Appendix - all 163 repaired entries

| Ref | PMID | Found by | Chars restored | Cited by (plant) |
|---|---|---|---|---|
| REF-0006 | 20854384 | heuristic, corrected ID | 778 | cinnamomum-verum |
| REF-0059 | 24201300 | bug replay only | 750 | coffea-arabica |
| REF-0114 | 30285042 | heuristic | 816 | oxycoccus-palustris |
| REF-0158 | 41608519 | heuristic, corrected ID | 193 | cuminum-cyminum |
| REF-0204 | 26764326 | bug replay only | 595 | allium-sativum |
| REF-0205 | 10819950 | heuristic | 516 | coffea-arabica |
| REF-0283 | 11498727 | heuristic | 101 | bacopa-monnieri |
| REF-0288 | 15897583 | heuristic | 182 | linum-usitatissimum |
| REF-0295 | 24642205 | heuristic | 382 | zingiber-officinale |
| REF-0321 | 19678785 | heuristic | 282 | taraxacum-officinale |
| REF-0374 | 26238568 | heuristic | 26 | achillea-millefolium |
| REF-0404 | 23642948 | heuristic | 427 | epilobium-parviflorum |
| REF-0422 | 32680575 | heuristic | 318 | boswellia-serrata |
| REF-0528 | 23889998 | heuristic | 640 | dioscorea-villosa |
| REF-0543 | 11020030 | heuristic | 106 | petasites-hybridus |
| REF-0563 | 18499602 | heuristic | 175 | passiflora-incarnata |
| REF-0571 | 29694707 | heuristic | 422 | serenoa-repens |
| REF-0572 | 28723522 | bug replay only | 390 | serenoa-repens |
| REF-0584 | 23543518 | heuristic | 79 | cynara-scolymus |
| REF-0586 | 25335553 | bug replay only | 1241 | astragalus-membranaceus |
| REF-0592 | 10936472 | heuristic | 271 | salix-alba |
| REF-0593 | 17063641 | heuristic | 610 | thymus-vulgaris |
| REF-0600 | 38752050 | heuristic | 495 | oenothera-biennis |
| REF-0602 | 12913771 | heuristic | 290 | potentilla-erecta |
| REF-0604 | 34187122 | bug replay only | 30 | foeniculum-vulgare |
| REF-0608 | 29641247 | heuristic | 10 | capsella-bursa-pastoris |
| REF-0615 | 41368330 | bug replay only | 11 | angelica-archangelica |
| REF-0616 | 28066246 | bug replay only | 914 | verbena-officinalis |
| REF-0634 | 37699474 | bug replay only | 19 | zingiber-officinale |
| REF-0635 | 31937153 | heuristic | 40 | zingiber-officinale |
| REF-0638 | 40806131 | heuristic | 532 | zingiber-officinale |
| REF-0658 | 26558156 | heuristic | 1127 | prunella-vulgaris |
| REF-0666 | 28887086 | heuristic | 856 | cinnamomum-verum |
| REF-0670 | 33021111 | heuristic | 119 | actaea-racemosa |
| REF-0677 | 22094055 | heuristic | 215 | aesculus-hippocastanum |
| REF-0699 | 34792008 | bug replay only | 569 | angelica-archangelica |
| REF-0700 | 34111592 | heuristic | 385 | arctostaphylos-uva-ursi |
| REF-0723 | 28348972 | heuristic, title match | 355 | arctium-minus |
| REF-0774 | 33628288 | heuristic | 691 | cnicus-benedictus |
| REF-0784 | 38504617 | heuristic | 486 | crataegus-laevigata |
| REF-0835 | 25837191 | heuristic | 96 | hedera-helix |
| REF-0842 | 28064110 | heuristic | 381 | hypericum-perforatum |
| REF-0857 | 37325306 | bug replay only | 147 | lavandula-angustifolia |
| REF-0858 | 33905827 | heuristic | 289 | lavandula-angustifolia |
| REF-0878 | 16297921 | bug replay only | 84 | primula-veris |
| REF-0881 | 26863038 | bug replay only | 432 | rhododendron-tomentosum |
| REF-0905 | 35280571 | bug replay only | 419 | stellaria-media |
| REF-0920 | 38489175 | heuristic | 162 | marrubium-vulgare |
| REF-0940 | 38469711 | bug replay only | 72 | oxycoccus-palustris |
| REF-0956 | 28632199 | heuristic | 57 | paullinia-cupana |
| REF-0980 | 35281919 | bug replay only | 171 | reynoutria-japonica |
| REF-1023 | 37049862 | bug replay only | 39 | sambucus-nigra |
| REF-1039 | 30843769 | heuristic | 310 | scrophularia-nodosa |
| REF-1122 | 33019940 | heuristic | 534 | trigonella-foenum-graecum |
| REF-1131 | 34103042 | heuristic | 304 | verbascum-thapsus |
| REF-1147 | 28392894 | heuristic | 32 | viola-odorata |
| REF-1150 | 32073874 | heuristic | 140 | viola-odorata |
| REF-1151 | 25763239 | heuristic | 144 | viola-odorata |
| REF-1156 | 31808709 | heuristic | 61 | matricaria-chamomilla |
| REF-1180 | 18072463 | bug replay only, title match | 74 | mahonia-aquifolium |
| REF-1187 | 28886527 | heuristic | 555 | malva-sylvestris |
| REF-1195 | 38575930 | bug replay only | 546 | melissa-officinalis |
| REF-1208 | 11766133 | bug replay only | 683 | mentha-piperita |
| REF-1223 | 38420828 | bug replay only | 143 | origanum-majorana |
| REF-1227 | 25662759 | heuristic | 363 | origanum-majorana |
| REF-1277 | 34641301 | heuristic | 321 | salvia-officinalis |
| REF-1331 | 31802554 | bug replay only | 10 | urtica-dioica |
| REF-1340 | 29046404 | bug replay only | 89 | vaccinium-macrocarpon |
| REF-1347 | 38214795 | heuristic | 236 | vaccinium-macrocarpon |
| REF-1348 | 37899385 | heuristic | 705 | valeriana-officinalis |
| REF-1352 | 33936782 | heuristic | 68 | valeriana-officinalis |
| REF-1358 | 32483479 | heuristic | 290 | verbena-officinalis |
| REF-1371 | 37576045 | heuristic | 165 | althaea-officinalis |
| REF-1391 | 32503652 | heuristic | 692 | anethum-graveolens |
| REF-1408 | 31600102 | heuristic | 135 | pimpinella-anisum |
| REF-1410 | 27860049 | heuristic | 83 | pimpinella-anisum |
| REF-1411 | 36903462 | bug replay only | 360 | pimpinella-anisum |
| REF-1412 | 32145331 | heuristic | 240 | pimpinella-anisum |
| REF-1427 | 36185698 | heuristic | 10 | ocimum-tenuiflorum |
| REF-1452 | 32864206 | bug replay only | 80 | origanum-vulgare |
| REF-1479 | 15623680 | heuristic | 259 | petasites-hybridus |
| REF-1564 | 38542772 | bug replay only | 226 | scutellaria-lateriflora |
| REF-1577 | 17163262 | heuristic | 664 | tanacetum-parthenium |
| REF-1585 | 12814145 | heuristic | 325 | trametes-versicolor |
| REF-1602 | 27516984 | heuristic, title match | 291 | viola-tricolor |
| REF-1604 | 31182888 | heuristic, title match | 516 | viola-tricolor |
| REF-1622 | 14748896 | heuristic | 36 | andrographis-paniculata |
| REF-1657 | 40784268 | bug replay only | 181 | foeniculum-vulgare |
| REF-1683 | 32213118 | heuristic | 9 | laurus-nobilis |
| REF-1685 | 33520200 | bug replay only | 209 | laurus-nobilis |
| REF-1708 | 34177406 | heuristic | 751 | coriandrum-sativum |
| REF-1713 | 25243870 | heuristic | 399 | crataegus-monogyna |
| REF-1727 | 30810975 | bug replay only | 624 | humulus-lupulus |
| REF-1728 | 30919241 | heuristic | 879 | humulus-lupulus |
| REF-1732 | 28742505 | bug replay only | 103 | humulus-lupulus |
| REF-1757 | 31970022 | heuristic | 486 | lamium-album |
| REF-1760 | 35044254 | heuristic | 271 | plantago-major |
| REF-1768 | 30988999 | heuristic | 71 | plantago-major |
| REF-1785 | 25880053 | heuristic | 8 | crataegus-laevigata |
| REF-1801 | 31694395 | heuristic | 82 | hyssopus-officinalis |
| REF-1805 | 32523876 | bug replay only, title match | 176 | hyssopus-officinalis |
| REF-1816 | 32565872 | heuristic | 846 | boswellia-serrata |
| REF-1817 | 36416059 | heuristic | 448 | boswellia-serrata |
| REF-1844 | 19801187 | bug replay only | 45 | hibiscus-sabdariffa |
| REF-1869 | 18646148 | heuristic | 55 | pelargonium-sidoides |
| REF-1870 | 24146345 | heuristic | 55 | pelargonium-sidoides |
| REF-1889 | 32274957 | heuristic | 95 | serenoa-repens |
| REF-1894 | 15049985 | heuristic | 201 | serenoa-repens |
| REF-1895 | 12887481 | bug replay only | 362 | serenoa-repens |
| REF-1941 | 38040876 | heuristic | 454 | artemisia-vulgaris |
| REF-1950 | 32984407 | bug replay only | 665 | borago-officinalis |
| REF-1978 | 36978458 | bug replay only | 14 | carum-carvi |
| REF-1979 | 26407909 | heuristic | 177 | carum-carvi |
| REF-1987 | 34199316 | bug replay only | 34 | carum-carvi |
| REF-2001 | 24299602 | heuristic | 386 | crocus-sativus |
| REF-2002 | 28735826 | heuristic | 63 | crocus-sativus |
| REF-2003 | 30741567 | bug replay only | 48 | crocus-sativus |
| REF-2030 | 27721054 | heuristic | 379 | filipendula-ulmaria |
| REF-2107 | 24252493 | heuristic | 84 | bacopa-monnieri |
| REF-2125 | 36632430 | heuristic | 144 | calendula-officinalis |
| REF-2153 | 36698182 | bug replay only | 246 | cordyceps-militaris |
| REF-2186 | 26223956 | heuristic | 30 | ginkgo-biloba |
| REF-2192 | 31226797 | heuristic | 220 | glycyrrhiza-glabra |
| REF-2221 | 38992480 | bug replay only | 350 | linum-usitatissimum |
| REF-2248 | 31517876 | heuristic | 239 | withania-somnifera |
| REF-2252 | 26609282 | heuristic | 629 | withania-somnifera |
| REF-2254 | 33600918 | heuristic | 522 | withania-somnifera |
| REF-2259 | 33204391 | bug replay only | 85 | astragalus-membranaceus |
| REF-2296 | 33108713 | heuristic | 539 | eleutherococcus-senticosus |
| REF-2310 | 34482524 | bug replay only | 131 | hedera-helix |
| REF-2348 | 22894890 | heuristic, title match | 553 | matricaria-chamomilla |
| REF-2350 | 26437613 | heuristic | 300 | matricaria-chamomilla |
| REF-2382 | 34715299 | heuristic | 207 | coffea-arabica |
| REF-2404 | 37079159 | heuristic | 230 | aesculus-hippocastanum |
| REF-2442 | 18254076 | heuristic | 835 | crataegus-laevigata, crataegus-monogyna |
| REF-2456 | 27009750 | heuristic | 390 | aloe-vera |
| REF-2472 | 28829155 | heuristic | 422 | withania-somnifera |
| REF-2477 | 10761967 | heuristic | 377 | panax-ginseng |
| REF-2480 | 28864749 | bug replay only | 568 | schisandra-chinensis |
| REF-2485 | 34899340 | bug replay only | 74 | curcuma-longa, nigella-sativa, olea-europaea |
| REF-2496 | 25484177 | bug replay only | 197 | crocus-sativus |
| REF-2502 | 38559777 | heuristic | 90 | crocus-sativus |
| REF-2505 | 20197017 | heuristic | 287 | schisandra-chinensis |
| REF-2507 | 39519602 | bug replay only | 148 | glycyrrhiza-glabra |
| REF-2509 | 38246526 | heuristic | 346 | glycyrrhiza-glabra |
| REF-2513 | 37341696 | bug replay only | 103 | nigella-sativa |
| REF-2516 | 29154069 | heuristic | 662 | nigella-sativa, trigonella-foenum-graecum |
| REF-2521 | 14616430 | heuristic | 618 | hypericum-perforatum |
| REF-2525 | 33514002 | heuristic | 9 | curcuma-longa |
| REF-2527 | 25875025 | heuristic | 215 | hibiscus-sabdariffa |
| REF-2539 | 29908682 | heuristic | 9 | lavandula-angustifolia, melissa-officinalis |
| REF-2540 | 34467577 | bug replay only | 55 | gymnema-sylvestre |
| REF-2542 | 39064727 | heuristic | 457 | gymnema-sylvestre |
| REF-2568 | 35763310 | bug replay only | 492 | cynara-scolymus |
| REF-2583 | 38692686 | heuristic | 741 | psilocybe-cubensis |
| REF-2584 | 36322843 | heuristic | 432 | psilocybe-cubensis |
| REF-2588 | 33331798 | heuristic | 460 | oenothera-biennis |
| REF-2594 | 32801033 | heuristic | 80 | potentilla-erecta |
| REF-2636 | 21375515 | bug replay only | 96 | stellaria-media |
| REF-2713 | 23627465 | heuristic | 586 | daucus-carota |
| REF-2716 | 26835241 | heuristic | 578 | daucus-carota |
| REF-2718 | 41471394 | heuristic | 635 | daucus-carota |
| REF-2995 | 12856861 | bug replay only | 68 | plantago-major |
