import dataclasses
import asyncio
import os
import importlib.metadata
from packaging.version import Version

from dify_sdk.knowledge_base.datasets.client import AsyncDatasetsClient
from dify_sdk.knowledge_base.documents.client import AsyncDocumentsClient
from dify_sdk.knowledge_base.metadata.client import AsyncMetadataClient
from dify_sdk.knowledge_base.models.client import AsyncModelsClient
from dify_sdk.knowledge_base.segments.client import AsyncSegmentsClient


PROJECT_NAME = "dify-openapi"
PROJECT_VERSION = importlib.metadata.version(PROJECT_NAME)


def postpone_run_in_this_version(target_version: str) -> bool:
    if not need_skip_run_until_this_version(target_version):
        raise Exception("This version need run this logic or remove this check!")
    return False


def need_skip_run_until_this_version(target_version: str) -> bool:
    return Version(target_version) > Version(PROJECT_VERSION)


RUNNING_IN_CI = any(
    [
        os.getenv("GITHUB_ACTIONS"),
    ]
)


@dataclasses.dataclass
class KnowledgeBaseClient:
    dataset: AsyncDatasetsClient
    document: AsyncDocumentsClient
    segment: AsyncSegmentsClient
    metadata: AsyncMetadataClient
    models: AsyncModelsClient


async def wait_for_document_indexing_completed(
    kb_client: KnowledgeBaseClient,
    dataset_id: str,
    batch_id: str,
    n: int = 7,
) -> None:
    BREAK_STATUS = "completed"
    for sleep_time in (2**i for i in range(n)):
        status_response = await kb_client.document.get_document_indexing_status(
            dataset_id=dataset_id,
            batch=batch_id,
        )
        assert status_response is not None
        for data in status_response.data or []:
            if data.indexing_status == BREAK_STATUS:
                return
        await asyncio.sleep(sleep_time)
    raise Exception("文档索引失败")
