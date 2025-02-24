from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_message_metadata import BaseMessageMetadata


T = TypeVar("T", bound="CompletionMessage")


@_attrs_define
class CompletionMessage:
    """
    Attributes:
        message_id (Union[Unset, str]): 消息唯一 ID
        created_at (Union[Unset, int]): 消息创建时间戳
        metadata (Union[Unset, BaseMessageMetadata]):
        mode (Union[Unset, str]): App 模式，固定为 completion
        answer (Union[Unset, str]): 完整回复内容
    """

    message_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, int] = UNSET
    metadata: Union[Unset, "BaseMessageMetadata"] = UNSET
    mode: Union[Unset, str] = UNSET
    answer: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_id = self.message_id

        created_at = self.created_at

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        mode = self.mode

        answer = self.answer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message_id is not UNSET:
            field_dict["message_id"] = message_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if mode is not UNSET:
            field_dict["mode"] = mode
        if answer is not UNSET:
            field_dict["answer"] = answer

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.base_message_metadata import BaseMessageMetadata

        d = src_dict.copy()
        message_id = d.pop("message_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, BaseMessageMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = BaseMessageMetadata.from_dict(_metadata)

        mode = d.pop("mode", UNSET)

        answer = d.pop("answer", UNSET)

        completion_message = cls(
            message_id=message_id,
            created_at=created_at,
            metadata=metadata,
            mode=mode,
            answer=answer,
        )

        completion_message.additional_properties = d
        return completion_message

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
