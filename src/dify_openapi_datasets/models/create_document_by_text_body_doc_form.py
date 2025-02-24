from typing import Literal, cast

CreateDocumentByTextBodyDocForm = Literal["hierarchical_model", "qa_model", "text_model"]

CREATE_DOCUMENT_BY_TEXT_BODY_DOC_FORM_VALUES: set[CreateDocumentByTextBodyDocForm] = {
    "hierarchical_model",
    "qa_model",
    "text_model",
}


def check_create_document_by_text_body_doc_form(value: str) -> CreateDocumentByTextBodyDocForm:
    if value in CREATE_DOCUMENT_BY_TEXT_BODY_DOC_FORM_VALUES or value is None:  # NOTE: @l8ng skip check for some case
        return cast(CreateDocumentByTextBodyDocForm, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_DOCUMENT_BY_TEXT_BODY_DOC_FORM_VALUES!r}")
