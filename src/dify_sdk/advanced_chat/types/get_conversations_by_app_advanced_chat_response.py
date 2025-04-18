# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .get_conversations_by_app_advanced_chat_response_data_item import (
    GetConversationsByAppAdvancedChatResponseDataItem,
)
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class GetConversationsByAppAdvancedChatResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[GetConversationsByAppAdvancedChatResponseDataItem]] = pydantic.Field(default=None)
    """
    Conversation list
    """

    has_more: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether there is more data
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of returned items, if input exceeds system limit, returns system limit quantity
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
