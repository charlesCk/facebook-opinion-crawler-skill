# Governance

`charlesSKILL` 是公开安全的 AI workflow / Codex Skill 项目组合，不是原始业务数据仓库。

## 发布原则

- 先写清楚业务价值，再提交脚本或 Skill。
- 每个新项目必须有入口 README，并写明适用场景、安全边界和后续维护方式。
- 能公开的是方法、模板、fake sample、字段框架、脚本入口和脱敏总结。
- 不能公开的是真实账号、合同、客户资料、业务导出、截图、日志、浏览器会话和内部链接。

## 项目准入

新增项目时至少满足：

- 已加入 `PROJECTS.md`。
- 有项目目录 README。
- 有安全边界说明。
- 如果包含脚本，有 smoke check 或参数校验计划。
- 如果来自私有项目，只保留 public-safe 方法层，不搬运原始数据。

## 推荐交付结构

```text
project-name/
  README.md
  docs/
    MANIFEST.md
    HANDOFF.md
  references/
  scripts/
  agents/
```

纯文档项目可以只保留 `README.md`、`docs/MANIFEST.md` 和 `docs/HANDOFF.md`。

## 版本和交接

- 重要项目增加 `docs/MANIFEST.md`，说明当前交付包包含什么、不包含什么。
- 重要项目增加 `docs/HANDOFF.md`，说明接手人如何复用、验证和扩展。
- 重要变更写入 `CHANGELOG.md`。

## 上传前要求

提交前运行：

```bash
python3 scripts/preflight_upload_check.py
node tests/smoke_check.mjs
git diff --check
```

如发现敏感内容，先移除或脱敏，不要继续提交。
