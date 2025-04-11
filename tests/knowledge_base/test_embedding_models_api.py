"""
测试嵌入模型相关的 API 接口，验证 OpenAPI Schema 的正确性
"""

from dify_sdk_testing import KnowledgeBaseClient


async def test_get_embedding_models(kb_client: KnowledgeBaseClient):
    """测试获取嵌入模型列表"""
    # 以下是正确的测试逻辑，当SDK添加models属性后可以启用
    # 获取嵌入模型列表
    models_response = await kb_client.models.get_embedding_model_list()

    # 验证返回的数据
    assert models_response is not None
    assert models_response.data is not None

    # 验证至少有一个模型提供商
    assert len(models_response.data) > 0

    # 验证模型提供商的结构
    for provider in models_response.data:
        assert provider.provider is not None
        assert provider.label is not None
        assert provider.icon_small is not None
        assert provider.icon_large is not None
        assert provider.status is not None
        assert provider.models is not None

        # 验证模型列表
        assert len(provider.models) > 0

        # 验证模型的结构
        for model in provider.models:
            assert model.model is not None
            assert model.label is not None
            assert model.model_type == "text-embedding"
            assert hasattr(model, "model_properties")

            # 验证模型属性
            if model.model_properties is not None:
                assert hasattr(model.model_properties, "context_size")
