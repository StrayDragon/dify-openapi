from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_conversations_response_200 import GetConversationsResponse200
from ...models.get_conversations_sort_by import GetConversationsSortBy
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user: str,
    last_id: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
    sort_by: Union[Unset, GetConversationsSortBy] = "-updated_at",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["user"] = user

    params["last_id"] = last_id

    params["limit"] = limit

    json_sort_by: Union[Unset, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by

    params["sort_by"] = json_sort_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/conversations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetConversationsResponse200]:
    if response.status_code == 200:
        response_200 = GetConversationsResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetConversationsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    user: str,
    last_id: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
    sort_by: Union[Unset, GetConversationsSortBy] = "-updated_at",
) -> Response[GetConversationsResponse200]:
    """获取会话列表

     获取当前用户的会话列表

    Args:
        user (str):
        last_id (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 20.
        sort_by (Union[Unset, GetConversationsSortBy]):  Default: '-updated_at'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetConversationsResponse200]
    """

    kwargs = _get_kwargs(
        user=user,
        last_id=last_id,
        limit=limit,
        sort_by=sort_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    user: str,
    last_id: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
    sort_by: Union[Unset, GetConversationsSortBy] = "-updated_at",
) -> Optional[GetConversationsResponse200]:
    """获取会话列表

     获取当前用户的会话列表

    Args:
        user (str):
        last_id (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 20.
        sort_by (Union[Unset, GetConversationsSortBy]):  Default: '-updated_at'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetConversationsResponse200
    """

    return sync_detailed(
        client=client,
        user=user,
        last_id=last_id,
        limit=limit,
        sort_by=sort_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    user: str,
    last_id: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
    sort_by: Union[Unset, GetConversationsSortBy] = "-updated_at",
) -> Response[GetConversationsResponse200]:
    """获取会话列表

     获取当前用户的会话列表

    Args:
        user (str):
        last_id (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 20.
        sort_by (Union[Unset, GetConversationsSortBy]):  Default: '-updated_at'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetConversationsResponse200]
    """

    kwargs = _get_kwargs(
        user=user,
        last_id=last_id,
        limit=limit,
        sort_by=sort_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    user: str,
    last_id: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
    sort_by: Union[Unset, GetConversationsSortBy] = "-updated_at",
) -> Optional[GetConversationsResponse200]:
    """获取会话列表

     获取当前用户的会话列表

    Args:
        user (str):
        last_id (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 20.
        sort_by (Union[Unset, GetConversationsSortBy]):  Default: '-updated_at'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetConversationsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            user=user,
            last_id=last_id,
            limit=limit,
            sort_by=sort_by,
        )
    ).parsed
