from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RetrieverResource")


@_attrs_define
class RetrieverResource:
    """
    Attributes:
        position (Union[Unset, int]): 位置
        dataset_id (Union[Unset, str]): 数据集ID
        dataset_name (Union[Unset, str]): 数据集名称
        document_id (Union[Unset, str]): 文档ID
        document_name (Union[Unset, str]): 文档名称
        segment_id (Union[Unset, str]): 分段ID
        score (Union[Unset, float]): 相关度分数
        content (Union[Unset, str]): 内容
    """

    position: Union[Unset, int] = UNSET
    dataset_id: Union[Unset, str] = UNSET
    dataset_name: Union[Unset, str] = UNSET
    document_id: Union[Unset, str] = UNSET
    document_name: Union[Unset, str] = UNSET
    segment_id: Union[Unset, str] = UNSET
    score: Union[Unset, float] = UNSET
    content: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position = self.position

        dataset_id = self.dataset_id

        dataset_name = self.dataset_name

        document_id = self.document_id

        document_name = self.document_name

        segment_id = self.segment_id

        score = self.score

        content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if position is not UNSET:
            field_dict["position"] = position
        if dataset_id is not UNSET:
            field_dict["dataset_id"] = dataset_id
        if dataset_name is not UNSET:
            field_dict["dataset_name"] = dataset_name
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
        if document_name is not UNSET:
            field_dict["document_name"] = document_name
        if segment_id is not UNSET:
            field_dict["segment_id"] = segment_id
        if score is not UNSET:
            field_dict["score"] = score
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        position = d.pop("position", UNSET)

        dataset_id = d.pop("dataset_id", UNSET)

        dataset_name = d.pop("dataset_name", UNSET)

        document_id = d.pop("document_id", UNSET)

        document_name = d.pop("document_name", UNSET)

        segment_id = d.pop("segment_id", UNSET)

        score = d.pop("score", UNSET)

        content = d.pop("content", UNSET)

        retriever_resource = cls(
            position=position,
            dataset_id=dataset_id,
            dataset_name=dataset_name,
            document_id=document_id,
            document_name=document_name,
            segment_id=segment_id,
            score=score,
            content=content,
        )

        retriever_resource.additional_properties = d
        return retriever_resource

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
