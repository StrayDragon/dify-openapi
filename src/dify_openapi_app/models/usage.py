from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Usage")


@_attrs_define
class Usage:
    """
    Attributes:
        prompt_tokens (Union[Unset, int]): 提示词使用的 token 数量
        completion_tokens (Union[Unset, int]): 补全使用的 token 数量
        total_tokens (Union[Unset, int]): 总共使用的 token 数量
        prompt_unit_price (Union[Unset, str]): 提示词单价
        prompt_price_unit (Union[Unset, str]): 提示词价格单位
        prompt_price (Union[Unset, str]): 提示词总价
        completion_unit_price (Union[Unset, str]): 补全单价
        completion_price_unit (Union[Unset, str]): 补全价格单位
        completion_price (Union[Unset, str]): 补全总价
        total_price (Union[Unset, str]): 总价格
        currency (Union[Unset, str]): 货币单位
        latency (Union[Unset, float]): 延迟时间
    """

    prompt_tokens: Union[Unset, int] = UNSET
    completion_tokens: Union[Unset, int] = UNSET
    total_tokens: Union[Unset, int] = UNSET
    prompt_unit_price: Union[Unset, str] = UNSET
    prompt_price_unit: Union[Unset, str] = UNSET
    prompt_price: Union[Unset, str] = UNSET
    completion_unit_price: Union[Unset, str] = UNSET
    completion_price_unit: Union[Unset, str] = UNSET
    completion_price: Union[Unset, str] = UNSET
    total_price: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    latency: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prompt_tokens = self.prompt_tokens

        completion_tokens = self.completion_tokens

        total_tokens = self.total_tokens

        prompt_unit_price = self.prompt_unit_price

        prompt_price_unit = self.prompt_price_unit

        prompt_price = self.prompt_price

        completion_unit_price = self.completion_unit_price

        completion_price_unit = self.completion_price_unit

        completion_price = self.completion_price

        total_price = self.total_price

        currency = self.currency

        latency = self.latency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if prompt_tokens is not UNSET:
            field_dict["prompt_tokens"] = prompt_tokens
        if completion_tokens is not UNSET:
            field_dict["completion_tokens"] = completion_tokens
        if total_tokens is not UNSET:
            field_dict["total_tokens"] = total_tokens
        if prompt_unit_price is not UNSET:
            field_dict["prompt_unit_price"] = prompt_unit_price
        if prompt_price_unit is not UNSET:
            field_dict["prompt_price_unit"] = prompt_price_unit
        if prompt_price is not UNSET:
            field_dict["prompt_price"] = prompt_price
        if completion_unit_price is not UNSET:
            field_dict["completion_unit_price"] = completion_unit_price
        if completion_price_unit is not UNSET:
            field_dict["completion_price_unit"] = completion_price_unit
        if completion_price is not UNSET:
            field_dict["completion_price"] = completion_price
        if total_price is not UNSET:
            field_dict["total_price"] = total_price
        if currency is not UNSET:
            field_dict["currency"] = currency
        if latency is not UNSET:
            field_dict["latency"] = latency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        prompt_tokens = d.pop("prompt_tokens", UNSET)

        completion_tokens = d.pop("completion_tokens", UNSET)

        total_tokens = d.pop("total_tokens", UNSET)

        prompt_unit_price = d.pop("prompt_unit_price", UNSET)

        prompt_price_unit = d.pop("prompt_price_unit", UNSET)

        prompt_price = d.pop("prompt_price", UNSET)

        completion_unit_price = d.pop("completion_unit_price", UNSET)

        completion_price_unit = d.pop("completion_price_unit", UNSET)

        completion_price = d.pop("completion_price", UNSET)

        total_price = d.pop("total_price", UNSET)

        currency = d.pop("currency", UNSET)

        latency = d.pop("latency", UNSET)

        usage = cls(
            prompt_tokens=prompt_tokens,
            completion_tokens=completion_tokens,
            total_tokens=total_tokens,
            prompt_unit_price=prompt_unit_price,
            prompt_price_unit=prompt_price_unit,
            prompt_price=prompt_price,
            completion_unit_price=completion_unit_price,
            completion_price_unit=completion_price_unit,
            completion_price=completion_price,
            total_price=total_price,
            currency=currency,
            latency=latency,
        )

        usage.additional_properties = d
        return usage

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
