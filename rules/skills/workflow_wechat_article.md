# 公众号文章创作工作流

## 元数据

- **类型**: Workflow
- **适用场景**: 需要创作一篇完整的公众号/博客文章，从选题、素材组织到成稿，希望全过程留痕在单一目录里
- **输出位置**: `contexts/writing/<slug>_<YYYYMMDD>/`
- **创建日期**: 2026-07-07

## 目标

为一篇文章提供一个自包含的容器：把选题动机、思考过程、素材引用、草稿和成稿收拢在同一个目录里，让一篇文章的生命周期可追溯、可检索。

这个 skill 解决的核心问题是：现有的调研、分析、改写、配图四个 skill 各管一段，但缺一个把它们组织起来的目录约定，导致一篇文章的草稿、成稿、思考笔记散落在不同地方，失去关联。

## 边界

这个 skill 做：

- 定义单篇文章的目录结构和文件分工
- 串联现有 skill 成一条链（选题 → 调研 → 分析 → 改写 → 配图）
- 约定素材的引用方式（指向 `survey_sessions`，不复制内容）
- 承载选题判断：这个题目值不值得写、需要多深的调研

这个 skill 不做：

- 不替代调研、分析、改写本身——路由到对应 skill
- 不做发布（Pelican 博客上传、公众号发布由用户显式触发时再走对应流程）
- 不强制所有文章走完整流程。短文可以只建 `meta.md` + `final.md`，跳过调研和 scratchpad

## 目录结构

每篇文章一个目录，建在 `contexts/writing/` 下：

```
contexts/writing/<slug>_<YYYYMMDD>/
  ├── meta.md          # 必需。选题动机、目标读者、状态、素材来源
  ├── scratchpad.md    # 可选。思考过程、论点演化（analytical_writing 的 Phase A-D 产出）
  ├── draft.md         # 可选。草稿，迭代到成稿
  ├── final.md         # 成稿。公众号成稿即权威版本
  └── assets/          # 可选。封面、配图（guizang_social_card 产出入这里）
```

命名约定：`<slug>` 用英文短语 snake_case，`<YYYYMMDD>` 是创建日期 8 位紧凑格式。示例：`agentic_ai_reliability_20260707/`。

`meta.md` 是唯一必需文件，先于其他一切创建。一篇文章只要有了 `meta.md`，目录就成立，后续文件按需补齐。`final.md` 一旦存在即代表文章进入可发布状态。

### 素材引用约定

深度调研的产出留在 `contexts/survey_sessions/`，**不在 writing 目录里复制副本**。在 `meta.md` 的素材来源区写路径引用：

```markdown
## 素材来源
- 调研报告：`contexts/survey_sessions/shenzhen_talent_rental_housing_20260707.md`
- 相关思考：`contexts/thought_review/ai_agent_term_inflation_20260707.md`
```

理由：单一信息源。调研报告可能被多篇文章引用，复制会产生版本漂移。引用路径让原始素材保持唯一权威。

## 可用资源

- 深度调研：[`workflow_deep_research_survey.md`](./workflow_deep_research_survey.md)
- 分析写作：[`workflow_analytical_writing.md`](./workflow_analytical_writing.md)（Thesis Catalog L1-L6）
- 文风改写：[`workflow_rewrite_in_my_style.md`](./workflow_rewrite_in_my_style.md)
- 配图：[`workflow_guizang_social_card.md`](./workflow_guizang_social_card.md)
- 写作约束：`rules/COMMUNICATION.md`

## 建议工作方式

### 选题阶段（本 skill 自己完成）

先在 `meta.md` 里回答几个问题，把选题判断显式化。这些问题本身比答案更重要——它们筛掉不值得写的题目：

- 为什么是现在写这个？触发点是什么（一次对话、一篇论文、一个产品发布、一个反复出现的困惑）
- 这篇文章要让读者带走什么？一个可复用的判断框架，还是一个具体的事实核对
- 这个选题和已有的调研、思考是什么关系？有没有现成素材可复用

如果选题判断走不通（"为什么是现在"答不上来，或"读者带走什么"只能说出"介绍一下 X"），建议不写，或回去补调研。

### 路由到现有 skill

选题明确后，按文章复杂度决定走哪些 skill。**不是每篇都要全走**：

- 需要事实核查 / 深度调研 → `workflow_deep_research_survey.md`，产出落 `survey_sessions/`，在 `meta.md` 引用
- 有调研素材，需要从"事实"走到"判断" → `workflow_analytical_writing.md`，产出落 `scratchpad.md`
- 草稿已成，需要统一成作者本人文风 → `workflow_rewrite_in_my_style.md`，产出落 `final.md`
- 需要封面或社媒配图 → `workflow_guizang_social_card.md`，产出入 `assets/`

一篇评论型短文（基于作者已有观点，无新调研）可以跳过调研和分析，直接从 `meta.md` → `final.md`。一篇深度调研长文可能四个 skill 全走。路由判断本身也是选题阶段的一部分，写在 `meta.md` 里。

### 成稿后的去向

`final.md` 是权威成稿。发布时按目标平台分流：

- **公众号**：成稿就在 writing 目录里，复制到公众号编辑器
- **个人 Pelican 博客**：复制到 `contexts/blog/content/` 并加 Pelican frontmatter（这是该目录的既有约定，由发布动作触发，不预先创建）

发布不在本 skill 范围内。只有用户显式要求时，才按对应流程执行。

## 验收标准

满足以下条件才算一篇文章目录成立：

1. 目录存在于 `contexts/writing/`，命名为 `<slug>_<YYYYMMDD>`
2. `meta.md` 存在，且包含：选题动机、目标读者、状态（drafting / ready / published）、素材来源（如适用）
3. 若 `meta.md` 的素材来源引用了文件，被引用的文件必须真实存在（指向 `survey_sessions` 或 `thought_review`）
4. `final.md` 存在时，必须经过 `rules/COMMUNICATION.md` 的风格自查

## 已知陷阱

- **目录只建不填**：建了 `meta.md` 但选题判断的三个问题空着，目录变成无意义的占位。判断标准：`meta.md` 的选题动机区不能是空壳。如果三天内仍填不出"为什么是现在写这个"，这个选题大概率不成立，删掉目录或回去补调研。

- **素材复制而非引用**：图省事把 `survey_sessions` 的内容复制进 `scratchpad.md`，之后调研报告更新，文章里的副本不会同步。强制用路径引用，不复制正文。`scratchpad.md` 里可以摘录关键段落并标注来源，但不能整篇复制。
