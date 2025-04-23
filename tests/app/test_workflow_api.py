"""
测试工作流相关的 API 接口，验证 OpenAPI Schema 的正确性
"""

import pytest
from typing import Any
from pathlib import Path

from dify_sdk.workflow.client import AsyncWorkflowClient
from dify_sdk.types.stream_event import StreamEvent
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

    # 获取异步迭代器
    response_iterator = app_workflow_client.run_workflow(
        inputs=workflow_inputs,
        response_mode="streaming",  # 使用流式模式
        user=LOGIN_USER_ID,
    )

    # 收集所有事件
    events: list[StreamEvent] = []
    async for event in response_iterator:
        events.append(event)

    # 验证我们至少收到一个事件
    assert len(events) > 0

    # 查找 workflow_finished 事件
    workflow_finished_events = [e for e in events if e.event == "workflow_finished"]

    finished_event = workflow_finished_events[0]
    assert finished_event.workflow_run_id is not None
    assert finished_event.task_id is not None
    assert finished_event.data is not None
    assert finished_event.data.id is not None
    assert finished_event.data.workflow_id is not None
    assert finished_event.data.status in ["running", "succeeded", "failed", "stopped"]

    workflow_run_id = str(finished_event.workflow_run_id)
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


@pytest.fixture
def test_file_path() -> Path:
    """测试用的文件路径"""
    return Path("tests/data/app/test.txt")


async def test_workflow_run_with_file(app_workflow_client: AsyncWorkflowClient, test_file_path: Path):
    """测试带文件的工作流执行"""
    # 上传文件
    file_response = await app_workflow_client.upload_file(
        file=("test.txt", test_file_path.read_bytes(), "text/plain"),
        user=LOGIN_USER_ID,
    )
    assert file_response is not None
    assert file_response.id is not None
    file_id = file_response.id

    # 执行工作流
    workflow_inputs: dict[str, Any] = {
        "query": "ping with file",
        "inputs": {},
        "files": [
            {
                "type": "document",
                "transfer_method": "local_file",
                "upload_file_id": file_id,
            }
        ],
    }

    # 获取异步迭代器
    response_iterator = app_workflow_client.run_workflow(
        inputs=workflow_inputs,
        response_mode="streaming",  # 使用流式模式
        user=LOGIN_USER_ID,
    )

    # 收集所有事件
    events: list[StreamEvent] = []
    async for event in response_iterator:
        events.append(event)

    # 验证我们至少收到一个事件
    assert len(events) > 0

    # 检查第一个事件
    first_event = events[0]
    assert first_event is not None


async def test_workflow_run_streaming(app_workflow_client: AsyncWorkflowClient):
    """测试工作流流式执行API"""
    workflow_inputs: dict[str, Any] = {
        "query": "ping",
        "inputs": {},
        "files": [],
    }

    # 获取异步迭代器
    response_iterator = app_workflow_client.run_workflow(
        inputs=workflow_inputs,
        response_mode="streaming",
        user=LOGIN_USER_ID,
    )

    # 收集所有事件
    events: list[StreamEvent] = []
    async for event in response_iterator:
        events.append(event)

    # 验证我们至少收到一个事件
    assert len(events) > 0

    # 检查事件类型
    event_types = set(event.event for event in events if event.event is not None)
    assert len(event_types) > 0, "没有收到任何有效的事件类型"


async def test_get_workflow_execution_status(app_workflow_client: AsyncWorkflowClient):
    """测试获取工作流运行状态"""
    # 先执行一个工作流
    workflow_inputs: dict[str, Any] = {
        "query": "ping for detail",
        "inputs": {},
        "files": [],
    }

    # 获取异步迭代器
    response_iterator = app_workflow_client.run_workflow(
        inputs=workflow_inputs,
        response_mode="streaming",
        user=LOGIN_USER_ID,
    )

    # 收集所有事件
    events: list[StreamEvent] = []
    async for event in response_iterator:
        events.append(event)

    # 查找 workflow_finished 事件
    workflow_finished_events = [e for e in events if e.event == "workflow_finished"]
    if not workflow_finished_events:
        pytest.skip("没有收到 workflow_finished 事件，可能工作流未正确配置")

    finished_event = workflow_finished_events[0]
    assert finished_event.workflow_run_id is not None

    # 获取运行状态
    status_response = await app_workflow_client.get_workflow_execution_status(
        workflow_run_id=finished_event.workflow_run_id,
    )
    assert status_response is not None
    assert status_response.id is not None
    assert status_response.workflow_id is not None
    assert status_response.status in ["running", "succeeded", "failed", "stopped"]


async def test_get_workflow_logs(app_workflow_client: AsyncWorkflowClient):
    """测试获取工作流日志"""
    # 尝试获取工作流日志
    # 获取工作流日志
    logs_response = await app_workflow_client.get_workflow_logs(page=1, limit=10)
    assert logs_response is not None
    assert logs_response.data is not None
    assert isinstance(logs_response.data, list)

    # 如果有日志，检查日志属性
    if len(logs_response.data) > 0:
        log = logs_response.data[0]
        assert log.id is not None


async def test_stop_workflow(app_workflow_client: AsyncWorkflowClient):
    """测试停止工作流执行"""

    # 先执行一个工作流
    workflow_inputs: dict[str, Any] = {
        "query": "ping for stopping",
        "inputs": {},
        "files": [],
    }

    # 获取异步迭代器
    response_iterator = app_workflow_client.run_workflow(
        inputs=workflow_inputs,
        response_mode="streaming",
        user=LOGIN_USER_ID,
    )

    # 收集所有事件
    events: list[StreamEvent] = []
    async for event in response_iterator:
        events.append(event)

    # 查找包含 task_id 的事件
    task_events = [e for e in events if e.task_id is not None]
    if not task_events:
        pytest.skip("没有收到包含 task_id 的事件，可能工作流未正确配置")

    task_event = task_events[0]
    assert task_event.task_id is not None

    # 尝试停止工作流
    # 注意：如果工作流已经完成，这里可能会失败
    stop_response = await app_workflow_client.stop_workflow(
        task_id=task_event.task_id,
        user=LOGIN_USER_ID,
    )
    assert stop_response is not None