"""List the BAFU-2026 datasets exported as ecoSpold "system terminated" (type=2).

In the EcoSpold01 schema, ``dataSetInformation@type`` says what a dataset holds:
1 = unit process (direct flows + links to suppliers), 2 = system terminated, i.e. the
cumulative elementary flows of the whole upstream chain - the LCI result. The type-2
datasets are the explicitly aggregated ones we want to rebuild as unit processes.
Schema documentation: https://github.com/brightway-lca/pyecospold/blob/main/pyecospold/schemas/v1/EcoSpold01MetaInformation.xsd#L26-L60

The flag is read from the raw XML because the Sentier import drops it. The dataset UUID in
the file name is the activity code in Brightway, so each hit is joined with the installed
database to add how it is used there (inputs, elementary flows, consuming processes).
Flagged datasets without a single exchange (empty placeholders) are dropped: there is
nothing to disaggregate.

Usage:
    uv run python scripts/list_system_terminated.py [--ecospold data/ecospold]
        [--project bafu-2026] [--out results/system_terminated.csv]
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path


# Data-origin families, from the source citation in the XML. The order matters: first match wins.
FAMILIES = [
    ("plasticseurope", re.compile(r"PlasticsEurope", re.I)),
    ("ecoinvent-v2-confidential", re.compile(r"Swiss Centre for LCI", re.I)),
    ("treeze-kbob", re.compile(r"treeze", re.I)),
    ("french-biobased", re.compile(r"Rapport méthodologique", re.I)),
    ("kbob-manufacturer", re.compile(r"Created for EcoSpold 1 compatibility", re.I)),
]


def family_of(source: str) -> str:
    for name, rx in FAMILIES:
        if rx.search(source):
            return name
    return "other"


def _norm(name: str) -> str:
    """Drop the "xx " obsolete prefix and numeric parameters (U=1.0 vs U=1.2 is the same product).
    Exact match after that - fuzzy matching confuses ethylene with diethylene glycol."""
    return re.sub(r"\d+(\.\d+)?", "#", re.sub(r"^x+ ", "", name).lower())


def unit_sibling(name: str, unit_names: dict[str, str]) -> str:
    """A type-1 dataset with technosphere inputs of the same product: a free template."""
    return unit_names.get(_norm(name), "")


def read_flagged(folder: Path) -> dict[str, dict]:
    """Every dataset with type=2, keyed by UUID, with the source report it cites."""
    files = sorted(folder.glob("process_*.xml"))
    if not files:
        sys.exit(f"no process_*.xml in {folder.resolve()} - unzip the BAFU zip there first")
    flagged = {}
    unit_names: dict[str, str] = {}  # normalised -> original, type-1 datasets with inputs
    for i, f in enumerate(files, 1):
        if i % 2000 == 0:
            print(f"  {i}/{len(files)}", file=sys.stderr)
        ds = ET.parse(f).getroot().find("dataset")
        pi = ds.find("metaInformation/processInformation")
        exchanges = ds.find("flowData").findall("exchange")
        if pi.find("dataSetInformation").get("type") != "2":
            if any(e.findtext("inputGroup") == "5" for e in exchanges):
                name = pi.find("referenceFunction").get("name", "")
                unit_names[_norm(name)] = name
            continue
        # the reference product is listed as an exchange too, so 1 means "empty"
        if len(exchanges) <= 1:
            print(f"  skipping empty dataset {f.name}", file=sys.stderr)
            continue
        rf = pi.find("referenceFunction")
        mv = ds.find("metaInformation/modellingAndValidation")
        ai = ds.find("metaInformation/administrativeInformation")
        srcs = mv.findall("source")
        persons = {x.get("number"): x for x in ai.findall("person")}
        rep = mv.find("representativeness")
        tp = pi.find("timePeriod")

        def who(number: str | None) -> str:
            """'Name [company/country]' - the address/email fields are anonymised in the export."""
            x = persons.get(number)
            if x is None:
                return ""
            return f"{x.get('name', '')} [{x.get('companyCode') or '?'}/{x.get('countryCode') or '?'}]"

        def cite(src) -> str:
            return " | ".join(x for x in (src.get("publisher"), src.get("year"), src.get("title")) if x)

        flagged[f.stem[len("process_"):]] = {
            "code": f.stem[len("process_"):],
            "name": rf.get("name", ""),
            "location": pi.find("geography").get("location", ""),
            "unit": rf.get("unit", ""),
            "bafu_category": f"{rf.get('category', '')} / {rf.get('subCategory', '')}",
            "generator": ds.get("generator", ""),
            "source": cite(srcs[0]) if srcs else "",
            "source_2": cite(srcs[1]) if len(srcs) > 1 else "",
            # the people behind the dataset: who to ask for the report or the confidential annex
            "data_entry": who(ai.find("dataEntryBy").get("person")),
            "data_generator": who(ai.find("dataGeneratorAndPublication").get("person")),
            "validator": who(mv.find("validation").get("proofReadingValidator")),
            "sampling_procedure": (rep.get("samplingProcedure") or "") if rep is not None else "",
            "representativeness_pct": (rep.get("percent") or "") if rep is not None else "",
            "time_period": f"{tp.findtext('startDate') or tp.findtext('startYear') or ''}-{tp.findtext('endDate') or tp.findtext('endYear') or ''}" if tp is not None else "",
        }
    for row in flagged.values():
        row["family"] = family_of(row["source"])
        row["unit_sibling"] = unit_sibling(row["name"], unit_names)
    return flagged


def add_brightway_usage(flagged: dict[str, dict], project: str, database: str) -> None:
    """Inputs, elementary flows and consumer counts from the installed database."""
    import bw2data as bd

    if project not in bd.projects:
        print(f"Brightway project {project!r} not found - usage columns left empty", file=sys.stderr)
        return
    bd.projects.set_current(project)
    acts = bd.Database(database).load()  # one bulk read instead of one query per activity
    used_by: Counter = Counter()
    for key, act in acts.items():
        for exc in act.get("exchanges", []):
            if exc.get("type") == "technosphere" and tuple(exc["input"]) != key:
                used_by[exc["input"][1]] += 1
    for code, row in flagged.items():
        act = acts.get((database, code))
        if act is None:
            continue
        kinds = Counter(e.get("type") for e in act.get("exchanges", []))
        row["n_technosphere_inputs"] = kinds["technosphere"]
        row["n_elementary_flows"] = kinds["biosphere"]
        row["n_used_by"] = used_by[code]


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--ecospold", default="data/ecospold", help="unzipped BAFU XML folder")
    p.add_argument("--project", default="bafu-2026", help="Brightway project with the BAFU import")
    p.add_argument("--database", default="bafu-2026")
    p.add_argument("--out", default="results/system_terminated.csv")
    args = p.parse_args()

    print(f"reading {args.ecospold}", file=sys.stderr)
    flagged = read_flagged(Path(args.ecospold))
    add_brightway_usage(flagged, args.project, args.database)

    fields = [
        "family", "code", "name", "location", "unit", "bafu_category",
        "n_technosphere_inputs", "n_elementary_flows", "n_used_by", "unit_sibling", "generator",
        "source", "source_2", "data_entry", "data_generator", "validator",
        "sampling_procedure", "representativeness_pct", "time_period",
    ]
    rows = sorted(flagged.values(), key=lambda r: (-r.get("n_used_by", 0), r["name"]))
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, restval="")
        w.writeheader()
        w.writerows(rows)

    print(f"\n{len(rows)} system-terminated (type=2) datasets -> {out}\n")
    print("by family (n, consuming processes, with a unit-process sibling in BAFU):")
    for fam in [f for f, _ in FAMILIES] + ["other"]:
        sub = [r for r in rows if r["family"] == fam]
        if sub:
            print(f"  {fam:28s} {len(sub):3d}  used={sum(r.get('n_used_by', 0) for r in sub):5d}  siblings={sum(bool(r['unit_sibling']) for r in sub)}")
    by_src = Counter(r["source"][:70] for r in rows)
    print("\nby source report:")
    print("\nby data generator (who to ask):")
    for who_, n in Counter(r["data_generator"] for r in rows).most_common(8):
        print(f"  {n:3d}  {who_ or '(none)'}")
    for src, n in by_src.most_common():
        print(f"  {n:3d}  {src or '(none)'}")
    print(f"\n{'used':>5s} {'inputs':>6s} {'flows':>6s}  name")
    for r in rows[:25]:
        print(f"{r.get('n_used_by', ''):>5} {r.get('n_technosphere_inputs', ''):>6} {r.get('n_elementary_flows', ''):>6}  {r['name'][:70]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
