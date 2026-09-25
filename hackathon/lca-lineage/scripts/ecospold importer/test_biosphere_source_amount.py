"""Check exact source-row selection without changing amounts or nearby rows."""

import copy
import math
import unittest

from biosphere_migrations import AMOUNT_FIELD, CONTEXT_FIELD
import test_biosphere_context as context_tests


class AmountScopedMigrationTests(unittest.TestCase):
    apply = context_tests.ContextMigrationTests.apply

    def setUp(self):
        context_tests.ContextMigrationTests.setUp(self)
        self.mapping["fields"].insert(-1, AMOUNT_FIELD)
        self.mapping["data"][0][0].insert(-1, "0.00011")
        self.importer.data[0]["exchanges"].extend(
            [
                dict(self.importer.data[0]["exchanges"][0], amount=amount)
                for amount in (0.00012, math.nextafter(0.00011, math.inf))
            ]
        )

    def assert_clean(self):
        for dataset in self.importer.data:
            for exchange in dataset["exchanges"]:
                self.assertNotIn(CONTEXT_FIELD, exchange)
                self.assertNotIn(AMOUNT_FIELD, exchange)

    def test_exact_amount_and_filename_only_and_idempotent(self):
        before = copy.deepcopy(self.importer.data)
        self.assertEqual(self.apply()["after"]["linked"], 1)
        self.assertEqual(
            self.importer.data[0]["exchanges"][1:], before[0]["exchanges"][1:]
        )
        self.assertEqual(self.importer.data[1], before[1])
        self.assertEqual(self.importer.data[0]["exchanges"][0]["amount"], 0.00011)
        self.assert_clean()
        once = copy.deepcopy(self.importer.data)
        self.apply()
        self.assertEqual(self.importer.data, once)

    def test_duplicate_exact_source_is_rejected_before_mutation(self):
        self.importer.data[0]["exchanges"].append(
            copy.deepcopy(self.importer.data[0]["exchanges"][0])
        )
        before = copy.deepcopy(self.importer.data)
        with self.assertRaisesRegex(ValueError, "Ambiguous amount-scoped source"):
            self.apply()
        self.assertEqual(self.importer.data, before)

    def test_invalid_or_noncanonical_rule_amount_rejected(self):
        before = copy.deepcopy(self.importer.data)
        for value in (0.00011, True, None, "nan", "inf", "0.000110", "1.1e-4"):
            with self.subTest(value=value):
                self.mapping["data"][0][0][-2] = value
                with self.assertRaisesRegex(
                    ValueError, "canonical finite numeric text"
                ):
                    self.apply()
                self.assertEqual(self.importer.data, before)

    def test_invalid_exchange_amount_rejected_before_mutation(self):
        for value in (True, None, "0.00011", float("inf")):
            with self.subTest(value=value):
                self.importer.data[0]["exchanges"][1]["amount"] = value
                before = copy.deepcopy(self.importer.data)
                with self.assertRaisesRegex(ValueError, "finite numeric amounts"):
                    self.apply()
                self.assertEqual(self.importer.data, before)

    def test_reserved_amount_field_preserved_and_rejected(self):
        self.importer.data[1]["exchanges"][0][AMOUNT_FIELD] = "keep this"
        before = copy.deepcopy(self.importer.data)
        with self.assertRaisesRegex(ValueError, "Reserved migration field"):
            self.apply()
        self.assertEqual(self.importer.data, before)

    def test_cleanup_after_migration_copies_records_then_fails(self):
        self.importer.fail = True
        before = copy.deepcopy(self.importer.data)
        with self.assertRaisesRegex(RuntimeError, "migration failed"):
            self.apply()
        self.assertEqual(self.importer.data, before)
        self.assert_clean()

    def test_already_linked_source_rejected(self):
        self.importer.data[0]["exchanges"][0]["input"] = ("old", "link")
        before = copy.deepcopy(self.importer.data)
        with self.assertRaisesRegex(ValueError, "already linked"):
            self.apply()
        self.assertEqual(self.importer.data, before)


if __name__ == "__main__":
    unittest.main()
