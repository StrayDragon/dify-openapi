import os
import warnings
import pytest

from dataclasses import dataclass

import dify_openapi_app
import dify_openapi_datasets

OFFICIAL_DIFY_HOST = "https://api.dify.ai/v1"

TEST_DIFY_HOST = os.environ.get("TEST_DIFY_HOST") or OFFICIAL_DIFY_HOST


@dataclass(frozen=True)
class AllClient:
    client: dify_openapi_datasets.AuthenticatedClient
    app_client: dify_openapi_app.AuthenticatedClient


@pytest.fixture()
async def c():
    client = dify_openapi_datasets.AuthenticatedClient(
        base_url=TEST_DIFY_HOST,
        token=os.environ["TEST_DIFY_DATASETS_API_KEY"],
    )
    app_client = dify_openapi_app.AuthenticatedClient(
        base_url=TEST_DIFY_HOST,
        token=os.environ["TEST_DIFY_APP_CHAT_API_KEY"],
    )
    yield AllClient(
        client=client,
        app_client=app_client,
    )


@pytest.fixture(autouse=True, scope="session")
def warning_info():
    if TEST_DIFY_HOST == OFFICIAL_DIFY_HOST:
        warnings.warn(
            "=== You are using the official Dify API, ensure you account has enough privileges and tokens! ==="
        )
