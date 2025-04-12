# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .get_app_meta_info_by_app_generation_response_tool_icons_value import (
    GetAppMetaInfoByAppGenerationResponseToolIconsValue,
)
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class GetAppMetaInfoByAppGenerationResponse(UniversalBaseModel):
    tool_icons: typing.Optional[typing.Dict[str, GetAppMetaInfoByAppGenerationResponseToolIconsValue]] = pydantic.Field(
        default=None
    )
    """
    Tool icons
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
