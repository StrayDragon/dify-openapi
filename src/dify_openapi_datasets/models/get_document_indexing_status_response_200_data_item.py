from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetDocumentIndexingStatusResponse200DataItem")


@_attrs_define
class GetDocumentIndexingStatusResponse200DataItem:
    """
    Attributes:
        id (Union[Unset, str]):
        indexing_status (Union[Unset, str]):
        processing_started_at (Union[Unset, float]):
        parsing_completed_at (Union[Unset, float]):
        cleaning_completed_at (Union[Unset, float]):
        splitting_completed_at (Union[Unset, float]):
        completed_at (Union[None, Unset, float]):
        paused_at (Union[None, Unset, float]):
        error (Union[None, Unset, str]):
        stopped_at (Union[None, Unset, float]):
        completed_segments (Union[Unset, int]):
        total_segments (Union[Unset, int]):
    """

    id: Union[Unset, str] = UNSET
    indexing_status: Union[Unset, str] = UNSET
    processing_started_at: Union[Unset, float] = UNSET
    parsing_completed_at: Union[Unset, float] = UNSET
    cleaning_completed_at: Union[Unset, float] = UNSET
    splitting_completed_at: Union[Unset, float] = UNSET
    completed_at: Union[None, Unset, float] = UNSET
    paused_at: Union[None, Unset, float] = UNSET
    error: Union[None, Unset, str] = UNSET
    stopped_at: Union[None, Unset, float] = UNSET
    completed_segments: Union[Unset, int] = UNSET
    total_segments: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        indexing_status = self.indexing_status

        processing_started_at = self.processing_started_at

        parsing_completed_at = self.parsing_completed_at

        cleaning_completed_at = self.cleaning_completed_at

        splitting_completed_at = self.splitting_completed_at

        completed_at: Union[None, Unset, float]
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        else:
            completed_at = self.completed_at

        paused_at: Union[None, Unset, float]
        if isinstance(self.paused_at, Unset):
            paused_at = UNSET
        else:
            paused_at = self.paused_at

        error: Union[None, Unset, str]
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        stopped_at: Union[None, Unset, float]
        if isinstance(self.stopped_at, Unset):
            stopped_at = UNSET
        else:
            stopped_at = self.stopped_at

        completed_segments = self.completed_segments

        total_segments = self.total_segments

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if indexing_status is not UNSET:
            field_dict["indexing_status"] = indexing_status
        if processing_started_at is not UNSET:
            field_dict["processing_started_at"] = processing_started_at
        if parsing_completed_at is not UNSET:
            field_dict["parsing_completed_at"] = parsing_completed_at
        if cleaning_completed_at is not UNSET:
            field_dict["cleaning_completed_at"] = cleaning_completed_at
        if splitting_completed_at is not UNSET:
            field_dict["splitting_completed_at"] = splitting_completed_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if paused_at is not UNSET:
            field_dict["paused_at"] = paused_at
        if error is not UNSET:
            field_dict["error"] = error
        if stopped_at is not UNSET:
            field_dict["stopped_at"] = stopped_at
        if completed_segments is not UNSET:
            field_dict["completed_segments"] = completed_segments
        if total_segments is not UNSET:
            field_dict["total_segments"] = total_segments

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        indexing_status = d.pop("indexing_status", UNSET)

        processing_started_at = d.pop("processing_started_at", UNSET)

        parsing_completed_at = d.pop("parsing_completed_at", UNSET)

        cleaning_completed_at = d.pop("cleaning_completed_at", UNSET)

        splitting_completed_at = d.pop("splitting_completed_at", UNSET)

        def _parse_completed_at(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        completed_at = _parse_completed_at(d.pop("completed_at", UNSET))

        def _parse_paused_at(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        paused_at = _parse_paused_at(d.pop("paused_at", UNSET))

        def _parse_error(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_stopped_at(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        stopped_at = _parse_stopped_at(d.pop("stopped_at", UNSET))

        completed_segments = d.pop("completed_segments", UNSET)

        total_segments = d.pop("total_segments", UNSET)

        get_document_indexing_status_response_200_data_item = cls(
            id=id,
            indexing_status=indexing_status,
            processing_started_at=processing_started_at,
            parsing_completed_at=parsing_completed_at,
            cleaning_completed_at=cleaning_completed_at,
            splitting_completed_at=splitting_completed_at,
            completed_at=completed_at,
            paused_at=paused_at,
            error=error,
            stopped_at=stopped_at,
            completed_segments=completed_segments,
            total_segments=total_segments,
        )

        get_document_indexing_status_response_200_data_item.additional_properties = d
        return get_document_indexing_status_response_200_data_item

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
