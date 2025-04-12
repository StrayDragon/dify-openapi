# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class GetAnnotationsListByAppAdvancedChatResponseDataItem(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Annotation ID
    """

    question: typing.Optional[str] = pydantic.Field(default=None)
    """
    Question
    """

    answer: typing.Optional[str] = pydantic.Field(default=None)
    """
    Answer
    """

    hit_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Hit count
    """

    created_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    Creation timestamp
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
