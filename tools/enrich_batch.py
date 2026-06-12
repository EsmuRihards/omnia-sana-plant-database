#!/usr/bin/env python3
"""
enrich_batch.py — fill out a batch of skeleton plant records from researched data.

Reads a batch JSON file describing fully-researched plant records (parts, actions,
constituents, contraindications) plus their references, then:
  - adds each reference to bibliography.bibtex (dedupe by DOI/citation, new REF ids),
  - overwrites the skeleton plants/*.yaml with the complete record.

Schema/architecture is unchanged; this only fills empty fields and upgrades status.

Batch JSON shape (list of plant objects):
[
  {
    "file": "agrimonia_eupatoria.yaml",
    "common_names": ["Agrimony", ...],
    "scientific_name": "Agrimonia eupatoria",
    "family": "Rosaceae",
    "references": {
      "<localkey>": {"type":"article|misc", "author":"...", "year":"2022",
                     "title":"...", "journal":"...", "doi":"...", "url":"..."},
      ...
    },
    "parts_used": [
      {"name":"Aerial parts", "actions":[
        {"action":"Astringent", "refs":["<localkey>", ...], "status":"verified"}]}],
    "constituents": [{"name":"Tannins", "note":"...", "refs":["<localkey>"]}],
    "contraindications": [{"note":"...", "refs":["<localkey>"], "status":"verified"}],
    "internal_notes": "...",
    "status": "verified"
  }, ...
]

Usage:  python tools/enrich_batch.py tools/sources/batch01.json
"""

import os
import re
import sys
import json
import unicodedata

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PLANTS_DIR = os.path.join(ROOT, "plants")
BIBLIO = os.path.join(ROOT, "bibliography.bibtex")
LAST_UPDATED = "2026-06-12"

STOP = {"the", "and", "for", "with", "from", "review", "study", "a", "an", "of",
        "its", "on", "in", "to", "as", "potential", "effects", "role"}


def ascii_fold(s):
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def esc(s):
    return s.replace("{", "(").replace("}", ")").replace("\\", "/")


def load_bib():
    text = open(BIBLIO, encoding="utf-8").read()
    cut = text.find("@")
    header, body = (text[:cut], text[cut:]) if cut != -1 else (text, "")
    entries, doi_idx, annote_idx = {}, {}, {}
    maxid = 0
    for blk in re.split(r"(?m)^(?=@)", body):
        blk = blk.strip()
        if not blk:
            continue
        km = re.match(r"@\w+\s*\{\s*([^,\s]+)", blk)
        key = km.group(1) if km else f"~u{len(entries)}"
        entries[key] = blk
        rid = re.search(r"REF-(\d+)", blk)
        rids = rid.group(0) if rid else None
        if rid:
            maxid = max(maxid, int(rid.group(1)))
        dm = re.search(r"doi\s*=\s*\{([^}]+)\}", blk)
        if dm and rids:
            doi_idx[dm.group(1).strip().lower()] = rids
        am = re.search(r"annote\s*=\s*\{(.+?)\}\s*\n\}", blk, re.DOTALL)
        if am and rids:
            annote_idx[re.sub(r"\s+", " ", am.group(1)).strip().lower()] = rids
    return header, entries, doi_idx, annote_idx, maxid


def main():
    batch_path = sys.argv[1]
    batch = json.load(open(batch_path, encoding="utf-8"))
    header, entries, doi_idx, annote_idx, maxid = load_bib()
    nextid = maxid + 1
    used_keys = set(entries)

    def make_key(author, year, title):
        sm = re.search(r"[A-Za-z]+", ascii_fold(author))
        surname = sm.group(0).lower() if sm else "anon"
        kw = ""
        for w in re.findall(r"[A-Za-z]{4,}", ascii_fold(title)):
            if w.lower() not in STOP:
                kw = w.lower()
                break
        base = re.sub(r"[^a-z0-9]", "", f"{surname}{year}{kw}") or surname
        key, n = base, 2
        while key in used_keys:
            key = f"{base}{n}"
            n += 1
        used_keys.add(key)
        return key

    def add_ref(r):
        nonlocal nextid
        author = r.get("author", "").strip()
        year = str(r.get("year", "n.d."))
        title = r.get("title", "").strip()
        journal = r.get("journal", "").strip()
        doi = r.get("doi", "").strip()
        url = r.get("url", "").strip()
        annote = r.get("annote", "").strip()
        if not annote:
            annote = f"{author} ({year}) {title}."
            if journal:
                annote += f" {journal}."
            if doi:
                annote += f" doi:{doi}."
            elif url:
                annote += f" Available at: {url}."
        # dedupe
        if doi and doi.lower() in doi_idx:
            return doi_idx[doi.lower()]
        sig = re.sub(r"\s+", " ", annote).strip().lower()
        if sig in annote_idx:
            return annote_idx[sig]
        typ = r.get("type") or ("article" if (doi or journal) else "misc")
        key = make_key(author or title or "anon", year, title or journal or "ref")
        rid = f"REF-{nextid:04d}"
        nextid += 1
        lines = []
        if author:
            lines.append(f"  author  = {{{esc(author)}}}")
        if title:
            lines.append(f"  title   = {{{esc(title)}}}")
        if journal:
            lines.append(f"  journal = {{{esc(journal)}}}")
        lines.append(f"  note    = {{{rid}}}")
        if year:
            lines.append(f"  year    = {{{esc(year)}}}")
        if doi:
            lines.append(f"  doi     = {{{esc(doi)}}}")
        if url:
            lines.append(f"  url     = {{{esc(url)}}}")
        lines.append(f"  annote  = {{{esc(annote)}}}")
        entries[key] = f"@{typ}{{{key},\n" + ",\n".join(lines) + "\n}"
        if doi:
            doi_idx[doi.lower()] = rid
        annote_idx[sig] = rid
        return rid

    written = []
    for p in batch:
        local = {k: add_ref(v) for k, v in p["references"].items()}

        def ids(keys):
            out = []
            for k in keys:
                if k not in local:
                    raise KeyError(f'{p["file"]}: unknown ref key {k!r}')
                if local[k] not in out:
                    out.append(local[k])
            return out

        parts = []
        for part in p["parts_used"]:
            acts = [{"action": a["action"], "reference_ids": ids(a["refs"]),
                     "status": a.get("status", "verified")} for a in part["actions"]]
            parts.append({"name": part["name"], "medicinal_actions": acts})
        cons = [{"name": c["name"], "note": c.get("note", ""), "reference_ids": ids(c["refs"])}
                for c in p.get("constituents", [])]
        contra = [{"note": c["note"], "reference_ids": ids(c["refs"]),
                   "status": c.get("status", "verified")} for c in p.get("contraindications", [])]
        rec = {
            "common_names": p["common_names"],
            "scientific_name": p["scientific_name"],
            "family": p["family"],
            "parts_used": parts,
            "constituents": cons,
            "contraindications": contra,
            "internal_notes": p.get("internal_notes", ""),
            "last_updated": LAST_UPDATED,
            "status": p.get("status", "verified"),
        }
        with open(os.path.join(PLANTS_DIR, p["file"]), "w", encoding="utf-8") as fh:
            yaml.safe_dump(rec, fh, sort_keys=False, allow_unicode=True,
                           default_flow_style=False, width=100)
        written.append(p["file"])

    ordered = [entries[k] for k in sorted(entries, key=str.lower)]
    with open(BIBLIO, "w", encoding="utf-8") as fh:
        fh.write(header.rstrip() + "\n\n" + "\n\n".join(ordered) + "\n")

    print(f"Enriched {len(written)} plant(s): {', '.join(written)}")
    print(f"Bibliography now has REF ids up to REF-{nextid-1:04d} ({len(entries)} entries)")


if __name__ == "__main__":
    main()
