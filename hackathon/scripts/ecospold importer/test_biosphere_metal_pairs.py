"""Verify pair restoration without duplicating mass or hiding ambiguous records."""

import copy
import json
import math
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from bw2io.strategies.migrations import migrate_datasets, migrate_exchanges
from biosphere_migrations import apply_biosphere_flow_migration, PAIR_FIELD


class Importer:
    def __init__(self, data):
        self.data, self.applied_strategies = data, []
        self.fail = False

    def migrate(self, name):
        if self.fail:
            self.data = copy.deepcopy(self.data)
            raise RuntimeError("migration failed")
        self.data = migrate_datasets(self.data, name)
        self.data = migrate_exchanges(self.data, name)
        self.applied_strategies.extend(["datasets", "exchanges"])

    def match_database(self, *args, **kwargs):
        for dataset in self.data:
            for exchange in dataset["exchanges"]:
                if exchange["name"] in ("Palladium II", "Rhodium III"):
                    exchange["input"] = ("test-biosphere", exchange["name"])
        self.applied_strategies.append("match")


class MetalPairTests(unittest.TestCase):
    def setUp(self):
        root = Path(__file__).resolve().parents[2]
        self.mapping = json.loads(
            (root / "schemas/mappings/bafu-2026-biosphere-pm10-metals.json").read_text()
        )
        self.mapping["data"] = self.mapping["data"][:2]
        record = dict(zip(self.mapping["fields"], self.mapping["data"][0][0]))
        filename = record.pop("_migration_source_file")
        amount = float(record.pop("_migration_source_amount"))
        record.pop(PAIR_FIELD)
        record.update(
            amount=amount,
            loc=math.log(amount),
            scale=0.4,
            **{"uncertainty type": 2, "comment": "original"}
        )
        self.importer = Importer(
            [
                {
                    "filename": filename,
                    "exchanges": [
                        copy.deepcopy(record),
                        copy.deepcopy(record),
                        dict(record, amount=1),
                    ],
                },
                {"filename": "other.xml", "exchanges": [copy.deepcopy(record)]},
            ]
        )

    def apply(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "pair-test.json"
            path.write_text(json.dumps(self.mapping))
            migration = MagicMock()
            migration.load.return_value = self.mapping
            targets = [
                {"name": name, "categories": ["air"], "unit": "kilogram"}
                for name in ("Palladium II", "Rhodium III")
            ]
            with (
                patch("biosphere_migrations.Migration", return_value=migration),
                patch("bw2io.strategies.migrations.Migration", return_value=migration),
                patch("bw2io.strategies.migrations.migrations", {path.stem: {}}),
                patch("biosphere_migrations.Database", return_value=targets),
            ):
                return apply_biosphere_flow_migration(
                    self.importer,
                    path,
                    "test-biosphere",
                    Path(directory) / "report.json",
                )

    def test_exact_pair_only_preserves_quantities_and_is_idempotent(self):
        before = copy.deepcopy(self.importer.data)
        self.assertEqual(self.apply()["after"]["linked"], 2)
        after = self.importer.data
        self.assertEqual(after[0]["exchanges"][2], before[0]["exchanges"][2])
        self.assertEqual(after[1], before[1])
        for exchange, name in zip(
            after[0]["exchanges"][:2], ("Palladium II", "Rhodium III")
        ):
            self.assertEqual(exchange["name"], name)
            self.assertEqual(
                {
                    k: v
                    for k, v in exchange.items()
                    if k not in ("name", "input", "bafu original biosphere")
                },
                {k: v for k, v in before[0]["exchanges"][0].items() if k != "name"},
            )
        once = copy.deepcopy(after)
        self.apply()
        self.assertEqual(once, self.importer.data)

    def test_ambiguous_missing_or_different_pairs_fail_before_mutation(self):
        original = copy.deepcopy(self.importer.data)
        for change in (
            "missing",
            "extra",
            "scale",
            "comment",
            "already linked",
            "both missing",
        ):
            with self.subTest(change=change):
                self.importer.data = copy.deepcopy(original)
                rows = self.importer.data[0]["exchanges"]
                if change == "missing":
                    rows.pop(0)
                elif change == "extra":
                    rows.append(copy.deepcopy(rows[0]))
                elif change == "both missing":
                    del rows[:2]
                elif change == "already linked":
                    rows[0]["input"] = ("old", "link")
                else:
                    rows[0][change] = 0.7 if change == "scale" else "different"
                before = copy.deepcopy(self.importer.data)
                with self.assertRaises(ValueError):
                    self.apply()
                self.assertEqual(before, self.importer.data)

    def test_one_target_per_metal_required(self):
        self.mapping["data"][1][1]["name"] = "Palladium II"
        with self.assertRaisesRegex(ValueError, "one Pd and one Rh"):
            self.apply()

    def test_cleanup_after_failure_and_reserved_field_rejection(self):
        self.importer.fail = True
        before = copy.deepcopy(self.importer.data)
        with self.assertRaisesRegex(RuntimeError, "migration failed"):
            self.apply()
        self.assertEqual(before, self.importer.data)
        self.importer.data[0]["exchanges"][0][PAIR_FIELD] = "keep"
        before = copy.deepcopy(self.importer.data)
        with self.assertRaisesRegex(ValueError, "Reserved"):
            self.apply()
        self.assertEqual(before, self.importer.data)


if __name__ == "__main__":
    unittest.main()
