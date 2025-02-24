from typing import Literal, cast

DatasetPermission = Literal["all_team_members", "only_me", "partial_members"]

DATASET_PERMISSION_VALUES: set[DatasetPermission] = {
    "all_team_members",
    "only_me",
    "partial_members",
}


def check_dataset_permission(value: str) -> DatasetPermission:
    if value in DATASET_PERMISSION_VALUES or value is None:  # NOTE: @l8ng skip check for some case
        return cast(DatasetPermission, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATASET_PERMISSION_VALUES!r}")
