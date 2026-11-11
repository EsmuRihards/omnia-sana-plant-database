# Symptom-tool audit - batch 7 of 19 (2026-11-11) - FIXED

Plants 61-70: eschscholzia-californica, eucalyptus-globulus, euphrasia-officinalis,
filipendula-ulmaria, filipendula-vulgaris, foeniculum-vulgare, galium-album (no indications),
galium-aparine, ganoderma-lingzhi, gentiana-lutea. 86 pairs, 41 direct sources.

Owner decision this batch (added to DATA_PRINCIPLES invariant 11): **"Ganoderma lucidum" in
reishi/lingzhi literature counts for G. lingzhi**, the species that name was long misapplied to.

Result: 132 changes; site-wide pairs 1,433 -> 1,411; 4 refs deleted, 1 added. Log: `batch07_changes.tsv`.

## High

| Plant / symptom | Problem | Fix |
|---|---|---|
| California poppy / anxiety, nervous tension, stress (5) | The only RCT (REF-0606) tested a **fixed combination** with hawthorn and magnesium | Purged. Scores 5 -> 2. EU monograph (mental stress, sleep) added |
| Eyebright / eye strain | Both clinical sources used Weleda/Wala **Euphrasia D3** eye drops (homeopathic potency); the RCT's primary outcome was also null (p = 0.85). The EMA concluded no monograph was possible: efficacy undocumented, home eye washes not safe | Both purged. EMA statement recorded as no-effect |
| Fennel / menstrual cramps (9) | Cochrane REF-2586 found "no consistent evidence" for fennel (MD -0.34, CI -0.74 to 0.06) | Moved to null_result_ids. Score 9 -> 8; the fennel-specific meta-analysis stays |
| Reishi / cancer | Cochrane 2012 (REF-0125) was superseded by the 2016 update | Replaced by REF-3394 (same conclusion: adjunct use). Also added to immune support. Cancer 2 -> 7 |
| Reishi / 7 pairs | The chapter REF-0298 names blood glucose, immunity, liver and bacteriostasis only. REF-0019's title, journal and volume were wrong (it is Bao 2002, Phytochemistry) | Removed from 7 pairs; metadata fixed. Arthritis, heart, insomnia and skin dropped |
| Meadowsweet / 15 pairs | "The Herbal Remedy Handbook" (Bridge 2008) is unverifiable. Grieve names only diarrhoea, stomach, strangury, dropsy and fevers | Removed. Grieve kept for urinary support and swelling. EU monograph (minor joint pain) added to arthritis and pain |
| Cleavers / 8 pairs | Only sources were BHP 1983 (not online) and Hoffmann (unverifiable since batch 2) | Removed; 6 pairs dropped. Wounds and infection now rest on the in vitro wound study and the 1883 BMJ ulcer note |

## Medium

- **Eucalyptus.** WHO vol. 2 was cited for 8 pairs; it was kept for cold and respiratory support
  only. The oil review names no cold or wounds. The EU leaf monograph (cough with colds) was added.
- **Eyebright.** The Herbal Reality page names allergies, catarrh, asthma, colds, eye problems,
  inflammation and infection. It was removed from arthritis, cough, diarrhoea, fever, skin and wounds.
- **Dropwort.** The rat pain study was cited for arthritis, the ulcer study for indigestion, the
  antimicrobial studies for wounds and the brain-energy study for cognition; all were removed.
- **Fennel.** Its review was removed from bronchitis, cough and wounds. The EU monograph (menstrual
  spasm, cough with colds) was added.
- **Gentian.** A genus-level Gentiana review was removed. The EU monograph names appetite and
  dyspepsia, not bloating.
- **Retags:** 7 refs. Metadata and abstracts were added to 3.

## For your spot-check (bot-blocked, kept per your batch-5 decision)

- **WHO vol. 2, Eucalyptus** (REF-0309): cold, respiratory support.
- **Reishi chapter** (REF-0298, NCBI Bookshelf behind reCAPTCHA): kept on what its abstract names.
- **EU monographs (EMA returns 429):** California poppy REF-3099 (stress, sleep); eucalyptus leaf
  REF-3083 (cold, respiratory); meadowsweet REF-3072 (arthritis, pain); bitter fennel REF-3080
  (menstrual cramps, cough, respiratory); gentian REF-0453 (appetite, indigestion).
- **Unreadable, removed:** BHP 1983 (cleavers). If you have a copy, its Galium indications
  could restore urinary and skin pairs.

Validate 0 errors; refs 3208/3208.
