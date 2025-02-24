from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conversation_inputs import ConversationInputs


T = TypeVar("T", bound="Conversation")


@_attrs_define
class Conversation:
    """
    Attributes:
        id (Union[Unset, str]): 会话 ID
        name (Union[Unset, str]): 会话名称
        inputs (Union[Unset, ConversationInputs]): 用户输入参数
        status (Union[Unset, str]): 会话状态
        introduction (Union[Unset, str]): 开场白
        created_at (Union[Unset, int]): 创建时间
        updated_at (Union[Unset, int]): 更新时间
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    inputs: Union[Unset, "ConversationInputs"] = UNSET
    status: Union[Unset, str] = UNSET
    introduction: Union[Unset, str] = UNSET
    created_at: Union[Unset, int] = UNSET
    updated_at: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        inputs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = self.inputs.to_dict()

        status = self.status

        introduction = self.introduction

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if status is not UNSET:
            field_dict["status"] = status
        if introduction is not UNSET:
            field_dict["introduction"] = introduction
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.conversation_inputs import ConversationInputs

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _inputs = d.pop("inputs", UNSET)
        inputs: Union[Unset, ConversationInputs]
        if isinstance(_inputs, Unset):
            inputs = UNSET
        else:
            inputs = ConversationInputs.from_dict(_inputs)

        status = d.pop("status", UNSET)

        introduction = d.pop("introduction", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        conversation = cls(
            id=id,
            name=name,
            inputs=inputs,
            status=status,
            introduction=introduction,
            created_at=created_at,
            updated_at=updated_at,
        )

        conversation.additional_properties = d
        return conversation

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
