from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document import Document


T = TypeVar("T", bound="UpdateDocumentByTextResponse200")


@_attrs_define
class UpdateDocumentByTextResponse200:
    """
    Attributes:
        document (Union[Unset, Document]):
        batch (Union[Unset, str]):
    """

    document: Union[Unset, "Document"] = UNSET
    batch: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.document, Unset):
            document = self.document.to_dict()

        batch = self.batch

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document is not UNSET:
            field_dict["document"] = document
        if batch is not UNSET:
            field_dict["batch"] = batch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.document import Document

        d = src_dict.copy()
        _document = d.pop("document", UNSET)
        document: Union[Unset, Document]
        if isinstance(_document, Unset):
            document = UNSET
        else:
            document = Document.from_dict(_document)

        batch = d.pop("batch", UNSET)

        update_document_by_text_response_200 = cls(
            document=document,
            batch=batch,
        )

        update_document_by_text_response_200.additional_properties = d
        return update_document_by_text_response_200

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
