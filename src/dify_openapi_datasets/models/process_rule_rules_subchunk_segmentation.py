from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessRuleRulesSubchunkSegmentation")


@_attrs_define
class ProcessRuleRulesSubchunkSegmentation:
    """
    Attributes:
        separator (Union[Unset, str]): 分段标识符
        max_tokens (Union[Unset, int]): 最大长度（token）
        chunk_overlap (Union[Unset, int]): 分段重叠长度
    """

    separator: Union[Unset, str] = UNSET
    max_tokens: Union[Unset, int] = UNSET
    chunk_overlap: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        separator = self.separator

        max_tokens = self.max_tokens

        chunk_overlap = self.chunk_overlap

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if separator is not UNSET:
            field_dict["separator"] = separator
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens
        if chunk_overlap is not UNSET:
            field_dict["chunk_overlap"] = chunk_overlap

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        separator = d.pop("separator", UNSET)

        max_tokens = d.pop("max_tokens", UNSET)

        chunk_overlap = d.pop("chunk_overlap", UNSET)

        process_rule_rules_subchunk_segmentation = cls(
            separator=separator,
            max_tokens=max_tokens,
            chunk_overlap=chunk_overlap,
        )

        process_rule_rules_subchunk_segmentation.additional_properties = d
        return process_rule_rules_subchunk_segmentation

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
