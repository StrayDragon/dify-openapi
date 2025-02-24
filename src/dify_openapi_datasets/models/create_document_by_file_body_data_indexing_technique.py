from typing import Literal, cast

CreateDocumentByFileBodyDataIndexingTechnique = Literal["economy", "high_quality"]

CREATE_DOCUMENT_BY_FILE_BODY_DATA_INDEXING_TECHNIQUE_VALUES: set[CreateDocumentByFileBodyDataIndexingTechnique] = {
    "economy",
    "high_quality",
}


def check_create_document_by_file_body_data_indexing_technique(
    value: str,
) -> CreateDocumentByFileBodyDataIndexingTechnique:
    if (
        value in CREATE_DOCUMENT_BY_FILE_BODY_DATA_INDEXING_TECHNIQUE_VALUES or value is None
    ):  # NOTE: @l8ng skip check for some case
        return cast(CreateDocumentByFileBodyDataIndexingTechnique, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_DOCUMENT_BY_FILE_BODY_DATA_INDEXING_TECHNIQUE_VALUES!r}"
    )
