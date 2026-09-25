"""Regression checks for timestamp precision, offsets, and scoped restoration."""

from datetime import datetime, timedelta, timezone
import unittest

from pyecospold.lxmlh.config import TYPE_FUNC_MAP

from timestamp_compat import iso_timestamp_parser, parse_iso_timestamp


class TimestampCompatibilityTests(unittest.TestCase):
    def test_observed_failure_preserves_milliseconds_and_offset(self):
        actual = parse_iso_timestamp("2023-03-29T18:04:18.534+02:00")
        self.assertEqual(actual.microsecond, 534000)
        self.assertEqual(actual.utcoffset(), timedelta(hours=2))
        self.assertEqual(
            actual.astimezone(timezone.utc),
            datetime(2023, 3, 29, 16, 4, 18, 534000, tzinfo=timezone.utc),
        )

    def test_microsecond_precision_is_retained(self):
        actual = parse_iso_timestamp("2023-03-29T18:04:18.123456-05:30")
        self.assertEqual(actual.microsecond, 123456)
        self.assertEqual(actual.utcoffset(), -timedelta(hours=5, minutes=30))

    def test_naive_timestamps_stay_naive(self):
        self.assertEqual(
            parse_iso_timestamp("2023-03-29T18:04:18"), datetime(2023, 3, 29, 18, 4, 18)
        )

    def test_z_is_utc(self):
        self.assertEqual(
            parse_iso_timestamp("2023-03-29T18:04:18Z").utcoffset(), timedelta(0)
        )

    def test_observed_dataset_timestamp_with_space_separator(self):
        self.assertEqual(
            parse_iso_timestamp("2025-09-04 18:38:44.741718"),
            datetime(2025, 9, 4, 18, 38, 44, 741718),
        )

    def test_finer_precision_is_not_silently_lost(self):
        with self.assertRaisesRegex(ValueError, "precision"):
            parse_iso_timestamp("2023-03-29T18:04:18.1234567+02:00")

    def test_invalid_calendar_dates_are_rejected(self):
        with self.assertRaises(ValueError):
            parse_iso_timestamp("2023-02-30T18:04:18+02:00")

    def test_converter_is_restored_after_success(self):
        original = TYPE_FUNC_MAP[datetime]
        with iso_timestamp_parser():
            self.assertIs(TYPE_FUNC_MAP[datetime], parse_iso_timestamp)
        self.assertIs(TYPE_FUNC_MAP[datetime], original)

    def test_converter_is_restored_after_extraction_error(self):
        original = TYPE_FUNC_MAP[datetime]
        with self.assertRaisesRegex(RuntimeError, "extraction failed"):
            with iso_timestamp_parser():
                raise RuntimeError("extraction failed")
        self.assertIs(TYPE_FUNC_MAP[datetime], original)


if __name__ == "__main__":
    unittest.main()
