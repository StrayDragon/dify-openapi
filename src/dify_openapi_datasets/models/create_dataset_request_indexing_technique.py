from typing import Literal, cast

CreateDatasetRequestIndexingTechnique = Literal["economy", "high_quality"]

CREATE_DATASET_REQUEST_INDEXING_TECHNIQUE_VALUES: set[CreateDatasetRequestIndexingTechnique] = {
    "economy",
    "high_quality",
}


def check_create_dataset_request_indexing_technique(value: str) -> CreateDatasetRequestIndexingTechnique:
    if (
        value in CREATE_DATASET_REQUEST_INDEXING_TECHNIQUE_VALUES or value is None
    ):  # NOTE: @l8ng skip check for some case
        return cast(CreateDatasetRequestIndexingTechnique, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_DATASET_REQUEST_INDEXING_TECHNIQUE_VALUES!r}")
