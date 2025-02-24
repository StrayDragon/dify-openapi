from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateSegmentBodySegment")


@_attrs_define
class UpdateSegmentBodySegment:
    """
    Attributes:
        content (Union[Unset, str]): 文本内容/问题内容
        answer (Union[Unset, str]): 答案内容（Q&A 模式必填）
        keywords (Union[Unset, list[str]]): 关键字列表
        enabled (Union[Unset, bool]): 是否启用
        regenerate_child_chunks (Union[Unset, bool]): 是否重新生成子分段
    """

    content: Union[Unset, str] = UNSET
    answer: Union[Unset, str] = UNSET
    keywords: Union[Unset, list[str]] = UNSET
    enabled: Union[Unset, bool] = UNSET
    regenerate_child_chunks: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        answer = self.answer

        keywords: Union[Unset, list[str]] = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        enabled = self.enabled

        regenerate_child_chunks = self.regenerate_child_chunks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if answer is not UNSET:
            field_dict["answer"] = answer
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if regenerate_child_chunks is not UNSET:
            field_dict["regenerate_child_chunks"] = regenerate_child_chunks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        content = d.pop("content", UNSET)

        answer = d.pop("answer", UNSET)

        keywords = cast(list[str], d.pop("keywords", UNSET))

        enabled = d.pop("enabled", UNSET)

        regenerate_child_chunks = d.pop("regenerate_child_chunks", UNSET)

        update_segment_body_segment = cls(
            content=content,
            answer=answer,
            keywords=keywords,
            enabled=enabled,
            regenerate_child_chunks=regenerate_child_chunks,
        )

        update_segment_body_segment.additional_properties = d
        return update_segment_body_segment

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
