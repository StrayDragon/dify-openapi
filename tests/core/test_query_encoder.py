import pydantic

from dify_sdk.core.query_encoder import encode_query, single_query_encoder, traverse_query_dict


class TestModel(pydantic.BaseModel):
    name: str
    value: int

    class Config:
        allow_population_by_field_name = True


class NestedTestModel(pydantic.BaseModel):
    id: str
    nested: TestModel

    class Config:
        allow_population_by_field_name = True


def test_traverse_query_dict_simple():
    """Test traversing a simple dictionary."""
    # Create a simple dictionary
    test_dict = {"a": 1, "b": "test"}

    # Traverse the dictionary
    result = traverse_query_dict(test_dict)

    # Check the result
    assert sorted(result) == sorted([("a", 1), ("b", "test")])


def test_traverse_query_dict_nested():
    """Test traversing a nested dictionary."""
    # Create a nested dictionary
    test_dict = {"a": 1, "b": {"c": 2, "d": "test"}}

    # Traverse the dictionary
    result = traverse_query_dict(test_dict)

    # Check the result
    assert sorted(result) == sorted([("a", 1), ("b[c]", 2), ("b[d]", "test")])


def test_traverse_query_dict_with_list():
    """Test traversing a dictionary with a list."""
    # Create a dictionary with a list
    test_dict = {"a": 1, "b": [1, 2, 3]}

    # Traverse the dictionary
    result = traverse_query_dict(test_dict)

    # Check the result
    assert sorted(result) == sorted([("a", 1), ("b", 1), ("b", 2), ("b", 3)])


def test_traverse_query_dict_with_list_of_dicts():
    """Test traversing a dictionary with a list of dictionaries."""
    # Create a dictionary with a list of dictionaries
    test_dict = {"a": 1, "b": [{"c": 2}, {"d": 3}]}

    # Traverse the dictionary
    result = traverse_query_dict(test_dict)

    # Check the result
    assert sorted(result) == sorted([("a", 1), ("b[c]", 2), ("b[d]", 3)])


def test_traverse_query_dict_deeply_nested():
    """Test traversing a deeply nested dictionary."""
    # Create a deeply nested dictionary
    test_dict = {"a": {"b": {"c": {"d": 1}}}}

    # Traverse the dictionary
    result = traverse_query_dict(test_dict)

    # Check the result
    assert result == [("a[b][c][d]", 1)]


def test_single_query_encoder_simple_value():
    """Test encoding a simple value."""
    # Encode a simple value
    result = single_query_encoder("key", "value")

    # Check the result
    assert result == [("key", "value")]


def test_single_query_encoder_dict():
    """Test encoding a dictionary."""
    # Create a dictionary
    test_dict = {"a": 1, "b": "test"}

    # Encode the dictionary
    result = single_query_encoder("key", test_dict)

    # Check the result
    assert sorted(result) == sorted([("key[a]", 1), ("key[b]", "test")])


def test_single_query_encoder_pydantic_model():
    """Test encoding a Pydantic model."""
    # Create a Pydantic model
    test_model = TestModel(name="test", value=42)

    # Encode the model
    result = single_query_encoder("key", test_model)

    # Check the result
    assert sorted(result) == sorted([("key[name]", "test"), ("key[value]", 42)])


def test_single_query_encoder_list_of_values():
    """Test encoding a list of values."""
    # Create a list of values
    test_list = [1, 2, 3]

    # Encode the list
    result = single_query_encoder("key", test_list)

    # Check the result
    assert sorted(result) == sorted([("key", 1), ("key", 2), ("key", 3)])


def test_single_query_encoder_list_of_dicts():
    """Test encoding a list of dictionaries."""
    # Create a list of dictionaries
    test_list = [{"a": 1}, {"b": 2}]

    # Encode the list
    result = single_query_encoder("key", test_list)

    # Check the result
    assert sorted(result) == sorted([("key[a]", 1), ("key[b]", 2)])


def test_single_query_encoder_list_of_models():
    """Test encoding a list of Pydantic models."""
    # Create a list of Pydantic models
    test_list = [TestModel(name="test1", value=1), TestModel(name="test2", value=2)]

    # Encode the list
    result = single_query_encoder("key", test_list)

    # Check the result
    expected = [("key[name]", "test1"), ("key[value]", 1), ("key[name]", "test2"), ("key[value]", 2)]
    assert sorted(result) == sorted(expected)


def test_encode_query_none():
    """Test encoding a None query."""
    # Encode a None query
    result = encode_query(None)

    # Check the result
    assert result is None


def test_encode_query_empty():
    """Test encoding an empty query."""
    # Encode an empty query
    result = encode_query({})

    # Check the result
    assert result == []


def test_encode_query_simple():
    """Test encoding a simple query."""
    # Create a simple query
    test_query = {"a": 1, "b": "test"}

    # Encode the query
    result = encode_query(test_query)

    # Check the result
    assert sorted(result) == sorted([("a", 1), ("b", "test")])


def test_encode_query_complex():
    """Test encoding a complex query."""
    # Create a complex query
    test_query = {"a": 1, "b": {"c": 2, "d": "test"}, "e": [1, 2, 3], "f": TestModel(name="test", value=42)}

    # Encode the query
    result = encode_query(test_query)

    # Check the result
    expected = [
        ("a", 1),
        ("b[c]", 2),
        ("b[d]", "test"),
        ("e", 1),
        ("e", 2),
        ("e", 3),
        ("f[name]", "test"),
        ("f[value]", 42),
    ]
    assert sorted(result) == sorted(expected)
