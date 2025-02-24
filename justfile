set dotenv-required
set dotenv-load

GENERATED_DIR := "src"

default: help

help:
    @echo "`just -l`"

# NOTE: openapi-generator-cli is deprecated, use openapi-python-client instead, due to buggy client generation
# gen-client-by-openapi-generator:
#     # clean generated
#     rm -rf {{ GENERATED_DIR }}
#     # gen code
#     uvx openapi-generator-cli generate \
#         -i ./schema/datasets.zh.yaml \
#         -g python \
#         -c configs/openapi-generator-config/datasets.yaml \
#         -o {{ GENERATED_DIR }}
#     rm -rf {{ GENERATED_DIR }}/dify_openapi_datasets/test
#     uvx openapi-generator-cli generate \
#         -i ./schema/app.zh.yaml \
#         -g python \
#         -c configs/openapi-generator-config/app.yaml \
#         -o {{ GENERATED_DIR }}
#     rm -rf {{ GENERATED_DIR }}/dify_openapi_app/test
#     # format code
#     ruff format {{ GENERATED_DIR }}


gen-client: && tmp-gen-cilent-full
    rm -rf {{ GENERATED_DIR }}/dify_openapi_datasets
    mkdir -p {{ GENERATED_DIR }}/dify_openapi_datasets
    uvx openapi-python-client generate \
        --path schema/datasets.zh.yaml \
        --output-path {{ GENERATED_DIR }}/dify_openapi_datasets \
        --meta none \
        --config configs/openapi-python-client/config.yaml \
        --custom-template-path=configs/openapi-python-client/templates \
        --overwrite
    rm -rf {{ GENERATED_DIR }}/dify_openapi_app
    mkdir -p {{ GENERATED_DIR }}/dify_openapi_app
    uvx openapi-python-client generate \
        --path schema/app.zh.yaml \
        --output-path {{ GENERATED_DIR }}/dify_openapi_app \
        --meta none \
        --config configs/openapi-python-client/config.yaml \
        --custom-template-path=configs/openapi-python-client/templates \
        --overwrite

tmp-gen-cilent-full:
    mkdir -p .tmp/dify_openapi_datasets
    uvx openapi-python-client generate \
        --path schema/datasets.zh.yaml \
        --output-path .tmp/dify_openapi_datasets \
        --config configs/openapi-python-client/config.yaml \
        --custom-template-path=configs/openapi-python-client/templates \
        --overwrite
    cp .tmp/dify_openapi_datasets/README.md src/dify_openapi_datasets/README.md
    mkdir -p .tmp/dify_openapi_app
    uvx openapi-python-client generate \
        --path schema/app.zh.yaml \
        --output-path .tmp/dify_openapi_app \
        --config configs/openapi-python-client/config.yaml \
        --custom-template-path=configs/openapi-python-client/templates \
        --overwrite
    cp .tmp/dify_openapi_app/README.md src/dify_openapi_app/README.md



run-openapi-ui:
    uv run scripts/preview-schema.py


test:
    uv run pytest
