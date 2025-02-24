from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.update_segment_body_segment import UpdateSegmentBodySegment


T = TypeVar("T", bound="UpdateSegmentBody")


@_attrs_define
class UpdateSegmentBody:
    """
    Attributes:
        segment (UpdateSegmentBodySegment):
    """

    segment: "UpdateSegmentBodySegment"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        segment = self.segment.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "segment": segment,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.update_segment_body_segment import UpdateSegmentBodySegment

        d = src_dict.copy()
        segment = UpdateSegmentBodySegment.from_dict(d.pop("segment"))

        update_segment_body = cls(
            segment=segment,
        )

        update_segment_body.additional_properties = d
        return update_segment_body

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
