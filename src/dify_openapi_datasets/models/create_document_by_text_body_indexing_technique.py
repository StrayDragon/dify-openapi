from typing import Literal, cast

CreateDocumentByTextBodyIndexingTechnique = Literal["economy", "high_quality"]

CREATE_DOCUMENT_BY_TEXT_BODY_INDEXING_TECHNIQUE_VALUES: set[CreateDocumentByTextBodyIndexingTechnique] = {
    "economy",
    "high_quality",
}


def check_create_document_by_text_body_indexing_technique(value: str) -> CreateDocumentByTextBodyIndexingTechnique:
    if (
        value in CREATE_DOCUMENT_BY_TEXT_BODY_INDEXING_TECHNIQUE_VALUES or value is None
    ):  # NOTE: @l8ng skip check for some case
        return cast(CreateDocumentByTextBodyIndexingTechnique, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_DOCUMENT_BY_TEXT_BODY_INDEXING_TECHNIQUE_VALUES!r}"
    )
