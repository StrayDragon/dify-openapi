# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .document_data_source_info import DocumentDataSourceInfo
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Document(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Document ID
    """

    position: typing.Optional[int] = pydantic.Field(default=None)
    """
    Position
    """

    data_source_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Data source type
    """

    data_source_info: typing.Optional[DocumentDataSourceInfo] = pydantic.Field(default=None)
    """
    Data source information
    """

    dataset_process_rule_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Dataset process rule ID
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Document name
    """

    created_from: typing.Optional[str] = pydantic.Field(default=None)
    """
    Created from
    """

    created_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    Creator ID
    """

    created_at: typing.Optional[float] = pydantic.Field(default=None)
    """
    Creation timestamp
    """

    tokens: typing.Optional[int] = pydantic.Field(default=None)
    """
    Token count
    """

    indexing_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indexing status
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error message
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether enabled
    """

    disabled_at: typing.Optional[float] = pydantic.Field(default=None)
    """
    Disabled timestamp
    """

    disabled_by: typing.Optional[float] = pydantic.Field(default=None)
    """
    Disabled by user ID
    """

    archived: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether archived
    """

    display_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Display status
    """

    word_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Word count
    """

    hit_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Hit count
    """

    doc_form: typing.Optional[str] = pydantic.Field(default=None)
    """
    Document form
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
