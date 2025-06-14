# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_application_parameters_by_app_chat_response_text_to_speech_auto_play import (
    GetApplicationParametersByAppChatResponseTextToSpeechAutoPlay,
)


class GetApplicationParametersByAppChatResponseTextToSpeech(UniversalBaseModel):
    """
    Text to speech settings
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether enabled
    """

    voice: typing.Optional[str] = pydantic.Field(default=None)
    """
    Voice type
    """

    language: typing.Optional[str] = pydantic.Field(default=None)
    """
    Language
    """

    auto_play: typing_extensions.Annotated[
        typing.Optional[GetApplicationParametersByAppChatResponseTextToSpeechAutoPlay], FieldMetadata(alias="autoPlay")
    ] = pydantic.Field(default=None)
    """
    Auto play
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
