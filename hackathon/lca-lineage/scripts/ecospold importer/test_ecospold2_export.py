"""Regression checks for exchange preservation and EcoSpold 2 serialization."""

import ast
from copy import deepcopy
import json
import math
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from lxml import etree
from pyecospold import Defaults

from ecospold2_export import (
    NS,
    SOURCE_INDEX,
    audit_and_exclude,
    dataset_xml,
    ids,
    label,
)
from mapped_import import BIOSPHERE_STAGES


class ExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name)
        self.ds = {
            "database": "test",
            "code": "a",
            "filename": "process_test.xml",
            "name": "A long source name " * 10,
            "reference product": "test product",
            "location": "CH",
            "unit": "kilogram",
            "tags": [
                ("ecoSpold01startDate", "2024-01-01"),
                ("ecoSpold01endDate", "2024-12-31"),
                ("ecoSpold01dataValidForEntirePeriod", False),
            ],
            "exchanges": [
                {
                    "type": "production",
                    "input": ("test", "a"),
                    "name": "test product",
                    "unit": "kilogram",
                    "amount": 1.0,
                    "loc": 1.0,
                    "uncertainty type": 0,
                }
            ],
        }
        self.bio_key = ("bio", "21e46cb8-6233-4c99-bac3-c41d2ab99498")
        self.bio = {
            self.bio_key: {
                "name": "Particles",
                "unit": "kilogram",
                "categories": ("air",),
            }
        }

    def source(self, size):
        path = self.folder / self.ds["filename"]
        root = etree.fromstring(b"""<ecoSpold><dataset><metaInformation>
          <administrativeInformation>
            <dataEntryBy person="1"/>
            <dataGeneratorAndPublication person="1" copyright="true"/>
            <person number="1" name="Source author" email="unknown"/>
          </administrativeInformation></metaInformation><flowData/>
          </dataset></ecoSpold>""")
        for index in range(size):
            etree.SubElement(
                root.find(".//flowData"),
                "exchange",
                number=str(index),
                meanValue="1",
                name="source label",
            )
        path.write_bytes(etree.tostring(root))
        return path

    def test_exclusions_preserve_duplicate_occurrences_and_all_fields(self):
        missing = {
            "type": "biosphere",
            "name": "Unresolved",
            "amount": -0.5,
            "unit": "kilogram",
            "categories": ("air",),
            "uncertainty type": 2,
            "loc": math.log(0.5),
            "scale": 0.2,
            "negative": True,
            "comment": "source explanation",
        }
        self.ds["exchanges"] += [deepcopy(missing), deepcopy(missing)]
        source = self.source(3)
        original = source.read_bytes()
        excluded, _ = audit_and_exclude([self.ds], self.folder, self.folder / "audit")
        rows = [
            json.loads(line)
            for line in (self.folder / "audit/excluded-exchanges.jsonl")
            .read_text()
            .splitlines()
        ]
        self.assertEqual(excluded, 2)
        self.assertEqual([r["source_exchange_index"] for r in rows], [1, 2])
        self.assertEqual(rows[0]["exchange"], json.loads(json.dumps(missing)))
        self.assertEqual(rows[0]["exchange"], rows[1]["exchange"])
        self.assertEqual(len(self.ds["exchanges"]), 1)
        self.assertEqual(source.read_bytes(), original)

    def test_never_drop_unlinked_technosphere(self):
        self.ds["exchanges"].append({"type": "technosphere", "amount": 1})
        before = deepcopy(self.ds)
        with self.assertRaisesRegex(ValueError, "non-biosphere"):
            audit_and_exclude([self.ds], self.folder, self.folder / "audit")
        self.assertEqual(self.ds, before)

    def test_xml_preserves_signed_uncertainty_zero_bounds_and_supplier_ids(self):
        from bw2io.extractors.ecospold2 import Ecospold2DataExtractor

        self.ds["exchanges"].append(
            {
                "type": "technosphere",
                "input": ("test", "a"),
                "unit": "kilogram",
                "amount": 0.0,
                "uncertainty type": 0,
                "loc": 0.0,
            }
        )
        for uncertainty in [
            {
                "amount": -0.12345678901234567,
                "uncertainty type": 2,
                "loc": math.log(0.12345678901234567),
                "scale": 3.0,
                "negative": True,
            },
            {"amount": 2.0, "uncertainty type": 3, "loc": 2.0, "scale": 0.123456789},
            {"amount": 1.0, "uncertainty type": 4, "minimum": 0.0, "maximum": 2.0},
            {
                "amount": 1.0,
                "uncertainty type": 5,
                "minimum": 0.0,
                "loc": 1.0,
                "maximum": 2.0,
            },
        ]:
            self.ds["exchanges"].append(
                {
                    "type": "biosphere",
                    "input": self.bio_key,
                    "unit": "kilogram",
                    **uncertainty,
                }
            )
        self.source(len(self.ds["exchanges"]))
        for i, exc in enumerate(self.ds["exchanges"]):
            exc[SOURCE_INDEX] = i
        original = deepcopy(self.ds)
        root = dataset_xml(self.ds, {("test", "a"): self.ds}, self.bio, self.folder)
        etree.XMLSchema(file=Defaults.SCHEMA_V2_FILE).assertValid(root)
        self.assertEqual(self.ds, original)
        self.assertEqual(len(label(self.ds["name"])), 120)
        self.assertNotEqual(label(self.ds["name"]), label(self.ds["name"] + "x"))
        rows = root.findall("{*}activityDataset/{*}flowData/*")
        self.assertEqual(rows[1].get("activityLinkId"), ids(self.ds)[0])
        self.assertEqual(rows[1].get("intermediateExchangeId"), ids(self.ds)[1])
        for el, original in zip(rows, self.ds["exchanges"]):
            # Use the actual installed extractor, independently of the writer.
            from lxml import objectify

            actual = Ecospold2DataExtractor.extract_exchange(
                objectify.fromstring(etree.tostring(el))
            )
            self.assertEqual(actual["amount"], original["amount"])
            self.assertEqual(actual["uncertainty type"], original["uncertainty type"])
            for field in ("loc", "scale", "minimum", "maximum"):
                if field in original:
                    self.assertAlmostEqual(actual[field], original[field])
            if original["type"] == "biosphere":
                self.assertEqual(actual["flow"], self.bio_key[1])

    def test_script_migration_order_matches_notebook(self):
        root = Path(__file__).resolve().parents[2]
        notebook = json.loads(
            (root / "scripts/import_fixed_ecospold.ipynb").read_text()
        )
        stages = []
        for cell in notebook["cells"]:
            if cell["cell_type"] != "code":
                continue
            for call in ast.walk(ast.parse("".join(cell["source"]))):
                if (
                    isinstance(call, ast.Call)
                    and isinstance(call.func, ast.Name)
                    and call.func.id.startswith("apply_biosphere_")
                ):
                    for arg in call.args:
                        if isinstance(arg, ast.BinOp) and isinstance(
                            arg.right, ast.Constant
                        ):
                            path = str(arg.right.value)
                            if path.startswith("schemas/mappings/"):
                                stages.append(
                                    Path(path).stem.removeprefix("bafu-2026-biosphere-")
                                )
        self.assertEqual(tuple(stages), BIOSPHERE_STAGES)

    def test_database_readback_allows_only_storage_output_keys(self):
        from import_export_ecospold2 import check_database

        ds = self.ds
        # The real writer mutates the importer by adding output references.
        ds["exchanges"][0]["output"] = ("test", "a")
        stored = {("test", "a"): deepcopy(ds)}
        ds["type"] = "process"
        stored[("test", "a")]["type"] = "processwithreferenceproduct"
        check_database([ds], stored)
        stored[("test", "a")]["exchanges"][0]["amount"] = 2.0
        with self.assertRaisesRegex(ValueError, "exchange records differ"):
            check_database([ds], stored)
        stored[("test", "a")]["exchanges"][0]["output"] = ("test", "b")
        with self.assertRaisesRegex(ValueError, "Wrong stored exchange output"):
            check_database([ds], stored)

    def test_aggregated_inventory_type_is_retained(self):
        self.source(1)
        self.ds["tags"].append(("ecoSpold01type", 2))
        self.ds["exchanges"][0][SOURCE_INDEX] = 0
        root = dataset_xml(self.ds, {("test", "a"): self.ds}, self.bio, self.folder)
        etree.XMLSchema(file=Defaults.SCHEMA_V2_FILE).assertValid(root)
        self.assertEqual(root.find(".//{*}activity").get("type"), "2")


if __name__ == "__main__":
    unittest.main()
