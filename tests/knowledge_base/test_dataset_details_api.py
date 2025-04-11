"""
测试知识库详情相关的 API 接口，验证 OpenAPI Schema 的正确性
"""

import pytest

from dify_sdk.types.dataset import Dataset
from dify_sdk_testing import KnowledgeBaseClient


@pytest.fixture
async def test_dataset(kb_client: KnowledgeBaseClient):
    """创建一个测试用的知识库"""
    dataset = await kb_client.dataset.create_empty_dataset(
        name="dify-openapi 测试-知识库详情测试",
        description="用于测试知识库详情相关接口",
        indexing_technique="high_quality",
    )
    assert dataset is not None
    assert dataset.id is not None

    try:
        yield dataset
    finally:
        await kb_client.dataset.delete_dataset(dataset_id=str(dataset.id))


async def test_view_knowledge_base_details(kb_client: KnowledgeBaseClient, test_dataset: Dataset):
    """测试查看知识库详情"""
    dataset_id = str(test_dataset.id)

    # 获取知识库详情
    dataset_details = await kb_client.dataset.view_knowledge_base_details(dataset_id=dataset_id)

    # 验证返回的数据
    assert dataset_details is not None
    assert dataset_details.id == test_dataset.id
    assert dataset_details.name == test_dataset.name
    assert dataset_details.description == test_dataset.description
    assert dataset_details.indexing_technique == test_dataset.indexing_technique

    # 验证其他字段
    assert hasattr(dataset_details, "app_count")
    assert hasattr(dataset_details, "document_count")
    assert hasattr(dataset_details, "word_count")
    assert hasattr(dataset_details, "created_at")
    assert hasattr(dataset_details, "updated_at")


async def test_update_knowledge_base_details(kb_client: KnowledgeBaseClient, test_dataset: Dataset):
    """测试更新知识库详情"""
    dataset_id = str(test_dataset.id)

    # 更新知识库详情
    updated_dataset = await kb_client.dataset.update_knowledge_base_details(
        dataset_id=dataset_id,
        indexing_technique="economy",  # 从 high_quality 改为 economy
        permission="only_me",
    )

    # 验证返回的数据
    assert updated_dataset is not None
    assert updated_dataset.id == test_dataset.id
    assert updated_dataset.name == test_dataset.name
    assert updated_dataset.indexing_technique == "economy"
    assert updated_dataset.permission == "only_me"

    # 再次获取知识库详情，确认更新成功
    dataset_details = await kb_client.dataset.view_knowledge_base_details(dataset_id=dataset_id)
    assert dataset_details.indexing_technique == "economy"
