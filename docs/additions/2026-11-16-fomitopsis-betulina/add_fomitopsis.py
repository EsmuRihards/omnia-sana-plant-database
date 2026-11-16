"""Add Fomitopsis betulina (birch polypore) to the Omnia Sana database: bibliography entries + plant record.

Run once from the repo root:  python docs/additions/2026-11-16-fomitopsis-betulina/add_fomitopsis.py
All-or-nothing: the bibliography is restored if writing the plant record fails.
Sources: PubMed records cached by docs/audits/2026-11-10-symptom-audit/deep_efetch.py (verbatim abstracts),
non-PubMed metadata in nonpubmed_sources.json (Crossref + OpenAlex), web pages read 2026-11-16.
Model: anthropic/claude-opus-5-5
"""
import json, os, re, sys, unicodedata
import yaml

ROOT = os.getcwd()
HERE = os.path.dirname(os.path.abspath(__file__))
BIB = os.path.join(ROOT, 'bibliography.bibtex')
PLANT = os.path.join(ROOT, 'plants', 'fomitopsis_betulina.yaml')
CACHE = json.load(open(os.path.join(ROOT, 'docs/audits/2026-11-10-symptom-audit/deep/abstracts.json'), encoding='utf-8'))
NONPM = json.load(open(os.path.join(HERE, 'nonpubmed_sources.json'), encoding='utf-8'))
TODAY = '2026-11-16'
FIRST_REF = 3881


def clean(s):
    return re.sub(r'\s+', ' ', (s or '').replace('{', '(').replace('}', ')')).strip()


def asc(s):
    return re.sub(r'[^a-z]', '', unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower())


SMALL = {'of', 'and', 'the', 'in', 'on', 'for', 'a', 'an', 'to', 'with', 'de', 'des', 'et', 'la', 'le', 'y', 'du'}


def journal(j):
    j = re.sub(r'\s*\(.*?\)\s*', ' ', j).split(' : ')[0].strip()
    return ' '.join(w if (k and w.lower() in SMALL) else (w[:1].upper() + w[1:]) for k, w in enumerate(j.split()))


def authors_pm(au):
    return au[0] if len(au) == 1 else ', '.join(au[:-1]) + ' and ' + au[-1]


def authors_cr(au):
    def initials(gv):
        parts = [g for g in re.split(r'[\s-]+', gv or '') if g]
        return '.'.join(g[0] for g in parts) + '.' if parts else ''
    names = [f'{f}, {initials(gv)}'.strip(', ') for f, gv in au if f]
    return names[0] if len(names) == 1 else ', '.join(names[:-1]) + ' and ' + names[-1]


# ---------------------------------------------------------------------------------------------------------------
# Source list. (slug, kind, id, study_type, summary)
#   kind pm      = PubMed record with verbatim abstract (cache)
#   kind pm0     = PubMed record without an abstract (title-only; summary says so)
#   kind oa      = DOI work outside PubMed, verbatim abstract from OpenAlex, metadata from Crossref
#   kind oa0     = DOI work outside PubMed, abstract omitted (mutilated or unavailable)
#   kind web     = web page read 2026-11-16
# ---------------------------------------------------------------------------------------------------------------
S = [
 # --- reviews / syntheses ---
 ('pleszczynska2017', 'pm', '28378220', 'narrative-review',
  'Narrative review of F. betulina (formerly Piptoporus betulinus); full text read (PMC5380686). Source for taxonomy (transfer to Fomitopsis by Han et al. 2016, MycoBank 812646), morphology, habitat (birch only; saprotroph, occasionally parasite), folk uses (infusion in Russia, Baltic countries, Hungary, Romania for nutritional and calming properties; tea against cancers, as immune-enhancing and anti-parasitic agent and for gastrointestinal disorders; fresh fruiting-body dressings on wounds as antiseptic and anti-bleeding; dried powder as a painkiller), constituents (triterpenoids, betulin, betulinic acid, lupeol, ergosterol peroxide, tocopherols, ascorbic acid, alpha- and beta-glucans; alpha-glucan up to 44-53% of cell-wall dry weight) and piptamine activity (MIC 0.78-12.5 ug/ml Gram-positive bacteria; 6.25 ug/ml Candida albicans). States that in vivo and clinical verification is still required.'),
 ('nowotarska2024sr', 'pm', '39512529', 'systematic-review',
  'PRISMA systematic review (PubMed, Google Scholar, Web of Science to July 2024; 450 screened, 5 included; full text read, PMC11538974) of in vitro cytotoxicity of F. betulina extracts on cancer and normal cells: selective cytotoxicity against cancer cells, strongest in prostate cancer and melanoma lines. Pools cell-culture studies only. Full text: "So far, there are no clinical studies confirming the efficacy and safety of Fomitopsis betulina in humans."'),
 ('li2024', 'pm', '39330376', 'narrative-review',
  'Narrative review of F. betulina secondary metabolites (over 100 compounds), cultivation and terpene-synthase genomics; full text read (PMC11432923). Cited for folk use (Russian folklore: tea from the fruiting bodies to alleviate fatigue and enhance immune function; use against cancer in Siberia, the Baltic states and Finland) and edibility of juvenile stages. Its abstract mentions anti-malarial effects but the body gives no anti-malarial data, so that claim is not used.'),
 ('grienke2014', 'pm', '24786572', 'narrative-review',
  'Narrative review of five central European medicinal polypores including Piptoporus betulinus (traditional uses, phytochemistry, bioactivity). Species section not read (paywalled), so it backs no specific claim here; kept as a general source.'),
 ('nerlich2021', 'pm', '34240239', 'narrative-review',
  'Review of 30 years of research on the Iceman: he had a Trichuris trichiura worm infestation and carried a birch polypore and a fern as potential anthelmintic remedies.'),
 ('tiupova2025', 'oa', 'W4411189390', 'narrative-review',
  'Narrative overview of P. betulinus: traditional use in Europe and Asia for infections, inflammations and gastrointestinal disorders; preclinical activities; states that well-designed in vivo studies and clinical trials remain essential to establish standardised use and safety.'),
 ('sari2025', 'oa', 'W4409534552', 'narrative-review',
  'German narrative review (Zeitschrift fur Phytotherapie) of F. betulina bioactive constituents (triterpenes incl. polyporenic acids) and in vitro and some in vivo activities. General source.'),
 ('verekar2021', 'oa0', 'W3186138993', 'narrative-review',
  'Book chapter (Advances in Macrofungi, CRC Press) on F. betulina metabolites. Its abstract states the infusion was popular in Russia, the Baltic countries, Hungary and Romania for nutritional and calming properties, that snuff from the ash is used as a pain reliever in North America and Siberia and the powder as snuff in Austria. Abstract not stored: the retrievable copy is mutilated ("F omitopsis").'),
 # --- ethnography / history ---
 ('serbia2021', 'pm', '33947042', 'traditional',
  'Ethnomycological field survey in Serbia (full text read, PMC8146042). Table row for Fomitopsis betulina ("brezina guba", 1 use report): food use "Mushroom should be eaten while still young"; medicinal use "As a preventative": tea (one spoon of dried and ground mushroom cooked in 1 L of water for 30 min) and a tincture (100 g soaked in 1 L brandy or vodka for 21 days, decanted, the mushroom then boiled in 3 L water for 3 h, tea and tincture mixed and drunk 1 to 3 times per day in small cups). Text notes an in vitro test (Shamtsyan et al.) found no strong immunomodulating effect versus other basidiomycetes.'),
 ('turi2013', 'pm', '23941666', 'traditional',
  'Analysis of Johan Turi\'s early 20th-century record of Sami folk healing (full text read, PMC3751750): a small amount of Piptoporus betulinus was burned directly on the affected area for toothache, fractures, rheumatism, headache and pneumonia.'),
 ('soukand2013', 'pm', '23941692', 'traditional',
  'Ethnobotanical review of recreational teas in Europe (full text read, PMC3852985): the Saami in Norway and Sweden made an infusion of Piptoporus betulinus, common before coffee arrived in the 1860s, revived during the Second World War and until recently made into a drink by Saami children in Norway.'),
 ('zink2019', 'pm', '30098946', 'traditional',
  'Paleopathology of the Tyrolean Iceman: re-evaluates his health problems and, with the medically effective fungi and plants found with him (birch polypore, fern), suggests care and treatment were already practised.'),
 ('lidstrom2022', 'pm', '35305672', 'traditional',
  'Ethnobiology of Sami traditional sports and games: the bracket fungus Fomitopsis betulina was used for making balls.'),
 ('svanberg2019', 'oa', 'W2988752057', 'traditional',
  'Ethnobiology Letters article on balls made from Fomitopsis betulina in Nordic traditional games.'),
 ('southtyrol2020', 'pm', '33243238', 'traditional',
  'Review of traditional medicinal plants in South Tyrol (full text read, PMC7690129): Fomitopsis betulina is reported as no longer used there and is classified as vulnerable or near threatened on the regional Red List.'),
 # --- identity / mycology ---
 ('spirin2024', 'pm', '38600960', 'preclinical',
  'Taxonomic revision of Fomitopsidaceae: Fomitopsis retained as a large genus and Piptoporus treated as its synonym. Identity source; no medicinal claim.'),
 ('minter2021', 'oa', 'W4200445874', 'traditional',
  'CABI Descriptions of Fungi and Bacteria sheet for Fomitopsis betulina: sporophores on living and dead trees, brown-rot decay of heartwood reducing it to a red-brown friable mass; distribution across Asia, Europe, North and Central America.'),
 # --- antimicrobial / antiviral / immune ---
 ('karaman2009', 'oa', 'W1971584263', 'preclinical',
  'Agar-well screen of 10 lignicolous fungi against 18 bacterial strains: extracts of Piptoporus betulinus were the most active, mainly against Gram-positive bacteria resistant to common antibiotics.'),
 ('dresch2015', 'pm', '25642401', 'preclinical',
  'Strain comparison of three European medicinal polypores: P. betulinus (and F. pinicola) ethanolic fruit-body extracts inhibited Bacillus subtilis and Staphylococcus aureus (MIC 31-125 ug/mL); antifungal activity of all three species was strain-specific (125-1000 ug/mL).'),
 ('vunduk2015', 'pm', '26854098', 'preclinical',
  'Hot water, partially purified and hot alkali extracts: moderate cytotoxicity (HeLa IC50 0.8 mg/ml for the hot water extract), antioxidant activity, in vitro ACE inhibition and antimicrobial activity notably against Enterococcus faecalis.'),
 ('alresly2016', 'oa0', 'W2626245397', 'preclinical',
  'Records of Natural Products 10(1):103-108. Isolated a new lanostane triterpene plus polyporenic acids A and C and derivatives, betulinic acid, betulin, ergosterol peroxide, 9,11-dehydroergosterol peroxide and fomefficinic acid from P. betulinus fruiting bodies; the new triterpene and some others were active against Gram-positive bacteria. Abstract not stored: the retrievable copy is mutilated (beta rendered as "b").'),
 ('krupodorova2019', 'oa', 'W2991695785', 'preclinical',
  'F. betulina culture liquid inhibited standard bacteria and multidrug-resistant clinical isolates (MBC 7.8-48.42 mg/ml for the clinical isolates).'),
 ('zaichenko2025', 'oa', 'W4408415091', 'preclinical',
  'Ethyl acetate extracts of 22 F. betulina strains: all showed antibacterial activity (B. subtilis, E. coli, K. pneumoniae, P. aeruginosa, S. aureus), DPPH radical scavenging and phenolic content, varying by strain.'),
 ('lysakova2025', 'pm', '41097066', 'preclinical',
  'Screen of 18 basidiomycete strains: culture-liquid extracts of Fomitopsis betulina strain 3 showed high antibacterial activity against Gram-positive and Gram-negative test cultures.'),
 ('kandefer1979', 'pm', '94746', 'preclinical',
  'Nucleic acids from Aspergillus niger, Piptoporus betulinus and Ganoderma applanatum reduced vaccinia virus plaques in chick embryo fibroblasts and protected mice from lethal tick-borne encephalitis virus infection.'),
 ('kawecki1978', 'pm', '219808', 'preclinical',
  'Crude RNA isolated from P. betulinus induced interferon in human fibroblasts.'),
 ('kandefer1982', 'pm', '7149923', 'preclinical',
  'RNA from P. betulinus induced interferon in human embryo fibroblasts and L929 cells, and in the spleen and liver of mice.'),
 ('grunewald2018', 'pm', '30806295', 'preclinical',
  'Water extract on primary human immune cells in vitro: strong increase in IFN-gamma release, IL-8 secretion by monocytes and dendritic cells, and dendritic-cell maturation; no effect on T-cell proliferation or activation.'),
 ('doskocil2016', 'pm', '26984176', 'preclinical',
  'Ethanol extracts of 27 central European polypores on human neutrophils: P. betulinus increased phagocytosis by 158%; its extract contained 74 mg/g beta-glucan and 155.2 umol GAE/g polyphenols.'),
 # --- anti-inflammatory ---
 ('kamo2003', 'pm', '12932134', 'preclinical',
  'Six lanostane triterpene acids from P. betulinus fruiting bodies (polyporenic acids A and C, derivatives and a new compound) suppressed TPA-induced mouse ear edema by 49-86% at 400 nmol/ear.'),
 ('wangun2004', 'pm0', '15712671', 'preclinical',
  'Journal of Antibiotics 57(11):755-758. Title states anti-inflammatory and anti-hyaluronate lyase activities of lanostanoids from P. betulinus; per Pleszczynska et al. 2017, polyporenic acid C and related triterpenoids strongly inhibited 3-alpha-hydroxysteroid dehydrogenase and bacterial hyaluronate lyase. No abstract in PubMed.'),
 ('sulkowska2018', 'pm', '30317427', 'preclinical',
  'Fruiting bodies vs mycelial cultures of F. betulina: phenolic acids, indole compounds, sterols (ergosterol, ergosterol peroxide), betulinic acid and betulin quantified; mycelium extract cytotoxic to prostate cancer cells; extract lowered COX-2 in LPS-activated A549 lung cells.'),
 # --- anticancer ---
 ('lemieszek2009', 'oa', 'W2054859249', 'preclinical',
  'Fraction from dried fruiting bodies reduced proliferation and motility of lung (A549), colon (HT-29) and glioma (C6) cancer cells with no or low toxicity to normal cells. Abstract also records folk use as an antiparasitic and antimicrobial agent for wounds, for rectal cancer and stomach diseases, and tea with antibacterial, antifatiguing, immunoenhancing and soothing properties.'),
 ('cyranka2011', 'pm', '22181840', 'preclinical',
  'Ether and ethanol extracts of in vitro grown mycelium decreased viability of LS180 colon cancer cells; cytotoxic to normal colon cells only at the highest concentration.'),
 ('pleszczynska2016', 'pm', '27465851', 'preclinical',
  'First indoor cultivation of fruiting bodies; water and ethanol extracts of cultured and wild fruiting bodies were antiproliferative and antimigrative in colon, lung and breast cancer cell lines.'),
 ('tohtahon2017', 'pm', '28800422', 'preclinical',
  'Piptolinic acids A-E (new lanostane triterpenoids) from fruiting bodies; piptolinic acid A cytotoxic to HL-60 and THP-1 leukemia cells comparably to fluorouracil.'),
 ('khalilov2019', 'pm', '30362364', 'preclinical',
  'Piptolinic acids F-J plus seven known lanostanes from fruiting bodies; one known compound moderately cytotoxic to A-375 melanoma and 786-O renal carcinoma cells.'),
 ('czerwonka2019', 'pm', '31440877', 'preclinical',
  'Glucooligosaccharides from F. betulina alpha-(1-3)-glucan were antiproliferative and pro-apoptotic against colon cancer cells but not normal colon epithelial cells.'),
 ('sari2020', 'pm', '32463994', 'preclinical',
  'Wild fruiting bodies at different growing stages: high beta-glucan content with no significant difference by size or location; a >300 kDa ultrafiltrated fraction blocked tumor cell migration by 38% in a scratch assay without cytotoxicity.'),
 ('sofrenic2021', 'pm', '33166752', 'preclinical',
  'Polyporenic acids E-M and fomitosides L-O (new 24-methylene lanostanes) plus 17 known analogues from fruiting bodies; fomitosides L and N and known compounds (dehydropachymic acid, pachymic acid, 3-epi-dehydrotumulosic acid) cytotoxic to HL60 leukemia cells.'),
 ('bozek2022', 'pm', '36430391', 'preclinical',
  'Ethanolic extract cytotoxic to WM115 and A375 melanoma cells with low toxicity to Hs27 skin fibroblasts; betulin identified as one active compound.'),
 ('nowotarska2024aq', 'pm', '39408283', 'preclinical',
  'Aqueous extract selectively cytotoxic to lung, melanoma and colorectal cancer lines while sparing four normal cell lines.'),
 ('blumenberg1963', 'pm0', '13971899', 'preclinical',
  'Arzneimittel-Forschung 1963 (German). Title reports inhibition of mouse sarcoma S-37 growth by the birch fungus (Polyporus betulinus). No abstract in PubMed; cited from the title only.'),
 # --- antioxidant / neuro ---
 ('raseta2025', 'pm', '41422539', 'preclinical',
  'Methanolic fruiting-body extract: polyamines (spermidine 60.21, spermine 41.71 mg/kg d.w.), gallic and quinic acids, apiin; DPPH and ABTS antioxidant capacity and 99% acetylcholinesterase inhibition, described as neuroprotective potential.'),
 ('zaichenko2026', 'pm', '41659796', 'preclinical',
  'Submerged-culture mycelium extracts: total phenolics and DPPH radical inhibition (up to about 90%) under different cultivation conditions.'),
 ('balkans2024', 'pm', '38257227', 'preclinical',
  'Five polypores from Serbia (full text read, PMC10819588): F. betulina methanol extract scavenged DPPH (92.18% at 5 mg/mL) and hydroxyl radicals (85% at 0.5 mg/mL) and inhibited linoleic acid peroxidation; p-hydroxybenzoic acid was its main phenolic acid; no selectivity in cytotoxicity.'),
 ('reis2011', 'pm', '21613974', 'preclinical',
  'Antioxidant molecule profiles of inedible wild mushrooms; the full text includes Piptoporus betulinus (highest lycopene of the species tested, at most 0.24 mg/100 g dw; tocopherols and ascorbic acid). The abstract does not name the species.'),
 # --- chemistry ---
 ('kawagishi2002', 'pm', '12596882', 'preclinical',
  'A new hydroquinone and polyporenic acid C isolated from P. betulinus as matrix metalloproteinase inhibitors.'),
 ('wiater2011', 'pm', '21188616', 'preclinical',
  'Water-insoluble, alkali-soluble alpha-(1-3)-D-glucans from four fungi including P. betulinus; carboxymethylated glucans showed concentration-dependent cytotoxicity.'),
 ('olennikov2012', 'pm', '22567888', 'preclinical',
  'Piptoporane I, a 270 kDa branched alpha-(1-3)-glucan with beta-glucose side residues, isolated from P. betulinus fruiting bodies.'),
 ('dejesus2018a', 'pm', '30177176', 'preclinical',
  'Separation of water-insoluble alpha- and beta-D-glucans from F. betulina fruiting bodies: a branched (1-3),(1-6)-beta-glucan and a linear (1-3)-alpha-glucan.'),
 ('dejesus2018b', 'pm', '29274425', 'preclinical',
  'Water-soluble (1-3)-beta-D-glucan (O-6 substituted) from P. betulinus; not toxic to Caco-2 cells up to 1000 ug/mL and promoted cell migration in a scratch assay. Cited for the glucan structure; a single in vitro migration result is not used as a wound-healing claim.'),
 ('rosecke2000', 'pm', '11014259', 'preclinical',
  'Hydrodistillation products of four wood-rotting basidiomycetes including P. betulinus: mono- and sesquiterpenes, aliphatic alcohols, aldehydes and ketones.'),
 ('cross1940', 'oa0', 'W2081254753', 'preclinical',
  'Journal of the Chemical Society 1940, 632: early isolation of the triterpene acids of Polyporus betulinus. Cited from the title; no abstract available.'),
 ('schlegel2000', 'pm0', '11099232', 'preclinical',
  'Journal of Antibiotics 53(9):973-974. Title reports piptamine, a new antibiotic produced by Piptoporus betulinus strain Lu 9-1. No abstract in PubMed; activity values from Pleszczynska et al. 2017.'),
 ('krejsa2021', 'pm', '34268685', 'preclinical',
  'Element contents of four birch-associated fungi: F. betulina fruiting bodies held high Ca (400), Fe (110), Mg (1100) and Zn (220 mg/kg dry matter).'),
 ('sofrenic2021dna', 'oa0', 'W3171060743', 'preclinical',
  'Journal of the Serbian Chemical Society 86(9):809-817. Eleven lanostane triterpenoids and betulin from F. betulina reduced micronucleus frequency (DNA damage) in human lymphocytes in vitro. Abstract not stored: the retrievable copy is mutilated (symbols replaced by "?").'),
 ('achenbach2026', 'pm', '42102927', 'preclinical',
  'Screen of 26 ethnomedicinal fungi: F. betulina extract was among the strongest inhibitors of endothelial (HUVEC) cell proliferation. Single-model finding; general source.'),
 # --- safety ---
 ('fajemiroye2017', 'pm', '28605341', 'preclinical',
  'Oral ethanolic extract, fractions and stigmasterol given acutely and for 14 days to normotensive rats did not alter blood pressure, heart rate or vascular conductance.'),
 ('button2020', 'pm', '31897873', 'preclinical',
  'Arsenic in F. betulina from a contaminated former-mine woodland was about tenfold higher than at an uncontaminated site (maximum 1.6 mg/kg), though low relative to soil-dwelling species.'),
 ('wiesiolek1968', 'pm0', '5669425', 'clinical',
  'Polish case report (Wiadomosci Lekarskie 1968), title only: Polyporus betulinus as a probable cause of congenital malformation in a fetus. No abstract; causality not established.'),
 # --- web (identification, harvest stage, lookalikes) ---
 ('fcc', 'web', None, 'traditional',
  'Foraging Course Company guide, read 2026-11-16. Young fruit body "Starting of as a spherical white bubble bursting from the wood of its host"; later the pores "turn buff and become more tough" and "older specimens can remain on the wood all year". Lookalikes: could be confused at first glance with horse hoof fungus (Fomes fomentarius) or the blushing bracket, "both of these are much more solid brackets"; Hazards: "None known". Notes use as a razor strop, plaster and tinder.'),
 ('firstnature', 'web', None, 'traditional',
  'First Nature species page (has a reference list), read 2026-11-16: "it is difficult to confuse this polypore with any other species because of its distinctive colouring"; grey-brown and almost spherical at first, flattening and turning white underneath as it matures; annual brackets that may persist through one winter; parasitic on living trees and saprobic once the tree dies.'),
 ('wildfooduk', 'web', None, 'traditional',
  'Wild Food UK species page, read 2026-11-16: "This distinctive mushroom is difficult to confuse with any other as it only grows on Birch"; fruiting body 10-20 cm, white turning grey/brown with age, starting globose, then hoof-shaped, finally a flat bracket; very fine white pores turning buff with maturity.'),
 ('psr', 'web', None, 'traditional',
  'Practical Self Reliance foraging article, read 2026-11-16: "Young birch polypores can be a bit more round as they\'re just bursting through the tree bark"; shows small specimens "already well past prime"; "Birch polypore grows primarily on birch trees, and has no look-alikes."'),
 ('mushroomexpert', 'web', None, 'traditional',
  'MushroomExpert.com species page by Michael Kuo (26 September 2022, with references), read 2026-11-16: cap at first lump-like and nearly spherical; flesh white, thick and corky; pores white, aging greyish to brownish; annual, but fruiting bodies are tough and often found the next year.'),
]

WEB = {
 'fcc': ('Foraging Course Company', 'Birch polypore - Fomitopsis betulina: foraging guide', 'https://foragingcoursecompany.co.uk/foraging-guide-birch-polypore', 'foragingcourse_birchpolypore'),
 'firstnature': ('First Nature', 'Fomitopsis betulina, Birch Polypore or Razor Strop Fungus', 'https://first-nature.com/fungi/piptoporus-betulinus.php', 'firstnature_birchpolypore'),
 'wildfooduk': ('Wild Food UK', 'Birch Polypore - Fomitopsis betulina', 'https://www.wildfooduk.com/mushroom-guide/birch-polypore-fomitopsis-betulina/', 'wildfooduk_birchpolypore'),
 'psr': ('Practical Self Reliance', 'Birch Polypore (Fomitopsis betulina)', 'https://practicalselfreliance.com/birch-polypore/', 'practicalselfreliance_birchpolypore'),
 'mushroomexpert': ('Kuo, M.', 'Fomitopsis betulina', 'https://mushroomexpert.com/fomitopsis_betulina.html', 'kuo2022fomitopsisbetulina'),
}
NONPM_META = {  # biblio not in Crossref
 'W2626245397': dict(author='Alresly, Z., Lindequist, U., Lalk, M., Porzel, A., Arnold, N. and Wessjohann, L.A.',
                     title='Bioactive Triterpenes from the Fungus Piptoporus betulinus', journal='Records of Natural Products',
                     year='2016', volume='10', number='1', pages='103--108', url='https://doaj.org/article/00cec7239bff46038a077c9fb2774ac6'),
 'W3186138993': dict(author='Verekar, S.A., Gupta, M.K. and Deshmukh, S.K.', title='Fomitopsis betulina: A Rich Source of Diverse Bioactive Metabolites',
                     journal='Advances in Macrofungi (CRC Press)', year='2021', pages='52--66', doi='10.1201/9781003191278-5'),
}
REF = {}


def mkkey(last, year, slug):
    # first-author surname + year + 'betulina' + any distinguishing suffix after the year in the slug (sr, aq, a, b, dna)
    return asc(last) + year + 'betulina' + re.sub(r'^.*?\d{4}', '', slug)


def entry(slug, kind, ident, st, summary, rid):
    if kind in ('pm', 'pm0'):
        x = CACHE[ident]
        key = mkkey(x['authors'][0].split(',')[0], x['year'], slug)
        f = [('author', clean(authors_pm(x['authors']))), ('title', clean(x['title']).rstrip('.')),
             ('journal', clean(journal(x['journal']))), ('year', x['year'])]
        f += [(k, x[k]) for k in ('volume', 'number', 'pages') if x.get(k)]
        if x.get('doi'):
            f.append(('doi', x['doi']))
        f += [('pmid', ident)]
        if not x.get('doi'):
            f.append(('url', f'https://pubmed.ncbi.nlm.nih.gov/{ident}/'))
        f += [('note', rid), ('study_type', st), ('summary', clean(summary))]
        if kind == 'pm':
            assert x['abstract'], ident
            f.append(('abstract', clean(x['abstract'])))
        else:
            assert not x['abstract'], ident
        return 'article', key, f
    if kind in ('oa', 'oa0'):
        src = NONPM.get(ident) or {}
        meta = NONPM_META.get(ident)
        if meta is None:
            c = src['crossref']
            meta = dict(author=authors_cr(c['authors']), title=clean(c['title']), journal=clean(c['journal']), year=str(c['year']))
            for a, b in (('volume', 'volume'), ('issue', 'number')):
                if c.get(a):
                    meta[b] = c[a]
            if c.get('page'):
                meta['pages'] = c['page'].replace('-', '--')
            meta['doi'] = src['doi']
        meta['author'] = meta['author'].replace('М', 'M')  # Crossref returns a Cyrillic capital M in one initial
        key = mkkey(meta['author'].split(',')[0], meta['year'], slug)
        f = [(k, meta[k]) for k in ('author', 'title', 'journal', 'year', 'volume', 'number', 'pages', 'doi', 'url') if meta.get(k)]
        f += [('note', rid), ('study_type', st), ('summary', clean(summary))]
        if kind == 'oa':
            a = re.sub(r'^Abstract\s+', '', src['openalex_abstract']).strip()
            assert a and '?g' not in a, ident
            f.append(('abstract', clean(a)))
        return 'article', key, f
    au, title, url, key = WEB[slug]
    f = [('author', au), ('title', title), ('url', url), ('year', '2026' if slug != 'mushroomexpert' else '2022'),
         ('note', rid), ('kind', 'misc'), ('study_type', st), ('summary', clean(summary))]
    return 'misc', key, f


def bibline(k, v):
    return f'  {k:<8} = {{{v}}},' if len(k) <= 8 else f'  {k} = {{{v}}},'


def write_bib(entries):
    text = open(BIB, encoding='utf-8', newline='').read()
    lines = text.split('\n')
    existing_keys = set(re.findall(r'^@\w+\{([^,]+),', text, re.M))
    for etype, key, fields in entries:
        assert key not in existing_keys, ('duplicate key', key)
        rid = dict(fields)['note']
        assert not re.search(r'note\s*=\s*\{' + rid + r'\}', text), rid
        for k, v in fields:
            assert '{' not in v and '}' not in v and '\n' not in v, (key, k)
        body = [f'@{etype}{{{key},'] + [bibline(k, v) for k, v in fields]
        body[-1] = body[-1][:-1]
        body += ['}', '']
        starts = [i for i, ln in enumerate(lines) if ln.startswith('@')]
        keys = [re.match(r'@\w+\{([^,]+),', lines[i]).group(1) for i in starts]
        pos = next((starts[j] for j, k in enumerate(keys) if k.lower() > key), len(lines))
        lines[pos:pos] = body
        existing_keys.add(key)
    open(BIB, 'w', encoding='utf-8', newline='').write('\n'.join(lines))


def R(*slugs):
    return [REF[s] for s in slugs]


def main():
    entries = []
    for n, (slug, kind, ident, st, summary) in enumerate(S):
        rid = f'REF-{FIRST_REF + n}'
        REF[slug] = rid
        entries.append(entry(slug, kind, ident, st, summary, rid))
    keys = [k for _, k, _ in entries]
    assert len(set(keys)) == len(keys), [k for k in keys if keys.count(k) > 1]
    for _, k, f in entries:
        for kk, v in f:
            if kk in ('summary',):
                assert '—' not in v and '–' not in v, (k, 'dash in summary')
    record = build_record()
    dump = yaml.safe_dump(record, sort_keys=False, allow_unicode=True, width=100, default_flow_style=False)
    assert '—' not in dump and '–' not in dump, 'em/en dash in record'
    snap = open(BIB, 'rb').read()
    try:
        write_bib(entries)
        assert not os.path.exists(PLANT), 'record already exists'
        open(PLANT, 'w', encoding='utf-8', newline='\n').write(dump)
    except BaseException:
        open(BIB, 'wb').write(snap)
        if os.path.exists(PLANT):
            os.remove(PLANT)
        raise
    with open(os.path.join(HERE, 'ref_map.tsv'), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write('ref\tkey\tslug\tsource\tstudy_type\n')
        for (slug, kind, ident, st, _), (_, key, _) in zip(S, entries):
            fh.write(f'{REF[slug]}\t{key}\t{slug}\t{ident or WEB[slug][2]}\t{st}\n')
    print(f'added {len(entries)} references REF-{FIRST_REF}..REF-{FIRST_REF + len(entries) - 1}; wrote {PLANT}')


def build_record():
    anticancer = R('nowotarska2024sr', 'lemieszek2009', 'cyranka2011', 'pleszczynska2016', 'tohtahon2017', 'khalilov2019',
                   'sulkowska2018', 'czerwonka2019', 'sari2020', 'sofrenic2021', 'bozek2022', 'nowotarska2024aq',
                   'vunduk2015', 'blumenberg1963')
    wired_general = R('grienke2014', 'sari2025', 'spirin2024', 'achenbach2026', 'sofrenic2021dna', 'fajemiroye2017')
    return {
        'id': 'fomitopsis-betulina',
        'scientific_name': 'Fomitopsis betulina',
        'common_names': ['Birch polypore', 'Birch bracket', 'Razor strop'],
        'common_slug': 'birch-polypore',
        'family': 'Fomitopsidaceae',
        'synonyms': ['Piptoporus betulinus', 'Polyporus betulinus', 'Boletus betulinus', 'Fomes betulinus', 'Ungulina betulina'],
        'external_ids': {'gbif': 9819973, 'wikidata': 'Q96894257'},
        'parts_used': ['Fruiting body'],
        'botanical_description': {
            'text': ('Annual bracket fungus (not a plant) that grows only on birch. Fruiting bodies emerge as white, rounded lumps '
                     'breaking through the bark, then expand into smooth, hoof- or kidney-shaped brackets attached to the trunk '
                     'without a stem, white at first and later grey-brown on top. The underside is a layer of very fine white '
                     'pores that turn buff to brownish with age, and the flesh is white, thick and corky. The fungus decays the '
                     'wood to a red-brown, crumbly brown rot.'),
            'height': 'Bracket about 10-20 cm across',
            'habit': 'Annual bracket (polypore) fungus on birch; mainly on dead trees, occasionally parasitic on living ones',
            'leaves': 'Not applicable (fungus)',
            'flowers': 'Not applicable (fungus); reproduces by spores',
            'stem': 'No stem; the bracket is attached directly to the trunk (sessile)',
            'root': 'Mycelium grows through the birch wood, causing brown rot',
            'fruit': 'Spores are shed from fine white pores on the underside; basidiospores smooth, colourless and cylindrical',
            'flowering_period': 'Annual fruiting bodies; old, tough brackets often remain on the tree into the following year',
            'reference_ids': R('pleszczynska2017', 'mushroomexpert', 'wildfooduk', 'firstnature', 'minter2021'),
            'status': 'verified',
        },
        'habitat': {
            'text': ('Grows only on birch (Betula species such as silver, downy and paper birch), mainly as a saprotroph on dead '
                     'trees and occasionally as a parasite of living ones, in northern temperate forests and parks of Europe, '
                     'Asia and North America. It is one of the commonest brown-rot fungi and reduces the heartwood to a '
                     'red-brown, crumbly mass.'),
            'reference_ids': R('pleszczynska2017', 'minter2021'),
            'status': 'verified',
        },
        'harvesting': {
            'text': ('The fruiting body is the part used. Folk practice favours young, fresh brackets: in Serbia it was eaten '
                     'only while still young, and dried, ground fruiting bodies were used for tea, while fresh pieces were laid '
                     'on wounds. Fruiting bodies take up arsenic from polluted ground (about ten times more near a former mine '
                     'than at a clean site), so gather away from mines and contaminated land. In South Tyrol the species is '
                     'listed as vulnerable or near threatened on the regional Red List.'),
            'parts': ['Fruiting body'],
            'reference_ids': R('serbia2021', 'pleszczynska2017', 'button2020', 'southtyrol2020'),
            'status': 'verified',
        },
        'harvest_readiness': [{
            'part': 'fruiting-body',
            'signals': ['Gather the fruiting body young: still white or off-white and rounded, freshly breaking through the '
                        'birch bark, with white pores and firm white flesh. Pass over brackets that have turned grey-brown, '
                        'tough or corky with buff pores; old brackets persist on the tree into the next year and are past '
                        'their prime.'],
            'basis': 'traditional',
            'source_quote': 'Mushroom should be eaten while still young',
            'reference_ids': R('serbia2021', 'psr', 'fcc', 'mushroomexpert', 'sari2020'),
            'independent_confirmation': ('Practical Self Reliance (independent, web): "Young birch polypores can be a bit more '
                                         'round as they\'re just bursting through the tree bark", contrasting small specimens '
                                         '"already well past prime". Foraging Course Company and MushroomExpert agree on the '
                                         'stage sequence (white sphere bursting through the bark; pores later buff and tougher; '
                                         'old brackets found the next year). Agrees.'),
            'species_confirmed': True,
            'status': 'verified',
            'notes': ('Primary quote is the food-use column of the Fomitopsis betulina row in the Serbian ethnomycological '
                      'survey (one use report). No constituent-based timing: Sari et al. 2020 found no significant difference '
                      'in beta-glucan content by fruiting-body size or growing stage. No months or regions given on purpose.'),
        }],
        'traditional_uses': {
            'text': ('Ötzi the Iceman, who lived about 5,300 years ago, carried two pieces of birch polypore; he had a whipworm '
                     'infection, and a medicinal (anthelmintic) purpose has been proposed, though this remains disputed. In '
                     'European folk medicine an infusion of the fruiting body was popular in Russia, the Baltic countries, '
                     'Hungary and Romania for its nutritional and calming properties, and the tea was used against cancers, '
                     'stomach and gastrointestinal complaints and parasites, to enhance immunity and to relieve fatigue. Fresh '
                     'pieces were applied to wounds as antiseptic, bleeding-stopping dressings, and the dried powder or its ash '
                     'was used as a painkiller or snuff. In Serbia it was recorded as a preventative taken as a tea or as a '
                     'tincture in brandy or vodka. The Sami drank a hot infusion of it (common before coffee arrived in the '
                     '1860s and revived during the Second World War), burned small pieces on the skin for toothache, '
                     'headache, rheumatism, fractures and pneumonia, and made balls from it for games. It was also used as '
                     'tinder and by barbers as a razor strop.'),
            'reference_ids': R('pleszczynska2017', 'nerlich2021', 'zink2019', 'lemieszek2009', 'li2024', 'verekar2021',
                               'tiupova2025', 'serbia2021', 'turi2013', 'soukand2013', 'svanberg2019', 'lidstrom2022', 'fcc'),
            'status': 'verified',
        },
        'preparations': [
            {'name': 'Decoction (tea)', 'text': ('Dried, ground fruiting body boiled in water and drunk as a tea; infusions of '
                                                 'the fruiting body were traditional in Russia, the Baltic countries, Hungary '
                                                 'and Romania, and among the Sami.'),
             'reference_ids': R('serbia2021', 'pleszczynska2017', 'soukand2013'), 'status': 'verified'},
            {'name': 'Tincture (folk record)', 'text': ('Serbian folk record: 100 g of the mushroom soaked in 1 L of brandy or '
                                                        'vodka for 21 days with daily shaking, then decanted; the mushroom is then '
                                                        'boiled in 3 L of water for 3 hours and the cooled tea mixed with the '
                                                        'tincture.'),
             'reference_ids': R('serbia2021'), 'status': 'verified'},
            {'name': 'Fresh dressing (traditional)', 'text': ('Fresh fruiting body applied to wounds as an antiseptic, '
                                                              'bleeding-stopping dressing.'),
             'reference_ids': R('pleszczynska2017'), 'status': 'verified'},
            {'name': 'Powder or ash (traditional)', 'text': ('Dried fruiting body powdered, or burned to ash, and used as a '
                                                             'painkiller or snuff.'),
             'reference_ids': R('pleszczynska2017', 'verekar2021'), 'status': 'verified'},
        ],
        'dosage': [
            {'name': 'Decoction (tea)', 'text': ('Serbian folk record from a single informant: one spoon of the dried, ground '
                                                 'mushroom cooked in 1 L of water for 30 minutes, taken as a preventative. A '
                                                 'recorded folk practice, not a tested dose; no human trial has studied birch '
                                                 'polypore. Educational reference only.'),
             'reference_ids': R('serbia2021', 'nowotarska2024sr'), 'status': 'verified'},
            {'name': 'Tincture and tea mixture (folk record)', 'text': ('Same Serbian record: the tincture-and-tea mixture was '
                                                                        'drunk 1 to 3 times a day in small cups. Folk practice '
                                                                        'only, not a tested dose. Educational reference only.'),
             'reference_ids': R('serbia2021'), 'status': 'verified'},
        ],
        'constituents': [
            {'name': 'Lanostane triterpene acids (polyporenic acids, piptolinic acids, fomitosides)', 'compounds': ['terpene'],
             'note': ('The main studied secondary metabolites: polyporenic acids A and C and their derivatives, polyporenic '
                      'acids E-M, piptolinic acids A-J, fomitosides L-O, pachymic and dehydrotumulosic acids, and fomefficinic '
                      'acid, isolated from the fruiting bodies.'),
             'reference_ids': R('kamo2003', 'tohtahon2017', 'khalilov2019', 'sofrenic2021', 'alresly2016', 'cross1940',
                                'kawagishi2002')},
            {'name': 'Betulin, betulinic acid and lupeol', 'compounds': ['terpene'],
             'note': 'Lupane triterpenes found in the fruiting bodies and in cultured mycelium; betulin was identified as one active compound of an ethanolic extract.',
             'reference_ids': R('sulkowska2018', 'alresly2016', 'bozek2022', 'pleszczynska2017')},
            {'name': 'Fungal sterols (ergosterol, ergosterol peroxide)',
             'note': 'Ergosterol, ergosterol peroxide and 9,11-dehydroergosterol peroxide.',
             'reference_ids': R('sulkowska2018', 'alresly2016')},
            {'name': 'Polysaccharides (alpha- and beta-glucans)', 'compounds': ['polysaccharide'],
             'note': ('A (1-3)-alpha-glucan (piptoporane I and related glucans) makes up to 44-53% of the cell-wall dry weight; '
                      'the fruiting bodies also contain branched (1-3),(1-6)-beta-glucans, with high beta-glucan content at all '
                      'growing stages (74 mg/g in one ethanol extract).'),
             'reference_ids': R('wiater2011', 'olennikov2012', 'dejesus2018a', 'dejesus2018b', 'sari2020', 'doskocil2016',
                                'pleszczynska2017')},
            {'name': 'Piptamine',
             'note': ('An antibiotic amine (N-benzyl-N-methylpentadecan-1-amine) produced by the fungus in culture, active '
                      'against Gram-positive bacteria (MIC 0.78-12.5 ug/ml) and yeasts including Candida albicans (MIC 6.25 ug/ml).'),
             'reference_ids': R('schlegel2000', 'pleszczynska2017')},
            {'name': 'Phenolic acids and polyamines', 'compounds': ['phenolic-acid', 'gallic-acid'],
             'note': ('Gallic, quinic, syringic and p-hydroxybenzoic acids; the polyamines spermidine (60 mg/kg dry weight) and '
                      'spermine (42 mg/kg).'),
             'reference_ids': R('raseta2025', 'sulkowska2018', 'balkans2024')},
            {'name': 'Hydroquinone matrix-metalloproteinase inhibitor',
             'note': '(E)-2-(4-hydroxy-3-methyl-2-butenyl)-hydroquinone, isolated with polyporenic acid C as an MMP inhibitor.',
             'reference_ids': R('kawagishi2002')},
            {'name': 'Volatile terpenes and aroma compounds', 'compounds': ['terpene'],
             'note': 'Mono- and sesquiterpenes, aliphatic alcohols, aldehydes and ketones in the distilled volatile fraction.',
             'reference_ids': R('rosecke2000', 'pleszczynska2017')},
            {'name': 'Antioxidant vitamins and minerals', 'compounds': ['carotenoid'],
             'note': ('Ascorbic acid, tocopherols, beta-carotene and lycopene; fruiting bodies are rich in calcium, iron, '
                      'magnesium and zinc.'),
             'reference_ids': R('reis2011', 'pleszczynska2017', 'krejsa2021')},
        ],
        'actions': [
            {'action': 'antimicrobial', 'reference_ids': R('karaman2009', 'dresch2015', 'vunduk2015', 'alresly2016',
                                                            'schlegel2000', 'krupodorova2019', 'zaichenko2025', 'lysakova2025'),
             'status': 'verified'},
            {'action': 'antifungal', 'reference_ids': R('dresch2015', 'pleszczynska2017'), 'status': 'verified'},
            {'action': 'antiviral', 'reference_ids': R('kandefer1979', 'pleszczynska2017'), 'status': 'needs-review'},
            {'action': 'immunomodulator', 'reference_ids': R('grunewald2018', 'doskocil2016', 'kawecki1978', 'kandefer1982'),
             'status': 'verified'},
            {'action': 'anti-inflammatory', 'reference_ids': R('kamo2003', 'wangun2004', 'sulkowska2018'), 'status': 'verified'},
            {'action': 'antioxidant', 'reference_ids': R('vunduk2015', 'raseta2025', 'zaichenko2025', 'zaichenko2026',
                                                          'balkans2024'), 'status': 'verified'},
            {'action': 'anticancer', 'reference_ids': anticancer, 'status': 'needs-review'},
            {'action': 'neuroprotective', 'reference_ids': R('raseta2025', 'pleszczynska2017'), 'status': 'needs-review'},
        ],
        'contraindications': [
            {'note': ('No human studies. As of the 2024 systematic review there are no clinical studies confirming the '
                      'efficacy or safety of birch polypore in humans; every activity listed here comes from cell, test-tube '
                      'or animal work. In rats, oral extracts given for 14 days did not change blood pressure or heart rate.'),
             'severity': 'info', 'reference_ids': R('nowotarska2024sr', 'tiupova2025', 'fajemiroye2017'), 'status': 'verified'},
            {'note': ('Pregnancy: safety is unknown, and a 1968 Polish case report named birch polypore (as Polyporus '
                      'betulinus) as a probable cause of a congenital malformation in a fetus.'),
             'severity': 'caution', 'reference_ids': R('wiesiolek1968', 'nowotarska2024sr'), 'status': 'verified'},
            {'note': ('Wild collection: fruiting bodies take up arsenic from contaminated ground (about ten times more near a '
                      'former mine than at a clean site, up to 1.6 mg/kg). Do not gather near mines or polluted land.'),
             'severity': 'caution', 'reference_ids': R('button2020'), 'status': 'verified'},
        ],
        'lookalikes_review': {
            'outcome': 'none-known',
            'reviewed_by': 'Omnia Sana (owner-authorized)',
            'reviewed_date': TODAY,
            'reference_ids': R('firstnature', 'fcc', 'wildfooduk', 'psr'),
        },
        'references': wired_general,
        'provenance': 'pubmed+europepmc+openalex+web',
        'status': 'verified',
        'last_updated': TODAY,
        'internal_notes': NOTES,
    }


NOTES = (
    '2026-11-16: record created (Model: anthropic/claude-opus-5-5). Accepted name Fomitopsis betulina (Bull.) B.K.Cui, '
    'M.L.Han & Y.C.Dai 2016 (GBIF 9819973 ACCEPTED; Wikidata Q96894257, the item with the sitelinks and common names; '
    'Q865591 is the older Piptoporus item). Spirin et al. 2024 keep Fomitopsis and sink Piptoporus into it. Public name '
    '"Birch polypore"; "brown birch polypore" is not attested in any source and was not used; "birch conk" avoided '
    '(chaga uses it). | SEARCH: PubMed all name variants (83 records, all abstracts read); Europe PMC incl. full text, '
    'patents, preprints, Agricola (302 records; every hit for patients/randomised/clinical trial/case report was a '
    'passing mention in a review, the one "case report" hit is a conference abstract on antioxidant chemistry); '
    'OpenAlex title/abstract (400 records) plus Chinese, Russian, Polish and German names (no relevant hits); '
    'ClinicalTrials.gov (no trial of this species; the two Fomitopsis RCTs, NCT04667247 and NCT04951336, used '
    'F. officinalis with Trametes versicolor); Crossref; PMC/Europe PMC full text of about 30 papers; 7 web pages. '
    'NOT searched: CNKI, eLibrary.ru, WHO ICTRP, EU CTR, Google Scholar. | HUMAN EVIDENCE: none. The 2024 PRISMA '
    'review (Nowotarska) states there are no clinical studies of efficacy or safety in humans. | NO INDICATIONS by owner '
    'decision 2026-11-16: symptom pairs need human evidence (a human trial or a review of human studies), one rule for all '
    'plants. The lab-only PRISMA review would otherwise have scored a cancer pair 7/10. All lab findings are recorded as '
    'actions. | REJECTED (wrong species): Piptoporus soloniensis (PMIDs 16233291, 21888369, 40997269), P. quercinus / '
    'Buglossoporus (15119356), Lenzites betulina (betulinans; not this species), F. pinicola and F. officinalis papers. '
    '| NOT USED: Li 2024 abstract claims anti-malarial effects but the body has no data; Herbal Reality page not read. '
    'Wound healing: de Jesus 2018 (isolated beta-glucan, Caco-2 scratch assay positive) conflicts with Wende 2010 '
    '(Planta Medica conference abstract; crude extracts not significant in HaCaT scratch assay), so no vulnerary action. '
    'ACE inhibition in vitro (Vunduk 2015; Western Balkans 2024) but oral extracts did not change blood pressure in rats '
    '(Fajemiroye 2017), so no antihypertensive action. Serbian survey notes Shamtsyan 2004 found no strong '
    'immunomodulating effect in vitro (not retrieved). | DEAD ENDS (paywalled, abstract not retrievable, so not cited): '
    'Papp et al. 2017 Transylvania ethnomycology (Genet Resour Crop Evol 64:101-111), Peintner, Poder & Pumpel 1998 '
    'The iceman\'s fungi (Mycol Res 102:1153-1162), Han et al. 2016 Fungal Diversity 80:343-373, Capasso 1998 Lancet '
    'letter. Not used: Efimenko 1960/1961 and Kandefer-Szerszen 1974 (titles only, no further data); Uzbekistan 2023 and '
    'Mazovia 2019 surveys repeat literature claims rather than recording local use. | DOSAGE: the only dose is a Serbian '
    'folk record from one informant; no EMA, WHO, ESCOP or Commission E monograph exists for this fungus, so no tincture '
    'practice record was built (the calculator degrades to general defaults). | Lookalikes: none-known, owner-authorized '
    '2026-11-16; confusables named in sources (Fomes fomentarius, blushing bracket) are not toxic. | Build script and '
    'source map: docs/additions/2026-11-16-fomitopsis-betulina/.'
)

if __name__ == '__main__':
    main()
