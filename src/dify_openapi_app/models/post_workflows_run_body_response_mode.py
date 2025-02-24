from typing import Literal, cast

PostWorkflowsRunBodyResponseMode = Literal["blocking", "streaming"]

POST_WORKFLOWS_RUN_BODY_RESPONSE_MODE_VALUES: set[PostWorkflowsRunBodyResponseMode] = {
    "blocking",
    "streaming",
}


def check_post_workflows_run_body_response_mode(value: str) -> PostWorkflowsRunBodyResponseMode:
    if value in POST_WORKFLOWS_RUN_BODY_RESPONSE_MODE_VALUES or value is None:  # NOTE: @l8ng skip check for some case
        return cast(PostWorkflowsRunBodyResponseMode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POST_WORKFLOWS_RUN_BODY_RESPONSE_MODE_VALUES!r}")
