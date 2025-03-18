# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class UpdateDocumentsMetadataRequestOperationDataItemMetadataListItem(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Metadata ID
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Metadata type
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    Metadata value
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Metadata name
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
