from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_data_source_info import DocumentDataSourceInfo


T = TypeVar("T", bound="Document")


@_attrs_define
class Document:
    """
    Attributes:
        id (Union[Unset, str]):
        position (Union[Unset, int]):
        data_source_type (Union[Unset, str]):
        data_source_info (Union[Unset, DocumentDataSourceInfo]):
        dataset_process_rule_id (Union[Unset, str]):
        name (Union[Unset, str]):
        created_from (Union[Unset, str]):
        created_by (Union[Unset, str]):
        created_at (Union[Unset, int]):
        tokens (Union[Unset, int]):
        indexing_status (Union[Unset, str]):
        error (Union[None, Unset, str]):
        enabled (Union[Unset, bool]):
        disabled_at (Union[None, Unset, str]):
        disabled_by (Union[None, Unset, str]):
        archived (Union[Unset, bool]):
        display_status (Union[Unset, str]):
        word_count (Union[Unset, int]):
        hit_count (Union[Unset, int]):
        doc_form (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    position: Union[Unset, int] = UNSET
    data_source_type: Union[Unset, str] = UNSET
    data_source_info: Union[Unset, "DocumentDataSourceInfo"] = UNSET
    dataset_process_rule_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    created_from: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_at: Union[Unset, int] = UNSET
    tokens: Union[Unset, int] = UNSET
    indexing_status: Union[Unset, str] = UNSET
    error: Union[None, Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    disabled_at: Union[None, Unset, str] = UNSET
    disabled_by: Union[None, Unset, str] = UNSET
    archived: Union[Unset, bool] = UNSET
    display_status: Union[Unset, str] = UNSET
    word_count: Union[Unset, int] = UNSET
    hit_count: Union[Unset, int] = UNSET
    doc_form: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        position = self.position

        data_source_type = self.data_source_type

        data_source_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data_source_info, Unset):
            data_source_info = self.data_source_info.to_dict()

        dataset_process_rule_id = self.dataset_process_rule_id

        name = self.name

        created_from = self.created_from

        created_by = self.created_by

        created_at = self.created_at

        tokens = self.tokens

        indexing_status = self.indexing_status

        error: Union[None, Unset, str]
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        enabled = self.enabled

        disabled_at: Union[None, Unset, str]
        if isinstance(self.disabled_at, Unset):
            disabled_at = UNSET
        else:
            disabled_at = self.disabled_at

        disabled_by: Union[None, Unset, str]
        if isinstance(self.disabled_by, Unset):
            disabled_by = UNSET
        else:
            disabled_by = self.disabled_by

        archived = self.archived

        display_status = self.display_status

        word_count = self.word_count

        hit_count = self.hit_count

        doc_form = self.doc_form

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if position is not UNSET:
            field_dict["position"] = position
        if data_source_type is not UNSET:
            field_dict["data_source_type"] = data_source_type
        if data_source_info is not UNSET:
            field_dict["data_source_info"] = data_source_info
        if dataset_process_rule_id is not UNSET:
            field_dict["dataset_process_rule_id"] = dataset_process_rule_id
        if name is not UNSET:
            field_dict["name"] = name
        if created_from is not UNSET:
            field_dict["created_from"] = created_from
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if tokens is not UNSET:
            field_dict["tokens"] = tokens
        if indexing_status is not UNSET:
            field_dict["indexing_status"] = indexing_status
        if error is not UNSET:
            field_dict["error"] = error
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if disabled_at is not UNSET:
            field_dict["disabled_at"] = disabled_at
        if disabled_by is not UNSET:
            field_dict["disabled_by"] = disabled_by
        if archived is not UNSET:
            field_dict["archived"] = archived
        if display_status is not UNSET:
            field_dict["display_status"] = display_status
        if word_count is not UNSET:
            field_dict["word_count"] = word_count
        if hit_count is not UNSET:
            field_dict["hit_count"] = hit_count
        if doc_form is not UNSET:
            field_dict["doc_form"] = doc_form

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.document_data_source_info import DocumentDataSourceInfo

        d = src_dict.copy()
        id = d.pop("id", UNSET)

        position = d.pop("position", UNSET)

        data_source_type = d.pop("data_source_type", UNSET)

        _data_source_info = d.pop("data_source_info", UNSET)
        data_source_info: Union[Unset, DocumentDataSourceInfo]
        if isinstance(_data_source_info, Unset):
            data_source_info = UNSET
        else:
            data_source_info = DocumentDataSourceInfo.from_dict(_data_source_info)

        dataset_process_rule_id = d.pop("dataset_process_rule_id", UNSET)

        name = d.pop("name", UNSET)

        created_from = d.pop("created_from", UNSET)

        created_by = d.pop("created_by", UNSET)

        created_at = d.pop("created_at", UNSET)

        tokens = d.pop("tokens", UNSET)

        indexing_status = d.pop("indexing_status", UNSET)

        def _parse_error(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        error = _parse_error(d.pop("error", UNSET))

        enabled = d.pop("enabled", UNSET)

        def _parse_disabled_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        disabled_at = _parse_disabled_at(d.pop("disabled_at", UNSET))

        def _parse_disabled_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        disabled_by = _parse_disabled_by(d.pop("disabled_by", UNSET))

        archived = d.pop("archived", UNSET)

        display_status = d.pop("display_status", UNSET)

        word_count = d.pop("word_count", UNSET)

        hit_count = d.pop("hit_count", UNSET)

        doc_form = d.pop("doc_form", UNSET)

        document = cls(
            id=id,
            position=position,
            data_source_type=data_source_type,
            data_source_info=data_source_info,
            dataset_process_rule_id=dataset_process_rule_id,
            name=name,
            created_from=created_from,
            created_by=created_by,
            created_at=created_at,
            tokens=tokens,
            indexing_status=indexing_status,
            error=error,
            enabled=enabled,
            disabled_at=disabled_at,
            disabled_by=disabled_by,
            archived=archived,
            display_status=display_status,
            word_count=word_count,
            hit_count=hit_count,
            doc_form=doc_form,
        )

        document.additional_properties = d
        return document

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
