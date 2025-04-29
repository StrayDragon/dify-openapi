#!/bin/uv run
"""
# 自动处理

```bash
$ ./scripts/gen_diff_by_versions.py --v1 1.1.0 --v2 1.1.1 --update # 初始化 submodule 后
$ ./scripts/gen_diff_by_versions.py --v1 1.1.0 --v2 1.1.1 --update --init # 未初始化 submodule
```

# 手动处理
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

然后

```bash
$ ./scripts/gen_diff_by_versions.py --v1 1.1.0 --v2 1.1.1
```

"""

import argparse
import logging
import subprocess
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).parent.parent
DIFY_REPO_DIR = PROJECT_ROOT / "libs" / "dify"
DOC_PATHS = [
    "web/app/components/develop/template/template.zh.mdx",
    "web/app/components/develop/template/template_advanced_chat.zh.mdx",
    "web/app/components/develop/template/template_chat.zh.mdx",
    "web/app/components/develop/template/template_workflow.zh.mdx",
    "web/app/(commonLayout)/datasets/template/template.zh.mdx",
]

def init_submodules():
    try:
        subprocess.run(["git", "submodule", "init"], check=True)
        subprocess.run(["git", "submodule", "update"], check=True)
        logger.info("Git submodules initialized successfully")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to initialize submodules: {e}")
        raise

def update_submodules():
    try:
        subprocess.run(["git", "pull", "origin", "main"], check=True, cwd=DIFY_REPO_DIR)
        subprocess.run(["git", "fetch"], check=True, cwd=DIFY_REPO_DIR)
        subprocess.run(["git", "add", "libs/dify"], check=True, cwd=PROJECT_ROOT)
        subprocess.run(["git", "commit", "-m", "submodule: update to latest"], check=True, cwd=PROJECT_ROOT)
        logger.info("Submodules updated successfully")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to update submodules: {e}")
        raise

def generate_diff(v1: str, v2: str):
    diff_file = PROJECT_ROOT / "misc" / "official_api_doc_changes" / f"{v1}__{v2}.diff"
    diff_file.parent.mkdir(parents=True, exist_ok=True)

    cmd = ["git", "diff", f"--output={diff_file}", v1, v2, "--"] + DOC_PATHS
    try:
        subprocess.run(cmd, check=True, cwd=DIFY_REPO_DIR)
        logger.info(f"Generated diff file: {diff_file}")
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to generate diff: {e}")
        raise

def main():
    parser = argparse.ArgumentParser(description="Generate API documentation diffs between Dify versions")
    parser.add_argument("--v1", default="0.15.3", help="Old version (default: 0.15.3)")
    parser.add_argument("--v2", default="1.0.0", help="New version (default: 1.0.0)")
    parser.add_argument("--init", action="store_true", help="Initialize submodules")
    parser.add_argument("--update", action="store_true", help="Update submodules")

    args = parser.parse_args()

    if args.init:
        init_submodules()
    if args.update:
        update_submodules()

    generate_diff(args.v1, args.v2)

if __name__ == "__main__":
    main()
