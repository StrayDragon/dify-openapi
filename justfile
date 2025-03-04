set dotenv-required
set dotenv-load

GENERATED_DIR := "src"


default: help


help:
    @echo "`just -l`"


update-fern-schema:
    cp schema/app.en.yaml schema/datasets.en.yaml fern/openapi/

gen-client: apply-i18n-overlay-to-openapi-schema update-fern-schema
    fern generate --local
    ruff format src/
    bash misc/fern_sdk_hotfix_patch.sh

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
