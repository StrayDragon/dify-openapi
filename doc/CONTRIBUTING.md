# Welcome to Contribute!

We warmly welcome your contributions to the Dify x OpenAPI project. Whether fixing bugs, improving documentation, or adding new features, your contributions help us build better tools.

## How to Contribute?

Basic process:
1. Fork this repository and clone it locally
2. Create a new branch for modifications
3. Submit a Pull Request
4. Wait for review and merge

You can refer to the following cases to make contributions!

### Case: Dify 1.0.1 -> 1.1.0

#### I. Research What Changes the Upgrade Produces

Reference code changes:
- dify:
  - [1.0.1__1.1.0.diff](../misc/official_api_doc_changes/1.0.1__1.1.0.diff)
    - Can refer to and use the [Generate Diff Script](../scripts/gen_diff_by_versions.py)
- dify-doc
  - https://github.com/langgenius/dify-docs/pull/563/files

> There was a small easter egg: https://github.com/langgenius/dify/issues/16179

After research, this version upgrade mainly focuses on Knowledge Base APIs, adding 6 new APIs that need new schemas, client (py) SDK generation, and simple test code.

#### II. Make Changes and Test

0. Apply changes to *.zh.yaml files in [schema](../schema) (we use zh.yaml as primary)
1. Translate Chinese descriptions to other languages using files in [schema/overlay](../schema/overlays), like *.en.overlay.yaml. Use `just apply-i18n-overlay-to-openapi-schema` to generate OpenAPI schemas
2. Use `just run-openapi-ui` to open local Swagger UI for testing
3. Generate new client test code: `just gen-client`
4. Write unit tests for new APIs in [test_datasets_api.py](../tests/knowledge_base/test_datasets_api.py) and test with `just test`
5. Update README.(zh).md with relevant changes
6. Submit PR

Each part can be split into subtasks with different git commit messages to track progress.
