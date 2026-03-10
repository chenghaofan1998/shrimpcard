# ShrimpCard 方案

目标：通过可安装 skill + 网页端渲染平台，生成可分享的“龙虾卡片”。卡片视觉参考 `原型图.jpg` 与 `线稿图.svg`，同时给用户 OpenClaw（自定义）空间。

## 1. 整体架构

组件
- Skill（命令触发，采集/总结信息，输出 JSON）
- Card Schema（严格字段与版本）
- Web Renderer（网页端渲染 + 可供平台截图）
- Optional Image Gen（有生图能力则生成主图，否则输出图像描述或占位）

数据流
- 用户添加 skill
- 用户输入命令，如 `龙虾卡片 生成`
- Skill 收集 memory 或用户补充信息
- Skill 生成卡片结构化 JSON
- Web 平台读取 JSON 渲染 HTML 卡片
- 平台头less截图导出 PNG（或用户在浏览器下载）

## 2. Skill 行为规范

触发方式
- 文本命令示例：`龙虾卡片 生成`、`生成我的龙虾卡片`

信息采集
- memory 中的个人信息（主人昵称、联系方式、兴趣/工作）
- skill 自身能力与使用频率（最长做的事）
- 用户可补充字段（名字、口号、二维码、头像、配色、标签）

内容产出要求
- `lobster_image_desc` 必须是“龙虾形象”描述
- `name` 是龙虾名字
- `tagline` 为一句话表达
- `top_skills` 固定 3 个标签
- `owner` 包含主人称呼与可选联系方式
- `qr` 可为空（后续可替换）

失败或缺失的兜底
- memory 缺失：要求用户补充最低字段（name, tagline, top_skills, owner.name）
- 无生图能力：提供 `lobster_image_desc` + `image_placeholder`

## 3. JSON Schema（版本化）

- 参考 `card-schema.json`
- 版本号 `schema_version: 1.0`
- 允许扩展字段 `meta` 与 `theme`

## 4. 视觉与布局要点

参考 `原型图.jpg` 与 `线稿图.svg`
- 卡片圆角、粗描边
- 顶部大图区域
- 名称大标题 + ID 小字
- 描述段落
- 三个胶囊标签
- 左下主人信息
- 右下 QR / Logo 占位

开放用户自定义（OpenClaw）
- 颜色主题（背景、边框、标签）
- 标签文案与顺序
- 名称/口号/描述风格
- 主图描述或上传图

## 5. 渲染平台要求

- 读取 JSON 并渲染 HTML
- 统一字体与尺寸，避免不同环境排版漂移
- 头less 截图建议 2x 像素密度

## 6. 安全与隐私

- 主人信息字段允许为空
- 默认不展示敏感字段
- QR 可留空或用占位

## 7. 可运行 Demo

- 本仓库提供静态渲染页面：`index.html`
- 可加载 `sample-card.json` 预览

