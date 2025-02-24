from typing import Literal, cast

DatasetIndexingTechnique = Literal["economy", "high_quality"]

DATASET_INDEXING_TECHNIQUE_VALUES: set[DatasetIndexingTechnique] = {
    "economy",
    "high_quality",
}


def check_dataset_indexing_technique(value: str) -> DatasetIndexingTechnique:
    if value in DATASET_INDEXING_TECHNIQUE_VALUES or value is None:  # NOTE: @l8ng skip check for some case
        return cast(DatasetIndexingTechnique, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATASET_INDEXING_TECHNIQUE_VALUES!r}")
