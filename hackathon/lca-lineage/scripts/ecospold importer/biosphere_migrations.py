"""Apply documented BAFU biosphere migrations and report exact-match failures."""

import hashlib
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path

from bw2data import Database
from bw2io import Migration
from bw2io.utils import activity_hash

CONTEXT_FIELD = "_migration_source_file"
AMOUNT_FIELD = "_migration_source_amount"
PAIR_FIELD = "_migration_pair_member"


def _amount_key(amount):
    """Represent an exact source quantity as text for bw2io's string hashes."""
    if (
        isinstance(amount, bool)
        or not isinstance(amount, (int, float))
        or not math.isfinite(amount)
    ):
        raise ValueError("Amount-scoped migrations require finite numeric amounts")
    return repr(float(amount))


def _source_context(dataset, exchange, amount_scoped=False):
    context = {CONTEXT_FIELD: Path(dataset["filename"]).name}
    if amount_scoped:
        context[AMOUNT_FIELD] = _amount_key(exchange.get("amount"))
    return context


def _identical_metal_pair_members(importer, mapping):
    """Restore an evidenced Pd/Rh pair only when its two source rows are identical.

    A member number distinguishes otherwise indistinguishable dictionaries for
    bw2io. It does not claim an individual-row lineage that the export lost.
    """
    fields = [field for field in mapping["fields"] if field != PAIR_FIELD]
    groups = defaultdict(dict)
    for source, replacement in mapping["data"]:
        record = dict(zip(mapping["fields"], source))
        member = record[PAIR_FIELD]
        if (
            member not in ("0", "1")
            or record["name"] != "Particulates, < 10 um"
            or record["categories"] != ["air"]
            or record["unit"] != "kilogram"
            or set(replacement) != {"name", "bafu original biosphere"}
        ):
            raise ValueError(
                "Expected a source-specific identical PM10-labelled metal pair"
            )
        key = activity_hash(record, fields)
        groups[key][member] = replacement
    if any(
        set(group) != {"0", "1"}
        or {r["name"] for r in group.values()} != {"Palladium II", "Rhodium III"}
        for group in groups.values()
    ):
        raise ValueError("Each metal pair requires exactly one Pd and one Rh rule")
    matched, completed = defaultdict(list), defaultdict(list)
    for dataset in importer.data:
        for exchange in dataset["exchanges"]:
            if exchange.get("type") != "biosphere":
                continue
            record = {**exchange, **_source_context(dataset, exchange, True)}
            key = activity_hash(record, fields)
            if key in groups:
                matched[key].append(exchange)
            elif exchange.get("bafu original biosphere"):
                original = {**record, **exchange["bafu original biosphere"]}
                key = activity_hash(original, fields)
                if key in groups:
                    completed[key].append(exchange)
    members = {}
    for key, replacements in groups.items():
        rows = matched[key]
        if not rows:
            done = completed[key]
            if (
                len(done) != 2
                or {row["name"] for row in done} != {"Palladium II", "Rhodium III"}
                or any(not row.get("input") for row in done)
            ):
                raise ValueError("Missing or partially applied metal pair")
            continue
        if len(rows) != 2 or rows[0] != rows[1] or completed[key]:
            raise ValueError("Metal pair requires exactly two identical source records")
        if any(row.get("input") for row in rows):
            raise ValueError("Metal pair source is already linked")
        for member, row in enumerate(rows):
            members[id(row)] = str(member)
    return members


def _elemental_mass_fraction(conversion):
    """Check the explicitly supplied simple formula and atomic-weight basis."""
    if set(conversion) != {"source formula", "target element", "atomic weights"}:
        raise ValueError("Expected a formula, target element, and atomic weights")
    formula = conversion["source formula"]
    if not isinstance(formula, str) or not formula:
        raise ValueError("Expected a simple molecular formula")
    parts = re.findall(r"([A-Z][a-z]?)([0-9]*)", formula)
    if "".join(element + count for element, count in parts) != formula:
        raise ValueError("Unsupported molecular formula")
    counts = Counter()
    for element, count in parts:
        counts[element] += int(count or 1)
    weights = conversion["atomic weights"]
    element = conversion["target element"]
    if (
        not isinstance(weights, dict)
        or set(weights) != set(counts)
        or not isinstance(element, str)
        or element not in counts
        or any(count <= 0 for count in counts.values())
        or any(
            isinstance(weight, bool)
            or not isinstance(weight, (int, float))
            or not math.isfinite(weight)
            or weight <= 0
            for weight in weights.values()
        )
    ):
        raise ValueError("Invalid elemental mass-conversion basis")
    return (
        counts[element]
        * weights[element]
        / sum(counts[symbol] * weight for symbol, weight in weights.items())
    )


def _biosphere_summary(importer):
    counts = Counter()
    unlinked = {}
    for dataset in importer.data:
        for exchange in dataset["exchanges"]:
            if exchange.get("type") != "biosphere":
                continue
            counts["total"] += 1
            if exchange.get("input"):
                counts["linked"] += 1
                continue
            counts["unlinked"] += 1
            key = (
                exchange["name"],
                tuple(exchange.get("categories", ())),
                exchange["unit"],
            )
            row = unlinked.setdefault(
                key,
                dict(
                    name=key[0],
                    categories=key[1],
                    unit=key[2],
                    occurrences=0,
                    examples=[],
                ),
            )
            row["occurrences"] += 1
            filename = Path(dataset["filename"]).name
            if len(row["examples"]) < 3 and filename not in row["examples"]:
                row["examples"].append(filename)
    return {
        "total": counts["total"],
        "linked": counts["linked"],
        "unlinked": counts["unlinked"],
        "unlinked_signatures": len(unlinked),
    }, sorted(unlinked.values(), key=lambda row: (-row["occurrences"], row["name"]))


def apply_biosphere_category_migration(importer, mapping_path, biosphere, report_path):
    """Apply category-only rules and link by name, complete categories, and unit.

    Unknown compartments and unmatched names/units remain available for review.
    This function does not drop exchanges or write an inventory database.
    """
    path = Path(mapping_path)
    mapping = json.loads(path.read_text(encoding="utf-8"))
    if mapping["fields"] != ["type", "categories"]:
        raise ValueError("Expected a biosphere category migration")
    keys = set()
    for source, replacement in mapping["data"]:
        if (
            len(source) != 2
            or source[0] != "biosphere"
            or set(replacement) != {"categories"}
            or not isinstance(source[1], list)
            or not isinstance(replacement["categories"], list)
        ):
            raise ValueError("Rules must only replace biosphere categories")
        key = activity_hash(dict(zip(mapping["fields"], source)), mapping["fields"])
        if key in keys:
            raise ValueError("Duplicate biosphere category rule")
        keys.add(key)

    return _apply_and_report(importer, path, mapping, biosphere, report_path)


def apply_biosphere_flow_migration(importer, mapping_path, biosphere, report_path):
    """Apply reviewed aliases, compartment corrections, and unit conversions.

    Unit conversions use bw2io's multiplier support to rescale amounts and
    uncertainty parameters together. The approved gas-volume label assumption
    bypasses rescaling to preserve every numerical field exactly. Each rule
    must identify one target flow. Source-file rules can additionally select an
    exact amount when labels collide; this uses temporary text for bw2io hashes
    and rejects multiple matching source rows before changing the importer.
    """
    path = Path(mapping_path)
    mapping = json.loads(path.read_text(encoding="utf-8"))
    fields = mapping["fields"]
    required_fields = ["type", "name", "categories", "unit"]
    permitted_fields = (required_fields, required_fields + ["CAS number"])
    if fields not in permitted_fields + tuple(
        values + [CONTEXT_FIELD] for values in permitted_fields
    ) + tuple(
        values + [AMOUNT_FIELD, CONTEXT_FIELD] for values in permitted_fields
    ) + tuple(
        values + [AMOUNT_FIELD, PAIR_FIELD, CONTEXT_FIELD]
        for values in permitted_fields
    ):
        raise ValueError("Expected complete biosphere flow signatures")
    contextual = CONTEXT_FIELD in fields
    amount_scoped = AMOUNT_FIELD in fields
    paired = PAIR_FIELD in fields
    reserved_fields = (
        {CONTEXT_FIELD, AMOUNT_FIELD} if amount_scoped else {CONTEXT_FIELD}
    )
    if paired:
        reserved_fields.add(PAIR_FIELD)
    filenames = set()
    if contextual:
        for dataset in importer.data:
            if not dataset.get("filename"):
                raise ValueError(
                    "Source filenames are required for contextual migrations"
                )
            filename = Path(dataset["filename"]).name
            if filename in filenames:
                raise ValueError(f"Ambiguous source filename: {filename}")
            filenames.add(filename)
            for exchange in dataset["exchanges"]:
                if reserved_fields & exchange.keys():
                    raise ValueError("Reserved migration field already present")
                if amount_scoped and exchange.get("type") == "biosphere":
                    _amount_key(exchange.get("amount"))
    target_fields = ["name", "categories", "unit"]
    targets = Counter(
        activity_hash(flow, target_fields) for flow in Database(biosphere)
    )
    keys = set()
    for source, replacement in mapping["data"]:
        if (
            len(source) != len(fields)
            or source[0] != "biosphere"
            or not replacement
            or not set(replacement)
            <= {
                "name",
                "unit",
                "multiplier",
                "categories",
                "bafu original biosphere",
                "bafu elemental conversion",
                "bafu energy conversion",
                "bafu unit assumption",
                "bafu conversion assumption",
            }
        ):
            raise ValueError("Unsupported biosphere replacement fields")
        record = dict(zip(fields, source))
        if amount_scoped:
            amount = record[AMOUNT_FIELD]
            try:
                valid = isinstance(amount, str) and amount == _amount_key(float(amount))
            except (ValueError, OverflowError):
                valid = False
            if not valid:
                raise ValueError("Source amount must be canonical finite numeric text")
        if contextual:
            filename = record[CONTEXT_FIELD]
            if (
                not isinstance(filename, str)
                or Path(filename).name != filename
                or not filename.endswith(".xml")
                or filename not in filenames
            ):
                raise ValueError(
                    f"Context source file is missing or invalid: {filename}"
                )
        if "categories" in replacement:
            categories = replacement["categories"]
            landfill_indicator = (
                record["name"]
                in (
                    "Waste mass, total, placed in landfill",
                    "Organic carbon, placed in landfill",
                )
                and record["categories"] == ["natural resource", "in ground"]
                and record["unit"] == "kilogram"
                and categories == ["inventory indicator", "waste"]
                and set(replacement) == {"categories", "bafu original biosphere"}
            )
            if (
                not isinstance(categories, list)
                or not categories
                or not all(isinstance(value, str) and value for value in categories)
                or (
                    categories[:1] != record["categories"][:1]
                    and not landfill_indicator
                )
            ):
                raise ValueError(
                    "A compartment correction must preserve its main class "
                    "except for the two documented landfill indicators"
                )
            if (
                record["categories"] != ["natural resource"]
                and "bafu original biosphere" not in replacement
            ):
                raise ValueError(
                    "Changing a stated subcategory requires source metadata"
                )
        if "bafu original biosphere" in replacement:
            original = replacement["bafu original biosphere"]
            if (
                not isinstance(original, dict)
                or set(original)
                not in (set(target_fields), set(target_fields) | {"region"})
                or any(original[field] != record[field] for field in target_fields)
            ):
                raise ValueError("Original biosphere metadata must preserve its source")
            if "region" in original:
                regional_water = record["name"].startswith(
                    "Water, "
                ) and replacement.get("name", "").startswith("Water")
                regional_rail = (
                    original["region"] == "CH"
                    and record["name"]
                    in (
                        "Occupation, traffic area, rail network, CH",
                        "Occupation, traffic area, rail/road embankment, CH",
                    )
                    and record["categories"] == ["natural resource", "land"]
                    and record["unit"] == "square meter-year"
                    and replacement.get("name") == record["name"].removesuffix(", CH")
                )
                if (
                    not isinstance(original["region"], str)
                    or not original["region"]
                    or not record["name"].endswith(f", {original['region']}")
                    or not (regional_water or regional_rail)
                ):
                    raise ValueError(
                        "Regional biosphere metadata must preserve its source"
                    )
        key = activity_hash(record, fields)
        if key in keys:
            raise ValueError("Duplicate biosphere flow rule")
        keys.add(key)
        if "bafu unit assumption" in replacement:
            assumption = replacement["bafu unit assumption"]
            if (
                not isinstance(assumption, dict)
                or isinstance(assumption.get("factor"), bool)
                or assumption
                != {
                    "factor": 1,
                    "source reference conditions": "unknown",
                    "basis": "user-approved unit-label assumption; no temperature/pressure conversion",
                }
                or record["name"]
                not in (
                    "Gas, natural/m3",
                    "Gas, mine, off-gas, process, coal mining/m3",
                )
                or record["categories"] != ["natural resource", "in ground"]
                or record["unit"] not in ("cubic meter", "normal cubic meter")
                or replacement.get("unit") != "standard cubic meter"
                or replacement.get("name") != record["name"].removesuffix("/m3")
                or "bafu original biosphere" not in replacement
                or {"multiplier", "categories", "bafu elemental conversion"}
                & replacement.keys()
            ):
                raise ValueError(
                    "Expected the documented 1:1 resource-gas label assumption"
                )
        elif ("unit" in replacement) != ("multiplier" in replacement):
            raise ValueError("A unit conversion requires both unit and multiplier")
        elemental = replacement.get("bafu elemental conversion")
        if "bafu elemental conversion" in replacement:
            permitted_elemental_context = record["categories"] == [
                "natural resource",
                "in ground",
            ] or (
                contextual
                and record["categories"] == ["air"]
                and replacement.get("categories", record["categories"]) == ["air"]
            )
            if (
                not isinstance(elemental, dict)
                or record["unit"] != "kilogram"
                or replacement.get("unit") != "kilogram"
                or not permitted_elemental_context
                or "bafu original biosphere" not in replacement
                or replacement.get("name", record["name"]) == record["name"]
                or "multiplier" not in replacement
            ):
                raise ValueError(
                    "Expected a documented compound-to-element resource or source-specific air conversion"
                )
            expected_factor = _elemental_mass_fraction(elemental)
        if "bafu energy conversion" in replacement:
            energy = replacement["bafu energy conversion"]
            target_categories = replacement.get("categories", record["categories"])
            peat_catalog_category = (
                isinstance(energy, dict)
                and energy.get("source flow UUID")
                == "e2fba107-6555-11dd-ad8b-0800200c9a66"
                and record["name"] == "Energy, from peat"
                and replacement.get("name") == "Peat"
                and target_categories == ["natural resource", "biotic"]
            )
            value = (
                energy.get("net calorific value, MJ/kg")
                if isinstance(energy, dict)
                else None
            )
            if (
                not contextual
                or not isinstance(energy, dict)
                or set(energy) != {"net calorific value, MJ/kg", "source flow UUID"}
                or isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(value)
                or value <= 0
                or not isinstance(energy["source flow UUID"], str)
                or not energy["source flow UUID"]
                or record["unit"] != "megajoule"
                or replacement.get("unit") != "kilogram"
                or record["categories"] != ["natural resource", "in ground"]
                or (
                    target_categories != record["categories"]
                    and not peat_catalog_category
                )
                or "bafu original biosphere" not in replacement
                or elemental is not None
            ):
                raise ValueError(
                    "Expected a source-specific net-calorific-value conversion"
                )
            expected_energy_factor = 1 / value
        if "multiplier" in replacement:
            factor = replacement["multiplier"]
            if (
                isinstance(factor, bool)
                or not isinstance(factor, (int, float))
                or not math.isfinite(factor)
                or factor <= 0
                or (replacement["unit"] == record["unit"] and elemental is None)
            ):
                raise ValueError(
                    "Expected a positive unit or documented elemental conversion"
                )
            if elemental is not None and not math.isclose(
                factor, expected_factor, rel_tol=1e-12
            ):
                raise ValueError(
                    "Multiplier disagrees with the elemental mass fraction"
                )
            if "bafu energy conversion" in replacement and not math.isclose(
                factor, expected_energy_factor, rel_tol=1e-12
            ):
                raise ValueError("Multiplier disagrees with the net calorific value")
        if "bafu conversion assumption" in replacement:
            assumption = replacement["bafu conversion assumption"]
            if (
                not contextual
                or record["categories"][:1] != ["natural resource"]
                or "bafu original biosphere" not in replacement
                or "multiplier" not in replacement
                or not isinstance(assumption, dict)
                or set(assumption)
                != {"basis", "source quantity unit", "multiplier", "documentation"}
                or any(
                    not isinstance(assumption.get(field), str)
                    or not assumption[field].strip()
                    for field in ("basis", "source quantity unit", "documentation")
                )
                or isinstance(assumption.get("multiplier"), bool)
                or not isinstance(assumption.get("multiplier"), (int, float))
                or not math.isclose(
                    assumption["multiplier"], replacement["multiplier"], rel_tol=1e-12
                )
                or {
                    "bafu energy conversion",
                    "bafu elemental conversion",
                    "bafu unit assumption",
                }
                & replacement.keys()
            ):
                raise ValueError(
                    "Expected a documented source-specific resource conversion assumption"
                )
        if targets[activity_hash({**record, **replacement}, target_fields)] != 1:
            raise ValueError(f"Migration target is missing or ambiguous: {source}")

    # Fresh data or a repeat of this same migration is safe. Stale links from a
    # different mapping require re-extraction instead of silently being retained.
    pair_members = _identical_metal_pair_members(importer, mapping) if paired else None
    source_hits = Counter()
    for dataset in importer.data:
        for exchange in dataset["exchanges"]:
            if exchange.get("type") != "biosphere":
                continue
            record = (
                {**exchange, **_source_context(dataset, exchange, amount_scoped)}
                if contextual
                else exchange
            )
            if pair_members is not None and id(exchange) in pair_members:
                record[PAIR_FIELD] = pair_members[id(exchange)]
            key = activity_hash(record, fields)
            if key in keys:
                source_hits[key] += 1
                if exchange.get("input"):
                    raise ValueError(
                        "A source flow is already linked; rerun extraction first"
                    )
    if amount_scoped and any(count > 1 for count in source_hits.values()):
        raise ValueError("Ambiguous amount-scoped source: multiple matching exchanges")
    return _apply_and_report(
        importer,
        path,
        mapping,
        biosphere,
        report_path,
        contextual=contextual,
        amount_scoped=amount_scoped,
        pair_members=pair_members,
    )


def _apply_and_report(
    importer,
    path,
    mapping,
    biosphere,
    report_path,
    contextual=False,
    amount_scoped=False,
    pair_members=None,
):
    before, _ = _biosphere_summary(importer)
    Migration(path.stem).write(mapping, f"BAFU 2026: {path.stem}")
    strategies_before = len(importer.applied_strategies)
    try:
        if contextual:
            for dataset in importer.data:
                for exchange in dataset["exchanges"]:
                    if exchange.get("type") == "biosphere":
                        exchange.update(
                            _source_context(dataset, exchange, amount_scoped)
                        )
                        if pair_members is not None and id(exchange) in pair_members:
                            exchange[PAIR_FIELD] = pair_members[id(exchange)]
        importer.migrate(path.stem)
    finally:
        if contextual:
            for dataset in importer.data:
                for exchange in dataset["exchanges"]:
                    exchange.pop(CONTEXT_FIELD, None)
                    if amount_scoped:
                        exchange.pop(AMOUNT_FIELD, None)
                    if pair_members is not None:
                        exchange.pop(PAIR_FIELD, None)
    if len(importer.applied_strategies) != strategies_before + 2:
        raise RuntimeError(f"Biosphere migration failed: {path.stem}")
    importer.match_database(
        biosphere, fields=["name", "categories", "unit"], edge_kinds=["biosphere"]
    )
    if len(importer.applied_strategies) != strategies_before + 3:
        raise RuntimeError("Biosphere linking failed")
    after, unlinked = _biosphere_summary(importer)

    by_name = defaultdict(list)
    for flow in Database(biosphere):
        by_name[flow["name"].lower()].append(flow)
    for row in unlinked:
        candidates = by_name[row["name"].lower()]
        if not candidates:
            reason = "name_not_found"
        elif any(tuple(flow["categories"]) == row["categories"] for flow in candidates):
            reason = "unit_mismatch"
        elif any(flow["unit"] == row["unit"] for flow in candidates):
            reason = "category_mismatch_or_missing_compartment"
        else:
            reason = "name_exists_other_unit_and_compartment"
        row["reason"] = reason

    report = {
        "biosphere_database": biosphere,
        "migration_file": path.name,
        "migration_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "rules": len(mapping["data"]),
        "before": before,
        "after": after,
        "unlinked": unlinked,
    }
    report_path = Path(report_path)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(
        f"Biosphere: {after['linked']:,} linked; {after['unlinked']:,} unlinked "
        f"across {after['unlinked_signatures']:,} signatures."
    )
    print(f"Unlinked biosphere report: {report_path}")
    return {"before": before, "after": after}
