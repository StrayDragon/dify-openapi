from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RetrievalModelRerankingModel")


@_attrs_define
class RetrievalModelRerankingModel:
    """Rerank 模型配置，非必填，如果启用了 reranking 则传值

    Attributes:
        reranking_provider_name (Union[Unset, str]): Rerank 模型提供商
        reranking_model_name (Union[Unset, str]): Rerank 模型名称
    """

    reranking_provider_name: Union[Unset, str] = UNSET
    reranking_model_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reranking_provider_name = self.reranking_provider_name

        reranking_model_name = self.reranking_model_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reranking_provider_name is not UNSET:
            field_dict["reranking_provider_name"] = reranking_provider_name
        if reranking_model_name is not UNSET:
            field_dict["reranking_model_name"] = reranking_model_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        reranking_provider_name = d.pop("reranking_provider_name", UNSET)

        reranking_model_name = d.pop("reranking_model_name", UNSET)

        retrieval_model_reranking_model = cls(
            reranking_provider_name=reranking_provider_name,
            reranking_model_name=reranking_model_name,
        )

        retrieval_model_reranking_model.additional_properties = d
        return retrieval_model_reranking_model

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
