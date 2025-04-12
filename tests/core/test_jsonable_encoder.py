import base64
import dataclasses
import datetime as dt
import enum
from pathlib import PurePath

import pydantic

from dify_sdk.core.jsonable_encoder import jsonable_encoder


class TestEnum(enum.Enum):
    VALUE1 = "value1"
    VALUE2 = "value2"


class TestModel(pydantic.BaseModel):
    name: str
    value: int
    optional: str | None = None

    class Config:
        allow_population_by_field_name = True


@dataclasses.dataclass
class TestDataClass:
    name: str
    value: int


def test_jsonable_encoder_none():
    """Test encoding None."""
    result = jsonable_encoder(None)
    assert result is None


def test_jsonable_encoder_primitive_types():
    """Test encoding primitive types."""
    assert jsonable_encoder("test") == "test"
    assert jsonable_encoder(42) == 42
    assert jsonable_encoder(3.14) == 3.14
    assert jsonable_encoder(True) is True
    assert jsonable_encoder(False) is False


def test_jsonable_encoder_bytes():
    """Test encoding bytes."""
    test_bytes = b"test bytes"
    result = jsonable_encoder(test_bytes)
    assert result == base64.b64encode(test_bytes).decode("utf-8")


def test_jsonable_encoder_enum():
    """Test encoding an enum."""
    result = jsonable_encoder(TestEnum.VALUE1)
    assert result == "value1"


def test_jsonable_encoder_path():
    """Test encoding a path."""
    test_path = PurePath("/test/path")
    result = jsonable_encoder(test_path)
    assert result == "/test/path"


def test_jsonable_encoder_datetime():
    """Test encoding a datetime."""
    test_dt = dt.datetime(2023, 1, 1, 12, 0, 0, tzinfo=dt.UTC)
    result = jsonable_encoder(test_dt)
    assert result == "2023-01-01T12:00:00Z"


def test_jsonable_encoder_date():
    """Test encoding a date."""
    test_date = dt.date(2023, 1, 1)
    result = jsonable_encoder(test_date)
    assert result == "2023-01-01"


def test_jsonable_encoder_dict():
    """Test encoding a dictionary."""
    test_dict = {"key1": "value1", "key2": 42, "key3": None}
    result = jsonable_encoder(test_dict)
    assert result == {"key1": "value1", "key2": 42, "key3": None}


def test_jsonable_encoder_nested_dict():
    """Test encoding a nested dictionary."""
    test_dict = {"key1": "value1", "key2": {"nested1": "nested_value1", "nested2": 42}}
    result = jsonable_encoder(test_dict)
    assert result == {"key1": "value1", "key2": {"nested1": "nested_value1", "nested2": 42}}


def test_jsonable_encoder_list():
    """Test encoding a list."""
    test_list = [1, "test", None, True]
    result = jsonable_encoder(test_list)
    assert result == [1, "test", None, True]


def test_jsonable_encoder_set():
    """Test encoding a set."""
    test_set = {1, 2, 3}
    result = jsonable_encoder(test_set)
    assert sorted(result) == [1, 2, 3]


def test_jsonable_encoder_pydantic_model():
    """Test encoding a Pydantic model."""
    test_model = TestModel(name="test", value=42)
    result = jsonable_encoder(test_model)
    assert result == {"name": "test", "value": 42, "optional": None}


def test_jsonable_encoder_dataclass():
    """Test encoding a dataclass."""
    test_dataclass = TestDataClass(name="test", value=42)
    result = jsonable_encoder(test_dataclass)
    assert result == {"name": "test", "value": 42}


def test_jsonable_encoder_custom_encoder():
    """Test encoding with a custom encoder."""

    def custom_encode_int(value: int) -> str:
        return f"custom-{value}"

    test_value = 42
    result = jsonable_encoder(test_value, custom_encoder={int: custom_encode_int})
    assert result == "custom-42"


def test_jsonable_encoder_complex_nested():
    """Test encoding a complex nested structure."""
    test_data = {
        "string": "value",
        "int": 42,
        "float": 3.14,
        "bool": True,
        "none": None,
        "list": [1, 2, 3],
        "dict": {"key": "value"},
        "model": TestModel(name="test", value=42),
        "enum": TestEnum.VALUE2,
        "date": dt.date(2023, 1, 1),
        "datetime": dt.datetime(2023, 1, 1, 12, 0, 0, tzinfo=dt.UTC),
        "bytes": b"test",
    }

    result = jsonable_encoder(test_data)

    assert result["string"] == "value"
    assert result["int"] == 42
    assert result["float"] == 3.14
    assert result["bool"] is True
    assert result["none"] is None
    assert result["list"] == [1, 2, 3]
    assert result["dict"] == {"key": "value"}
    assert result["model"] == {"name": "test", "value": 42, "optional": None}
    assert result["enum"] == "value2"
    assert result["date"] == "2023-01-01"
    assert result["datetime"] == "2023-01-01T12:00:00Z"
    assert result["bytes"] == base64.b64encode(b"test").decode("utf-8")
