# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .usage import Usage
from .retriever_resource import RetrieverResource
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class StreamEventMetadata(UniversalBaseModel):
    usage: typing.Optional[Usage] = None
    retriever_resources: typing.Optional[typing.List[RetrieverResource]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
