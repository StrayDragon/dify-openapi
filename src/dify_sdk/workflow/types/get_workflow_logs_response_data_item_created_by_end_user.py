# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetWorkflowLogsResponseDataItemCreatedByEndUser(UniversalBaseModel):
    """
    User
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifier
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type
    """

    is_anonymous: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether anonymous
    """

    session_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Session identifier
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
