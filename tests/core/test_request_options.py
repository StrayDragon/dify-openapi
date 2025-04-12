from typing import Any

from dify_sdk.core.request_options import RequestOptions


def test_request_options_empty():
    """Test creating an empty RequestOptions."""
    # Create an empty RequestOptions
    options: RequestOptions = {}

    # Check that it's empty
    assert len(options) == 0


def test_request_options_with_timeout():
    """Test RequestOptions with timeout_in_seconds."""
    # Create RequestOptions with timeout
    options: RequestOptions = {"timeout_in_seconds": 30}

    # Check the timeout
    assert options["timeout_in_seconds"] == 30


def test_request_options_with_max_retries():
    """Test RequestOptions with max_retries."""
    # Create RequestOptions with max_retries
    options: RequestOptions = {"max_retries": 3}

    # Check the max_retries
    assert options["max_retries"] == 3


def test_request_options_with_additional_headers():
    """Test RequestOptions with additional_headers."""
    # Create RequestOptions with additional_headers
    headers: dict[str, Any] = {"X-Custom-Header": "value"}
    options: RequestOptions = {"additional_headers": headers}

    # Check the additional_headers
    assert options["additional_headers"] == headers


def test_request_options_with_additional_query_parameters():
    """Test RequestOptions with additional_query_parameters."""
    # Create RequestOptions with additional_query_parameters
    query_params: dict[str, Any] = {"custom_param": "value"}
    options: RequestOptions = {"additional_query_parameters": query_params}

    # Check the additional_query_parameters
    assert options["additional_query_parameters"] == query_params


def test_request_options_with_additional_body_parameters():
    """Test RequestOptions with additional_body_parameters."""
    # Create RequestOptions with additional_body_parameters
    body_params: dict[str, Any] = {"custom_param": "value"}
    options: RequestOptions = {"additional_body_parameters": body_params}

    # Check the additional_body_parameters
    assert options["additional_body_parameters"] == body_params


def test_request_options_with_chunk_size():
    """Test RequestOptions with chunk_size."""
    # Create RequestOptions with chunk_size
    options: RequestOptions = {"chunk_size": 1024}

    # Check the chunk_size
    assert options["chunk_size"] == 1024


def test_request_options_with_multiple_parameters():
    """Test RequestOptions with multiple parameters."""
    # Create RequestOptions with multiple parameters
    options: RequestOptions = {
        "timeout_in_seconds": 30,
        "max_retries": 3,
        "additional_headers": {"X-Custom-Header": "value"},
        "additional_query_parameters": {"custom_param": "value"},
        "additional_body_parameters": {"custom_body_param": "value"},
        "chunk_size": 1024,
    }

    # Check all parameters
    assert options["timeout_in_seconds"] == 30
    assert options["max_retries"] == 3
    assert options["additional_headers"] == {"X-Custom-Header": "value"}
    assert options["additional_query_parameters"] == {"custom_param": "value"}
    assert options["additional_body_parameters"] == {"custom_body_param": "value"}
    assert options["chunk_size"] == 1024
