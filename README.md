# Zhao's Space

Zhao's Space 是使用 [Astro](https://astro.build/) 构建的个人网站，集中展示个人介绍、文章和 Web 工具。仓库同时包含网站源码与构建配置。

## 功能

- 使用 Markdown 和 MDX 管理文章内容。
- 提供响应式深色界面。
- 集成 Malody 转 osu!mania、osu! 谱面下载等交互工具。
- 支持生成静态站点并部署至 GitHub Pages。

## 开发环境

- Node.js 22.12 或更高版本
- npm

## 本地运行

```sh
npm install
npm run dev
```

默认开发服务器启动后，终端会显示本地访问地址。

## 构建与预览

```sh
npm run build
npm run preview
```

构建产物由 Astro 输出，部署设置以仓库中的工作流与 Astro 配置为准。

## 许可

除非仓库另有说明，网站内容与代码不自动授予额外使用权。引用或复用前请先确认相关文件的许可信息。
