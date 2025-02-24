from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_messages_message_id_feedbacks_body import PostMessagesMessageIdFeedbacksBody
from ...models.post_messages_message_id_feedbacks_response_200 import PostMessagesMessageIdFeedbacksResponse200
from ...types import Response


def _get_kwargs(
    message_id: str,
    *,
    body: PostMessagesMessageIdFeedbacksBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/messages/{message_id}/feedbacks".format(
            message_id=message_id,
        ),
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PostMessagesMessageIdFeedbacksResponse200]:
    if response.status_code == 200:
        response_200 = PostMessagesMessageIdFeedbacksResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PostMessagesMessageIdFeedbacksResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    message_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostMessagesMessageIdFeedbacksBody,
) -> Response[PostMessagesMessageIdFeedbacksResponse200]:
    """消息反馈

    Args:
        message_id (str):
        body (PostMessagesMessageIdFeedbacksBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostMessagesMessageIdFeedbacksResponse200]
    """

    kwargs = _get_kwargs(
        message_id=message_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    message_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostMessagesMessageIdFeedbacksBody,
) -> Optional[PostMessagesMessageIdFeedbacksResponse200]:
    """消息反馈

    Args:
        message_id (str):
        body (PostMessagesMessageIdFeedbacksBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostMessagesMessageIdFeedbacksResponse200
    """

    return sync_detailed(
        message_id=message_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    message_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostMessagesMessageIdFeedbacksBody,
) -> Response[PostMessagesMessageIdFeedbacksResponse200]:
    """消息反馈

    Args:
        message_id (str):
        body (PostMessagesMessageIdFeedbacksBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostMessagesMessageIdFeedbacksResponse200]
    """

    kwargs = _get_kwargs(
        message_id=message_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    message_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PostMessagesMessageIdFeedbacksBody,
) -> Optional[PostMessagesMessageIdFeedbacksResponse200]:
    """消息反馈

    Args:
        message_id (str):
        body (PostMessagesMessageIdFeedbacksBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostMessagesMessageIdFeedbacksResponse200
    """

    return (
        await asyncio_detailed(
            message_id=message_id,
            client=client,
            body=body,
        )
    ).parsed
