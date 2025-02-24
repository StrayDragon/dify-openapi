"""
测试知识库-文档相关的 API 接口，验证 OpenAPI Schema 的正确性
"""

import asyncio
from http import HTTPStatus
import os
from pathlib import Path
import pytest
from io import BytesIO
from typing import cast

from dify_openapi_datasets.models.create_dataset_request import CreateDatasetRequest
from dify_openapi_datasets.models.create_document_by_text_body import CreateDocumentByTextBody
from dify_openapi_datasets.models.update_document_by_text_body import UpdateDocumentByTextBody
from dify_openapi_datasets.models.process_rule import ProcessRule
from dify_openapi_datasets.models.create_document_by_file_body import CreateDocumentByFileBody
from dify_openapi_datasets.models.create_document_by_file_body_data import CreateDocumentByFileBodyData
from dify_openapi_datasets.models.update_document_by_file_body import UpdateDocumentByFileBody
from dify_openapi_datasets.models.document import Document
from dify_openapi_datasets.types import UNSET, File
from dify_openapi_datasets.api.datasets import create_empty_dataset, delete_dataset
from dify_openapi_datasets.api.documents import (
    create_document_by_text,
    create_document_by_file,
    get_document_indexing_status,
    update_document_by_text,
    get_document_list,
    delete_document,
    get_upload_file,
)


@pytest.fixture
def text_file1():
    yield Path("tests/data/datasets/test2.txt")


@pytest.fixture
def markdown_file1():
    yield Path("tests/data/datasets/test.md")


@pytest.fixture
async def dataset1(c):
    """创建一个测试用的知识库"""
    dataset_request = CreateDatasetRequest(
        name="dify-openapi 测试-文档测试库",
        description="用于测试文档相关接口",
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


async def test_text_document_workflow(c, dataset1, text_file1):
    """测试文本文档相关的工作流程"""
    # 1. 通过文本创建文档
    doc_request = CreateDocumentByTextBody(
        name="test_document.txt",
        text=text_file1.read_text(),
        indexing_technique="high_quality",
        process_rule=ProcessRule(mode="automatic"),
    )

    create_response = await create_document_by_text.asyncio_detailed(
        client=c.client, dataset_id=str(dataset1.id), body=doc_request
    )
    assert create_response is not None
    assert create_response.status_code == HTTPStatus.OK
    assert create_response.parsed is not None
    assert create_response.parsed.document is not UNSET
    document = cast(Document, create_response.parsed.document)
    doc_id = str(document.id)
    assert create_response.parsed.batch is not UNSET
    batch_id = str(create_response.parsed.batch)

    # 2. 获取文档嵌入状态
    status_response = await get_document_indexing_status.asyncio_detailed(
        client=c.client,
        dataset_id=str(dataset1.id),
        batch=batch_id,
    )
    assert status_response is not None
    assert status_response.parsed is not None

    # 等待几秒，确保文档处理完成
    await asyncio.sleep(5)

    # 3. 更新文档内容
    update_request = UpdateDocumentByTextBody(
        text=text_file1.read_text() + "\n# 这是更新后的内容",
        name="updated_test_document.txt",
        process_rule=ProcessRule(mode="automatic"),
    )
    update_response = await update_document_by_text.asyncio_detailed(
        client=c.client,
        dataset_id=str(dataset1.id),
        document_id=doc_id,
        body=update_request,
    )
    assert update_response is not None
    assert update_response.parsed is not None

    # 4. 获取文档列表
    list_response = await get_document_list.asyncio_detailed(
        client=c.client,
        dataset_id=str(dataset1.id),
        page=1,
        limit=20,
        keyword="test",  # 测试搜索功能
    )
    assert list_response is not None
    assert list_response.parsed is not None
    assert list_response.parsed.data is not UNSET
    assert isinstance(list_response.parsed.data, list)
    assert len(list_response.parsed.data) > 0

    # 5. 删除文档
    delete_response = await delete_document.asyncio_detailed(
        client=c.client, dataset_id=str(dataset1.id), document_id=doc_id
    )
    assert delete_response is not None
    assert delete_response.status_code == HTTPStatus.OK


async def test_file_document_workflow(c, dataset1, markdown_file1):
    """测试文件文档相关的工作流程"""
    # 1. 通过文件创建文档
    with open(markdown_file1, "rb") as f:
        file_content = f.read()
        file_doc_request = CreateDocumentByFileBody(
            file=File(
                payload=BytesIO(file_content),
                file_name=os.path.basename(markdown_file1),
                mime_type="text/markdown",
            ),
            data=CreateDocumentByFileBodyData(
                indexing_technique="high_quality",
                process_rule=ProcessRule(mode="automatic"),
            ),
        )

        create_response = await create_document_by_file.asyncio_detailed(
            client=c.client, dataset_id=str(dataset1.id), body=file_doc_request
        )
        assert create_response is not None
        assert create_response.parsed is not None
        assert create_response.parsed.document is not UNSET
        document = cast(Document, create_response.parsed.document)
        doc_id = str(document.id)

    # 2. 更新文档内容 # FIXME: @l8ng 上游有bug，暂时跳过
    # with open(markdown_file1, "rb") as f:
    #     file_content = f.read()
    #     update_request = UpdateDocumentByFileBody(
    #         file=File(
    #             payload=BytesIO(file_content),
    #             file_name="updated_test_document.md",
    #             mime_type="text/markdown",
    #         ),
    #         name="updated_test_document.md",
    #         process_rule=ProcessRule(mode="automatic"),
    #     )

    #     update_response = await update_document_by_file.asyncio_detailed(
    #         client=client2.client, dataset_id=str(dataset1.id), document_id=doc_id, body=update_request
    #     )
    #     assert update_response is not None
    #     assert update_response.parsed is not None

    # 3. 获取上传文件
    file_response = await get_upload_file.asyncio_detailed(
        client=c.client, dataset_id=str(dataset1.id), document_id=doc_id
    )
    assert file_response is not None
    assert file_response.parsed is not None
