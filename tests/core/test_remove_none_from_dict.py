from dify_sdk.core.remove_none_from_dict import remove_none_from_dict


def test_remove_none_from_dict_empty():
    """Test removing None values from an empty dictionary."""
    # Create an empty dictionary
    test_dict = {}

    # Remove None values
    result = remove_none_from_dict(test_dict)

    # Check the result
    assert result == {}
    assert isinstance(result, dict)


def test_remove_none_from_dict_no_none_values():
    """Test removing None values from a dictionary with no None values."""
    # Create a dictionary with no None values
    test_dict = {"a": 1, "b": "test", "c": [1, 2, 3], "d": {"nested": "value"}}

    # Remove None values
    result = remove_none_from_dict(test_dict)

    # Check the result
    assert result == test_dict
    assert isinstance(result, dict)


def test_remove_none_from_dict_with_none_values():
    """Test removing None values from a dictionary with None values."""
    # Create a dictionary with None values
    test_dict = {"a": 1, "b": None, "c": [1, 2, 3], "d": None}

    # Remove None values
    result = remove_none_from_dict(test_dict)

    # Check the result
    assert result == {"a": 1, "c": [1, 2, 3]}
    assert isinstance(result, dict)
    assert "b" not in result
    assert "d" not in result


def test_remove_none_from_dict_all_none_values():
    """Test removing None values from a dictionary with all None values."""
    # Create a dictionary with all None values
    test_dict = {"a": None, "b": None, "c": None}

    # Remove None values
    result = remove_none_from_dict(test_dict)

    # Check the result
    assert result == {}
    assert isinstance(result, dict)


def test_remove_none_from_dict_with_falsy_values():
    """Test removing None values from a dictionary with falsy but non-None values."""
    # Create a dictionary with falsy but non-None values
    test_dict = {"a": 0, "b": "", "c": False, "d": [], "e": {}, "f": None}

    # Remove None values
    result = remove_none_from_dict(test_dict)

    # Check the result
    assert result == {"a": 0, "b": "", "c": False, "d": [], "e": {}}
    assert isinstance(result, dict)
    assert "f" not in result
