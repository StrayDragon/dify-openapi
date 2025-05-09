# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RetrieverResource(UniversalBaseModel):
    position: typing.Optional[int] = pydantic.Field(default=None)
    """
    Position
    """

    dataset_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Dataset ID
    """

    dataset_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Dataset name
    """

    document_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Document ID
    """

    document_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Document name
    """

    segment_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Segment ID
    """

    score: typing.Optional[float] = pydantic.Field(default=None)
    """
    Relevance score
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Content
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
