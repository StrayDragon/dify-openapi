from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_input_transfer_method import FileInputTransferMethod, check_file_input_transfer_method
from ..models.file_input_type import FileInputType, check_file_input_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileInput")


@_attrs_define
class FileInput:
    """
    Attributes:
        type_ (Union[Unset, FileInputType]): 文件类型
        transfer_method (Union[Unset, FileInputTransferMethod]): 传递方式
        url (Union[Unset, str]): 远程URL
        upload_file_id (Union[Unset, str]): 上传文件ID
    """

    type_: Union[Unset, FileInputType] = UNSET
    transfer_method: Union[Unset, FileInputTransferMethod] = UNSET
    url: Union[Unset, str] = UNSET
    upload_file_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        transfer_method: Union[Unset, str] = UNSET
        if not isinstance(self.transfer_method, Unset):
            transfer_method = self.transfer_method

        url = self.url

        upload_file_id = self.upload_file_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if transfer_method is not UNSET:
            field_dict["transfer_method"] = transfer_method
        if url is not UNSET:
            field_dict["url"] = url
        if upload_file_id is not UNSET:
            field_dict["upload_file_id"] = upload_file_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, FileInputType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_file_input_type(_type_)

        _transfer_method = d.pop("transfer_method", UNSET)
        transfer_method: Union[Unset, FileInputTransferMethod]
        if isinstance(_transfer_method, Unset):
            transfer_method = UNSET
        else:
            transfer_method = check_file_input_transfer_method(_transfer_method)

        url = d.pop("url", UNSET)

        upload_file_id = d.pop("upload_file_id", UNSET)

        file_input = cls(
            type_=type_,
            transfer_method=transfer_method,
            url=url,
            upload_file_id=upload_file_id,
        )

        file_input.additional_properties = d
        return file_input

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
