from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentMetadata")


@_attrs_define
class DocumentMetadata:
    """文档元数据，根据文档类型有不同的字段要求

    Attributes:
        title (Union[Unset, str]): 标题
        language (Union[Unset, str]): 语言
        author (Union[Unset, str]): 作者
        publisher (Union[Unset, str]): 出版商/发布者
        publication_date (Union[Unset, str]): 发布日期
        isbn (Union[Unset, str]): ISBN号码（图书类型专用）
        category (Union[Unset, str]): 分类
        url (Union[Unset, str]): URL地址（网页类型专用）
        topic (Union[Unset, str]): 主题
        keywords (Union[Unset, list[str]]): 关键词
        description (Union[Unset, str]): 描述信息
    """

    title: Union[Unset, str] = UNSET
    language: Union[Unset, str] = UNSET
    author: Union[Unset, str] = UNSET
    publisher: Union[Unset, str] = UNSET
    publication_date: Union[Unset, str] = UNSET
    isbn: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    topic: Union[Unset, str] = UNSET
    keywords: Union[Unset, list[str]] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        language = self.language

        author = self.author

        publisher = self.publisher

        publication_date = self.publication_date

        isbn = self.isbn

        category = self.category

        url = self.url

        topic = self.topic

        keywords: Union[Unset, list[str]] = UNSET
        if not isinstance(self.keywords, Unset):
            keywords = self.keywords

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if language is not UNSET:
            field_dict["language"] = language
        if author is not UNSET:
            field_dict["author"] = author
        if publisher is not UNSET:
            field_dict["publisher"] = publisher
        if publication_date is not UNSET:
            field_dict["publication_date"] = publication_date
        if isbn is not UNSET:
            field_dict["isbn"] = isbn
        if category is not UNSET:
            field_dict["category"] = category
        if url is not UNSET:
            field_dict["url"] = url
        if topic is not UNSET:
            field_dict["topic"] = topic
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        language = d.pop("language", UNSET)

        author = d.pop("author", UNSET)

        publisher = d.pop("publisher", UNSET)

        publication_date = d.pop("publication_date", UNSET)

        isbn = d.pop("isbn", UNSET)

        category = d.pop("category", UNSET)

        url = d.pop("url", UNSET)

        topic = d.pop("topic", UNSET)

        keywords = cast(list[str], d.pop("keywords", UNSET))

        description = d.pop("description", UNSET)

        document_metadata = cls(
            title=title,
            language=language,
            author=author,
            publisher=publisher,
            publication_date=publication_date,
            isbn=isbn,
            category=category,
            url=url,
            topic=topic,
            keywords=keywords,
            description=description,
        )

        document_metadata.additional_properties = d
        return document_metadata

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
