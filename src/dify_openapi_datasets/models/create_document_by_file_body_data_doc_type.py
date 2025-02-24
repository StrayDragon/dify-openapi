from typing import Literal, cast

CreateDocumentByFileBodyDataDocType = Literal[
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

CREATE_DOCUMENT_BY_FILE_BODY_DATA_DOC_TYPE_VALUES: set[CreateDocumentByFileBodyDataDocType] = {
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


def check_create_document_by_file_body_data_doc_type(value: str) -> CreateDocumentByFileBodyDataDocType:
    if (
        value in CREATE_DOCUMENT_BY_FILE_BODY_DATA_DOC_TYPE_VALUES or value is None
    ):  # NOTE: @l8ng skip check for some case
        return cast(CreateDocumentByFileBodyDataDocType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_DOCUMENT_BY_FILE_BODY_DATA_DOC_TYPE_VALUES!r}"
    )
