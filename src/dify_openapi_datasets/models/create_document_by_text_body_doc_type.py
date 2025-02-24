from typing import Literal, cast

CreateDocumentByTextBodyDocType = Literal[
    "book",
    "business_document",
    "im_chat_log",
    "others",
    "paper",
    "personal_document",
    "social_media_post",
    "synced_from_github",
    "synced_from_notion",
    "web_page",
    "wikipedia_entry",
]

CREATE_DOCUMENT_BY_TEXT_BODY_DOC_TYPE_VALUES: set[CreateDocumentByTextBodyDocType] = {
    "book",
    "business_document",
    "im_chat_log",
    "others",
    "paper",
    "personal_document",
    "social_media_post",
    "synced_from_github",
    "synced_from_notion",
    "web_page",
    "wikipedia_entry",
}


def check_create_document_by_text_body_doc_type(value: str) -> CreateDocumentByTextBodyDocType:
    if value in CREATE_DOCUMENT_BY_TEXT_BODY_DOC_TYPE_VALUES or value is None:  # NOTE: @l8ng skip check for some case
        return cast(CreateDocumentByTextBodyDocType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CREATE_DOCUMENT_BY_TEXT_BODY_DOC_TYPE_VALUES!r}")
