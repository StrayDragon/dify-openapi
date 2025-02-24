from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadedFile")


@_attrs_define
class UploadedFile:
    """
    Attributes:
        id (Union[Unset, str]): 文件 ID
        name (Union[Unset, str]): 文件名
        size (Union[Unset, int]): 文件大小（byte）
        extension (Union[Unset, str]): 文件后缀
        mime_type (Union[Unset, str]): 文件 mime-type
        created_by (Union[Unset, str]): 上传人 ID
        created_at (Union[Unset, int]): 上传时间
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    extension: Union[Unset, str] = UNSET
    mime_type: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_at: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        size = self.size

        extension = self.extension

        mime_type = self.mime_type

        created_by = self.created_by

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if size is not UNSET:
            field_dict["size"] = size
        if extension is not UNSET:
            field_dict["extension"] = extension
        if mime_type is not UNSET:
            field_dict["mime_type"] = mime_type
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        size = d.pop("size", UNSET)

        extension = d.pop("extension", UNSET)

        mime_type = d.pop("mime_type", UNSET)

        created_by = d.pop("created_by", UNSET)

        created_at = d.pop("created_at", UNSET)

        uploaded_file = cls(
            id=id,
            name=name,
            size=size,
            extension=extension,
            mime_type=mime_type,
            created_by=created_by,
            created_at=created_at,
        )

        uploaded_file.additional_properties = d
        return uploaded_file

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
