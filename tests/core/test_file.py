import io
import pytest

from dify_sdk.core.file import convert_file_dict_to_httpx_tuples, with_content_type


def test_convert_file_dict_to_httpx_tuples_single_file():
    """Test converting a dictionary with a single file to HTTPX tuples."""
    # Create a test file
    test_file = io.BytesIO(b"test content")
    file_dict = {"file": test_file}

    # Convert to HTTPX tuples
    result = convert_file_dict_to_httpx_tuples(file_dict)

    # Check the result
    assert len(result) == 1
    assert result[0][0] == "file"
    assert result[0][1] == test_file


def test_convert_file_dict_to_httpx_tuples_multiple_files():
    """Test converting a dictionary with multiple files to HTTPX tuples."""
    # Create test files
    test_file1 = io.BytesIO(b"test content 1")
    test_file2 = io.BytesIO(b"test content 2")
    file_dict = {"file": [test_file1, test_file2]}

    # Convert to HTTPX tuples
    result = convert_file_dict_to_httpx_tuples(file_dict)

    # Check the result
    assert len(result) == 2
    assert result[0][0] == "file"
    assert result[0][1] == test_file1
    assert result[1][0] == "file"
    assert result[1][1] == test_file2


def test_convert_file_dict_to_httpx_tuples_mixed():
    """Test converting a dictionary with both single and multiple files."""
    # Create test files
    test_file1 = io.BytesIO(b"test content 1")
    test_file2 = io.BytesIO(b"test content 2")
    test_file3 = io.BytesIO(b"test content 3")
    file_dict = {"file1": test_file1, "file2": [test_file2, test_file3]}

    # Convert to HTTPX tuples
    result = convert_file_dict_to_httpx_tuples(file_dict)

    # Check the result
    assert len(result) == 3
    assert result[0][0] == "file1"
    assert result[0][1] == test_file1
    assert result[1][0] == "file2"
    assert result[1][1] == test_file2
    assert result[2][0] == "file2"
    assert result[2][1] == test_file3


def test_with_content_type_file_only():
    """Test adding content type to a file-only input."""
    # Create a test file
    test_file = io.BytesIO(b"test content")

    # Add content type
    result = with_content_type(file=test_file, default_content_type="application/octet-stream")

    # Check the result
    assert len(result) == 3
    assert result[0] is None  # No filename
    assert result[1] == test_file
    assert result[2] == "application/octet-stream"


def test_with_content_type_filename_and_file():
    """Test adding content type to a (filename, file) tuple."""
    # Create a test file
    test_file = io.BytesIO(b"test content")
    file_tuple = ("test.txt", test_file)

    # Add content type
    result = with_content_type(file=file_tuple, default_content_type="application/octet-stream")

    # Check the result
    assert len(result) == 3
    assert result[0] == "test.txt"
    assert result[1] == test_file
    assert result[2] == "application/octet-stream"


def test_with_content_type_with_existing_content_type():
    """Test adding content type when one is already provided."""
    # Create a test file
    test_file = io.BytesIO(b"test content")
    file_tuple = ("test.txt", test_file, "text/plain")

    # Add content type
    result = with_content_type(file=file_tuple, default_content_type="application/octet-stream")

    # Check the result
    assert len(result) == 3
    assert result[0] == "test.txt"
    assert result[1] == test_file
    assert result[2] == "text/plain"  # Original content type is preserved


def test_with_content_type_with_headers():
    """Test adding content type to a tuple with headers."""
    # Create a test file
    test_file = io.BytesIO(b"test content")
    headers = {"Content-Disposition": "attachment; filename=test.txt"}
    file_tuple = ("test.txt", test_file, None, headers)

    # Add content type
    result = with_content_type(file=file_tuple, default_content_type="application/octet-stream")

    # Check the result
    assert len(result) == 4
    assert result[0] == "test.txt"
    assert result[1] == test_file
    assert result[2] == "application/octet-stream"
    assert result[3] == headers


def test_with_content_type_with_existing_content_type_and_headers():
    """Test adding content type when one is already provided with headers."""
    # Create a test file
    test_file = io.BytesIO(b"test content")
    headers = {"Content-Disposition": "attachment; filename=test.txt"}
    file_tuple = ("test.txt", test_file, "text/plain", headers)

    # Add content type
    result = with_content_type(file=file_tuple, default_content_type="application/octet-stream")

    # Check the result
    assert len(result) == 4
    assert result[0] == "test.txt"
    assert result[1] == test_file
    assert result[2] == "text/plain"  # Original content type is preserved
    assert result[3] == headers


def test_with_content_type_invalid_tuple_length():
    """Test adding content type to a tuple with invalid length."""
    # Create an invalid tuple (too many elements)
    invalid_tuple = ("test.txt", io.BytesIO(b"test"), "text/plain", {}, "extra")

    # Check that an error is raised
    with pytest.raises(ValueError, match="Unexpected tuple length"):
        with_content_type(file=invalid_tuple, default_content_type="application/octet-stream")
