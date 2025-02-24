from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dataset import Dataset


T = TypeVar("T", bound="DatasetList")


@_attrs_define
class DatasetList:
    """
    Attributes:
        data (Union[Unset, list['Dataset']]):
        has_more (Union[Unset, bool]): 是否还有更多数据
        limit (Union[Unset, int]): 每页数量限制
        total (Union[Unset, int]): 总记录数
        page (Union[Unset, int]): 当前页码
    """

    data: Union[Unset, list["Dataset"]] = UNSET
    has_more: Union[Unset, bool] = UNSET
    limit: Union[Unset, int] = UNSET
    total: Union[Unset, int] = UNSET
    page: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        has_more = self.has_more

        limit = self.limit

        total = self.total

        page = self.page

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if has_more is not UNSET:
            field_dict["has_more"] = has_more
        if limit is not UNSET:
            field_dict["limit"] = limit
        if total is not UNSET:
            field_dict["total"] = total
        if page is not UNSET:
            field_dict["page"] = page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.dataset import Dataset

        d = src_dict.copy()
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = Dataset.from_dict(data_item_data)

            data.append(data_item)

        has_more = d.pop("has_more", UNSET)

        limit = d.pop("limit", UNSET)

        total = d.pop("total", UNSET)

        page = d.pop("page", UNSET)

        dataset_list = cls(
            data=data,
            has_more=has_more,
            limit=limit,
            total=total,
            page=page,
        )

        dataset_list.additional_properties = d
        return dataset_list

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
