"""Restrict changes of main compartment to the two reviewed landfill indicators."""

import copy
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from biosphere_migrations import apply_biosphere_flow_migration


class LandfillIndicatorTests(unittest.TestCase):
    def setUp(self):
        root = Path(__file__).resolve().parents[2]
        mapping = json.loads(
            (
                root / "schemas/mappings/bafu-2026-biosphere-compartments.json"
            ).read_text()
        )
        self.mapping = {
            "fields": mapping["fields"],
            "data": [
                row
                for row in mapping["data"]
                if row[1].get("categories") == ["inventory indicator", "waste"]
            ],
        }

    def apply(self, mapping):
        targets = [
            {**dict(zip(mapping["fields"], source)), **replacement}
            for source, replacement in mapping["data"]
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "landfill-indicators.json"
            path.write_text(json.dumps(mapping))
            with (
                patch("biosphere_migrations.Database", return_value=targets),
                patch("biosphere_migrations._apply_and_report", return_value="applied"),
            ):
                return apply_biosphere_flow_migration(
                    SimpleNamespace(data=[]), path, "test-biosphere", path
                )

    def test_two_documented_indicators(self):
        self.assertEqual(len(self.mapping["data"]), 2)
        self.assertEqual(self.apply(self.mapping), "applied")

    def test_reject_other_changes_of_main_compartment(self):
        def other_resource(source, replacement):
            source[1] = "Gravel, resource correction"
            replacement["bafu original biosphere"]["name"] = source[1]

        def other_source_category(source, replacement):
            source[2] = ["air"]
            replacement["bafu original biosphere"]["categories"] = source[2]

        changes = (
            other_resource,
            other_source_category,
            lambda s, r: r.update(categories=["inventory indicator", "other"]),
            lambda s, r: r.update(unit="ton", multiplier=0.001),
            lambda s, r: r.update(name="Different landfill indicator"),
            lambda s, r: r.pop("bafu original biosphere"),
        )
        for index, change in enumerate(changes):
            with self.subTest(change=index):
                mapping = copy.deepcopy(self.mapping)
                change(*mapping["data"][0])
                with self.assertRaisesRegex(ValueError, "main class"):
                    self.apply(mapping)


if __name__ == "__main__":
    unittest.main()
