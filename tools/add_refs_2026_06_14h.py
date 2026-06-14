#!/usr/bin/env python3
"""Add new references for the 2026-06-14 enrichment batch 8.

Targets five more records that carried only two references each:

    Epilobium parviflorum (Willowherb), Centaurium erythraea (Centaury),
    Aloysia citrodora (Lemon Verbena), Stachys officinalis (Wood Betony),
    Lactuca virosa (Wild Lettuce).

(Rubus fruticosus / Blackberry Leaf was also considered but deferred: the
species-specific PubMed reviews available were for other Rubus species
(R. chingii, R. geoides), and its existing review + antioxidant-study baseline
already covers it.)

New sources from PubMed/PMC are added as REF-0618..REF-0622 and cited from the
relevant actions / constituents in the plant YAML files (edited alongside this
script, provenance in each record's internal_notes).

Additive and idempotent: each entry is inserted at the correct alphabetical
position by citation key without reordering existing entries.
"""

import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
BIB = os.path.join(HERE, "..", "bibliography.bibtex")

NEW_ENTRIES = {
    "granica2014epilobium": """@article{granica2014epilobium,
  author  = {Granica, S., Piwowarski, J.P., Czerwinska, M.E. and Kiss, A.K.},
  title   = {Phytochemistry, pharmacology and traditional uses of different Epilobium species (Onagraceae): a review},
  journal = {Journal of Ethnopharmacology},
  note    = {REF-0618},
  year    = {2014},
  doi     = {10.1016/j.jep.2014.08.036},
  annote  = {Granica, S., Piwowarski, J.P., Czerwinska, M.E. and Kiss, A.K. (2014) 'Phytochemistry, pharmacology and traditional uses of different Epilobium species (Onagraceae): a review', Journal of Ethnopharmacology, 156, pp. 316-346. doi:10.1016/j.jep.2014.08.036.}
}

""",
    "elmenyiy2021centaurium": """@article{elmenyiy2021centaurium,
  author  = {El Menyiy, N., Guaouguaou, F.E., El Baaboua, A., El Omari, N., Taha, D. and others},
  title   = {Phytochemical properties, biological activities and medicinal use of Centaurium erythraea Rafn},
  journal = {Journal of Ethnopharmacology},
  note    = {REF-0619},
  year    = {2021},
  doi     = {10.1016/j.jep.2021.114171},
  annote  = {El Menyiy, N., Guaouguaou, F.E., El Baaboua, A., El Omari, N., Taha, D., et al. (2021) 'Phytochemical properties, biological activities and medicinal use of Centaurium erythraea Rafn.', Journal of Ethnopharmacology, 276, 114171. doi:10.1016/j.jep.2021.114171.}
}

""",
    "buchwald2018lemonverbena": """@article{buchwald2018lemonverbena,
  author  = {Buchwald-Werner, S., Naka, I., Wilhelm, M., Schutz, E., Schoen, C. and Reule, C.},
  title   = {Effects of lemon verbena extract (Recoverben) supplementation on muscle strength and recovery after exhaustive exercise: a randomized, placebo-controlled trial},
  journal = {Journal of the International Society of Sports Nutrition},
  note    = {REF-0620},
  year    = {2018},
  doi     = {10.1186/s12970-018-0208-0},
  annote  = {Buchwald-Werner, S., Naka, I., Wilhelm, M., Schutz, E., Schoen, C. and Reule, C. (2018) 'Effects of lemon verbena extract (Recoverben) supplementation on muscle strength and recovery after exhaustive exercise: a randomized, placebo-controlled trial', Journal of the International Society of Sports Nutrition, 15, 5. doi:10.1186/s12970-018-0208-0.}
}

""",
    "matkowski2006lamiaceae": """@article{matkowski2006lamiaceae,
  author  = {Matkowski, A. and Piotrowska, M.},
  title   = {Antioxidant and free radical scavenging activities of some medicinal plants from the Lamiaceae},
  journal = {Fitoterapia},
  note    = {REF-0621},
  year    = {2006},
  doi     = {10.1016/j.fitote.2006.04.004},
  annote  = {Matkowski, A. and Piotrowska, M. (2006) 'Antioxidant and free radical scavenging activities of some medicinal plants from the Lamiaceae', Fitoterapia, 77(5), pp. 346-353. doi:10.1016/j.fitote.2006.04.004. [Stachys officinalis was among the strongest antioxidant species tested.]}
}

""",
    "wesolowska2006lactucin": """@article{wesolowska2006lactucin,
  author  = {Wesolowska, A., Nikiforuk, A., Michalska, K., Kisiel, W. and Chojnacka-Wojcik, E.},
  title   = {Analgesic and sedative activities of lactucin and some lactucin-like guaianolides in mice},
  journal = {Journal of Ethnopharmacology},
  note    = {REF-0622},
  year    = {2006},
  doi     = {10.1016/j.jep.2006.03.003},
  annote  = {Wesolowska, A., Nikiforuk, A., Michalska, K., Kisiel, W. and Chojnacka-Wojcik, E. (2006) 'Analgesic and sedative activities of lactucin and some lactucin-like guaianolides in mice', Journal of Ethnopharmacology, 107(2), pp. 254-258. doi:10.1016/j.jep.2006.03.003. [Lactucin and lactucopicrin, characteristic of Lactuca virosa, showed analgesia comparable to ibuprofen and sedative activity.]}
}

""",
}


def citation_key(entry_text):
    m = re.match(r"@\w+\{([^,]+),", entry_text)
    return m.group(1) if m else ""


def main():
    with open(BIB, encoding="utf-8") as fh:
        text = fh.read()

    parts = re.split(r"(?m)^(?=@)", text)
    preamble, entries = parts[0], parts[1:]
    keys = [citation_key(e) for e in entries]
    existing_notes = set(re.findall(r"REF-\d+", text))

    added = 0
    for key in sorted(NEW_ENTRIES):
        block = NEW_ENTRIES[key]
        ref_id = re.search(r"REF-\d+", block).group(0)
        if ref_id in existing_notes or key in keys:
            continue
        pos = len(entries)
        for i, k in enumerate(keys):
            if k > key:
                pos = i
                break
        entries.insert(pos, block)
        keys.insert(pos, key)
        existing_notes.add(ref_id)
        added += 1

    with open(BIB, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(preamble + "".join(entries))

    print(f"Added {added} new reference(s); bibliography now has {len(entries)} entries.")


if __name__ == "__main__":
    main()
