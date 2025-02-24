from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.process_rule_rules_parent_mode import ProcessRuleRulesParentMode, check_process_rule_rules_parent_mode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_rule_rules_pre_processing_rules_item import ProcessRuleRulesPreProcessingRulesItem
    from ..models.process_rule_rules_segmentation import ProcessRuleRulesSegmentation
    from ..models.process_rule_rules_subchunk_segmentation import ProcessRuleRulesSubchunkSegmentation


T = TypeVar("T", bound="ProcessRuleRules")


@_attrs_define
class ProcessRuleRules:
    """自定义规则（自动模式下为空）

    Attributes:
        pre_processing_rules (Union[Unset, list['ProcessRuleRulesPreProcessingRulesItem']]):
        segmentation (Union[Unset, ProcessRuleRulesSegmentation]):
        parent_mode (Union[Unset, ProcessRuleRulesParentMode]): 父分段的召回模式
        subchunk_segmentation (Union[Unset, ProcessRuleRulesSubchunkSegmentation]):
    """

    pre_processing_rules: Union[Unset, list["ProcessRuleRulesPreProcessingRulesItem"]] = UNSET
    segmentation: Union[Unset, "ProcessRuleRulesSegmentation"] = UNSET
    parent_mode: Union[Unset, ProcessRuleRulesParentMode] = UNSET
    subchunk_segmentation: Union[Unset, "ProcessRuleRulesSubchunkSegmentation"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pre_processing_rules: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.pre_processing_rules, Unset):
            pre_processing_rules = []
            for pre_processing_rules_item_data in self.pre_processing_rules:
                pre_processing_rules_item = pre_processing_rules_item_data.to_dict()
                pre_processing_rules.append(pre_processing_rules_item)

        segmentation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.segmentation, Unset):
            segmentation = self.segmentation.to_dict()

        parent_mode: Union[Unset, str] = UNSET
        if not isinstance(self.parent_mode, Unset):
            parent_mode = self.parent_mode

        subchunk_segmentation: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.subchunk_segmentation, Unset):
            subchunk_segmentation = self.subchunk_segmentation.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pre_processing_rules is not UNSET:
            field_dict["pre_processing_rules"] = pre_processing_rules
        if segmentation is not UNSET:
            field_dict["segmentation"] = segmentation
        if parent_mode is not UNSET:
            field_dict["parent_mode"] = parent_mode
        if subchunk_segmentation is not UNSET:
            field_dict["subchunk_segmentation"] = subchunk_segmentation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.process_rule_rules_pre_processing_rules_item import ProcessRuleRulesPreProcessingRulesItem
        from ..models.process_rule_rules_segmentation import ProcessRuleRulesSegmentation
        from ..models.process_rule_rules_subchunk_segmentation import ProcessRuleRulesSubchunkSegmentation

        d = src_dict.copy()
        pre_processing_rules = []
        _pre_processing_rules = d.pop("pre_processing_rules", UNSET)
        for pre_processing_rules_item_data in _pre_processing_rules or []:
            pre_processing_rules_item = ProcessRuleRulesPreProcessingRulesItem.from_dict(pre_processing_rules_item_data)

            pre_processing_rules.append(pre_processing_rules_item)

        _segmentation = d.pop("segmentation", UNSET)
        segmentation: Union[Unset, ProcessRuleRulesSegmentation]
        if isinstance(_segmentation, Unset):
            segmentation = UNSET
        else:
            segmentation = ProcessRuleRulesSegmentation.from_dict(_segmentation)

        _parent_mode = d.pop("parent_mode", UNSET)
        parent_mode: Union[Unset, ProcessRuleRulesParentMode]
        if isinstance(_parent_mode, Unset):
            parent_mode = UNSET
        else:
            parent_mode = check_process_rule_rules_parent_mode(_parent_mode)

        _subchunk_segmentation = d.pop("subchunk_segmentation", UNSET)
        subchunk_segmentation: Union[Unset, ProcessRuleRulesSubchunkSegmentation]
        if isinstance(_subchunk_segmentation, Unset):
            subchunk_segmentation = UNSET
        else:
            subchunk_segmentation = ProcessRuleRulesSubchunkSegmentation.from_dict(_subchunk_segmentation)

        process_rule_rules = cls(
            pre_processing_rules=pre_processing_rules,
            segmentation=segmentation,
            parent_mode=parent_mode,
            subchunk_segmentation=subchunk_segmentation,
        )

        process_rule_rules.additional_properties = d
        return process_rule_rules

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
