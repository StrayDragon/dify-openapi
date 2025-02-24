from typing import Literal, cast

CreateDocumentByFileBodyDataDocForm = Literal["hierarchical_model", "qa_model", "text_model"]

CREATE_DOCUMENT_BY_FILE_BODY_DATA_DOC_FORM_VALUES: set[CreateDocumentByFileBodyDataDocForm] = {
    "hierarchical_model",
    "qa_model",
    "text_model",
}


def check_create_document_by_file_body_data_doc_form(value: str) -> CreateDocumentByFileBodyDataDocForm:
    if (
        value in CREATE_DOCUMENT_BY_FILE_BODY_DATA_DOC_FORM_VALUES or value is None
    ):  # NOTE: @l8ng skip check for some case
        return cast(CreateDocumentByFileBodyDataDocForm, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_DOCUMENT_BY_FILE_BODY_DATA_DOC_FORM_VALUES!r}"
    )
