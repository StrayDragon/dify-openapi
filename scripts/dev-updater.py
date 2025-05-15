#!/bin/uv run
"""
生成喂给LLM的prompt, 用于修改/更新schema等

同时提供自动化生成新变动schema的代码工作流
"""

import os
from pathlib import Path
import subprocess
import argparse
import yaml
from typing import Any

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain  # type: ignore
from langchain_community.document_loaders import TextLoader  # type: ignore
from langchain_community.vectorstores import FAISS

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
- If you want to invoke `filesystem` tool, you need call shell cmd `pwd` get the current working directory at first and use it as the above given path prefix
- Prefer using increasing edit mode to adjust code, if you got large context write problem, try using another way to finish
- Another helpful context is a preset diff file between {v1} to {v2} change, you can find it in {diff_file_path}
""".strip()
    for local_schema_path, upstream_mdx_doc_path in LOCAL_SCHEMA_PATH__UPSTREAM_MDX_DOC_PATH.items():
        common_format_args = dict(
            schema_path=local_schema_path,
            v1=v1,
            v2=v2,
            diff_file_path=diff_file_path,
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


class SchemaGenerator:
    """使用LLM自动生成/更新OpenAPI schema的类"""

    def __init__(self, openai_api_key: str | None = None, v1: str = "", v2: str = ""):
        """初始化SchemaGenerator

        Args:
            openai_api_key: OpenAI API密钥，如果不提供则从环境变量获取
        """
        self.openai_api_key = openai_api_key or os.environ.get("OPENAI_API_KEY")
        if not self.openai_api_key:
            raise ValueError("OpenAI API密钥未提供，请设置OPENAI_API_KEY环境变量或直接传入参数")

        # 使用API密钥
        from pydantic import SecretStr

        api_key_secret = SecretStr(self.openai_api_key)

        self.llm = ChatOpenAI(model="gpt-4o", temperature=0.0, api_key=api_key_secret)

        self.embeddings = OpenAIEmbeddings(api_key=api_key_secret)
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        self.v1 = v1
        self.v2 = v2
        diff_file_path = f"misc/official_api_doc_changes/{v1}__{v2}.diff"
        self.ab_diff_file_path = PROJECT_ROOT / diff_file_path

    def load_and_process_mdx(self, mdx_path: str) -> list[Document]:
        """加载并处理MDX文档

        Args:
            mdx_path: MDX文档路径

        Returns:
            处理后的文档列表
        """
        try:
            loader = TextLoader(mdx_path)
            documents = loader.load()

            # 分割文档
            split_docs = self.text_splitter.split_documents(documents)
            return split_docs
        except Exception as e:
            print(f"加载MDX文档时出错: {e}")
            return []

    def load_schema(self, schema_path: str) -> dict[str, Any]:
        """加载OpenAPI schema

        Args:
            schema_path: Schema文件路径

        Returns:
            加载的schema字典
        """
        try:
            with open(schema_path, encoding="utf-8") as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"加载Schema文件时出错: {e}")
            return {}

    def load_overlay(self, overlay_path: str) -> dict[str, Any]:
        """加载overlay文件

        Args:
            overlay_path: Overlay文件路径

        Returns:
            加载的overlay字典
        """
        try:
            with open(overlay_path, encoding="utf-8") as f:
                return yaml.safe_load(f)
        except Exception as e:
            print(f"加载Overlay文件时出错: {e}")
            return {}

    def save_schema(self, schema_path: str, schema_data: dict[str, Any]) -> bool:
        """保存schema到文件

        Args:
            schema_path: 保存路径
            schema_data: Schema数据

        Returns:
            是否保存成功
        """
        try:
            with open(schema_path, "w", encoding="utf-8") as f:
                yaml.dump(schema_data, f, allow_unicode=True, sort_keys=False)
            return True
        except Exception as e:
            print(f"保存Schema文件时出错: {e}")
            return False

    def save_overlay(self, overlay_path: str, overlay_data: dict[str, Any]) -> bool:
        """保存overlay到文件

        Args:
            overlay_path: 保存路径
            overlay_data: Overlay数据

        Returns:
            是否保存成功
        """
        try:
            with open(overlay_path, "w", encoding="utf-8") as f:
                yaml.dump(overlay_data, f, allow_unicode=True, sort_keys=False)
            return True
        except Exception as e:
            print(f"保存Overlay文件时出错: {e}")
            return False

    def create_vector_store(self, documents: list[Document]):
        """创建向量存储

        Args:
            documents: 文档列表

        Returns:
            向量存储
        """
        return FAISS.from_documents(documents, self.embeddings)

    def generate_schema_updates(
        self, mdx_path: str, schema_path: str, overlay_path: str, feedback: str = "", iteration: int = 0
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        """生成schema和overlay更新

        Args:
            mdx_path: MDX文档路径
            schema_path: Schema文件路径
            overlay_path: Overlay文件路径
            feedback: 上一次迭代的反馈信息
            iteration: 当前迭代次数

        Returns:
            更新后的schema和overlay
        """
        # 加载文档和创建向量存储
        documents = self.load_and_process_mdx(mdx_path)
        if not documents:
            print(f"无法处理MDX文档: {mdx_path}")
            return {}, {}

        vectorstore = self.create_vector_store(documents)
        retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

        # 加载当前schema和overlay
        current_schema = self.load_schema(schema_path)
        current_overlay = self.load_overlay(overlay_path)

        if not current_schema or not current_overlay:
            print("无法加载当前schema或overlay文件")
            return {}, {}

        # 创建基础提示模板
        base_prompt = """
        你是一位OpenAPI schema专家，需要根据MDX文档更新OpenAPI schema。

        以下是从MDX文档中检索到的相关内容:
        {context}

        当前的OpenAPI schema是:
        ```yaml
        {current_schema}
        ```

        当前的Overlay文件是:
        ```yaml
        {current_overlay}
        ```
        """

        # 添加迭代反馈信息
        if iteration > 0 and feedback:
            feedback_prompt = f"""
        这是第{iteration}次尝试生成更新。上一次尝试的反馈如下:

        ```
        {feedback}
        ```

        请根据上述反馈修复问题。
        """
            base_prompt += feedback_prompt

        # 添加任务说明
        task_prompt = """
        请分析MDX文档中的API定义，并更新OpenAPI schema。

        要求:
        0. 参考预设的diff文件, 这个文件记录版本{v1}到{v2}的变化
        1. 保持原有的schema结构，只更新或添加必要的部分
        2. 确保所有API路径、参数、响应都正确定义
        3. 确保schema符合OpenAPI 3.0规范
        4. 对于新增或修改的中文描述，同时更新overlay文件中的英文翻译
        5. 确保生成的YAML格式正确，不包含语法错误
        6. 如果有错误信息提示某些字段缺失或格式不正确，请特别注意修复这些问题

        请返回两个YAML格式的结果，分别是更新后的schema和overlay:

        更新后的schema:
        ```yaml
        {schema_placeholder}
        ```

        更新后的overlay:
        ```yaml
        {overlay_placeholder}
        ```

        预设的diff文件
        ```diff
        #diff_file_content#
        ```
        """.replace("#diff_file_content#", self.ab_diff_file_path.read_text(encoding="utf-8").strip())

        full_prompt = base_prompt + task_prompt
        schema_prompt = ChatPromptTemplate.from_template(full_prompt)

        # 创建检索链
        document_chain = create_stuff_documents_chain(self.llm, schema_prompt)
        retrieval_chain = create_retrieval_chain(retriever, document_chain)

        # 执行检索和生成
        response = retrieval_chain.invoke(
            {
                "current_schema": yaml.dump(current_schema, allow_unicode=True),
                "current_overlay": yaml.dump(current_overlay, allow_unicode=True),
                "schema_placeholder": "",
                "overlay_placeholder": "",
                "query": f"根据MDX文档更新OpenAPI schema: {os.path.basename(mdx_path)}，迭代次数: {iteration}",
            }
        )

        # 解析结果
        result = response["answer"]

        # 提取更新后的schema和overlay
        schema_yaml = self._extract_yaml_block(result, "更新后的schema")
        overlay_yaml = self._extract_yaml_block(result, "更新后的overlay")

        updated_schema: dict[str, Any] = yaml.safe_load(schema_yaml) if schema_yaml else {}
        updated_overlay: dict[str, Any] = yaml.safe_load(overlay_yaml) if overlay_yaml else {}

        return updated_schema, updated_overlay

    def _extract_yaml_block(self, text: str, block_name: str) -> str:
        """从文本中提取YAML块

        Args:
            text: 包含YAML块的文本
            block_name: YAML块的名称标识

        Returns:
            提取的YAML文本
        """
        start_marker = f"{block_name}:\n```yaml"
        end_marker = "```"

        try:
            start_idx = text.find(start_marker)
            if start_idx == -1:
                # 尝试其他可能的格式
                start_marker = f"{block_name}:\n```"
                start_idx = text.find(start_marker)
                if start_idx == -1:
                    return ""

            start_idx = text.find("\n", start_idx) + 1  # 跳过标记行
            end_idx = text.find(end_marker, start_idx)

            if end_idx == -1:
                return ""

            return text[start_idx:end_idx].strip()
        except Exception:
            return ""

    def apply_overlay(self) -> tuple[bool, str]:
        """应用overlay生成对应语言的schema

        Returns:
            元组，包含是否成功应用overlay和命令输出结果
        """
        try:
            result = subprocess.run(["just", "apply-i18n-overlay-to-openapi-schema"], capture_output=True, text=True)
            output = result.stdout + "\n" + result.stderr if result.stderr else result.stdout
            print(output)

            if result.returncode != 0:
                print("应用overlay失败")
                return False, output
            return True, output
        except Exception as e:
            error_msg = f"执行apply-i18n-overlay-to-openapi-schema命令时出错: {e}"
            print(error_msg)
            return False, error_msg

    def process_schema(self, schema_key: str, max_iterations: int = 5) -> bool:
        """处理指定的schema，支持多次迭代尝试

        Args:
            schema_key: Schema键名，对应LOCAL_SCHEMA_PATH__UPSTREAM_MDX_DOC_PATH中的键
            max_iterations: 最大迭代次数，默认为5次

        Returns:
            是否成功处理
        """
        if schema_key not in LOCAL_SCHEMA_PATH__UPSTREAM_MDX_DOC_PATH:
            print(f"未知的schema键: {schema_key}")
            return False

        # 获取路径
        schema_path = schema_key
        mdx_doc_path = LOCAL_SCHEMA_PATH__UPSTREAM_MDX_DOC_PATH[schema_key]
        overlay_path = SCHEMA_OVERLAY_PATH_PREFIX + LOCAL_SCHEMA_PATH__OVERLAY_EN_PATH[schema_key]

        # 确定完整的MDX路径
        if "knowledge_base" in schema_key:
            full_mdx_path = KB_DOC_PATH_PREFIX + mdx_doc_path
        else:
            full_mdx_path = APP_DOC_PATH_PREFIX + mdx_doc_path

        print(f"处理schema: {schema_key}")
        print(f"MDX文档: {full_mdx_path}")
        print(f"Overlay: {overlay_path}")

        # 迭代处理
        iteration = 0
        feedback = ""
        success = False

        while iteration < max_iterations and not success:
            print(f"\n开始第 {iteration + 1} 次迭代...")

            # 生成更新
            updated_schema, updated_overlay = self.generate_schema_updates(
                full_mdx_path, schema_path, overlay_path, feedback, iteration
            )

            if not updated_schema or not updated_overlay:
                print("生成更新失败")
                feedback = "生成更新失败，请检查MDX文档和schema结构"
                iteration += 1
                continue

            # 保存更新
            schema_saved = self.save_schema(schema_path, updated_schema)
            overlay_saved = self.save_overlay(overlay_path, updated_overlay)

            if not schema_saved or not overlay_saved:
                print("保存更新失败")
                feedback = "保存更新失败，请检查生成的YAML格式是否正确"
                iteration += 1
                continue

            print("Schema和Overlay更新成功，尝试应用overlay...")

            # 应用overlay
            overlay_applied, output = self.apply_overlay()
            if not overlay_applied:
                print("应用overlay失败，将在下一次迭代中修复")
                feedback = f"应用overlay失败，错误信息如下:\n{output}"
                iteration += 1
                continue

            print("成功应用overlay")
            success = True

        if success:
            print(f"成功处理schema: {schema_key}，共迭代 {iteration + 1} 次")
        else:
            print(f"处理schema: {schema_key} 失败，已达到最大迭代次数 {max_iterations}")

        return success

    def process_all_schemas(self, max_iterations: int = 5) -> dict[str, bool]:
        """处理所有schema

        Args:
            max_iterations: 每个schema的最大迭代次数，默认为5次

        Returns:
            各schema处理结果的字典
        """
        results: dict[str, bool] = {}
        for schema_key in LOCAL_SCHEMA_PATH__UPSTREAM_MDX_DOC_PATH:
            print(f"\n开始处理: {schema_key}")
            result = self.process_schema(schema_key, max_iterations)
            results[schema_key] = result
            print(f"处理完成: {schema_key}, 结果: {'成功' if result else '失败'}")

            # 询问是否继续
            if (
                list(LOCAL_SCHEMA_PATH__UPSTREAM_MDX_DOC_PATH.keys()).index(schema_key)
                < len(LOCAL_SCHEMA_PATH__UPSTREAM_MDX_DOC_PATH) - 1
            ):
                if input("继续处理下一个? [yes]/no: ") == "no":
                    break

        return results


def rag_schema_generator(
    *,
    schema_key: str | None = None,
    max_iterations: int = 5,
    v1: str,
    v2: str,
):
    """使用RAG方式生成schema更新

    Args:
        schema_key: 要处理的特定schema键，如果为None则处理所有schema
        max_iterations: 最大迭代次数，默认为5次
    """
    generator = SchemaGenerator(
        v1=v1,
        v2=v2,
    )

    if schema_key:
        if schema_key in LOCAL_SCHEMA_PATH__UPSTREAM_MDX_DOC_PATH:
            result = generator.process_schema(schema_key, max_iterations)
            print(f"处理结果: {'成功' if result else '失败'}")
        else:
            print(f"未知的schema键: {schema_key}")
            print(f"可用的schema键: {list(LOCAL_SCHEMA_PATH__UPSTREAM_MDX_DOC_PATH.keys())}")
    else:
        results = generator.process_all_schemas(max_iterations)
        print("\n处理结果汇总:")
        for schema, success in results.items():
            print(f"{schema}: {'成功' if success else '失败'}")


def main():
    parser = argparse.ArgumentParser(description="Dify OpenAPI Schema生成工具")
    parser.add_argument(
        "--mode", choices=["prompt", "rag"], default="prompt", help="运行模式: prompt(生成提示) 或 rag(自动生成schema)"
    )
    parser.add_argument("--schema", help="要处理的特定schema键")
    parser.add_argument("--max-iterations", type=int, default=5, help="最大迭代次数，默认为5次")
    parser.add_argument("--v1", help="旧版本号")
    parser.add_argument("--v2", help="新版本号")

    args = parser.parse_args()
    v1 = args.v1
    v2 = args.v2
    print(v1, v2)

    if not all((v1, v2)):
        raise ValueError("必须提供版本号")

    v1 = str(v1).strip()
    v2 = str(v2).strip()

    if args.mode == "prompt":
        schema_upgrade_prompt(v1=v1, v2=v2)
        more_test_coverage_prompt(v1=v1, v2=v2)
        update_readme_prompt(v1=v1, v2=v2)
    elif args.mode == "rag":
        rag_schema_generator(
            schema_key=args.schema,
            max_iterations=args.max_iterations,
            v1=v1,
            v2=v2,
        )


if __name__ == "__main__":
    main()
