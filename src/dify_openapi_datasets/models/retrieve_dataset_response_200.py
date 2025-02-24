from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.retrieve_dataset_response_200_query import RetrieveDatasetResponse200Query
    from ..models.retrieve_dataset_response_200_records_item import RetrieveDatasetResponse200RecordsItem


T = TypeVar("T", bound="RetrieveDatasetResponse200")


@_attrs_define
class RetrieveDatasetResponse200:
    """
    Attributes:
        query (Union[Unset, RetrieveDatasetResponse200Query]):
        records (Union[Unset, list['RetrieveDatasetResponse200RecordsItem']]):
    """

    query: Union[Unset, "RetrieveDatasetResponse200Query"] = UNSET
    records: Union[Unset, list["RetrieveDatasetResponse200RecordsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        records: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.records, Unset):
            records = []
            for records_item_data in self.records:
                records_item = records_item_data.to_dict()
                records.append(records_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if query is not UNSET:
            field_dict["query"] = query
        if records is not UNSET:
            field_dict["records"] = records

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.retrieve_dataset_response_200_query import RetrieveDatasetResponse200Query
        from ..models.retrieve_dataset_response_200_records_item import RetrieveDatasetResponse200RecordsItem

        d = src_dict.copy()
        _query = d.pop("query", UNSET)
        query: Union[Unset, RetrieveDatasetResponse200Query]
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = RetrieveDatasetResponse200Query.from_dict(_query)

        records = []
        _records = d.pop("records", UNSET)
        for records_item_data in _records or []:
            records_item = RetrieveDatasetResponse200RecordsItem.from_dict(records_item_data)

            records.append(records_item)

        retrieve_dataset_response_200 = cls(
            query=query,
            records=records,
        )

        retrieve_dataset_response_200.additional_properties = d
        return retrieve_dataset_response_200

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
