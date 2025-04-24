# Dify x OpenAPI

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Package Manager: uv](https://img.shields.io/badge/package%20manager-uv-black)](https://github.com/astral-sh/uv)
[![codecov](https://codecov.io/gh/straydragon/dify-openapi/branch/main/graph/badge.svg)](https://codecov.io/gh/straydragon/dify-openapi)


<div align="center">

English | [中文](./README.zh.md)

</div>

Provides OpenAPI Schema for [Dify](https://github.com/langgenius/dify) API, which can be previewed using [OpenAPI UI](https://github.com/swagger-api/swagger-ui) or used to generate clients with [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator)

## Swagger UI Preview online

### Application APIs
- [Chat Application - SwaggerUI(English)](https://petstore.swagger.io/?url=https://raw.githubusercontent.com/StrayDragon/dify-openapi/refs/heads/main/schema/app_chat.en.yaml)
- [Advanced Chat Application - SwaggerUI(English)](https://petstore.swagger.io/?url=https://raw.githubusercontent.com/StrayDragon/dify-openapi/refs/heads/main/schema/app_advanced_chat.en.yaml)
- [Text Generation Application - SwaggerUI(English)](https://petstore.swagger.io/?url=https://raw.githubusercontent.com/StrayDragon/dify-openapi/refs/heads/main/schema/app_generation.en.yaml)
- [Workflow Application - SwaggerUI(English)](https://petstore.swagger.io/?url=https://raw.githubusercontent.com/StrayDragon/dify-openapi/refs/heads/main/schema/app_workflow.en.yaml)

### Knowledge Base APIs
- [Knowledge Base - SwaggerUI(English)](https://petstore.swagger.io/?url=https://raw.githubusercontent.com/StrayDragon/dify-openapi/refs/heads/main/schema/knowledge_base.en.yaml)
- [External Knowledge - SwaggerUI(English)](https://petstore.swagger.io/?url=https://raw.githubusercontent.com/StrayDragon/dify-openapi/refs/heads/main/schema/external_knowledge_base.en.yaml)

> [!note]
> There are some web UIs that support OpenAPI schema. You can take a look and use them in your way
> - https://github.com/rapi-doc/RapiDoc

## API List

> [!tip]
> This indicates that the API has passed at least one test case request. If you find any API errors, feel free to submit an issue or PR!

- Knowledge Base: [OpenAPI Schema(中文)](./schema/knowledge_base.zh.yaml) | [OpenAPI Schema(English)](./schema/knowledge_base.en.yaml) | [Official Documentation Source](https://github.com/langgenius/dify/tree/1.3.0/web/app/(commonLayout)/datasets/template)
  - [x] POST /datasets - Create empty knowledge base
  - [x] POST /datasets/{dataset_id} - Update knowledge base
  - [x] GET /datasets/{dataset_id}/documents - Get document list
  - [x] DELETE /datasets/{dataset_id}/documents/{document_id} - Delete document
  - [x] POST /datasets/{dataset_id}/document/create-by-text - Create document by text
  - [x] POST /datasets/{dataset_id}/document/create-by-file - Create document by file
  - [x] PUT /datasets/{dataset_id}/documents/{document_id} - Update document
  - [x] POST /datasets/{dataset_id}/documents/{document_id}/update-by-file - Update document by file
  - [x] GET /datasets/{dataset_id}/documents/{document_id}/upload-file - Get upload file
  - [x] GET /datasets/{dataset_id}/documents/{batch}/indexing-status - Get document embedding status
  - [x] GET /datasets/{dataset_id}/documents/{document_id}/segments - Query document segments
  - [x] POST /datasets/{dataset_id}/documents/{document_id}/segments - Create document segment
  - [x] DELETE /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id} - Delete document segment
  - [x] POST /datasets/{dataset_id}/documents/{document_id}/segments/{segment_id} - Update document segment
  - [x] POST /datasets/{dataset_id}/metadata - Create metadata
  - [x] GET /datasets/{dataset_id}/metadata - List dataset metadata
  - [x] PATCH /datasets/{dataset_id}/metadata/{metadata_id} - Update metadata
  - [x] DELETE /datasets/{dataset_id}/metadata/{metadata_id} - Delete metadata
  - [x] POST /datasets/{dataset_id}/metadata/built-in/{action} - Enable/disable built-in metadata
  - [x] POST /datasets/{dataset_id}/documents/metadata - Update document metadata

- Chat Application: [OpenAPI Schema(中文)](./schema/app_chat.zh.yaml) | [OpenAPI Schema(English)](./schema/app_chat.en.yaml) | [Official Documentation Source](https://github.com/langgenius/dify/tree/1.3.0/web/app/components/develop/template)
  - [x] POST /chat-messages - Send conversation message
  - [x] POST /files/upload - Upload file
  - [x] POST /messages/{message_id}/feedbacks - Message feedback
  - [x] POST /conversations/{conversation_id}/name - Rename conversation
  - [x] DELETE /conversations/{conversation_id} - Delete conversation
  - [x] GET /messages - Get conversation history messages
  - [x] GET /info - Get application basic information
  - [x] GET /parameters - Get application parameters

- Advanced Chat Application: [OpenAPI Schema(中文)](./schema/app_advanced_chat.zh.yaml) | [OpenAPI Schema(English)](./schema/app_advanced_chat.en.yaml) | [Official Documentation Source](https://github.com/langgenius/dify/tree/1.3.0/web/app/components/develop/template)
  - [x] POST /audio-to-text - Speech to text
  - [x] POST /text-to-audio - Text to speech
  - [x] GET /apps/annotations - Get annotation list
  - [x] POST /apps/annotations - Create annotation
  - [x] PUT /apps/annotations/{annotation_id} - Update annotation
  - [x] DELETE /apps/annotations/{annotation_id} - Delete annotation
  - [x] POST /apps/annotation-reply/{action} - Initialize annotation reply settings
  - [x] GET /apps/annotation-reply/{action}/status/{job_id} - Check annotation reply settings status

- Text Generation Application: [OpenAPI Schema(中文)](./schema/app_generation.zh.yaml) | [OpenAPI Schema(English)](./schema/app_generation.en.yaml) | [Official Documentation Source](https://github.com/langgenius/dify/tree/1.3.0/web/app/components/develop/template)
  - [x] POST /completion-messages - Send message

- Workflow Application: [OpenAPI Schema(中文)](./schema/app_workflow.zh.yaml) | [OpenAPI Schema(English)](./schema/app_workflow.en.yaml) | [Official Documentation Source](https://github.com/langgenius/dify/tree/1.3.0/web/app/components/develop/template)
  - [x] POST /workflows/run - Execute workflow
  - [x] GET /workflows/run/{workflow_run_id} - Get workflow execution status
  - [x] POST /workflows/tasks/{task_id}/stop - Stop response
  - [x] GET /workflows/logs - Get workflow logs

- External Knowledge: [OpenAPI Schema(中文)](./schema/external_knowledge_base.zh.yaml) | [OpenAPI Schema(English)](./schema/external_knowledge_base.en.yaml) | [Official Documentation Source](https://docs.dify.ai/v1.2.0/guides/knowledge-base/external-knowledge-api-documentation)
  - [ ] POST /retrieval - Retrieve knowledge content

## Project Structure

```
.
├── schema/           # OpenAPI schema
├── src/             # Generated client code
├── tests/           # Test client code to verify schema/* correctness
└── configs/         # Code generator configuration
```

## Contribution & Local Development

Install these tools:

- [uv](https://github.com/astral-sh/uv) - Python package manager
- [just](https://github.com/casey/just) - Alternative to `Makefile`
- [ruff](https://github.com/astral-sh/ruff) - Python code formatting and checking tool

See [CONTRIBUTING.md](./doc/CONTRIBUTING.md) for more inspiration

### Development Process

#### Maintaining Unit Tests

1. Install dependencies:
```bash
uv venv && uv pip install -e ".[dev]"
```

2. Generate client code:
```bash
just gen-client
```

3. Preview API documentation:
```bash
just run-openapi-ui
```

4. Edit environment variables:

```
cp .env.example .env
# Fill in the relevant variables
```

5. Run tests:
```bash
just test
```
6. Submit PR

#### Maintaining Multilingual Support

1. Add a language overlay file, e.g., `./schema/overlays/app_chat.en.overlay.yaml`
2. Run `just apply-i18n-overlay-to-openapi-schema` to generate the corresponding language schema (if it is a new language, please check if it is handled in [justfile](./justfile))
3. Run `just run-openapi-ui` to preview API documentation
4. Submit PR
