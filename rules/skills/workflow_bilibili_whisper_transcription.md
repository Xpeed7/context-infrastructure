# 视频下载与语音识别工作流

## 元数据
- 类型: Workflow
- 适用场景: Bilibili/YouTube 视频批量下载 + Whisper 语音识别
- 创建日期: 2025-02-12
- 最后更新: 2026-07-31
- 原项目已归档（不再保留在 workspace 中）

## 路径约定

- 临时下载与中间产物：`tmp/<task_name>/`
- 最终可长期保留的 transcript：`adhoc_jobs/videos_transcribe/transcripts/`
- 最终默认只保留**不带时间轴的纯文本脚本**，文件名建议：`YYYYMMDD_platform_videoid_short_slug.md`
- 音频、`.srt`、`.vtt`、`.tsv`、`.json` 等中间产物在 transcript 落盘后清理到废纸篓

## 核心流程

**三阶段工作流：**

1. **获取列表** → 使用 yt-dlp 提取视频ID（注意B站API限制，可能返回352错误）
2. **单线程下载** → 逐个下载音频，每次间隔2-3秒，避免触发反爬
3. **多进程转录** → 并行运行Whisper，4-8个进程，根据硬件选择模型大小

## 关键决策

| 决策点 | 选择 | 原因 |
|--------|------|------|
| 下载并发 | 单线程 | 避免触发B站反爬机制 |
| 转录并发 | 多进程（4-8） | CPU密集，充分利用多核 |
| 模型选择 | 根据需求 | 见下表 |
| 输出格式 | 最终保留纯文本 transcript | 后续检索更稳定，中间产物可回收 |

## Whisper 模型选择

| 模型 | 参数量 | 速度（CPU） | 准确度 | 推荐场景 |
|------|--------|-------------|--------|----------|
| tiny | 39M | 1-2分钟/10分钟 | 较低 | 快速预览 |
| base | 74M | 2-5分钟/10分钟 | 中等 | 平衡选择 |
| small | 244M | 5-10分钟/10分钟 | 较高 | 日常使用 |
| medium | 769M | 10-20分钟/10分钟 | 高 | 高质量需求 |
| large-v3 | 1550M | 20-60分钟/10分钟 | 最高 | 最高质量要求 |

**性能参考**：12个视频（3.5小时）+ large-v3 + 7进程 ≈ 20分钟

## LLM 后处理

Whisper 原始输出通常需要后处理：

1. **转换为简体中文** — 识别可能为繁体
2. **添加标点符号** — 根据语义添加逗号、句号、问号
3. **合理分段** — 按主题划分段落，添加小标题
4. **纠正术语** — 专业名词识别错误（如"木质布"→"木质部"、"筛管细胞"）
5. **优化可读性** — 调整语序、补充缺失内容

## 踩坑记录

| 问题 | 现象 | 解决方案 |
|------|------|----------|
| **352错误** | 请求被B站拦截 | 添加User-Agent/Referer headers，增加延迟，或手动获取ID |
| **404错误** | 视频已删除或ID错误 | 验证ID有效性，跳过无效视频，记录失败ID |
| **内存不足** | 多进程转录时内存溢出 | 减少并行进程数（4-6个），使用较小模型，分批处理 |
| **下载不完整** | .m4a文件无法播放 | 检查文件大小，重新下载，添加完整性验证 |
| **转录太慢** | large-v3单个视频20-60分钟 | 选择合适模型大小，使用GPU加速，分块处理长视频 |

## 最佳实践

**下载阶段：** 单线程 + 2-3秒延迟 + User-Agent headers + 只下载音频 + 记录失败ID

**转录阶段：** 多进程（4-8） + 指定language参数 + 跳过已处理文件 + 根据硬件选择模型

**落盘阶段：** 在 `tmp/` 完成下载和转录，整理出纯文本脚本后移入 `adhoc_jobs/videos_transcribe/transcripts/`

**清理阶段：** transcript 落盘后删除或回收音频、时间轴字幕和 sidecar 文件，只保留最终脚本

**质量优化：** 关键内容用large-v3，快速预览用base/small，必要时人工校对

**错误处理：** 实现重试机制，验证文件完整性，处理异常避免脚本中断

## 对话类视频的说话人分离（Speaker Diarization）

适用：访谈、尬聊、辩论、播客等**多人对话**视频。单人讲解类视频用不上，不要无脑套用。

### 为什么需要单独一步

通用 ASR（Whisper、火山 bigmodel 等）只输出"谁说了什么"的文本流，不带说话人归属。对话类视频如果直接落盘，读者无法区分轮次——"stay safe man" 是 UP 主说的还是对方说的，全靠猜。声纹分离（diarization）补的就是这一层：用声音特征给每段时间打上匿名 speaker 标签，再由人（或 LLM）根据内容映射成身份。

### 核心流程（三阶段）

1. **ASR 转写**：用现有引擎（火山/Whisper/SenseVoice）跑一遍，**必须开启 `show_utterances` 拿到带时间戳的分句**，不能只要纯文本。时间戳是后面和声纹对齐的锚点。
2. **声纹分离**：用 pyannote.audio 对同一音频跑 diarization，输出 `[(start_sec, end_sec, speaker_id)]` 时序片段。speaker_id 是匿名编号（SPEAKER_00/01/...），不是身份。
3. **时间轴对齐 + 身份映射**：遍历每个 ASR 分句，取中点时间，落入哪个声纹片段就标那个 speaker_id。得到匿名标签稿后，**根据语义内容把匿名 ID 映射成身份**（Alan / 警察 / 健身小哥）。最后一步必须人工或 LLM 介入，声纹给不出身份。

### 引擎选择

| 方案 | 说话人来源 | 卡点 | 适用 |
|------|-----------|------|------|
| **火山极速版 (flash)** | ❌ 实测不返回 speaker | 极速版官方明确不支持 diarization | 不要用，已验证 |
| 火山标准版 (submit/query) | API 原生 `enable_speaker_info` | 需额外开通 `volc.bigasr.auc`（独立计费）+ 音频挂公网 URL + 英文效果无保证 | 中文音频、已开通资源时 |
| **pyannote.audio（推荐）** | 本地声纹聚类 | 模型需从 HF 下载（gated，要点协议）+ CPU 跑得慢 | 任何语言，纯声学特征，英文对话是主场 |

默认走 pyannote。理由：语言无关（纯声学）、效果稳、不依赖额外云资源开通。

### pyannote 落地细节

**依赖版本锁定（重要，踩坑点）：**
- `pyannote.audio==3.3.2`（4.x 引入了 `speaker-diarization-community-1` 这个额外的 gated 依赖，更难下）
- `torch==2.4.1` + `torchaudio==2.4.1`（pyannote 3.x 用了已废弃的 `torchaudio.AudioMetaData`，新版本会报错）
- `huggingface_hub<0.26`（新版废弃了 `use_auth_token` 参数，pyannote 3.x 内部硬编码用旧参数名）

**模型（三个，全部 gated，需 HF 账号点"Agree and access"）：**
- `pyannote/speaker-diarization-3.1`（pipeline 配置）
- `pyannote/segmentation-3.0`（分段子模型，小文件）
- `pyannote/wespeaker-voxceleb-resnet34-LM`（声纹 embedding，~26MB，LFS 大文件）

**国内网络下不动的应对：**
- HF 的 xet CDN（cas-bridge.xethub.hf.co）和 hf-mirror 的 LFS 都可能被 SSL 断连
- 小文件（segmentation、config）走 `HF_ENDPOINT=https://hf-mirror.com` 通常能下
- LFS 大文件（wespeaker 的 pytorch_model.bin）若镜像也不行，**手动浏览器下载后放进 HF 缓存目录**：
  - 缓存结构：`~/.cache/huggingface/hub/models--{org}--{model}/{refs,blobs,snapshots}`
  - blob 文件名必须是 LFS sha256 oid（`git lfs` 指针文件里有，用 `shasum -a 256` 校验）
  - snapshot 目录里软链指向 blob
- 放好后设 `HF_HUB_OFFLINE=1` 强制本地模式，绕过下载校验

**pipeline 构造（绕过自动下载）：**
- `Pipeline.from_pretrained("pyannote/speaker-diarization-3.1")` 内部会对 embedding 模型调 `hf_hub_download`，offline 模式下校验 etag 仍可能失败
- 解法：手动构造 `SpeakerDiarization(segmentation=Model对象, embedding=Model对象, ...)`，把两个子模型都用 `Model.from_pretrained(checkpoint=本地路径, hparams_file=config路径)` 显式加载后传入
- pipeline 超参用 3.1 默认值：`clustering.threshold=0.7045654963945799, min_cluster_size=12`

**性能：** 10 分钟音频，M 芯片 CPU，约 20 分钟（多核满载）。不是实时的，预留时间。

### 对齐策略

```python
# 每个 ASR 分句取中点，落入哪个声纹片段就标那个 speaker
mid_sec = (start_ms + end_ms) / 2 / 1000
speaker = speaker_at(mid_sec)  # 二分查找覆盖该时间点的片段
```

- 多个片段重叠时取**持续时间最长**的那个（更可能是主说话人）
- 完全没有片段覆盖的间隙（静音），取最近片段的 speaker 填充

### 身份映射的把关纪律（踩坑记录）

**声纹分离的固有局限：**
- pyannote 按声音特征聚类，**不同场景里声学相近的人会被合并到同一 ID**。实测一个视频里场景 2 的陌生人和场景 5-7 的墨西哥女孩被归到了同一个 SPEAKER_05，但语义上明显是两个人。
- 同理，**快节奏问答**（警察那段）pyannote 可能把连续几个轮次都标成同一个 speaker，因为切换太快、片段没切到。出现"Alan 自问自答"式的段落时，要怀疑是标签串了。

**核对纪律（重要）：**
- 不能盲信声纹标签。得到匿名标签稿后，**对每个场景通读一遍，按语义核对每轮对话的归属**。
- 重点核对：对话节奏快的段落（轮次间隔 <2 秒）、说话人切换密集的段落。
- 判断依据：内容逻辑（谁问谁答）、人称代词（I/you/he）、上下文连续性。声纹给线索，语义做裁决。
- 宁可人工修正，不要把"标签和内容对不上"的地方糊弄过去。

### 与原工作流的衔接

这套 diarization 是原"下载 → 转写 → 后处理"流程的**可选增强步骤**，插在转写之后、后处理之前：

```
下载音频 → ASR 转写（保留 utterances 时间戳）→ [对话类?] → 声纹分离 → 时间轴对齐 → 身份映射 → 后处理（标点/分段/术语）→ 落盘
```

单视频救急时不必集成进 bili2text 工程，写一次性脚本即可：复用已有的 ASR 结果（`.b2t/transcripts/original/` 或探测接口的 raw response），只补 diarization 这一步。脚本和中间产物放 `adhoc_jobs/tmp_speaker_diarize/`，最终带说话人标注的稿子归档到 `adhoc_jobs/videos_transcribe/transcripts/`，文件名加 `_speaker` 后缀与无标注稿区分。

### 输出格式约定

```markdown
## 场景 N：场景标题（mm:ss-mm:ss）

**身份** [mm:ss]: 文本内容。

**身份**: 对话内容。
```

- 带时间戳方便核对原文
- 身份用具体角色名（Alan / 警察 / 健身小哥），判断不了的用 `说话人A/B`
- 按场景分节，场景内按对话轮次组织

