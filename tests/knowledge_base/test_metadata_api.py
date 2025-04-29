"""
测试知识库元数据API的完整工作流程
"""

from dify_sdk.knowledge_base import (

    UpdateDocumentsMetadataRequestOperationDataItem,
)
from dify_sdk.knowledge_base.types.process_rule import ProcessRule
from dify_sdk_testing import KnowledgeBaseClient, wait_for_document_indexing_completed
from dify_sdk.knowledge_base.metadata.types.update_documents_metadata_request_operation_data_item_metadata_list_item import (
    UpdateDocumentsMetadataRequestOperationDataItemMetadataListItem,
)
from dify_sdk.knowledge_base.types.dataset import Dataset
from dify_sdk.knowledge_base.metadata.types.list_dataset_metadata_response import ListDatasetMetadataResponse
from dify_sdk.knowledge_base.metadata.types.create_metadata_response import CreateMetadataResponse
from dify_sdk.knowledge_base.metadata.types.update_metadata_response import UpdateMetadataResponse


async def test_metadata_workflow(kb_client: KnowledgeBaseClient):
    """测试知识库元数据API的完整工作流程"""
    # 1. 创建空数据集
    dataset: Dataset = await kb_client.dataset.create_empty_dataset(
        name="dify-sdk metadata test dataset",
        description="Test dataset for metadata API integration tests",
        indexing_technique="high_quality",
    )
    assert dataset is not None
    assert dataset.id is not None
    dataset_id = str(dataset.id)

    try:
        # 2. 获取元数据列表 (初始应该为空)
        metadata_list: ListDatasetMetadataResponse = await kb_client.metadata.list_dataset_metadata(
            dataset_id=dataset_id
        )
        assert metadata_list is not None
        assert metadata_list.doc_metadata is not None
        assert len(metadata_list.doc_metadata) == 0

        # 3. 创建自定义元数据字段
        created_metadata: CreateMetadataResponse = await kb_client.metadata.create_metadata(
            dataset_id=dataset_id,
            type="string",
            name="test_metadata",
        )
        assert created_metadata is not None
        assert created_metadata.id is not None
        metadata_id = str(created_metadata.id)

        # 4. 再次获取元数据列表 (应该包含新创建的字段)
        metadata_list = await kb_client.metadata.list_dataset_metadata(dataset_id=dataset_id)
        assert metadata_list is not None
        assert metadata_list.doc_metadata is not None
        assert len(metadata_list.doc_metadata) == 1
        assert metadata_list.doc_metadata[0].name == "test_metadata"
        assert metadata_list.doc_metadata[0].type == "string"

        # 5. 更新元数据字段名称
        updated_metadata: UpdateMetadataResponse = await kb_client.metadata.update_metadata(
            dataset_id=dataset_id,
            metadata_id=metadata_id,
            name="updated_test_metadata",
        )
        assert updated_metadata is not None
        assert updated_metadata.name == "updated_test_metadata"

        # 6. 切换内置元数据
        await kb_client.metadata.toggle_built_in_metadata(
            dataset_id=dataset_id,
            action="enable",
        )

        # 7. 创建一个测试用的知识库文档
        ## 1. 通过文本创建文档
        create_response = await kb_client.document.create_document_by_text(
            dataset_id=dataset_id,
            name="test_document.txt",
            text="test_document_text",
            indexing_technique="high_quality",
            process_rule=ProcessRule(mode="automatic", rules=None),
        )
        assert create_response is not None
        assert create_response.document is not None
        document = create_response.document
        document_id = str(document.id)
        assert create_response.batch is not None
        batch_id = str(create_response.batch)
        ## 2. 获取文档嵌入状态, 查询状态直到处理完成
        await wait_for_document_indexing_completed(kb_client=kb_client, dataset_id=dataset_id, batch_id=batch_id)

        # 8. 更新文档元数据
        operation_data: list[UpdateDocumentsMetadataRequestOperationDataItem] = [
            UpdateDocumentsMetadataRequestOperationDataItem(
                document_id=document_id,
                metadata_list=[
                    UpdateDocumentsMetadataRequestOperationDataItemMetadataListItem(
                        id=metadata_id,
                        name="updated_test_metadata",
                        value="test_value",
                    )
                ],
            )
        ]
        await kb_client.metadata.update_documents_metadata(
            dataset_id=dataset_id,
            operation_data=operation_data,
        )

        # 9. 删除元数据字段
        await kb_client.metadata.delete_metadata(
            dataset_id=dataset_id,
            metadata_id=metadata_id,
        )

        # 10. 最终检查元数据列表 (应该为空)
        final_metadata_list = await kb_client.metadata.list_dataset_metadata(dataset_id=dataset_id)
        assert final_metadata_list is not None
        assert final_metadata_list.doc_metadata is not None
        assert len(final_metadata_list.doc_metadata) == 0

    finally:
        # 11. 清理 - 删除测试数据集
        await kb_client.dataset.delete_dataset(dataset_id=dataset_id)
