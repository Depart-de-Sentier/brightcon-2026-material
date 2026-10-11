"""Brightway access: the BAFU database, the sandbox, and name resolution."""

from __future__ import annotations

import csv
import difflib
import re
from functools import lru_cache
from pathlib import Path

import bw2data as bd

INVENTORY_DB = "bafu-2026"
BIOSPHERE_DBS = ("ef-3.1-biosphere", "bafu-2026-residual")
SANDBOX_DB = "reverse-bafu-sandbox"
SYSTEM_TERMINATED_CSV = Path("results/system_terminated.csv")
SYSTEM_TERMINATED_EXTENDED_CSV = Path("results/system_terminated_extended.csv")

# when a name matches in several locations and the spec does not say which
LOCATION_PREFERENCE = ("RER", "CH", "DE", "GLO", "Europe")


def set_project(project: str) -> None:
    if project not in bd.projects:
        raise SystemExit(f"Brightway project {project!r} not found; run `uv run sentier-brightway db --project {project}`")
    bd.projects.set_current(project)



@lru_cache(maxsize=1)
def aggregated_codes() -> frozenset[str]:
    """Codes of the ecoSpold type=2 datasets, from the screening CSV (empty set if absent).

    Flag-based and deliberately unchanged: ``benchmark.py`` uses this set to decide which BAFU unit
    processes may be drawn as synthetic test cases, so widening it would move every published
    benchmark number. Use :func:`aggregated_codes_all` wherever the question is "is this input a
    system process?".
    """
    if not SYSTEM_TERMINATED_CSV.exists():
        return frozenset()
    return frozenset(r["code"] for r in csv.DictReader(SYSTEM_TERMINATED_CSV.open()))


@lru_cache(maxsize=1)
def aggregated_codes_all() -> frozenset[str]:
    """Every system process: the ecoSpold type=2 flag *plus* the ones the flag
    missed, found by structure (``scripts/find_system_processes.py`` -> the extended CSV).

    This is what resolve and check must use. The flag is incomplete: the APME / PlasticsEurope era
    eco-profiles (styrene, benzene, propylene, butadiene, the nylons, ABS, polycarbonate, PMMA, ...)
    were never marked, so a rebuild that links one of them used to be reported as "no dependency on
    another system process" when it had in fact terminated on one. Falls back to the
    flag-based set when the extended CSV has not been generated.
    """
    if not SYSTEM_TERMINATED_EXTENDED_CSV.exists():
        return aggregated_codes()
    return aggregated_codes() | frozenset(
        r["code"] for r in csv.DictReader(SYSTEM_TERMINATED_EXTENDED_CSV.open()))


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().lower())


@lru_cache(maxsize=1)
def activity_index() -> dict[str, list[dict]]:
    """normalised name -> [{code, location, unit, n_inputs, aggregated}] for the BAFU database."""
    idx: dict[str, list[dict]] = {}
    agg = aggregated_codes_all()
    for key, act in bd.Database(INVENTORY_DB).load().items():
        n_in = sum(1 for e in act.get("exchanges", []) if e.get("type") == "technosphere")
        idx.setdefault(_norm(act["name"]), []).append(
            {"name": act["name"], "code": key[1], "location": act.get("location", ""), "unit": act.get("unit", ""),
             "n_inputs": n_in, "aggregated": key[1] in agg})
    # Sorted, because `Database.load()` returns a dict whose order is not stable between processes
    # and `resolve_activity` falls back to the first entry when several share a location. Without
    # this, running the same spec twice could resolve the same name to two different datasets.
    for entries in idx.values():
        entries.sort(key=lambda e: (e["location"], e["code"]))
    return idx


@lru_cache(maxsize=1)
def flow_index() -> dict[str, list[dict]]:
    """normalised name -> [{database, code, categories, unit}] over both biosphere databases."""
    idx: dict[str, list[dict]] = {}
    for dbname in BIOSPHERE_DBS:
        for key, flow in bd.Database(dbname).load().items():
            idx.setdefault(_norm(flow["name"]), []).append(
                {"name": flow["name"], "database": dbname, "code": key[1],
                 "categories": tuple(str(c) for c in flow.get("categories", ())), "unit": flow.get("unit", "")})
    # Sorted for the same reason as in `activity_index`, and it matters more here: `resolve_flow`
    # scores only on the *top-level* compartment and on whether the sub-compartment is
    # "unspecified", so two sub-compartments of the same substance often tie - e.g. "Sodium
    # chloride" in `resources / in ground` and in `resources / in water`. `max()` then returns
    # whichever came first out of the database, which is not reproducible: the drafted epoxy-resin
    # spec resolved its 1.8 kg of rock salt to `in ground` on one run and to `in water` on the
    # next, moving the kilogram mass it covers from 75 % to 57 %. Sorting by categories makes the
    # tie-break deterministic (and, on that case, right).
    for entries in idx.values():
        entries.sort(key=lambda e: (e["categories"], e["database"], e["code"]))
    return idx


def resolve_activity(name: str, location: str = "", prefer: str = "") -> tuple[dict | None, list[str]]:
    """Best BAFU activity for a name (+ optional location); (None, suggestions) if nothing matches."""
    idx = activity_index()
    cands = idx.get(_norm(name), [])
    if not cands:
        close = difflib.get_close_matches(_norm(name), idx.keys(), n=5, cutoff=0.6)
        return None, [idx[c][0]["name"] for c in close]
    if location:
        exact = [c for c in cands if c["location"] == location]
        if exact:
            return exact[0], []
    for loc in (prefer, *LOCATION_PREFERENCE):
        for c in cands:
            if c["location"] == loc:
                return c, []
    return cands[0], []


def resolve_flow(name: str, category: str = "") -> tuple[dict | None, list[str]]:
    """Best biosphere flow for a name and a top-level category hint ('air', 'water', 'soil', 'resources').
    EF 3.1 flows exist in several sub-compartments; prefer the 'unspecified' one, and break the
    remaining ties on the sorted order of `flow_index` so that the choice is reproducible."""
    idx = flow_index()
    cands = idx.get(_norm(name), [])
    if not cands:
        close = difflib.get_close_matches(_norm(name), idx.keys(), n=5, cutoff=0.6)
        return None, [idx[c][0]["name"] for c in close]
    hint = category.lower()
    def score(c: dict) -> tuple:
        cats = " / ".join(c["categories"]).lower()
        return (hint in cats, "unspecified" in cats and "long-term" not in cats, c["database"] == BIOSPHERE_DBS[0])
    best = max(cands, key=score)
    return best, []


def sandbox() -> bd.Database:
    if SANDBOX_DB not in bd.databases:
        db = bd.Database(SANDBOX_DB)
        db.register(depends=[INVENTORY_DB, *BIOSPHERE_DBS], comment="reverse-bafu: rebuilt unit processes")
    return bd.Database(SANDBOX_DB)
