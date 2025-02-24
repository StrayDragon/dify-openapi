from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stream_event_event import StreamEventEvent, check_stream_event_event
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stream_event_data import StreamEventData
    from ..models.stream_event_metadata import StreamEventMetadata


T = TypeVar("T", bound="StreamEvent")


@_attrs_define
class StreamEvent:
    """
    Attributes:
        event (Union[Unset, StreamEventEvent]): 事件类型
        task_id (Union[Unset, str]): 任务 ID
        message_id (Union[Unset, str]): 消息唯一 ID
        conversation_id (Union[Unset, str]): 会话 ID
        workflow_run_id (Union[Unset, str]): workflow 执行 ID
        answer (Union[Unset, str]): 回复内容
        audio (Union[Unset, str]): 语音合成音频数据（base64编码）
        data (Union[Unset, StreamEventData]): 事件相关数据
        metadata (Union[Unset, StreamEventMetadata]):
        created_at (Union[Unset, int]): 创建时间戳
    """

    event: Union[Unset, StreamEventEvent] = UNSET
    task_id: Union[Unset, str] = UNSET
    message_id: Union[Unset, str] = UNSET
    conversation_id: Union[Unset, str] = UNSET
    workflow_run_id: Union[Unset, str] = UNSET
    answer: Union[Unset, str] = UNSET
    audio: Union[Unset, str] = UNSET
    data: Union[Unset, "StreamEventData"] = UNSET
    metadata: Union[Unset, "StreamEventMetadata"] = UNSET
    created_at: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event: Union[Unset, str] = UNSET
        if not isinstance(self.event, Unset):
            event = self.event

        task_id = self.task_id

        message_id = self.message_id

        conversation_id = self.conversation_id

        workflow_run_id = self.workflow_run_id

        answer = self.answer

        audio = self.audio

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event is not UNSET:
            field_dict["event"] = event
        if task_id is not UNSET:
            field_dict["task_id"] = task_id
        if message_id is not UNSET:
            field_dict["message_id"] = message_id
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if workflow_run_id is not UNSET:
            field_dict["workflow_run_id"] = workflow_run_id
        if answer is not UNSET:
            field_dict["answer"] = answer
        if audio is not UNSET:
            field_dict["audio"] = audio
        if data is not UNSET:
            field_dict["data"] = data
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.stream_event_data import StreamEventData
        from ..models.stream_event_metadata import StreamEventMetadata

        d = src_dict.copy()
        _event = d.pop("event", UNSET)
        event: Union[Unset, StreamEventEvent]
        if isinstance(_event, Unset):
            event = UNSET
        else:
            event = check_stream_event_event(_event)

        task_id = d.pop("task_id", UNSET)

        message_id = d.pop("message_id", UNSET)

        conversation_id = d.pop("conversation_id", UNSET)

        workflow_run_id = d.pop("workflow_run_id", UNSET)

        answer = d.pop("answer", UNSET)

        audio = d.pop("audio", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, StreamEventData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = StreamEventData.from_dict(_data)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, StreamEventMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = StreamEventMetadata.from_dict(_metadata)

        created_at = d.pop("created_at", UNSET)

        stream_event = cls(
            event=event,
            task_id=task_id,
            message_id=message_id,
            conversation_id=conversation_id,
            workflow_run_id=workflow_run_id,
            answer=answer,
            audio=audio,
            data=data,
            metadata=metadata,
            created_at=created_at,
        )

        stream_event.additional_properties = d
        return stream_event

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
