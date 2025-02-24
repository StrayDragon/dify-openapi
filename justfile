GENERATED_DIR := "src"

default: help

help:
    @echo "`just -l`"

gen-client-by-openapi-generator:
    # clean generated
    rm -rf {{ GENERATED_DIR }}
    # gen code
    uvx openapi-generator-cli generate \
        -i ./schema/datasets.zh.yaml \
        -g python \
        -c configs/openapi-generator-config/datasets.yaml \
        -o {{ GENERATED_DIR }}
    uvx openapi-generator-cli generate \
        -i ./schema/app.zh.yaml \
        -g python \
        -c configs/openapi-generator-config/app.yaml \
        -o {{ GENERATED_DIR }}
    # clean test code stub
    rm -rf {{ GENERATED_DIR }}/dify_openapi_datasets/test
    rm -rf {{ GENERATED_DIR }}/dify_openapi_app/test
    # format code
    ruff format {{ GENERATED_DIR }}run-openapi-ui:

run-openapi-ui:
    uv run scripts/preview-schema.py
