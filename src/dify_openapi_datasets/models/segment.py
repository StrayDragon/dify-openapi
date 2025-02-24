from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Segment")


@_attrs_define
class Segment:
    """
    Attributes:
        id (Union[Unset, str]):
        position (Union[Unset, int]):
        document_id (Union[Unset, str]):
        content (Union[Unset, str]):
        answer (Union[None, Unset, str]):
        word_count (Union[Unset, int]):
        tokens (Union[Unset, int]):
        keywords (Union[Unset, list[str]]):
        index_node_id (Union[Unset, str]):
        index_node_hash (Union[Unset, str]):
        hit_count (Union[Unset, int]):
        enabled (Union[Unset, bool]):
        disabled_at (Union[None, Unset, str]):
        disabled_by (Union[None, Unset, str]):
        status (Union[Unset, str]):
        created_by (Union[Unset, str]):
        created_at (Union[Unset, int]):
        indexing_at (Union[Unset, int]):
        completed_at (Union[Unset, int]):
        error (Union[None, Unset, str]):
        stopped_at (Union[None, Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    position: Union[Unset, int] = UNSET
    document_id: Union[Unset, str] = UNSET
    content: Union[Unset, str] = UNSET
    answer: Union[None, Unset, str] = UNSET
    word_count: Union[Unset, int] = UNSET
    tokens: Union[Unset, int] = UNSET
    keywords: Union[Unset, list[str]] = UNSET
    index_node_id: Union[Unset, str] = UNSET
    index_node_hash: Union[Unset, str] = UNSET
    hit_count: Union[Unset, int] = UNSET
    enabled: Union[Unset, bool] = UNSET
    disabled_at: Union[None, Unset, str] = UNSET
    disabled_by: Union[None, Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_at: Union[Unset, int] = UNSET
    indexing_at: Union[Unset, int] = UNSET
    completed_at: Union[Unset, int] = UNSET
    error: Union[None, Unset, str] = UNSET
    stopped_at: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        position = self.position

        document_id = self.document_id

        content = self.content

        answer: Union[None, Unset, str]
        if isinstance(self.answer, Unset):
            answer = UNSET
        else:
            answer = self.answer

        word_count = self.word_count

        tokens = self.tokens

        keywords: Union[Unset, list[str]] = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        index_node_id = self.index_node_id

        index_node_hash = self.index_node_hash

        hit_count = self.hit_count

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

        status = self.status

        created_by = self.created_by

        created_at = self.created_at

        indexing_at = self.indexing_at

        completed_at = self.completed_at

        error: Union[None, Unset, str]
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        stopped_at: Union[None, Unset, str]
        if isinstance(self.stopped_at, Unset):
            stopped_at = UNSET
        else:
            stopped_at = self.stopped_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if position is not UNSET:
            field_dict["position"] = position
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
        if content is not UNSET:
            field_dict["content"] = content
        if answer is not UNSET:
            field_dict["answer"] = answer
        if word_count is not UNSET:
            field_dict["word_count"] = word_count
        if tokens is not UNSET:
            field_dict["tokens"] = tokens
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if index_node_id is not UNSET:
            field_dict["index_node_id"] = index_node_id
        if index_node_hash is not UNSET:
            field_dict["index_node_hash"] = index_node_hash
        if hit_count is not UNSET:
            field_dict["hit_count"] = hit_count
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if disabled_at is not UNSET:
            field_dict["disabled_at"] = disabled_at
        if disabled_by is not UNSET:
            field_dict["disabled_by"] = disabled_by
        if status is not UNSET:
            field_dict["status"] = status
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if indexing_at is not UNSET:
            field_dict["indexing_at"] = indexing_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if error is not UNSET:
            field_dict["error"] = error
        if stopped_at is not UNSET:
            field_dict["stopped_at"] = stopped_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        position = d.pop("position", UNSET)

        document_id = d.pop("document_id", UNSET)

        content = d.pop("content", UNSET)

        def _parse_answer(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        answer = _parse_answer(d.pop("answer", UNSET))

        word_count = d.pop("word_count", UNSET)

        tokens = d.pop("tokens", UNSET)

        keywords = cast(list[str], d.pop("keywords", UNSET))

        index_node_id = d.pop("index_node_id", UNSET)

        index_node_hash = d.pop("index_node_hash", UNSET)

        hit_count = d.pop("hit_count", UNSET)

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

        status = d.pop("status", UNSET)

        created_by = d.pop("created_by", UNSET)

        created_at = d.pop("created_at", UNSET)

        indexing_at = d.pop("indexing_at", UNSET)

        completed_at = d.pop("completed_at", UNSET)

        def _parse_error(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_stopped_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        stopped_at = _parse_stopped_at(d.pop("stopped_at", UNSET))

        segment = cls(
            id=id,
            position=position,
            document_id=document_id,
            content=content,
            answer=answer,
            word_count=word_count,
            tokens=tokens,
            keywords=keywords,
            index_node_id=index_node_id,
            index_node_hash=index_node_hash,
            hit_count=hit_count,
            enabled=enabled,
            disabled_at=disabled_at,
            disabled_by=disabled_by,
            status=status,
            created_by=created_by,
            created_at=created_at,
            indexing_at=indexing_at,
            completed_at=completed_at,
            error=error,
            stopped_at=stopped_at,
        )

        segment.additional_properties = d
        return segment

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
