#!/bin/uv run
# /// script
# requires-python = ">=3.13"
# dependencies = [
#   "typer",
# ]
# ///


"""
简单检测文档中是否包含中文字符的脚本，并显示第一个中文字符的位置
"""

import os
import re
import typer
from typing import Optional, Tuple

app = typer.Typer()


def detect_chinese(file_path: str) -> Tuple[bool, Optional[int], Optional[str]]:
    chinese_pattern = re.compile(r"[\u4e00-\u9fff\u3400-\u4dbf\u3000-\u303f\uff00-\uffef]")
    comment_pattern = re.compile(r".*#.*")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line_num, line in enumerate(file, 1):
                if comment_pattern.match(line):
                    continue

                match = chinese_pattern.search(line)
                if match:
                    return True, line_num, match.group(0)
        return False, None, None
    except UnicodeDecodeError:
        for encoding in ["gbk", "gb2312", "big5"]:
            try:
                with open(file_path, "r", encoding=encoding) as file:
                    for line_num, line in enumerate(file, 1):
                        if comment_pattern.match(line):
                            continue

                        match = chinese_pattern.search(line)
                        if match:
                            return True, line_num, match.group(0)
                    return False, None, None
            except UnicodeDecodeError:
                continue
        return False, None, None
    except Exception as e:
        typer.echo(f"无法读取文件 {file_path}: {str(e)}")
        return False, None, None


@app.command()
def check(
    path: str = typer.Argument(..., help="要检查的文件或目录路径"),
    recursive: bool = typer.Option(False, "--recursive", "-r", help="如果指定的是目录，是否递归检查子目录"),
):
    if os.path.isfile(path):
        has_chinese, line_num, char = detect_chinese(path)
        if has_chinese:
            typer.echo(f"{path}:{line_num} 包含中文字符，第一个中文字符 '{char}'")
        else:
            typer.echo(f"{path}: 不包含中文字符")

    elif os.path.isdir(path):
        files_to_check: list[str] = []

        if recursive:
            for root, _, files in os.walk(path):
                for file in files:
                    files_to_check.append(os.path.join(root, file))
        else:
            files_to_check = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

        total_files = 0
        chinese_files = 0

        for file_path in files_to_check:
            total_files += 1
            has_chinese, line_num, char = detect_chinese(file_path)

            if has_chinese:
                chinese_files += 1
                typer.echo(f"{file_path}: 包含中文字符，第一个中文字符 '{char}' 出现在第 {line_num} 行")

        typer.echo(f"\n检查了 {total_files} 个文件，其中 {chinese_files} 个文件包含中文字符")

    else:
        typer.echo(f"错误: 路径 '{path}' 不存在")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
