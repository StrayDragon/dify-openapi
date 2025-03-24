import dataclasses
import asyncio
import os

from dify_sdk.datasets.client import AsyncDatasetsClient
from dify_sdk.documents.client import AsyncDocumentsClient
from dify_sdk.metadata.client import AsyncMetadataClient
from dify_sdk.segments.client import AsyncSegmentsClient


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
