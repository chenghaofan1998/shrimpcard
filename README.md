# ShrimpCard

一个用于生成“龙虾/小龙虾角色卡片”的小型项目。包含：
- 单文件 HTML 卡片模板（遵循 `design.md` 设计规范）
- JSON 数据结构与示例
- OpenClaw 技能（用于输出准确 JSON/图片信息）

## 目录结构
- `index.html`：单文件卡片模板（含内联 CSS 与注释）
- `design.md`：设计规范
- `card-schema.json`：卡片 JSON Schema
- `sample-card.json`：示例数据
- `SOLUTION.md`：整体方案说明
- `skills/openclaw-shrimpcard/`：OpenClaw 技能（含校验脚本与参考）
- `原型图.jpg` / `线稿图.svg`：视觉参考

## 使用方式

### 1) 直接打开卡片模板

打开 `index.html` 即可预览。

### 2) 通过注入数据渲染

`index.html` 支持 `window.__CARD_DATA__` 注入：

```html
<script>
  window.__CARD_DATA__ = {
    card_id: "ID:#0x81e2",
    name: "麻辣小龙虾1号",
    bio: "我是一只性格超级热烈的小龙虾，\n擅长帮主人完成小红书运营工作",
    skills: ["任务操作", "内容创作", "回复机器人"],
    footer: ["DEPLOYED BY @HAO_FAN", "WeChat: haofan0703"],
    image: null,
    qr: null
  };
</script>
```

### 3) OpenClaw 技能

技能路径：`skills/openclaw-shrimpcard/`

- 产出 ShrimpCard JSON（符合 `card-schema.json`）
- 支持生成或输出图像描述
- 支持校验脚本：

```bash
python3 skills/openclaw-shrimpcard/scripts/validate_card.py sample-card.json
```

## 设计规范

请以 `design.md` 为准：
- 90s 复古波普 + 现代瑞士网格
- 2D 平面、强对比、粗黑描边
- 固定布局（顶部插画 / 身份 / 简介 / 标签 / 底部信息 + QR）

## License

未声明。
