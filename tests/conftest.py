import os
import pytest

from dataclasses import dataclass

import dify_openapi_app
import dify_openapi_datasets

DIFY_HOST = os.environ.get("TEST_DIFY_HOST") or "https://api.dify.ai/v1"

@dataclass(frozen=True)
class AllClient:
    client: dify_openapi_datasets.AuthenticatedClient
    app_client: dify_openapi_app.AuthenticatedClient


@pytest.fixture()
async def c():
    client = dify_openapi_datasets.AuthenticatedClient(
        base_url=DIFY_HOST,
        token=os.environ["TEST_DIFY_DATASETS_API_KEY"],
    )
    app_client = dify_openapi_app.AuthenticatedClient(
        base_url=DIFY_HOST,
        token=os.environ["TEST_DIFY_APP_CHAT_API_KEY"],
    )
    yield AllClient(
        client=client,
        app_client=app_client,
    )
