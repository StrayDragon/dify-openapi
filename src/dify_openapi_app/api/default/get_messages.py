from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_messages_response_200 import GetMessagesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    conversation_id: str,
    user: str,
    first_id: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["conversation_id"] = conversation_id

    params["user"] = user

    params["first_id"] = first_id

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/messages",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetMessagesResponse200]:
    if response.status_code == 200:
        response_200 = GetMessagesResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetMessagesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    conversation_id: str,
    user: str,
    first_id: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
) -> Response[GetMessagesResponse200]:
    """获取会话历史消息

    Args:
        conversation_id (str):
        user (str):
        first_id (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMessagesResponse200]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        user=user,
        first_id=first_id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    conversation_id: str,
    user: str,
    first_id: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
) -> Optional[GetMessagesResponse200]:
    """获取会话历史消息

    Args:
        conversation_id (str):
        user (str):
        first_id (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMessagesResponse200
    """

    return sync_detailed(
        client=client,
        conversation_id=conversation_id,
        user=user,
        first_id=first_id,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    conversation_id: str,
    user: str,
    first_id: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
) -> Response[GetMessagesResponse200]:
    """获取会话历史消息

    Args:
        conversation_id (str):
        user (str):
        first_id (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetMessagesResponse200]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        user=user,
        first_id=first_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    conversation_id: str,
    user: str,
    first_id: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
) -> Optional[GetMessagesResponse200]:
    """获取会话历史消息

    Args:
        conversation_id (str):
        user (str):
        first_id (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetMessagesResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            conversation_id=conversation_id,
            user=user,
            first_id=first_id,
            limit=limit,
        )
    ).parsed
