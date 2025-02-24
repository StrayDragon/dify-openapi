from typing import Literal, cast

PostCompletionMessagesBodyResponseMode = Literal["blocking", "streaming"]

POST_COMPLETION_MESSAGES_BODY_RESPONSE_MODE_VALUES: set[PostCompletionMessagesBodyResponseMode] = {
    "blocking",
    "streaming",
}


def check_post_completion_messages_body_response_mode(value: str) -> PostCompletionMessagesBodyResponseMode:
    if (
        value in POST_COMPLETION_MESSAGES_BODY_RESPONSE_MODE_VALUES or value is None
    ):  # NOTE: @l8ng skip check for some case
        return cast(PostCompletionMessagesBodyResponseMode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_COMPLETION_MESSAGES_BODY_RESPONSE_MODE_VALUES!r}"
    )
