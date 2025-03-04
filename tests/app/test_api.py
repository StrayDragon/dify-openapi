import pytest
from pathlib import Path
from typing import Any, Optional

from dify_sdk.client import AsyncDifyApi
from dify_sdk.types import (
    PostCompletionMessagesRequestInputs,
    FileInput,
)

LOGIN_USER_ID = "test123"


async def test_get_app_info(app_chat_client: AsyncDifyApi):
    """测试获取应用信息"""
    response = await app_chat_client.get_application_basic_information()
    assert response.name is not None and len(response.name) > 0
    assert response.description is not None
    assert isinstance(response.tags, list)

    for tag in response.tags:
        assert isinstance(tag, str)


async def test_get_app_info_error_handling(app_chat_client: AsyncDifyApi):
    """测试获取应用信息时错误处理"""
    original_host = app_chat_client._client_wrapper._base_url  # type: ignore
    app_chat_client._client_wrapper._base_url = "https://invalid.example.com"  # type: ignore

    with pytest.raises(Exception):
        await app_chat_client.get_application_basic_information()

    app_chat_client._client_wrapper._base_url = original_host  # type: ignore


async def test_chat_messages(app_chat_client: AsyncDifyApi) -> Optional[str]:
    """测试对话消息接口"""
    response = await app_chat_client.send_chat_message_conversational_app(
        query="ping",
        response_mode="blocking",
        user=LOGIN_USER_ID,
        inputs=None,
    )
    assert response is not None
    assert response.message_id is not None
    return response.message_id


async def test_message_feedback(app_chat_client: AsyncDifyApi):
    """测试消息反馈接口"""
    message_id = await test_chat_messages(app_chat_client)
    assert message_id is not None

    response = await app_chat_client.message_feedback(
        message_id=message_id,
        rating="like",
        user=LOGIN_USER_ID,
    )
    assert response is not None
    assert response.result == "success"


async def test_conversation_management(app_chat_client: AsyncDifyApi):
    """测试会话管理相关接口"""
    conversations = await app_chat_client.get_conversation_list(user=LOGIN_USER_ID, sort_by="created_at")
    assert conversations is not None
    assert conversations.data is not None

    if conversations.data and len(conversations.data) > 0:
        conversation = conversations.data[0]
        assert conversation.id is not None
        conversation_id = str(conversation.id)

        renamed = await app_chat_client.rename_conversation(
            conversation_id=conversation_id,
            user=LOGIN_USER_ID,
            name="dify-openapi 测试会话",
        )
        assert renamed is not None
        assert renamed.name == "dify-openapi 测试会话"
        if renamed.id is None:
            pytest.skip("无法获取重命名后的会话ID")
        conversation_id = str(renamed.id)

        messages = await app_chat_client.get_conversation_history_messages(
            conversation_id=conversation_id,
            user=LOGIN_USER_ID,
        )
        assert messages is not None
        assert messages.data is not None

        delete_response = await app_chat_client.delete_conversation(
            conversation_id=conversation_id,
            user=LOGIN_USER_ID,
        )
        assert delete_response is not None
        assert delete_response.result == "success"


async def test_get_parameters(app_chat_client: AsyncDifyApi):
    """测试获取应用参数"""
    response = await app_chat_client.get_application_parameters()
    assert response is not None
    assert response.opening_statement is not None
    assert response.suggested_questions is not None
    assert response.speech_to_text is not None
    assert response.retriever_resource is not None


@pytest.fixture
def test_file_path() -> Path:
    """测试用的文件路径"""
    return Path("tests/data/app/test.txt")


@pytest.fixture
def test_audio_file_path() -> Path:
    """创建测试用的临时音频文件"""
    return Path("tests/data/app/audio.mp3")


async def test_file_upload(app_chat_client: AsyncDifyApi, test_file_path: Path) -> Optional[str]:
    """测试文件上传接口"""
    response = await app_chat_client.upload_file(
        file=("test.txt", test_file_path.read_bytes(), "text/plain"),
        user=LOGIN_USER_ID,
    )
    assert response.id is not None
    return response.id


async def test_chat_with_suggested_questions(app_chat_client: AsyncDifyApi):
    """测试对话并获取下一轮建议问题"""
    # 1. 发送对话消息
    chat_response = await app_chat_client.send_chat_message_conversational_app(
        query="dify-openapi 测试问题",
        response_mode="blocking",
        user=LOGIN_USER_ID,
        inputs=None,
    )
    assert chat_response is not None

    # 2. 获取应用参数，检查是否启用了建议问题功能
    params = await app_chat_client.get_application_parameters()
    if params.suggested_questions_after_answer and params.suggested_questions_after_answer.enabled:
        # 如果启用了建议问题功能，应该在chat_response中包含建议问题
        response_dict = chat_response.model_dump()
        if "suggested_questions" in response_dict:
            suggested_questions: list[str] = response_dict["suggested_questions"]
            assert isinstance(suggested_questions, list)
            for question in suggested_questions:
                assert isinstance(question, str)


async def test_chat_with_file(app_chat_client: AsyncDifyApi, test_file_path: Path):
    """测试带文件的对话"""
    # 1. 先上传文件
    file_id = await test_file_upload(app_chat_client, test_file_path)

    # 2. 发送带文件的对话消息
    file_input = FileInput(
        type="document",
        transfer_method="local_file",
        upload_file_id=file_id,
    )

    response = await app_chat_client.send_chat_message_conversational_app(
        query="dify-openapi 测试问题 - 请分析上传的文件",
        response_mode="blocking",
        user=LOGIN_USER_ID,
        files=[file_input],
        inputs=None,
    )
    assert response is not None
    assert hasattr(response, "message_id")


async def test_audio_to_text(app_chat_client: AsyncDifyApi, test_audio_file_path: Path):
    """测试语音转文字接口"""
    response = await app_chat_client.audio_to_text(
        file=("test.mp3", test_audio_file_path.read_bytes(), "audio/mp3"),
        user=LOGIN_USER_ID,
    )
    assert response is not None
    assert hasattr(response, "text")
    assert response.text is not None
    assert response.text != ""


async def test_text_to_audio(app_chat_client: AsyncDifyApi):
    """测试文字转语音接口"""
    audio_chunks: list[bytes] = []
    audio_stream = app_chat_client.text_to_audio(
        text="Hi",
        user=LOGIN_USER_ID,
    )
    async for chunk in audio_stream:
        audio_chunks.append(chunk)

    assert len(audio_chunks) > 0
    for chunk in audio_chunks:
        assert isinstance(chunk, bytes)


async def test_completion_message(app_completion_client: AsyncDifyApi):
    """测试文本生成接口"""
    response = await app_completion_client.send_message_text_generation_app(
        inputs=PostCompletionMessagesRequestInputs(query="ping"),
        response_mode="blocking",
        user=LOGIN_USER_ID,
    )

    assert response is not None
    assert response.message_id is not None


async def test_workflow_run(app_workflow_client: AsyncDifyApi):
    """Test workflow execution API"""
    workflow_inputs: dict[str, Any] = {
        "query": "ping",
        "inputs": {},
        "files": [],
    }

    response = await app_workflow_client.run_workflow_workflow_app(
        inputs=workflow_inputs,
        response_mode="blocking",
        user=LOGIN_USER_ID,
    )
    assert response is not None
    assert response.workflow_run_id is not None
    assert response.task_id is not None
    assert response.data is not None
    assert response.data.id is not None
    assert response.data.workflow_id is not None
    assert response.data.status in ["running", "succeeded", "failed", "stopped"]
