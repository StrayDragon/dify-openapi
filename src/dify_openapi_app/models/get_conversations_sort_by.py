from typing import Literal, cast

GetConversationsSortBy = Literal["-created_at", "-updated_at", "created_at", "updated_at"]

GET_CONVERSATIONS_SORT_BY_VALUES: set[GetConversationsSortBy] = {
    "-created_at",
    "-updated_at",
    "created_at",
    "updated_at",
}


def check_get_conversations_sort_by(value: str) -> GetConversationsSortBy:
    if value in GET_CONVERSATIONS_SORT_BY_VALUES or value is None:  # NOTE: @l8ng skip check for some case
        return cast(GetConversationsSortBy, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_CONVERSATIONS_SORT_BY_VALUES!r}")
