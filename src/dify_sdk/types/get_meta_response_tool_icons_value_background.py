# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class GetMetaResponseToolIconsValueBackground(UniversalBaseModel):
    background: typing.Optional[str] = pydantic.Field(default=None)
    """
    Background color in hex format
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Emoji
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
