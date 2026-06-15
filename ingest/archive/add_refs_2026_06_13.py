#!/usr/bin/env python3
"""Add the 2026-06-13 PubMed enrichment references to bibliography.bibtex.

This is the bibliography half of the 2026-06-13 enrichment pass that targeted the
13 least-cited plant records (those carrying a single reference). For each plant,
additional primary studies / systematic reviews were sourced from PubMed and added
here as REF-0536..REF-0558. The matching citations were added to the plant YAML
records (see each record's internal_notes for the per-plant provenance line).

Idempotent: entries whose citation key already exists are skipped. The full entry
list is re-sorted alphabetically by citation key (case-insensitive), preserving the
existing REF-XXXX ids, exactly as the other ingestion tools do.
"""
import re
import sys
from pathlib import Path

BIB = Path(__file__).resolve().parent.parent / "bibliography.bibtex"

NEW_ENTRIES = r"""
@article{okawara2013diosgenin,
  author  = {Okawara, M. and Tokudome, Y. and Todo, H. and Sugibayashi, K. and Hashimoto, F.},
  title   = {Enhancement of diosgenin distribution in the skin by cyclodextrin complexation following oral administration},
  journal = {Biological & Pharmaceutical Bulletin},
  note    = {REF-0536},
  year    = {2013},
  doi     = {10.1248/bpb.b12-00467},
  annote  = {Okawara, M., Tokudome, Y., Todo, H., Sugibayashi, K. and Hashimoto, F. (2013) Enhancement of diosgenin distribution in the skin by cyclodextrin complexation following oral administration. Biological & Pharmaceutical Bulletin, 36(1), pp. 36-40. doi:10.1248/bpb.b12-00467.}
}

@article{badgujar2014fennel,
  author  = {Badgujar, S.B. and Patel, V.V. and Bandivdekar, A.H.},
  title   = {Foeniculum vulgare Mill: a review of its botany, phytochemistry, pharmacology, contemporary application, and toxicology},
  journal = {BioMed Research International},
  note    = {REF-0537},
  year    = {2014},
  doi     = {10.1155/2014/842674},
  annote  = {Badgujar, S.B., Patel, V.V. and Bandivdekar, A.H. (2014) Foeniculum vulgare Mill: a review of its botany, phytochemistry, pharmacology, contemporary application, and toxicology. BioMed Research International, 2014, 842674. doi:10.1155/2014/842674.}
}

@article{gao2016inula,
  author  = {Gao, S. and Wang, Q. and Tian, X.H. and Li, H.L. and Shen, Y.H. and Xu, X.K. and Wu, G.Z. and Hu, Z.L. and Zhang, W.D.},
  title   = {Total sesquiterpene lactones prepared from Inula helenium L. has potentials in prevention and therapy of rheumatoid arthritis},
  journal = {Journal of Ethnopharmacology},
  note    = {REF-0538},
  year    = {2016},
  doi     = {10.1016/j.jep.2016.12.020},
  annote  = {Gao, S., Wang, Q., Tian, X.H., Li, H.L., Shen, Y.H., Xu, X.K., Wu, G.Z., Hu, Z.L. and Zhang, W.D. (2016) Total sesquiterpene lactones prepared from Inula helenium L. has potentials in prevention and therapy of rheumatoid arthritis. Journal of Ethnopharmacology, 196, pp. 39-46. doi:10.1016/j.jep.2016.12.020.}
}

@article{stojanovic2012antistaphylococcal,
  author  = {Stojanovic-Radic, Z. and Comic, Lj. and Radulovic, N. and Blagojevic, P. and Denic, M. and Miltojevic, A. and Rajkovic, J. and Mihajilov-Krstev, T.},
  title   = {Antistaphylococcal activity of Inula helenium L. root essential oil: eudesmane sesquiterpene lactones induce cell membrane damage},
  journal = {European Journal of Clinical Microbiology & Infectious Diseases},
  note    = {REF-0539},
  year    = {2012},
  doi     = {10.1007/s10096-011-1400-1},
  annote  = {Stojanovic-Radic, Z., Comic, Lj., Radulovic, N., Blagojevic, P., Denic, M., Miltojevic, A., Rajkovic, J. and Mihajilov-Krstev, T. (2012) Antistaphylococcal activity of Inula helenium L. root essential oil: eudesmane sesquiterpene lactones induce cell membrane damage. European Journal of Clinical Microbiology & Infectious Diseases, 31(6), pp. 1015-1025. doi:10.1007/s10096-011-1400-1.}
}

@article{cantrell1999antimycobacterial,
  author  = {Cantrell, C.L. and Abate, L. and Fronczek, F.R. and Franzblau, S.G. and Quijano, L. and Fischer, N.H.},
  title   = {Antimycobacterial eudesmanolides from Inula helenium and Rudbeckia subtomentosa},
  journal = {Planta Medica},
  note    = {REF-0540},
  year    = {1999},
  doi     = {10.1055/s-1999-14001},
  annote  = {Cantrell, C.L., Abate, L., Fronczek, F.R., Franzblau, S.G., Quijano, L. and Fischer, N.H. (1999) Antimycobacterial eudesmanolides from Inula helenium and Rudbeckia subtomentosa. Planta Medica, 65(4), pp. 351-355. doi:10.1055/s-1999-14001.}
}

@article{paul2024malva,
  author  = {Paul, Z.A. and Malla, A.T. and Dar, M.A. and Masoodi, M.H.},
  title   = {Phytochemistry and Pharmacological Activity of Malva sylvestris L.: A Detailed Insight},
  journal = {Combinatorial Chemistry & High Throughput Screening},
  note    = {REF-0541},
  year    = {2024},
  doi     = {10.2174/0113862073269336231009110313},
  annote  = {Paul, Z.A., Malla, A.T., Dar, M.A. and Masoodi, M.H. (2024) Phytochemistry and Pharmacological Activity of Malva sylvestris L.: A Detailed Insight. Combinatorial Chemistry & High Throughput Screening, 27(16), pp. 2309-2322. doi:10.2174/0113862073269336231009110313.}
}

@article{batiha2022malva,
  author  = {Batiha, G.E. and Tene, S.T. and Teibo, J.O. and Shaheen, H.M. and Oluwatoba, O.S. and Teibo, T.K.A. and Al-Kuraishy, H.M. and Al-Garbee, A.I. and Alexiou, A. and Papadakis, M.},
  title   = {The phytochemical profiling, pharmacological activities, and safety of Malva sylvestris: a review},
  journal = {Naunyn-Schmiedeberg's Archives of Pharmacology},
  note    = {REF-0542},
  year    = {2022},
  doi     = {10.1007/s00210-022-02329-w},
  annote  = {Batiha, G.E., Tene, S.T., Teibo, J.O., Shaheen, H.M., Oluwatoba, O.S., Teibo, T.K.A., Al-Kuraishy, H.M., Al-Garbee, A.I., Alexiou, A. and Papadakis, M. (2022) The phytochemical profiling, pharmacological activities, and safety of Malva sylvestris: a review. Naunyn-Schmiedeberg's Archives of Pharmacology, 396(3), pp. 421-440. doi:10.1007/s00210-022-02329-w.}
}

@article{grossmann2000petasites,
  author  = {Grossmann, M. and Schmidramsl, H.},
  title   = {An extract of Petasites hybridus is effective in the prophylaxis of migraine},
  journal = {International Journal of Clinical Pharmacology and Therapeutics},
  note    = {REF-0543},
  year    = {2000},
  doi     = {10.5414/cpp38430},
  annote  = {Grossmann, M. and Schmidramsl, H. (2000) An extract of Petasites hybridus is effective in the prophylaxis of migraine. International Journal of Clinical Pharmacology and Therapeutics, 38(9), pp. 430-435. doi:10.5414/cpp38430.}
}

@article{guo2007herbal,
  author  = {Guo, R. and Pittler, M.H. and Ernst, E.},
  title   = {Herbal medicines for the treatment of allergic rhinitis: a systematic review},
  journal = {Annals of Allergy, Asthma & Immunology},
  note    = {REF-0544},
  year    = {2007},
  doi     = {10.1016/S1081-1206(10)60375-4},
  annote  = {Guo, R., Pittler, M.H. and Ernst, E. (2007) Herbal medicines for the treatment of allergic rhinitis: a systematic review. Annals of Allergy, Asthma & Immunology, 99(6), pp. 483-495. doi:10.1016/S1081-1206(10)60375-4.}
}

@article{kreydiyyeh2002diuretic,
  author  = {Kreydiyyeh, S.I. and Usta, J.},
  title   = {Diuretic effect and mechanism of action of parsley},
  journal = {Journal of Ethnopharmacology},
  note    = {REF-0545},
  year    = {2002},
  doi     = {10.1016/s0378-8741(01)00408-1},
  annote  = {Kreydiyyeh, S.I. and Usta, J. (2002) Diuretic effect and mechanism of action of parsley. Journal of Ethnopharmacology, 79(3), pp. 353-357. doi:10.1016/s0378-8741(01)00408-1.}
}

@article{mahmood2014parsley,
  author  = {Mahmood, S. and Hussain, S. and Malik, F.},
  title   = {Critique of medicinal conspicuousness of Parsley (Petroselinum crispum): a culinary herb of Mediterranean region},
  journal = {Pakistan Journal of Pharmaceutical Sciences},
  note    = {REF-0546},
  year    = {2014},
  annote  = {Mahmood, S., Hussain, S. and Malik, F. (2014) Critique of medicinal conspicuousness of Parsley (Petroselinum crispum): a culinary herb of Mediterranean region. Pakistan Journal of Pharmaceutical Sciences, 27(1), pp. 193-202. PMID:24374449.}
}

@article{wilt2002pygeum,
  author  = {Wilt, T. and Ishani, A. and Mac Donald, R. and Rutks, I. and Stark, G.},
  title   = {Pygeum africanum for benign prostatic hyperplasia},
  journal = {Cochrane Database of Systematic Reviews},
  note    = {REF-0547},
  year    = {2002},
  doi     = {10.1002/14651858.CD001044},
  annote  = {Wilt, T., Ishani, A., Mac Donald, R., Rutks, I. and Stark, G. (2002) Pygeum africanum for benign prostatic hyperplasia. Cochrane Database of Systematic Reviews, (1), CD001044. doi:10.1002/14651858.CD001044.}
}

@article{dedhia2008phytotherapy,
  author  = {Dedhia, R.C. and McVary, K.T.},
  title   = {Phytotherapy for lower urinary tract symptoms secondary to benign prostatic hyperplasia},
  journal = {The Journal of Urology},
  note    = {REF-0548},
  year    = {2008},
  doi     = {10.1016/j.juro.2008.01.094},
  annote  = {Dedhia, R.C. and McVary, K.T. (2008) Phytotherapy for lower urinary tract symptoms secondary to benign prostatic hyperplasia. The Journal of Urology, 179(6), pp. 2119-2125. doi:10.1016/j.juro.2008.01.094.}
}

@article{krzyzanowska2018pulmonaria,
  author  = {Krzyzanowska-Kowalczyk, J. and Pecio, L. and Moldoch, J. and Ludwiczuk, A. and Kowalczyk, M.},
  title   = {Novel Phenolic Constituents of Pulmonaria officinalis L. LC-MS/MS Comparison of Spring and Autumn Metabolite Profiles},
  journal = {Molecules},
  note    = {REF-0549},
  year    = {2018},
  doi     = {10.3390/molecules23092277},
  annote  = {Krzyzanowska-Kowalczyk, J., Pecio, L., Moldoch, J., Ludwiczuk, A. and Kowalczyk, M. (2018) Novel Phenolic Constituents of Pulmonaria officinalis L. LC-MS/MS Comparison of Spring and Autumn Metabolite Profiles. Molecules, 23(9), 2277. doi:10.3390/molecules23092277.}
}

@article{gao2008skullcap,
  author  = {Gao, J. and Sanchez-Medina, A. and Pendry, B.A. and Hughes, M.J. and Webb, G.P. and Corcoran, O.},
  title   = {Validation of a HPLC method for flavonoid biomarkers in skullcap (Scutellaria) and its use to illustrate wide variability in the quality of commercial tinctures},
  journal = {Journal of Pharmacy & Pharmaceutical Sciences},
  note    = {REF-0550},
  year    = {2008},
  doi     = {10.18433/j39g6v},
  annote  = {Gao, J., Sanchez-Medina, A., Pendry, B.A., Hughes, M.J., Webb, G.P. and Corcoran, O. (2008) Validation of a HPLC method for flavonoid biomarkers in skullcap (Scutellaria) and its use to illustrate wide variability in the quality of commercial tinctures. Journal of Pharmacy & Pharmaceutical Sciences, 11(1), pp. 77-87. doi:10.18433/j39g6v.}
}

@article{brock2014skullcap,
  author  = {Brock, C. and Whitehouse, J. and Tewfik, I. and Towell, T.},
  title   = {American Skullcap (Scutellaria lateriflora): a randomised, double-blind placebo-controlled crossover study of its effects on mood in healthy volunteers},
  journal = {Phytotherapy Research},
  note    = {REF-0551},
  year    = {2014},
  doi     = {10.1002/ptr.5044},
  annote  = {Brock, C., Whitehouse, J., Tewfik, I. and Towell, T. (2014) American Skullcap (Scutellaria lateriflora): a randomised, double-blind placebo-controlled crossover study of its effects on mood in healthy volunteers. Phytotherapy Research, 28(5), pp. 692-698. doi:10.1002/ptr.5044.}
}

@article{tassorelli2005parthenolide,
  author  = {Tassorelli, C. and Greco, R. and Morazzoni, P. and Riva, A. and Sandrini, G. and Nappi, G.},
  title   = {Parthenolide is the component of Tanacetum parthenium that inhibits nitroglycerin-induced Fos activation: studies in an animal model of migraine},
  journal = {Cephalalgia},
  note    = {REF-0552},
  year    = {2005},
  doi     = {10.1111/j.1468-2982.2005.00915.x},
  annote  = {Tassorelli, C., Greco, R., Morazzoni, P., Riva, A., Sandrini, G. and Nappi, G. (2005) Parthenolide is the component of Tanacetum parthenium that inhibits nitroglycerin-induced Fos activation: studies in an animal model of migraine. Cephalalgia, 25(8), pp. 612-621. doi:10.1111/j.1468-2982.2005.00915.x.}
}

@article{majdi2011parthenolide,
  author  = {Majdi, M. and Liu, Q. and Karimzadeh, G. and Malboobi, M.A. and Beekwilder, J. and Cankar, K. and de Vos, R. and Todorovic, S. and Simonovic, A. and Bouwmeester, H.},
  title   = {Biosynthesis and localization of parthenolide in glandular trichomes of feverfew (Tanacetum parthenium L. Schulz Bip.)},
  journal = {Phytochemistry},
  note    = {REF-0553},
  year    = {2011},
  doi     = {10.1016/j.phytochem.2011.04.021},
  annote  = {Majdi, M., Liu, Q., Karimzadeh, G., Malboobi, M.A., Beekwilder, J., Cankar, K., de Vos, R., Todorovic, S., Simonovic, A. and Bouwmeester, H. (2011) Biosynthesis and localization of parthenolide in glandular trichomes of feverfew (Tanacetum parthenium L. Schulz Bip.). Phytochemistry, 72(14-15), pp. 1739-1750. doi:10.1016/j.phytochem.2011.04.021.}
}

@article{guller2021linden,
  author  = {Guller, U. and Guller, P. and Ciftci, M.},
  title   = {Radical Scavenging and Antiacetylcholinesterase Activities of Ethanolic Extracts of Carob, Clove, and Linden},
  journal = {Alternative Therapies in Health and Medicine},
  note    = {REF-0554},
  year    = {2021},
  annote  = {Guller, U., Guller, P. and Ciftci, M. (2021) Radical Scavenging and Antiacetylcholinesterase Activities of Ethanolic Extracts of Carob, Clove, and Linden (linden flowers = Tilia cordata). Alternative Therapies in Health and Medicine, 27(5), pp. 33-37. PMID:32619207.}
}

@article{nogueron2015tilia,
  author  = {Nogueron-Merino, M.C. and Jimenez-Ferrer, E. and Roman-Ramos, R. and Zamilpa, A. and Tortoriello, J. and Herrera-Ruiz, M.},
  title   = {Interactions of a standardized flavonoid fraction from Tilia americana with Serotoninergic drugs in elevated plus maze},
  journal = {Journal of Ethnopharmacology},
  note    = {REF-0555},
  year    = {2015},
  doi     = {10.1016/j.jep.2015.01.029},
  annote  = {Nogueron-Merino, M.C., Jimenez-Ferrer, E., Roman-Ramos, R., Zamilpa, A., Tortoriello, J. and Herrera-Ruiz, M. (2015) Interactions of a standardized flavonoid fraction from Tilia americana with Serotoninergic drugs in elevated plus maze. Journal of Ethnopharmacology, 164, pp. 319-327. doi:10.1016/j.jep.2015.01.029. (Related species Tilia americana; genus-level mechanistic support for the calming/anxiolytic action of Tilia flavonoids such as tiliroside.)}
}

@article{svangard2004cyclotides,
  author  = {Svangard, E. and Goransson, U. and Hocaoglu, Z. and Gullbo, J. and Larsson, R. and Claeson, P. and Bohlin, L.},
  title   = {Cytotoxic cyclotides from Viola tricolor},
  journal = {Journal of Natural Products},
  note    = {REF-0556},
  year    = {2004},
  doi     = {10.1021/np030101l},
  annote  = {Svangard, E., Goransson, U., Hocaoglu, Z., Gullbo, J., Larsson, R., Claeson, P. and Bohlin, L. (2004) Cytotoxic cyclotides from Viola tricolor. Journal of Natural Products, 67(2), pp. 144-147. doi:10.1021/np030101l.}
}

@article{velazquez2005zeamays,
  author  = {Velazquez, D.V.O. and Xavier, H.S. and Batista, J.E.M. and de Castro-Chaves, C.},
  title   = {Zea mays L. extracts modify glomerular function and potassium urinary excretion in conscious rats},
  journal = {Phytomedicine},
  note    = {REF-0557},
  year    = {2005},
  doi     = {10.1016/j.phymed.2003.12.010},
  annote  = {Velazquez, D.V.O., Xavier, H.S., Batista, J.E.M. and de Castro-Chaves, C. (2005) Zea mays L. extracts modify glomerular function and potassium urinary excretion in conscious rats. Phytomedicine, 12(5), pp. 363-369. doi:10.1016/j.phymed.2003.12.010.}
}

@article{caixeta2025cornsilk,
  author  = {Caixeta, G.A.B. and dos Santos Reis, D. and Soares, K.I. and de Brito Ramos, I. and Mendes, G.H.L. and others},
  title   = {Toxicological Assessment of a Standardized Dry Extract of Zea mays L. (Poaceae) Stigmas During Gestation: Effects on Maternal Parameters and Fetal Outcomes in Wistar Rats},
  journal = {Birth Defects Research},
  note    = {REF-0558},
  year    = {2025},
  doi     = {10.1002/bdr2.2526},
  annote  = {Caixeta, G.A.B., dos Santos Reis, D., Soares, K.I., de Brito Ramos, I., Mendes, G.H.L., et al. (2025) Toxicological Assessment of a Standardized Dry Extract of Zea mays L. (Poaceae) Stigmas During Gestation: Effects on Maternal Parameters and Fetal Outcomes in Wistar Rats. Birth Defects Research, 117(9), e2526. doi:10.1002/bdr2.2526.}
}
"""


def parse_existing(text: str):
    """Return (header, [(key_lower, exact_entry_text), ...]).

    Entries are located by the byte offset of each line that starts with
    '@article{' (the only place that token appears at column 0). Each entry's
    text is the exact slice up to the next entry start, then stripped of
    surrounding blank lines. This never reconstructs content, so nothing is lost.
    """
    matches = list(re.finditer(r"(?m)^@article\{([^,]+),", text))
    starts = [m.start() for m in matches] + [len(text)]
    header = text[: starts[0]].rstrip("\n")
    entries = []
    for i, m in enumerate(matches):
        seg = text[starts[i] : starts[i + 1]].strip()
        entries.append((m.group(1).lower(), seg))
    return header, entries


def parse_new(block_text: str):
    out = []
    for m in re.finditer(r"(?ms)^@article\{([^,]+),.*?^\}", block_text):
        out.append((m.group(1).lower(), m.group(0).strip()))
    return out


def main():
    raw = BIB.read_text(encoding="utf-8")
    header, existing = parse_existing(raw)
    existing_keys = {k for k, _ in existing}

    added, skipped = [], []
    for k, t in parse_new(NEW_ENTRIES):
        if k in existing_keys:
            skipped.append(k)
        else:
            added.append((k, t))

    combined = existing + added
    combined.sort(key=lambda kt: kt[0])  # case-insensitive keys already lowered

    BIB.write_text(header + "\n\n" + "\n\n".join(t for _, t in combined) + "\n",
                   encoding="utf-8")

    print(f"existing entries: {len(existing)}")
    print(f"added: {len(added)} -> {[k for k, _ in added]}")
    if skipped:
        print(f"skipped (already present): {skipped}")
    print(f"total entries now: {len(combined)}")


if __name__ == "__main__":
    sys.exit(main())
