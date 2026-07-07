我搜了一轮公开仓库，优先挑了和你这次主题最接近的 5 个 GitHub 项目。结论先说：有不少“AI 生成测试用例”的 repo，但真正同时覆盖 需求文档 -> 测试用例 -> Gherkin/Jira/自动化 的并不多，很多还是 PoC 或作品集项目。下面这 5 个是相对更接近的。
KunalDutta03/test-case-generation-and-jira-integration
简介：一个比较贴近你目标链路的 PoC，支持多格式需求文档摄取，用 RAG + Azure OpenAI 生成 Gherkin 测试用例，并带 QA 审批流和 Jira 注入。
特点：最像“产品化方案”，不是单纯 prompt demo。它有文档上传、向量检索、测试生成、人工审批、Jira 回写这几个关键环节，和你想做的流程重合度最高。

prashant1507/test-intellect-ai
简介：一个更完整的 Web 应用，支持从 Jira 或自由文本读取需求，生成 Gherkin 风格测试用例，写回 Jira，并继续跑 UI/API 自动化。
特点：它比很多 repo 多了一段“测试生成后继续执行”的闭环，还带 LangGraph agentic pipeline、Playwright 自动化、历史记录和审计。对你要研究“生成后如何衔接自动化”很有参考价值。

arunprasath403/TraceGenAI
简介：偏企业 traceability 的多 agent 方案，把 requirements、design、code context 串起来，最后输出可追踪的测试用例。
特点：它强调 deterministic pipeline、validation-first 和 SDLC traceability，不是只做测试文本生成。对“需求文档 + 开发文档联合生成测试资产”这件事，思路比单点 Gherkin 生成器更成熟。

viktoriqa/qa-ai-assistant-tool
简介：一个 QA 分析助手，把原始需求转成结构化测试资产，包括 test cases、gap report、risk assessment、test data spec、coverage matrix，并支持导出 Excel。
特点：它不以 Gherkin 为核心，而是把“测试设计前的 QA 分析层”做得更厚。对你这次方案里“先出 Jira 文本用例，再决定哪些转 Gherkin”这一步很有借鉴意义，尤其是 gap、risk、test data 这些中间产物。

marcobaturan/gherkin-generator
简介：一个很轻量的 Gherkin 生成器，输入 plain English 功能描述，输出 3-5 条 BDD 场景。
特点：它很简单，但也因此适合看“最小闭环”怎么做。适合作为你方案里的最小 demo 参考，不过它没有 Jira、审查、traceability，也没有自动化执行闭环。

我的判断：
如果你想看“最像你目标方案”的，先看 test-case-generation-and-jira-integration 和 test-intellect-ai。
如果你想看“更企业化的架构思路”，看 TraceGenAI。
如果你想看“测试设计中间层怎么补厚”，看 qa-ai-assistant-tool。
如果你只想看“最小 Gherkin 生成 demo”，看 gherkin-generator。
我这次检索里也发现一个现象：真正公开、成熟、开源、并且把 requirements -> Jira cases -> Gherkin -> automation 全链路做完整的 repo 其实不多，更多是局部方案。你的方向不是没人做，而是公开实现还比较碎。
如果你要，我下一步可以继续做两件事中的一个：
把这 5 个项目按“与你方案的匹配度”做一个对比表
深挖其中最有参考价值的 2 个 repo，拆它们的架构、prompt 流程和优缺点