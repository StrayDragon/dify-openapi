from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.process_rule_rules_pre_processing_rules_item_id import (
    ProcessRuleRulesPreProcessingRulesItemId,
    check_process_rule_rules_pre_processing_rules_item_id,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProcessRuleRulesPreProcessingRulesItem")


@_attrs_define
class ProcessRuleRulesPreProcessingRulesItem:
    """
    Attributes:
        id (Union[Unset, ProcessRuleRulesPreProcessingRulesItemId]): 预处理规则的唯一标识符
        enabled (Union[Unset, bool]): 是否选中该规则
    """

    id: Union[Unset, ProcessRuleRulesPreProcessingRulesItemId] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: Union[Unset, str] = UNSET
        if not isinstance(self.id, Unset):
            id = self.id

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _id = d.pop("id", UNSET)
        id: Union[Unset, ProcessRuleRulesPreProcessingRulesItemId]
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = check_process_rule_rules_pre_processing_rules_item_id(_id)

        enabled = d.pop("enabled", UNSET)

        process_rule_rules_pre_processing_rules_item = cls(
            id=id,
            enabled=enabled,
        )

        process_rule_rules_pre_processing_rules_item.additional_properties = d
        return process_rule_rules_pre_processing_rules_item

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
