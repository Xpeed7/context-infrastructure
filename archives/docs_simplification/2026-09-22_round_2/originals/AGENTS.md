# AGENTS.md - 本工程入口

本工程用于维护个人上下文、规则和可复用工作流。配置说明见 `setup_guide.md`。

## 当前工具范围

- 客户端：Codex CLI、Kimi CLI、Zcode（使用 GLM）。
- 已订阅：Codex、Kimi、GLM Coding Plan；不据此假设拥有独立 API 额度或跨客户端模型路由。
- 不使用 Cursor、OpenCode、Gemini、Grok；不把它们列为安装前提、默认执行入口或备选模型。
- 客户端工具、子代理和参数以当前会话实际暴露的能力为准，不编造跨客户端调用方式。
- `archives/` 保存历史原版，不属于现行规则或默认检索范围；仅回溯历史时读取。

## Every Session

Before doing anything else:

1. Read `rules/SOUL.md` — this is who you are
2. Read `rules/USER.md` — this is who you're helping
3. Read `rules/WORKSPACE.md` — file routing table, check before searching for files
4. Read `rules/COMMUNICATION.md` — how to think and communicate (especially for non-coding tasks)
5. Read `rules/EXECUTION_BOUNDARY.md` — 讨论与实施的边界
6. Read `rules/PROJECT_GOVERNANCE.md` — 项目规范与进度管理
7. Read `rules/SAFETY.md` — 安全约束
8. Read `rules/skills/INDEX.md` — 按任务选择工作流，具体文件按需读取

## Multi-Agent Nudge

This harness can delegate work to multiple sub-agents. You don't need to use them by default, but keep the capability in mind for tasks that are large, parallelizable, research-heavy, or benefit from independent cross-checking.

使用前读取 `rules/skills/workflow_parallel_subagents.md`，遵循当前客户端的工具与权限边界；缺少子代理能力时按相同任务边界串行完成。

## File Routing

**找文件时，先查 `rules/WORKSPACE.md`，再搜索。** WORKSPACE.md 是这个 workspace 的目录索引，记录了每类内容的存放位置。绝大多数情况下查一下就能定位到目标目录，不需要全盘 glob/grep。如果发现新目录或项目没被收录，顺手更新 WORKSPACE.md。

## Skills

**Skills** 是 AI 可复用的能力，包括工作流、API 指南、最佳实践等。

**重要：遇到"怎么做 X"时，先查 skill 再查系统工具。** 搜索顺序：(1) 下方速查表 → (2) `rules/skills/INDEX.md` → (3) 系统工具。

**需要执行某项任务** → 先查 `rules/skills/INDEX.md` 找到对应的 skill
**想添加新能力** → 参考现有 skill 格式，更新 INDEX.md

### 常用 Skill 速查（以 INDEX.md 为准）

**深度调研任务** → `rules/skills/workflow_deep_research_survey.md`
**调用后台 Agent / 并行 Subagent** → `rules/skills/workflow_parallel_subagents.md`

命中后读对应 skill 文件再执行；INDEX.md 是唯一路由源，这里不展开步骤。

## Axioms（公理）

从个人经历提炼的决策原则，用于启发深度思考。分类索引、使用指南和触发词见 `rules/axioms/INDEX.md`。

## Memory System（记忆系统）

三层记忆架构：
- **L3（全局约束）**：启动时读取上述核心规则，其他规则按索引按需加载
- **L1/L2（动态记忆）**：`contexts/memory/OBSERVATIONS.md`，agent 主动检索
- **自动积累（待适配）**：`periodic_jobs/ai_heartbeat/` 保留旧实现，尚未适配当前客户端；状态见 `docs/CRONTAB.md`

## Safety

- Don't exfiltrate private data. Ever.
- Don't run destructive commands without asking.
- When in doubt, ask.
