from typing import Literal, cast

ProcessRuleRulesPreProcessingRulesItemId = Literal["remove_extra_spaces", "remove_urls_emails"]

PROCESS_RULE_RULES_PRE_PROCESSING_RULES_ITEM_ID_VALUES: set[ProcessRuleRulesPreProcessingRulesItemId] = {
    "remove_extra_spaces",
    "remove_urls_emails",
}


def check_process_rule_rules_pre_processing_rules_item_id(value: str) -> ProcessRuleRulesPreProcessingRulesItemId:
    if (
        value in PROCESS_RULE_RULES_PRE_PROCESSING_RULES_ITEM_ID_VALUES or value is None
    ):  # NOTE: @l8ng skip check for some case
        return cast(ProcessRuleRulesPreProcessingRulesItemId, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROCESS_RULE_RULES_PRE_PROCESSING_RULES_ITEM_ID_VALUES!r}"
    )
