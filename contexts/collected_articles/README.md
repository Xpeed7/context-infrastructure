# 外部文章收录库

收录工程外作者公开发表的文章（教程、思考、方法论），作为个人学习参考库。内容只做本地私藏，不对外发布。

## 定位与分工

- 本目录收 stormzhang 以外的外部作者；stormzhang 专属收录库在工程外：`/Users/chenruiyan/2026-project/stormzhang/articles/`（规范见该目录 README.md）。
- 对收录文章的调研、分析、二次创作，放 `contexts/survey_sessions/` 和 `contexts/writing/`，引用这里的收录路径，不复制内容。
- 从平台页面复制来的原始草稿先进 `contexts/draft/`，整理入库后原稿由用户决定是否删除。

## 目录结构

```
collected_articles/
├── README.md        # 本文件：收录规范
├── INDEX.md         # 收录总索引，每收录一条更新一行
├── tutorials/       # 教程：有操作主线，跟着做能完成一件事
├── thoughts/        # 思考：观点、复盘、行业观察类文章
└── prompts/         # 从文章中抽出可单独使用的 prompt（按需创建）
```

新类型（访谈、翻译、演讲稿等）出现时，新增同级目录，同步更新本文件和 INDEX.md。

## 收录规范

- **整理原则**：只清理平台 UI 噪音（快捷键提示、订阅引导、签名尾巴）、恢复标题层级和列表结构，正文措辞不改动；嵌在正文里的 prompt 用代码块包裹，保证可复制。
- **文件命名**：`YYYYMMDD_english_slug.md`，日期用原文发布日期；查不到时用收录日，并在 front-matter 标注。
- **原文 URL**：能查到就填；查不到写「待补」，日后补上。

## Front-matter 模板

```markdown
---
title: 原文标题
author: 作者名（平台 handle）
source: 原文 URL（未知写「待补」+ 平台说明）
published: YYYY-MM-DD（未知写 unknown）
collected: YYYY-MM-DD
type: tutorial / thought
tags: []
---

（全文正文）

## 收录备注

（可选：为什么收录、和哪些项目或文章有关联）
```

## 收录流程

1. 核对来源平台、作者和发布日期。
2. 清理噪音、恢复格式，按命名规则起文件名，填 front-matter。
3. 文末加收录备注（为什么收录、关联项目）。
4. 更新 INDEX.md。
