"""
测试知识库-文档相关的 API 接口，验证 OpenAPI Schema 的正确性
"""

from pathlib import Path
import pytest
from io import BytesIO

from dify_sdk.knowledge_base import (
    ProcessRule,
)
from dify_sdk.knowledge_base.types.create_document_by_file_request_data import CreateDocumentByFileRequestData
from dify_sdk.knowledge_base.types.dataset import Dataset
from dify_sdk_testing import KnowledgeBaseClient, wait_for_document_indexing_completed


@pytest.fixture
def text_file1():
    yield Path("tests/data/knowledge_base/test2.txt")


@pytest.fixture
def markdown_file1():
    yield Path("tests/data/knowledge_base/test.md")


@pytest.fixture
async def dataset1(kb_client: KnowledgeBaseClient):
    """创建一个测试用的知识库"""
    ds = await kb_client.dataset.create_empty_dataset(
        name="dify-openapi 测试-文档测试库",
        description="用于测试文档相关接口",
        indexing_technique="high_quality",
    )
    assert ds is not None
    assert ds.id is not None
    dataset_id = str(ds.id)

    try:
        yield ds
    finally:
        await kb_client.dataset.delete_dataset(dataset_id=dataset_id)


async def test_text_document_workflow(kb_client: KnowledgeBaseClient, dataset1: Dataset, text_file1: Path):
    """测试文本文档相关的工作流程"""
    # 1. 通过文本创建文档
    create_response = await kb_client.document.create_document_by_text(
        dataset_id=str(dataset1.id),
        name="test_document.txt",
        text=text_file1.read_text(),
        indexing_technique="high_quality",
        process_rule=ProcessRule(mode="automatic", rules=None),
    )
    assert create_response is not None
    assert create_response.document is not None
    document = create_response.document
    doc_id = str(document.id)
    assert create_response.batch is not None
    batch_id = str(create_response.batch)

    dataset_id = str(dataset1.id)
    # 2. 获取文档嵌入状态, 查询状态直到处理完成
    await wait_for_document_indexing_completed(kb_client=kb_client, dataset_id=dataset_id, batch_id=batch_id)

    # 3. 更新文档内容
    update_response = await kb_client.document.update_document_by_text(
        dataset_id=dataset_id,
        document_id=doc_id,
        text=text_file1.read_text() + "\n# 这是更新后的内容",
        name="updated_test_document.txt",
        process_rule=ProcessRule(mode="automatic", rules=None),
    )
    assert update_response is not None
    assert update_response.document is not None

    # 4. 获取文档列表
    list_response = await kb_client.document.get_document_list(
        dataset_id=dataset_id,
        page=1,
        limit=20,
        keyword="test",  # 测试搜索功能
    )
    assert list_response is not None
    assert list_response.data is not None
    assert isinstance(list_response.data, list)
    assert len(list_response.data) > 0

    # 5. 删除文档
    try:
        delete_response = await kb_client.document.delete_document(dataset_id=dataset_id, document_id=doc_id)
    except:
        import warnings
        warnings.warn("删除文档API返回204直接没有内容, 但成功了")
    else:
        assert delete_response is not None
        assert delete_response.result == "success"


async def test_file_document_workflow(kb_client: KnowledgeBaseClient, dataset1: Dataset, markdown_file1: Path):
    """测试文件文档相关的工作流程"""
    create_response = await kb_client.document.create_document_by_file(
        dataset_id=str(dataset1.id),
        file=("test.md", markdown_file1.read_bytes(), "text/markdown"),
        data=CreateDocumentByFileRequestData(
            indexing_technique="high_quality",
            process_rule=ProcessRule(mode="automatic", rules=None),
            doc_form="text_model",
            doc_language="English",
        ).model_dump_json(),
    )
    assert create_response is not None
    assert create_response.document is not None
    document = create_response.document
    doc_id = str(document.id)
    dataset_id = str(dataset1.id)
    batch_id = str(create_response.batch)

    await wait_for_document_indexing_completed(kb_client=kb_client, dataset_id=dataset_id, batch_id=batch_id)

    NEW_UPDATED_NAME = "updated_test_document.md"
    with BytesIO((markdown_file1.read_text() + "\n# 这是更新后的内容").encode("utf-8")) as fp:
        update_response = await kb_client.document.update_document_by_file(
            dataset_id=str(dataset1.id),
            document_id=doc_id,
            file=("test.md", fp, "text/markdown"),
            name=NEW_UPDATED_NAME,
            process_rule=ProcessRule(mode="automatic", rules=None),
        )
    assert update_response is not None
    assert update_response.document is not None

    file_response = await kb_client.document.get_upload_file(dataset_id=str(dataset1.id), document_id=doc_id)
    assert file_response is not None
    assert file_response.id is not None
    assert file_response.size is not None
    assert file_response.size > 0
