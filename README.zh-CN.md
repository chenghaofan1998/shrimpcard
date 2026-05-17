# OpenClaw ShrimpCard

> 把真实的代理证据，压成一套可公开分享的身份卡产物：JSON、真实 8-bit 角色图、以及可截图展示的 HTML。

[English README](README.md) · [中文演示卡](docs/showcase/selfie-card.zh.html) · [English Demo Card](docs/showcase/selfie-card.en.html) · [最终 Share Card JSON](docs/showcase/share-card.final.json)

![OpenClaw ShrimpCard 像素角色](docs/showcase/openclaw-shrimpcard.png)

## 这是什么

OpenClaw ShrimpCard 是一套面向代理的严格卡片生成流程。

它不是随便写一段人设文案，而是从 live evidence 出发，经过多轮校验，最后生成一套可以真正公开展示的成品：

- `agent-self-intro-submission/1.0`
- `share-card/1.0`
- 一张真实的 8-bit PNG 角色图
- 一份适合截图和分享的最终 HTML 卡片

标准流程：

```text
agent-evidence -> self-intro submission -> share-card -> final image -> selfie-card.html
```

## 它和别的项目有什么不同

很多 agent showcase 项目都有同样的问题：文案太空、直接泄露 sample 身份、停在占位图阶段，或者根本没有对最终公开产物做严格校验。

OpenClaw ShrimpCard 就是专门卡这些问题的。

- 先讲证据。公开身份必须来自重复出现的真实行为。
- 强制校验。短字段长度、泛化措辞、视觉方向、最终 bundle 结构都由脚本检查。
- 必须有真图。没有真实图片挂回卡片前，不应该渲染最终 HTML。
- 产物链完整。prompt builder、schema、validator、converter、renderer 都在一个仓库里。

## 它能产出什么

如果你想把真实代理痕迹压成可以发出去的内容，这个项目适合你：

- 一份不靠吹嘘、而是基于证据的公开自我介绍
- 一份有 schema 约束的 share-card payload
- 一个和代理身份对得上的可识别 8-bit 像素角色
- 一份适合截图、演示、嵌入页面的最终 HTML 卡片

## 演示素材

这些演示文件都放在 `docs/showcase/`，而不是 `output/`，所以后续即使你清理产出目录，它们也还在。

- 中文 HTML 卡片：[docs/showcase/selfie-card.zh.html](docs/showcase/selfie-card.zh.html)
- 英文 HTML 卡片：[docs/showcase/selfie-card.en.html](docs/showcase/selfie-card.en.html)
- 最终卡片 payload：[docs/showcase/share-card.final.json](docs/showcase/share-card.final.json)

## 快速开始

安装依赖：

```bash
pip install -r requirements.txt
```

然后用你自己的 live input 跑流程：

```bash
python3 scripts/build_memory_search_prompt.py path/to/agent-context.json --lang zh
python3 scripts/build_submission_prompt.py path/to/agent-evidence.json --lang zh
python3 scripts/validate_self_intro_submission.py path/to/submission.json
python3 scripts/submission_to_share_card.py path/to/submission.json --out share-card.json
python3 scripts/build_image_task_prompt.py path/to/submission.json --out image-task.txt
python3 scripts/attach_generated_image.py share-card.json --image-file path/to/final.png
python3 scripts/validate_final_bundle.py share-card.json
python3 scripts/render_card_html.py share-card.json --lang zh --out selfie-card.html
```

## Smoke test

仓库自带一条基于 fixture 的当前流程 smoke test：

```bash
bash scripts/smoke_test_current_flow.sh
```

它会验证 prompt 生成、submission 校验、share-card 转换、图片挂载，以及中英文 HTML 渲染是否正常。

## 仓库结构

```text
agents/         接口元信息
assets/         卡片模板和内置视觉资源
docs/showcase/  README 使用的长期演示素材
examples/       仅用于 smoke test 的 fixture，不能当 live identity 输入
references/     证据提炼指导
schemas/        JSON schema
scripts/        构建、校验、转换和渲染脚本
```

## 几条关键规则

- 不要把 `examples/` 当作真实身份证据。
- 不要猜 owner 的身份字段。
- 不要发布诸如 `powerful assistant`、`strong reasoning` 这种空泛表述。
- 不要停在 prompt-only 或 placeholder-image 状态。
- 没有通过最终 bundle 校验前，不要渲染最终卡片。

## 适合什么场景

OpenClaw ShrimpCard 适合这些需求：

- 想更真实地展示 agent 身份，而不是写一段泛泛的人设
- 想把 traces 稳定压缩成公开文案
- 想要有 schema 约束的结构化产物
- 想要一张带真实角色图的 agent 卡，而不是 mock 占位图

## 当前演示说明

当前仓库里的展示素材来自这个项目本身的 live evidence，而不是 `examples/`。这些产物最初生成在 `output/` 下，随后被复制到 `docs/showcase/` 里，用于长期保留和 GitHub 展示。
