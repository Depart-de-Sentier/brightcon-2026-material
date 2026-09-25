"""Verify source-file isolation and cleanup while using bw2io migration strategies."""

import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from bw2io.strategies.migrations import migrate_datasets, migrate_exchanges

from biosphere_migrations import CONTEXT_FIELD, apply_biosphere_flow_migration


class Importer:
    def __init__(self, data, fail=False):
        self.data = data
        self.fail = fail
        self.applied_strategies = []

    def migrate(self, name):
        self.data = migrate_datasets(self.data, name)
        if self.fail:
            self.data = copy.deepcopy(self.data)
            raise RuntimeError("migration failed")
        self.data = migrate_exchanges(self.data, name)
        self.applied_strategies.extend(["datasets", "exchanges"])

    def match_database(self, *args, **kwargs):
        for dataset in self.data:
            for exchange in dataset["exchanges"]:
                if exchange["type"] == "biosphere" and exchange["name"] == "Water":
                    exchange["input"] = ("test-biosphere", "water")
        self.applied_strategies.append("match")


class ContextMigrationTests(unittest.TestCase):
    def setUp(self):
        source = {
            "type": "biosphere",
            "name": "Waste water/m3",
            "categories": ["water"],
            "unit": "cubic meter",
            "amount": 0.00011,
        }
        self.importer = Importer(
            [
                {"filename": filename, "exchanges": [copy.deepcopy(source)]}
                for filename in ("reviewed.xml", "other.xml")
            ]
        )
        self.mapping = {
            "fields": ["type", "name", "categories", "unit", CONTEXT_FIELD],
            "data": [
                [
                    [
                        "biosphere",
                        "Waste water/m3",
                        ["water"],
                        "cubic meter",
                        "reviewed.xml",
                    ],
                    {
                        "name": "Water",
                        "bafu original biosphere": {
                            key: source[key] for key in ("name", "categories", "unit")
                        },
                    },
                ]
            ],
        }

    def apply(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "context-test.json"
            path.write_text(json.dumps(self.mapping))
            migration = MagicMock()
            migration.load.return_value = self.mapping
            with (
                patch("biosphere_migrations.Migration", return_value=migration),
                patch("bw2io.strategies.migrations.Migration", return_value=migration),
                patch("bw2io.strategies.migrations.migrations", {path.stem: {}}),
                patch(
                    "biosphere_migrations.Database",
                    return_value=[
                        {
                            "name": "Water",
                            "categories": ["water"],
                            "unit": "cubic meter",
                        }
                    ],
                ),
            ):
                return apply_biosphere_flow_migration(
                    self.importer,
                    path,
                    "test-biosphere",
                    Path(directory) / "report.json",
                )

    def assert_clean(self):
        for dataset in self.importer.data:
            for exchange in dataset["exchanges"]:
                self.assertNotIn(CONTEXT_FIELD, exchange)

    def test_only_reviewed_file_changes_and_repeat_is_idempotent(self):
        other = copy.deepcopy(self.importer.data[1])
        result = self.apply()
        self.assertEqual(result["after"]["linked"], 1)
        self.assertEqual(self.importer.data[1], other)
        changed = self.importer.data[0]["exchanges"][0]
        self.assertEqual(changed["amount"], 0.00011)
        self.assertEqual(changed["bafu original biosphere"]["name"], "Waste water/m3")
        self.assert_clean()
        first = copy.deepcopy(self.importer.data)
        self.apply()
        self.assertEqual(self.importer.data, first)

    def test_cleanup_after_strategy_failure_even_if_records_are_copied(self):
        self.importer.fail = True
        before = copy.deepcopy(self.importer.data)
        with self.assertRaisesRegex(RuntimeError, "migration failed"):
            self.apply()
        self.assert_clean()
        self.assertEqual(self.importer.data, before)

    def test_reject_reserved_field_without_overwriting_it(self):
        self.importer.data[1]["exchanges"][0][CONTEXT_FIELD] = "keep this"
        before = copy.deepcopy(self.importer.data)
        with self.assertRaisesRegex(ValueError, "Reserved migration field"):
            self.apply()
        self.assertEqual(self.importer.data, before)

    def test_reject_missing_or_ambiguous_source_files(self):
        for filename in ("missing.xml", "../reviewed.xml", None):
            with self.subTest(filename=filename):
                self.mapping["data"][0][0][-1] = filename
                with self.assertRaisesRegex(ValueError, "Context source file"):
                    self.apply()
                self.assert_clean()
        self.mapping["data"][0][0][-1] = "reviewed.xml"
        self.importer.data[1]["filename"] = "reviewed.xml"
        with self.assertRaisesRegex(ValueError, "Ambiguous source filename"):
            self.apply()

    def test_source_cas_restricts_context_mapping(self):
        self.mapping["fields"].insert(-1, "CAS number")
        self.mapping["data"][0][0].insert(-1, "007732-18-5")
        self.assertEqual(self.apply()["after"]["linked"], 0)
        self.importer.data[0]["exchanges"][0]["CAS number"] = "007732-18-5"
        self.assertEqual(self.apply()["after"]["linked"], 1)

    def test_existing_link_in_other_file_does_not_block_reviewed_file(self):
        self.importer.data[1]["exchanges"][0]["input"] = ("keep", "existing")
        self.apply()
        self.assertEqual(
            self.importer.data[1]["exchanges"][0]["input"], ("keep", "existing")
        )

    def test_reject_already_linked_source_in_reviewed_file(self):
        self.importer.data[0]["exchanges"][0]["input"] = ("old", "link")
        with self.assertRaisesRegex(ValueError, "already linked"):
            self.apply()
        self.assert_clean()


if __name__ == "__main__":
    unittest.main()
