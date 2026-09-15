# Agent Atlas

**中文 | English** · A bilingual, community-maintainable roadmap for learning LLM agents, from the first tool-calling loop to frontier research, ending in a project of your own.

🌐 Live page: `https://ankky-zhao.github.io/llm-agent-roadmap/` (enable GitHub Pages, see below)

## 这是什么 / What it is

- **领域地图 / Landscape** · 五层结构（模型层、单 agent 核心机制、系统层、应用领域、贯穿的保障层），每个节点链接到对应模块。
- **学习路线 / Learning path** · 7 个阶段、26 个模块。每个模块含「为什么重要」、要能说清楚的概念、自检问题、按了解 / 掌握 / 深入分层的资源，以及一个动手任务；前沿模块另附开放问题。
- **277 条经核验的资源** · 官方文档、课程、视频、博客、论文、代码、书。每条链接在 2026-09-15 逐一访问确认可达。标「必读」的约 150 小时构成核心路径。
- **99 篇关键论文时间线** · 2020 到 2026，按方向筛选，每篇一句话说明它改变了什么。
- **项目阶梯 / Project ladder** · 从一个周末到两个月，按求职 / 科研分岔。
- **科研入门六步、自检清单**，以及求职 / 科研两条路线的筛选。
- 进度勾选保存在浏览器本地（localStorage），不上传任何数据。

## 仓库结构 / Repository layout

```
data/
  content.json     # 阶段、模块、领域地图、项目阶梯、科研路径、自检清单（中英双语）
  resources.json   # 资源条目：topic, level, type, lang, track, title, url, hours, must, why{zh,en}
  papers.json      # 论文时间线：date, title, authors, url, arxiv, area, why{zh,en}
template.html      # 页面模板（HTML + CSS + JS，无外部依赖，字体来自 Google Fonts）
build.py           # 把 data/*.json 注入模板，生成 index.html
index.html         # 生成产物，直接用于 GitHub Pages
```

## 本地构建 / Build locally

```bash
python3 build.py        # 生成 index.html（无第三方依赖，Python 3.8+）
```

`build.py` 会做基本一致性检查：每个模块都属于某个阶段、每条资源的 topic 都存在、URL 不重复。

## 部署到 GitHub Pages / Deploy

1. Fork 或 push 本仓库。
2. Settings → Pages → Source 选 **GitHub Actions**。
3. `.github/workflows/pages.yml` 会在每次 push 到 `main` 时重新构建并发布。

或者更简单：Source 选 **Deploy from a branch** → `main` / root，直接发布已提交的 `index.html`。

## 自动维护 / Maintenance

- `.github/workflows/link-check.yml` 每周一检查所有链接，发现 404 或无法连接时自动开一个 `link-rot` issue（403/429 只记为无法验证，不算坏链）。也可以在 Actions 页手动运行。
- 内容更新（新论文、新资源）需要人工审阅后合并，见 CONTRIBUTING.md。

## 贡献 / Contributing

见 [CONTRIBUTING.md](CONTRIBUTING.md)。简单说：改 `data/` 下的 JSON，跑一次 `python3 build.py`，提交 PR。新增资源请附上你访问过该链接的日期。

## 许可 / License

- 内容（`data/`、文案）：[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- 代码（`template.html`、`build.py`）：MIT

Curated by Anqi (Ankky) Zhao · TUM. 资源与论文的版权归各自作者所有。
