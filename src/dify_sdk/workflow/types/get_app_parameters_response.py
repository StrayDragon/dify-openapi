# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .get_app_parameters_response_user_input_form_item import (
    GetAppParametersResponseUserInputFormItem,
)
import pydantic
from .get_app_parameters_response_file_upload import GetAppParametersResponseFileUpload
from .get_app_parameters_response_system_parameters import (
    GetAppParametersResponseSystemParameters,
)
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class GetAppParametersResponse(UniversalBaseModel):
    user_input_form: typing.Optional[typing.List[GetAppParametersResponseUserInputFormItem]] = pydantic.Field(
        default=None
    )
    """
    User input form configuration
    """

    file_upload: typing.Optional[GetAppParametersResponseFileUpload] = pydantic.Field(default=None)
    """
    File upload configuration
    """

    system_parameters: typing.Optional[GetAppParametersResponseSystemParameters] = pydantic.Field(default=None)
    """
    System parameters
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
