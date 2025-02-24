from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.retrieve_dataset_body_external_retrieval_model import RetrieveDatasetBodyExternalRetrievalModel
    from ..models.retrieve_dataset_body_retrieval_model import RetrieveDatasetBodyRetrievalModel


T = TypeVar("T", bound="RetrieveDatasetBody")


@_attrs_define
class RetrieveDatasetBody:
    """
    Attributes:
        query (str): 检索关键词
        retrieval_model (Union[Unset, RetrieveDatasetBodyRetrievalModel]): 检索参数配置
        external_retrieval_model (Union[Unset, RetrieveDatasetBodyExternalRetrievalModel]): 未启用字段
    """

    query: str
    retrieval_model: Union[Unset, "RetrieveDatasetBodyRetrievalModel"] = UNSET
    external_retrieval_model: Union[Unset, "RetrieveDatasetBodyExternalRetrievalModel"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        retrieval_model: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.retrieval_model, Unset):
            retrieval_model = self.retrieval_model.to_dict()

        external_retrieval_model: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.external_retrieval_model, Unset):
            external_retrieval_model = self.external_retrieval_model.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if retrieval_model is not UNSET:
            field_dict["retrieval_model"] = retrieval_model
        if external_retrieval_model is not UNSET:
            field_dict["external_retrieval_model"] = external_retrieval_model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.retrieve_dataset_body_external_retrieval_model import RetrieveDatasetBodyExternalRetrievalModel
        from ..models.retrieve_dataset_body_retrieval_model import RetrieveDatasetBodyRetrievalModel

        d = src_dict.copy()
        query = d.pop("query")

        _retrieval_model = d.pop("retrieval_model", UNSET)
        retrieval_model: Union[Unset, RetrieveDatasetBodyRetrievalModel]
        if isinstance(_retrieval_model, Unset):
            retrieval_model = UNSET
        else:
            retrieval_model = RetrieveDatasetBodyRetrievalModel.from_dict(_retrieval_model)

        _external_retrieval_model = d.pop("external_retrieval_model", UNSET)
        external_retrieval_model: Union[Unset, RetrieveDatasetBodyExternalRetrievalModel]
        if isinstance(_external_retrieval_model, Unset):
            external_retrieval_model = UNSET
        else:
            external_retrieval_model = RetrieveDatasetBodyExternalRetrievalModel.from_dict(_external_retrieval_model)

        retrieve_dataset_body = cls(
            query=query,
            retrieval_model=retrieval_model,
            external_retrieval_model=external_retrieval_model,
        )

        retrieve_dataset_body.additional_properties = d
        return retrieve_dataset_body

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
