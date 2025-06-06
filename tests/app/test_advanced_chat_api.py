import asyncio
import pytest
from pathlib import Path

from dify_sdk.advanced_chat import ChunkChatCompletionResponse
from dify_sdk.advanced_chat.client import AsyncAdvancedChatClient
from dify_sdk.advanced_chat.types.file_input import FileInput
from dify_sdk_testing import RUNNING_IN_CI

LOGIN_USER_ID = "test123"


async def test_get_app_info(app_advanced_chat_client: AsyncAdvancedChatClient):
    """测试获取应用信息"""
    response = await app_advanced_chat_client.get_application_info_by_app_advanced_chat()
    assert response.name is not None and len(response.name) > 0
    assert response.description is not None
    assert isinstance(response.tags, list)

    for tag in response.tags:
        assert isinstance(tag, str)


async def test_get_app_info_error_handling(app_advanced_chat_client: AsyncAdvancedChatClient):
    """测试获取应用信息时错误处理"""
    # 获取原始客户端和原始 base_url
    raw_client = app_advanced_chat_client._raw_client  # type: ignore
    original_host = raw_client._client_wrapper.get_base_url()  # type: ignore

    # 修改 base_url 为无效地址
    raw_client._client_wrapper._base_url = "https://invalid.example.com"  # type: ignore

    with pytest.raises(Exception):
        await app_advanced_chat_client.get_application_info_by_app_advanced_chat()

    # 恢复原始 base_url
    raw_client._client_wrapper._base_url = original_host  # type: ignore


async def test_chat_messages(app_advanced_chat_client: AsyncAdvancedChatClient) -> str | None:
    """测试对话消息接口"""
    response_iterator = app_advanced_chat_client.send_chat_message_by_app_advanced_chat(
        query="ping",
        response_mode="streaming",  # 使用流式模式
        user=LOGIN_USER_ID,
        inputs=None,
    )

    message_id = None

    async for event_ in response_iterator:
        if isinstance(event_, str):
            # 跳过空字符串
            if not event_.strip():
                continue
            event = ChunkChatCompletionResponse.model_validate_json(event_)
        else:
            event = event_
        if not message_id and event.message_id:
            message_id = event.message_id

    assert message_id is not None, "无法获取 message_id"
    return message_id


async def test_message_feedback(app_advanced_chat_client: AsyncAdvancedChatClient):
    """测试消息反馈接口"""
    message_id = await test_chat_messages(app_advanced_chat_client)
    assert message_id is not None

    response = await app_advanced_chat_client.send_message_feedback_by_app_advanced_chat(
        message_id=message_id,
        rating="like",
        user=LOGIN_USER_ID,
    )
    assert response is not None
    assert response.result == "success"


async def test_conversation_management(app_advanced_chat_client: AsyncAdvancedChatClient):
    """测试会话管理相关接口"""
    conversations = await app_advanced_chat_client.get_conversations_by_app_advanced_chat(
        user=LOGIN_USER_ID, sort_by="created_at"
    )
    assert conversations is not None
    assert conversations.data is not None

    if conversations.data and len(conversations.data) > 0:
        conversation = conversations.data[0]
        assert conversation.id is not None
        conversation_id = str(conversation.id)

        renamed = await app_advanced_chat_client.rename_conversation_by_app_advanced_chat(
            conversation_id=conversation_id,
            user=LOGIN_USER_ID,
            name="dify-openapi 测试会话",
        )
        assert renamed is not None
        assert renamed.name == "dify-openapi 测试会话"
        if renamed.id is None:
            pytest.skip("无法获取重命名后的会话ID")
        conversation_id = str(renamed.id)

        messages = await app_advanced_chat_client.get_conversation_messages_by_app_advanced_chat(
            conversation_id=conversation_id,
            user=LOGIN_USER_ID,
        )
        assert messages is not None
        assert messages.data is not None

        # 删除会话API返回204 No Content，SDK返回None
        delete_response = await app_advanced_chat_client.delete_conversation_by_app_advanced_chat(
            conversation_id=conversation_id,
            user=LOGIN_USER_ID,
        )
        # 204 No Content响应，delete_response应该为None
        assert delete_response is None


async def test_get_parameters(app_advanced_chat_client: AsyncAdvancedChatClient):
    """测试获取应用参数"""
    response = await app_advanced_chat_client.get_application_parameters_by_app_advanced_chat()
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


async def test_file_upload(app_advanced_chat_client: AsyncAdvancedChatClient, test_file_path: Path) -> str | None:
    """测试文件上传接口"""
    response = await app_advanced_chat_client.upload_file_by_app_advanced_chat(
        file=("test.txt", test_file_path.read_bytes(), "text/plain"),
        user=LOGIN_USER_ID,
    )
    assert response.id is not None
    return response.id


async def test_chat_with_suggested_questions(app_advanced_chat_client: AsyncAdvancedChatClient):
    """测试对话并获取下一轮建议问题"""
    # 1. 发送对话消息
    response_iterator = app_advanced_chat_client.send_chat_message_by_app_advanced_chat(
        query="dify-openapi 测试问题",
        response_mode="streaming",  # 使用流式模式
        user=LOGIN_USER_ID,
        inputs=None,
    )

    message_id = None
    async for event_ in response_iterator:
        if isinstance(event_, str):
            # 跳过空字符串
            if not event_.strip():
                continue
            event = ChunkChatCompletionResponse.model_validate_json(event_)
        else:
            event = event_

        if not message_id and event.message_id:
            message_id = event.message_id

    assert message_id is not None, "无法获取 message_id"

    # 2. 获取建议问题
    params = await app_advanced_chat_client.get_application_parameters_by_app_advanced_chat()
    if params.suggested_questions_after_answer and params.suggested_questions_after_answer.enabled:
        suggested_questions = await app_advanced_chat_client.get_suggested_questions_by_app_advanced_chat(
            message_id=message_id,
            user=LOGIN_USER_ID,
        )
        assert suggested_questions is not None
        assert isinstance(suggested_questions.data, list)
        for question in suggested_questions.data:
            assert isinstance(question, str)


async def test_chat_with_file(app_advanced_chat_client: AsyncAdvancedChatClient, test_file_path: Path):
    """测试带文件的对话"""
    # 1. 先上传文件
    file_id = await test_file_upload(app_advanced_chat_client, test_file_path)
    assert file_id

    # 2. 发送带文件的对话消息
    file_input = FileInput(
        type="document",
        transfer_method="local_file",
        upload_file_id=file_id,
    )

    response_iterator = app_advanced_chat_client.send_chat_message_by_app_advanced_chat(
        query="dify-openapi 测试问题 - 请分析上传的文件",
        response_mode="streaming",
        user=LOGIN_USER_ID,
        files=[file_input],
        inputs=None,
    )

    message_id = None
    async for event_ in response_iterator:
        if isinstance(event_, str):
            # 跳过空字符串
            if not event_.strip():
                continue
            event = ChunkChatCompletionResponse.model_validate_json(event_)
        else:
            event = event_
        if not message_id and event.message_id:
            message_id = event.message_id

    assert message_id is not None, "无法获取 message_id"
    return message_id


async def test_audio_to_text(app_advanced_chat_client: AsyncAdvancedChatClient, test_audio_file_path: Path):
    """测试语音转文字接口"""
    # 先检查应用是否启用了语音转文字功能
    params = await app_advanced_chat_client.get_application_parameters_by_app_advanced_chat()
    params_dict = params.model_dump()
    if (
        "speech_to_text" not in params_dict
        or not params_dict["speech_to_text"]
        or not params_dict["speech_to_text"].get("enabled", False)
    ):
        pytest.skip("Speech to text is not enabled for this application")

    try:
        response = await app_advanced_chat_client.convert_audio_to_text_by_app_advanced_chat(
            file=("test.mp3", test_audio_file_path.read_bytes(), "audio/mp3"),
            user=LOGIN_USER_ID,
        )
        assert response is not None
        assert hasattr(response, "text")
        assert response.text is not None
        assert response.text != ""
    except Exception as e:
        if "Speech to text is not enabled" in str(e):
            pytest.skip(f"Speech to text API failed: {e}")


@pytest.mark.skipif(
    RUNNING_IN_CI,
    reason="CI中使用官方服务器, 经常报504超时, 影响CI流程, 请使用本地服务测试",
)
async def test_text_to_audio(app_advanced_chat_client: AsyncAdvancedChatClient):
    """测试文字转语音接口"""
    # 先检查应用是否启用了文字转语音功能
    params = await app_advanced_chat_client.get_application_parameters_by_app_advanced_chat()
    params_dict = params.model_dump()
    if (
        "text_to_speech" not in params_dict
        or not params_dict["text_to_speech"]
        or not params_dict["text_to_speech"].get("enabled", False)
    ):
        pytest.skip("Text to speech is not enabled for this application")

    try:
        audio_chunks: list[bytes] = []
        async for chunk in app_advanced_chat_client.convert_text_to_audio_by_app_advanced_chat(
            text="Hi",
            user=LOGIN_USER_ID,
        ):
            audio_chunks.append(chunk)

        assert len(audio_chunks) > 0
        for chunk in audio_chunks:
            assert isinstance(chunk, bytes)
    except Exception as e:
        if "TTS is not enabled" in str(e):
            pytest.skip(f"Text to speech API failed: {e}")
        else:
            raise


@pytest.mark.skipif(
    RUNNING_IN_CI,
    reason="CI中使用官方服务器, 经常报504超时, 影响CI流程, 请使用本地服务测试",
)
async def test_get_app_feedbacks(app_advanced_chat_client: AsyncAdvancedChatClient):
    """测试获取应用反馈"""
    feedbacks = await app_advanced_chat_client.get_app_feedbacks_by_app_advanced_chat(
        page=1,
        limit=10
    )
    assert feedbacks is not None
    assert hasattr(feedbacks, "data")
    assert isinstance(feedbacks.data, list)


async def test_get_app_site_settings(app_advanced_chat_client: AsyncAdvancedChatClient):
    """测试获取应用WebApp设置"""
    settings = await app_advanced_chat_client.get_app_web_app_settings_by_app_advanced_chat()
    assert settings is not None
    assert hasattr(settings, "title")
    assert hasattr(settings, "icon_type")
    assert hasattr(settings, "description")
    assert hasattr(settings, "default_language")


async def test_annotation_features(app_advanced_chat_client: AsyncAdvancedChatClient):
    """测试标注相关功能"""
    # 创建标注
    annotation_response = await app_advanced_chat_client.create_annotation_by_app_advanced_chat(
        question="What is Dify?",
        answer="Dify is an LLM application development platform.",
    )
    assert annotation_response is not None
    assert annotation_response.id is not None

    # 配置标注回复
    config_response = await app_advanced_chat_client.configure_annotation_reply_by_app_advanced_chat(
        action="enable",
        embedding_provider_name="siliconflow",
        embedding_model_name="BAAI/bge-large-en-v1.5",
        score_threshold=0.8,
    )
    assert config_response is not None
    assert config_response.job_id is not None

    # 获取标注回复状态
    await asyncio.sleep(5)
    # 如果前面的配置标注回复成功了，才获取状态
    status_response = await app_advanced_chat_client.get_annotation_reply_status_by_app_advanced_chat(
        action="enable",
        job_id=config_response.job_id,
    )
    assert status_response is not None
    # 检查响应中是否有状态信息
    response_dict = status_response.model_dump()
    assert "job_status" in response_dict
    assert response_dict["job_status"] in ["pending", "running", "completed", "failed", "waiting"]
