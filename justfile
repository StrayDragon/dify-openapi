set dotenv-required
set dotenv-load

GENERATED_DIR := "src"


default: help


help:
    @echo "`just -l`"


update-fern-schema:
    cp schema/app.en.yaml schema/knowledge_base.en.yaml fern/openapi/

gen-client: apply-i18n-overlay-to-openapi-schema update-fern-schema
    fern generate --local
    ruff format src/
    bash misc/fern_sdk_hotfix_patch.sh

apply-i18n-overlay-to-openapi-schema:
    for name in app knowledge_base external_knowledge_base; do \
        for lang in en; do \
            echo "=== $name.$lang.yaml ==="; \
            npx bump overlay schema/$name.zh.yaml schema/overlays/$name.$lang.overlay.yaml > schema/$name.$lang.yaml; \
        done; \
    done

run-openapi-ui:
    uv run scripts/preview-schema.py

bump-version-guide:
    @echo "search/replace by vscode,add version to replace and selected match whole word, add files to exclude=> libs/dify,overlays,scripts,uv.lock"

test:
    uv run pytest
