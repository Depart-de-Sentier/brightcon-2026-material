"""Regression checks for reversible schema repairs and explicit missing facts."""

from copy import deepcopy
import unittest

from lxml import etree

from repair_schema import NS, canonical, repair_schema, reverse_changes
from validate_collection import verify_inventory


def fixture():
    root = etree.Element(NS + "ecoSpold", nsmap={None: NS[1:-1]})
    ds = etree.SubElement(root, NS + "dataset", number="1")
    mi = etree.SubElement(ds, NS + "metaInformation")
    pi = etree.SubElement(mi, NS + "processInformation")
    etree.SubElement(pi, NS + "referenceFunction", name="product", amount="1.0")
    etree.SubElement(pi, NS + "geography", location="CH")
    etree.SubElement(pi, NS + "technology")
    tp = etree.SubElement(pi, NS + "timePeriod")
    etree.SubElement(tp, NS + "startYear").text = "2020"
    etree.SubElement(tp, NS + "endYear").text = "2021"
    etree.SubElement(pi, NS + "dataSetInformation", timestamp="2025-01-01T12:00:00")
    mv = etree.SubElement(mi, NS + "modellingAndValidation")
    etree.SubElement(mv, NS + "representativeness", percent="100.0")
    etree.SubElement(
        mv, NS + "source", number="2", year="2021", title="Study", firstAuthor="Author"
    )
    etree.SubElement(mv, NS + "validation")
    ai = etree.SubElement(mi, NS + "administrativeInformation")
    etree.SubElement(ai, NS + "dataEntryBy", person="3")
    etree.SubElement(ai, NS + "dataGeneratorAndPublication", person="3")
    etree.SubElement(
        ai, NS + "person", number="3", name="Name", address="Address", countryCode="CH"
    )
    flow = etree.SubElement(ds, NS + "flowData")
    exc = etree.SubElement(
        flow,
        NS + "exchange",
        number="4",
        meanValue="-1.234e-8",
        uncertaintyType="1",
        standardDeviation95="2.5",
        location="CH",
    )
    etree.SubElement(exc, NS + "inputGroup").text = "1"
    return root


def get(root, name):
    return root.find(f".//{NS}{name}")


class SchemaRepairTests(unittest.TestCase):
    def repair(self, root, **kwargs):
        data = etree.tostring(root)
        repaired, changes, unresolved = repair_schema(
            data,
            "fixture.xml",
            kwargs.get("catalog", {}),
            kwargs.get("aliases", {}),
            kwargs.get("overrides", {}),
        )
        result = etree.fromstring(repaired)
        self.assertEqual(canonical(reverse_changes(result, changes)), canonical(root))
        return result, changes, unresolved

    def test_format_changes_keep_numeric_and_boolean_values(self):
        root = fixture()
        get(root, "representativeness").set("percent", "100")
        get(root, "dataSetInformation").set("timestamp", "2025-01-01 12:00:00.123456")
        get(root, "exchange").set("infrastructureProcess", "False")
        result, changes, _ = self.repair(root)
        self.assertEqual(get(result, "representativeness").get("percent"), "100.0")
        self.assertEqual(
            get(result, "dataSetInformation").get("timestamp"),
            "2025-01-01T12:00:00.123456",
        )
        self.assertEqual(get(result, "exchange").get("infrastructureProcess"), "false")
        self.assertEqual(get(result, "exchange").get("meanValue"), "-1.234e-8")

    def test_unknown_country_and_period_are_not_invented(self):
        root = fixture()
        get(root, "person").set("countryCode", "")
        get(root, "timePeriod")[:] = []
        result, _, unresolved = self.repair(root)
        self.assertEqual(get(result, "person").get("countryCode"), "")
        self.assertEqual(len(get(result, "timePeriod")), 0)
        self.assertEqual(
            {item["kind"] for item in unresolved}, {"missing_country", "missing_period"}
        )

    def test_explicit_overrides_are_applied_and_reversible(self):
        root = fixture()
        get(root, "person").set("countryCode", "")
        get(root, "timePeriod")[:] = []
        overrides = {
            "person_countries": {"3": {"value": "CH", "evidence": "User decision"}},
            "periods": {
                "fixture.xml": {
                    "start_year": 2024,
                    "end_year": 2024,
                    "evidence": "Documented year",
                }
            },
        }
        result, changes, unresolved = self.repair(root, overrides=overrides)
        self.assertEqual(get(result, "person").get("countryCode"), "CH")
        self.assertEqual(get(result, "startYear").text, "2024")
        self.assertFalse(unresolved)
        self.assertTrue(all("evidence" in change for change in changes))

    def test_required_names_and_invalid_optional_values_preserved_in_comments(self):
        root = fixture()
        get(root, "person").set("name", "An overlong person name " * 3)
        get(root, "exchange").set("CASNumber", "unknown")
        get(root, "source").set("volumeNo", "nan")
        result, changes, _ = self.repair(root)
        self.assertEqual(get(result, "person").get("name"), "")
        self.assertIsNone(get(result, "exchange").get("CASNumber"))
        self.assertEqual(len(changes), 3)

    def test_source_year_comes_from_explicit_text(self):
        root = fixture()
        get(root, "source").set("year", "")
        get(root, "source").set("text", "Title.\\nYear: 2007\\n")
        result, _, unresolved = self.repair(root)
        self.assertEqual(get(result, "source").get("year"), "2007")
        self.assertFalse(unresolved)

    def test_unknown_source_year_override_is_scoped_to_file_and_source(self):
        root = fixture()
        get(root, "source").set("year", "")
        result, _, unresolved = self.repair(root)
        self.assertEqual(unresolved[0]["kind"], "missing_source_year")
        override = {
            "source_years": {
                "fixture.xml": {
                    "2": {
                        "value": 2026,
                        "evidence": "Approved placeholder, original year unknown",
                    }
                }
            }
        }
        result, _, unresolved = self.repair(root, overrides=override)
        self.assertEqual(get(result, "source").get("year"), "2026")
        self.assertFalse(unresolved)
        other = deepcopy(root)
        get(other, "source").set("number", "9")
        result, _, unresolved = self.repair(other, overrides=override)
        self.assertEqual(get(result, "source").get("year"), "")
        self.assertEqual(unresolved[0]["kind"], "missing_source_year")

    def test_inventory_verifier_detects_amount_uncertainty_and_direction_changes(self):
        root = fixture()
        for field in ("meanValue", "uncertaintyType", "standardDeviation95"):
            with self.subTest(field=field):
                changed = deepcopy(root)
                get(changed, "exchange").set(field, "999")
                with self.assertRaisesRegex(AssertionError, "Inventory payload"):
                    verify_inventory(root, changed, {})
        changed = deepcopy(root)
        get(changed, "inputGroup").text = "4"
        with self.assertRaisesRegex(AssertionError, "Inventory payload"):
            verify_inventory(root, changed, {})

    def test_inventory_verifier_accepts_only_documented_schema_differences(self):
        root = fixture()
        get(root, "exchange").set("infrastructureProcess", "False")
        get(root, "exchange").set("CASNumber", "")
        get(root, "exchange").set("location", "Europe without Switzerland")
        result, _, _ = self.repair(
            root, aliases={"Europe without Switzerland": "LBFAC32"}
        )
        self.assertEqual(
            verify_inventory(root, result, {"LBFAC32": "Europe without Switzerland"}),
            (1, 1),
        )

    def test_reordering_keeps_attached_comments_and_removes_only_empty_duplicate(self):
        root = fixture()
        pi = get(root, "processInformation")
        tp = get(root, "timePeriod")
        pi.remove(tp)
        pi.insert(0, tp)
        tp.addprevious(etree.Comment("attached time comment"))
        mv = get(root, "modellingAndValidation")
        etree.SubElement(mv, NS + "validation")
        result, _, _ = self.repair(root)
        self.assertEqual(
            etree.QName(get(result, "processInformation")[0]).localname,
            "referenceFunction",
        )
        self.assertEqual(
            get(result, "timePeriod").getprevious().text, "attached time comment"
        )
        self.assertEqual(
            len(get(result, "modellingAndValidation").findall(NS + "validation")), 1
        )

    def test_nonempty_extra_validation_is_not_discarded(self):
        root = fixture()
        etree.SubElement(
            get(root, "modellingAndValidation"),
            NS + "validation",
            proofReadingDetails="Another review",
        )
        with self.assertRaisesRegex(ValueError, "nonempty"):
            self.repair(root)

    def test_location_alias_and_zero_id_keep_exchange_contents(self):
        root = fixture()
        exc = get(root, "exchange")
        exc.set("location", "Europe without Switzerland")
        exc.set("number", "0")
        result, _, _ = self.repair(
            root, aliases={"Europe without Switzerland": "LBFAC32"}
        )
        repaired = get(result, "exchange")
        self.assertEqual(repaired.get("location"), "LBFAC32")
        self.assertEqual(repaired.get("number"), "1")
        for field in ("meanValue", "uncertaintyType", "standardDeviation95"):
            self.assertEqual(repaired.get(field), exc.get(field))

    def test_missing_citation_restored_only_when_identity_agrees(self):
        root = fixture()
        get(root, "dataGeneratorAndPublication").set("referenceToPublishedSource", "8")
        attrs = {
            "number": "8",
            "title": "Another study",
            "year": "2020",
            "firstAuthor": "Other",
        }
        result, _, unresolved = self.repair(root, catalog={"8": [(attrs, "other.xml")]})
        self.assertEqual(len(result.findall(f".//{NS}source")), 2)
        self.assertFalse(unresolved)
        conflicting = dict(attrs, title="Different study")
        result, _, unresolved = self.repair(
            root, catalog={"8": [(attrs, "a.xml"), (conflicting, "b.xml")]}
        )
        self.assertEqual(len(result.findall(f".//{NS}source")), 1)
        self.assertEqual(unresolved[0]["kind"], "ambiguous_missing_source")

    def test_idempotence(self):
        root = fixture()
        get(root, "exchange").set("infrastructureProcess", "True")
        repaired, _, _ = self.repair(root)
        _, changes, _ = self.repair(repaired)
        self.assertEqual(changes, [])

    def test_unknown_boolean_requires_documented_override(self):
        root = fixture()
        get(root, "timePeriod").set("dataValidForEntirePeriod", "")
        result, _, unresolved = self.repair(root)
        self.assertEqual(get(result, "timePeriod").get("dataValidForEntirePeriod"), "")
        self.assertEqual(unresolved[0]["kind"], "missing_boolean")
        override = {
            "empty_booleans": {
                "timePeriod.dataValidForEntirePeriod": {
                    "value": "false",
                    "evidence": "User decision; source unknown",
                }
            }
        }
        result, changes, unresolved = self.repair(root, overrides=override)
        self.assertEqual(
            get(result, "timePeriod").get("dataValidForEntirePeriod"), "false"
        )
        self.assertFalse(unresolved)

    def test_unsupported_text_is_preserved_and_not_overwritten_into_comment(self):
        root = fixture()
        ref = get(root, "referenceFunction")
        ref.set("text", "extra technical description")
        ref.set("generalComment", "existing description")
        result, changes, _ = self.repair(root)
        self.assertIsNone(get(result, "referenceFunction").get("text"))
        self.assertEqual(
            get(result, "referenceFunction").get("generalComment"),
            "existing description",
        )
        self.assertEqual(changes[0]["original_value"], "extra technical description")


if __name__ == "__main__":
    unittest.main()
