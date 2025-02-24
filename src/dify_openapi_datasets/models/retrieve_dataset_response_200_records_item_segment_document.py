from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RetrieveDatasetResponse200RecordsItemSegmentDocument")


@_attrs_define
class RetrieveDatasetResponse200RecordsItemSegmentDocument:
    """
    Attributes:
        id (Union[Unset, str]):
        data_source_type (Union[Unset, str]):
        name (Union[Unset, str]):
        doc_type (Union[None, Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    data_source_type: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    doc_type: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        data_source_type = self.data_source_type

        name = self.name

        doc_type: Union[None, Unset, str]
        if isinstance(self.doc_type, Unset):
            doc_type = UNSET
        else:
            doc_type = self.doc_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if data_source_type is not UNSET:
            field_dict["data_source_type"] = data_source_type
        if name is not UNSET:
            field_dict["name"] = name
        if doc_type is not UNSET:
            field_dict["doc_type"] = doc_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        data_source_type = d.pop("data_source_type", UNSET)

        name = d.pop("name", UNSET)

        def _parse_doc_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        doc_type = _parse_doc_type(d.pop("doc_type", UNSET))

        retrieve_dataset_response_200_records_item_segment_document = cls(
            id=id,
            data_source_type=data_source_type,
            name=name,
            doc_type=doc_type,
        )

        retrieve_dataset_response_200_records_item_segment_document.additional_properties = d
        return retrieve_dataset_response_200_records_item_segment_document

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
