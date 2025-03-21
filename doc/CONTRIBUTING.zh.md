# 欢迎贡献!

我们非常欢迎您为 Dify x OpenAPI 项目做出贡献。无论是修复错误、改进文档还是添加新功能,您的贡献都将帮助我们打造更好的工具。

## 如何贡献?

基本上的流程:
1. Fork 本仓库并克隆到本地
2. 创建新的分支进行修改
3. 提交 Pull Request
4. 等待 Review 和合并

你可以参考以下几个案例, 以完成贡献!


### 案例: Dify 1.0.1 -> 1.1.0

#### I. 调研升级产生那些变动

关联代码变动参考:
- dify:
  - [1.0.1__1.1.0.diff](../misc/official_api_doc_changes/1.0.1__1.1.0.diff)
    - 可以参考并使用 [生成Diff脚本](../scripts/gen_diff_by_versions.py) 生成
- dify-doc
  - https://github.com/langgenius/dify-docs/pull/563/files


> 这里有一个小插曲: 见: https://github.com/langgenius/dify/issues/16179

经过以上调研, 发现这次版本升级中主要围绕着知识库API, 其增加了6个新的API, 这些新的API需要新增schema, 并且需要生成新的客户端(py)SDK, 并且编写对其的简单测通测试代码


#### II. 进行更改与测试

0. 根据调研中变动你可以使用合适的方式将变动应用到 [schema](../schema) 中的 *.zh.yaml 文件 (我们这里以 zh.yaml 为主更新)
1. 将相关产生变动中的中文描述翻译为多语言版本使用 [schema/overlay](../schema/overlays) 中的 对应语言的文件, 比如 *.en.overlay.yaml , 之后使用 `just apply-i18n-overlay-to-openapi-schema` 生成对应版本的 OpenAPI schema, 生成后请检查对应 schame 中是否有问题
2. 使用 `just run-openapi-ui` 打开 本地 swagger UI 页面进行简单的测试和调试验证schema是否编写正确
3. 生成新的客户端测试代码: `just gen-client`, 检查命令是否正常执行, 新代码是否生成
4. 根据这次代码变动, 需要编写新的API产生的单元测试, 根据分类应该实现在 [test_datasets_api.py](../tests/knowledge_base/test_datasets_api.py) 中 然后使用 `just test` 测试代码是否正常
5. 调整README.(zh).md中的相关变动产生的新说明
6. 发布PR


这其中每个部分都可以分为多个子任务, 并且使用多个 `git commit` 中不同的msg标识进度

