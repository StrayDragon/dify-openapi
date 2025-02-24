from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostConversationsConversationIdNameBody")


@_attrs_define
class PostConversationsConversationIdNameBody:
    """
    Attributes:
        user (str): 用户标识
        name (Union[Unset, str]): 新名称
        auto_generate (Union[Unset, bool]): 是否自动生成 Default: False.
    """

    user: str
    name: Union[Unset, str] = UNSET
    auto_generate: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user

        name = self.name

        auto_generate = self.auto_generate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if auto_generate is not UNSET:
            field_dict["auto_generate"] = auto_generate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        user = d.pop("user")

        name = d.pop("name", UNSET)

        auto_generate = d.pop("auto_generate", UNSET)

        post_conversations_conversation_id_name_body = cls(
            user=user,
            name=name,
            auto_generate=auto_generate,
        )

        post_conversations_conversation_id_name_body.additional_properties = d
        return post_conversations_conversation_id_name_body

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
