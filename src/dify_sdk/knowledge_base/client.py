# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .datasets.client import AsyncDatasetsClient, DatasetsClient
from .documents.client import AsyncDocumentsClient, DocumentsClient
from .metadata.client import AsyncMetadataClient, MetadataClient
from .models.client import AsyncModelsClient, ModelsClient
from .raw_client import AsyncRawKnowledgeBaseClient, RawKnowledgeBaseClient
from .segments.client import AsyncSegmentsClient, SegmentsClient
from .tags.client import AsyncTagsClient, TagsClient


class KnowledgeBaseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawKnowledgeBaseClient(client_wrapper=client_wrapper)
        self.datasets = DatasetsClient(client_wrapper=client_wrapper)

        self.documents = DocumentsClient(client_wrapper=client_wrapper)

        self.segments = SegmentsClient(client_wrapper=client_wrapper)

        self.metadata = MetadataClient(client_wrapper=client_wrapper)

        self.models = ModelsClient(client_wrapper=client_wrapper)

        self.tags = TagsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawKnowledgeBaseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawKnowledgeBaseClient
        """
        return self._raw_client


class AsyncKnowledgeBaseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawKnowledgeBaseClient(client_wrapper=client_wrapper)
        self.datasets = AsyncDatasetsClient(client_wrapper=client_wrapper)

        self.documents = AsyncDocumentsClient(client_wrapper=client_wrapper)

        self.segments = AsyncSegmentsClient(client_wrapper=client_wrapper)

        self.metadata = AsyncMetadataClient(client_wrapper=client_wrapper)

        self.models = AsyncModelsClient(client_wrapper=client_wrapper)

        self.tags = AsyncTagsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawKnowledgeBaseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawKnowledgeBaseClient
        """
        return self._raw_client
