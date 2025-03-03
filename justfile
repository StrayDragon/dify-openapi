set dotenv-required
set dotenv-load

GENERATED_DIR := "src"


default: help


help:
    @echo "`just -l`"


update-fern-schema:
    cp schema/app.en.yaml schema/datasets.en.yaml fern/openapi/

gen-client: apply-i18n-overlay-to-openapi-schema update-fern-schema && tmp-gen-cilent-full
    # TODO: @l8ng remove old generated clients replace with fern (better code implementation)
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

    fern generate --local
    ruff format src/


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


apply-i18n-overlay-to-openapi-schema:
    for name in app datasets; do \
        for lang in en; do \
            npx bump overlay schema/$name.zh.yaml schema/overlays/$name.$lang.overlay.yaml > schema/$name.$lang.yaml; \
        done; \
    done

run-openapi-ui:
    uv run scripts/preview-schema.py


test:
    uv run pytest
