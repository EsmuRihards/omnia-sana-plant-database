#!/usr/bin/env python3
"""
scripts/verify_names.py — Multilingual Plant-Name Dictionary verification pipeline.

Anchors each plant's botanical identity (GBIF / Wikidata / POWO ids) and harvests
VERIFIED vernacular (common) names per language from authoritative sources, applying a
STRICT multi-source accept rule. There is NO machine translation anywhere in the accept
path: a name is only published (status: verified) when it is attested by

    >= 1 curated authority (Catalogue of Life / POWO-WCVP / EPPO)   OR
    >= 2 independent sources agreeing.

Everything below that bar is kept as status: needs-review and is NEVER served publicly
(build.py drops it from build/names.json).

Sources (all keyless): GBIF vernacularNames, Wikidata P1843 (taxon common name) +
sitelinks, Wikipedia titles. EPPO is queried only if EPPO_TOKEN is set in the env.

Writes, per plant:
  * external_ids (gbif / wikidata / powo) back into plants/<id>.yaml — surgical text
    insert, minimal diff, never clobbers other keys. This is the reusable botanical anchor.
  * names/<id>.yaml — the verified vernacular-name record (schema/vernacular_names.schema.json).

Idempotent and cached (.names_cache.json, gitignored). New-plant automation just calls this
with the new id. Usage:
    python scripts/verify_names.py                         # every plant
    python scripts/verify_names.py matricaria-chamomilla   # one or more ids
    python scripts/verify_names.py --refresh <id>          # bypass cache for these
    python scripts/verify_names.py --no-anchor             # names only, don't touch plants/
"""
import os, re, sys, json, glob, time, datetime, unicodedata, urllib.parse, urllib.request, urllib.error, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLANTS = os.path.join(ROOT, "plants")
VOCAB = os.path.join(ROOT, "vocabularies")
NAMESDIR = os.path.join(ROOT, "names")
CACHE = os.path.join(ROOT, ".names_cache.json")
UA = "OmniaSanaNamesBot/1.0 (+https://omniasana.bio; multilingual plant-name dictionary)"
EPPO_TOKEN = os.environ.get("EPPO_TOKEN", "").strip()
TODAY = datetime.date.today().isoformat()

# GBIF vernacular `source` dataset -> curated-authority class. WCVP powers POWO; COL /
# Species 2000 / World Flora Online / Euro+Med are curated taxonomic checklists.
CURATED_POWO_RE = re.compile(r"world checklist of vascular plants|wcvp|wcsp", re.I)
CURATED_COL_RE = re.compile(r"catalogue of life|species 2000|world flora online|euro\+?\s*med|the plant list", re.I)

_cache = {}


def load_cache():
    global _cache
    if os.path.exists(CACHE):
        try:
            _cache = json.load(open(CACHE, encoding="utf-8"))
        except Exception:
            _cache = {}


def save_cache():
    json.dump(_cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False)


def http_json(url, headers=None, refresh=False, tries=4):
    """GET JSON with UA, on-disk cache, and polite retry/backoff. Returns dict/list or None."""
    if not refresh and url in _cache:
        return _cache[url]
    h = {"User-Agent": UA, "Accept": "application/json"}
    if headers:
        h.update(headers)
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers=h)
            with urllib.request.urlopen(req, timeout=30) as r:
                data = json.loads(r.read().decode("utf-8"))
            _cache[url] = data
            time.sleep(0.15)   # be a good API citizen
            return data
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(1.5 * (attempt + 1))
                continue
            if e.code in (403, 404):   # not-found / access-denied (e.g. POWO) — cache the miss, stay quiet
                _cache[url] = None
                return None
            break
        except Exception as e:
            last = e
            time.sleep(1.0 * (attempt + 1))
    sys.stderr.write(f"  ! http_json failed: {url} ({last})\n")
    return None


# ---------------------------------------------------------------- text helpers
def nfc(s):
    return unicodedata.normalize("NFC", s or "")


def norm(s):
    return re.sub(r"\s+", " ", nfc(str(s)).replace(" ", " ")).strip()


def normkey(s):
    return norm(s).casefold()


def dataset_slug(source):
    s = re.sub(r"[^a-z0-9]+", "-", (source or "gbif").lower()).strip("-")
    return (s or "gbif")[:40]


def strip_disambig(title):
    # Wikipedia titles: drop a trailing " (…)" disambiguation and underscores.
    return norm(re.sub(r"\s*\([^()]*\)\s*$", "", str(title).replace("_", " ")))


# ---------------------------------------------------------------- language maps
def load_langs():
    langs = yaml.safe_load(open(os.path.join(VOCAB, "languages.yaml"), encoding="utf-8"))
    enabled, order, iso_to_code = [], [], {}
    for x in langs:
        if not x.get("enabled"):
            continue
        code = x["code"]
        enabled.append(code)
        order.append(code)
        iso_to_code[code.lower()] = code
        iso_to_code[str(x.get("iso3", "")).lower()] = code
        for a in x.get("iso3_alt", []) or []:
            iso_to_code[str(a).lower()] = code
    # Wikidata / Wikipedia sublanguage codes that fold onto an enabled code.
    for sub, base in {"nb": "no", "nn": "no", "nob": "no", "nno": "no",
                      "sr-el": "sr", "sr-ec": "sr", "be-tarask": "be", "pt-br": "pt"}.items():
        if base in enabled:
            iso_to_code[sub] = base
    iso_to_code.pop("", None)
    return set(enabled), order, iso_to_code


# ---------------------------------------------------------------- GBIF
def gbif_match(sci, refresh=False):
    url = "https://api.gbif.org/v1/species/match?" + urllib.parse.urlencode({"name": sci, "strict": "true"})
    d = http_json(url, refresh=refresh)
    if d and d.get("matchType") not in (None, "NONE") and d.get("usageKey"):
        return d
    # relax strictness on failure
    url2 = "https://api.gbif.org/v1/species/match?" + urllib.parse.urlencode({"name": sci})
    d2 = http_json(url2, refresh=refresh)
    if d2 and d2.get("usageKey") and d2.get("matchType") not in (None, "NONE"):
        return d2
    return None


def gbif_vernaculars(key, refresh=False):
    out, offset = [], 0
    while True:
        url = f"https://api.gbif.org/v1/species/{key}/vernacularNames?" + urllib.parse.urlencode(
            {"limit": 500, "offset": offset})
        d = http_json(url, refresh=refresh)
        if not d:
            break
        out.extend(d.get("results", []))
        if d.get("endOfRecords") or offset > 4000:
            break
        offset += 500
    return out


# ---------------------------------------------------------------- Wikidata
def wikidata_qid(sci, synonyms, refresh=False):
    names = [sci] + list(synonyms or [])
    for nm in names:
        q = 'SELECT ?item WHERE { ?item wdt:P225 "%s". } LIMIT 3' % nm.replace('"', '\\"')
        url = "https://query.wikidata.org/sparql?" + urllib.parse.urlencode({"format": "json", "query": q})
        d = http_json(url, headers={"Accept": "application/sparql-results+json"}, refresh=refresh)
        try:
            b = d["results"]["bindings"]
            if b:
                return b[0]["item"]["value"].rsplit("/", 1)[-1]
        except Exception:
            pass
    return None


def wikidata_names(qid, iso_to_code, refresh=False):
    """Return (p1843[list of (code,text)], sitelinks[list of (code,title)])."""
    url = ("https://www.wikidata.org/w/api.php?" + urllib.parse.urlencode(
        {"action": "wbgetentities", "ids": qid, "props": "claims|sitelinks", "format": "json"}))
    d = http_json(url, refresh=refresh)
    p1843, sites = [], []
    try:
        ent = d["entities"][qid]
    except Exception:
        return p1843, sites
    for cl in ent.get("claims", {}).get("P1843", []):
        try:
            dv = cl["mainsnak"]["datavalue"]["value"]
            lang = iso_to_code.get(str(dv.get("language", "")).lower())
            if lang:
                p1843.append((lang, dv.get("text", "")))
        except Exception:
            continue
    for sk, sv in ent.get("sitelinks", {}).items():
        if not sk.endswith("wiki"):
            continue
        wl = sk[:-4]                        # 'dewiki' -> 'de'
        lang = iso_to_code.get(wl.lower())
        if lang:
            sites.append((lang, sv.get("title", "")))
    return p1843, sites


# ---------------------------------------------------------------- EPPO (optional)
def eppo_names(sci, refresh=False):
    if not EPPO_TOKEN:
        return []
    su = "https://data.eppo.int/api/rest/1.0/tools/search?" + urllib.parse.urlencode(
        {"authtoken": EPPO_TOKEN, "kw": sci, "searchfor": 3, "searchmode": 3, "typeorg": 1})
    hits = http_json(su, refresh=refresh) or []
    if not isinstance(hits, list) or not hits:
        return []
    code = hits[0].get("eppocode")
    if not code:
        return []
    nu = f"https://data.eppo.int/api/rest/1.0/taxon/{code}/names?" + urllib.parse.urlencode({"authtoken": EPPO_TOKEN})
    rows = http_json(nu, refresh=refresh) or []
    out = []
    for r in rows if isinstance(rows, list) else []:
        lang3 = str(r.get("isolang", "")).lower()
        nm = r.get("fullname") or r.get("preferred_name")
        if lang3 and nm:
            out.append((lang3, nm, code))
    return out


# ---------------------------------------------------------------- POWO id (anchor only)
def powo_id(sci, refresh=False):
    url = "https://powo.science.kew.org/api/2/search?" + urllib.parse.urlencode({"q": sci, "perPage": 5})
    # POWO/Kew often blocks server-side API calls (403) or is unreachable; it is an
    # anchor-only nicety (GBIF + Wikidata already anchor identity), so fail fast.
    d = http_json(url, headers={"Accept": "application/json"}, refresh=refresh, tries=1)
    try:
        for res in d.get("results", []):
            if res.get("accepted") and normkey(res.get("name", "")) == normkey(sci):
                return res.get("fqId") or res.get("url")
        if d.get("results"):
            return d["results"][0].get("fqId") or d["results"][0].get("url")
    except Exception:
        pass
    return None


# ---------------------------------------------------------------- core harvest
def source_token(provider, dataset=""):
    if provider == "gbif":
        if CURATED_POWO_RE.search(dataset or ""):
            return "powo:wcvp"
        if CURATED_COL_RE.search(dataset or ""):
            return "col:" + dataset_slug(dataset)
        slug = dataset_slug(dataset)
        return "gbif:" + ("backbone" if slug in ("", "gbif") else slug)
    return provider


def harvest(plant, langset, iso_to_code, refresh=False):
    sci = plant["scientific_name"]
    synonyms = plant.get("synonyms", [])
    ids, queried = {}, []
    # cand[lang][normkey] = {"display": Counter-ish, "sources": set(), "wiki": bool}
    cand = {}

    def add(lang, raw, token, is_wiki=False):
        nm = strip_disambig(raw) if is_wiki else norm(raw)
        if not nm or len(nm) < 2:
            return
        if normkey(nm) in {normkey(sci)} | {normkey(s) for s in synonyms}:
            return                       # skip the Latin binomial itself
        if re.search(r"\d", nm) or "×" in nm:
            return
        d = cand.setdefault(lang, {}).setdefault(normkey(nm), {"forms": {}, "sources": set()})
        d["forms"][nm] = d["forms"].get(nm, 0) + 1
        d["sources"].add(token)

    # -- GBIF --
    m = gbif_match(sci, refresh=refresh)
    if m:
        ids["gbif"] = m["usageKey"]
        queried.append("gbif")
        for v in gbif_vernaculars(m["usageKey"], refresh=refresh):
            lang = iso_to_code.get(str(v.get("language", "")).lower())
            if lang and lang in langset and v.get("vernacularName"):
                add(lang, v["vernacularName"], source_token("gbif", v.get("source", "")))

    # -- Wikidata + Wikipedia --
    qid = wikidata_qid(sci, synonyms, refresh=refresh)
    if qid:
        ids["wikidata"] = qid
        queried.append("wikidata")
        p1843, sites = wikidata_names(qid, iso_to_code, refresh=refresh)
        for lang, txt in p1843:
            if lang in langset:
                add(lang, txt, "wikidata:" + qid)
        queried.append("wikipedia")
        for lang, title in sites:
            if lang in langset:
                add(lang, title, "wikipedia:" + lang, is_wiki=True)

    # -- EPPO (optional) --
    for lang3, nm, code in eppo_names(sci, refresh=refresh):
        lang = iso_to_code.get(lang3)
        if lang and lang in langset:
            add(lang, nm, "eppo:" + code)
            if "eppo" not in queried:
                queried.append("eppo")

    # -- POWO id anchor --
    pid = powo_id(sci, refresh=refresh)
    if pid:
        ids["powo"] = pid
        if "powo" not in queried:
            queried.append("powo")

    return ids, cand, queried


def is_curated(sources):
    return any(s.startswith(("eppo:", "powo:", "col:")) for s in sources)


def build_names(cand, order, common_names):
    """Apply the strict accept rule and pick a preferred name per language.

    Preferred pick prioritises, in order: (1) a name the editor already listed in the
    plant's curated common_names (by their order — so common_names[0] wins, and the
    editor's casing is used); (2) the Wikipedia article title for that language; (3) a
    curated-authority source; (4) most independent sources; then shorter / alphabetical.
    """
    cn_index = {}
    for i, cn in enumerate(common_names or []):
        cn_index.setdefault(normkey(cn), (i, norm(cn)))
    names = {}
    for lang in order:
        entries = cand.get(lang)
        if not entries:
            continue
        rows = []
        for nk, d in entries.items():
            sources = sorted(d["sources"])
            # best display casing: most frequent raw form (ties -> longer, then alpha)
            display = sorted(d["forms"].items(), key=lambda kv: (-kv[1], -len(kv[0]), kv[0]))[0][0]
            ci = cn_index.get(nk)
            if ci is not None:
                display = ci[1]                       # editor's canonical casing wins
            curated = is_curated(sources)
            has_wiki = any(s.startswith("wikipedia:") for s in sources)
            verified = curated or len(sources) >= 2
            rows.append({"name": display, "sources": sources,
                         "status": "verified" if verified else "needs-review",
                         "_curated": curated, "_n": len(sources), "_wiki": has_wiki,
                         "_cn": ci[0] if ci else 999})
        rank = lambda r: (r["_cn"], not r["_wiki"], not r["_curated"], -r["_n"],
                          len(r["name"]), r["name"].casefold())
        vrows = [r for r in rows if r["status"] == "verified"]
        if vrows:
            sorted(vrows, key=rank)[0]["preferred"] = True
        # deterministic output order: preferred, then verified by strength, then review
        rows.sort(key=lambda r: (r["status"] != "verified", not r.get("preferred", False)) + rank(r))
        out = []
        for r in rows:
            e = {"name": r["name"]}
            if r.get("preferred"):
                e["preferred"] = True
            e["sources"] = r["sources"]
            if r["status"] != "verified":
                e["status"] = "needs-review"
            out.append(e)
        names[lang] = out
    return names


# ---------------------------------------------------------------- writers
def yaml_scalar(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, int):
        return str(v)
    s = str(v)
    if re.match(r"^[A-Za-z0-9_.-]+$", s):
        return s
    return "'" + s.replace("'", "''") + "'"


ID_ORDER = ("gbif", "powo", "wikidata", "usda", "ncbi_taxon")


def set_external_ids(path, new_ids):
    """Surgically insert/refresh a top-level external_ids: block. Minimal diff. Returns bool changed."""
    text = open(path, encoding="utf-8").read()
    doc = yaml.safe_load(text)
    cur = dict(doc.get("external_ids") or {})
    merged = dict(cur)
    for k, v in new_ids.items():
        if v not in (None, ""):
            merged[k] = v
    if merged == cur:
        return False
    lines = text.split("\n")
    # 1) drop any existing top-level external_ids block
    stripped, i, n = [], 0, len(lines)
    while i < n:
        if re.match(r"^external_ids:", lines[i]):
            i += 1
            while i < n and (lines[i][:1] in (" ", "\t")) and lines[i].strip():
                i += 1
            continue
        stripped.append(lines[i])
        i += 1
    # 2) build fresh block
    block = ["external_ids:"]
    for k in ID_ORDER:
        if k in merged:
            block.append(f"  {k}: {yaml_scalar(merged[k])}")
    # 3) insert right after the top-level family: line (fallback: scientific_name:)
    res, done = [], False
    for line in stripped:
        res.append(line)
        if not done and re.match(r"^family:", line):
            res.extend(block)
            done = True
    if not done:
        res2 = []
        for line in res:
            res2.append(line)
            if not done and re.match(r"^scientific_name:", line):
                res2.extend(block)
                done = True
        res = res2
    open(path, "w", encoding="utf-8", newline="\n").write("\n".join(res))
    return True


def write_names_file(pid, sci, names, checked, queried):
    doc = {
        "id": pid,
        "scientific_name": sci,
        "names": names,
        "verification": {
            "checked_languages": checked,
            "sources_queried": sorted(set(queried)),
            "last_run": TODAY,
        },
        "last_verified": TODAY,
    }
    txt = yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=100)
    os.makedirs(NAMESDIR, exist_ok=True)
    open(os.path.join(NAMESDIR, pid + ".yaml"), "w", encoding="utf-8", newline="\n").write(txt)


# ---------------------------------------------------------------- main
def main():
    args = sys.argv[1:]
    refresh = "--refresh" in args
    no_anchor = "--no-anchor" in args
    ids_arg = [a for a in args if not a.startswith("--")]

    langset, order, iso_to_code = load_langs()
    load_cache()

    files = sorted(glob.glob(os.path.join(PLANTS, "*.yaml")))
    plants = [yaml.safe_load(open(f, encoding="utf-8")) for f in files]
    by_id = {p["id"]: (p, f) for p, f in zip(plants, files)}
    todo = ids_arg if ids_arg else [p["id"] for p in plants]

    tot_v = tot_r = tot_anchor = 0
    for k, pid in enumerate(todo, 1):
        if pid not in by_id:
            sys.stderr.write(f"[{k}/{len(todo)}] unknown id: {pid}\n")
            continue
        plant, path = by_id[pid]
        sci = plant["scientific_name"]
        ids, cand, queried = harvest(plant, langset, iso_to_code, refresh=refresh)
        names = build_names(cand, order, plant.get("common_names", []))
        nv = sum(1 for lang in names for e in names[lang] if e.get("status") != "needs-review")
        nr = sum(1 for lang in names for e in names[lang] if e.get("status") == "needs-review")
        # keep only languages that ended up with >=1 entry; publish set = verified
        pub = {lang: [e for e in es] for lang, es in names.items() if es}
        langs_with_verified = sum(1 for lang in pub if any(e.get("status") != "needs-review" for e in pub[lang]))
        write_names_file(pid, sci, pub, order, queried)
        changed = False
        if not no_anchor and ids:
            changed = set_external_ids(path, ids)
        tot_v += nv
        tot_r += nr
        tot_anchor += 1 if changed else 0
        save_cache()
        print(f"[{k}/{len(todo)}] {pid:32s} gbif={ids.get('gbif','-')!s:>9} wd={ids.get('wikidata','-'):>9} "
              f"| {langs_with_verified:2d} langs verified, {nv:3d} names (+{nr} review){' [anchored]' if changed else ''}")

    save_cache()
    print(f"\nDone: {len(todo)} plants | {tot_v} verified names | {tot_r} held for review | {tot_anchor} anchors written")


if __name__ == "__main__":
    main()
