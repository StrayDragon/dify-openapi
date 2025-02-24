from typing import Literal, cast

RetrieveDatasetBodyRetrievalModelSearchMethod = Literal[
    "full_text_search", "hybrid_search", "keyword_search", "semantic_search"
]

RETRIEVE_DATASET_BODY_RETRIEVAL_MODEL_SEARCH_METHOD_VALUES: set[RetrieveDatasetBodyRetrievalModelSearchMethod] = {
    "full_text_search",
    "hybrid_search",
    "keyword_search",
    "semantic_search",
}


def check_retrieve_dataset_body_retrieval_model_search_method(
    value: str,
) -> RetrieveDatasetBodyRetrievalModelSearchMethod:
    if (
        value in RETRIEVE_DATASET_BODY_RETRIEVAL_MODEL_SEARCH_METHOD_VALUES or value is None
    ):  # NOTE: @l8ng skip check for some case
        return cast(RetrieveDatasetBodyRetrievalModelSearchMethod, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RETRIEVE_DATASET_BODY_RETRIEVAL_MODEL_SEARCH_METHOD_VALUES!r}"
    )
