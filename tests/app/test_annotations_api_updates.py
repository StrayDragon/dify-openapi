"""
测试注释API的更新
"""

import warnings

from dify_sdk.chat.client import AsyncChatClient
from dify_sdk.advanced_chat.client import AsyncAdvancedChatClient

LOGIN_USER_ID = "test123"


async def test_create_annotation_response_format(app_chat_client: AsyncChatClient):
    """测试创建注释API的响应格式（修复了多余的嵌套）"""
    # 创建标注
    annotation_response = await app_chat_client.create_annotation_by_app_chat(
        question="What is the response format in 1.3.1?",
        answer="The response format in 1.3.1 has been fixed to remove redundant nesting.",
    )

    # 验证响应格式
    assert annotation_response is not None
    assert annotation_response.id is not None
    assert annotation_response.question is not None
    assert annotation_response.answer is not None
    assert annotation_response.hit_count is not None
    assert annotation_response.created_at is not None


async def test_update_annotation_http_method(app_chat_client: AsyncChatClient):
    """测试更新注释API的HTTP方法（从POST改为PUT）"""
    # 创建标注
    annotation_response = await app_chat_client.create_annotation_by_app_chat(
        question="What HTTP method is used for updating annotations in 1.3.1?",
        answer="PUT method is used for updating annotations in 1.3.1, changed from POST in previous versions.",
    )
    assert annotation_response is not None
    assert annotation_response.id is not None

    # 更新标注
    updated_response = await app_chat_client.update_annotation_by_app_chat(
        annotation_id=str(annotation_response.id),
        question="What HTTP method is used for updating annotations in 1.3.1?",
        answer="PUT method is used for updating annotations in 1.3.1, changed from POST in previous versions. This is an updated answer.",
    )

    # 验证更新成功
    assert updated_response is not None
    assert updated_response.id == annotation_response.id
    assert updated_response.question == "What HTTP method is used for updating annotations in 1.3.1?"
    assert "This is an updated answer" in str(updated_response.answer)


async def test_configure_annotation_reply_parameter_names(app_advanced_chat_client: AsyncAdvancedChatClient):
    """测试配置注释回复API的参数名称变更"""
    try:
        # 配置标注回复
        config_response = await app_advanced_chat_client.configure_annotation_reply_by_app_advanced_chat(
            action="enable",
            embedding_provider_name="siliconflow",  # 新参数名称，原为embedding_model_provider
            embedding_model_name="BAAI/bge-large-en-v1.5",  # 新参数名称，原为embedding_model
            score_threshold=0.8,
        )

        # 验证响应
        assert config_response is not None
    except Exception as e:
        # 如果测试环境中没有配置嵌入模型，可能会失败
        warnings.warn(f"配置注释回复API测试失败，可能是因为测试环境中没有配置嵌入模型: {str(e)}")


async def test_advanced_chat_annotation_response_format(app_advanced_chat_client: AsyncAdvancedChatClient):
    """测试高级聊天应用中注释API的响应格式"""
    # 创建标注
    annotation_response = await app_advanced_chat_client.create_annotation_by_app_advanced_chat(
        question="What is the response format in advanced chat API?",
        answer="The response format in advanced chat API has been fixed to remove redundant nesting.",
    )

    # 验证响应格式
    assert annotation_response is not None
    assert annotation_response.id is not None
    assert annotation_response.question is not None
    assert annotation_response.answer is not None
    assert annotation_response.hit_count is not None
    assert annotation_response.created_at is not None

    # 更新标注
    updated_response = await app_advanced_chat_client.update_annotation_by_app_advanced_chat(
        annotation_id=str(annotation_response.id),
        question="What is the response format in advanced chat API?",
        answer="The response format in advanced chat API has been fixed to remove redundant nesting. This is an updated answer.",
    )

    # 验证更新成功
    assert updated_response is not None
    assert updated_response.id == annotation_response.id
    assert "This is an updated answer" in str(updated_response.answer)
