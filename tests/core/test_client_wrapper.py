import httpx

from dify_sdk.core.client_wrapper import BaseClientWrapper, SyncClientWrapper, AsyncClientWrapper


def test_base_client_wrapper_initialization():
    """Test initializing BaseClientWrapper."""
    # Create a BaseClientWrapper with a string token
    client = BaseClientWrapper(token="test_token", base_url="https://api.example.com", timeout=30.0)

    # Check the attributes
    assert client._token == "test_token"
    assert client._base_url == "https://api.example.com"
    assert client._timeout == 30.0


def test_base_client_wrapper_with_callable_token():
    """Test BaseClientWrapper with a callable token."""

    # Define a token function
    def get_token() -> str:
        return "dynamic_token"

    # Create a BaseClientWrapper with a callable token
    client = BaseClientWrapper(token=get_token, base_url="https://api.example.com")

    # Check that the token function is called
    assert client._get_token() == "dynamic_token"


def test_base_client_wrapper_get_headers():
    """Test getting headers from BaseClientWrapper."""
    # Create a BaseClientWrapper
    client = BaseClientWrapper(token="test_token", base_url="https://api.example.com")

    # Get the headers
    headers = client.get_headers()

    # Check the headers
    assert "X-Fern-Language" in headers
    assert headers["X-Fern-Language"] == "Python"
    assert "Authorization" in headers
    assert headers["Authorization"] == "Bearer test_token"


def test_base_client_wrapper_get_base_url():
    """Test getting base URL from BaseClientWrapper."""
    # Create a BaseClientWrapper
    client = BaseClientWrapper(token="test_token", base_url="https://api.example.com")

    # Get the base URL
    base_url = client.get_base_url()

    # Check the base URL
    assert base_url == "https://api.example.com"


def test_base_client_wrapper_get_timeout():
    """Test getting timeout from BaseClientWrapper."""
    # Create a BaseClientWrapper with a timeout
    client_with_timeout = BaseClientWrapper(token="test_token", base_url="https://api.example.com", timeout=30.0)

    # Get the timeout
    timeout = client_with_timeout.get_timeout()

    # Check the timeout
    assert timeout == 30.0

    # Create a BaseClientWrapper without a timeout
    client_without_timeout = BaseClientWrapper(token="test_token", base_url="https://api.example.com")

    # Get the timeout
    timeout = client_without_timeout.get_timeout()

    # Check the timeout
    assert timeout is None


def test_sync_client_wrapper_initialization():
    """Test initializing SyncClientWrapper."""
    # Create a SyncClientWrapper
    client = SyncClientWrapper(
        token="test_token", base_url="https://api.example.com", timeout=30.0, httpx_client=httpx.Client()
    )

    # Check that the httpx_client is initialized
    assert client.httpx_client is not None


def test_async_client_wrapper_initialization():
    """Test initializing AsyncClientWrapper."""
    # Create an AsyncClientWrapper
    client = AsyncClientWrapper(
        token="test_token", base_url="https://api.example.com", timeout=30.0, httpx_client=httpx.AsyncClient()
    )

    # Check that the httpx_client is initialized
    assert client.httpx_client is not None
