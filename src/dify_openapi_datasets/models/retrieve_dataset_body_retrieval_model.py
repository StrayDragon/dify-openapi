from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.retrieve_dataset_body_retrieval_model_search_method import (
    RetrieveDatasetBodyRetrievalModelSearchMethod,
    check_retrieve_dataset_body_retrieval_model_search_method,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.retrieve_dataset_body_retrieval_model_reranking_model import (
        RetrieveDatasetBodyRetrievalModelRerankingModel,
    )


T = TypeVar("T", bound="RetrieveDatasetBodyRetrievalModel")


@_attrs_define
class RetrieveDatasetBodyRetrievalModel:
    """检索参数配置

    Attributes:
        search_method (Union[Unset, RetrieveDatasetBodyRetrievalModelSearchMethod]): 检索方法
        reranking_enable (Union[Unset, bool]): 是否启用 Reranking
        reranking_model (Union[Unset, RetrieveDatasetBodyRetrievalModelRerankingModel]):
        weights (Union[Unset, float]): 混合检索模式下语意检索的权重设置
        top_k (Union[Unset, int]): 返回结果数量
        score_threshold_enabled (Union[Unset, bool]): 是否开启 score 阈值
        score_threshold (Union[Unset, float]): Score 阈值
    """

    search_method: Union[Unset, RetrieveDatasetBodyRetrievalModelSearchMethod] = UNSET
    reranking_enable: Union[Unset, bool] = UNSET
    reranking_model: Union[Unset, "RetrieveDatasetBodyRetrievalModelRerankingModel"] = UNSET
    weights: Union[Unset, float] = UNSET
    top_k: Union[Unset, int] = UNSET
    score_threshold_enabled: Union[Unset, bool] = UNSET
    score_threshold: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        search_method: Union[Unset, str] = UNSET
        if not isinstance(self.search_method, Unset):
            search_method = self.search_method

        reranking_enable = self.reranking_enable

        reranking_model: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.reranking_model, Unset):
            reranking_model = self.reranking_model.to_dict()

        weights = self.weights

        top_k = self.top_k

        score_threshold_enabled = self.score_threshold_enabled

        score_threshold = self.score_threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if search_method is not UNSET:
            field_dict["search_method"] = search_method
        if reranking_enable is not UNSET:
            field_dict["reranking_enable"] = reranking_enable
        if reranking_model is not UNSET:
            field_dict["reranking_model"] = reranking_model
        if weights is not UNSET:
            field_dict["weights"] = weights
        if top_k is not UNSET:
            field_dict["top_k"] = top_k
        if score_threshold_enabled is not UNSET:
            field_dict["score_threshold_enabled"] = score_threshold_enabled
        if score_threshold is not UNSET:
            field_dict["score_threshold"] = score_threshold

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.retrieve_dataset_body_retrieval_model_reranking_model import (
            RetrieveDatasetBodyRetrievalModelRerankingModel,
        )

        d = src_dict.copy()
        _search_method = d.pop("search_method", UNSET)
        search_method: Union[Unset, RetrieveDatasetBodyRetrievalModelSearchMethod]
        if isinstance(_search_method, Unset):
            search_method = UNSET
        else:
            search_method = check_retrieve_dataset_body_retrieval_model_search_method(_search_method)

        reranking_enable = d.pop("reranking_enable", UNSET)

        _reranking_model = d.pop("reranking_model", UNSET)
        reranking_model: Union[Unset, RetrieveDatasetBodyRetrievalModelRerankingModel]
        if isinstance(_reranking_model, Unset):
            reranking_model = UNSET
        else:
            reranking_model = RetrieveDatasetBodyRetrievalModelRerankingModel.from_dict(_reranking_model)

        weights = d.pop("weights", UNSET)

        top_k = d.pop("top_k", UNSET)

        score_threshold_enabled = d.pop("score_threshold_enabled", UNSET)

        score_threshold = d.pop("score_threshold", UNSET)

        retrieve_dataset_body_retrieval_model = cls(
            search_method=search_method,
            reranking_enable=reranking_enable,
            reranking_model=reranking_model,
            weights=weights,
            top_k=top_k,
            score_threshold_enabled=score_threshold_enabled,
            score_threshold=score_threshold,
        )

        retrieve_dataset_body_retrieval_model.additional_properties = d
        return retrieve_dataset_body_retrieval_model

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
