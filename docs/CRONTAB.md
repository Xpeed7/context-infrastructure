# 定时任务状态

本页描述仓库中自动任务与当前工具的兼容状态，不代表本机已经安装或停用了任何 cron。本轮未读取或修改系统 crontab。

## 自动记忆任务待适配

当前使用 Codex CLI、Kimi CLI、Zcode（GLM）。仓库内下列脚本仍依赖 `periodic_jobs/ai_heartbeat/src/v0/opencode_client.py`：

- `observer.py`：扫描变化并生成观察记录。
- `reflector.py`：合并和提炼记忆。
- `jobs/crontab_monitor.py`：定时任务健康检查。
- `jobs/ai_news_survey.py`、`jobs/daily_newsletter.py`：资讯与邮件流程。

这些是保留的旧实现，不是当前工具的可用集成。旧时间线、命令示例和配置说明见 [历史原版](../archives/retired_tooling/2026-09-22/originals/docs/CRONTAB.md)。

## 启用条件

后续若需要自动运行，先适配实际客户端的调用方式与认证，验证单次运行、超时取消、日志和输出文件，再单独配置调度。Coding Plan 订阅不代表可以直接作为 API 使用。

会话导出统一写入 `contexts/ai_sessions/<source>/`，只配置经验证支持的来源。搜索方法见 [会话检索](../rules/skills/ai_session_search_archive.md)。不假设同一个导出器支持所有客户端。

邮件、发布、记忆删除和系统配置仍遵守 `rules/SAFETY.md`，定时任务不能扩大用户授权。
