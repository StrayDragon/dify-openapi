# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class GetParametersResponseAnnotationReply(UniversalBaseModel):
    """
    Annotation reply settings
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether annotation reply is enabled
    """

    score_threshold: typing.Optional[float] = pydantic.Field(default=None)
    """
    Similarity score threshold
    """

    embedding_model: typing.Optional[str] = pydantic.Field(default=None)
    """
    Embedding model
    """

    embedding_model_provider: typing.Optional[str] = pydantic.Field(default=None)
    """
    Embedding model provider
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
