import json
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, Unset

if TYPE_CHECKING:
    from ..models.create_document_by_file_body_data import CreateDocumentByFileBodyData


T = TypeVar("T", bound="CreateDocumentByFileBody")


@_attrs_define
class CreateDocumentByFileBody:
    """
    Attributes:
        file (File): 需要上传的文件
        data (Union[Unset, CreateDocumentByFileBodyData]): 文档配置信息，JSON字符串格式，包含以下字段：
            - original_document_id: 源文档ID（选填），用于重新上传或修改文档配置
            - indexing_technique: 索引方式（high_quality/economy）
            - doc_form: 索引内容形式（text_model/hierarchical_model/qa_model）
            - doc_type: 文档类型
            - doc_metadata: 文档元数据
            - doc_language: 文档语言（Q&A模式必填）
            - process_rule: 处理规则
             Example: {"indexing_technique":"high_quality","process_rule":{"rules":{"pre_processing_rules":[{"id":"remove_ex
            tra_spaces","enabled":true},{"id":"remove_urls_emails","enabled":true}],"segmentation":{"separator":"###","max_t
            okens":500}},"mode":"custom"}}
            .
    """

    file: File
    data: Union[Unset, "CreateDocumentByFileBodyData"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        data: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.data, Unset):
            data = (None, json.dumps(self.data.to_dict()).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "file": file,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.create_document_by_file_body_data import CreateDocumentByFileBodyData

        d = src_dict.copy()
        file = File(payload=BytesIO(d.pop("file")))

        _data = d.pop("data", UNSET)
        data: Union[Unset, CreateDocumentByFileBodyData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = CreateDocumentByFileBodyData.from_dict(_data)

        create_document_by_file_body = cls(
            file=file,
            data=data,
        )

        create_document_by_file_body.additional_properties = d
        return create_document_by_file_body

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
