from typing import Literal, cast

ProcessRuleMode = Literal["automatic", "custom"]

PROCESS_RULE_MODE_VALUES: set[ProcessRuleMode] = {
    "automatic",
    "custom",
}


def check_process_rule_mode(value: str) -> ProcessRuleMode:
    if value in PROCESS_RULE_MODE_VALUES or value is None:  # NOTE: @l8ng skip check for some case
        return cast(ProcessRuleMode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROCESS_RULE_MODE_VALUES!r}")
