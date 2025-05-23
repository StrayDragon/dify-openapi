# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dataset import Dataset


class DatasetList(UniversalBaseModel):
    data: typing.Optional[typing.List[Dataset]] = None
    has_more: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether there is more data
    """

    limit: typing.Optional[int] = pydantic.Field(default=None)
    """
    Page size limit
    """

    total: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total record count
    """

    page: typing.Optional[int] = pydantic.Field(default=None)
    """
    Current page number
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
