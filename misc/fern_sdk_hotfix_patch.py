#!/bin/uv run
# /// script
# requires-python = ">=3.12"
# dependencies = [
# ]
# ///
"""
Python 标准库实现的 fern_sdk_hotfix_patch 脚本
用于修补 Fern 生成的 SDK 中的已知问题
"""

import os
import re
from re import Pattern, Match
import json
import tempfile
import shutil
from typing import Any


def get_fern_api_version() -> str:
    """获取 fern-api 版本"""
    version: str = ""
    if os.path.isfile("fern/fern.config.json"):
        try:
            with open("fern/fern.config.json") as f:
                config: dict[str, Any] = json.load(f)
                version = config.get("version", "")
        except (json.JSONDecodeError, FileNotFoundError):
            # 如果 JSON 解析失败，尝试使用正则表达式
            try:
                with open("fern/fern.config.json") as f:
                    content: str = f.read()
                    match: None | Match[str] = re.search(r'"version":\s*"([0-9]*\.[0-9]*\.[0-9]*)"', content)
                    if match:
                        version = match.group(1)
            except FileNotFoundError:
                pass
    return version


def get_python_sdk_version() -> str:
    """获取 fern-python-sdk 版本"""
    version: str = ""
    if os.path.isfile("fern/generators.yml"):
        try:
            with open("fern/generators.yml") as f:
                content: str = f.read()
                match: None | Match[str] = re.search(r"version:\s*([0-9]*\.[0-9]*\.[0-9]*)", content)
                if match:
                    version = match.group(1)
        except FileNotFoundError:
            pass
    return version


def patch_file(file_path: str, pattern: str | Pattern[str], replacement: str) -> bool:
    """修补文件内容"""
    if not os.path.isfile(file_path):
        print(f"文件不存在: {file_path}")
        return False

    # 检查文件是否包含需要修补的内容
    with open(file_path) as f:
        content: str = f.read()

    if not re.search(pattern, content):
        print(f"文件不需要修补: {file_path}")
        return False

    # 创建临时文件
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as tmp:
        tmp_path: str = tmp.name
        # 替换内容并写入临时文件
        patched_content: str = re.sub(pattern, replacement, content)
        tmp.write(patched_content)

    # 替换原文件
    shutil.move(tmp_path, file_path)
    print(f"已修补文件: {file_path}")
    return True


def main() -> None:
    """主函数"""
    fern_api_version: str = get_fern_api_version()
    python_sdk_version: str = get_python_sdk_version()

    print(f"Fern API 版本: {fern_api_version}")
    print(f"Python SDK 版本: {python_sdk_version}")

    target_file: str = "src/dify_sdk/documents/raw_client.py"
    pattern: str = r'"process_rule": process_rule'
    replacement: str = r'"process_rule": process_rule.model_dump_json() if process_rule else None'
    patch_file(target_file, pattern, replacement)

    target_file: str = "src/dify_sdk/workflow/raw_client.py"
    pattern: str = r"(\s*)(if len\(_text\) == 0:)"
    replacement: str = r'\1_text = _text.removeprefix("data: ")\n\1if len(_text) == 0:'
    patch_file(target_file, pattern, replacement)


if __name__ == "__main__":
    main()
