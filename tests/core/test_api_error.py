import pytest

from dify_sdk.core.api_error import ApiError


def test_api_error_initialization():
    """Test initializing ApiError."""
    # Create an ApiError with status code and body
    error = ApiError(status_code=404, body={"message": "Not found"})

    # Check the attributes
    assert error.status_code == 404
    assert error.body == {"message": "Not found"}


def test_api_error_initialization_with_none():
    """Test initializing ApiError with None values."""
    # Create an ApiError with None values
    error = ApiError()

    # Check the attributes
    assert error.status_code is None
    assert error.body is None


def test_api_error_str_representation():
    """Test the string representation of ApiError."""
    # Create an ApiError
    error = ApiError(status_code=500, body={"message": "Internal server error"})

    # Check the string representation
    assert str(error) == "status_code: 500, body: {'message': 'Internal server error'}"


def test_api_error_as_exception():
    """Test using ApiError as an exception."""

    # Define a function that raises ApiError
    def raise_api_error():
        raise ApiError(status_code=400, body={"message": "Bad request"})

    # Check that the function raises ApiError
    with pytest.raises(ApiError) as excinfo:
        raise_api_error()

    # Check the attributes of the raised exception
    assert excinfo.value.status_code == 400
    assert excinfo.value.body == {"message": "Bad request"}
