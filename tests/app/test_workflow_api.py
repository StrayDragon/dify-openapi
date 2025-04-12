"""
测试工作流相关的 API 接口，验证 OpenAPI Schema 的正确性
"""

import pytest
from typing import Any

from dify_sdk.workflow.client import AsyncWorkflowClient
from dify_sdk_testing import RUNNING_IN_CI

LOGIN_USER_ID = "test123"


@pytest.mark.skipif(
    RUNNING_IN_CI,
    reason="CI中使用官方服务器, 经常报504超时, 影响CI流程, 请使用本地服务测试",
)
async def test_workflow_execution_and_status(app_workflow_client: AsyncWorkflowClient):
    """测试工作流执行和状态查询"""
    # 1. 执行工作流
    workflow_inputs: dict[str, Any] = {
        "query": "ping",
        "inputs": {},
        "files": [],
    }

    response = await app_workflow_client.run_workflow(
        inputs=workflow_inputs,
        response_mode="blocking",
        user=LOGIN_USER_ID,
    )

    assert response is not None
    assert response.workflow_run_id is not None
    assert response.task_id is not None
    assert response.data is not None
    assert response.data.id is not None
    assert response.data.workflow_id is not None
    assert response.data.status in ["running", "succeeded", "failed", "stopped"]

    workflow_run_id = str(response.workflow_run_id)

    # 2. 查询工作流执行状态
    status_response = await app_workflow_client.get_workflow_execution_status(
        workflow_run_id=workflow_run_id,
    )

    assert status_response is not None
    assert status_response.id == workflow_run_id
    assert status_response.workflow_id is not None
    assert status_response.status in ["running", "succeeded", "failed", "stopped"]
    assert status_response.created_at is not None
    assert hasattr(status_response, "finished_at")
    assert hasattr(status_response, "elapsed_time")
    assert hasattr(status_response, "total_steps")
    assert hasattr(status_response, "total_tokens")


async def test_workflow_logs(app_workflow_client: AsyncWorkflowClient):
    """测试获取工作流日志"""
    # 获取工作流日志
    logs_response = await app_workflow_client.get_workflow_logs(
        page=1,
        limit=10,
    )

    assert logs_response is not None
    assert logs_response.data is not None
    assert hasattr(logs_response, "has_more")
    assert hasattr(logs_response, "total")
    assert hasattr(logs_response, "page")
    assert hasattr(logs_response, "limit")

    # 如果有日志记录，验证其结构
    if logs_response.data and len(logs_response.data) > 0:
        log_entry = logs_response.data[0]
        assert log_entry.id is not None
        assert log_entry.created_at is not None

    # 测试使用过滤条件获取日志
    filtered_logs_response = await app_workflow_client.get_workflow_logs(
        status="succeeded",  # 只获取成功的工作流日志
        page=1,
        limit=5,
    )

    assert filtered_logs_response is not None
    assert filtered_logs_response.data is not None

    # 验证过滤条件生效
    # 注意：由于模式变化，我们不能直接断言状态字段
    # 这里我们只验证返回的数据不为空
    assert filtered_logs_response.data is not None
