"""
测试知识库相关的 API 接口，验证 OpenAPI Schema 的正确性
"""

from pathlib import Path
import pytest

from dify_openapi_datasets.models.create_dataset_request import CreateDatasetRequest
from dify_openapi_datasets.models.create_document_by_text_body import CreateDocumentByTextBody
from dify_openapi_datasets.models.create_document_by_file_body_data import CreateDocumentByFileBodyData
from dify_openapi_datasets.models.process_rule import ProcessRule
from dify_openapi_datasets.models.retrieve_dataset_body import RetrieveDatasetBody
from dify_openapi_datasets.models.retrieve_dataset_body_retrieval_model import RetrieveDatasetBodyRetrievalModel
from dify_openapi_datasets.models.create_document_by_file_body import CreateDocumentByFileBody
from dify_openapi_datasets.types import UNSET, File
from dify_openapi_datasets.api.datasets import (
    create_empty_dataset,
    get_dataset_list,
    retrieve_dataset,
    delete_dataset,
)
from dify_openapi_datasets.api.documents import create_document_by_text, create_document_by_file


@pytest.fixture
def test_text_file():
    yield Path("tests/data/datasets/test.txt")


@pytest.fixture
def test_pdf_file():
    """创建一个测试 PDF 文件"""
    yield Path("tests/data/datasets/test.pdf")


async def test_datasets_workflow(c, test_text_file, test_pdf_file):
    """测试知识库相关的完整工作流程"""
    # 1. 创建空知识库
    dataset_request = CreateDatasetRequest(
        name="dify-openapi 测试-知识库",
        description="用于测试知识库相关接口",
        indexing_technique="high_quality",
    )

    create_response = await create_empty_dataset.asyncio_detailed(client=c.client, body=dataset_request)
    assert create_response is not None
    assert create_response.parsed is not None
    assert create_response.parsed.id is not UNSET
    dataset_id = str(create_response.parsed.id)  # 确保 dataset_id 是字符串类型

    try:
        # 2. 获取知识库列表
        list_response = await get_dataset_list.asyncio_detailed(client=c.client, page=1, limit=20)
        assert list_response is not None
        assert list_response.parsed is not None
        assert list_response.parsed.data is not UNSET
        assert isinstance(list_response.parsed.data, list)
        assert len(list_response.parsed.data) > 0
        assert any(d.id is not UNSET and str(d.id) == dataset_id for d in list_response.parsed.data)

        # 3. 创建文本文档
        doc_request = CreateDocumentByTextBody(
            name="test_content.txt",
            text=test_text_file.read_text(),
            indexing_technique="high_quality",
            process_rule=ProcessRule(mode="automatic"),
        )

        text_doc_response = await create_document_by_text.asyncio_detailed(
            client=c.client,
            dataset_id=dataset_id,
            body=doc_request,
        )
        assert text_doc_response is not None
        assert text_doc_response.parsed is not None

        # 4. 创建 PDF 文档
        file_doc_request = CreateDocumentByFileBody(
            data=CreateDocumentByFileBodyData(
                indexing_technique="high_quality",
                process_rule=ProcessRule(mode="automatic"),
            ),
            file=File(
                payload=test_pdf_file.read_bytes(),
                file_name=test_pdf_file.name,
                mime_type="application/pdf",
            ),
        )

        file_doc_response = await create_document_by_file.asyncio_detailed(
            client=c.client,
            dataset_id=dataset_id,
            body=file_doc_request,
        )
        assert file_doc_response is not None
        assert file_doc_response.parsed is not None

        # 等待文档被索引
        import asyncio

        await asyncio.sleep(5)

        # 5. 检索知识库 - 语义搜索
        semantic_request = RetrieveDatasetBody(
            query="Python API",
            retrieval_model=RetrieveDatasetBodyRetrievalModel(
                search_method="semantic_search",
                top_k=5,
                score_threshold_enabled=True,
                score_threshold=0.5,
                reranking_enable=False,
            ),
        )

        semantic_response = await retrieve_dataset.asyncio_detailed(
            client=c.client, dataset_id=dataset_id, body=semantic_request
        )
        assert semantic_response is not None
        assert semantic_response.parsed is not None

        # 6. 检索知识库 - 关键词搜索
        keyword_request = RetrieveDatasetBody(
            query="测试",
            retrieval_model=RetrieveDatasetBodyRetrievalModel(
                search_method="keyword_search", top_k=5, score_threshold_enabled=False, reranking_enable=False
            ),
        )

        keyword_response = await retrieve_dataset.asyncio_detailed(
            client=c.client, dataset_id=dataset_id, body=keyword_request
        )
        assert keyword_response is not None
        assert keyword_response.parsed is not None

        # 7. 检索知识库 - 全文搜索
        fulltext_request = RetrieveDatasetBody(
            query="test",
            retrieval_model=RetrieveDatasetBodyRetrievalModel(
                search_method="full_text_search", top_k=5, score_threshold_enabled=False, reranking_enable=False
            ),
        )

        fulltext_response = await retrieve_dataset.asyncio_detailed(
            client=c.client, dataset_id=dataset_id, body=fulltext_request
        )
        assert fulltext_response is not None
        assert fulltext_response.parsed is not None

    finally:
        # 8. 删除知识库
        delete_response = await delete_dataset.asyncio_detailed(client=c.client, dataset_id=dataset_id)
        assert delete_response is not None
        assert delete_response.status_code == 204
