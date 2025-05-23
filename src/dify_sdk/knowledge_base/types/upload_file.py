# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UploadFile(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    File ID
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    File name
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    File size
    """

    extension: typing.Optional[str] = pydantic.Field(default=None)
    """
    File extension
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Preview URL
    """

    download_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Download URL
    """

    mime_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    MIME type
    """

    created_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    Creator ID
    """

    created_at: typing.Optional[float] = pydantic.Field(default=None)
    """
    Creation timestamp
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
