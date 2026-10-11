"""Catalogue the literature behind the BAFU-2026 datasets from the ecoSpold metadata.

Every ecoSpold dataset cites one ``source`` (report, article, company data) in
``modellingAndValidation/source`` with author, year, title, publisher and a free-text citation.
Some comments additionally embed DOIs. This script writes two catalogues:

    results/sources.csv   one row per distinct source: citation, type, how many datasets cite
                          it, how many of those are "system terminated" (type=2)
    results/dois.csv      one row per distinct DOI found in comments, with the datasets citing it

The official BAFU documentation bundle ships the reports as PDFs named after the same
``source.title`` (``2007 - LCI detergents - Zah.pdf``); with ``--reports`` pointing at that folder
each source gets a ``pdf`` column.

Usage:
    uv run python scripts/list_sources.py [--ecospold data/ecospold] [--out-dir results]
        [--reports "BAFU-2026 v1_Documentation/BAFU-2026 v1_Documentation/BAFU-2026 v1 LCI Reports"]
"""

from __future__ import annotations

import argparse
import csv
import difflib
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

# ecoSpold01 sourceType codes (EcoSpold01MetaInformation.xsd, spoldID 305)
SOURCE_TYPES = {
    "0": "undefined", "1": "article", "2": "chapter in anthology", "3": "separate publication",
    "4": "measurement on site", "5": "oral communication", "6": "personal written communication",
    "7": "questionnaire",
}
DOI_RX = re.compile(r"\b(10\.\d{4,9}/[^\s\"'<>;,)]+)")
EMPTY = {None, "", "-", "0", "na", "<null>", "none", "nan", "unknown", "Unknown", "Unspecified"}


def clean(v: str | None) -> str:
    return "" if v in EMPTY else v.replace("\\n", " ").strip()


def _key(title: str) -> str:
    ascii_ = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", ascii_.lower())


def match_pdfs(sources: dict[str, dict], reports: Path | None) -> None:
    """Attach the report PDF whose file name equals the source title (a few titles are
    abbreviated in the XML, e.g. "exp." for "expansion", so fall back to a close match that
    keeps year and author)."""
    if reports is None or not reports.is_dir():
        return
    pdfs = {_key(f.stem): f.name for f in reports.glob("*.pdf")}
    for row in sources.values():
        k = _key(row["title"])
        hit = pdfs.get(k)
        if not hit:
            close = difflib.get_close_matches(k, pdfs, n=1, cutoff=0.85)
            if close and close[0][:4] == k[:4] and close[0][-6:] == k[-6:]:  # same year, same author
                hit = pdfs[close[0]]
        row["pdf"] = hit or ""


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--ecospold", default="data/ecospold")
    p.add_argument("--out-dir", default="results")
    p.add_argument("--reports", default="BAFU-2026 v1_Documentation/BAFU-2026 v1_Documentation/BAFU-2026 v1 LCI Reports",
                   help="folder with the BAFU LCI report PDFs (optional)")
    args = p.parse_args()

    files = sorted(Path(args.ecospold).glob("process_*.xml"))
    if not files:
        sys.exit(f"no process_*.xml in {args.ecospold}")
    sources: dict[str, dict] = {}
    dois: dict[str, dict] = defaultdict(lambda: {"datasets": [], "categories": set()})
    for i, f in enumerate(files, 1):
        if i % 2000 == 0:
            print(f"  {i}/{len(files)}", file=sys.stderr)
        ds = ET.parse(f).getroot().find("dataset")
        pi = ds.find("metaInformation/processInformation")
        rf = pi.find("referenceFunction")
        name, cat = rf.get("name", ""), rf.get("category", "")
        is_t2 = pi.find("dataSetInformation").get("type") == "2"
        for src in ds.findall("metaInformation/modellingAndValidation/source"):  # some cite two
            key = src.get("number", "")
            row = sources.setdefault(key, {
                "source_number": key,
                "citation": clean(src.get("text")) or " ".join(
                    x for x in (clean(src.get("firstAuthor")), clean(src.get("year")), clean(src.get("title"))) if x),
                "first_author": clean(src.get("firstAuthor")), "year": clean(src.get("year")),
                "title": clean(src.get("title")), "publisher": clean(src.get("publisher")),
                "anthology": clean(src.get("titleOfAnthology")), "volume": clean(src.get("volumeNo")),
                "source_type": SOURCE_TYPES.get(src.get("sourceType", "0"), src.get("sourceType", "")),
                "n_datasets": 0, "n_system_terminated": 0, "categories": set(), "example_dataset": name,
            })
            row["n_datasets"] += 1
            row["n_system_terminated"] += is_t2
            row["categories"].add(cat)
        blob = " ".join(v for e in ds.iter() for v in e.attrib.values())
        for doi in set(DOI_RX.findall(blob)):
            doi = doi.rstrip(".").lower()  # DOIs are case-insensitive
            dois[doi]["datasets"].append(name)
            dois[doi]["categories"].add(cat)

    match_pdfs(sources, Path(args.reports) if args.reports else None)
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    rows = sorted(sources.values(), key=lambda r: (-r["n_system_terminated"], -r["n_datasets"]))
    with (out / "sources.csv").open("w", newline="") as fh:
        fields = ["source_number", "n_datasets", "n_system_terminated", "year", "first_author", "title", "pdf",
                  "publisher", "anthology", "volume", "source_type", "categories", "example_dataset", "citation"]
        w = csv.DictWriter(fh, fieldnames=fields, restval="")
        w.writeheader()
        for r in rows:
            w.writerow({**r, "categories": "; ".join(sorted(r["categories"]))})
    with (out / "dois.csv").open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["doi", "url", "n_datasets", "categories", "example_datasets"])
        for doi, d in sorted(dois.items(), key=lambda kv: -len(kv[1]["datasets"])):
            w.writerow([doi, f"https://doi.org/{doi}", len(d["datasets"]),
                        "; ".join(sorted(d["categories"])), " | ".join(sorted(set(d["datasets"]))[:3])])

    with_pdf = sum(1 for r in rows if r.get("pdf"))
    print(f"\n{len(rows)} distinct sources -> {out / 'sources.csv'}  ({with_pdf} with a report PDF, "
          f"covering {sum(r['n_datasets'] for r in rows if r.get('pdf'))} datasets)")
    print(f"{len(dois)} distinct DOIs -> {out / 'dois.csv'}\n")
    print(f"{'datasets':>8s} {'t2':>4s}  {'year':4s}  {'type':22s} title")
    for r in rows[:30]:
        print(f"{r['n_datasets']:8d} {r['n_system_terminated']:4d}  {r['year']:4s}  {r['source_type'][:22]:22s} {r['title'][:60]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
