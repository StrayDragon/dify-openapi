from typing import Literal, cast

ProcessRuleRulesParentMode = Literal["full-doc", "paragraph"]

PROCESS_RULE_RULES_PARENT_MODE_VALUES: set[ProcessRuleRulesParentMode] = {
    "full-doc",
    "paragraph",
}


def check_process_rule_rules_parent_mode(value: str) -> ProcessRuleRulesParentMode:
    if value in PROCESS_RULE_RULES_PARENT_MODE_VALUES or value is None:  # NOTE: @l8ng skip check for some case
        return cast(ProcessRuleRulesParentMode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROCESS_RULE_RULES_PARENT_MODE_VALUES!r}")
