"""Regression checks for structural repairs and attached provenance comments."""

import unittest

from lxml import etree

from repair_administrative_order import repair_administrative_order
from repair_namespace import NAMESPACE


def document(children):
    return (
        f'<ecoSpold xmlns="{NAMESPACE}"><dataset number="1"><metaInformation>'
        f"<administrativeInformation>{children}</administrativeInformation>"
        "</metaInformation></dataset></ecoSpold>"
    ).encode()


class AdministrativeOrderTests(unittest.TestCase):
    def test_valid_order_remains_byte_identical(self):
        data = document(
            '<dataEntryBy person="1"/><dataGeneratorAndPublication person="1"/>'
            '<person number="1"/>'
        )
        self.assertEqual(repair_administrative_order(data), (data, []))

    def test_comments_remain_with_people_and_person_order_is_stable(self):
        data = document(
            '\n<dataGeneratorAndPublication person="2"/>'
            '\n<!-- person-two --><person number="2"/>'
            '\n<dataEntryBy person="1"/>'
            '\n<!-- person-one --><person number="1"/>\n'
        )
        fixed, changes = repair_administrative_order(data)
        self.assertEqual(len(changes), 1)
        root = etree.fromstring(fixed)
        admin = root.find(f".//{{{NAMESPACE}}}administrativeInformation")
        elements = [node for node in admin if isinstance(node.tag, str)]
        self.assertEqual(
            [etree.QName(node).localname for node in elements],
            ["dataEntryBy", "dataGeneratorAndPublication", "person", "person"],
        )
        self.assertEqual([node.get("number") for node in elements[2:]], ["2", "1"])
        self.assertEqual(
            [
                (comment.text.strip(), comment.getnext().get("number"))
                for comment in admin.xpath("comment()")
            ],
            [("person-two", "2"), ("person-one", "1")],
        )
        self.assertEqual(len(fixed), len(data))

    def test_explicit_end_tags_and_foreign_extensions(self):
        extension = (
            '<extra xmlns="urn:example"><value>keep &amp; preserve</value></extra>'
        )
        data = document(
            extension
            + '<dataGeneratorAndPublication person="1"></dataGeneratorAndPublication>'
            '<person number="1"></person><dataEntryBy person="1"></dataEntryBy>'
        )
        fixed, _ = repair_administrative_order(data)
        admin = etree.fromstring(fixed).find(
            f".//{{{NAMESPACE}}}administrativeInformation"
        )
        self.assertEqual(admin[-1].tag, "{urn:example}extra")
        self.assertIn(extension.encode(), fixed)
        self.assertIn(b'<dataEntryBy person="1"></dataEntryBy>', fixed)

    def test_repair_is_idempotent(self):
        data = document(
            '<person number="1"/><dataGeneratorAndPublication person="1"/>'
            '<dataEntryBy person="1"/>'
        )
        fixed, changes = repair_administrative_order(data)
        self.assertTrue(changes)
        self.assertEqual(repair_administrative_order(fixed), (fixed, []))

    def test_multiple_sections_are_repaired_independently(self):
        data = document(
            '<person number="1"/><dataEntryBy person="1"/><dataGeneratorAndPublication/>'
        )
        dataset = data[
            data.index(b"<dataset") : data.index(b"</dataset>") + len(b"</dataset>")
        ]
        data = data.replace(
            dataset, dataset + dataset.replace(b'number="1"', b'number="2"')
        )
        fixed, changes = repair_administrative_order(data)
        self.assertEqual([change["dataset_number"] for change in changes], ["1", "2"])
        self.assertEqual(len(etree.fromstring(fixed)), 2)

    def test_unexpected_same_namespace_child_is_not_guessed(self):
        with self.assertRaisesRegex(ValueError, "Unexpected administrative child"):
            repair_administrative_order(document("<unknown/>"))


if __name__ == "__main__":
    unittest.main()
