from typing import Literal, cast

PostMessagesMessageIdFeedbacksResponse200Result = Literal["success"]

POST_MESSAGES_MESSAGE_ID_FEEDBACKS_RESPONSE_200_RESULT_VALUES: set[PostMessagesMessageIdFeedbacksResponse200Result] = {
    "success",
}


def check_post_messages_message_id_feedbacks_response_200_result(
    value: str,
) -> PostMessagesMessageIdFeedbacksResponse200Result:
    if (
        value in POST_MESSAGES_MESSAGE_ID_FEEDBACKS_RESPONSE_200_RESULT_VALUES or value is None
    ):  # NOTE: @l8ng skip check for some case
        return cast(PostMessagesMessageIdFeedbacksResponse200Result, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MESSAGES_MESSAGE_ID_FEEDBACKS_RESPONSE_200_RESULT_VALUES!r}"
    )
