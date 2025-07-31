# Dify x OpenAPI

[![Dify Version Support](https://img.shields.io/badge/Support_Dify_Version-1.7.1-blue)](https://github.com/langgenius/dify)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Package Manager: uv](https://img.shields.io/badge/package%20manager-uv-black)](https://github.com/astral-sh/uv)
[![codecov](https://codecov.io/gh/straydragon/dify-openapi/branch/main/graph/badge.svg)](https://codecov.io/gh/straydragon/dify-openapi)


<div align="center">

[English](./README.md) | 中文

</div>

> [!warning]
> 由于 Dify 官方提供了 OpenAPI 支持，本项目将不再维护。详见 https://docs.dify.ai/api-reference/chat/send-chat-message  。你可以从官方文档中"复制" OpenAPI schema（好久没看官方文档, 几分钟前才发现这个新tab...）。

提供 [Dify](https://github.com/langgenius/dify) API 的 OpenAPI Schema，可以使用 [OpenAPI UI](https://github.com/swagger-api/swagger-ui) 预览或使用 [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) 生成客户端

## Swagger UI 在线查看

### 应用 API
- [聊天应用 - SwaggerUI](https://petstore.swagger.io/?url=https://raw.githubusercontent.com/StrayDragon/dify-openapi/refs/heads/main/schema/app_chat.zh.yaml)
- [高级聊天应用 - SwaggerUI](https://petstore.swagger.io/?url=https://raw.githubusercontent.com/StrayDragon/dify-openapi/refs/heads/main/schema/app_advanced_chat.zh.yaml)
- [文本生成应用 - SwaggerUI](https://petstore.swagger.io/?url=https://raw.githubusercontent.com/StrayDragon/dify-openapi/refs/heads/main/schema/app_generation.zh.yaml)
- [工作流应用 - SwaggerUI](https://petstore.swagger.io/?url=https://raw.githubusercontent.com/StrayDragon/dify-openapi/refs/heads/main/schema/app_workflow.zh.yaml)

### 知识库 API
- [知识库 - SwaggerUI](https://petstore.swagger.io/?url=https://raw.githubusercontent.com/StrayDragon/dify-openapi/refs/heads/main/schema/knowledge_base.zh.yaml)
- [外部知识库 - SwaggerUI](https://petstore.swagger.io/?url=https://raw.githubusercontent.com/StrayDragon/dify-openapi/refs/heads/main/schema/external_knowledge_base.zh.yaml)


> [!note]
> 有一些支持 OpenAPI 模式的 Web 用户界面。你可以去看看并按你自己的方式使用它们
> - https://github.com/rapi-doc/RapiDoc


## 接口列表

> [!tip]
> 这里指至少可以通过一次测试用例请求, 如果你发现有哪些API错误, 欢迎提issue或者pr!

- 知识库: [OpenAPI Schema(中文)](./schema/knowledge_base.zh.yaml) | [OpenAPI Schema(English)](./schema/knowledge_base.en.yaml) | [官方文档源码](https://github.com/langgenius/dify/tree/1.7.1/web/app/(commonLayout)/datasets/template)
  - [x] POST /datasets - 创建空知识库
  - [x] POST /datasets/{dataset_id} - 更新知识库
  - [x] GET /datasets/{dataset_id}/documents - 获取文档列表
  - [x] DELETE /datasets/{dataset_id}/documents/{document_id} - 删除文档
  - [x] POST /datasets/{dataset_id}/document/create-by-text - 通过文本创建文档
  - [x] POST /datasets/{dataset_id}/document/create-by-file - 通过文件创建文档
  - [x] PUT /datasets/{dataset_id}/documents/{document_id} - 更新文档
  - [x] POST /datasets/{dataset_id}/documents/{document_id}/update-by-file - 通过文件更新文档
  - [x] GET /datasets/{dataset_id}/documents/{document_id}/upload-file - 获取上传文件
  - [x] GET /datasets/{dataset_id}/documents/{batch}/indexing-status - 获取文档嵌入状态
  - [x] PATCH /datasets/{dataset_id}/documents/status/{action} - 批量更新文档状态
  - [x] GET /datasets/{dataset_id}/documents/{document_id}/segments - 查询文档分段
  - [x] POST /datasets/{dataset_id}/documents/{document_id}/segments - 创建文档分段
  - [x] DELETE /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id} - 删除文档分段
  - [x] POST /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id} - 更新文档分段
  - [x] POST /datasets/{dataset_id}/metadata - 新增元数据
  - [x] GET /datasets/{dataset_id}/metadata - 查询知识库元数据列表
  - [x] PATCH /datasets/{dataset_id}/metadata/{metadata_id} - 更新元数据
  - [x] DELETE /datasets/{dataset_id}/metadata/{metadata_id} - 删除元数据
  - [x] POST /datasets/{dataset_id}/metadata/built-in/{action} - 启用/禁用内置元数据
  - [x] POST /datasets/{dataset_id}/documents/metadata - 更新文档元数据
  - [x] GET /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id} - 查看文档分段详情
  - [x] POST /datasets/tags - 新增知识库类型标签
  - [x] GET /datasets/tags - 获取知识库类型标签
  - [x] PATCH /datasets/tags - 修改知识库类型标签名称
  - [x] DELETE /datasets/tags - 删除知识库类型标签
  - [x] POST /datasets/tags/binding - 绑定知识库到知识库类型标签
  - [x] POST /datasets/tags/unbinding - 解绑知识库和知识库类型标签
  - [x] POST /datasets/{dataset_id}/tags - 查询知识库已绑定的标签
  - [x] POST /datasets/{dataset_id}/retrieval - 带元数据过滤条件的检索

- 聊天应用: [OpenAPI Schema(中文)](./schema/app_chat.zh.yaml) | [OpenAPI Schema(English)](./schema/app_chat.en.yaml) | [官方文档源码](https://github.com/langgenius/dify/tree/1.7.1/web/app/components/develop/template)
  - [x] POST /chat-messages - 发送对话消息
  - [x] POST /files/upload - 上传文件
  - [x] POST /messages/{message_id}/feedbacks - 消息反馈
  - [x] POST /conversations/{conversation_id}/name - 会话重命名
  - [x] DELETE /conversations/{conversation_id} - 删除会话
  - [x] GET /messages - 获取会话历史消息
  - [x] GET /conversations/{conversation_id}/variables - 获取对话变量
  - [x] GET /app/feedbacks - 获取应用反馈
  - [x] GET /site - 获取应用WebApp设置
  - [x] GET /info - 获取应用基本信息
  - [x] GET /parameters - 获取应用参数

- 高级聊天应用: [OpenAPI Schema(中文)](./schema/app_advanced_chat.zh.yaml) | [OpenAPI Schema(English)](./schema/app_advanced_chat.en.yaml) | [官方文档源码](https://github.com/langgenius/dify/tree/1.7.1/web/app/components/develop/template)
  - [x] POST /audio-to-text - 语音转文字
  - [x] POST /text-to-audio - 文字转语音
  - [x] GET /apps/annotations - 获取标注列表
  - [x] POST /apps/annotations - 创建标注
  - [x] PUT /apps/annotations/{annotation_id} - 更新标注
  - [x] DELETE /apps/annotations/{annotation_id} - 删除标注
  - [x] POST /apps/annotation-reply/{action} - 初始化标注回复设置
  - [x] GET /apps/annotation-reply/{action}/status/{job_id} - 检查标注回复设置状态
  - [x] GET /app/feedbacks - 获取应用反馈
  - [x] GET /site - 获取应用WebApp设置
  - [x] GET /conversations/{conversation_id}/variables - 获取对话变量
  - [x] GET /info - 获取应用基本信息
  - [x] GET /parameters - 获取应用参数（包含文字转语音设置）

- 文本生成应用: [OpenAPI Schema(中文)](./schema/app_generation.zh.yaml) | [OpenAPI Schema(English)](./schema/app_generation.en.yaml) | [官方文档源码](https://github.com/langgenius/dify/tree/1.7.1/web/app/components/develop/template)
  - [x] POST /completion-messages - 发送消息

- 工作流应用: [OpenAPI Schema(中文)](./schema/app_workflow.zh.yaml) | [OpenAPI Schema(English)](./schema/app_workflow.en.yaml) | [官方文档源码](https://github.com/langgenius/dify/tree/1.7.1/web/app/components/develop/template)
  - [x] POST /workflows/run - 执行工作流
  - [x] GET /workflows/run/{workflow_run_id} - 获取工作流执行状态
  - [x] POST /workflows/tasks/{task_id}/stop - 停止响应
  - [x] GET /workflows/logs - 获取工作流日志
  - [x] GET /site - 获取应用WebApp设置

- 外部知识库: [OpenAPI Schema(中文)](./schema/external_knowledge_base.zh.yaml) | [OpenAPI Schema(English)](./schema/external_knowledge_base.en.yaml) | [官方文档源码](https://docs.dify.ai/v1.2.0/guides/knowledge-base/external-knowledge-api-documentation)
  - [ ] POST /retrieval - 检索知识内容

## 项目结构

```
.
├── schema/           # OpenAPI schema
├── src/             # 生成的客户端代码
├── tests/           # 通过测试客户端代码, 校验 schema/* 是否正确
└── configs/         # 代码生成器配置
```

## 贡献 & 本地开发

安装这些工具：

- [uv](https://github.com/astral-sh/uv) - Python 包管理器
- [just](https://github.com/casey/just) - 替代 `Makefile`
- [ruff](https://github.com/astral-sh/ruff) - Python 代码格式化和检查工具

更多灵感请参考 [CONTRIBUTING.zh.md](./doc/CONTRIBUTING.zh.md)

### 开发流程

#### 维护单元测试

1. 安装依赖：
```bash
uv venv && uv pip install -e ".[dev]"
```

2. 生成客户端代码：
```bash
just gen-client
```

3. 预览 API 文档：
```bash
just run-openapi-ui
```

4. 编辑环境变量：

```
cp .env.example .env
# 填写相关的变量
```

5. 运行测试：
```bash
just test
```
6. 提交 PR

#### 维护多语言支持

1. 新增/修改语言的 overlay 文件, 例如 `./schema/overlays/app_chat.en.overlay.yaml`
2. 运行 `just apply-i18n-overlay-to-openapi-schema` 生成对应语言的schema (如果是新的语言, 请检查 [justfile](./justfile) 中是否处理了对应的名字)
3. 运行 `just run-openapi-ui` 预览 API 文档
4. 提交 PR


