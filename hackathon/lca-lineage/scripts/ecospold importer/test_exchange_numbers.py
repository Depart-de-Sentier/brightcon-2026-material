"""Checks that duplicate-ID repair preserves rows and avoids ambiguous references."""

import json
import unittest

from lxml import etree

from repair_exchange_numbers import MAX_INDEX, NS, repair_exchange_numbers
from repair_metadata import ATTRIBUTE, COMMENT_PREFIX, start_tag_end
from repair_namespace import NAMESPACE


def document(flow_data):
    return (
        f'<ecoSpold xmlns="{NAMESPACE}"><dataset number="42"><flowData>'
        f"{flow_data}</flowData></dataset></ecoSpold>"
    ).encode("utf-8")


def restore_exchange_numbers(data):
    """Reverse comments and number patches to check exact original byte recovery."""
    prefix = f"<!--{COMMENT_PREFIX}".encode("ascii")
    patches = []
    cursor = 0
    restored = 0
    while (start := data.find(prefix, cursor)) != -1:
        end = data.index(b"-->", start) + 3
        change = json.loads(data[start + len(prefix) : end - 3])
        cursor = end
        if change.get("action") != "reassign_number_preserving_inventory_row":
            continue
        tag_end = start_tag_end(data, end)
        tag = data[end:tag_end]
        matches = [m for m in ATTRIBUTE.finditer(tag) if m.group(1) == b"number"]
        if len(matches) != 1:
            raise ValueError("Repair comment not adjacent to a numbered exchange")
        match = matches[0]
        if match.group(3).decode("ascii") != change["replacement_value"]:
            raise ValueError("Repair comment does not match the new number")
        patches.extend(
            [
                (start, end, b""),
                (
                    end + match.start(3),
                    end + match.end(3),
                    change["original_xml_value"].encode("ascii"),
                ),
            ]
        )
        restored += 1
    chunks, previous = [], 0
    for start, end, replacement in sorted(patches):
        chunks.extend((data[previous:start], replacement))
        previous = end
    chunks.append(data[previous:])
    return b"".join(chunks), restored


class ExchangeNumberTests(unittest.TestCase):
    def test_distinct_rows_and_all_other_bytes_are_preserved(self):
        original = document(
            '<!--existing café comment--><exchange number="7" name="steel" '
            'meanValue="1e-05" generalComment="A > B"><inputGroup>1</inputGroup></exchange>'
            "<exchange number = '7' name='steel' meanValue='-0.0004' "
            "uncertaintyType='1' generalComment='different row'><inputGroup>1</inputGroup></exchange>"
            '<exchange number="1" name="product"><outputGroup>0</outputGroup></exchange>'
        )
        repaired, changes = repair_exchange_numbers(original)
        exchanges = etree.fromstring(repaired).findall(
            f"{NS}dataset/{NS}flowData/{NS}exchange"
        )
        self.assertEqual([el.get("number") for el in exchanges], ["7", "2", "1"])
        self.assertEqual(
            [el.get("meanValue") for el in exchanges], ["1e-05", "-0.0004", None]
        )
        self.assertEqual(len(changes), 1)
        self.assertEqual(changes[0]["exchange_index"], 2)
        self.assertEqual(restore_exchange_numbers(repaired), (original, 1))

    def test_numeric_identity_and_original_lexical_values(self):
        original = document(
            '<exchange number="+007"/><exchange number="&#55;"/><exchange number="0007"/>'
        )
        repaired, changes = repair_exchange_numbers(original)
        self.assertEqual(
            [change["replacement_value"] for change in changes], ["1", "2"]
        )
        self.assertEqual(restore_exchange_numbers(repaired), (original, 2))

    def test_id_scope_is_each_dataset(self):
        dataset = '<dataset><flowData><exchange number="8"/><exchange number="8"/></flowData></dataset>'
        original = (
            f'<ecoSpold xmlns="{NAMESPACE}">{dataset}{dataset}</ecoSpold>'.encode()
        )
        repaired, changes = repair_exchange_numbers(original)
        self.assertEqual([change["dataset_index"] for change in changes], [1, 2])
        self.assertEqual(
            [change["replacement_value"] for change in changes], ["1", "1"]
        )
        self.assertEqual(restore_exchange_numbers(repaired), (original, 2))

    def test_ambiguous_allocation_references_are_rejected(self):
        for allocation in (
            '<allocation referenceToCoProduct="7"/>',
            '<allocation referenceToCoProduct="9"><referenceToInputOutput>7</referenceToInputOutput></allocation>',
        ):
            with self.subTest(allocation=allocation):
                with self.assertRaisesRegex(ValueError, "ambiguous allocation"):
                    repair_exchange_numbers(
                        document(
                            '<exchange number="7"/><exchange number="7"/>' + allocation
                        )
                    )

    def test_unambiguous_references_unchanged_and_dangling_ids_reserved(self):
        original = document(
            '<exchange number="7"/><exchange number="7"/><exchange number="9"/>'
            '<allocation referenceToCoProduct="9"><referenceToInputOutput>1</referenceToInputOutput></allocation>'
        )
        repaired, changes = repair_exchange_numbers(original)
        self.assertEqual(changes[0]["replacement_value"], "2")
        self.assertEqual(restore_exchange_numbers(repaired), (original, 1))

    def test_maximum_integer_does_not_overflow(self):
        repaired, changes = repair_exchange_numbers(
            document(
                f'<exchange number="{MAX_INDEX}"/><exchange number="{MAX_INDEX}"/>'
            )
        )
        self.assertEqual(changes[0]["replacement_value"], "1")

    def test_unique_ids_are_byte_identical_and_repair_is_idempotent(self):
        unique = document('<exchange number="1"/><exchange number="2"/>')
        self.assertEqual(repair_exchange_numbers(unique), (unique, []))
        repaired, _ = repair_exchange_numbers(
            document('<exchange number="4"/><exchange number="4"/>')
        )
        self.assertEqual(repair_exchange_numbers(repaired), (repaired, []))

    def test_extension_references_are_not_guessed(self):
        original = document(
            '<exchange number="7"/><exchange number="7"/><x:reference xmlns:x="urn:example" number="7"/>'
        )
        with self.assertRaisesRegex(ValueError, "foreign extension"):
            repair_exchange_numbers(original)

    def test_out_of_range_ids_retained_while_other_duplicates_are_repaired(self):
        for number in ("0", "-1", str(MAX_INDEX + 1)):
            with self.subTest(number=number):
                original = document(
                    f'<exchange number="{number}"/><exchange number="7"/><exchange number="7"/>'
                )
                repaired, changes = repair_exchange_numbers(original)
                self.assertEqual(len(changes), 1)
                self.assertEqual(changes[0]["original_value"], "7")
                self.assertEqual(restore_exchange_numbers(repaired), (original, 1))

    def test_malformed_ids_are_rejected(self):
        for number in ("7.0", ""):
            with self.subTest(number=number):
                with self.assertRaises(ValueError):
                    repair_exchange_numbers(document(f'<exchange number="{number}"/>'))

    def test_doctype_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "DOCTYPE"):
            repair_exchange_numbers(
                b"<!DOCTYPE ecoSpold []>" + document('<exchange number="1"/>')
            )


if __name__ == "__main__":
    unittest.main()
