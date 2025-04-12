from typing_extensions import TypedDict
from typing import Annotated

import pydantic

from dify_sdk.core.serialization import (
    FieldMetadata,
    convert_and_respect_annotation_metadata,
    get_alias_to_field_mapping,
    get_field_to_alias_mapping,
)


class TestModel(pydantic.BaseModel):
    name: str
    value: int

    class Config:
        allow_population_by_field_name = True


class TestTypedDict(TypedDict):
    field1: str
    field2: int
    field3: Annotated[str, FieldMetadata(alias="aliased_field3")]


class TestNestedTypedDict(TypedDict):
    nested: TestTypedDict
    other: str


def test_field_metadata_initialization():
    """Test initializing FieldMetadata."""
    metadata = FieldMetadata(alias="test_alias")
    assert metadata.alias == "test_alias"


def test_convert_none():
    """Test converting None."""
    result = convert_and_respect_annotation_metadata(object_=None, annotation=str, direction="write")
    assert result is None


def test_convert_pydantic_model():
    """Test converting a Pydantic model."""
    model = TestModel(name="test", value=42)
    result = convert_and_respect_annotation_metadata(object_=model.dict(), annotation=TestModel, direction="write")
    assert result == {"name": "test", "value": 42}


def test_convert_typed_dict():
    """Test converting a TypedDict."""
    data = {"field1": "value1", "field2": 42, "field3": "value3"}
    result = convert_and_respect_annotation_metadata(object_=data, annotation=TestTypedDict, direction="write")
    assert result == {"field1": "value1", "field2": 42, "aliased_field3": "value3"}


def test_convert_dict():
    """Test converting a dictionary."""
    data = {"key1": "value1", "key2": 42}
    result = convert_and_respect_annotation_metadata(object_=data, annotation=dict[str, str | int], direction="write")
    assert result == {"key1": "value1", "key2": 42}


def test_convert_list():
    """Test converting a list."""
    data = [1, 2, 3]
    result = convert_and_respect_annotation_metadata(object_=data, annotation=list[int], direction="write")
    assert result == [1, 2, 3]


def test_convert_set():
    """Test converting a set."""
    data = {1, 2, 3}
    result = convert_and_respect_annotation_metadata(object_=data, annotation=set[int], direction="write")
    assert result == {1, 2, 3}


def test_convert_union():
    """Test converting a union type."""
    data = "test"
    result = convert_and_respect_annotation_metadata(object_=data, annotation=str | int, direction="write")
    assert result == "test"


def test_convert_nested_typed_dict():
    """Test converting a nested TypedDict."""
    data = {"nested": {"field1": "value1", "field2": 42, "field3": "value3"}, "other": "value"}
    result = convert_and_respect_annotation_metadata(object_=data, annotation=TestNestedTypedDict, direction="write")
    assert result == {"nested": {"field1": "value1", "field2": 42, "aliased_field3": "value3"}, "other": "value"}


def test_convert_read_direction():
    """Test converting with read direction."""
    data = {"field1": "value1", "field2": 42, "aliased_field3": "value3"}
    result = convert_and_respect_annotation_metadata(object_=data, annotation=TestTypedDict, direction="read")
    assert result == {"field1": "value1", "field2": 42, "field3": "value3"}


def test_get_alias_to_field_mapping():
    """Test getting alias to field mapping."""
    result = get_alias_to_field_mapping(TestTypedDict)
    assert result == {"aliased_field3": "field3"}


def test_get_field_to_alias_mapping():
    """Test getting field to alias mapping."""
    result = get_field_to_alias_mapping(TestTypedDict)
    assert result == {"field3": "aliased_field3"}
