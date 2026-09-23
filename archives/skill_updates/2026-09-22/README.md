# 写作技能沉淀、本地路由与编码规则导入

- 新增 `rules/skills/workflow_wechat_article_stormzhang.md`，根据本地总结提炼八步人机协作流程，原 `workflow_wechat_article.md` 保留。
- 五个 writing-skill 路由优先读取本地 clone，正文相对引用按正文目录解析；GitHub 仅保留来源与缺失时备用。不自动拉取更新。
- 深度调研中的两处外部写作链接改为走本地路由；技能索引新增八步流程入口。
- ODP-CLEARING 新增 Codex／Zcode 共用 `AGENTS.md` 和编码规则副本，不修改 `CLAUDE.md`、`.claude/` 或业务代码。

## 归档与验证

本轮修改前原版位于 `originals/`，SHA-256 清单在 `manifest.json`。新 skill 在临时目录按 Codex skill 格式校验通过，所有改动后的本地链接和五个写作正文路径检查通过；原总结和原公众号工作流未改动。

ODP-CLEARING 的 Codex 真实只读新会话通过规则预检。Zcode 加载器确认支持 `AGENTS.md`，但 plan 模式会话因尚未选择模型而失败，不能声称真实会话通过。详见目标项目 `docs/AGENT_RULES_VERIFICATION.md`。

按用户指定，本次技能采用 `rules/skills/*.md` 和 `INDEX.md` 发现链，不另建全局 skill 或自动安装客户端插件。
