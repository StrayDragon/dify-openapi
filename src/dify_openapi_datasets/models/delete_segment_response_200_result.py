from typing import Literal, cast

DeleteSegmentResponse200Result = Literal["success"]

DELETE_SEGMENT_RESPONSE_200_RESULT_VALUES: set[DeleteSegmentResponse200Result] = {
    "success",
}


def check_delete_segment_response_200_result(value: str) -> DeleteSegmentResponse200Result:
    if value in DELETE_SEGMENT_RESPONSE_200_RESULT_VALUES or value is None:  # NOTE: @l8ng skip check for some case
        return cast(DeleteSegmentResponse200Result, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DELETE_SEGMENT_RESPONSE_200_RESULT_VALUES!r}")
