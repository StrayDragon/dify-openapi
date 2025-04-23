# /// script
# requires-python = ">=3.13"
# dependencies = [
# ]
# ///
"""
生成喂给LLM的prompt, 用于修改/更新schema等

TODO: @l8ng 使用RAG方式, 构建一个自动化的schema的工作流
"""

import os
import subprocess


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

def schema_upgrade_prompt():
    prompt_pattern = """
You are a expert coder and api doc maintainer, master on openapi schema writing and can read and understand mdx doc, you task is based on  mdx doc @{dify_mdx_doc} , then check/fix/update this openapi schema @{schema_path}, make a plan to finish this task, and try your best to done, then check and adjust the english overlay file @{schema_overlay_en_path}

After done, try to use `just apply-i18n-overlay-to-openapi-schema` to generate the corresponding language schema, you need read the last part of command output to check the overlay work well, if has any problems, try to fix and repeat this process until no error report

Except for the just commands permitted by me above, please DO NOT run any other commands (like `just test` or `just gen-client`). Once everything is completed, please provide a brief summary report.

NOTE:
- If you want to invoke `filesystem` tool, you need call shell cmd `pwd` get the current working directory at first and use it as the above given path prefix
- Prefer using increasing edit mode to adjust code, if you got large context write problem, try using another way to finish
""".strip()
    for local_schema_path, upstream_mdx_doc_path in LOCAL_SCHEMA_PATH__UPSTREAM_MDX_DOC_PATH.items():
        prompt = prompt_pattern.format(
            schema_path=local_schema_path,
            dify_mdx_doc=APP_DOC_PATH_PREFIX + upstream_mdx_doc_path,
            schema_overlay_en_path=SCHEMA_OVERLAY_PATH_PREFIX + LOCAL_SCHEMA_PATH__OVERLAY_EN_PATH[local_schema_path],
        )
        if "knowledge_base" in local_schema_path:
            prompt = prompt_pattern.format(
                schema_path=local_schema_path,
                dify_mdx_doc=KB_DOC_PATH_PREFIX + upstream_mdx_doc_path,
                schema_overlay_en_path=SCHEMA_OVERLAY_PATH_PREFIX
                + LOCAL_SCHEMA_PATH__OVERLAY_EN_PATH[local_schema_path],
            )

        print(
            "\n" + prompt,
            end="\n\n",
        )
        CB.copy(prompt)
        if input("Next? [yes]/no") == "no":
            break


def more_test_coverage():
    return """
I already update the @src/dify_sdk by `just gen-client`, maybe some tests is broken, please fix @tests/ base on original logic and test by `just test` for check result
""".strip()


def main():
    schema_upgrade_prompt()


if __name__ == "__main__":
    main()
