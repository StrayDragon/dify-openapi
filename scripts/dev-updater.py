#!/bin/uv run
"""
生成喂给LLM的prompt, 用于修改/更新schema等

同时提供自动化生成新变动schema的代码工作流
"""

import os
from pathlib import Path
import subprocess
import argparse

PROJECT_ROOT = Path(__file__).parent.parent

APP_DOC_PATH_PREFIX = "libs/dify/web/app/components/develop/template"
KB_DOC_PATH_PREFIX = "libs/dify/web/app/(commonLayout)/datasets/template"

LOCAL_SCHEMA_PATH__UPSTREAM_MDX_DOC_PATH = {
    "schema/app_generation.zh.yaml": "/template.zh.mdx",
    "schema/app_advanced_chat.zh.yaml": "/template_advanced_chat.zh.mdx",
    "schema/app_chat.zh.yaml": "/template_chat.zh.mdx",
    "schema/app_workflow.zh.yaml": "/template_workflow.zh.mdx",
    "schema/knowledge_base.zh.yaml": "/template.zh.mdx",
}

SCHEMA_OVERLAY_PATH_PREFIX = "schema/overlays"

LOCAL_SCHEMA_PATH__OVERLAY_EN_PATH = {
    "schema/app_generation.zh.yaml": "/app_generation.en.overlay.yaml",
    "schema/app_advanced_chat.zh.yaml": "/app_advanced_chat.en.overlay.yaml",
    "schema/app_chat.zh.yaml": "/app_chat.en.overlay.yaml",
    "schema/app_workflow.zh.yaml": "/app_workflow.en.overlay.yaml",
    "schema/knowledge_base.zh.yaml": "/knowledge_base.en.overlay.yaml",
}


class Clipboard:
    def copy(self, text: str):
        if not os.environ.get("XDG_SESSION_TYPE") == "wayland":
            raise NotImplementedError()
        # use `wl-copy <text>` to copy the text to clipboard
        subprocess.run(["wl-copy", text])


CB = Clipboard()


def schema_upgrade_prompt(v1: str, v2: str):
    diff_file_path = f"misc/official_api_doc_changes/{v1}__{v2}.diff"
    """原始方法：生成用于手动更新schema的提示"""
    prompt_pattern = """
You are a expert coder and api doc maintainer, master on openapi schema writing and can read and understand mdx doc, you task is based on  mdx doc @{dify_mdx_doc} , then check/fix/update this openapi schema @{schema_path}, make a plan to finish this task, and try your best to done, then check and adjust the english overlay file @{schema_overlay_en_path}

After done, try to use `just apply-i18n-overlay-to-openapi-schema` to generate the corresponding language schema, you need read the last part of command output to check the overlay work well, if has any problems, try to fix and repeat this process until no error report

Except for the just commands permitted by me above, please DO NOT run any other commands (like `just test` or `just gen-client`). Once everything is completed, please provide a brief summary report.

NOTE:
- If you want to invoke `filesystem` tool or something like tools, i tell you some current working directory info:
  - Project root: {PROJECT_ROOT}
- Prefer using increasing edit mode to adjust code, if you got large context write problem, try using another way to finish
- Another helpful context is a preset diff file between {v1} to {v2} change, you can find it in {diff_file_path}
""".strip()
    for local_schema_path, upstream_mdx_doc_path in LOCAL_SCHEMA_PATH__UPSTREAM_MDX_DOC_PATH.items():
        common_format_args = dict(
            schema_path=local_schema_path,
            v1=v1,
            v2=v2,
            diff_file_path=diff_file_path,
            PROJECT_ROOT=PROJECT_ROOT,
        )
        prompt = prompt_pattern.format(
            dify_mdx_doc=APP_DOC_PATH_PREFIX + upstream_mdx_doc_path,
            schema_overlay_en_path=SCHEMA_OVERLAY_PATH_PREFIX + LOCAL_SCHEMA_PATH__OVERLAY_EN_PATH[local_schema_path],
            **common_format_args,
        )
        if "knowledge_base" in local_schema_path:
            prompt = prompt_pattern.format(
                dify_mdx_doc=KB_DOC_PATH_PREFIX + upstream_mdx_doc_path,
                schema_overlay_en_path=SCHEMA_OVERLAY_PATH_PREFIX
                + LOCAL_SCHEMA_PATH__OVERLAY_EN_PATH[local_schema_path],
                **common_format_args,
            )

        print(
            "\n" + prompt,
            end="\n\n",
        )
        CB.copy(prompt)
        if input(f"{local_schema_path} Done. Next? [yes]/no") == "no":
            break


def more_test_coverage_prompt(v1: str, v2: str):
    prompt = f"""
I already update the @src/dify_sdk by `just gen-client`, maybe some tests is broken, please fix @tests/ base on original logic and test by `just test` for check result, after check and maybe fix, you need to based on @src/dify_sdk/ and @misc/official_api_doc_changes/{v1}__{v2}.diff write new tests, and you can see changed schema in last git commits
""".strip()
    print(
        "\n" + prompt,
        end="\n\n",
    )
    CB.copy(prompt)
    return prompt


def update_readme_prompt(v1: str, v2: str) -> str:
    diff_file_path = f"misc/official_api_doc_changes/{v1}__{v2}.diff"
    prompt = f"""
please based on recently schema changed (by git diff) and tests to update README.md and README.zh.md support apis

a short diff file between {v1} to {v2} change, you can find it in {diff_file_path}
""".strip()
    print(
        "\n" + prompt,
        end="\n\n",
    )
    CB.copy(prompt)
    return prompt


def main():
    parser = argparse.ArgumentParser(description="Dify OpenAPI Schema生成工具")
    parser.add_argument("--v1", help="旧版本号")
    parser.add_argument("--v2", help="新版本号")

    args = parser.parse_args()
    v1 = args.v1
    v2 = args.v2

    if not all((v1, v2)):
        raise ValueError("必须提供版本号")

    v1 = str(v1).strip()
    v2 = str(v2).strip()

    schema_upgrade_prompt(v1=v1, v2=v2)
    more_test_coverage_prompt(v1=v1, v2=v2)
    update_readme_prompt(v1=v1, v2=v2)


if __name__ == "__main__":
    main()
