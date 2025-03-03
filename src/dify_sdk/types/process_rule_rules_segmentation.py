# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ProcessRuleRulesSegmentation(UniversalBaseModel):
    """
    Segmentation configuration
    """

    separator: typing.Optional[str] = pydantic.Field(default=None)
    """
    Custom segmentation identifier
    """

    max_tokens: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum length (tokens)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
