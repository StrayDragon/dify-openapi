from typing import Literal, cast

CreateDatasetRequestProvider = Literal["external", "vendor"]

CREATE_DATASET_REQUEST_PROVIDER_VALUES: set[CreateDatasetRequestProvider] = {
    "external",
    "vendor",
}


def check_create_dataset_request_provider(value: str) -> CreateDatasetRequestProvider:
    if value in CREATE_DATASET_REQUEST_PROVIDER_VALUES or value is None:  # NOTE: @l8ng skip check for some case
        return cast(CreateDatasetRequestProvider, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_DATASET_REQUEST_PROVIDER_VALUES!r}")
