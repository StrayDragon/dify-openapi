from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_document_by_text_body_doc_form import (
    CreateDocumentByTextBodyDocForm,
    check_create_document_by_text_body_doc_form,
)
from ..models.create_document_by_text_body_doc_type import (
    CreateDocumentByTextBodyDocType,
    check_create_document_by_text_body_doc_type,
)
from ..models.create_document_by_text_body_indexing_technique import (
    CreateDocumentByTextBodyIndexingTechnique,
    check_create_document_by_text_body_indexing_technique,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_document_by_text_body_doc_metadata import CreateDocumentByTextBodyDocMetadata
    from ..models.process_rule import ProcessRule


T = TypeVar("T", bound="CreateDocumentByTextBody")


@_attrs_define
class CreateDocumentByTextBody:
    """
    Attributes:
        name (str): 文档名称
        text (str): 文档内容
        indexing_technique (CreateDocumentByTextBodyIndexingTechnique): 索引方式
        process_rule (ProcessRule):
        doc_type (Union[Unset, CreateDocumentByTextBodyDocType]): 文档类型
        doc_metadata (Union[Unset, CreateDocumentByTextBodyDocMetadata]): 文档元数据
        doc_form (Union[Unset, CreateDocumentByTextBodyDocForm]): 索引内容的形式
        doc_language (Union[Unset, str]): 文档语言（Q&A 模式下必填）
    """

    name: str
    text: str
    indexing_technique: CreateDocumentByTextBodyIndexingTechnique
    process_rule: "ProcessRule"
    doc_type: Union[Unset, CreateDocumentByTextBodyDocType] = UNSET
    doc_metadata: Union[Unset, "CreateDocumentByTextBodyDocMetadata"] = UNSET
    doc_form: Union[Unset, CreateDocumentByTextBodyDocForm] = UNSET
    doc_language: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        text = self.text

        indexing_technique: str = self.indexing_technique

        process_rule = self.process_rule.to_dict()

        doc_type: Union[Unset, str] = UNSET
        if not isinstance(self.doc_type, Unset):
            doc_type = self.doc_type

        doc_metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.doc_metadata, Unset):
            doc_metadata = self.doc_metadata.to_dict()

        doc_form: Union[Unset, str] = UNSET
        if not isinstance(self.doc_form, Unset):
            doc_form = self.doc_form

        doc_language = self.doc_language

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "text": text,
                "indexing_technique": indexing_technique,
                "process_rule": process_rule,
            }
        )
        if doc_type is not UNSET:
            field_dict["doc_type"] = doc_type
        if doc_metadata is not UNSET:
            field_dict["doc_metadata"] = doc_metadata
        if doc_form is not UNSET:
            field_dict["doc_form"] = doc_form
        if doc_language is not UNSET:
            field_dict["doc_language"] = doc_language

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.create_document_by_text_body_doc_metadata import CreateDocumentByTextBodyDocMetadata
        from ..models.process_rule import ProcessRule

        d = src_dict.copy()
        name = d.pop("name")

        text = d.pop("text")

        indexing_technique = check_create_document_by_text_body_indexing_technique(d.pop("indexing_technique"))

        process_rule = ProcessRule.from_dict(d.pop("process_rule"))

        _doc_type = d.pop("doc_type", UNSET)
        doc_type: Union[Unset, CreateDocumentByTextBodyDocType]
        if isinstance(_doc_type, Unset):
            doc_type = UNSET
        else:
            doc_type = check_create_document_by_text_body_doc_type(_doc_type)

        _doc_metadata = d.pop("doc_metadata", UNSET)
        doc_metadata: Union[Unset, CreateDocumentByTextBodyDocMetadata]
        if isinstance(_doc_metadata, Unset):
            doc_metadata = UNSET
        else:
            doc_metadata = CreateDocumentByTextBodyDocMetadata.from_dict(_doc_metadata)

        _doc_form = d.pop("doc_form", UNSET)
        doc_form: Union[Unset, CreateDocumentByTextBodyDocForm]
        if isinstance(_doc_form, Unset):
            doc_form = UNSET
        else:
            doc_form = check_create_document_by_text_body_doc_form(_doc_form)

        doc_language = d.pop("doc_language", UNSET)

        create_document_by_text_body = cls(
            name=name,
            text=text,
            indexing_technique=indexing_technique,
            process_rule=process_rule,
            doc_type=doc_type,
            doc_metadata=doc_metadata,
            doc_form=doc_form,
            doc_language=doc_language,
        )

        create_document_by_text_body.additional_properties = d
        return create_document_by_text_body

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
