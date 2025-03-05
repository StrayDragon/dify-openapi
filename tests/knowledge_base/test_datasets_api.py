"""
测试数据集API的完整工作流程
"""

from pathlib import Path
import pytest
import asyncio

from dify_sdk import (
    ProcessRule,
    RetrieveDatasetRequestRetrievalModel,
)
from dify_sdk.types.create_document_by_file_request_data import CreateDocumentByFileRequestData
from dify_sdk_testing import KnowledgeBaseClient


@pytest.fixture
def test_text_file():
    """测试用的文本文件"""
    yield Path("tests/data/knowledge_base/test.txt")


@pytest.fixture
def test_pdf_file():
    """测试用的PDF文件"""
    yield Path("tests/data/knowledge_base/test.pdf")


async def test_datasets_workflow(kb_client: KnowledgeBaseClient, test_text_file: Path, test_pdf_file: Path):
    """测试数据集API的完整工作流程"""
    # 1. 创建空数据集
    dataset = await kb_client.dataset.create_empty_dataset(
        name="dify-sdk test dataset",
        description="Test dataset for SDK integration tests",
        indexing_technique="high_quality",
    )
    assert dataset is not None
    assert dataset.id is not None
    dataset_id = str(dataset.id)

    try:
        # 2. 获取数据集列表
        dataset_list = await kb_client.dataset.get_dataset_list(page=1, limit=20)
        assert dataset_list is not None
        assert dataset_list.data is not None
        assert len(dataset_list.data) > 0
        assert any(str(d.id) == dataset_id for d in dataset_list.data)

        # 3. 创建文本文档
        text_doc_response = await kb_client.document.create_document_by_text(
            dataset_id=dataset_id,
            name="test_content.txt",
            text=test_text_file.read_text(),
            indexing_technique="high_quality",
            process_rule=ProcessRule(mode="automatic", rules=None),
        )
        assert text_doc_response is not None
        assert text_doc_response.document is not None
        assert text_doc_response.document.id is not None

        # 4. 创建PDF文档
        req_data = CreateDocumentByFileRequestData(
            indexing_technique="high_quality",
            process_rule=ProcessRule(mode="automatic"),
        ).model_dump_json(exclude_unset=True)
        file_doc_response = await kb_client.document.create_document_by_file(
            dataset_id=dataset_id,
            file=(test_pdf_file.name, test_pdf_file.read_bytes(), "application/pdf"),
            data=req_data,
        )
        assert file_doc_response is not None
        assert file_doc_response.document is not None
        assert file_doc_response.document.id is not None

        # 等待文档被索引
        await asyncio.sleep(5)

        # 5. 测试语义搜索
        semantic_results = await kb_client.dataset.retrieve_dataset(
            dataset_id=dataset_id,
            query="Python API",
            retrieval_model=RetrieveDatasetRequestRetrievalModel(
                search_method="semantic_search",
                top_k=5,
                score_threshold_enabled=True,
                score_threshold=0.5,
                reranking_enable=False,
            ),
        )
        assert semantic_results is not None
        assert semantic_results.query is not None

        # 6. 测试关键词搜索
        keyword_results = await kb_client.dataset.retrieve_dataset(
            dataset_id=dataset_id,
            query="测试",
            retrieval_model=RetrieveDatasetRequestRetrievalModel(
                search_method="keyword_search",
                top_k=5,
                score_threshold_enabled=False,
                reranking_enable=False,
            ),
        )
        assert keyword_results is not None
        assert keyword_results.query is not None

        # 7. 测试全文搜索
        fulltext_results = await kb_client.dataset.retrieve_dataset(
            dataset_id=dataset_id,
            query="test",
            retrieval_model=RetrieveDatasetRequestRetrievalModel(
                search_method="full_text_search",
                top_k=5,
                score_threshold_enabled=False,
                reranking_enable=False,
            ),
        )
        assert fulltext_results is not None
        assert fulltext_results.query is not None

    finally:
        # 8. 删除数据集
        await kb_client.dataset.delete_dataset(dataset_id=dataset_id)
