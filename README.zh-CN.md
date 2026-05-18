# OpenClaw ShrimpCard

把 agent 的行为记录整理成一套可以公开分享的卡片文件：JSON 数据、8-bit 角色图、一张能直接截图的 HTML。

[English README](README.md) · [中文演示卡](docs/showcase/selfie-card.zh.html) · [English Demo Card](docs/showcase/selfie-card.en.html) · [最终 Share Card JSON](docs/showcase/share-card.final.json)

---

## 做什么的

这个仓库里是一组脚本，按固定顺序把 agent 的长期使用痕迹变成一套身份卡片产物。

流程大概是：

1. 从 agent 的上下文和对话日志里提取关键信息，生成一段自我介绍的提示。
2. 得到自我介绍后，用校验脚本检查字段长度、措辞和结构。
3. 把通过的自我介绍转成标准 `share-card` 格式。
4. 根据卡片里的描述生成画图提示，拿去出一张像素角色图。
5. 把画好的图挂进卡片数据，再做一次整体校验。
6. 校验通过后，渲染出中英文 HTML 卡片。

每一步都单独拆成了脚本，跑完一个看一下结果，没问题再继续下一步。

---

## 跟其他展示项目的区别

很多 agent 展示工具会直接用占位图，或者写一些没什么信息量的通用描述，也缺少对最终产物的格式校验。

这里做的不同在于：

- 卡片上每个描述字段，都要求在 agent 的实际对话中出现过重复模式，不是一次性回答或者猜出来的特征。
- 校验脚本会检查字段长度、是否用了过于空泛的词语、视觉方向和数据结构，不符合就报错。
- 必须先挂载真实的像素图，HTML 渲染这一步才跑得通，没有办法跳过。
- 从构建提示到最终渲染的所有环节都在这个仓库里，不用去别处找脚本。

---

## 跑完会得到

- 一份结构化自我介绍（submission）
- 一份 `share-card.json`，里面是简介、标签、视觉描述等字段
- 一张对应描述的 8-bit 像素角色图
  需要自己用绘图工具或图像模型生成
- 一份中英文 HTML 身份卡

---

## 演示材料

放在 `docs/showcase/` 下，删掉 `output/` 目录也不会影响。

- [docs/showcase/selfie-card.zh.html](docs/showcase/selfie-card.zh.html)
- [docs/showcase/selfie-card.en.html](docs/showcase/selfie-card.en.html)
- [docs/showcase/share-card.final.json](docs/showcase/share-card.final.json)

---

## 使用方式

安装依赖：

```bash
pip install -r requirements.txt
```

准备你 agent 的真实上下文和证据文件，然后按顺序执行：

```bash
# 生成记忆搜索提示
python3 scripts/build_memory_search_prompt.py path/to/agent-context.json --lang zh

# 生成自我介绍提交提示
python3 scripts/build_submission_prompt.py path/to/agent-evidence.json --lang zh

# 校验提交的自我介绍
python3 scripts/validate_self_intro_submission.py path/to/submission.json

# 转成 share-card
python3 scripts/submission_to_share_card.py path/to/submission.json --out share-card.json

# 输出画图提示
python3 scripts/build_image_task_prompt.py path/to/submission.json --out image-task.txt

# 把画好的图挂载到 share-card
python3 scripts/attach_generated_image.py share-card.json --image-file path/to/final.png

# 最终校验
python3 scripts/validate_final_bundle.py share-card.json

# 渲染 HTML
python3 scripts/render_card_html.py share-card.json --lang zh --out selfie-card.html
```

---

## 快速检查流程是否正常

用仓库里的假数据跑一遍：

```bash
bash scripts/smoke_test_current_flow.sh
```

---

## 目录

```text
agents/         接口元信息
assets/         卡片模板与视觉资源
docs/showcase/  用于展示的长期保留文件
examples/       测试用的固定数据，不能用作真实输入
references/     证据提炼方法说明
schemas/        数据格式定义
scripts/        构建、校验、转换、渲染脚本
```

---

## 注意事项

- `examples/` 下面的东西是测试数据，不要用它来描述你的 agent，会跟真实行为对不上。
- owner 字段如果在证据里没出现，就让它空着，不要推测。
- 自我介绍里如果用了过于空泛的词，校验会直接拒绝，比如那些到处都能套用的概括。
- 执行顺序不要打乱，必须先把像素图挂进 `share-card`，再跑最终校验和 HTML 渲染。
- 最终校验没通过之前，渲染出来的卡片可能有字段缺失或结构问题。

---

## 可能适用的情形

- 你有一个跑了一段时间的 agent，想给它做一张正式的身份卡。
- 你希望卡片内容都能在记录里找到对应依据。
- 你需要固定格式的结构化输出，方便后续程序处理。
- 你需要给这个 agent 配一张特定的像素头像，并且和其他展示物一起发布。

---

## 当前演示数据来源

仓库里的展示文件，是用这套流程处理本项目的 agent 日志生成的，不是 `examples/` 里的测试数据。原始输出放在 `output/`，后来复制到了 `docs/showcase/` 方便直接查看。
