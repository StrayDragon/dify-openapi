from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.post_files_upload_body import PostFilesUploadBody
from ...models.uploaded_file import UploadedFile
from ...types import Response


def _get_kwargs(
    *,
    body: PostFilesUploadBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/files/upload",
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Error, UploadedFile]]:
    if response.status_code == 200:
        response_200 = UploadedFile.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 413:
        response_413 = Error.from_dict(response.json())

        return response_413
    if response.status_code == 415:
        response_415 = Error.from_dict(response.json())

        return response_415
    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Error, UploadedFile]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostFilesUploadBody,
) -> Response[Union[Any, Error, UploadedFile]]:
    """上传文件

     上传文件并在发送消息时使用。
    支持的文件类型取决于应用类型和配置。
    上传的文件仅供当前终端用户使用。

    Args:
        body (PostFilesUploadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, UploadedFile]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostFilesUploadBody,
) -> Optional[Union[Any, Error, UploadedFile]]:
    """上传文件

     上传文件并在发送消息时使用。
    支持的文件类型取决于应用类型和配置。
    上传的文件仅供当前终端用户使用。

    Args:
        body (PostFilesUploadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error, UploadedFile]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostFilesUploadBody,
) -> Response[Union[Any, Error, UploadedFile]]:
    """上传文件

     上传文件并在发送消息时使用。
    支持的文件类型取决于应用类型和配置。
    上传的文件仅供当前终端用户使用。

    Args:
        body (PostFilesUploadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Error, UploadedFile]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostFilesUploadBody,
) -> Optional[Union[Any, Error, UploadedFile]]:
    """上传文件

     上传文件并在发送消息时使用。
    支持的文件类型取决于应用类型和配置。
    上传的文件仅供当前终端用户使用。

    Args:
        body (PostFilesUploadBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Error, UploadedFile]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
