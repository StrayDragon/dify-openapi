from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.upload_file import UploadFile
from ...types import Response


def _get_kwargs(
    dataset_id: str,
    document_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/datasets/{dataset_id}/documents/{document_id}/upload-file".format(
            dataset_id=dataset_id,
            document_id=document_id,
        ),
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UploadFile]]:
    if response.status_code == 200:
        response_200 = UploadFile.from_dict(response.json())

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
) -> Response[Union[Any, UploadFile]]:
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
) -> Response[Union[Any, UploadFile]]:
    """获取上传文件

     获取指定文档的上传文件信息

    Args:
        dataset_id (str):
        document_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UploadFile]]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        document_id=document_id,
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
) -> Optional[Union[Any, UploadFile]]:
    """获取上传文件

     获取指定文档的上传文件信息

    Args:
        dataset_id (str):
        document_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UploadFile]
    """

    return sync_detailed(
        dataset_id=dataset_id,
        document_id=document_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    document_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, UploadFile]]:
    """获取上传文件

     获取指定文档的上传文件信息

    Args:
        dataset_id (str):
        document_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UploadFile]]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        document_id=document_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    document_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, UploadFile]]:
    """获取上传文件

     获取指定文档的上传文件信息

    Args:
        dataset_id (str):
        document_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UploadFile]
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            document_id=document_id,
            client=client,
        )
    ).parsed
