"""Guard the approved label-only exception to biosphere unit conversions."""

import copy
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from biosphere_migrations import apply_biosphere_flow_migration


class GasUnitAssumptionTests(unittest.TestCase):
    def setUp(self):
        root = Path(__file__).resolve().parents[2]
        self.mapping = json.loads(
            (root / "schemas/mappings/bafu-2026-biosphere-gas-units.json").read_text()
        )
        self.targets = [
            {
                "name": name,
                "categories": ["natural resource", "in ground"],
                "unit": "standard cubic meter",
            }
            for name in ("Gas, natural", "Gas, mine, off-gas, process, coal mining")
        ]

    def apply(self, mapping):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "gas-units.json"
            path.write_text(json.dumps(mapping))
            with (
                patch("biosphere_migrations.Database", return_value=self.targets),
                patch("biosphere_migrations._apply_and_report", return_value="applied"),
            ):
                return apply_biosphere_flow_migration(
                    SimpleNamespace(data=[]), path, "test-biosphere", path
                )

    def test_four_approved_rules_pass_without_numeric_rescaling(self):
        self.assertEqual(len(self.mapping["data"]), 4)
        self.assertTrue(
            all(
                "multiplier" not in replacement
                for _, replacement in self.mapping["data"]
            )
        )
        self.assertEqual(self.apply(self.mapping), "applied")

    def test_reject_undocumented_or_different_assumptions(self):
        changes = [
            lambda s, r: r.pop("bafu unit assumption"),
            lambda s, r: r.pop("bafu original biosphere"),
            lambda s, r: r.update(multiplier=1),
            lambda s, r: r["bafu unit assumption"].update(factor=1.1),
            lambda s, r: r["bafu unit assumption"].update(factor=True),
            lambda s, r: r["bafu unit assumption"].update(
                {"source reference conditions": "known"}
            ),
            lambda s, r: r.update(unit="kilogram"),
            lambda s, r: r.update(categories=["natural resource", "in ground"]),
            lambda s, r: r.update(name="Gas, mine, off-gas, process, coal mining"),
            lambda s, r: s.__setitem__(1, "Unreviewed resource gas"),
        ]
        for index, change in enumerate(changes):
            with self.subTest(change=index):
                mapping = copy.deepcopy(self.mapping)
                change(*mapping["data"][0])
                with self.assertRaises(ValueError):
                    self.apply(mapping)

    def test_target_must_exist_and_be_unique(self):
        self.targets.append(copy.deepcopy(self.targets[0]))
        with self.assertRaisesRegex(ValueError, "missing or ambiguous"):
            self.apply(self.mapping)
        self.targets = []
        with self.assertRaisesRegex(ValueError, "missing or ambiguous"):
            self.apply(self.mapping)


if __name__ == "__main__":
    unittest.main()
