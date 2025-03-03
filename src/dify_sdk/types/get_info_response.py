# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class GetInfoResponse(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Application name
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Application description
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Application tags
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
