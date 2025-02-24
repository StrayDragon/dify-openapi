from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dataset_indexing_technique import DatasetIndexingTechnique, check_dataset_indexing_technique
from ..models.dataset_permission import DatasetPermission, check_dataset_permission
from ..models.dataset_provider import DatasetProvider, check_dataset_provider
from ..types import UNSET, Unset

T = TypeVar("T", bound="Dataset")


@_attrs_define
class Dataset:
    """
    Attributes:
        id (Union[Unset, str]): 知识库 ID
        name (Union[Unset, str]): 知识库名称
        description (Union[None, Unset, str]): 知识库描述
        provider (Union[Unset, DatasetProvider]): 知识库提供者
        permission (Union[Unset, DatasetPermission]): 访问权限
        data_source_type (Union[None, Unset, str]): 数据源类型
        indexing_technique (Union[Unset, DatasetIndexingTechnique]): 索引技术
        app_count (Union[Unset, int]): 应用数量
        document_count (Union[Unset, int]): 文档数量
        word_count (Union[Unset, int]): 字数统计
        created_by (Union[Unset, str]): 创建者 ID
        created_at (Union[Unset, int]): 创建时间戳
        updated_by (Union[Unset, str]): 最后更新者 ID
        updated_at (Union[Unset, int]): 最后更新时间戳
        embedding_model (Union[None, Unset, str]): Embedding 模型名称
        embedding_model_provider (Union[None, Unset, str]): Embedding 模型提供商
        embedding_available (Union[None, Unset, bool]): Embedding 是否可用
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    provider: Union[Unset, DatasetProvider] = UNSET
    permission: Union[Unset, DatasetPermission] = UNSET
    data_source_type: Union[None, Unset, str] = UNSET
    indexing_technique: Union[Unset, DatasetIndexingTechnique] = UNSET
    app_count: Union[Unset, int] = UNSET
    document_count: Union[Unset, int] = UNSET
    word_count: Union[Unset, int] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_at: Union[Unset, int] = UNSET
    updated_by: Union[Unset, str] = UNSET
    updated_at: Union[Unset, int] = UNSET
    embedding_model: Union[None, Unset, str] = UNSET
    embedding_model_provider: Union[None, Unset, str] = UNSET
    embedding_available: Union[None, Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        provider: Union[Unset, str] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider

        permission: Union[Unset, str] = UNSET
        if not isinstance(self.permission, Unset):
            permission = self.permission

        data_source_type: Union[None, Unset, str]
        if isinstance(self.data_source_type, Unset):
            data_source_type = UNSET
        else:
            data_source_type = self.data_source_type

        indexing_technique: Union[Unset, str] = UNSET
        if not isinstance(self.indexing_technique, Unset):
            indexing_technique = self.indexing_technique

        app_count = self.app_count

        document_count = self.document_count

        word_count = self.word_count

        created_by = self.created_by

        created_at = self.created_at

        updated_by = self.updated_by

        updated_at = self.updated_at

        embedding_model: Union[None, Unset, str]
        if isinstance(self.embedding_model, Unset):
            embedding_model = UNSET
        else:
            embedding_model = self.embedding_model

        embedding_model_provider: Union[None, Unset, str]
        if isinstance(self.embedding_model_provider, Unset):
            embedding_model_provider = UNSET
        else:
            embedding_model_provider = self.embedding_model_provider

        embedding_available: Union[None, Unset, bool]
        if isinstance(self.embedding_available, Unset):
            embedding_available = UNSET
        else:
            embedding_available = self.embedding_available

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if provider is not UNSET:
            field_dict["provider"] = provider
        if permission is not UNSET:
            field_dict["permission"] = permission
        if data_source_type is not UNSET:
            field_dict["data_source_type"] = data_source_type
        if indexing_technique is not UNSET:
            field_dict["indexing_technique"] = indexing_technique
        if app_count is not UNSET:
            field_dict["app_count"] = app_count
        if document_count is not UNSET:
            field_dict["document_count"] = document_count
        if word_count is not UNSET:
            field_dict["word_count"] = word_count
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if embedding_model is not UNSET:
            field_dict["embedding_model"] = embedding_model
        if embedding_model_provider is not UNSET:
            field_dict["embedding_model_provider"] = embedding_model_provider
        if embedding_available is not UNSET:
            field_dict["embedding_available"] = embedding_available

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, DatasetProvider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = check_dataset_provider(_provider)

        _permission = d.pop("permission", UNSET)
        permission: Union[Unset, DatasetPermission]
        if isinstance(_permission, Unset):
            permission = UNSET
        else:
            permission = check_dataset_permission(_permission)

        def _parse_data_source_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        data_source_type = _parse_data_source_type(d.pop("data_source_type", UNSET))

        _indexing_technique = d.pop("indexing_technique", UNSET)
        indexing_technique: Union[Unset, DatasetIndexingTechnique]
        if isinstance(_indexing_technique, Unset):
            indexing_technique = UNSET
        else:
            indexing_technique = check_dataset_indexing_technique(_indexing_technique)

        app_count = d.pop("app_count", UNSET)

        document_count = d.pop("document_count", UNSET)

        word_count = d.pop("word_count", UNSET)

        created_by = d.pop("created_by", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_by = d.pop("updated_by", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        def _parse_embedding_model(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        embedding_model = _parse_embedding_model(d.pop("embedding_model", UNSET))

        def _parse_embedding_model_provider(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        embedding_model_provider = _parse_embedding_model_provider(d.pop("embedding_model_provider", UNSET))

        def _parse_embedding_available(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        embedding_available = _parse_embedding_available(d.pop("embedding_available", UNSET))

        dataset = cls(
            id=id,
            name=name,
            description=description,
            provider=provider,
            permission=permission,
            data_source_type=data_source_type,
            indexing_technique=indexing_technique,
            app_count=app_count,
            document_count=document_count,
            word_count=word_count,
            created_by=created_by,
            created_at=created_at,
            updated_by=updated_by,
            updated_at=updated_at,
            embedding_model=embedding_model,
            embedding_model_provider=embedding_model_provider,
            embedding_available=embedding_available,
        )

        dataset.additional_properties = d
        return dataset

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
