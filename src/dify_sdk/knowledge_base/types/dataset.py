# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dataset_external_knowledge_info import DatasetExternalKnowledgeInfo
from .dataset_external_retrieval_model import DatasetExternalRetrievalModel
from .dataset_indexing_technique import DatasetIndexingTechnique
from .dataset_permission import DatasetPermission
from .dataset_provider import DatasetProvider
from .dataset_retrieval_model_dict import DatasetRetrievalModelDict


class Dataset(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Knowledge Base ID
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Knowledge Base name
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Knowledge Base description
    """

    provider: typing.Optional[DatasetProvider] = pydantic.Field(default=None)
    """
    Knowledge Base provider
    """

    permission: typing.Optional[DatasetPermission] = pydantic.Field(default=None)
    """
    Access permission
    """

    data_source_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Data source type
    """

    indexing_technique: typing.Optional[DatasetIndexingTechnique] = pydantic.Field(default=None)
    """
    Indexing technique
    """

    app_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of applications
    """

    document_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of documents
    """

    word_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Word count
    """

    created_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    Creator ID
    """

    created_at: typing.Optional[float] = pydantic.Field(default=None)
    """
    Creation timestamp
    """

    updated_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    Last updated by ID
    """

    updated_at: typing.Optional[float] = pydantic.Field(default=None)
    """
    Last updated timestamp
    """

    embedding_model: typing.Optional[str] = pydantic.Field(default=None)
    """
    Embedding model name
    """

    embedding_model_provider: typing.Optional[str] = pydantic.Field(default=None)
    """
    Embedding model provider
    """

    embedding_available: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether embedding is available
    """

    retrieval_model_dict: typing.Optional[DatasetRetrievalModelDict] = pydantic.Field(default=None)
    """
    Retrieval model configuration
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Tags list
    """

    doc_form: typing.Optional[str] = pydantic.Field(default=None)
    """
    Document form
    """

    external_knowledge_info: typing.Optional[DatasetExternalKnowledgeInfo] = pydantic.Field(default=None)
    """
    External knowledge information
    """

    external_retrieval_model: typing.Optional[DatasetExternalRetrievalModel] = pydantic.Field(default=None)
    """
    External retrieval model
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
