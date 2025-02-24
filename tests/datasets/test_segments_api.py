"""
测试知识库-分段相关的 API 接口，验证 OpenAPI Schema 的正确性
"""

import asyncio
from http import HTTPStatus
import pytest

from dify_openapi_datasets.models.create_dataset_request import CreateDatasetRequest
from dify_openapi_datasets.models.create_document_by_text_body import CreateDocumentByTextBody
from dify_openapi_datasets.models.create_segments_body import CreateSegmentsBody
from dify_openapi_datasets.models.create_segments_body_segments_item import CreateSegmentsBodySegmentsItem
from dify_openapi_datasets.models.update_segment_body import UpdateSegmentBody
from dify_openapi_datasets.models.update_segment_body_segment import UpdateSegmentBodySegment
from dify_openapi_datasets.models.process_rule import ProcessRule
from dify_openapi_datasets.types import UNSET
from dify_openapi_datasets.api.datasets import create_empty_dataset, delete_dataset
from dify_openapi_datasets.api.documents import create_document_by_text
from dify_openapi_datasets.api.segments import create_segments, get_segments, update_segment, delete_segment


@pytest.fixture
async def dataset_for_seg1(c):
    """创建一个测试用的知识库"""
    dataset_request = CreateDatasetRequest(
        name="dify-openapi 测试-分段测试库",
        description="用于测试分段相关接口",
        indexing_technique="high_quality",
    )

    create_response = await create_empty_dataset.asyncio_detailed(client=c.client, body=dataset_request)
    assert create_response is not None
    assert create_response.parsed is not None
    dataset = create_response.parsed

    try:
        yield dataset
    finally:
        await delete_dataset.asyncio_detailed(client=c.client, dataset_id=str(dataset.id))


@pytest.fixture
async def document_for_seg1(c, dataset_for_seg1):
    """创建一个测试用的文档"""
    content = """
    # 测试文档

    这是一个用于测试分段功能的文档。

    ## 第一部分
    这是第一个段落，用于测试基本的分段功能。
    包含一些关键词：测试、分段、API。

    ## 第二部分
    这是第二个段落，用于测试分段更新功能。
    我们将测试以下功能：
    1. 创建分段
    2. 更新分段
    3. 删除分段

    ## 第三部分
    这是第三个段落，用于测试高级分段功能。
    包含一些特殊字符：
    * 列表项1
    * 列表项2
    * 列表项3
    """

    doc_request = CreateDocumentByTextBody(
        name="test_segments.md",
        text=content,
        indexing_technique="high_quality",
        process_rule=ProcessRule(mode="automatic"),
    )

    create_response = await create_document_by_text.asyncio_detailed(
        client=c.client, dataset_id=str(dataset_for_seg1.id), body=doc_request
    )
    assert create_response is not None
    assert create_response.parsed is not None
    return create_response.parsed


@pytest.mark.asyncio
async def test_segments_workflow(c, dataset_for_seg1, document_for_seg1):
    """测试分段相关的完整工作流程"""
    # 1. 创建分段 - 文本模式
    text_segments_request = CreateSegmentsBody(
        segments=[
            CreateSegmentsBodySegmentsItem(
                content="这是第一个手动创建的测试分段", keywords=["测试", "分段", "文本"], answer=UNSET
            ),
            CreateSegmentsBodySegmentsItem(
                content="这是第二个手动创建的测试分段", keywords=["测试", "分段", "文本"], answer=UNSET
            ),
        ]
    )

    dataset_id = str(dataset_for_seg1.id)
    document_id = str(document_for_seg1.document.id)

    await asyncio.sleep(5)

    text_create_response = await create_segments.asyncio_detailed(
        client=c.client,
        dataset_id=dataset_id,
        document_id=document_id,
        body=text_segments_request,
    )
    assert text_create_response is not None
    assert text_create_response.parsed is not None

    # 2. 创建分段 - QA 模式
    qa_segments_request = CreateSegmentsBody(
        segments=[
            CreateSegmentsBodySegmentsItem(
                content="什么是分段测试？",
                answer="分段测试是验证文档分段功能的一种测试方法。",
                keywords=["测试", "分段", "QA"],
            ),
            CreateSegmentsBodySegmentsItem(
                content="如何进行分段测试？",
                answer="通过创建、更新、删除分段来验证功能的正确性。",
                keywords=["测试", "方法", "QA"],
            ),
        ]
    )

    qa_create_response = await create_segments.asyncio_detailed(
        client=c.client,
        dataset_id=dataset_id,
        document_id=document_id,
        body=qa_segments_request,
    )
    assert qa_create_response is not None
    assert qa_create_response.parsed is not None

    # 3. 获取分段列表 - 全部
    all_segments_response = await get_segments.asyncio_detailed(
        client=c.client, dataset_id=dataset_id, document_id=document_id
    )
    assert all_segments_response is not None
    assert all_segments_response.parsed is not None
    assert all_segments_response.parsed.data is not UNSET
    assert isinstance(all_segments_response.parsed.data, list)
    assert len(all_segments_response.parsed.data) > 0

    segment = all_segments_response.parsed.data[0]
    segment_id = str(segment.id)

    # 4. 更新分段 - 启用状态和内容
    update_request = UpdateSegmentBody(
        segment=UpdateSegmentBodySegment(
            content="这是更新后的分段内容",
            keywords=["更新", "测试", "分段"],
            answer="这是更新后的答案内容",
            enabled=True,
            regenerate_child_chunks=False,
        )
    )

    update_response = await update_segment.asyncio_detailed(
        client=c.client,
        dataset_id=dataset_id,
        document_id=document_id,
        segment_id=segment_id,
        body=update_request,
    )
    assert update_response is not None
    assert update_response.parsed is not None

    # 5. 更新分段 - 禁用状态
    disable_request = UpdateSegmentBody(
        segment=UpdateSegmentBodySegment(
            content=str(segment.content) if segment.content is not UNSET else "",
            keywords=segment.keywords if segment.keywords is not UNSET else [],
            answer=str(segment.answer) if segment.answer is not UNSET else "",
            enabled=False,
            regenerate_child_chunks=False,
        )
    )

    disable_response = await update_segment.asyncio_detailed(
        client=c.client,
        dataset_id=dataset_id,
        document_id=document_id,
        segment_id=segment_id,
        body=disable_request,
    )
    assert disable_response is not None
    assert disable_response.parsed is not None

    # 6. 删除分段
    delete_response = await delete_segment.asyncio_detailed(
        client=c.client,
        dataset_id=dataset_id,
        document_id=document_id,
        segment_id=segment_id,
    )
    assert delete_response is not None
    assert delete_response.status_code == HTTPStatus.OK
