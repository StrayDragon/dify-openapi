# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetApplicationParametersByAppAdvancedChatResponseSuggestedQuestionsAfterAnswer(UniversalBaseModel):
    """
    Enable recommended questions after answer
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to enable
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
