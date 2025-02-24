from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_message_data import WorkflowMessageData


T = TypeVar("T", bound="WorkflowMessage")


@_attrs_define
class WorkflowMessage:
    """
    Attributes:
        workflow_run_id (Union[Unset, str]): workflow 执行 ID
        task_id (Union[Unset, str]): 任务 ID
        data (Union[Unset, WorkflowMessageData]):
    """

    workflow_run_id: Union[Unset, str] = UNSET
    task_id: Union[Unset, str] = UNSET
    data: Union[Unset, "WorkflowMessageData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        workflow_run_id = self.workflow_run_id

        task_id = self.task_id

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if workflow_run_id is not UNSET:
            field_dict["workflow_run_id"] = workflow_run_id
        if task_id is not UNSET:
            field_dict["task_id"] = task_id
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.workflow_message_data import WorkflowMessageData

        d = src_dict.copy()
        workflow_run_id = d.pop("workflow_run_id", UNSET)

        task_id = d.pop("task_id", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, WorkflowMessageData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = WorkflowMessageData.from_dict(_data)

        workflow_message = cls(
            workflow_run_id=workflow_run_id,
            task_id=task_id,
            data=data,
        )

        workflow_message.additional_properties = d
        return workflow_message

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
