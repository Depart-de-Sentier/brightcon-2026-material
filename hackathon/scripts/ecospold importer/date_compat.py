"""Scoped XML Schema date support for pyecospold's EcoSpold 1 time periods."""

from contextlib import contextmanager
from datetime import datetime
import re

XML_DATE = re.compile(
    r"(?P<day>[0-9]{4}-[0-9]{2}-[0-9]{2})(?P<offset>Z|[+-][0-9]{2}:[0-9]{2})?"
)


def parse_xml_date(value):
    """Read BAFU's complete dates without shifting the stated calendar day.

    Return a datetime at local midnight for compatibility with pyecospold's
    parse(...).date() calls. Retain the offset until that existing conversion to
    date; it is not converted to UTC. No time-of-day precision is added to XML.
    This supports observed four-digit AD years, not every XML Schema date form.
    """
    if not isinstance(value, str):
        raise ValueError(f"Expected a date string, got {type(value).__name__}")
    match = XML_DATE.fullmatch(value.strip())
    if match is None:
        raise ValueError(f"Unsupported XML Schema date: {value!r}")
    offset = match.group("offset") or ""
    if offset and offset != "Z":
        hours, minutes = (int(part) for part in offset[1:].split(":"))
        if hours > 14 or minutes > 59 or (hours == 14 and minutes != 0):
            raise ValueError(f"Invalid XML Schema date offset: {value!r}")
    return datetime.fromisoformat(
        f"{match.group('day')}T00:00:00{offset.replace('Z', '+00:00')}"
    )


@contextmanager
def xml_date_parser():
    """Temporarily adapt only the EcoSpold 1 model's local parser reference.

    Delegate partial dates and other inputs to the original parser so that the
    installed year/month period-boundary handling stays in effect. The standard
    schema validation still runs before extraction. As with the timestamp
    adapter, use only for single-threaded, non-multiprocessing extraction.
    """
    from pyecospold import model_v1

    original = model_v1.parse

    def parse(value, *args, **kwargs):
        if (
            not args
            and not kwargs
            and isinstance(value, str)
            and XML_DATE.fullmatch(value.strip())
        ):
            return parse_xml_date(value)
        return original(value, *args, **kwargs)

    model_v1.parse = parse
    try:
        yield
    finally:
        model_v1.parse = original
