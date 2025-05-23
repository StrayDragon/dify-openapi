# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_application_parameters_by_app_generation_response_user_input_form_item_text_input_text_input import (
    GetApplicationParametersByAppGenerationResponseUserInputFormItemTextInputTextInput,
)


class GetApplicationParametersByAppGenerationResponseUserInputFormItemTextInput(UniversalBaseModel):
    text_input: typing_extensions.Annotated[
        typing.Optional[GetApplicationParametersByAppGenerationResponseUserInputFormItemTextInputTextInput],
        FieldMetadata(alias="text-input"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
