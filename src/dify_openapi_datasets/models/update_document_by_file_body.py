import json
from io import BytesIO
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, File, Unset

if TYPE_CHECKING:
    from ..models.process_rule import ProcessRule


T = TypeVar("T", bound="UpdateDocumentByFileBody")


@_attrs_define
class UpdateDocumentByFileBody:
    """
    Attributes:
        file (File): 上传的文件
        name (Union[Unset, str]): 文档名称
        process_rule (Union[Unset, ProcessRule]):
    """

    file: File
    name: Union[Unset, str] = UNSET
    process_rule: Union[Unset, "ProcessRule"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        name = self.name

        process_rule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.process_rule, Unset):
            process_rule = self.process_rule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if process_rule is not UNSET:
            field_dict["process_rule"] = process_rule

        return field_dict

    def to_multipart(self) -> dict[str, Any]:
        file = self.file.to_tuple()

        name = self.name if isinstance(self.name, Unset) else (None, str(self.name).encode(), "text/plain")

        process_rule: Union[Unset, tuple[None, bytes, str]] = UNSET
        if not isinstance(self.process_rule, Unset):
            process_rule = (None, json.dumps(self.process_rule.to_dict()).encode(), "application/json")

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = (None, str(prop).encode(), "text/plain")

        field_dict.update(
            {
                "file": file,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if process_rule is not UNSET:
            field_dict["process_rule"] = process_rule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.process_rule import ProcessRule

        d = src_dict.copy()
        file = File(payload=BytesIO(d.pop("file")))

        name = d.pop("name", UNSET)

        _process_rule = d.pop("process_rule", UNSET)
        process_rule: Union[Unset, ProcessRule]
        if isinstance(_process_rule, Unset):
            process_rule = UNSET
        else:
            process_rule = ProcessRule.from_dict(_process_rule)

        update_document_by_file_body = cls(
            file=file,
            name=name,
            process_rule=process_rule,
        )

        update_document_by_file_body.additional_properties = d
        return update_document_by_file_body

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
