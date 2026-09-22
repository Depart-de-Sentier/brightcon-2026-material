"""Reject inconsistent conversion assumptions before any inventory mutation."""

import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from biosphere_migrations import apply_biosphere_flow_migration


class ConversionAssumptionTests(unittest.TestCase):
    def setUp(self):
        root = Path(__file__).resolve().parents[2]
        self.mapping = json.loads(
            (
                root / "schemas/mappings/bafu-2026-biosphere-uranium-convention.json"
            ).read_text()
        )
        self.mapping["data"] = self.mapping["data"][:1]
        source, self.replacement = self.mapping["data"][0]
        record = dict(zip(self.mapping["fields"], source))
        filename = record.pop("_migration_source_file")
        record.update(amount=0.86912, **{"uncertainty type": 2, "scale": 0.4})
        self.importer = type("Importer", (), {})()
        self.importer.data = [{"filename": filename, "exchanges": [record]}]

    def apply(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "mapping.json"
            path.write_text(json.dumps(self.mapping))
            with (
                patch(
                    "biosphere_migrations.Database",
                    return_value=[
                        {
                            "name": "Uranium",
                            "unit": "kilogram",
                            "categories": ["natural resource", "in ground"],
                        }
                    ],
                ),
                patch("biosphere_migrations._apply_and_report") as apply,
            ):
                result = apply_biosphere_flow_migration(
                    self.importer, path, "test-biosphere", Path(folder) / "report.json"
                )
                apply.assert_called_once()
                return result

    def test_approved_assumption_passes_validation(self):
        self.apply()

    def test_invalid_assumptions_fail_without_mutation(self):
        original = copy.deepcopy(self.mapping)
        for field, value in (
            ("multiplier", 560000),
            ("multiplier", True),
            ("multiplier", float("nan")),
            ("basis", ""),
            ("source quantity unit", None),
            ("documentation", ""),
        ):
            with self.subTest(field=field, value=value):
                self.mapping = copy.deepcopy(original)
                self.mapping["data"][0][1]["bafu conversion assumption"][field] = value
                before = copy.deepcopy(self.importer.data)
                with self.assertRaisesRegex(
                    ValueError, "resource conversion assumption"
                ):
                    self.apply()
                self.assertEqual(self.importer.data, before)

    def test_assumption_requires_source_file_scope(self):
        self.mapping["fields"].pop()
        self.mapping["data"][0][0].pop()
        with self.assertRaisesRegex(ValueError, "resource conversion assumption"):
            self.apply()


if __name__ == "__main__":
    unittest.main()
