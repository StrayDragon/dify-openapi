import os
import warnings
import httpx
import pytest
from typing import AsyncGenerator

from dify_sdk.client import AsyncDifyApi
from dify_sdk_testing import KnowledgeBaseClient

OFFICIAL_DIFY_HOST = "https://api.dify.ai/v1"
TEST_DIFY_HOST = os.environ.get("TEST_DIFY_HOST") or OFFICIAL_DIFY_HOST


@pytest.fixture(autouse=True, scope="session")
def warning_info() -> None:
    if TEST_DIFY_HOST == OFFICIAL_DIFY_HOST:
        warnings.warn(
            "=== You are using the official Dify API, ensure you account has enough privileges and tokens! ==="
        )


@pytest.fixture()
async def app_chat_client() -> AsyncGenerator[AsyncDifyApi, None]:
    client = AsyncDifyApi(
        token=os.environ["TEST_DIFY_APP_CHAT_API_KEY"],
        base_url=TEST_DIFY_HOST,
        httpx_client=httpx.AsyncClient(
            timeout=60,
            follow_redirects=True,
            transport=httpx.AsyncHTTPTransport(retries=3),
        ),
    )
    yield client


@pytest.fixture()
async def app_workflow_client() -> AsyncGenerator[AsyncDifyApi, None]:
    client = AsyncDifyApi(
        token=os.environ["TEST_DIFY_APP_WORKFLOW_API_KEY"],
        base_url=TEST_DIFY_HOST,
    )
    yield client


@pytest.fixture()
async def app_completion_client() -> AsyncGenerator[AsyncDifyApi, None]:
    client = AsyncDifyApi(
        token=os.environ["TEST_DIFY_APP_COMPLETION_API_KEY"],
        base_url=TEST_DIFY_HOST,
    )
    yield client


@pytest.fixture()
async def kb_client() -> AsyncGenerator[KnowledgeBaseClient, None]:
    client = AsyncDifyApi(
        token=os.environ["TEST_DIFY_KNOWLEDGE_BASE_API_KEY"],
        base_url=TEST_DIFY_HOST,
    )
    yield KnowledgeBaseClient(
        dataset=client.datasets,
        document=client.documents,
        segment=client.segments,
        metadata=client.metadata,
    )
