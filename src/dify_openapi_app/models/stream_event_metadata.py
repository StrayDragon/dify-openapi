from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.retriever_resource import RetrieverResource
    from ..models.usage import Usage


T = TypeVar("T", bound="StreamEventMetadata")


@_attrs_define
class StreamEventMetadata:
    """
    Attributes:
        usage (Union[Unset, Usage]):
        retriever_resources (Union[Unset, list['RetrieverResource']]):
    """

    usage: Union[Unset, "Usage"] = UNSET
    retriever_resources: Union[Unset, list["RetrieverResource"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        usage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        retriever_resources: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.retriever_resources, Unset):
            retriever_resources = []
            for retriever_resources_item_data in self.retriever_resources:
                retriever_resources_item = retriever_resources_item_data.to_dict()
                retriever_resources.append(retriever_resources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if usage is not UNSET:
            field_dict["usage"] = usage
        if retriever_resources is not UNSET:
            field_dict["retriever_resources"] = retriever_resources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.retriever_resource import RetrieverResource
        from ..models.usage import Usage

        d = src_dict.copy()
        _usage = d.pop("usage", UNSET)
        usage: Union[Unset, Usage]
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = Usage.from_dict(_usage)

        retriever_resources = []
        _retriever_resources = d.pop("retriever_resources", UNSET)
        for retriever_resources_item_data in _retriever_resources or []:
            retriever_resources_item = RetrieverResource.from_dict(retriever_resources_item_data)

            retriever_resources.append(retriever_resources_item)

        stream_event_metadata = cls(
            usage=usage,
            retriever_resources=retriever_resources,
        )

        stream_event_metadata.additional_properties = d
        return stream_event_metadata

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
