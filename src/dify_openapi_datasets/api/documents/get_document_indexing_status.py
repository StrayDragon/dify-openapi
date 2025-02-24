from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_document_indexing_status_response_200 import GetDocumentIndexingStatusResponse200
from ...types import Response


def _get_kwargs(
    dataset_id: str,
    batch: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasets/{dataset_id}/documents/{batch}/indexing-status".format(
            dataset_id=dataset_id,
            batch=batch,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetDocumentIndexingStatusResponse200]]:
    if response.status_code == 200:
        response_200 = GetDocumentIndexingStatusResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GetDocumentIndexingStatusResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataset_id: str,
    batch: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, GetDocumentIndexingStatusResponse200]]:
    """获取文档嵌入状态

     获取文档处理和索引的进度状态

    Args:
        dataset_id (str):
        batch (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetDocumentIndexingStatusResponse200]]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        batch=batch,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_id: str,
    batch: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, GetDocumentIndexingStatusResponse200]]:
    """获取文档嵌入状态

     获取文档处理和索引的进度状态

    Args:
        dataset_id (str):
        batch (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetDocumentIndexingStatusResponse200]
    """

    return sync_detailed(
        dataset_id=dataset_id,
        batch=batch,
        client=client,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    batch: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, GetDocumentIndexingStatusResponse200]]:
    """获取文档嵌入状态

     获取文档处理和索引的进度状态

    Args:
        dataset_id (str):
        batch (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetDocumentIndexingStatusResponse200]]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        batch=batch,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    batch: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, GetDocumentIndexingStatusResponse200]]:
    """获取文档嵌入状态

     获取文档处理和索引的进度状态

    Args:
        dataset_id (str):
        batch (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetDocumentIndexingStatusResponse200]
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            batch=batch,
            client=client,
        )
    ).parsed
