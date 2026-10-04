# 维护指南

[English](maintenance-guide-en.md) · [首页](README-zh.md)

## 职责与修改

语言目录中的 `research-proposal-toolkit-en`／`research-proposal-toolkit-zh` 是可安装 Skill。SKILL.md 负责触发、路由和边界，references 保存细规则，agents/openai.yaml 保存 UI 文案。普通文档不重复语言后缀，根目录双语文档保留后缀。生成的 guide 是完整附件版，不应手改。

先说明具体失效及希望改变的判断，再改对应模块；避免堆提醒或引入不必要文件。中英文手工维护结构、能力和例外，允许自然表达；构建脚本不做机器翻译。用户可按学科、学校和工具替换环节，保持问题—证据—决定可追溯。

## 构建与检查

使用 Python 3.10 或更新版本，脚本仅需标准库：

```sh
python scripts/build_guides.py
python scripts/build_guides.py --check
python scripts/validate_structure.py
```

可用 `--language zh` 或 `--language en` 单独构建。检查覆盖名称、当前使用的简单 YAML/JSON 字段、UI 文案、双语模块、引用路由、链接、生成一致性与部分敏感模式。CITATION.cff 使用 JSON 兼容 YAML，未虚构 DOI、发布日期或版本号。

这些检查不验证完整 YAML/CFF schema、翻译等价、文献真实性或研究质量。若环境提供官方 Skill 校验器可再运行；任何行为测试都要报告真实输入、输出与限制，不将规则走查称为实跑。

## 学术回归与发布

检查宽泛愿望、已有答案、反证、理论/质性研究、范围过大、用户已授权修改及离线场景。工作流还应检查摘要堆砌、两稿矛盾、样稿与强制格式冲突、缺少原文和未核指标。先修研究判断与结构，后修措辞。

公开文件只含通用方法与授权资料，不从真实研究、私人对话或样稿抽取案例。发现可疑材料先隔离并标记，不复制；Git 历史不由本脚本重写。发布前人工复核隐私与授权，按 README、使用说明、Skill 和完整引导四个入口检查体验。

CHANGELOG 记录功能与学术理由；使用说明不写开发历史。保留 MIT 许可证与署名。版本标签和 GitHub About 由维护者管理；本包不自动发布、修改账号设置或更新用户安装副本。

## Forge 核心同步

`references/forge/` 内嵌上游相同语言的五个模块，来源仓库、内容快照 ID 与每文件 SHA-256 记录在 forge-core-sync.json。它是内容版本，不伪装成未存在的发布标签；MIT 署名保留于许可证。

有本地 Forge 源码时显式执行：

```sh
python scripts/sync_forge_core.py --source ../research-question-forge --check
python scripts/sync_forge_core.py --source ../research-question-forge
python scripts/build_guides.py
python scripts/validate_structure.py
```

同步后审查 Forge 集成、写作和引文规则，不手工在嵌入副本中发展另一套逻辑。独立分发不需要旁边有 Forge；只有主动同步或跨仓库检查时需要其路径。
