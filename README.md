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

- [Chat Application (Aggregated) - SwaggerUI(English)](https://petstore.swagger.io/?url=https://raw.githubusercontent.com/StrayDragon/dify-openapi/refs/heads/main/schema/app.en.yaml)
- [Knowledge Base - SwaggerUI(English)](https://petstore.swagger.io/?url=https://raw.githubusercontent.com/StrayDragon/dify-openapi/refs/heads/main/schema/knowledge_base.en.yaml)
- [External Knowledge - SwaggerUI(English)](https://petstore.swagger.io/?url=https://raw.githubusercontent.com/StrayDragon/dify-openapi/refs/heads/main/schema/external_knowledge_base.en.yaml)

## API List

> [!tip]
> This indicates that the API has passed at least one test case request. If you find any API errors, feel free to submit an issue or PR!

- Knowledge Base: [OpenAPI Schema(中文)](../schema/knowledge_base.zh.yaml) | [OpenAPI Schema(English)](../schema/knowledge_base.en.yaml) | [Official Documentation Source](https://github.com/langgenius/dify/tree/1.0.0/web/app/(commonLayout)/datasets/template)
  - [x] POST /datasets - Create empty knowledge base
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

- Chat Application (Aggregated): [OpenAPI Schema(中文)](../schema/app.zh.yaml) | [OpenAPI Schema(English)](../schema/app.en.yaml) | [Official Documentation Source](https://github.com/langgenius/dify/tree/1.0.0/web/app/components/develop/template)
  - [x] POST /completion-messages - Send message (text generation application)
  - [x] POST /chat-messages - Send conversation message (conversation application)
  - [x] POST /workflows/run - Execute workflow (workflow application)
  - [x] POST /files/upload - Upload file
  - [x] POST /messages/{message_id}/feedbacks - Message feedback
  - [x] POST /conversations/{conversation_id}/name - Rename conversation
  - [x] DELETE /conversations/{conversation_id} - Delete conversation
  - [x] GET /messages - Get conversation history messages
  - [x] GET /info - Get application basic information
  - [x] GET /parameters - Get application parameters
  - [x] POST /audio-to-text - Speech to text
  - [x] POST /text-to-audio - Text to speech

- External Knowledge: [OpenAPI Schema(中文)](../schema/external_knowledge_base.zh.yaml) | [OpenAPI Schema(English)](../schema/external_knowledge_base.en.yaml) | [Official Documentation Source](https://docs.dify.ai/guides/knowledge-base/external-knowledge-api-documentation)
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

1. Add a language overlay file, e.g., `./schema/overlays/app.en.overlay.yaml`
2. Run `just apply-i18n-overlay-to-openapi-schema` to generate the corresponding language schema (if it is a new language, please check if it is handled in [justfile](./justfile))
3. Run `just run-openapi-ui` to preview API documentation
4. Submit PR
