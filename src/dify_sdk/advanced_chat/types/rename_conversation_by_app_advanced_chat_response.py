# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class RenameConversationByAppAdvancedChatResponse(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Conversation ID
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Conversation name
    """

    inputs: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    User input parameters
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Conversation status
    """

    introduction: typing.Optional[str] = pydantic.Field(default=None)
    """
    Opening statement
    """

    created_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    Creation time
    """

    updated_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    Update time
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
