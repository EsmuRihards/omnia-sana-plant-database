# Cancer Research Enrichment — Progress Tracker

Deeper, multi-source anticancer-literature pass across all 187 plants. This supersedes the
first (title-only, already-cited-refs) pass that added the `cancer` condition to 82 plants.
Each plant here is re-examined with real literature search (PubMed, Europe PMC, Consensus,
ClinicalTrials.gov, ChEMBL, web) using scientific + common names.

Quality bar: ACCEPT only studies genuinely about *this* plant's (or a clearly-justified close
synonym's) anticancer/antitumor/antiproliferative/chemopreventive activity, title AND abstract
supporting it. REJECT supportive-care, benign conditions (e.g. BPH), pure tox/epidemiology,
throwaway-mention reviews, and nanoparticle-synthesis (herb = reducing agent only) studies.
"reviewed — no genuine fit found" is a correct, honest outcome, not a gap.

Status values: `done-enriched` | `done-no-fit` | `needs-deeper-look` | `pending`

| plant_id | status | citations_added | date | notes |
|----------|--------|-----------------|------|-------|
| achillea_millefolium | done-enriched | 3 (REF-0369 reused, REF-2821, REF-2822) | 2026-07-14 | NEW cancer entry (missed by pass 1). Csupor-Löffler 2009 primary: yarrow flavonoids/sesquiterpenoids (centaureidin, casticin) antiproliferative on HeLa/MCF-7/A431; + genus Achillea anticancer review + A. millefolium pharmacognosy review. Rejected: A. conferta/falcata/clavennae (other species), brine-shrimp tox, radiodermatitis supportive-care, doxorubicin-nephroprotection. |
| acorus_calamus | done-enriched | 5 new (REF-2823..2827; +existing REF-2280) = 6 total | 2026-07-14 | Strengthened pass-1 entry. A. calamus extract vs gastric cancer (AGS, anti-angiogenic) + β-asarone (major constituent) apoptosis/anti-invasion in gastric, bladder, esophageal cancer + chemosensitization. Rejected: AgNP green-synthesis, chemo-neuropathy supportive-care, asarone genotoxicity/tox reviews. |
| actaea_racemosa | done-enriched | 4 (REF-2828..2831) | 2026-07-14 | NEW cancer entry (created actions key too — none existed). Actein/black-cohosh extract inhibit MCF-7/MDA-MB-231 breast + colon + HepG2 liver cancer cells, chemo-synergy (Einbond, Rice). Rejected: hot-flash supportive-care review, actein genotoxicity, phytoestrogen/menopause studies, C. foetida actein-derivative synthesis. |
| aegopodium_podagraria | done-no-fit | 0 | 2026-07-14 | Reviewed — no genuine anticancer fit. Only hits: goutweed antioxidant vs fluoride-oxidative-stress (THP-1), Apiaceae antiaging/cosmetic, and a Po-210/Pb-210 radiotoxicity cancer-RISK assessment. No antitumor/antiproliferative literature exists for this species. |
| aesculus_hippocastanum | done-enriched | 4 new (REF-2832..2835; +existing REF-0471/0675) = 6 total | 2026-07-14 | Strengthened pass-1 entry (which cited only the escin review, twice). Added escin primaries: β-escin+5-FU synergy MCF-7 breast, escin HCC (PD-L1/anti-PD-1, in vivo), escin+sorafenib lung (in vivo), escin pancreatic NF-κB chemosensitization. Rejected: CuO-TiO2-chitosan-escin nanocomposite (activity = nanocomposite), triterpenoid melanoma review (escin one of many). |
