# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Segment(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Segment ID
    """

    position: typing.Optional[int] = pydantic.Field(default=None)
    """
    Position
    """

    document_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Document ID
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Content
    """

    answer: typing.Optional[str] = pydantic.Field(default=None)
    """
    Answer
    """

    word_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Word count
    """

    tokens: typing.Optional[int] = pydantic.Field(default=None)
    """
    Token count
    """

    keywords: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Keywords
    """

    index_node_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Index node ID
    """

    index_node_hash: typing.Optional[str] = pydantic.Field(default=None)
    """
    Index node hash
    """

    hit_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Hit count
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether enabled
    """

    disabled_at: typing.Optional[float] = pydantic.Field(default=None)
    """
    Disabled timestamp
    """

    disabled_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    Disabled by user ID
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Status
    """

    created_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    Creator ID
    """

    created_at: typing.Optional[float] = pydantic.Field(default=None)
    """
    Creation timestamp
    """

    indexing_at: typing.Optional[float] = pydantic.Field(default=None)
    """
    Indexing timestamp
    """

    completed_at: typing.Optional[float] = pydantic.Field(default=None)
    """
    Completion timestamp
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error message
    """

    stopped_at: typing.Optional[float] = pydantic.Field(default=None)
    """
    Stop timestamp
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
