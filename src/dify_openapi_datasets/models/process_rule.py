from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.process_rule_mode import ProcessRuleMode, check_process_rule_mode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_rule_rules import ProcessRuleRules


T = TypeVar("T", bound="ProcessRule")


@_attrs_define
class ProcessRule:
    """
    Attributes:
        mode (ProcessRuleMode): 清洗、分段模式
        rules (Union[Unset, ProcessRuleRules]): 自定义规则（自动模式下为空）
    """

    mode: ProcessRuleMode
    rules: Union[Unset, "ProcessRuleRules"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode: str = self.mode

        rules: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = self.rules.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
            }
        )
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.process_rule_rules import ProcessRuleRules

        d = src_dict.copy()
        mode = check_process_rule_mode(d.pop("mode"))

        _rules = d.pop("rules", UNSET)
        rules: Union[Unset, ProcessRuleRules]
        if isinstance(_rules, Unset):
            rules = UNSET
        else:
            rules = ProcessRuleRules.from_dict(_rules)

        process_rule = cls(
            mode=mode,
            rules=rules,
        )

        process_rule.additional_properties = d
        return process_rule

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
