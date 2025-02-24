from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_conversations_conversation_id_body import DeleteConversationsConversationIdBody
from ...models.delete_conversations_conversation_id_response_200 import DeleteConversationsConversationIdResponse200
from ...types import Response


def _get_kwargs(
    conversation_id: str,
    *,
    body: DeleteConversationsConversationIdBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/conversations/{conversation_id}".format(
            conversation_id=conversation_id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DeleteConversationsConversationIdResponse200]:
    if response.status_code == 200:
        response_200 = DeleteConversationsConversationIdResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DeleteConversationsConversationIdResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    conversation_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DeleteConversationsConversationIdBody,
) -> Response[DeleteConversationsConversationIdResponse200]:
    """删除会话

    Args:
        conversation_id (str):
        body (DeleteConversationsConversationIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteConversationsConversationIdResponse200]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    conversation_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DeleteConversationsConversationIdBody,
) -> Optional[DeleteConversationsConversationIdResponse200]:
    """删除会话

    Args:
        conversation_id (str):
        body (DeleteConversationsConversationIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteConversationsConversationIdResponse200
    """

    return sync_detailed(
        conversation_id=conversation_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    conversation_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DeleteConversationsConversationIdBody,
) -> Response[DeleteConversationsConversationIdResponse200]:
    """删除会话

    Args:
        conversation_id (str):
        body (DeleteConversationsConversationIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteConversationsConversationIdResponse200]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    conversation_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DeleteConversationsConversationIdBody,
) -> Optional[DeleteConversationsConversationIdResponse200]:
    """删除会话

    Args:
        conversation_id (str):
        body (DeleteConversationsConversationIdBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteConversationsConversationIdResponse200
    """

    return (
        await asyncio_detailed(
            conversation_id=conversation_id,
            client=client,
            body=body,
        )
    ).parsed
