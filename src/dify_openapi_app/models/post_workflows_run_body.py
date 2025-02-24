from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_workflows_run_body_response_mode import (
    PostWorkflowsRunBodyResponseMode,
    check_post_workflows_run_body_response_mode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_input import FileInput
    from ..models.post_workflows_run_body_inputs import PostWorkflowsRunBodyInputs


T = TypeVar("T", bound="PostWorkflowsRunBody")


@_attrs_define
class PostWorkflowsRunBody:
    """
    Attributes:
        inputs (PostWorkflowsRunBodyInputs): 工作流输入参数
        response_mode (PostWorkflowsRunBodyResponseMode): 响应模式
        user (str): 用户标识
        files (Union[Unset, list['FileInput']]):
    """

    inputs: "PostWorkflowsRunBodyInputs"
    response_mode: PostWorkflowsRunBodyResponseMode
    user: str
    files: Union[Unset, list["FileInput"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inputs = self.inputs.to_dict()

        response_mode: str = self.response_mode

        user = self.user

        files: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "inputs": inputs,
                "response_mode": response_mode,
                "user": user,
            }
        )
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.file_input import FileInput
        from ..models.post_workflows_run_body_inputs import PostWorkflowsRunBodyInputs

        d = src_dict.copy()
        inputs = PostWorkflowsRunBodyInputs.from_dict(d.pop("inputs"))

        response_mode = check_post_workflows_run_body_response_mode(d.pop("response_mode"))

        user = d.pop("user")

        files = []
        _files = d.pop("files", UNSET)
        for files_item_data in _files or []:
            files_item = FileInput.from_dict(files_item_data)

            files.append(files_item)

        post_workflows_run_body = cls(
            inputs=inputs,
            response_mode=response_mode,
            user=user,
            files=files,
        )

        post_workflows_run_body.additional_properties = d
        return post_workflows_run_body

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
