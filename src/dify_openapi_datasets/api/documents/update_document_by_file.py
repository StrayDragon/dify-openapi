from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_document_by_file_body import UpdateDocumentByFileBody
from ...models.update_document_by_file_response_200 import UpdateDocumentByFileResponse200
from ...types import Response


def _get_kwargs(
    dataset_id: str,
    document_id: str,
    *,
    body: UpdateDocumentByFileBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/datasets/{dataset_id}/documents/{document_id}/update-by-file".format(
            dataset_id=dataset_id,
            document_id=document_id,
        ),
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, UpdateDocumentByFileResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateDocumentByFileResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 413:
        response_413 = cast(Any, None)
        return response_413
    if response.status_code == 415:
        response_415 = cast(Any, None)
        return response_415
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, UpdateDocumentByFileResponse200]]:
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
    body: UpdateDocumentByFileBody,
) -> Response[Union[Any, UpdateDocumentByFileResponse200]]:
    """通过文件更新文档

     通过文件更新已存在的文档

    Args:
        dataset_id (str):
        document_id (str):
        body (UpdateDocumentByFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateDocumentByFileResponse200]]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        document_id=document_id,
        body=body,
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
    body: UpdateDocumentByFileBody,
) -> Optional[Union[Any, UpdateDocumentByFileResponse200]]:
    """通过文件更新文档

     通过文件更新已存在的文档

    Args:
        dataset_id (str):
        document_id (str):
        body (UpdateDocumentByFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateDocumentByFileResponse200]
    """

    return sync_detailed(
        dataset_id=dataset_id,
        document_id=document_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    document_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateDocumentByFileBody,
) -> Response[Union[Any, UpdateDocumentByFileResponse200]]:
    """通过文件更新文档

     通过文件更新已存在的文档

    Args:
        dataset_id (str):
        document_id (str):
        body (UpdateDocumentByFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UpdateDocumentByFileResponse200]]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        document_id=document_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    document_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateDocumentByFileBody,
) -> Optional[Union[Any, UpdateDocumentByFileResponse200]]:
    """通过文件更新文档

     通过文件更新已存在的文档

    Args:
        dataset_id (str):
        document_id (str):
        body (UpdateDocumentByFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UpdateDocumentByFileResponse200]
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            document_id=document_id,
            client=client,
            body=body,
        )
    ).parsed
