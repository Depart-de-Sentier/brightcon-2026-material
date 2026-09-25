"""Regression checks for calendar days, offsets, and actual TimePeriod access."""

from datetime import date, datetime, timedelta
import unittest

from dateutil import parser as dateutil_parser
from lxml import etree
from pyecospold import model_v1
from pyecospold.core import EcospoldLookupV1
from pyecospold.lxmlh.config import TYPE_FUNC_MAP

from date_compat import parse_xml_date, xml_date_parser
from timestamp_compat import iso_timestamp_parser


def time_period(start_tag, start, end_tag, end):
    parser = etree.XMLParser()
    parser.set_element_class_lookup(EcospoldLookupV1())
    return etree.fromstring(
        (
            '<timePeriod xmlns="http://www.EcoInvent.org/EcoSpold01">'
            f"<{start_tag}>{start}</{start_tag}><{end_tag}>{end}</{end_tag}>"
            "</timePeriod>"
        ).encode(),
        parser,
    )


class DateCompatibilityTests(unittest.TestCase):
    def test_observed_failure_preserves_day_and_offset(self):
        actual = parse_xml_date("2023-12-31+01:00")
        self.assertEqual(actual.date(), date(2023, 12, 31))
        self.assertEqual(actual.utcoffset(), timedelta(hours=1))

    def test_timezone_forms_do_not_shift_the_calendar_day(self):
        for suffix, offset in (
            ("+14:00", timedelta(hours=14)),
            ("-14:00", timedelta(hours=-14)),
            ("-05:30", -timedelta(hours=5, minutes=30)),
            ("Z", timedelta(0)),
            ("+00:00", timedelta(0)),
            ("-00:00", timedelta(0)),
            ("", None),
        ):
            with self.subTest(suffix=suffix):
                actual = parse_xml_date(f"2024-01-01{suffix}")
                self.assertEqual(actual.date(), date(2024, 1, 1))
                self.assertEqual(actual.utcoffset(), offset)

    def test_invalid_dates_and_offsets_are_rejected(self):
        for value in (
            "2023-02-29+01:00",
            "2024-02-30Z",
            "2024-01-01+14:01",
            "2024-01-01-15:00",
            "2024-01-01+01:60",
            "2024-01-01+0100",
            "2024-01-01T12:00:00Z",
            "2024-01",
            "",
            None,
        ):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    parse_xml_date(value)

    def test_time_period_reads_offsets_without_rewriting_xml(self):
        period = time_period(
            "startDate", "2021-01-01+01:00", "endDate", "2023-12-31+01:00"
        )
        before = etree.tostring(period)
        with self.assertRaises(dateutil_parser.ParserError):
            _ = period.endDate
        with xml_date_parser():
            self.assertEqual(period.startDate, date(2021, 1, 1))
            self.assertEqual(period.endDate, date(2023, 12, 31))
        self.assertEqual(etree.tostring(period), before)

    def test_partial_period_bounds_remain_unchanged_including_leap_year(self):
        for start_tag, start, end_tag, end in (
            ("startYear", "2024", "endYear", "2024"),
            ("startYearMonth", "2024-02", "endYearMonth", "2024-02"),
        ):
            with self.subTest(start_tag=start_tag):
                baseline = time_period(start_tag, start, end_tag, end)
                expected = (baseline.startDate, baseline.endDate)
                with xml_date_parser():
                    adapted = time_period(start_tag, start, end_tag, end)
                    self.assertEqual((adapted.startDate, adapted.endDate), expected)
                if start_tag == "startYearMonth":
                    self.assertEqual(expected, (date(2024, 2, 1), date(2024, 2, 29)))

    def test_dateutil_itself_is_unchanged_and_original_reference_restored(self):
        original = model_v1.parse
        original_dateutil = dateutil_parser.parse
        with xml_date_parser():
            self.assertIsNot(model_v1.parse, original)
            self.assertIs(dateutil_parser.parse, original_dateutil)
            self.assertEqual(
                model_v1.parse("2024-02", default=datetime(2000, 1, 1)),
                original("2024-02", default=datetime(2000, 1, 1)),
            )
        self.assertIs(model_v1.parse, original)

    def test_both_adapters_are_restored_after_extraction_error(self):
        original_date = model_v1.parse
        original_timestamp = TYPE_FUNC_MAP[datetime]
        with self.assertRaisesRegex(RuntimeError, "extraction failed"):
            with iso_timestamp_parser(), xml_date_parser():
                raise RuntimeError("extraction failed")
        self.assertIs(model_v1.parse, original_date)
        self.assertIs(TYPE_FUNC_MAP[datetime], original_timestamp)


if __name__ == "__main__":
    unittest.main()
