import dataclasses

from dify_sdk.datasets.client import AsyncDatasetsClient
from dify_sdk.documents.client import AsyncDocumentsClient
from dify_sdk.segments.client import AsyncSegmentsClient


@dataclasses.dataclass
class KnowledgeBaseClient:
    dataset: AsyncDatasetsClient
    document: AsyncDocumentsClient
    segment: AsyncSegmentsClient
