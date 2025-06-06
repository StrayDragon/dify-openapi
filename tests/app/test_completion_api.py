"""
测试文本生成客户端的API功能
"""

import pytest
from pathlib import Path

from dify_sdk.generation.client import AsyncGenerationClient
from dify_sdk.core.request_options import RequestOptions
from dify_sdk.generation.types.send_completion_message_by_app_generation_request_inputs import (
    SendCompletionMessageByAppGenerationRequestInputs,
)
from dify_sdk_testing import RUNNING_IN_CI, parse_stream_event

LOGIN_USER_ID = "test123"


async def test_get_app_info(app_completion_client: AsyncGenerationClient):
    """测试获取应用信息"""
    response = await app_completion_client.get_application_info_by_app_generation()
    assert response.name is not None and len(response.name) > 0
    assert response.description is not None
    assert isinstance(response.tags, list)

    for tag in response.tags:
        assert isinstance(tag, str)


async def test_get_app_info_error_handling(app_completion_client: AsyncGenerationClient):
    """测试获取应用信息时错误处理"""
    # 获取原始客户端和原始 base_url
    raw_client = app_completion_client._raw_client  # type: ignore
    original_host = raw_client._client_wrapper.get_base_url()  # type: ignore

    # 修改 base_url 为无效地址
    raw_client._client_wrapper._base_url = "https://invalid.example.com"  # type: ignore

    with pytest.raises(Exception):
        await app_completion_client.get_application_info_by_app_generation()

    # 恢复原始 base_url
    raw_client._client_wrapper._base_url = original_host  # type: ignore


async def test_completion_message(app_completion_client: AsyncGenerationClient) -> str | None:
    """测试文本生成接口"""
    response_iterator = app_completion_client.send_completion_message_by_app_generation(
        inputs=SendCompletionMessageByAppGenerationRequestInputs(query="ping"),
        response_mode="streaming",
        user=LOGIN_USER_ID,
        request_options=RequestOptions(timeout_in_seconds=30),
    )

    message_id = None
    async for event_ in response_iterator:
        event = parse_stream_event(event_, "generation")
        if event is None:
            continue
        if not message_id and event.message_id:
            message_id = event.message_id

    assert message_id is not None, "无法获取 message_id"
    return message_id


async def test_message_feedback(app_completion_client: AsyncGenerationClient):
    """测试消息反馈接口"""
    message_id = await test_completion_message(app_completion_client)
    assert message_id is not None

    response = await app_completion_client.send_message_feedback_by_app_generation(
        message_id=message_id,
        rating="like",
        user=LOGIN_USER_ID,
    )
    assert response is not None
    assert response.result == "success"


async def test_get_parameters(app_completion_client: AsyncGenerationClient):
    """测试获取应用参数"""
    response = await app_completion_client.get_application_parameters_by_app_generation()
    assert response is not None
    # opening_statement 可能为 None
    assert hasattr(response, "opening_statement")
    assert hasattr(response, "suggested_questions")
    assert hasattr(response, "speech_to_text")
    assert hasattr(response, "retriever_resource")


@pytest.fixture
def test_file_path() -> Path:
    """测试用的文件路径"""
    return Path("tests/data/app/test.txt")


@pytest.fixture
def test_audio_file_path() -> Path:
    """创建测试用的临时音频文件"""
    return Path("tests/data/app/audio.mp3")


async def test_file_upload(app_completion_client: AsyncGenerationClient, test_file_path: Path) -> str | None:
    """测试文件上传接口"""
    response = await app_completion_client.upload_file_by_app_generation(
        file=("test.txt", test_file_path.read_bytes(), "text/plain"),
        user=LOGIN_USER_ID,
    )
    assert response.id is not None
    return response.id


async def test_get_app_meta_info(app_completion_client: AsyncGenerationClient):
    """测试获取应用元信息"""
    response = await app_completion_client.get_app_meta_info_by_app_generation()
    assert response is not None
    # 新版本中可能不再有 tools 属性
    # 检查是否有 tool_icons 属性
    assert hasattr(response, "tool_icons")
    assert isinstance(response.tool_icons, dict)


@pytest.mark.skipif(
    RUNNING_IN_CI,
    reason="CI中使用官方服务器, 经常报504超时, 影响CI流程, 请使用本地服务测试",
)
async def test_text_to_audio(app_completion_client: AsyncGenerationClient):
    """测试文字转语音接口"""
    # 先检查应用是否启用了文字转语音功能
    params = await app_completion_client.get_application_parameters_by_app_generation()
    params_dict = params.model_dump()
    if (
        "text_to_speech" not in params_dict
        or not params_dict["text_to_speech"]
        or not params_dict["text_to_speech"].get("enabled", False)
    ):
        pytest.skip("Text to speech is not enabled for this application")

    try:
        audio_chunks: list[bytes] = []
        async for chunk in app_completion_client.convert_text_to_audio_by_app_generation(
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
