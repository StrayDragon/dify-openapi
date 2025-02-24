from typing import Literal, cast

PostChatMessagesBodyResponseMode = Literal["blocking", "streaming"]

POST_CHAT_MESSAGES_BODY_RESPONSE_MODE_VALUES: set[PostChatMessagesBodyResponseMode] = {
    "blocking",
    "streaming",
}


def check_post_chat_messages_body_response_mode(value: str) -> PostChatMessagesBodyResponseMode:
    if value in POST_CHAT_MESSAGES_BODY_RESPONSE_MODE_VALUES or value is None:  # NOTE: @l8ng skip check for some case
        return cast(PostChatMessagesBodyResponseMode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POST_CHAT_MESSAGES_BODY_RESPONSE_MODE_VALUES!r}")
