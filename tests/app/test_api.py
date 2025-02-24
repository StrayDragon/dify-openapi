import pytest
from pathlib import Path
from io import BytesIO
from typing import cast, Optional, Union

from dify_openapi_app.models.post_chat_messages_body import PostChatMessagesBody
from dify_openapi_app.models.delete_conversations_conversation_id_body import DeleteConversationsConversationIdBody
from dify_openapi_app.models.post_messages_message_id_feedbacks_body import PostMessagesMessageIdFeedbacksBody
from dify_openapi_app.models.post_conversations_conversation_id_name_body import PostConversationsConversationIdNameBody
from dify_openapi_app.models.post_text_to_audio_body import PostTextToAudioBody
from dify_openapi_app.models.file_input import FileInput
from dify_openapi_app.models.post_chat_messages_body_inputs import PostChatMessagesBodyInputs
from dify_openapi_app.models.post_files_upload_body import PostFilesUploadBody
from dify_openapi_app.models.post_audio_to_text_body import PostAudioToTextBody
from dify_openapi_app.models.chat_message import ChatMessage
from dify_openapi_app.models.conversation import Conversation
from dify_openapi_app.models.uploaded_file import UploadedFile
from dify_openapi_app.types import UNSET, File, Unset

from dify_openapi_app.api.default import (
    get_info,
    get_parameters,
    get_conversations,
    get_messages,
    post_chat_messages,
    post_messages_message_id_feedbacks,
    post_conversations_conversation_id_name,
    delete_conversations_conversation_id,
    post_files_upload,
    post_audio_to_text,
    post_text_to_audio,
)

LOGIN_USER_ID = "test123"


async def test_get_app_info(c):
    """测试获取应用基本信息接口"""
    response = await get_info.asyncio(client=c.app_client)

    # 验证响应不为空
    assert response is not None

    # 验证基本字段存在
    assert hasattr(response, "name")
    assert hasattr(response, "description")
    assert hasattr(response, "tags")

    # 验证name字段类型正确且不为空
    assert isinstance(response.name, str)
    assert len(response.name) > 0

    # 如果有tags，验证其为列表类型
    if response.tags:
        assert isinstance(response.tags, list)
        for tag in response.tags:
            assert isinstance(tag, str)


async def test_get_app_info_error_handling(c):
    """测试获取应用基本信息接口的错误处理"""
    # 这里我们可以通过修改client的配置来触发错误
    # 比如修改host为一个无效的地址
    original_host = c.app_client._base_url
    c.app_client._base_url = "https://invalid.example.com"

    with pytest.raises(Exception):
        await get_info.asyncio(client=c.app_client)

    # 恢复原始配置
    c.app_client._base_url = original_host


async def test_chat_messages(c):
    """测试发送对话消息接口"""
    inputs = PostChatMessagesBodyInputs()
    request = PostChatMessagesBody(
        query="ping",
        user=LOGIN_USER_ID,
        response_mode="blocking",
        inputs=inputs,
    )

    response = await post_chat_messages.asyncio(client=c.app_client, body=request)
    assert response is not None
    assert hasattr(response, "message_id")

    # 保存message_id用于后续测试
    return response.message_id


async def test_message_feedback(c):
    """测试消息反馈接口"""
    # 先发送一条消息
    message_id = await test_chat_messages(c)
    if message_id is None or isinstance(message_id, Unset):
        pytest.skip("无法获取消息ID")

    # 测试点赞功能
    request = PostMessagesMessageIdFeedbacksBody(
        rating="like",
        user=LOGIN_USER_ID,
    )

    response = await post_messages_message_id_feedbacks.asyncio(
        client=c.app_client, message_id=str(message_id), body=request
    )
    assert response is not None
    assert hasattr(response, "result")
    assert response.result == "success"


async def test_conversation_management(c):
    """测试会话管理相关接口"""
    # 1. 获取会话列表
    conversations = await get_conversations.asyncio(client=c.app_client, user=LOGIN_USER_ID)
    assert conversations is not None
    assert hasattr(conversations, "data")

    if (
        conversations.data is not None
        and isinstance(conversations.data, list)
        and len(conversations.data) > 0
        and isinstance(conversations.data[0], Conversation)
    ):
        conversation = conversations.data[0]
        if conversation.id is None or isinstance(conversation.id, Unset):
            pytest.skip("无法获取会话ID")
        conversation_id = str(conversation.id)

        # 2. 测试重命名会话
        rename_request = PostConversationsConversationIdNameBody(
            name="dify-openapi 测试会话",
            user=LOGIN_USER_ID,
        )
        renamed = await post_conversations_conversation_id_name.asyncio(
            client=c.app_client, conversation_id=conversation_id, body=rename_request
        )
        assert renamed is not None
        assert renamed.name == "dify-openapi 测试会话"
        if renamed.id is None or isinstance(renamed.id, Unset):
            pytest.skip("无法获取重命名后的会话ID")
        conversation_id = str(renamed.id)

        # 3. 获取会话历史消息
        messages = await get_messages.asyncio(
            client=c.app_client,
            conversation_id=conversation_id,
            user=LOGIN_USER_ID,
        )
        assert messages is not None
        assert hasattr(messages, "data")

        # 4. 删除会话
        delete_request = DeleteConversationsConversationIdBody(
            user=LOGIN_USER_ID,
        )
        delete_response = await delete_conversations_conversation_id.asyncio(
            client=c.app_client,
            conversation_id=conversation_id,
            body=delete_request,
        )
        assert delete_response is not None
        assert delete_response.result == "success"


async def test_get_parameters(c):
    """测试获取应用参数接口"""
    response = await get_parameters.asyncio(client=c.app_client)
    assert response is not None

    # 验证关键参数字段存在
    assert hasattr(response, "opening_statement")
    assert hasattr(response, "suggested_questions")
    assert hasattr(response, "speech_to_text")
    assert hasattr(response, "retriever_resource")


@pytest.fixture
def test_file_path():
    yield Path("tests/data/app/test.txt")


@pytest.fixture
def test_audio_file_path():
    """创建测试用的临时音频文件"""
    file_path = Path("tests/data/app/audio.mp3")
    yield file_path


async def test_file_upload(c, test_file_path):
    """测试文件上传接口"""
    with open(test_file_path, "rb") as f:
        file_data = BytesIO(f.read())
        request = PostFilesUploadBody(
            file=File(payload=file_data),
            user=LOGIN_USER_ID,
        )
        response = await post_files_upload.asyncio(client=c.app_client, body=request)
        if isinstance(response, UploadedFile):
            assert response.id is not None
            return response.id
        return None


@pytest.mark.skip(reason="FIXME: sdk暂不支持, 可以直接用openapi-ui测试")
async def test_audio_to_text(c, test_audio_file_path):
    """测试语音转文字接口"""
    file_data = BytesIO(test_audio_file_path.read_bytes())
    request = PostAudioToTextBody(
        file=File(payload=file_data),
        user=LOGIN_USER_ID,
    )
    response = await post_audio_to_text.asyncio(client=c.app_client, body=request)

    assert response is not None
    assert hasattr(response, "text")
    return response.text


@pytest.mark.skip(reason="FIXME: sdk暂不支持, 可以直接用openapi-ui测试")
async def test_text_to_audio(c):
    """测试文字转语音接口"""
    request = PostTextToAudioBody(
        text="dify-openapi 测试文本转语音",
        user=LOGIN_USER_ID,
    )

    # 注意：这个接口返回二进制音频数据
    response = await post_text_to_audio.asyncio_detailed(client=c.app_client, body=request)
    assert response is not None
    assert len(response.content) > 0  # 确保返回了音频数据


async def test_chat_with_suggested_questions(c):
    """测试对话并获取下一轮建议问题"""
    # 1. 发送对话消息
    inputs = PostChatMessagesBodyInputs()
    request = PostChatMessagesBody(
        query="dify-openapi 测试问题",
        user=LOGIN_USER_ID,
        response_mode="blocking",
        inputs=inputs,
    )

    chat_response = await post_chat_messages.asyncio(client=c.app_client, body=request)
    assert chat_response is not None
    if not isinstance(chat_response, ChatMessage):
        pytest.skip("响应类型不正确")

    # 2. 获取应用参数，检查是否启用了建议问题功能
    params = await get_parameters.asyncio(client=c.app_client)
    if (
        params is not None
        and params.suggested_questions_after_answer
        and params.suggested_questions_after_answer.enabled
    ):
        # 如果启用了建议问题功能，应该在chat_response的additional_properties中包含建议问题
        if "suggested_questions" in chat_response.additional_properties:
            suggested_questions = chat_response.additional_properties["suggested_questions"]
            assert isinstance(suggested_questions, list)
            for question in suggested_questions:
                assert isinstance(question, str)


@pytest.mark.skip(reason="FIXME: sdk不支持")
async def test_chat_with_file(c, test_file_path):
    """测试带文件的对话"""
    # 1. 先上传文件
    file_id = await test_file_upload(c, test_file_path)

    # 2. 发送带文件的对话消息
    inputs = PostChatMessagesBodyInputs()
    request = PostChatMessagesBody(
        query="dify-openapi 测试问题 - 请分析上传的文件",
        user=LOGIN_USER_ID,
        response_mode="blocking",
        files=[
            FileInput(
                type_="document", transfer_method="local_file", upload_file_id=file_id if file_id is not None else UNSET
            )
        ],
        inputs=inputs,
    )

    response = await post_chat_messages.asyncio(client=c.app_client, body=request)
    assert response is not None
    assert hasattr(response, "message_id")
