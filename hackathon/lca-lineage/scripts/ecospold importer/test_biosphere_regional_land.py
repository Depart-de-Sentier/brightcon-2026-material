"""Keep the approved Swiss rail aggregation scoped to its reviewed targets."""

import copy
import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from biosphere_migrations import apply_biosphere_flow_migration


class RegionalLandTests(unittest.TestCase):
    def setUp(self):
        root = Path(__file__).resolve().parents[2]
        mapping = json.loads(
            (root / "schemas/mappings/bafu-2026-biosphere-followup.json").read_text()
        )
        self.mapping = {
            "fields": mapping["fields"],
            "data": [
                row
                for row in mapping["data"]
                if row[1]["bafu original biosphere"].get("region") == "CH"
            ],
        }

    def apply(self, mapping):
        # Supply even invalid targets to check that metadata validation, not
        # merely an absent catalog entry, rejects the unapproved aggregation.
        targets = [
            {**dict(zip(mapping["fields"], source)), **replacement}
            for source, replacement in mapping["data"]
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "regional-land.json"
            path.write_text(json.dumps(mapping))
            with (
                patch("biosphere_migrations.Database", return_value=targets),
                patch("biosphere_migrations._apply_and_report", return_value="applied"),
            ):
                return apply_biosphere_flow_migration(
                    SimpleNamespace(data=[]), path, "test-biosphere", path
                )

    def test_approved_swiss_targets(self):
        self.assertEqual(len(self.mapping["data"]), 2)
        self.assertEqual(self.apply(self.mapping), "applied")

    def test_reject_wrong_region_or_land_class(self):
        for change in (
            lambda r: r["bafu original biosphere"].update(region="DE"),
            lambda r: r["bafu original biosphere"].update(region=""),
            lambda r: r.update(name="Occupation, traffic area, road network"),
        ):
            with self.subTest(change=change):
                mapping = copy.deepcopy(self.mapping)
                change(mapping["data"][0][1])
                with self.assertRaisesRegex(ValueError, "Regional biosphere"):
                    self.apply(mapping)

    def test_unreviewed_country_is_not_implicitly_approved(self):
        mapping = copy.deepcopy(self.mapping)
        source, replacement = mapping["data"][0]
        source[1] = source[1].replace(", CH", ", DE")
        replacement["bafu original biosphere"].update(name=source[1], region="DE")
        with self.assertRaisesRegex(ValueError, "Regional biosphere"):
            self.apply(mapping)


if __name__ == "__main__":
    unittest.main()
