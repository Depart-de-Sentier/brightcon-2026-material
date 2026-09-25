#!/usr/bin/env python3
"""Verify the recent land/resource/carbon and PM10-metal migrations without writing inventory."""

import copy
import hashlib
import json
import math
import os
from collections import Counter
from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parents[2]
os.environ["BRIGHTWAY2_DIR"] = str(ROOT / "artifacts/brightway")


def add(digest, record):
    digest.update(json.dumps(record, sort_keys=True, default=str).encode())
    digest.update(b"\n")


def check_conversion_stage(namespace, notebook, slug, evidence, statistics, digest):
    """Check each full record against an independently calculated lognormal scaling."""
    importer = namespace["importer"]
    path = ROOT / f"schemas/mappings/bafu-2026-biosphere-{slug}.json"
    mapping = json.loads(path.read_text())
    rows = [row for row in evidence["rows"] if row["proposal"] == slug]
    assert len(mapping["data"]) == len(rows)
    targets = list(namespace["bd"].Database(namespace["BIOSPHERE"]))

    def key(record, filename):
        return (
            record["type"],
            record["name"],
            tuple(record["categories"]),
            record["unit"],
            record.get("CAS number") or "",
            filename,
        )

    rules = {}
    for source, replacement in mapping["data"]:
        record = dict(zip(mapping["fields"], source))
        filename = record["_migration_source_file"]
        row = next(row for row in rows if row["filename"] == filename)
        factor = (
            1 / 560000
            if slug == "uranium-convention"
            else 1 / (14.7 * 632.5) if "05a10e4b" in filename else 1 / 632.5
        )
        assert factor == replacement["multiplier"] == row["factor"]
        assert replacement["bafu conversion assumption"]["multiplier"] == factor
        target = [
            flow
            for flow in targets
            if flow["name"] == replacement["name"]
            and tuple(flow["categories"])
            == tuple(replacement.get("categories", record["categories"]))
            and flow["unit"] == replacement["unit"]
        ]
        assert len(target) == 1 and target[0]["code"] == row["target_code"]
        rules[key(record, filename)] = replacement, target[0].key, row
    assert len(rules) == len(rows)
    expected, hits, conversions = hashlib.sha256(), Counter(), []
    before = statistics()
    for dataset in importer.data:
        filename = Path(dataset["filename"]).name
        add(expected, {k: v for k, v in dataset.items() if k != "exchanges"})
        for exchange in dataset["exchanges"]:
            fixed = copy.deepcopy(exchange)
            signature = key(exchange, filename)
            if signature in rules:
                replacement, target_key, row = rules[signature]
                assert not exchange.get("input")
                assert exchange["amount"] == row["source_amount"]
                # These nine source rows all use lognormal uncertainty. Fail if
                # this changes rather than silently accepting another model.
                assert exchange["uncertainty type"] == 2
                assert not exchange.get("formula")
                factor = replacement["multiplier"]
                amount = exchange["amount"] * factor
                fixed.update(
                    {k: v for k, v in replacement.items() if k != "multiplier"}
                )
                fixed.update(
                    amount=amount, loc=math.log(abs(amount)), negative=amount < 0
                )
                for bound in ("minimum", "maximum"):
                    if bound in fixed:
                        fixed[bound] = exchange[bound] * factor
                fixed["input"] = target_key
                assert fixed["scale"] == exchange["scale"]
                assert math.isclose(
                    fixed["loc"] - exchange["loc"], math.log(factor), rel_tol=1e-12
                )
                assert amount == row["converted_amount"]
                conversions.append(
                    {
                        "filename": filename,
                        "before": copy.deepcopy(exchange),
                        "after": fixed,
                    }
                )
                hits[signature] += 1
            add(expected, fixed)
    assert set(hits) == set(rules) and set(hits.values()) == {1}
    cell = next(
        c
        for c in notebook.cells
        if c.cell_type == "code"
        and f"biosphere_{slug.replace('-', '_')}_result = " in c.source
    )
    exec(compile(cell.source, slug, "exec"), namespace)
    after, first_digest = statistics(), digest()
    assert first_digest == expected.hexdigest(), "Unexpected conversion-stage changes"
    assert before["unlinked_biosphere"] - after["unlinked_biosphere"] == len(rows)
    assert after["datasets"] == 11947 and after["exchanges"] == 420063
    assert after["biosphere"] == 293747 and after.get("unlinked_technosphere", 0) == 0
    report_name = (
        "biosphere-unlinked-after-uranium-convention.json"
        if slug == "uranium-convention"
        else "biosphere-unlinked-after-wood-density.json"
    )
    report_path = ROOT / "reports/generated" / report_name
    report = report_path.read_text()
    exec(compile(cell.source, "repeat " + slug, "exec"), namespace)
    assert digest() == first_digest, "Repeated conversion changed records"
    report_path.write_text(report)
    return {
        "stage": slug,
        "before": before,
        "after": after,
        "new_links": len(rows),
        "rule_count": len(rules),
        "migration_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "each_rule_matches_exactly_once": True,
        "only_declared_fields_and_distribution_scaling_changed": True,
        "all_other_records_unchanged": True,
        "idempotent": True,
        "rows": conversions,
    }


def check_pm10_metals(namespace, notebook, statistics, digest):
    importer = namespace["importer"]
    path = ROOT / "schemas/mappings/bafu-2026-biosphere-pm10-metals.json"
    mapping = json.loads(path.read_text())
    evidence = json.loads(
        (ROOT / "reports/generated/biosphere-pm10-metals-evidence.json").read_text()
    )
    for artifact in evidence["source_artifacts"]:
        assert (
            hashlib.sha256((ROOT / artifact["path"]).read_bytes()).hexdigest()
            == artifact["sha256"]
        )
    assert len(evidence["groups"]) == 13 and len(mapping["data"]) == 26
    targets = list(namespace["bd"].Database(namespace["BIOSPHERE"]))
    changes, checked_rows = {}, []
    for group in evidence["groups"]:
        datasets = [
            ds for ds in importer.data if Path(ds["filename"]).name == group["filename"]
        ]
        assert len(datasets) == 1
        pm10 = [
            e
            for e in datasets[0]["exchanges"]
            if e["name"] == "Particulates, < 10 um"
            and tuple(e["categories"]) == ("air",)
            and e["unit"] == "kilogram"
        ]
        pair = [e for e in pm10 if e["amount"] == group["amount_each_kg"]]
        assert len(pm10) == 3 and len(pair) == 2 and pair[0] == pair[1]
        assert [e["amount"] for e in pm10 if e not in pair] == group["retained_pm10_kg"]
        assert not any(e.get("input") for e in pair)
        for exchange, target_info in zip(pair, group["targets"]):
            source = [
                "biosphere",
                "Particulates, < 10 um",
                ["air"],
                "kilogram",
                "",
                repr(group["amount_each_kg"]),
                target_info["member"],
                group["filename"],
            ]
            replacements = [repl for key, repl in mapping["data"] if key == source]
            assert len(replacements) == 1
            replacement = replacements[0]
            assert replacement == {
                "name": target_info["name"],
                "bafu original biosphere": {
                    "name": exchange["name"],
                    "categories": ["air"],
                    "unit": "kilogram",
                },
            }
            target = [
                f
                for f in targets
                if f["name"] == target_info["name"]
                and tuple(f["categories"]) == ("air",)
                and f["unit"] == "kilogram"
            ]
            assert len(target) == 1 and target[0]["code"] == target_info["code"]
            fixed = {**copy.deepcopy(exchange), **replacement, "input": target[0].key}
            changes[id(exchange)] = fixed
            checked_rows.append(
                {
                    "filename": group["filename"],
                    "before": copy.deepcopy(exchange),
                    "after": fixed,
                }
            )
    assert len(changes) == 26
    before, expected = statistics(), hashlib.sha256()
    for dataset in importer.data:
        add(expected, {k: v for k, v in dataset.items() if k != "exchanges"})
        for exchange in dataset["exchanges"]:
            add(expected, changes.get(id(exchange), exchange))
    cell = next(
        c
        for c in notebook.cells
        if c.cell_type == "code" and "biosphere_pm10_metals_result = " in c.source
    )
    exec(compile(cell.source, "PM10 metal restoration", "exec"), namespace)
    after, first_digest = statistics(), digest()
    assert first_digest == expected.hexdigest(), "Unexpected PM10-metal-stage changes"
    assert before["unlinked_biosphere"] == 3017 and after["unlinked_biosphere"] == 2991
    assert after["unlinked_biosphere_signatures"] == 155
    report_path = ROOT / "reports/generated/biosphere-unlinked.json"
    report = report_path.read_text()
    remaining = json.loads(report)["unlinked"]
    assert (
        next(
            r
            for r in remaining
            if r["name"] == "Particulates, < 10 um" and r["categories"] == ["air"]
        )["occurrences"]
        == 94
    )
    exec(compile(cell.source, "repeat PM10 metal restoration", "exec"), namespace)
    assert digest() == first_digest
    report_path.write_text(report)
    return {
        "before": before,
        "after": after,
        "new_links": 26,
        "migration_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "source_evidence_hashes_verified": True,
        "target_uniqueness_verified": True,
        "all_13_pairs_identical_before_restoration": True,
        "only_declared_names_original_metadata_and_input_links_changed": True,
        "all_amounts_uncertainty_and_other_fields_preserved": True,
        "all_other_records_unchanged": True,
        "idempotent": True,
        "PM10_remaining": 94,
        "rows": checked_rows,
    }


def main():
    os.chdir(ROOT / "scripts")
    notebook_path = ROOT / "scripts/import_fixed_ecospold.ipynb"
    notebook = nbformat.read(notebook_path, as_version=4)
    nbformat.validate(notebook)
    index = next(
        i
        for i, cell in enumerate(notebook.cells)
        if cell.cell_type == "code" and "biosphere_land_mosaic_result = " in cell.source
    )
    namespace = {}
    for cell in notebook.cells[:index]:
        if cell.cell_type == "code":
            exec(
                compile(cell.source, "notebook before mosaic stage", "exec"), namespace
            )
    importer, bd = namespace["importer"], namespace["bd"]
    database_metadata = json.dumps(dict(bd.databases), sort_keys=True, default=str)
    mapping_path = ROOT / "schemas/mappings/bafu-2026-biosphere-land-mosaic.json"
    mapping = json.loads(mapping_path.read_text())
    evidence = json.loads(
        (ROOT / "reports/generated/biosphere-land-mosaic-evidence.json").read_text()
    )
    for artifact in evidence["source_artifacts"]:
        assert (
            hashlib.sha256((ROOT / artifact["path"]).read_bytes()).hexdigest()
            == artifact["sha256"]
        )
    assert len(mapping["data"]) == len(evidence["rows"]) == 18
    targets = list(bd.Database(namespace["BIOSPHERE"]))

    def signature(exchange, filename):
        return (
            exchange["type"],
            exchange["name"],
            tuple(exchange["categories"]),
            exchange["unit"],
            exchange.get("CAS number") or "",
            filename,
        )

    rules = {}
    for source, replacement in mapping["data"]:
        record = dict(zip(mapping["fields"], source))
        filename = record["_migration_source_file"]
        match = [
            target
            for target in targets
            if target["name"] == replacement["name"]
            and tuple(target["categories"]) == tuple(record["categories"])
            and target["unit"] == record["unit"]
        ]
        assert len(match) == 1
        original = [
            row
            for row in evidence["rows"]
            if row["filename"] == filename and row["source_name"] == record["name"]
        ]
        assert len(original) == 1 and original[0]["target_code"] == match[0]["code"]
        assert set(replacement) == {"name", "bafu original biosphere"}
        rules[signature(record, filename)] = (
            replacement,
            match[0].key,
            original[0]["amount_preserved"],
        )
    assert len(rules) == 18

    def statistics():
        counts = Counter(datasets=len(importer.data))
        signatures = set()
        for dataset in importer.data:
            for exchange in dataset["exchanges"]:
                counts["exchanges"] += 1
                counts[exchange["type"]] += 1
                if not exchange.get("input"):
                    counts["unlinked_" + exchange["type"]] += 1
                    if exchange["type"] == "biosphere":
                        signatures.add(signature(exchange, "")[:4])
        counts["unlinked_biosphere_signatures"] = len(signatures)
        return dict(counts)

    def digest():
        result = hashlib.sha256()
        for dataset in importer.data:
            add(
                result,
                {key: value for key, value in dataset.items() if key != "exchanges"},
            )
            for exchange in dataset["exchanges"]:
                add(result, exchange)
        return result.hexdigest()

    before = statistics()
    assert (
        before["unlinked_biosphere"] == 3056
        and before["unlinked_biosphere_signatures"] == 160
    )
    expected, hits = hashlib.sha256(), Counter()
    for dataset in importer.data:
        filename = Path(dataset["filename"]).name
        add(
            expected,
            {key: value for key, value in dataset.items() if key != "exchanges"},
        )
        for exchange in dataset["exchanges"]:
            fixed = copy.deepcopy(exchange)
            key = signature(exchange, filename)
            if key in rules:
                replacement, target_key, amount = rules[key]
                assert not exchange.get("input") and exchange["amount"] == amount
                hits[key] += 1
                fixed.update(replacement)
                fixed["input"] = target_key
            add(expected, fixed)
    assert set(hits) == set(rules) and set(hits.values()) == {1}
    exec(compile(notebook.cells[index].source, "mosaic stage", "exec"), namespace)
    after = statistics()
    first_digest = digest()
    assert first_digest == expected.hexdigest(), "Undeclared record changes"
    assert (
        after["unlinked_biosphere"] == 3038
        and after["unlinked_biosphere_signatures"] == 158
    )
    assert after["datasets"] == before["datasets"] == 11947
    assert after["exchanges"] == before["exchanges"] == 420063
    assert after["biosphere"] == before["biosphere"] == 293747
    assert (
        after.get("unlinked_technosphere", 0)
        == before.get("unlinked_technosphere", 0)
        == 0
    )
    report_path = ROOT / "reports/generated/biosphere-unlinked-after-land-mosaic.json"
    report = report_path.read_text()
    exec(
        compile(notebook.cells[index].source, "repeat mosaic stage", "exec"), namespace
    )
    assert digest() == first_digest, "Repeat application changed records"
    report_path.write_text(report)
    mosaic_after = after
    carbon_path = ROOT / "schemas/mappings/bafu-2026-biosphere-diesel-carbon.json"
    carbon_mapping = json.loads(carbon_path.read_text())
    carbon_evidence = json.loads(
        (ROOT / "reports/generated/biosphere-diesel-carbon-evidence.json").read_text()
    )
    for artifact in carbon_evidence["source_artifacts"]:
        assert (
            hashlib.sha256((ROOT / artifact["path"]).read_bytes()).hexdigest()
            == artifact["sha256"]
        )
    assert len(carbon_mapping["data"]) == len(carbon_evidence["rows"]) == 12
    carbon_rules = {}
    for source, replacement in carbon_mapping["data"]:
        record = dict(zip(carbon_mapping["fields"], source))
        filename = record["_migration_source_file"]
        assert replacement == {
            "name": record["name"] + ", fossil",
            "bafu original biosphere": {
                "name": record["name"],
                "categories": ["air"],
                "unit": "kilogram",
            },
        }
        assert (
            record["name"] in ("Carbon dioxide", "Carbon monoxide")
            and record["categories"] == ["air"]
            and record["unit"] == "kilogram"
        )
        match = [
            target
            for target in targets
            if target["name"] == replacement["name"]
            and tuple(target["categories"]) == ("air",)
            and target["unit"] == "kilogram"
        ]
        assert len(match) == 1
        original = [
            row
            for row in carbon_evidence["rows"]
            if row["filename"] == filename and row["source"]["name"] == record["name"]
        ]
        assert len(original) == 1 and original[0]["target_code"] == match[0]["code"]
        carbon_rules[signature(record, filename)] = (
            replacement,
            match[0].key,
            original[0]["amount_unchanged"],
        )
    assert len(carbon_rules) == 12
    expected_carbon, carbon_hits = hashlib.sha256(), Counter()
    for dataset in importer.data:
        filename = Path(dataset["filename"]).name
        add(
            expected_carbon,
            {key: value for key, value in dataset.items() if key != "exchanges"},
        )
        for exchange in dataset["exchanges"]:
            fixed = copy.deepcopy(exchange)
            key = signature(exchange, filename)
            if key in carbon_rules:
                replacement, target_key, amount = carbon_rules[key]
                assert not exchange.get("input") and exchange["amount"] == amount
                carbon_hits[key] += 1
                fixed.update(replacement)
                fixed["input"] = target_key
            add(expected_carbon, fixed)
    assert set(carbon_hits) == set(carbon_rules) and set(carbon_hits.values()) == {1}
    carbon_cell = next(
        cell
        for cell in notebook.cells
        if cell.cell_type == "code"
        and "biosphere_diesel_carbon_result = " in cell.source
    )
    exec(compile(carbon_cell.source, "approved diesel-carbon stage", "exec"), namespace)
    after = statistics()
    first_digest = digest()
    assert (
        first_digest == expected_carbon.hexdigest()
    ), "Undeclared carbon-stage record changes"
    assert (
        after["unlinked_biosphere"] == 3026
        and after["unlinked_biosphere_signatures"] == 158
    )
    assert (
        after["datasets"] == 11947
        and after["exchanges"] == 420063
        and after["biosphere"] == 293747
    )
    assert after.get("unlinked_technosphere", 0) == 0
    report_path = ROOT / "reports/generated/biosphere-unlinked-after-diesel-carbon.json"
    report = report_path.read_text()
    exec(compile(carbon_cell.source, "repeat diesel-carbon stage", "exec"), namespace)
    assert digest() == first_digest
    report_path.write_text(report)
    carbon_after = after
    conversion_evidence_path = (
        ROOT / "reports/generated/biosphere-uranium-wood-evidence.json"
    )
    conversion_evidence = json.loads(conversion_evidence_path.read_text())
    for artifact in conversion_evidence["source_artifacts"]:
        assert (
            hashlib.sha256((ROOT / artifact["path"]).read_bytes()).hexdigest()
            == artifact["sha256"]
        )
    assert (
        hashlib.sha256(
            Path(conversion_evidence["wood_target_master_path"]).read_bytes()
        ).hexdigest()
        == conversion_evidence["wood_target_master_sha256"]
    )
    conversion_checks = [
        check_conversion_stage(
            namespace, notebook, slug, conversion_evidence, statistics, digest
        )
        for slug in ("uranium-convention", "wood-density")
    ]
    after, first_digest = statistics(), digest()
    assert after["unlinked_biosphere"] == 3017
    assert after["unlinked_biosphere_signatures"] == 155
    conversion_after = after
    pm10_check = check_pm10_metals(namespace, notebook, statistics, digest)
    after, first_digest = statistics(), digest()
    audit = next(
        cell
        for cell in notebook.cells
        if cell.cell_type == "code" and "biosphere_audit_result = " in cell.source
    )
    exec(compile(audit.source, "final biosphere audit", "exec"), namespace)
    assert digest() == first_digest
    assert namespace["biosphere_audit_result"]["occurrences"] == 2991
    assert namespace["biosphere_audit_result"]["signatures"] == 155
    assert database_metadata == json.dumps(
        dict(bd.databases), sort_keys=True, default=str
    )
    assert all(
        not {
            "_migration_source_file",
            "_migration_source_amount",
            "_migration_pair_member",
        }
        & exchange.keys()
        for dataset in importer.data
        for exchange in dataset["exchanges"]
    )
    out = {
        "project": namespace["PROJECT"],
        "biosphere": namespace["BIOSPHERE"],
        "before": before,
        "after": mosaic_after,
        "new_links": 18,
        "rule_count": 18,
        "migration_sha256": hashlib.sha256(mapping_path.read_bytes()).hexdigest(),
        "notebook_sha256": hashlib.sha256(notebook_path.read_bytes()).hexdigest(),
        "source_evidence_hashes_verified": True,
        "only_declared_names_original_label_metadata_and_input_links_changed": True,
        "all_amounts_uncertainty_compartments_units_comments_and_CAS_preserved": True,
        "each_rule_matches_exactly_once": True,
        "all_other_records_unchanged": True,
        "all_exchange_rows_preserved": True,
        "temporary_fields_removed": True,
        "idempotent": True,
        "remaining_worklist_matches_live_importer": True,
        "inventory_database_written": False,
    }
    (ROOT / "reports/generated/biosphere-land-mosaic-migration-check.json").write_text(
        json.dumps(out, indent=2) + "\n"
    )
    carbon_out = {
        **out,
        "before": mosaic_after,
        "after": carbon_after,
        "new_links": 12,
        "rule_count": 12,
        "migration_sha256": hashlib.sha256(carbon_path.read_bytes()).hexdigest(),
        "decision": "User approved documented fossil approximation; retain originals.",
    }
    (
        ROOT / "reports/generated/biosphere-diesel-carbon-migration-check.json"
    ).write_text(json.dumps(carbon_out, indent=2) + "\n")
    conversion_out = {
        "project": namespace["PROJECT"],
        "biosphere": namespace["BIOSPHERE"],
        "before": carbon_after,
        "after": conversion_after,
        "new_links": 9,
        "notebook_sha256": hashlib.sha256(notebook_path.read_bytes()).hexdigest(),
        "helper_sha256": hashlib.sha256(
            (ROOT / "scripts/ecospold importer/biosphere_migrations.py").read_bytes()
        ).hexdigest(),
        "source_evidence_hashes_verified": True,
        "each_target_unique": True,
        "amounts_and_uncertainty_scaled_together": True,
        "remaining_worklist_matches_live_importer": True,
        "temporary_fields_removed": True,
        "inventory_database_written": False,
        "stages": conversion_checks,
    }
    (ROOT / "reports/generated/biosphere-uranium-wood-migration-check.json").write_text(
        json.dumps(conversion_out, indent=2) + "\n"
    )
    pm10_check.update(
        project=namespace["PROJECT"],
        biosphere=namespace["BIOSPHERE"],
        notebook_sha256=conversion_out["notebook_sha256"],
        helper_sha256=conversion_out["helper_sha256"],
        remaining_worklist_matches_live_importer=True,
        temporary_fields_removed=True,
        inventory_database_written=False,
    )
    (ROOT / "reports/generated/biosphere-pm10-metals-migration-check.json").write_text(
        json.dumps(pm10_check, indent=2) + "\n"
    )
    print("PASS: prior reassessment stages and 26 PM10-metal links;", after, flush=True)


if __name__ == "__main__":
    main()
