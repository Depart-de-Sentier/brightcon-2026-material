"""Who inside BAFU-2026 consumes the system processes?

    uv run python scripts/ecoprofile_consumers.py [--project bafu-2026]

The ecoSpold ``type=2`` flag finds 101 system processes; ``scripts/find_system_processes.py``
finds 37 more by structure (the APME / PlasticsEurope eco-profiles). This script answers the
question that decides how much the second set matters: how deep in the database are they?

Counted on BAFU-2026: 466 datasets consume at least one of the 37, against 936 for the 101. The
unflagged ones are not only at the top of a survey - ordinary unit processes terminate on them
(``Ethyl benzene, at plant`` -> ``Benzene, at plant``; ``Cumene, at plant`` -> benzene and
propylene; ``Glass fibre, at plant`` -> ``Nylon 6, at plant``).
"""
from __future__ import annotations

import argparse
import csv
import warnings
from collections import defaultdict
from pathlib import Path

warnings.filterwarnings("ignore")

import bw2data as bd  # noqa: E402

from reverse_bafu import db  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--project", default="bafu-2026")
    ap.add_argument("--datasets", default="results/system_terminated_extended.csv")
    a = ap.parse_args()
    db.set_project(a.project)
    rows = list(csv.DictReader(open(a.datasets)))
    struct = {r["code"]: r["name"] for r in rows if r["detected_by"] == "structure"}
    flag = {r["code"]: r["name"] for r in rows if r["detected_by"] == "flag"}
    cons_struct: dict[str, set[str]] = defaultdict(set)
    cons_flag: dict[str, set[str]] = defaultdict(set)
    for act in bd.Database(db.INVENTORY_DB):
        for e in act.technosphere():
            c = e.input["code"]
            if act["code"] == c:
                continue
            if c in struct:
                cons_struct[c].add(act["code"])
            if c in flag:
                cons_flag[c].add(act["code"])
    u_s = set().union(*cons_struct.values()) if cons_struct else set()
    u_f = set().union(*cons_flag.values()) if cons_flag else set()
    print(f"datasets consuming at least one of the {len(struct)} structure-detected eco-profiles: {len(u_s)}")
    print(f"datasets consuming at least one of the {len(flag)} flagged datasets:                   {len(u_f)}")
    print("\nmost-consumed unflagged eco-profiles:")
    for c, s in sorted(cons_struct.items(), key=lambda kv: -len(kv[1]))[:15]:
        print(f"  {len(s):5d} consumers  {struct[c]}")
    orphans = [n for c, n in struct.items() if c not in cons_struct]
    print(f"\nunflagged eco-profiles with no consumer at all ({len(orphans)}):")
    for n in orphans:
        print("  ", n)


if __name__ == "__main__":
    main()
