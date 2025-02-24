from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_chat_messages_body_response_mode import (
    PostChatMessagesBodyResponseMode,
    check_post_chat_messages_body_response_mode,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_input import FileInput
    from ..models.post_chat_messages_body_inputs import PostChatMessagesBodyInputs


T = TypeVar("T", bound="PostChatMessagesBody")


@_attrs_define
class PostChatMessagesBody:
    """
    Attributes:
        query (str): 用户输入/提问内容
        inputs (Union[Unset, PostChatMessagesBodyInputs]): 允许传入 App 定义的各变量值
        response_mode (Union[Unset, PostChatMessagesBodyResponseMode]): 响应模式:
            - streaming: 流式模式（推荐），基于 SSE 实现类似打字机输出
            - blocking: 阻塞模式，等待执行完毕后返回结果
        user (Union[Unset, str]): 用户标识
        conversation_id (Union[Unset, str]): 会话 ID
        files (Union[Unset, list['FileInput']]):
        auto_generate_name (Union[Unset, bool]): 是否自动生成标题 Default: True.
    """

    query: str
    inputs: Union[Unset, "PostChatMessagesBodyInputs"] = UNSET
    response_mode: Union[Unset, PostChatMessagesBodyResponseMode] = UNSET
    user: Union[Unset, str] = UNSET
    conversation_id: Union[Unset, str] = UNSET
    files: Union[Unset, list["FileInput"]] = UNSET
    auto_generate_name: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        inputs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = self.inputs.to_dict()

        response_mode: Union[Unset, str] = UNSET
        if not isinstance(self.response_mode, Unset):
            response_mode = self.response_mode

        user = self.user

        conversation_id = self.conversation_id

        files: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        auto_generate_name = self.auto_generate_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if response_mode is not UNSET:
            field_dict["response_mode"] = response_mode
        if user is not UNSET:
            field_dict["user"] = user
        if conversation_id is not UNSET:
            field_dict["conversation_id"] = conversation_id
        if files is not UNSET:
            field_dict["files"] = files
        if auto_generate_name is not UNSET:
            field_dict["auto_generate_name"] = auto_generate_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.file_input import FileInput
        from ..models.post_chat_messages_body_inputs import PostChatMessagesBodyInputs

        d = src_dict.copy()
        query = d.pop("query")

        _inputs = d.pop("inputs", UNSET)
        inputs: Union[Unset, PostChatMessagesBodyInputs]
        if isinstance(_inputs, Unset):
            inputs = UNSET
        else:
            inputs = PostChatMessagesBodyInputs.from_dict(_inputs)

        _response_mode = d.pop("response_mode", UNSET)
        response_mode: Union[Unset, PostChatMessagesBodyResponseMode]
        if isinstance(_response_mode, Unset):
            response_mode = UNSET
        else:
            response_mode = check_post_chat_messages_body_response_mode(_response_mode)

        user = d.pop("user", UNSET)

        conversation_id = d.pop("conversation_id", UNSET)

        files = []
        _files = d.pop("files", UNSET)
        for files_item_data in _files or []:
            files_item = FileInput.from_dict(files_item_data)

            files.append(files_item)

        auto_generate_name = d.pop("auto_generate_name", UNSET)

        post_chat_messages_body = cls(
            query=query,
            inputs=inputs,
            response_mode=response_mode,
            user=user,
            conversation_id=conversation_id,
            files=files,
            auto_generate_name=auto_generate_name,
        )

        post_chat_messages_body.additional_properties = d
        return post_chat_messages_body

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
