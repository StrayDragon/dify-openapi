from typing import Literal, cast

WorkflowMessageDataStatus = Literal["failed", "running", "stopped", "succeeded"]

WORKFLOW_MESSAGE_DATA_STATUS_VALUES: set[WorkflowMessageDataStatus] = {
    "failed",
    "running",
    "stopped",
    "succeeded",
}


def check_workflow_message_data_status(value: str) -> WorkflowMessageDataStatus:
    if value in WORKFLOW_MESSAGE_DATA_STATUS_VALUES or value is None:  # NOTE: @l8ng skip check for some case
        return cast(WorkflowMessageDataStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKFLOW_MESSAGE_DATA_STATUS_VALUES!r}")
