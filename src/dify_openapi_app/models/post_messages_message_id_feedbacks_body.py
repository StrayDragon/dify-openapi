from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_messages_message_id_feedbacks_body_rating_type_1 import (
    PostMessagesMessageIdFeedbacksBodyRatingType1,
    check_post_messages_message_id_feedbacks_body_rating_type_1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostMessagesMessageIdFeedbacksBody")


@_attrs_define
class PostMessagesMessageIdFeedbacksBody:
    """
    Attributes:
        rating (Union[None, PostMessagesMessageIdFeedbacksBodyRatingType1]): 反馈类型
        user (str): 用户标识
        content (Union[Unset, str]): 反馈内容
    """

    rating: Union[None, PostMessagesMessageIdFeedbacksBodyRatingType1]
    user: str
    content: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rating: Union[None, str]
        if isinstance(self.rating, str):
            rating = self.rating
        else:
            rating = self.rating

        user = self.user

        content = self.content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rating": rating,
                "user": user,
            }
        )
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_rating(data: object) -> Union[None, PostMessagesMessageIdFeedbacksBodyRatingType1]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                rating_type_1 = check_post_messages_message_id_feedbacks_body_rating_type_1(data)

                return rating_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, PostMessagesMessageIdFeedbacksBodyRatingType1], data)

        rating = _parse_rating(d.pop("rating"))

        user = d.pop("user")

        content = d.pop("content", UNSET)

        post_messages_message_id_feedbacks_body = cls(
            rating=rating,
            user=user,
            content=content,
        )

        post_messages_message_id_feedbacks_body.additional_properties = d
        return post_messages_message_id_feedbacks_body

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
