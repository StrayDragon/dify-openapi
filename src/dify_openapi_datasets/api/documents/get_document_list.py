from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_document_list_response_200 import GetDocumentListResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dataset_id: str,
    *,
    keyword: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasets/{dataset_id}/documents".format(
            dataset_id=dataset_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetDocumentListResponse200]]:
    if response.status_code == 200:
        response_200 = GetDocumentListResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetDocumentListResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataset_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    keyword: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
) -> Response[Union[Any, GetDocumentListResponse200]]:
    """获取知识库文档列表

     获取指定知识库下的所有文档列表

    Args:
        dataset_id (str):
        keyword (Union[Unset, str]):
        page (Union[Unset, int]):  Default: 1.
        limit (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetDocumentListResponse200]]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        keyword=keyword,
        page=page,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    keyword: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
) -> Optional[Union[Any, GetDocumentListResponse200]]:
    """获取知识库文档列表

     获取指定知识库下的所有文档列表

    Args:
        dataset_id (str):
        keyword (Union[Unset, str]):
        page (Union[Unset, int]):  Default: 1.
        limit (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetDocumentListResponse200]
    """

    return sync_detailed(
        dataset_id=dataset_id,
        client=client,
        keyword=keyword,
        page=page,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    keyword: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
) -> Response[Union[Any, GetDocumentListResponse200]]:
    """获取知识库文档列表

     获取指定知识库下的所有文档列表

    Args:
        dataset_id (str):
        keyword (Union[Unset, str]):
        page (Union[Unset, int]):  Default: 1.
        limit (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetDocumentListResponse200]]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        keyword=keyword,
        page=page,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    keyword: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = 1,
    limit: Union[Unset, int] = 20,
) -> Optional[Union[Any, GetDocumentListResponse200]]:
    """获取知识库文档列表

     获取指定知识库下的所有文档列表

    Args:
        dataset_id (str):
        keyword (Union[Unset, str]):
        page (Union[Unset, int]):  Default: 1.
        limit (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetDocumentListResponse200]
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            client=client,
            keyword=keyword,
            page=page,
            limit=limit,
        )
    ).parsed
