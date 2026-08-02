# Whisper 词级时间戳调研

日期：2026-07-31
模式：Technical research
主题：Whisper 词级时间戳（word-level timestamps）的原理、优劣、能力边界与使用方法

## TL;DR

- **是什么**：语音转写时给每个词打精确起止时间，而非只给整句/整段。
- **原理**：Native Whisper 靠 cross-attention 权重 + DTW（动态时间规整）从注意力矩阵里反推词位置，是转写的**副产品**，不是模型优化目标。
- **优点**：零额外推理开销；解锁逐词级应用（字幕、歌词同步、逐词高亮、剪辑对齐）；本地原生支持。
- **局限**：精度差，会取整到 1 秒，误差可达数秒；翻译场景不可靠；端到端模型根本不为对齐设计。
- **选型**：要精度和生产可用 → **WhisperX**（wav2vec2 forced alignment）；要词置信度 → **whisper-timestamped**；快速验证 → native。

---

## 1. 是什么

**词级时间戳（word-level timestamps）** = 在语音转文字时，给**每一个词**打上精确的起止时间 `start` / `end`（秒），而不只是给整句/整段打时间戳。

```
segment 级：  [00:00 - 00:03]  "今天天气真好"
词级：        [00:00.2-00:00.5]今天  [00:00.5-00:00.9]天气  [00:00.9-00:01.3]真好
```

## 2. 技术原理（理解一切的基础）

Whisper 是**端到端 Transformer ASR**，它原生**不是为时间戳精度设计的**。词级时间戳是靠"挖模型内部状态"得到的，核心机制是 **cross-attention（交叉注意力）+ DTW（动态时间规整）**：

1. Whisper 解码时，decoder 和音频（mel-spectrogram）之间产生 **cross-attention 权重**——这套权重天然编码了"文本 token 和音频时间帧"的对齐关系（是转写的副产品，不是优化目标）。
2. 由 OpenAI 的 Jong Wook Kim 提出的方法：对这个 attention 权重矩阵跑 **DTW（Dynamic Time Warping）**，把每个文本 token 对齐到音频时间轴上，从而算出每个词的起止时间。

> 一句话：词级时间戳是从注意力权重里"反推"出来的，不是模型直接预测的。这决定了它所有的优点和局限。

## 3. 优点

| 优点 | 说明 |
|------|------|
| **零额外推理开销** | 直接复用已有的 attention 权重，不需要再跑一遍模型 |
| **解锁逐词级应用** | 动态字幕、歌词同步、视频自动剪辑、逐词高亮、语音质检对齐——没有词级时间戳这些都做不了 |
| **本地原生支持** | OpenAI Whisper 开源版自带 `--word_timestamps`，API 有 `timestamp_granularities`，开箱即用 |

## 4. 局限（坑都在这）

1. **精度差，会"取整到 1 秒"** ⚠️
   Native Whisper 的 timestamp token 分辨率太粗，时间戳经常 snap 到整秒边界——对"词"这个粒度来说完全不可用（`whisper-timestamped` 文档原话：too inaccurate for words）。

2. **几秒级误差**
   WhisperX 文档实测：native 时间戳是 utterance 级的，"误差可达数秒"（inaccurate by several seconds）。

3. **端到端模型的根本局限**
   cross-attention 权重是转写副产品，不是为对齐优化的；30 秒窗口 + mel 帧粒度限制了 sub-word 精度，模型会把时间戳"snap"到粗糙的边界上。

4. **翻译场景完全不可靠**
   翻译时词序、语义都会变，timestamp 对不上。LessWrong 的建议：**要词级时间戳就做 transcription（转写），别用 translation（翻译）**。

5. **不连续语音处理差**
   犹豫、填充词（uh/um）会以特殊标记 `[*]` 出现，破坏对齐。

## 5. 主流方案对比

| 方案 | 机制 | 精度 | 适合场景 |
|------|------|------|---------|
| **Native Whisper** `--word_timestamps` | cross-attention + DTW | ❌ 差（取整、数秒误差） | 粗略对齐、快速验证 |
| **whisper-timestamped** | DTW + 启发式平滑 + **词置信度** | ⚠️ 比 native 好 | 实验/原型，非生产；唯一能免费给**词置信度**的 |
| **WhisperX** ⭐ | **放弃 Whisper 时间戳**，用外部 **wav2vec2 音素模型做 forced alignment** | ✅ **最高** | 生产级、需要批量+VAD+说话人分离 |
| **CrisperWhisper** | 调整 tokenizer 修复取整问题 | ✅ 高 | 追求精度但不想引入外部模型 |

**选型建议**：
- 要**精度**和**生产可用** → **WhisperX**（行业标准，INTERSPEECH 2023 论文背书）
- 要**词置信度**（知道哪些词识别不准）→ **whisper-timestamped**（唯一原生支持）
- 只要**快速试一下** → native Whisper 一行命令

## 6. 怎么用（三套代码）

### 6.1 OpenAI API（最省事）

```python
from openai import OpenAI
client = OpenAI()

# 词级时间戳必须配 verbose_json
result = client.audio.transcriptions.create(
    model="gpt-4o-transcribe",   # 或 "whisper-1"
    file=open("audio.mp3", "rb"),
    response_format="verbose_json",
    timestamp_granularities=["word"],   # 也可以 ["word", "segment"] 同时拿
)

for w in result.words:
    print(f"{w.start:.2f}-{w.end:.2f}s  {w.word}")
```

关键参数：**`timestamp_granularities=["word"]` + `response_format="verbose_json"`** 两个必须一起设置。词级时间戳在非 verbose_json 格式下不会返回。

### 6.2 whisper-timestamped（带词置信度）

```bash
pip install whisper-timestamped
```

```python
import whisper_timestamped as whisper

audio = whisper.load_audio("AUDIO.wav")
model = whisper.load_model("medium", device="cpu")
result = whisper.transcribe(model, audio, language="zh")

# 每个 word 带 start, end, confidence
for seg in result["segments"]:
    for w in seg["words"]:
        print(f"{w['start']:.2f}-{w['end']:.2f}s  conf={w['confidence']:.2f}  {w['text']}")
```

注意：`compute_word_confidence` 和 `include_punctuation_in_confidence` 可控制置信度行为。该库官方声明适合实验，非重生产用途。

### 6.3 WhisperX（生产级，精度最高）

```bash
pip install whisperx
```

```python
import whisperx

device = "cuda"  # Mac 用 "cpu" 或 "mps"
audio = whisperx.load_audio("audio.mp3")

# 1) 批量转写（VAD 预处理，70x 实时）
model = whisperx.load_model("large-v2", device, compute_type="float16")
result = model.transcribe(audio, batch_size=16)

# 2) forced alignment —— 这是精度关键，用 wav2vec2 重对齐
model_a, metadata = whisperx.load_align_model(
    language_code=result["language"], device=device)
result = whisperx.align(result["segments"], model_a, metadata,
                        audio, device, return_char_alignments=False)

# 3) 说话人分离（可选，需 HF_TOKEN）
# diarize_model = whisperx.DiarizationPipeline(token=HF_TOKEN, device=device)
# result = whisperx.assign_word_speakers(diarize_model(audio), result)

for seg in result["segments"]:
    for w in seg["words"]:
        print(f"{w['start']:.2f}-{w['end']:.2f}s  {w['word']}")
```

WhisperX 三步：批量转写（`--without_timestamps True`，1 forward pass/sample）→ wav2vec2 forced alignment → 可选说话人分离（pyannote-audio）。VAD 预处理降低 WER 和音频幻觉。

## 7. 一句话总结

> Native Whisper 的词级时间戳是"从注意力权重里反推的副产品"，能用但精度差（取整、数秒误差）；**真要生产级精度，上 WhisperX**——它用独立的音素模型做 forced alignment，是当前业界最优解。

---

## Sources

- [whisper-timestamped (linto-ai) — DTW + cross-attention + 词置信度](https://github.com/linto-ai/whisper-timestamped)
- [WhisperX — wav2vec2 forced alignment + VAD + diarization](https://github.com/m-bain/whisperX)
- [WhisperX 论文 (INTERSPEECH 2023)](https://www.isca-archive.org/interspeech_2023/bain23_interspeech.pdf)
- [CrisperWhisper — tokenizer 调优修复取整 (arXiv:2408.16589)](https://arxiv.org/html/2408.16589v1)
- [OpenAI API Reference — Create transcription](https://developers.openai.com/api/reference/resources/audio/subresources/transcriptions/methods/create/)
- [OpenAI 社区：word + segment 时间戳](https://community.openai.com/t/word-level-timestamps-and-sentence-timestamps-together/666462)
- [LessWrong：word-level timestamps 讨论（含翻译不可靠警告）](https://www.lesswrong.com/posts/eoCNoG92HrvemW4DR/whisper-s-word-level-timestamps-are-out)
