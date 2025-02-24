from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostTextToAudioBody")


@_attrs_define
class PostTextToAudioBody:
    """
    Attributes:
        message_id (Union[Unset, str]): 消息ID
        text (Union[Unset, str]): 待转换文本
        user (Union[Unset, str]): 用户标识
    """

    message_id: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    user: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message_id = self.message_id

        text = self.text

        user = self.user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message_id is not UNSET:
            field_dict["message_id"] = message_id
        if text is not UNSET:
            field_dict["text"] = text
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        message_id = d.pop("message_id", UNSET)

        text = d.pop("text", UNSET)

        user = d.pop("user", UNSET)

        post_text_to_audio_body = cls(
            message_id=message_id,
            text=text,
            user=user,
        )

        post_text_to_audio_body.additional_properties = d
        return post_text_to_audio_body

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
