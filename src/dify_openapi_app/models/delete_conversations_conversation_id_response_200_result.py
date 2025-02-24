from typing import Literal, cast

DeleteConversationsConversationIdResponse200Result = Literal["success"]

DELETE_CONVERSATIONS_CONVERSATION_ID_RESPONSE_200_RESULT_VALUES: set[
    DeleteConversationsConversationIdResponse200Result
] = {
    "success",
}


def check_delete_conversations_conversation_id_response_200_result(
    value: str,
) -> DeleteConversationsConversationIdResponse200Result:
    if (
        value in DELETE_CONVERSATIONS_CONVERSATION_ID_RESPONSE_200_RESULT_VALUES or value is None
    ):  # NOTE: @l8ng skip check for some case
        return cast(DeleteConversationsConversationIdResponse200Result, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DELETE_CONVERSATIONS_CONVERSATION_ID_RESPONSE_200_RESULT_VALUES!r}"
    )
