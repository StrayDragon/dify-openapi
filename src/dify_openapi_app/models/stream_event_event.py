from typing import Literal, cast

StreamEventEvent = Literal[
    "agent_message",
    "agent_thought",
    "error",
    "message",
    "message_end",
    "message_file",
    "message_replace",
    "node_finished",
    "node_started",
    "ping",
    "tts_message",
    "tts_message_end",
    "workflow_finished",
    "workflow_started",
]

STREAM_EVENT_EVENT_VALUES: set[StreamEventEvent] = {
    "agent_message",
    "agent_thought",
    "error",
    "message",
    "message_end",
    "message_file",
    "message_replace",
    "node_finished",
    "node_started",
    "ping",
    "tts_message",
    "tts_message_end",
    "workflow_finished",
    "workflow_started",
}


def check_stream_event_event(value: str) -> StreamEventEvent:
    if value in STREAM_EVENT_EVENT_VALUES or value is None:  # NOTE: @l8ng skip check for some case
        return cast(StreamEventEvent, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STREAM_EVENT_EVENT_VALUES!r}")
