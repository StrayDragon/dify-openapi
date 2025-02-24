from typing import Literal, cast

CreateDatasetRequestPermission = Literal["all_team_members", "only_me", "partial_members"]

CREATE_DATASET_REQUEST_PERMISSION_VALUES: set[CreateDatasetRequestPermission] = {
    "all_team_members",
    "only_me",
    "partial_members",
}


def check_create_dataset_request_permission(value: str) -> CreateDatasetRequestPermission:
    if value in CREATE_DATASET_REQUEST_PERMISSION_VALUES or value is None:  # NOTE: @l8ng skip check for some case
        return cast(CreateDatasetRequestPermission, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_DATASET_REQUEST_PERMISSION_VALUES!r}")
