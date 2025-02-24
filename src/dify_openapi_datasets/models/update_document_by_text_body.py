from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_document_by_text_body_doc_type import (
    UpdateDocumentByTextBodyDocType,
    check_update_document_by_text_body_doc_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.process_rule import ProcessRule
    from ..models.update_document_by_text_body_doc_metadata import UpdateDocumentByTextBodyDocMetadata


T = TypeVar("T", bound="UpdateDocumentByTextBody")


@_attrs_define
class UpdateDocumentByTextBody:
    """
    Attributes:
        name (Union[Unset, str]): 文档名称
        text (Union[Unset, str]): 文档内容
        doc_type (Union[Unset, UpdateDocumentByTextBodyDocType]): 文档类型
        doc_metadata (Union[Unset, UpdateDocumentByTextBodyDocMetadata]): 文档元数据
        process_rule (Union[Unset, ProcessRule]):
    """

    name: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    doc_type: Union[Unset, UpdateDocumentByTextBodyDocType] = UNSET
    doc_metadata: Union[Unset, "UpdateDocumentByTextBodyDocMetadata"] = UNSET
    process_rule: Union[Unset, "ProcessRule"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        text = self.text

        doc_type: Union[Unset, str] = UNSET
        if not isinstance(self.doc_type, Unset):
            doc_type = self.doc_type

        doc_metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.doc_metadata, Unset):
            doc_metadata = self.doc_metadata.to_dict()

        process_rule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.process_rule, Unset):
            process_rule = self.process_rule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if text is not UNSET:
            field_dict["text"] = text
        if doc_type is not UNSET:
            field_dict["doc_type"] = doc_type
        if doc_metadata is not UNSET:
            field_dict["doc_metadata"] = doc_metadata
        if process_rule is not UNSET:
            field_dict["process_rule"] = process_rule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.process_rule import ProcessRule
        from ..models.update_document_by_text_body_doc_metadata import UpdateDocumentByTextBodyDocMetadata

        d = src_dict.copy()
        name = d.pop("name", UNSET)

        text = d.pop("text", UNSET)

        _doc_type = d.pop("doc_type", UNSET)
        doc_type: Union[Unset, UpdateDocumentByTextBodyDocType]
        if isinstance(_doc_type, Unset):
            doc_type = UNSET
        else:
            doc_type = check_update_document_by_text_body_doc_type(_doc_type)

        _doc_metadata = d.pop("doc_metadata", UNSET)
        doc_metadata: Union[Unset, UpdateDocumentByTextBodyDocMetadata]
        if isinstance(_doc_metadata, Unset):
            doc_metadata = UNSET
        else:
            doc_metadata = UpdateDocumentByTextBodyDocMetadata.from_dict(_doc_metadata)

        _process_rule = d.pop("process_rule", UNSET)
        process_rule: Union[Unset, ProcessRule]
        if isinstance(_process_rule, Unset):
            process_rule = UNSET
        else:
            process_rule = ProcessRule.from_dict(_process_rule)

        update_document_by_text_body = cls(
            name=name,
            text=text,
            doc_type=doc_type,
            doc_metadata=doc_metadata,
            process_rule=process_rule,
        )

        update_document_by_text_body.additional_properties = d
        return update_document_by_text_body

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
