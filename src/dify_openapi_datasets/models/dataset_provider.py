from typing import Literal, cast

DatasetProvider = Literal["external", "vendor"]

DATASET_PROVIDER_VALUES: set[DatasetProvider] = {
    "external",
    "vendor",
}


def check_dataset_provider(value: str) -> DatasetProvider:
    if value in DATASET_PROVIDER_VALUES or value is None:  # NOTE: @l8ng skip check for some case
        return cast(DatasetProvider, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATASET_PROVIDER_VALUES!r}")
