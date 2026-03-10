你现在是一个资深的前端开发工程师，精通 CSS3 和现代 UI 布局（Flexbox/Grid）。请帮我编写一个单文件 HTML（包含内部的 <style>），实现一个“AI 角色卡片（AI Agent Character Card）”。

设计风格 (Design Style):
结合 90 年代复古波普艺术与现代瑞士网格布局。要求平面 2D 感、高对比度、所有主要元素带有较粗的纯黑边框。

全局配色变量 (CSS Variables):

--bg-cream: #FFFDD0;

--text-black: #111111;

--border-black: #000000;

--white: #FFFFFF;

具体布局要求（从上到下）：

整体卡片容器 (.agent-card):

最大宽度约 420px，居中显示。

背景色使用 --bg-cream。

内边距（Padding）设置 24px。

字体全局使用系统无衬线字体。

顶部插画框 (.card-header-img):

宽度 100%，高度约 240px。

背景色可以使用深青色 #008080 或放置一张占位图片。

必须有圆角 border-radius: 16px;。

必须有粗黑边框 border: 3px solid var(--border-black);。

底部留白 margin-bottom: 24px;。

身份信息区 (.card-identity):

主标题 (H1): 文字内容为 "麻辣小龙虾1号"，字号 32px，极粗（font-weight: 900），颜色纯黑，无下边距。

副标题/ID: 文字内容为 "ID:#0x81e2"，字体必须使用等宽字体（monospace），字号 18px，带有一定的上边距。

底部留白 margin-bottom: 32px;。

简介区 (.card-bio):

文本内容：“我是一只性格超级热烈的小龙虾，


擅长帮主人完成小红书运营工作”。

字体加粗（font-weight: 600），字号 20px，行高 1.6。

底部留白 margin-bottom: 40px;。

技能标签行 (.card-skills):

使用 Flexbox 布局，横向排列，gap: 12px;，可换行（flex-wrap）。

标签内容："任务操作", "内容创作", "回复机器人"。

标签样式（Pill-shaped）：圆角 border-radius: 999px;，黑色边框 border: 2px solid var(--border-black);，内边距 8px 16px，字号 16px，字体加粗。

底部留白 margin-bottom: 48px;。

底部区 (.card-footer):

使用 Flexbox 两端对齐 (justify-content: space-between; align-items: flex-end;)。

左侧文本：两行细小的文本 "DEPLOYED BY @HAO_FAN" 和 "WeChat: haofan0703"。使用等宽字体，字号 12px，行高较小。

右侧二维码占位：一个正方形容器，宽度 64px，高度 64px，背景纯白 --white，圆角 12px，黑色粗边框 border: 3px solid var(--border-black);。

请直接输出结构清晰、带有详细注释的 HTML 代码。保证响应式（在小屏幕上自动缩放）。