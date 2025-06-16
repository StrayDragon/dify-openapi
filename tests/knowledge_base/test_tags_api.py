"""
测试知识库标签管理 API 的完整工作流程
"""

import pytest

from dify_sdk.knowledge_base.types.knowledge_tag import KnowledgeTag
from dify_sdk_testing import KnowledgeBaseClient


async def test_knowledge_tags_workflow(kb_client: KnowledgeBaseClient):
    """测试知识库标签管理的完整工作流程"""

    # 1. 获取初始标签列表
    initial_tags = await kb_client.tags.get_knowledge_tags()
    assert initial_tags is not None
    assert isinstance(initial_tags, list)
    initial_count = len(initial_tags)

    # 2. 创建新标签
    test_tag_name = "SDK测试标签"
    created_tag = await kb_client.tags.create_knowledge_tag(name=test_tag_name)
    assert created_tag is not None
    assert created_tag.id is not None
    assert created_tag.name == test_tag_name
    assert created_tag.type == "knowledge"
    assert created_tag.binding_count == 0

    tag_id = str(created_tag.id)

    try:
        # 3. 获取标签列表，验证新标签已创建
        updated_tags = await kb_client.tags.get_knowledge_tags()
        assert len(updated_tags) == initial_count + 1
        assert any(str(tag.id) == tag_id for tag in updated_tags)

        # 4. 更新标签名称
        new_tag_name = "SDK测试标签-已更新"
        updated_tag = await kb_client.tags.update_knowledge_tag(tag_id=tag_id, name=new_tag_name)
        assert updated_tag is not None
        assert str(updated_tag.id) == tag_id
        assert updated_tag.name == new_tag_name

        # 5. 验证标签名称已更新
        current_tags = await kb_client.tags.get_knowledge_tags()
        test_tag = next((tag for tag in current_tags if str(tag.id) == tag_id), None)
        assert test_tag is not None
        assert test_tag.name == new_tag_name

    finally:
        # 6. 删除测试标签
        delete_response = await kb_client.tags.delete_knowledge_tag(tag_id=tag_id)
        # 删除操作成功时返回None (HTTP 204 No Content)
        assert delete_response is None

        # 7. 验证标签已删除
        final_tags = await kb_client.tags.get_knowledge_tags()
        assert len(final_tags) == initial_count
        assert not any(str(tag.id) == tag_id for tag in final_tags)


async def create_knowledge_tag(kb_client: KnowledgeBaseClient, tag_name: str):
    try:
        t = await kb_client.tags.create_knowledge_tag(name=tag_name)
    except:
        t = next((tag for tag in await kb_client.tags.get_knowledge_tags() if tag.name == tag_name), None)
        if t is None:
            raise Exception(f"{tag_name} 不存在")
    return t


@pytest.fixture
async def knowledge_tag1(kb_client: KnowledgeBaseClient):
    tag_name = "测试绑定标签1"
    tag = await create_knowledge_tag(kb_client, tag_name)

    yield tag

    try:
        await kb_client.tags.delete_knowledge_tag(tag_id=str(tag.id))
    except:
        pass


@pytest.fixture
async def knowledge_tag2(kb_client: KnowledgeBaseClient):
    tag_name = "测试绑定标签2"
    tag = await create_knowledge_tag(kb_client, tag_name)

    yield tag

    try:
        await kb_client.tags.delete_knowledge_tag(tag_id=str(tag.id))
    except:
        pass


async def test_dataset_tag_binding_workflow(
    kb_client: KnowledgeBaseClient, knowledge_tag1: KnowledgeTag, knowledge_tag2: KnowledgeTag
):
    """测试知识库与标签绑定的完整工作流程"""

    # 1. 创建测试标签
    tag1_id = str(knowledge_tag1.id)
    tag2_id = str(knowledge_tag2.id)

    # 2. 创建测试数据集
    dataset = await kb_client.dataset.create_empty_dataset(
        name="标签绑定测试数据集",
        description="用于测试标签绑定功能的数据集",
        indexing_technique="high_quality",
    )
    dataset_id = str(dataset.id)

    try:
        # 3. 绑定数据集到多个标签
        bind_response = await kb_client.tags.bind_dataset_to_tag(tag_ids=[tag1_id, tag2_id], target_id=dataset_id)
        # 绑定操作成功时返回None (HTTP 204 No Content)
        assert bind_response is None

        # 4. 查询数据集已绑定的标签
        dataset_tags = await kb_client.tags.get_dataset_tags(dataset_id=dataset_id)
        assert dataset_tags is not None
        assert dataset_tags.data is not None
        assert isinstance(dataset_tags.total, int)
        assert dataset_tags.total >= 2

        # 验证绑定的标签ID
        bound_tag_ids = [str(tag.id) for tag in dataset_tags.data]
        assert tag1_id in bound_tag_ids
        assert tag2_id in bound_tag_ids

        # 5. 解绑其中一个标签
        unbind_response = await kb_client.tags.unbind_dataset_from_tag(tag_id=tag1_id, target_id=dataset_id)
        # 解绑操作成功时返回None (HTTP 204 No Content)
        assert unbind_response is None

        # 6. 验证解绑效果
        updated_dataset_tags = await kb_client.tags.get_dataset_tags(dataset_id=dataset_id)
        assert updated_dataset_tags is not None
        assert updated_dataset_tags.data is not None
        assert isinstance(dataset_tags.total, int)
        assert updated_dataset_tags.total == dataset_tags.total - 1

        # 验证tag1已解绑，tag2仍然绑定
        remaining_tag_ids = [str(tag.id) for tag in updated_dataset_tags.data]
        assert tag1_id not in remaining_tag_ids
        assert tag2_id in remaining_tag_ids

    finally:
        # 清理资源
        # 删除数据集
        await kb_client.dataset.delete_dataset(dataset_id=dataset_id)

        # 删除测试标签
        await kb_client.tags.delete_knowledge_tag(tag_id=tag1_id)
        await kb_client.tags.delete_knowledge_tag(tag_id=tag2_id)


async def test_tag_api_error_handling(kb_client: KnowledgeBaseClient):
    """测试标签API的错误处理"""

    # 1. 测试删除不存在的标签
    with pytest.raises(Exception):
        await kb_client.tags.delete_knowledge_tag(tag_id="non-existent-tag-id")

    # 2. 测试更新不存在的标签
    with pytest.raises(Exception):
        await kb_client.tags.update_knowledge_tag(tag_id="non-existent-tag-id", name="新名称")

    # 3. 测试绑定不存在的标签到数据集
    dataset = await kb_client.dataset.create_empty_dataset(
        name="错误处理测试数据集",
        description="用于测试错误处理的数据集",
        indexing_technique="high_quality",
    )
    dataset_id = str(dataset.id)

    try:
        with pytest.raises(Exception):
            await kb_client.tags.bind_dataset_to_tag(tag_ids=["non-existent-tag-id"], target_id=dataset_id)
    finally:
        await kb_client.dataset.delete_dataset(dataset_id=dataset_id)
