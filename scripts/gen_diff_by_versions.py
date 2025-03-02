#!/bin/uv run
"""
- 需要正确初始化submodule才能使用, 如果你没有使用 `git clone --recurse-submodules ...` 来clone, 请先运行以下命令:
```bash
git submodule init
git submodule update
```
- 如果你想获取最新的代码, 请使用以下命令更新后运行
```bash
cd libs/dify
git pull origin main
cd ..
git add libs/dify
git commit -m "submodule: update to latest"
```
"""

from pathlib import Path
import subprocess

PROJECT_ROOT = Path(__file__).parent.parent
DIFY_REPO_DIR = PROJECT_ROOT / "libs" / "dify"

V1 = input("Enter the old version (default: 0.15.3): ") or "0.15.3"
V2 = input("Enter the new version (default: 1.0.0): ") or "1.0.0"

DOC_LIST = [
    "web/app/components/develop/template/template.zh.mdx",
    "web/app/components/develop/template/template_advanced_chat.zh.mdx",
    "web/app/components/develop/template/template_chat.zh.mdx",
    "web/app/components/develop/template/template_workflow.zh.mdx",
    "web/app/(commonLayout)/datasets/template/template.zh.mdx",
]


DIFF_FILE = PROJECT_ROOT / "misc" / "official_api_doc_changes" / f"{V1}__{V2}.diff"

GIT_DIFF2_COMMAND = ["git", "diff", f"--output={DIFF_FILE}", V1, V2, "--"]
GIT_DIFF2_COMMAND.extend(DOC_LIST)

subprocess.run(GIT_DIFF2_COMMAND, check=True, cwd=DIFY_REPO_DIR)
