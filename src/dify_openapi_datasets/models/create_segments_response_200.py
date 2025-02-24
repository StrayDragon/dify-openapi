from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.segment import Segment


T = TypeVar("T", bound="CreateSegmentsResponse200")


@_attrs_define
class CreateSegmentsResponse200:
    """
    Attributes:
        data (Union[Unset, list['Segment']]):
        doc_form (Union[Unset, str]):
    """

    data: Union[Unset, list["Segment"]] = UNSET
    doc_form: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        doc_form = self.doc_form

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if doc_form is not UNSET:
            field_dict["doc_form"] = doc_form

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.segment import Segment

        d = src_dict.copy()
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = Segment.from_dict(data_item_data)

            data.append(data_item)

        doc_form = d.pop("doc_form", UNSET)

        create_segments_response_200 = cls(
            data=data,
            doc_form=doc_form,
        )

        create_segments_response_200.additional_properties = d
        return create_segments_response_200

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
