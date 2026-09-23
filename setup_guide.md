# 本工程使用指南

在 Codex CLI、Kimi CLI 或 Zcode 中进入本工程，先读取 [AGENTS.md](AGENTS.md)。客户端、订阅和停用工具以该入口与 [USER.md](rules/USER.md) 为准。

## 开始任务

- 查找或存放材料前，按 [WORKSPACE.md](rules/WORKSPACE.md) 定位具体目录。
- 执行某类任务前，查 [Skills 索引](rules/skills/INDEX.md)，只读取命中的工作流。
- 需要历史判断时，按任务检索 [记忆记录](contexts/memory/OBSERVATIONS.md) 与 [公理索引](rules/axioms/INDEX.md)。
- 提问和讨论遵守 [执行边界](rules/EXECUTION_BOUNDARY.md)；发布、删除和系统配置遵守 [安全规则](rules/SAFETY.md)。

身份和偏好文件已维护，不需要每次重新填写。发现其中内容与用户明确说明不一致时，再更新对应条目。

## 维护文档

新经验优先写入对应任务材料；可复用的方法再整理为 skill。创建或重写前读 [Skill 写作指南](rules/skills/bestpractice_skill_writing.md)，写清目标、边界、验收标准与输出位置，并更新索引。

规则修改先保留原版到 `archives/<topic>/<batch>/originals/<原相对路径>`，附说明和清单；现行文件保留有效内容，并检查引用关系。归档原文只用于回溯，不进入默认规则加载或新记忆采集。

## 需要额外配置的能力

| 能力 | 当前使用条件 |
|---|---|
| 自动观察与反思 | 旧脚本尚未适配当前客户端，见 [定时任务状态](docs/CRONTAB.md) |
| AI 会话归档 | `contexts/ai_sessions/` 是约定输出目录，目前尚未创建；先验证导出器支持的来源，见 [会话检索](rules/skills/ai_session_search_archive.md) |
| 语义搜索 | 先核对已安装工具和 embedding 配置，外部资料见 [技能目录](docs/SKILL_ECOSYSTEM.md) |
| 邮件与 Web 分享 | 按实际目的核对服务、账号与发布授权；外部资料见 [技能目录](docs/SKILL_ECOSYSTEM.md)，报告发布参考 [分享工作流](rules/skills/share_report.md) |
| Python 脚本 | 使用目标项目已有环境；根目录 `.venv/` 当前不存在，不把约定路径当作已安装环境 |

外部资料被收录不代表已安装、已验证或需要购买。Coding Plan 订阅也不等同于独立 API 额度。

## 整理记录

历次变更的原版、原因和验证结果见 [本地归档](archives/README.md)。本次文档整理没有配置外部服务、修改全局目录或启停定时任务。
