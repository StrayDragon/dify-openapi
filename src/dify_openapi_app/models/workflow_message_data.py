from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_message_data_status import WorkflowMessageDataStatus, check_workflow_message_data_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_message_data_outputs import WorkflowMessageDataOutputs


T = TypeVar("T", bound="WorkflowMessageData")


@_attrs_define
class WorkflowMessageData:
    """
    Attributes:
        id (Union[Unset, str]): workflow 执行 ID
        workflow_id (Union[Unset, str]): 关联 Workflow ID
        status (Union[Unset, WorkflowMessageDataStatus]): 执行状态
        outputs (Union[Unset, WorkflowMessageDataOutputs]): 输出内容
        error (Union[Unset, str]): 错误原因
        elapsed_time (Union[Unset, float]): 耗时(s)
        total_tokens (Union[Unset, int]): 总使用 tokens
        total_steps (Union[Unset, int]): 总步数
        created_at (Union[Unset, int]): 开始时间
        finished_at (Union[Unset, int]): 结束时间
    """

    id: Union[Unset, str] = UNSET
    workflow_id: Union[Unset, str] = UNSET
    status: Union[Unset, WorkflowMessageDataStatus] = UNSET
    outputs: Union[Unset, "WorkflowMessageDataOutputs"] = UNSET
    error: Union[Unset, str] = UNSET
    elapsed_time: Union[Unset, float] = UNSET
    total_tokens: Union[Unset, int] = UNSET
    total_steps: Union[Unset, int] = UNSET
    created_at: Union[Unset, int] = UNSET
    finished_at: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workflow_id = self.workflow_id

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        outputs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.outputs, Unset):
            outputs = self.outputs.to_dict()

        error = self.error

        elapsed_time = self.elapsed_time

        total_tokens = self.total_tokens

        total_steps = self.total_steps

        created_at = self.created_at

        finished_at = self.finished_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if workflow_id is not UNSET:
            field_dict["workflow_id"] = workflow_id
        if status is not UNSET:
            field_dict["status"] = status
        if outputs is not UNSET:
            field_dict["outputs"] = outputs
        if error is not UNSET:
            field_dict["error"] = error
        if elapsed_time is not UNSET:
            field_dict["elapsed_time"] = elapsed_time
        if total_tokens is not UNSET:
            field_dict["total_tokens"] = total_tokens
        if total_steps is not UNSET:
            field_dict["total_steps"] = total_steps
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.workflow_message_data_outputs import WorkflowMessageDataOutputs

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        workflow_id = d.pop("workflow_id", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, WorkflowMessageDataStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_workflow_message_data_status(_status)

        _outputs = d.pop("outputs", UNSET)
        outputs: Union[Unset, WorkflowMessageDataOutputs]
        if isinstance(_outputs, Unset):
            outputs = UNSET
        else:
            outputs = WorkflowMessageDataOutputs.from_dict(_outputs)

        error = d.pop("error", UNSET)

        elapsed_time = d.pop("elapsed_time", UNSET)

        total_tokens = d.pop("total_tokens", UNSET)

        total_steps = d.pop("total_steps", UNSET)

        created_at = d.pop("created_at", UNSET)

        finished_at = d.pop("finished_at", UNSET)

        workflow_message_data = cls(
            id=id,
            workflow_id=workflow_id,
            status=status,
            outputs=outputs,
            error=error,
            elapsed_time=elapsed_time,
            total_tokens=total_tokens,
            total_steps=total_steps,
            created_at=created_at,
            finished_at=finished_at,
        )

        workflow_message_data.additional_properties = d
        return workflow_message_data

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
