#!/usr/bin/env python3
"""
migrate_phase4_compounds.py — architecture migration, Phase 4.

Generates the compound entities (compounds/<id>.yaml) for the bioactive classes
and notable named compounds that appear across the plant constituents. Each
carries `synonyms` = the free-text match-keywords; the Phase 5 plant rewrite reads
these to link constituents -> compound ids (constituents keep their original
free-text `name`, so nothing is lost).

Idempotent: re-running overwrites the generated entities with the same content.
Usage:  python ingest/migrate_phase4_compounds.py
"""
import os, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "compounds")

# (id, display name, class, [match keywords / synonyms])
COMPOUNDS = [
    # ---- classes ----
    ("flavonoid", "Flavonoids", "flavonoid", ["flavonoid", "flavonoids", "flavonol", "flavone", "flavanone"]),
    ("anthocyanin", "Anthocyanins", "flavonoid", ["anthocyanin", "anthocyanins"]),
    ("proanthocyanidin", "Proanthocyanidins", "flavonoid", ["proanthocyanidin", "proanthocyanidins", "oligomeric proanthocyanidin"]),
    ("catechin", "Catechins", "flavonoid", ["catechin", "catechins", "epigallocatechin", "epicatechin"]),
    ("phenolic-acid", "Phenolic acids", "phenolic", ["phenolic acid", "phenolic acids"]),
    ("phenolic-compound", "Phenolic compounds", "phenolic", ["phenolic compound", "phenolic compounds", "polyphenol", "polyphenols", "phenolics"]),
    ("tannin", "Tannins", "phenolic", ["tannin", "tannins", "ellagitannin", "ellagitannins", "gallotannin"]),
    ("coumarin", "Coumarins", "phenolic", ["coumarin", "coumarins", "furanocoumarin", "furanocoumarins"]),
    ("lignan", "Lignans", "lignan", ["lignan", "lignans"]),
    ("anthraquinone", "Anthraquinones", "phenolic", ["anthraquinone", "anthraquinones", "sennoside", "sennosides"]),
    ("terpene", "Terpenes / terpenoids", "terpene", ["terpene", "terpenes", "terpenoid", "terpenoids", "monoterpene", "monoterpenes", "diterpene", "diterpenes", "triterpene", "triterpenes"]),
    ("sesquiterpene", "Sesquiterpenes", "terpene", ["sesquiterpene", "sesquiterpenes"]),
    ("sesquiterpene-lactone", "Sesquiterpene lactones", "terpene", ["sesquiterpene lactone", "sesquiterpene lactones"]),
    ("essential-oil", "Essential (volatile) oil", "volatile-oil", ["essential oil", "volatile oil", "volatile (volatile) oil", "essential (volatile) oil"]),
    ("carotenoid", "Carotenoids", "terpene", ["carotenoid", "carotenoids", "beta-carotene", "lycopene"]),
    ("glycoside", "Glycosides", "glycoside", ["glycoside", "glycosides"]),
    ("iridoid-glycoside", "Iridoid glycosides", "glycoside", ["iridoid", "iridoids", "iridoid glycoside", "iridoid glycosides"]),
    ("saponin", "Saponins", "saponin", ["saponin", "saponins"]),
    ("triterpene-saponin", "Triterpene saponins", "saponin", ["triterpene saponin", "triterpene saponins", "triterpene glycoside", "triterpene glycosides"]),
    ("alkaloid", "Alkaloids", "alkaloid", ["alkaloid", "alkaloids"]),
    ("phytosterol", "Phytosterols", "sterol", ["phytosterol", "phytosterols", "sterol", "sterols", "beta-sitosterol", "sitosterol"]),
    ("polysaccharide", "Polysaccharides", "polysaccharide", ["polysaccharide", "polysaccharides", "fructan", "fructans", "glucan", "glucans", "arabinogalactan", "rhamnogalacturonan"]),
    ("mucilage", "Mucilage", "polysaccharide", ["mucilage", "mucilages"]),
    ("inulin", "Inulin", "polysaccharide", ["inulin"]),
    ("pectin", "Pectin", "polysaccharide", ["pectin"]),
    ("starch", "Starch", "polysaccharide", ["starch"]),
    ("organosulfur", "Organosulfur compounds", "organosulfur", ["organosulfur", "organosulphur"]),
    # ---- named compounds ----
    ("rosmarinic-acid", "Rosmarinic acid", "phenolic", ["rosmarinic"]),
    ("chlorogenic-acid", "Chlorogenic acid", "phenolic", ["chlorogenic", "caffeoylquinic"]),
    ("caffeic-acid", "Caffeic acid", "phenolic", ["caffeic"]),
    ("ferulic-acid", "Ferulic acid", "phenolic", ["ferulic"]),
    ("gallic-acid", "Gallic acid", "phenolic", ["gallic"]),
    ("ellagic-acid", "Ellagic acid", "phenolic", ["ellagic"]),
    ("luteolin", "Luteolin", "flavonoid", ["luteolin"]),
    ("apigenin", "Apigenin", "flavonoid", ["apigenin"]),
    ("quercetin", "Quercetin", "flavonoid", ["quercetin"]),
    ("rutin", "Rutin", "flavonoid", ["rutin"]),
    ("kaempferol", "Kaempferol", "flavonoid", ["kaempferol"]),
    ("silymarin", "Silymarin (silybin)", "flavonoid", ["silymarin", "silybin", "silibinin"]),
    ("allicin", "Allicin / organosulfur thiosulfinates", "organosulfur", ["allicin", "ajoene", "s-allyl-cysteine", "alliin"]),
    ("berberine", "Berberine", "alkaloid", ["berberine"]),
    ("thymol", "Thymol", "terpene", ["thymol"]),
    ("carvacrol", "Carvacrol", "terpene", ["carvacrol"]),
    ("menthol", "Menthol", "terpene", ["menthol"]),
    ("eugenol", "Eugenol", "phenolic", ["eugenol"]),
    ("cineole", "1,8-Cineole (eucalyptol)", "terpene", ["cineole", "eucalyptol"]),
    ("camphor", "Camphor", "terpene", ["camphor"]),
    ("bisabolol", "Alpha-bisabolol", "terpene", ["bisabolol"]),
    ("chamazulene", "Chamazulene", "terpene", ["chamazulene"]),
    ("linalool", "Linalool", "terpene", ["linalool"]),
    ("citral", "Citral (neral / geranial)", "terpene", ["citral", "neral", "geranial"]),
    ("curcumin", "Curcumin", "phenolic", ["curcumin"]),
    ("gingerol", "Gingerols / shogaols", "phenolic", ["gingerol", "gingerols", "shogaol", "shogaols"]),
    ("parthenolide", "Parthenolide", "terpene", ["parthenolide"]),
    ("valerenic-acid", "Valerenic acid", "terpene", ["valerenic"]),
    ("hypericin", "Hypericin", "phenolic", ["hypericin"]),
    ("hyperforin", "Hyperforin", "phenolic", ["hyperforin"]),
    ("withanolide", "Withanolides", "terpene", ["withanolide", "withanolides"]),
    ("ginsenoside", "Ginsenosides / eleutherosides", "saponin", ["ginsenoside", "ginsenosides", "eleutheroside", "eleutherosides"]),
    ("glycyrrhizin", "Glycyrrhizin", "saponin", ["glycyrrhizin", "glycyrrhizic"]),
    ("escin", "Escin (aescin)", "saponin", ["escin", "aescin"]),
    ("asarone", "Asarones (alpha-/beta-asarone)", "phenolic", ["asarone", "asarones"]),
    ("boswellic-acid", "Boswellic acids", "terpene", ["boswellic"]),
    ("harpagoside", "Harpagoside", "glycoside", ["harpagoside"]),
    ("verbascoside", "Verbascoside (acteoside)", "phenolic", ["verbascoside", "acteoside"]),
    ("arctigenin", "Arctigenin / arctiin", "lignan", ["arctigenin", "arctiin"]),
    ("allantoin", "Allantoin", "other", ["allantoin"]),
    ("silica", "Silica", "mineral", ["silica"]),
    ("gla", "Gamma-linolenic acid (GLA)", "fatty-acid", ["gamma-linolenic", "linolenic acid"]),
]


def main():
    os.makedirs(OUT, exist_ok=True)
    ids = set()
    for cid, name, klass, syns in COMPOUNDS:
        assert cid not in ids, "duplicate compound id: " + cid
        ids.add(cid)
        rec = {"id": cid, "name": name, "class": klass, "synonyms": sorted(set(syns))}
        with open(os.path.join(OUT, cid + ".yaml"), "w", encoding="utf-8") as fh:
            yaml.safe_dump(rec, fh, allow_unicode=True, sort_keys=False)
    print("Wrote %d compound entities to compounds/" % len(COMPOUNDS))


if __name__ == "__main__":
    main()
