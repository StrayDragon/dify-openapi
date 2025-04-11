# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class DatasetExternalRetrievalModel(UniversalBaseModel):
    """
    External retrieval model
    """

    top_k: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of results to return
    """

    score_threshold: typing.Optional[float] = pydantic.Field(default=None)
    """
    Score threshold
    """

    score_threshold_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether score threshold is enabled
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
