"""Check source-specific energy conversion and its narrow peat category exception."""

import copy
import json
import math
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from bw2io.strategies.migrations import migrate_datasets, migrate_exchanges

from biosphere_migrations import CONTEXT_FIELD, apply_biosphere_flow_migration


class Importer:
    def __init__(self, data):
        self.data = data
        self.applied_strategies = []

    def migrate(self, name):
        self.data = migrate_datasets(self.data, name)
        self.data = migrate_exchanges(self.data, name)
        self.applied_strategies.extend(["datasets", "exchanges"])

    def match_database(self, *args, **kwargs):
        for dataset in self.data:
            for exchange in dataset["exchanges"]:
                if exchange["name"] == "Peat" and exchange["unit"] == "kilogram":
                    exchange["input"] = ("test-biosphere", "peat")
        self.applied_strategies.append("match")


class EnergyConversionTests(unittest.TestCase):
    def setUp(self):
        self.source = {
            "type": "biosphere",
            "name": "Energy, from peat",
            "categories": ["natural resource", "in ground"],
            "unit": "megajoule",
            "amount": 1.8403e-5,
            "uncertainty type": 2,
            "loc": math.log(1.8403e-5),
            "scale": 0.4,
            "minimum": 1e-5,
            "maximum": 3e-5,
        }
        self.importer = Importer([
            {"filename": name, "exchanges": [copy.deepcopy(self.source)]}
            for name in ("reviewed.xml", "other.xml")
        ])
        self.mapping = {
            "fields": ["type", "name", "categories", "unit", CONTEXT_FIELD],
            "data": [[
                ["biosphere", "Energy, from peat", self.source["categories"],
                 "megajoule", "reviewed.xml"],
                {
                    "name": "Peat",
                    "categories": ["natural resource", "biotic"],
                    "unit": "kilogram",
                    "multiplier": 1 / 8.4,
                    "bafu original biosphere": {
                        key: self.source[key] for key in ("name", "categories", "unit")
                    },
                    "bafu energy conversion": {
                        "net calorific value, MJ/kg": 8.4,
                        "source flow UUID": "e2fba107-6555-11dd-ad8b-0800200c9a66",
                    },
                },
            ]],
        }

    def apply(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "energy-test.json"
            path.write_text(json.dumps(self.mapping))
            migration = MagicMock()
            migration.load.return_value = self.mapping
            with (
                patch("biosphere_migrations.Migration", return_value=migration),
                patch("bw2io.strategies.migrations.Migration", return_value=migration),
                patch("bw2io.strategies.migrations.migrations", {path.stem: {}}),
                patch("biosphere_migrations.Database", return_value=[{
                    "name": "Peat", "categories": ["natural resource", "biotic"],
                    "unit": "kilogram",
                }]),
            ):
                return apply_biosphere_flow_migration(
                    self.importer, path, "test-biosphere", Path(directory) / "report.json"
                )

    def test_peat_conversion_scales_uncertainty_once_and_preserves_other_file(self):
        other = copy.deepcopy(self.importer.data[1])
        self.assertEqual(self.apply()["after"]["linked"], 1)
        exchange = self.importer.data[0]["exchanges"][0]
        self.assertAlmostEqual(exchange["amount"], self.source["amount"] / 8.4)
        self.assertAlmostEqual(exchange["loc"], self.source["loc"] - math.log(8.4))
        self.assertEqual(exchange["scale"], self.source["scale"])
        for bound in ("minimum", "maximum"):
            self.assertAlmostEqual(exchange[bound], self.source[bound] / 8.4)
        self.assertEqual(exchange["bafu original biosphere"]["categories"],
                         ["natural resource", "in ground"])
        self.assertNotIn(CONTEXT_FIELD, exchange)
        self.assertEqual(self.importer.data[1], other)
        first = copy.deepcopy(self.importer.data)
        self.apply()
        self.assertEqual(self.importer.data, first)

    def test_reject_inverted_or_inconsistent_calorific_factor_before_mutation(self):
        self.mapping["data"][0][1]["multiplier"] = 8.4
        before = copy.deepcopy(self.importer.data)
        with self.assertRaisesRegex(ValueError, "net calorific value"):
            self.apply()
        self.assertEqual(self.importer.data, before)

    def test_category_exception_does_not_allow_other_source_flows_or_categories(self):
        original = copy.deepcopy(self.mapping)
        for field, value in (("uuid", "other-flow"),
                             ("categories", ["natural resource", "in water"])):
            with self.subTest(field=field):
                self.mapping = copy.deepcopy(original)
                replacement = self.mapping["data"][0][1]
                if field == "uuid":
                    replacement["bafu energy conversion"]["source flow UUID"] = value
                else:
                    replacement[field] = value
                before = copy.deepcopy(self.importer.data)
                with self.assertRaisesRegex(ValueError, "net-calorific-value"):
                    self.apply()
                self.assertEqual(self.importer.data, before)


if __name__ == "__main__":
    unittest.main()
