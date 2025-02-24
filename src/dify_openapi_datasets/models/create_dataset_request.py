from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_dataset_request_indexing_technique import (
    CreateDatasetRequestIndexingTechnique,
    check_create_dataset_request_indexing_technique,
)
from ..models.create_dataset_request_permission import (
    CreateDatasetRequestPermission,
    check_create_dataset_request_permission,
)
from ..models.create_dataset_request_provider import CreateDatasetRequestProvider, check_create_dataset_request_provider
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateDatasetRequest")


@_attrs_define
class CreateDatasetRequest:
    """
    Attributes:
        name (str): 知识库名称（必填）
        description (Union[Unset, str]): 知识库描述（选填）
        indexing_technique (Union[Unset, CreateDatasetRequestIndexingTechnique]): 索引模式（选填，建议填写）
            - high_quality: 高质量
            - economy: 经济
        permission (Union[Unset, CreateDatasetRequestPermission]): 权限（选填，默认 only_me）
            - only_me: 仅自己
            - all_team_members: 所有团队成员
            - partial_members: 部分团队成员
             Default: 'only_me'.
        provider (Union[Unset, CreateDatasetRequestProvider]): Provider（选填，默认 vendor）
            - vendor: 上传文件
            - external: 外部知识库
             Default: 'vendor'.
        external_knowledge_api_id (Union[Unset, str]): 外部知识库 API_ID（选填）
        external_knowledge_id (Union[Unset, str]): 外部知识库 ID（选填）
    """

    name: str
    description: Union[Unset, str] = UNSET
    indexing_technique: Union[Unset, CreateDatasetRequestIndexingTechnique] = UNSET
    permission: Union[Unset, CreateDatasetRequestPermission] = "only_me"
    provider: Union[Unset, CreateDatasetRequestProvider] = "vendor"
    external_knowledge_api_id: Union[Unset, str] = UNSET
    external_knowledge_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        indexing_technique: Union[Unset, str] = UNSET
        if not isinstance(self.indexing_technique, Unset):
            indexing_technique = self.indexing_technique

        permission: Union[Unset, str] = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission

        provider: Union[Unset, str] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider

        external_knowledge_api_id = self.external_knowledge_api_id

        external_knowledge_id = self.external_knowledge_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if indexing_technique is not UNSET:
            field_dict["indexing_technique"] = indexing_technique
        if permission is not UNSET:
            field_dict["permission"] = permission
        if provider is not UNSET:
            field_dict["provider"] = provider
        if external_knowledge_api_id is not UNSET:
            field_dict["external_knowledge_api_id"] = external_knowledge_api_id
        if external_knowledge_id is not UNSET:
            field_dict["external_knowledge_id"] = external_knowledge_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description", UNSET)

        _indexing_technique = d.pop("indexing_technique", UNSET)
        indexing_technique: Union[Unset, CreateDatasetRequestIndexingTechnique]
        if isinstance(_indexing_technique, Unset):
            indexing_technique = UNSET
        else:
            indexing_technique = check_create_dataset_request_indexing_technique(_indexing_technique)

        _permission = d.pop("permission", UNSET)
        permission: Union[Unset, CreateDatasetRequestPermission]
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = check_create_dataset_request_permission(_permission)

        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, CreateDatasetRequestProvider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = check_create_dataset_request_provider(_provider)

        external_knowledge_api_id = d.pop("external_knowledge_api_id", UNSET)

        external_knowledge_id = d.pop("external_knowledge_id", UNSET)

        create_dataset_request = cls(
            name=name,
            description=description,
            indexing_technique=indexing_technique,
            permission=permission,
            provider=provider,
            external_knowledge_api_id=external_knowledge_api_id,
            external_knowledge_id=external_knowledge_id,
        )

        create_dataset_request.additional_properties = d
        return create_dataset_request

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
