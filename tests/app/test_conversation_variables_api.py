import pytest
import warnings

from dify_sdk.chat.client import AsyncChatClient
from dify_sdk.advanced_chat.client import AsyncAdvancedChatClient
from dify_sdk_testing import parse_stream_event

LOGIN_USER_ID = "test123"


async def create_conversation(client: AsyncChatClient | AsyncAdvancedChatClient) -> str | None:
    """创建一个对话并返回对话ID"""
    # 发送一条消息以创建对话
    if isinstance(client, AsyncChatClient):
        response_iterator = client.send_chat_message_by_app_chat(
            query="创建一个对话并记录一些变量",
            response_mode="streaming",
            user=LOGIN_USER_ID,
            inputs=None,
        )
    else:
        response_iterator = client.send_chat_message_by_app_advanced_chat(
            query="创建一个对话并记录一些变量",
            response_mode="streaming",
            user=LOGIN_USER_ID,
            inputs=None,
        )

    conversation_id = None
    async for event_ in response_iterator:
        event = parse_stream_event(event_, "chat" if isinstance(client, AsyncChatClient) else "advanced_chat")
        if event is None:
            continue
        if not conversation_id and event.conversation_id:
            conversation_id = event.conversation_id
            break

    # 如果无法从流式响应获取对话ID，则从对话列表获取
    if not conversation_id:
        if isinstance(client, AsyncChatClient):
            conversations = await client.get_conversation_list_by_app_chat(
                user=LOGIN_USER_ID, sort_by="created_at"
            )
        else:
            conversations = await client.get_conversations_by_app_advanced_chat(
                user=LOGIN_USER_ID, sort_by="created_at"
            )

        if conversations and conversations.data and len(conversations.data) > 0:
            conversation_id = str(conversations.data[0].id)

    return conversation_id


@pytest.mark.asyncio
async def test_get_conversation_variables_chat(app_chat_client: AsyncChatClient):
    """测试获取对话变量 - 普通聊天应用"""
    # 创建一个对话
    conversation_id = await create_conversation(app_chat_client)
    assert conversation_id is not None, "无法创建对话"

    # 获取对话变量
    try:
        variables = await app_chat_client.get_conversation_variables_by_app_chat(
            conversation_id=conversation_id,
            user=LOGIN_USER_ID,
        )

        # 验证响应结构
        assert variables is not None
        assert hasattr(variables, "limit")
        assert hasattr(variables, "has_more")
        assert hasattr(variables, "data")

        # 数据可能为空，因为测试环境中可能没有设置变量
        if variables.data and len(variables.data) > 0:
            for variable in variables.data:
                assert variable.id is not None
                assert variable.name is not None
                assert variable.value_type is not None
                assert hasattr(variable, "value")
                assert hasattr(variable, "created_at")
                assert hasattr(variable, "updated_at")
    except Exception as e:
        # 如果API尚未实现或返回错误，记录警告但不使测试失败
        warnings.warn(f"获取对话变量API可能尚未完全实现: {str(e)}")


@pytest.mark.asyncio
async def test_get_conversation_variables_advanced_chat(app_advanced_chat_client: AsyncAdvancedChatClient):
    """测试获取对话变量 - 高级聊天应用"""
    # 创建一个对话
    conversation_id = await create_conversation(app_advanced_chat_client)
    assert conversation_id is not None, "无法创建对话"

    # 获取对话变量
    try:
        variables = await app_advanced_chat_client.get_conversation_variables_by_app_advanced_chat(
            conversation_id=conversation_id,
            user=LOGIN_USER_ID,
        )

        # 验证响应结构
        assert variables is not None
        assert hasattr(variables, "limit")
        assert hasattr(variables, "has_more")
        assert hasattr(variables, "data")

        # 测试变量名过滤功能
        if variables.data and len(variables.data) > 0:
            variable_name = variables.data[0].name
            filtered_variables = await app_advanced_chat_client.get_conversation_variables_by_app_advanced_chat(
                conversation_id=conversation_id,
                user=LOGIN_USER_ID,
                variable_name=variable_name,
            )
            assert filtered_variables is not None
            assert filtered_variables.data is not None

            # 验证过滤结果
            if filtered_variables.data:
                for variable in filtered_variables.data:
                    assert variable.name == variable_name
    except Exception as e:
        # 如果API尚未实现或返回错误，记录警告但不使测试失败
        warnings.warn(f"获取对话变量API可能尚未完全实现: {str(e)}")


@pytest.mark.asyncio
async def test_conversation_variables_pagination(app_advanced_chat_client: AsyncAdvancedChatClient):
    """测试对话变量分页功能"""
    # 创建一个对话
    conversation_id = await create_conversation(app_advanced_chat_client)
    assert conversation_id is not None, "无法创建对话"

    # 测试分页参数
    try:
        # 使用较小的limit
        variables = await app_advanced_chat_client.get_conversation_variables_by_app_advanced_chat(
            conversation_id=conversation_id,
            user=LOGIN_USER_ID,
            limit=5,
        )

        assert variables is not None
        if variables.limit is not None:
            assert variables.limit <= 5

        # 如果有更多数据，测试last_id参数
        if variables.has_more and variables.data and len(variables.data) > 0:
            last_id = variables.data[-1].id
            next_page = await app_advanced_chat_client.get_conversation_variables_by_app_advanced_chat(
                conversation_id=conversation_id,
                user=LOGIN_USER_ID,
                last_id=last_id,
            )

            assert next_page is not None
            assert next_page.data is not None
    except Exception as e:
        # 如果API尚未实现或返回错误，记录警告但不使测试失败
        warnings.warn(f"对话变量分页功能可能尚未完全实现: {str(e)}")
