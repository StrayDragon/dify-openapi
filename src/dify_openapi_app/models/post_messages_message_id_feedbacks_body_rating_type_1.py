from typing import Literal, cast

PostMessagesMessageIdFeedbacksBodyRatingType1 = Literal["dislike", "like"]

POST_MESSAGES_MESSAGE_ID_FEEDBACKS_BODY_RATING_TYPE_1_VALUES: set[PostMessagesMessageIdFeedbacksBodyRatingType1] = {
    "dislike",
    "like",
}


def check_post_messages_message_id_feedbacks_body_rating_type_1(
    value: str,
) -> PostMessagesMessageIdFeedbacksBodyRatingType1:
    if (
        value in POST_MESSAGES_MESSAGE_ID_FEEDBACKS_BODY_RATING_TYPE_1_VALUES or value is None
    ):  # NOTE: @l8ng skip check for some case
        return cast(PostMessagesMessageIdFeedbacksBodyRatingType1, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {POST_MESSAGES_MESSAGE_ID_FEEDBACKS_BODY_RATING_TYPE_1_VALUES!r}"
    )
