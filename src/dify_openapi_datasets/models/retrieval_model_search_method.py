from typing import Literal, cast

RetrievalModelSearchMethod = Literal["full_text_search", "hybrid_search", "keyword_search", "semantic_search"]

RETRIEVAL_MODEL_SEARCH_METHOD_VALUES: set[RetrievalModelSearchMethod] = {
    "full_text_search",
    "hybrid_search",
    "keyword_search",
    "semantic_search",
}


def check_retrieval_model_search_method(value: str) -> RetrievalModelSearchMethod:
    if value in RETRIEVAL_MODEL_SEARCH_METHOD_VALUES or value is None:  # NOTE: @l8ng skip check for some case
        return cast(RetrievalModelSearchMethod, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RETRIEVAL_MODEL_SEARCH_METHOD_VALUES!r}")
