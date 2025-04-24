"""
测试知识库-子分段相关的 API 接口，验证 OpenAPI Schema 的正确性
"""

import asyncio
from multiprocessing.pool import RUN
import pytest

from dify_sdk import (
    ProcessRule,
    ProcessRuleRules,
)
from dify_sdk.types.dataset import Dataset
from dify_sdk.types.document import Document
from dify_sdk.segments import (
    CreateSegmentsRequestSegmentsItem,
)
from dify_sdk.types.segment import Segment
from dify_sdk_testing import RUNNING_IN_CI, KnowledgeBaseClient


@pytest.fixture
async def dataset_for_child_chunks(kb_client: KnowledgeBaseClient):
    """创建一个测试用的知识库"""
    dataset = await kb_client.dataset.create_empty_dataset(
        name="dify-openapi 测试-子分段测试库",
        description="用于测试子分段相关接口",
        indexing_technique="high_quality",
    )
    assert dataset is not None
    assert dataset.id is not None

    try:
        yield dataset
    finally:
        await kb_client.dataset.delete_dataset(dataset_id=str(dataset.id))


@pytest.fixture
async def document_for_child_chunks(kb_client: KnowledgeBaseClient, dataset_for_child_chunks: Dataset):
    """创建一个测试用的文档"""
    content = """
    # 测试文档

    这是一个用于测试子分段功能的文档。

    ## 第一部分
    这是第一个段落，用于测试基本的子分段功能。
    包含一些关键词：测试、子分段、API。

    ## 第二部分
    这是第二个段落，用于测试子分段更新功能。
    我们将测试以下功能：
    1. 创建子分段
    2. 更新子分段
    3. 删除子分段

    ## 第三部分
    这是第三个段落，用于测试高级子分段功能。
    包含一些特殊字符：
    * 列表项1
    * 列表项2
    * 列表项3
    """

    doc_response = await kb_client.document.create_document_by_text(
        dataset_id=str(dataset_for_child_chunks.id),
        name="test_child_chunks.md",
        text=content,
        indexing_technique="high_quality",
        process_rule=ProcessRule(
            mode="automatic",
            rules=ProcessRuleRules(),
        ),
    )
    assert doc_response is not None
    assert doc_response.document is not None
    return doc_response.document


@pytest.fixture
async def segment_for_child_chunks(
    kb_client: KnowledgeBaseClient, dataset_for_child_chunks: Dataset, document_for_child_chunks: Document
):
    """创建一个测试用的分段"""
    # 等待文档处理完成
    await asyncio.sleep(5)

    # 获取分段列表
    segments_response = await kb_client.segment.get_segments(
        dataset_id=str(dataset_for_child_chunks.id),
        document_id=str(document_for_child_chunks.id),
        page=1,
        limit=1,
    )

    assert segments_response is not None
    assert segments_response.data is not None
    assert len(segments_response.data) > 0

    # 如果没有分段，则创建一个
    if len(segments_response.data) == 0:
        segments = [
            CreateSegmentsRequestSegmentsItem(
                content="这是一个用于测试子分段功能的父分段",
                keywords=["测试", "子分段", "父分段"],
                answer=None,
            ),
        ]

        create_response = await kb_client.segment.create_segments(
            dataset_id=str(dataset_for_child_chunks.id),
            document_id=str(document_for_child_chunks.id),
            segments=segments,
        )

        assert create_response is not None
        assert create_response.data is not None
        assert len(create_response.data) > 0

        return create_response.data[0]

    return segments_response.data[0]


@pytest.mark.skipif(
    RUNNING_IN_CI,
    reason="这个测试中有些功能需要付费账号才能使用(CI中使用官方服务器, 测试账号受限), 请使用本地服务测试",
)
async def test_child_chunks_workflow(
    kb_client: KnowledgeBaseClient,
    dataset_for_child_chunks: Dataset,
    document_for_child_chunks: Document,
    segment_for_child_chunks: Segment,
):
    """测试子分段相关的完整工作流程"""
    dataset_id = str(dataset_for_child_chunks.id)
    document_id = str(document_for_child_chunks.id)
    segment_id = str(segment_for_child_chunks.id)

    # 1. 创建子分段
    child_chunk_content = "这是一个测试用的子分段内容"
    create_response = await kb_client.segment.create_document_child_segment(
        dataset_id=dataset_id,
        document_id=document_id,
        segment_id=segment_id,
        content=child_chunk_content,
    )

    assert create_response is not None
    assert create_response.data is not None
    assert create_response.data.content == child_chunk_content

    child_chunk_id = str(create_response.data.id)

    # 等待索引完成
    await asyncio.sleep(2)

    # 2. 查询子分段列表
    query_response = await kb_client.segment.query_document_child_segments(
        dataset_id=dataset_id,
        document_id=document_id,
        segment_id=segment_id,
        page=1,
        limit=10,
    )

    assert query_response is not None
    assert query_response.data is not None
    assert len(query_response.data) > 0
    assert any(str(chunk.id) == child_chunk_id for chunk in query_response.data)

    # 3. 更新子分段
    updated_content = "这是更新后的子分段内容"
    update_response = await kb_client.segment.update_document_child_segment(
        dataset_id=dataset_id,
        document_id=document_id,
        segment_id=segment_id,
        child_chunk_id=child_chunk_id,
        content=updated_content,
    )

    assert update_response is not None
    assert update_response.data is not None
    assert update_response.data.content == updated_content

    # 等待索引完成
    await asyncio.sleep(2)

    # 4. 再次查询子分段列表，验证更新成功
    query_response = await kb_client.segment.query_document_child_segments(
        dataset_id=dataset_id,
        document_id=document_id,
        segment_id=segment_id,
        page=1,
        limit=10,
    )

    assert query_response is not None
    assert query_response.data is not None
    assert len(query_response.data) > 0

    updated_chunk = next((chunk for chunk in query_response.data if str(chunk.id) == child_chunk_id), None)
    assert updated_chunk is not None
    assert updated_chunk.content == updated_content

    # 5. 删除子分段
    delete_response = await kb_client.segment.delete_document_child_segment(
        dataset_id=dataset_id,
        document_id=document_id,
        segment_id=segment_id,
        child_chunk_id=child_chunk_id,
    )

    assert delete_response is not None
    assert delete_response.result == "success"

    # 等待索引完成
    await asyncio.sleep(2)

    # 6. 再次查询子分段列表，验证删除成功
    query_response = await kb_client.segment.query_document_child_segments(
        dataset_id=dataset_id,
        document_id=document_id,
        segment_id=segment_id,
        page=1,
        limit=10,
    )

    assert query_response is not None
    assert query_response.data is not None

    # 验证已删除
    assert not any(str(chunk.id) == child_chunk_id for chunk in query_response.data)
