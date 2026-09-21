"""Scoped ISO timestamp support for pyecospold's datetime conversion."""

from contextlib import contextmanager
from datetime import datetime
import re

TIMESTAMP = re.compile(
    r"\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}:\d{2}"
    r"(?:\.(?P<fraction>\d+))?(?:Z|[+-]\d{2}:\d{2})?"
)


def parse_iso_timestamp(value):
    """Preserve fractional seconds and UTC offsets for BAFU's ISO timestamps.

    Python datetime has microsecond precision. Reject finer precision explicitly
    instead of letting fromisoformat silently truncate it. This is an adapter for
    the observed BAFU timestamp forms, not a replacement XML Schema validator.
    """
    if not isinstance(value, str):
        raise ValueError(f"Expected a timestamp string, got {type(value).__name__}")
    value = value.strip()
    match = TIMESTAMP.fullmatch(value)
    if match is None:
        raise ValueError(f"Unsupported ISO timestamp: {value!r}")
    if len(match.group("fraction") or "") > 6:
        raise ValueError(f"Timestamp exceeds Python's microsecond precision: {value!r}")
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


@contextmanager
def iso_timestamp_parser():
    """Temporarily replace pyecospold's converter in this single-process import.

    The original converter is restored on both success and failure. This changes
    a process-global mapping and is intended for the CLI's single-threaded,
    non-multiprocessing extraction step.
    """
    from pyecospold.lxmlh.config import TYPE_FUNC_MAP

    original = TYPE_FUNC_MAP[datetime]
    TYPE_FUNC_MAP[datetime] = parse_iso_timestamp
    try:
        yield
    finally:
        TYPE_FUNC_MAP[datetime] = original
