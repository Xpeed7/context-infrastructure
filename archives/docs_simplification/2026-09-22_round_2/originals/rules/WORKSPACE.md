# WORKSPACE.md - 目录路由速查

目标：让 AI 每轮 session 都能快速知道"去哪里找/放什么"。**找任何文件前先查这里。**

## 路由规则

### 项目与代码
- 写代码 / 跑脚本 / 一次性项目：`adhoc_jobs/<project>/`
- 工具脚本（邮件、语义搜索、分享报告等）：`tools/`
- 定时任务：`periodic_jobs/`

### 知识与记录
- 通用调研报告：`contexts/survey_sessions/`
- 思考 / 复盘 / 方法论：`contexts/thought_review/`
- 可复用 Prompt 模板：`contexts/prompts/`
- 外部文章收录（stormzhang 以外的作者）：`contexts/collected_articles/`（跨作者通用，收录规范见该目录 README.md；stormzhang 专属库在工程外，见快速查询）
- 待整理草稿：`contexts/draft/`（整理入库后待清理的原始稿）
- 公众号 / 博客文章创作（每篇一目录）：`contexts/writing/`（素材引用 `survey_sessions`，不复制）
- 每日日志：`contexts/daily_records/`
- 个人学习计划与进度：`contexts/learning_plans/`（Superlinear 三个月课程计划：`superlinear_2026/`）
- AI 会话归档：`contexts/ai_sessions/<source>/`（使用 ai_session_export 生成；搜索流程见 `rules/skills/ai_session_search_archive.md`）

### 系统与规则
- 可复用技术方案 / Skill：`rules/skills/`
- 核心公理（Axioms）：`rules/axioms/`
- 记忆系统：`contexts/memory/` + `periodic_jobs/ai_heartbeat/`
- 本工程历史文档与废弃规则：`archives/`；不默认加载或检索。2026-09-22 工具整理记录见 `archives/retired_tooling/2026-09-22/README.md`，改动前原文按原相对路径保存在该目录的 `originals/`。

## 命名规则
- 目录和文件名：小写 + 下划线 (snake_case)
- 临时一次性项目：`tmp_<name>/`

## Python 环境
- 根目录 `.venv/` 为工作区级环境，用 `uv pip install` 管理依赖
- 需要隔离时在 `adhoc_jobs/<project>/.venv/` 建独立环境

## 快速查询

<!-- 随着你的项目增长，在这里添加活跃项目的快捷路由 -->
<!-- 格式：- `project-name` → `adhoc_jobs/project_name/` (说明) -->
- `playwright_demo` → `adhoc_jobs/playwright_demo/` (playwright-cli + spec-kit 驱动的 TodoMVC 测试演示，spec-driven testing 样板，12 场景全绿，独立 git)
- `muyun_homepage` → `adhoc_jobs/muyun_homepage/` (个人主页，镜像自 stormzhang.ai 静态站，已改名 muyun，待替换个人内容)
- `stormzhang 文章收录` → `/Users/chenruiyan/2026-project/stormzhang/articles/` (stormzhang 教程/思考/prompt 收录库，收录规范见该目录 README.md)
- `writing-skill` → `/Users/chenruiyan/2026-project/writing-skill/` (grapeot 公开写作工作流 repo：内部/外部写作工作流、prose lint CLI、thesis catalog；本仓库已迁移的分析/外部写作 skill 内容在此)
