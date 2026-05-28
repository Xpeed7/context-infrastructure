# Guizang Social Card 工作流

## 元数据

- **类型**: Workflow
- **适用场景**: 需要把文章、脚本、截图或产品说明转成小红书图文卡片、公众号封面图、社媒配图
- **依赖 Skill**: `~/.codex/skills/guizang-social-card-skill/SKILL.md`
- **创建日期**: 2026-05-28

## 目标

在当前 workspace 中稳定调用 `guizang-social-card-skill`，产出可直接发布或继续微调的社媒图文卡片，不把任务误路由到 PPT 或普通图片编辑流程。

## 边界

这个 skill 做：

- 路由到已安装的 Guizang Social Card 主 skill。
- 明确输入素材缺口（平台、比例、标题、截图/照片、风格偏好）。
- 约束输出目录与命名，保证后续可追踪和复用。

这个 skill 不做：

- 不替代 `~/.codex/skills/guizang-social-card-skill/SKILL.md` 里的版式规则与组件细节。
- 不处理完整演示文稿（PPT）生成。
- 不承诺超出主 skill 能力圈的视觉类型（例如纯摄影风格 OOTD 摆拍）。

## 可用资源

- 主 skill：`~/.codex/skills/guizang-social-card-skill/SKILL.md`
- 主 skill 参考资料：`~/.codex/skills/guizang-social-card-skill/references/`
- 主 skill 模板：`~/.codex/skills/guizang-social-card-skill/assets/`

## 建议工作方式

- 用户提到小红书图文、公众号封面、3:4 卡片、21:9+1:1 封面组图时，优先走这个 skill。
- 执行前先确认最低输入：目标平台、核心标题、可用素材（截图/照片/插图来源）、风格倾向。
- 如果用户只有文本没有图片，先一次性给出素材补齐选项，然后继续推进，不重复追问。
- 默认在当前任务目录创建 `social-card-<slug>/`，并按主 skill 约定放置 `assets/` 与 `output/`。

## 验收标准

满足以下条件才算完成：

1. 已明确路由并实际遵循 `guizang-social-card-skill` 的主文档，而非临时拼装模板。
2. 输出图片尺寸与目标平台一致（例如小红书 3:4、公众号 21:9 + 1:1）。
3. 输出文件在任务目录可追踪（至少包含源素材目录和渲染结果目录）。
4. 交付前完成一次可读性检查（标题可读、核心视觉不被裁切、无明显溢出）。

## 已知陷阱（当前版本）

- 常见失败是把任务误判为「做 PPT 封面」或「单张海报精修」，导致布局目标跑偏。触发词只要包含社媒卡片/组图/封面配对，优先使用本 skill。
- 另一个高频问题是只收文本不收素材，最终图像证据层不足。遇到教程、产品评测、数据解读类内容，必须优先索要或补齐截图/照片来源。
