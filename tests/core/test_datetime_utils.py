import datetime as dt
from zoneinfo import ZoneInfo

from dify_sdk.core.datetime_utils import serialize_datetime


def test_serialize_datetime_with_utc_timezone():
    """Test serializing a datetime with UTC timezone."""
    # Create a datetime with UTC timezone
    test_dt = dt.datetime(2023, 1, 1, 12, 0, 0, tzinfo=dt.UTC)

    # Serialize the datetime
    result = serialize_datetime(test_dt)

    # Check that the result ends with Z (UTC indicator)
    assert result.endswith("Z")
    assert result == "2023-01-01T12:00:00Z"


def test_serialize_datetime_with_non_utc_timezone():
    """Test serializing a datetime with a non-UTC timezone."""
    # Create a datetime with a non-UTC timezone
    test_dt = dt.datetime(2023, 1, 1, 12, 0, 0, tzinfo=ZoneInfo("America/New_York"))

    # Serialize the datetime
    result = serialize_datetime(test_dt)

    # Check that the result includes the timezone offset
    assert "+" in result or "-" in result
    # New York is UTC-5 (or UTC-4 during daylight saving)
    assert "-05:00" in result or "-04:00" in result


def test_serialize_datetime_without_timezone():
    """Test serializing a datetime without timezone info."""
    # Create a datetime without timezone
    test_dt = dt.datetime(2023, 1, 1, 12, 0, 0)

    # Serialize the datetime
    result = serialize_datetime(test_dt)

    # Check that the result includes some timezone information
    assert "+" in result or "-" in result or "Z" in result

    # The result should be in ISO format
    assert result.startswith("2023-01-01T12:00:00")
