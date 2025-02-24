from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_segments_response_200 import GetSegmentsResponse200
from ...models.get_segments_status import GetSegmentsStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dataset_id: str,
    document_id: str,
    *,
    keyword: Union[Unset, str] = UNSET,
    status: Union[Unset, GetSegmentsStatus] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["keyword"] = keyword

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasets/{dataset_id}/documents/{document_id}/segments".format(
            dataset_id=dataset_id,
            document_id=document_id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetSegmentsResponse200]]:
    if response.status_code == 200:
        response_200 = GetSegmentsResponse200.from_dict(response.json())

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
) -> Response[Union[Any, GetSegmentsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataset_id: str,
    document_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    keyword: Union[Unset, str] = UNSET,
    status: Union[Unset, GetSegmentsStatus] = UNSET,
) -> Response[Union[Any, GetSegmentsResponse200]]:
    """查询文档分段

     获取指定文档的所有分段

    Args:
        dataset_id (str):
        document_id (str):
        keyword (Union[Unset, str]):
        status (Union[Unset, GetSegmentsStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetSegmentsResponse200]]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        document_id=document_id,
        keyword=keyword,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_id: str,
    document_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    keyword: Union[Unset, str] = UNSET,
    status: Union[Unset, GetSegmentsStatus] = UNSET,
) -> Optional[Union[Any, GetSegmentsResponse200]]:
    """查询文档分段

     获取指定文档的所有分段

    Args:
        dataset_id (str):
        document_id (str):
        keyword (Union[Unset, str]):
        status (Union[Unset, GetSegmentsStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetSegmentsResponse200]
    """

    return sync_detailed(
        dataset_id=dataset_id,
        document_id=document_id,
        client=client,
        keyword=keyword,
        status=status,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    document_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    keyword: Union[Unset, str] = UNSET,
    status: Union[Unset, GetSegmentsStatus] = UNSET,
) -> Response[Union[Any, GetSegmentsResponse200]]:
    """查询文档分段

     获取指定文档的所有分段

    Args:
        dataset_id (str):
        document_id (str):
        keyword (Union[Unset, str]):
        status (Union[Unset, GetSegmentsStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetSegmentsResponse200]]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        document_id=document_id,
        keyword=keyword,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    document_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    keyword: Union[Unset, str] = UNSET,
    status: Union[Unset, GetSegmentsStatus] = UNSET,
) -> Optional[Union[Any, GetSegmentsResponse200]]:
    """查询文档分段

     获取指定文档的所有分段

    Args:
        dataset_id (str):
        document_id (str):
        keyword (Union[Unset, str]):
        status (Union[Unset, GetSegmentsStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetSegmentsResponse200]
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            document_id=document_id,
            client=client,
            keyword=keyword,
            status=status,
        )
    ).parsed
