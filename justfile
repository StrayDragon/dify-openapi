set dotenv-required
set dotenv-load

# extra .env.* can be used for local development
# NOTE: if you using VSCode, you can also set in .vscode/settings.json :
# {   ...
#     "python.envFile":"${workspaceFolder}/.env.local"
# }
# set dotenv-filename := '.env.local'

GENERATED_DIR := "src"


default: help


help:
    @echo "`just -l`"


gen-client: apply-i18n-overlay-to-openapi-schema
    rm -rf src/dify_sdk
    fern generate --local
    ruff format src/
    uv run misc/fern_sdk_hotfix_patch.py
    # bash misc/fern_sdk_hotfix_patch.sh

# bump from bump-cli using this cmd to global install `npm install -g bump-cli`
apply-i18n-overlay-to-openapi-schema: && check-i18n-openapi-schema
    for name in app_generation app_chat app_advanced_chat app_workflow knowledge_base external_knowledge_base; do \
        for lang in en; do \
            echo "=== $name.$lang.yaml ==="; \
            npx bump overlay schema/$name.zh.yaml schema/overlays/$name.$lang.overlay.yaml > schema/$name.$lang.yaml; \
        done; \
    done


check-i18n-openapi-schema:
    for name in app_generation app_chat app_advanced_chat app_workflow knowledge_base external_knowledge_base; do \
        for lang in en; do \
            ./scripts/detect-chinese-char-in-files.py schema/$name.$lang.yaml; \
        done; \
    done

run-openapi-ui:
    uv run scripts/preview-schema.py

bump-version-guide:
    @echo "search/replace by vscode,add version to replace and selected match whole word, add files to exclude=> libs/dify,overlays,scripts,uv.lock"

test *pattern='':
    #!/usr/bin/env bash
    if [ -z "{{pattern}}" ]; then
        uv run pytest
    else
        uv run pytest {{pattern}}
    fi
