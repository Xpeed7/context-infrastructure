# AGENTS.md - 本工程入口

本工程维护个人上下文、规则和可复用工作流。使用说明见 [setup_guide.md](setup_guide.md)。

## 当前工具范围

- 客户端：Codex CLI、Kimi CLI、Zcode（使用 GLM）。
- 已订阅：Codex、Kimi、GLM Coding Plan；不据此假设拥有独立 API 额度或跨客户端模型路由。
- 不使用 Cursor、OpenCode、Gemini、Grok；不把它们列为安装前提、默认执行入口或备选模型。
- 客户端工具、子代理和参数以当前会话实际暴露的能力为准，不编造跨客户端调用方式。
- `archives/` 保存历史原版，不属于现行规则或默认检索范围；仅回溯历史时读取。

## 每次会话先读

1. [SOUL.md](rules/SOUL.md)：身份与协作原则。
2. [USER.md](rules/USER.md)：称呼、背景与偏好。
3. [WORKSPACE.md](rules/WORKSPACE.md)：文件路由，搜索前必读。
4. [COMMUNICATION.md](rules/COMMUNICATION.md)：思考与表达。
5. [EXECUTION_BOUNDARY.md](rules/EXECUTION_BOUNDARY.md)：讨论与实施边界。
6. [PROJECT_GOVERNANCE.md](rules/PROJECT_GOVERNANCE.md)：项目规范与进度管理。
7. [SAFETY.md](rules/SAFETY.md)：安全红线，不能因其他工作流而降低。
8. [Skills 索引](rules/skills/INDEX.md)：按任务选择工作流，正文按需读取。

## 按需读取

- 找文件先按 `WORKSPACE.md` 定位目录，再局部搜索；发现已确认的新目录用途时更新路由。
- 遇到“怎么做”或执行任务，先查 Skills 索引并读取对应工作流，再选工具；新增技能须更新索引。
- 大型独立检索或交叉验证可使用子代理，先读 [并行工作流](rules/skills/workflow_parallel_subagents.md)；能力或权限不支持时串行完成。
- 决策原则见 [公理索引](rules/axioms/INDEX.md)，历史经验按任务检索 `contexts/memory/OBSERVATIONS.md`。
- 自动记忆的适配状态见 [定时任务状态](docs/CRONTAB.md)。归档材料不作为现行规则加载。
