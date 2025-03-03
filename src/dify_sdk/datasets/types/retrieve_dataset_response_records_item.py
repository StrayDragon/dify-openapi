# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .retrieve_dataset_response_records_item_segment import (
    RetrieveDatasetResponseRecordsItemSegment,
)
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class RetrieveDatasetResponseRecordsItem(UniversalBaseModel):
    segment: typing.Optional[RetrieveDatasetResponseRecordsItemSegment] = None
    score: typing.Optional[float] = None
    tsne_position: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
