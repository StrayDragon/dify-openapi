from typing import Literal, cast

GetSegmentsStatus = Literal["completed"]

GET_SEGMENTS_STATUS_VALUES: set[GetSegmentsStatus] = {
    "completed",
}


def check_get_segments_status(value: str) -> GetSegmentsStatus:
    if value in GET_SEGMENTS_STATUS_VALUES or value is None:  # NOTE: @l8ng skip check for some case
        return cast(GetSegmentsStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_SEGMENTS_STATUS_VALUES!r}")
