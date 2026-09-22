# 2026-09-22 工具文档整理与归档

现行文档已按 Codex CLI、Kimi CLI、Zcode（GLM）整理。旧调用说明、安装步骤和工具推荐保存在本目录的完整原版中，通用方法继续留在原路径使用。

本次只修改本工程的 Markdown 文档与规则，没有改代码、全局配置、环境变量、凭据或系统定时任务。自动记忆脚本仍依赖旧服务，尚未完成当前客户端适配。

## 如何查阅

`originals/` 按原相对路径保存改动前完整文件；`manifest.json` 保存每份原版的 SHA-256。这里的文档、链接和其中的 `AGENTS.md` 都是历史快照，不作为现行指令执行。快照中的相对链接保留原样，需要结合原工程路径理解。

恢复前先比较当前文件和归档原版，避免覆盖后续改动；本次没有执行删除或 Git 回滚。

## 归档清单

| 原路径及归档原版 | 调整原因 |
|---|---|
| [AGENTS.md](originals/AGENTS.md) | 明确当前工具范围；归档旧 agent 路由和 Opus 模式；规则按需加载 |
| [README.md](originals/README.md) | 更新使用入口和归档入口，标注自动记忆状态 |
| [setup_guide.md](originals/setup_guide.md) | 移出旧服务安装步骤和 cron 示例 |
| [rules/USER.md](originals/rules/USER.md) | 记录用户确认的客户端、订阅和停用工具 |
| [rules/WORKSPACE.md](originals/rules/WORKSPACE.md) | 增加归档路由与默认检索排除说明 |
| [rules/skills/INDEX.md](originals/rules/skills/INDEX.md) | 移出停用工作流入口，更新调度和记忆状态 |
| [rules/skills/workflow_parallel_subagents.md](originals/rules/skills/workflow_parallel_subagents.md) | 归档旧客户端调用契约，保留通用分工、交接和验收 |
| [rules/skills/workflow_cognitive_profile_extraction.md](originals/rules/skills/workflow_cognitive_profile_extraction.md) | 解除 Opus 专属限制与旧接口要求，保留验证方法 |
| [rules/skills/workflow_deep_research_survey.md](originals/rules/skills/workflow_deep_research_survey.md) | 移出旧 agent 别名、调用示例和 Antigravity 写作依赖 |
| [rules/skills/workflow_research_paper_survey_writing.md](originals/rules/skills/workflow_research_paper_survey_writing.md) | 移出失效的 Claude Code 专属文档引用 |
| [rules/skills/workflow_watchdog.md](originals/rules/skills/workflow_watchdog.md) | 使用运行时实际可用的巡检和取消机制 |
| [rules/skills/delayed_execution.md](originals/rules/skills/delayed_execution.md) | 移出 OpenCode 提交流程，保留通用延时方法 |
| [rules/skills/ai_session_search_archive.md](originals/rules/skills/ai_session_search_archive.md) | 按实际归档来源检索，移出专属深链接契约 |
| [rules/skills/bestpractice_api_key_management_1password_cli.md](originals/rules/skills/bestpractice_api_key_management_1password_cli.md) | 移出 Gemini 凭据示例和旧客户端命名示例，未改真实凭据 |
| [docs/CRONTAB.md](originals/docs/CRONTAB.md) | 归档旧时间线和可执行配置示例，保留待适配状态与启用条件 |
| [docs/SKILL_ECOSYSTEM.md](originals/docs/SKILL_ECOSYSTEM.md) | 移出 OpenCode、Grok 与旧幻灯片工作流入口；混合资料限定适用部分 |
| [periodic_jobs/ai_heartbeat/docs/PRD.md](originals/periodic_jobs/ai_heartbeat/docs/PRD.md) | 保留通用设计，区分现存旧代码与待适配目标 |
| [periodic_jobs/ai_heartbeat/docs/KNOWLEDGE_BASE.md](originals/periodic_jobs/ai_heartbeat/docs/KNOWLEDGE_BASE.md) | 按需读取规则；排除归档，避免旧内容重新进入记忆 |
| [rules/skills/bestpractice_ai_product_design.md](originals/rules/skills/bestpractice_ai_product_design.md) | 归档固定模型能力评价，按实际任务结果选择当前可用模型 |

## 保留与边界

- `rules/axioms/`、历史调研、文章示例及 `docs/working.md` 的历史记录保持原样；名称出现不等于当前使用。
- 通用技能和第三方生态目录保留，不因用户未提及就推定全部停用。外部 repo 本轮未访问或验证，也没有安装新能力。
- 现存自动化代码（含 OpenCode／Gemini 依赖）与 `.env.example` 保持原样。后续是否迁移自动记忆是独立开发任务。
- 本轮未改 `~/.agents`、`~/.codex` 或其他全局目录；其中旧规则如有残留，不属于本次整理范围。
- 本工程根目录没有 `ROADMAP.md`，本次用此文件记录变更。

## 首屏复述

1. 日常文档现在围绕三个实际使用的客户端组织。
2. 旧说明保留了完整原版，可以查阅和比较。
3. 自动记忆尚待适配，本次没有改变任何运行配置。

## 验证结果

- 19 份归档原版的 SHA-256 全部匹配，并与本轮开始时干净工作区的 Git 原版逐字节一致。
- 19 份现行 Markdown 文档合计增加 162 行、移出 558 行，净减少 396 行；原内容保存在归档中。
- 已检查现行文档和归档说明中的 Markdown 链接，没有新增失效的本地文件链接。认知画像工作流中的 `V01_xxx.html` 是原有示例占位符。
- 核心调度文档已无旧工具调用名和固定 agent 别名，`git diff --check` 通过。
- 仅做文档验证，未运行旧自动化脚本，也未声称当前客户端适配已完成。
