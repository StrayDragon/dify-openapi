# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .file_input_transfer_method import FileInputTransferMethod
from .file_input_type import FileInputType


class FileInput(UniversalBaseModel):
    type: typing.Optional[FileInputType] = pydantic.Field(default=None)
    """
    File type
    """

    transfer_method: typing.Optional[FileInputTransferMethod] = pydantic.Field(default=None)
    """
    Transfer method
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Remote URL
    """

    upload_file_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Upload file ID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
