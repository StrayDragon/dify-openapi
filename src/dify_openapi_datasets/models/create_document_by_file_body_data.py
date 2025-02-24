from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_document_by_file_body_data_doc_form import (
    CreateDocumentByFileBodyDataDocForm,
    check_create_document_by_file_body_data_doc_form,
)
from ..models.create_document_by_file_body_data_doc_type import (
    CreateDocumentByFileBodyDataDocType,
    check_create_document_by_file_body_data_doc_type,
)
from ..models.create_document_by_file_body_data_indexing_technique import (
    CreateDocumentByFileBodyDataIndexingTechnique,
    check_create_document_by_file_body_data_indexing_technique,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_metadata import DocumentMetadata
    from ..models.process_rule import ProcessRule
    from ..models.retrieval_model import RetrievalModel


T = TypeVar("T", bound="CreateDocumentByFileBodyData")


@_attrs_define
class CreateDocumentByFileBodyData:
    """文档配置信息，JSON字符串格式，包含以下字段：
    - original_document_id: 源文档ID（选填），用于重新上传或修改文档配置
    - indexing_technique: 索引方式（high_quality/economy）
    - doc_form: 索引内容形式（text_model/hierarchical_model/qa_model）
    - doc_type: 文档类型
    - doc_metadata: 文档元数据
    - doc_language: 文档语言（Q&A模式必填）
    - process_rule: 处理规则

        Example:
            {"indexing_technique":"high_quality","process_rule":{"rules":{"pre_processing_rules":[{"id":"remove_extra_spaces
                ","enabled":true},{"id":"remove_urls_emails","enabled":true}],"segmentation":{"separator":"###","max_tokens":500
                }},"mode":"custom"}}

        Attributes:
            original_document_id (Union[Unset, str]): 源文档ID，用于重新上传或修改文档配置
            indexing_technique (Union[Unset, CreateDocumentByFileBodyDataIndexingTechnique]): 索引方式
            doc_form (Union[Unset, CreateDocumentByFileBodyDataDocForm]): 索引内容形式
            doc_type (Union[Unset, CreateDocumentByFileBodyDataDocType]): 文档类型
            doc_metadata (Union[Unset, DocumentMetadata]): 文档元数据，根据文档类型有不同的字段要求
            doc_language (Union[Unset, str]): 文档语言（Q&A模式必填）
            process_rule (Union[Unset, ProcessRule]):
            retrieval_model (Union[Unset, RetrievalModel]):
            embedding_model (Union[Unset, str]): Embedding模型名称
            embedding_model_provider (Union[Unset, str]): Embedding模型供应商
    """

    original_document_id: Union[Unset, str] = UNSET
    indexing_technique: Union[Unset, CreateDocumentByFileBodyDataIndexingTechnique] = UNSET
    doc_form: Union[Unset, CreateDocumentByFileBodyDataDocForm] = UNSET
    doc_type: Union[Unset, CreateDocumentByFileBodyDataDocType] = UNSET
    doc_metadata: Union[Unset, "DocumentMetadata"] = UNSET
    doc_language: Union[Unset, str] = UNSET
    process_rule: Union[Unset, "ProcessRule"] = UNSET
    retrieval_model: Union[Unset, "RetrievalModel"] = UNSET
    embedding_model: Union[Unset, str] = UNSET
    embedding_model_provider: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        original_document_id = self.original_document_id

        indexing_technique: Union[Unset, str] = UNSET
        if not isinstance(self.indexing_technique, Unset):
            indexing_technique = self.indexing_technique

        doc_form: Union[Unset, str] = UNSET
        if not isinstance(self.doc_form, Unset):
            doc_form = self.doc_form

        doc_type: Union[Unset, str] = UNSET
        if not isinstance(self.doc_type, Unset):
            doc_type = self.doc_type

        doc_metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.doc_metadata, Unset):
            doc_metadata = self.doc_metadata.to_dict()

        doc_language = self.doc_language

        process_rule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.process_rule, Unset):
            process_rule = self.process_rule.to_dict()

        retrieval_model: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.retrieval_model, Unset):
            retrieval_model = self.retrieval_model.to_dict()

        embedding_model = self.embedding_model

        embedding_model_provider = self.embedding_model_provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if original_document_id is not UNSET:
            field_dict["original_document_id"] = original_document_id
        if indexing_technique is not UNSET:
            field_dict["indexing_technique"] = indexing_technique
        if doc_form is not UNSET:
            field_dict["doc_form"] = doc_form
        if doc_type is not UNSET:
            field_dict["doc_type"] = doc_type
        if doc_metadata is not UNSET:
            field_dict["doc_metadata"] = doc_metadata
        if doc_language is not UNSET:
            field_dict["doc_language"] = doc_language
        if process_rule is not UNSET:
            field_dict["process_rule"] = process_rule
        if retrieval_model is not UNSET:
            field_dict["retrieval_model"] = retrieval_model
        if embedding_model is not UNSET:
            field_dict["embedding_model"] = embedding_model
        if embedding_model_provider is not UNSET:
            field_dict["embedding_model_provider"] = embedding_model_provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.document_metadata import DocumentMetadata
        from ..models.process_rule import ProcessRule
        from ..models.retrieval_model import RetrievalModel

        d = src_dict.copy()
        original_document_id = d.pop("original_document_id", UNSET)

        _indexing_technique = d.pop("indexing_technique", UNSET)
        indexing_technique: Union[Unset, CreateDocumentByFileBodyDataIndexingTechnique]
        if isinstance(_indexing_technique, Unset):
            indexing_technique = UNSET
        else:
            indexing_technique = check_create_document_by_file_body_data_indexing_technique(_indexing_technique)

        _doc_form = d.pop("doc_form", UNSET)
        doc_form: Union[Unset, CreateDocumentByFileBodyDataDocForm]
        if isinstance(_doc_form, Unset):
            doc_form = UNSET
        else:
            doc_form = check_create_document_by_file_body_data_doc_form(_doc_form)

        _doc_type = d.pop("doc_type", UNSET)
        doc_type: Union[Unset, CreateDocumentByFileBodyDataDocType]
        if isinstance(_doc_type, Unset):
            doc_type = UNSET
        else:
            doc_type = check_create_document_by_file_body_data_doc_type(_doc_type)

        _doc_metadata = d.pop("doc_metadata", UNSET)
        doc_metadata: Union[Unset, DocumentMetadata]
        if isinstance(_doc_metadata, Unset):
            doc_metadata = UNSET
        else:
            doc_metadata = DocumentMetadata.from_dict(_doc_metadata)

        doc_language = d.pop("doc_language", UNSET)

        _process_rule = d.pop("process_rule", UNSET)
        process_rule: Union[Unset, ProcessRule]
        if isinstance(_process_rule, Unset):
            process_rule = UNSET
        else:
            process_rule = ProcessRule.from_dict(_process_rule)

        _retrieval_model = d.pop("retrieval_model", UNSET)
        retrieval_model: Union[Unset, RetrievalModel]
        if isinstance(_retrieval_model, Unset):
            retrieval_model = UNSET
        else:
            retrieval_model = RetrievalModel.from_dict(_retrieval_model)

        embedding_model = d.pop("embedding_model", UNSET)

        embedding_model_provider = d.pop("embedding_model_provider", UNSET)

        create_document_by_file_body_data = cls(
            original_document_id=original_document_id,
            indexing_technique=indexing_technique,
            doc_form=doc_form,
            doc_type=doc_type,
            doc_metadata=doc_metadata,
            doc_language=doc_language,
            process_rule=process_rule,
            retrieval_model=retrieval_model,
            embedding_model=embedding_model,
            embedding_model_provider=embedding_model_provider,
        )

        create_document_by_file_body_data.additional_properties = d
        return create_document_by_file_body_data

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
