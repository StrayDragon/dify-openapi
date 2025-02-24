from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSegmentsBodySegmentsItem")


@_attrs_define
class CreateSegmentsBodySegmentsItem:
    """
    Attributes:
        content (str): 文本内容/问题内容
        answer (Union[Unset, str]): 答案内容，非必填，如果知识库的模式为 Q&A 模式则传值
        keywords (Union[Unset, list[str]]): 关键字列表，非必填
    """

    content: str
    answer: Union[Unset, str] = UNSET
    keywords: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        answer = self.answer

        keywords: Union[Unset, list[str]] = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )
        if answer is not UNSET:
            field_dict["answer"] = answer
        if keywords is not UNSET:
            field_dict["keywords"] = keywords

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        content = d.pop("content")

        answer = d.pop("answer", UNSET)

        keywords = cast(list[str], d.pop("keywords", UNSET))

        create_segments_body_segments_item = cls(
            content=content,
            answer=answer,
            keywords=keywords,
        )

        create_segments_body_segments_item.additional_properties = d
        return create_segments_body_segments_item

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
