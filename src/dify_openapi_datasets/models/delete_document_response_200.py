from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delete_document_response_200_result import (
    DeleteDocumentResponse200Result,
    check_delete_document_response_200_result,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteDocumentResponse200")


@_attrs_define
class DeleteDocumentResponse200:
    """
    Attributes:
        result (Union[Unset, DeleteDocumentResponse200Result]):
    """

    result: Union[Unset, DeleteDocumentResponse200Result] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        result: Union[Unset, str] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _result = d.pop("result", UNSET)
        result: Union[Unset, DeleteDocumentResponse200Result]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = check_delete_document_response_200_result(_result)

        delete_document_response_200 = cls(
            result=result,
        )

        delete_document_response_200.additional_properties = d
        return delete_document_response_200

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
