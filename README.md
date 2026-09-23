# Context Infrastructure

本地个人上下文工程：集中维护 AI 协作规则、技能索引、调研与写作材料，以及可检索的经验记录。当前使用 Codex CLI、Kimi CLI、Zcode（GLM）；具体使用范围见 [AGENTS.md](AGENTS.md)。

## 日常入口

| 需要做什么 | 从哪里开始 |
|---|---|
| 开始一次 AI 会话 | [工程规则](AGENTS.md) |
| 了解如何使用和维护 | [使用指南](setup_guide.md) |
| 查找或存放文件 | [目录路由](rules/WORKSPACE.md) |
| 查找可复用工作流 | [Skills 索引](rules/skills/INDEX.md) |
| 回顾个人偏好与经验 | [用户背景](rules/USER.md)、[记忆记录](contexts/memory/OBSERVATIONS.md) |
| 查阅整理前的文档 | [本地归档](archives/README.md) |

## 目录分工

- `rules/`：核心规范、公理和按需读取的技能。
- `contexts/`：调研、思考、写作、学习与记忆材料，具体子目录以目录路由为准。
- `adhoc_jobs/`：独立项目和一次性任务。
- `tools/`：工具脚本与模板，使用前检查依赖和配置。
- `periodic_jobs/`：定时任务代码；自动记忆仍为旧实现，状态见 [CRONTAB.md](docs/CRONTAB.md)。
- `docs/`：组件状态和外部能力资料。
- `archives/`：退出日常使用的文档原版，不默认加载。

## 能力状态

核心规则、现有技能文档和手工记忆记录可以使用。文档存在不代表相关工具已安装或调用链已验证；自动记忆、会话导出和外部服务需要各自核验。

需要额外能力时参考 [外部技能目录](docs/SKILL_ECOSYSTEM.md)，按实际任务选用，不必安装整套工具。安全与发布边界见 [SAFETY.md](rules/SAFETY.md)。

## 来源

本工程基于 [grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure) 的参考结构维护。上游背景文章：[为什么 AI 只会说正确的废话，以及怎么把它逼出舒适区](https://yage.ai/context-infrastructure.html)。历史案例保留原有语境，不代表用户当前工具或所有偏好。

License：MIT。
