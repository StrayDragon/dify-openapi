from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.retrieve_dataset_response_200_records_item_segment import RetrieveDatasetResponse200RecordsItemSegment
    from ..models.retrieve_dataset_response_200_records_item_tsne_position_type_0 import (
        RetrieveDatasetResponse200RecordsItemTsnePositionType0,
    )


T = TypeVar("T", bound="RetrieveDatasetResponse200RecordsItem")


@_attrs_define
class RetrieveDatasetResponse200RecordsItem:
    """
    Attributes:
        segment (Union[Unset, RetrieveDatasetResponse200RecordsItemSegment]):
        score (Union[Unset, float]):
        tsne_position (Union['RetrieveDatasetResponse200RecordsItemTsnePositionType0', None, Unset]):
    """

    segment: Union[Unset, "RetrieveDatasetResponse200RecordsItemSegment"] = UNSET
    score: Union[Unset, float] = UNSET
    tsne_position: Union["RetrieveDatasetResponse200RecordsItemTsnePositionType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.retrieve_dataset_response_200_records_item_tsne_position_type_0 import (
            RetrieveDatasetResponse200RecordsItemTsnePositionType0,
        )

        segment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.segment, Unset):
            segment = self.segment.to_dict()

        score = self.score

        tsne_position: Union[None, Unset, dict[str, Any]]
        if isinstance(self.tsne_position, Unset):
            tsne_position = UNSET
        elif isinstance(self.tsne_position, RetrieveDatasetResponse200RecordsItemTsnePositionType0):
            tsne_position = self.tsne_position.to_dict()
        else:
            tsne_position = self.tsne_position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if segment is not UNSET:
            field_dict["segment"] = segment
        if score is not UNSET:
            field_dict["score"] = score
        if tsne_position is not UNSET:
            field_dict["tsne_position"] = tsne_position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.retrieve_dataset_response_200_records_item_segment import (
            RetrieveDatasetResponse200RecordsItemSegment,
        )
        from ..models.retrieve_dataset_response_200_records_item_tsne_position_type_0 import (
            RetrieveDatasetResponse200RecordsItemTsnePositionType0,
        )

        d = src_dict.copy()
        _segment = d.pop("segment", UNSET)
        segment: Union[Unset, RetrieveDatasetResponse200RecordsItemSegment]
        if isinstance(_segment, Unset):
            segment = UNSET
        else:
            segment = RetrieveDatasetResponse200RecordsItemSegment.from_dict(_segment)

        score = d.pop("score", UNSET)

        def _parse_tsne_position(
            data: object,
        ) -> Union["RetrieveDatasetResponse200RecordsItemTsnePositionType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tsne_position_type_0 = RetrieveDatasetResponse200RecordsItemTsnePositionType0.from_dict(data)

                return tsne_position_type_0
            except:  # noqa: E722
                pass
            return cast(Union["RetrieveDatasetResponse200RecordsItemTsnePositionType0", None, Unset], data)

        tsne_position = _parse_tsne_position(d.pop("tsne_position", UNSET))

        retrieve_dataset_response_200_records_item = cls(
            segment=segment,
            score=score,
            tsne_position=tsne_position,
        )

        retrieve_dataset_response_200_records_item.additional_properties = d
        return retrieve_dataset_response_200_records_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
