import dataclasses
import os
import typing
import importlib.metadata
from packaging.version import Version

from dify_sdk.knowledge_base.datasets.client import AsyncDatasetsClient
from dify_sdk.knowledge_base.documents.client import AsyncDocumentsClient
from dify_sdk.knowledge_base.metadata.client import AsyncMetadataClient
from dify_sdk.knowledge_base.models.client import AsyncModelsClient
from dify_sdk.knowledge_base.segments.client import AsyncSegmentsClient
from dify_sdk.chat.types.chunk_chat_completion_response import ChunkChatCompletionResponse as ChatChunkResponse
from dify_sdk.advanced_chat.types.chunk_chat_completion_response import (
    ChunkChatCompletionResponse as AdvancedChatChunkResponse,
)
from dify_sdk.generation.types.chunk_chat_completion_response import (
    ChunkChatCompletionResponse as GenerationChunkResponse,
)


PROJECT_NAME = "dify-openapi"
PROJECT_VERSION = importlib.metadata.version(PROJECT_NAME)


def postpone_run_in_this_version(target_version: str) -> bool:
    if not need_skip_run_until_this_version(target_version):
        raise Exception("This version need run this logic or remove this check!")
    return False

def need_skip_run_until_this_version(target_version: str) -> bool:
    return Version(target_version) > Version(PROJECT_VERSION)


RUNNING_IN_CI = any(
    [
        os.getenv("GITHUB_ACTIONS"),
    ]
)


@dataclasses.dataclass
class KnowledgeBaseClient:
    dataset: AsyncDatasetsClient
    document: AsyncDocumentsClient
    segment: AsyncSegmentsClient
    metadata: AsyncMetadataClient
    models: AsyncModelsClient


def parse_stream_event(
    event_: typing.Any,
    response_type: str = "chat",
) -> typing.Any | None:
    """
    解析流式响应事件，处理空字符串和JSON解析

    Args:
        event_: 流式响应事件（可能是字符串或已解析的对象）
        response_type: 响应类型，可选值: "chat", "advanced_chat", "generation"

    Returns:
        解析后的事件对象，如果是空字符串则返回None
    """
    if isinstance(event_, str):
        # 跳过空字符串
        if not event_.strip():
            return None

        # 根据类型选择对应的响应类
        response_class = {
            "chat": ChatChunkResponse,
            "advanced_chat": AdvancedChatChunkResponse,
            "generation": GenerationChunkResponse,
        }.get(response_type, ChatChunkResponse)

        return response_class.model_validate_json(event_)
    else:
        return event_
