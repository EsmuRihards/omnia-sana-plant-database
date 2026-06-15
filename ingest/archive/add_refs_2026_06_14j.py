#!/usr/bin/env python3
"""Add new references for the 2026-06-14 enrichment batch 10 (final).

Clears most of the remaining two-reference tail:

    Pulmonaria officinalis (Lungwort), Scrophularia nodosa (Figwort),
    Saponaria officinalis (Soapwort), Veronica officinalis (Speedwell),
    Plantago lanceolata (Ribwort Plantain).

New sources from PubMed/PMC are added as REF-0629..REF-0633 and cited from the
relevant actions / constituents in the plant YAML files (edited alongside this
script, provenance in each record's internal_notes).

Two records remain at two references and are documented as deferred: Elymus
repens (Couch Grass) and Rubus fruticosus (Blackberry Leaf). Neither has
species-specific primary literature findable in PubMed beyond the regulatory
monographs / reviews already cited; PubMed hits resolve only to other Rubus
species or are absent, so no honest species-specific source could be added.

Additive and idempotent: each entry is inserted at the correct alphabetical
position by citation key without reordering existing entries.
"""

import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
BIB = os.path.join(HERE, "..", "bibliography.bibtex")

NEW_ENTRIES = {
    "krzyzanowska2017pulmonaria": """@article{krzyzanowska2017pulmonaria,
  author  = {Krzyzanowska-Kowalczyk, J., Kolodziejczyk-Czepas, J., Kowalczyk, M., Pecio, L., Nowak, P. and Stochmal, A.},
  title   = {Yunnaneic Acid B, a Component of Pulmonaria officinalis Extract, Prevents Peroxynitrite-Induced Oxidative Stress in Vitro},
  journal = {Journal of Agricultural and Food Chemistry},
  note    = {REF-0629},
  year    = {2017},
  doi     = {10.1021/acs.jafc.7b00718},
  annote  = {Krzyzanowska-Kowalczyk, J., Kolodziejczyk-Czepas, J., Kowalczyk, M., Pecio, L., Nowak, P. and Stochmal, A. (2017) 'Yunnaneic Acid B, a Component of Pulmonaria officinalis Extract, Prevents Peroxynitrite-Induced Oxidative Stress in Vitro', Journal of Agricultural and Food Chemistry, 65(19), pp. 3827-3834. doi:10.1021/acs.jafc.7b00718.}
}

""",
    "ahmad2012scrophularia": """@article{ahmad2012scrophularia,
  author  = {Ahmad, M., Muhammad, N., Mehjabeen, Jahan, N., Ahmad, M., Obaidullah, Qureshi, M. and Jan, S.U.},
  title   = {Spasmolytic effects of Scrophularia nodosa extract on isolated rabbit intestine},
  journal = {Pakistan Journal of Pharmaceutical Sciences},
  note    = {REF-0630},
  year    = {2012},
  annote  = {Ahmad, M., Muhammad, N., Mehjabeen, Jahan, N., Ahmad, M., Obaidullah, Qureshi, M. and Jan, S.U. (2012) 'Spasmolytic effects of Scrophularia nodosa extract on isolated rabbit intestine', Pakistan Journal of Pharmaceutical Sciences, 25(1), pp. 267-275. [Isolated seven flavonoids; the extract relaxed intestinal smooth muscle, apparently via muscarinic receptors.]}
}

""",
    "jarzebski2020saponaria": """@article{jarzebski2020saponaria,
  author  = {Jarzebski, M., Siejak, P., Smulek, W., Fathordoobady, F., Guo, Y. and others},
  title   = {Plant Extracts Containing Saponins Affects the Stability and Biological Activity of Hempseed Oil Emulsion System},
  journal = {Molecules},
  note    = {REF-0631},
  year    = {2020},
  doi     = {10.3390/molecules25112696},
  annote  = {Jarzebski, M., Siejak, P., Smulek, W., Fathordoobady, F., Guo, Y., et al. (2020) 'Plant Extracts Containing Saponins Affects the Stability and Biological Activity of Hempseed Oil Emulsion System', Molecules, 25(11), 2696. doi:10.3390/molecules25112696. [Demonstrates the surfactant/emulsifying behaviour of Saponaria officinalis saponins - the basis of its "natural soap" use.]}
}

""",
    "grundemann2012veronica": """@article{grundemann2012veronica,
  author  = {Grundemann, C., Garcia-Kaufer, M., Sauer, B., Stangenberg, E., Konczol, M., Merfort, I., Zehl, M. and Huber, R.},
  title   = {Traditionally used Veronica officinalis inhibits proinflammatory mediators via the NF-kB signalling pathway in a human lung cell line},
  journal = {Journal of Ethnopharmacology},
  note    = {REF-0632},
  year    = {2012},
  doi     = {10.1016/j.jep.2012.10.039},
  annote  = {Grundemann, C., Garcia-Kaufer, M., Sauer, B., Stangenberg, E., Konczol, M., Merfort, I., Zehl, M. and Huber, R. (2012) 'Traditionally used Veronica officinalis inhibits proinflammatory mediators via the NF-kB signalling pathway in a human lung cell line', Journal of Ethnopharmacology, 145(1), pp. 118-126. doi:10.1016/j.jep.2012.10.039. [V. officinalis extract inhibited COX-2 and eotaxin in lung epithelial cells; verproside and verminoside were the main iridoids.]}
}

""",
    "vigo2005plantago": """@article{vigo2005plantago,
  author  = {Vigo, E., Cepeda, A., Gualillo, O. and Perez-Fernandez, R.},
  title   = {In-vitro anti-inflammatory activity of Pinus sylvestris and Plantago lanceolata extracts: effect on inducible NOS, COX-1, COX-2 and their products in J774A.1 murine macrophages},
  journal = {Journal of Pharmacy and Pharmacology},
  note    = {REF-0633},
  year    = {2005},
  doi     = {10.1211/0022357055605},
  annote  = {Vigo, E., Cepeda, A., Gualillo, O. and Perez-Fernandez, R. (2005) 'In-vitro anti-inflammatory activity of Pinus sylvestris and Plantago lanceolata extracts: effect on inducible NOS, COX-1, COX-2 and their products in J774A.1 murine macrophages', Journal of Pharmacy and Pharmacology, 57(3), pp. 383-391. doi:10.1211/0022357055605. [Plantago lanceolata extract inhibited nitric oxide production and iNOS expression in macrophages, supporting its traditional respiratory anti-inflammatory use.]}
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
