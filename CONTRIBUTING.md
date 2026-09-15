# Contributing / 贡献指南

Thanks for helping keep Agent Atlas current. 欢迎补充与纠错。

## Add or fix a resource / 增加或修正资源

Edit `data/resources.json`. Each entry:

```json
{
  "topic": "agentic_rl",            // must be an existing module key in data/content.json
  "level": "core",                  // intro | core | deep
  "type": "official",               // official | course | video | blog | paper | code | book
  "lang": "en",                     // en | zh
  "track": "both",                  // both | job | research
  "title": "TRL GRPO Trainer docs",
  "url": "https://huggingface.co/docs/trl/grpo_trainer",
  "hours": 2,
  "must": true,                     // part of the ~150 h core path; keep this rare
  "why": {"en": "…≤ 20 words…", "zh": "…≤ 34 字…"}
}
```

Rules / 规则

- Verify the URL resolves on the day you submit and mention the date in the PR. 提交前确认链接可达，并在 PR 里写明访问日期。
- Prefer primary sources (official docs, the authors' own posts, the paper) over secondary summaries. 优先一手来源。
- Keep `why` short and specific: what it teaches and why it matters, with the year if known. 说明它教什么、为什么重要，尽量带年份。
- Do not add more than one `must` per PR without discussion. `must` 条目影响核心路径时长，请先讨论。
- One PR per topic is easier to review. 一个 PR 只改一个模块最好审。

## Add a paper / 增加论文

Edit `data/papers.json`:

```json
{"date": "2025-03", "title": "…", "authors": "First Author et al. (Org)", "url": "https://arxiv.org/abs/…", "arxiv": "2503.xxxxx", "area": "rl", "why": {"en": "…", "zh": "…"}}
```

`area` is one of: foundations, reasoning, tool-use, memory, multi-agent, coding, computer-use, rl, evals, safety, protocol.
Timeline entries should be papers or releases that changed what people build or measure, not every strong paper. 时间线只收「改变了大家做什么或怎么衡量」的工作。

## Edit module text / 修改模块文案

Edit `data/content.json`. Every user-facing string is `{"zh": "...", "en": "..."}`; please update both languages, or mark the missing one clearly in the PR so a maintainer can fill it in.

## Build and check / 构建与检查

```bash
python3 build.py
```

The build fails loudly on unknown topics, duplicate URLs, or modules not assigned to a stage. Open `index.html` in a browser and check the changed module in both languages before submitting.
