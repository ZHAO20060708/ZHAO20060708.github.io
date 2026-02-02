# Auto-Translate Configuration Guide
# 自动翻译配置指南

This document explains how to configure the auto-translate feature for this Hugo Stack theme site.
此文档说明如何为这个 Hugo Stack 主题网站配置自动翻译功能。

## Configuration / 配置

Add the following to your `config/_default/params.toml`:
在 `config/_default/params.toml` 中添加以下配置：

```toml
[autoTranslate]
enable = false  # Set to true to enable auto-translate / 设置为 true 以启用自动翻译
service = "client.edge"  # Options: "client.edge" or "translate.service"
languages = []  # Empty array means all languages are available / 空数组表示所有语言都可用
ignoreID = []  # IDs to ignore during translation / 翻译时忽略的 ID
ignoreClass = []  # Classes to ignore during translation / 翻译时忽略的类名
ignoreTag = []  # Tags to ignore during translation / 翻译时忽略的标签
detectLocalLanguage = false  # Auto-detect user's language / 自动检测用户语言
cdn = "https://cdn.jsdelivr.net/npm/i18n-jsautotranslate@latest"  # CDN for translate.js
enterprise = false  # Enable enterprise translation channel (requires subscription)
```

## Features / 功能特性

### 1. Automatic Page Translation / 自动页面翻译
- Translates entire pages to user's selected language
- 将整个页面翻译成用户选择的语言

### 2. Floating Language Selector / 浮动语言选择器
- Fixed position selector in bottom-right corner
- 右下角固定位置的选择器
- Supports all 16 configured languages
- 支持所有 16 种配置的语言

### 3. URL Parameter Support / URL 参数支持
- Use `?lang=english` to set translation language
- 使用 `?lang=english` 设置翻译语言
- Example: `https://your-site.com?lang=french`
- 示例：`https://your-site.com?lang=french`

## Supported Languages / 支持的语言

The auto-translate feature supports the following language codes:
自动翻译功能支持以下语言代码：

- `chinese_simplified` - 简体中文
- `english` - English
- `chinese_traditional` - 繁體中文
- `japanese` - 日本語
- `korean` - 한국어
- `french` - Français
- `german` - Deutsch
- `spanish` - Español
- `italian` - Italiano
- `portuguese` - Português
- `dutch` - Nederlands
- `thai` - ไทย
- `greek` - Ελληνικά
- `ukrainian` - Українська
- `arabic` - العربية
- `indonesian` - Bahasa Indonesia

## Translation Services / 翻译服务

### Free Service (Default) / 免费服务（默认）
- Service: `client.edge`
- Daily limit: 2 million characters
- 每日限额：200 万字符
- No API key required
- 无需 API 密钥

### Enterprise Service / 企业服务
- Service: `translate.service`
- Higher speed and reliability
- 更高的速度和可靠性
- Requires subscription
- 需要订阅
- Set `enterprise = true` in config
- 在配置中设置 `enterprise = true`

## How to Enable / 如何启用

1. **Edit params.toml** / **编辑 params.toml**
   ```toml
   [autoTranslate]
   enable = true
   ```

2. **Rebuild your site** / **重新构建网站**
   ```bash
   hugo
   ```

3. **Test the translation** / **测试翻译**
   - Visit your site
   - 访问你的网站
   - Look for the 🌐 selector in the bottom-right
   - 在右下角查找 🌐 选择器
   - Select a language to translate
   - 选择一种语言进行翻译

## Ignoring Elements / 忽略元素

To prevent certain elements from being translated:
要防止某些元素被翻译：

```toml
[autoTranslate]
enable = true
ignoreID = ["comments", "giscus"]  # Ignore by ID
ignoreClass = ["no-translate", "keep-original"]  # Ignore by class
ignoreTag = ["code", "pre"]  # Ignore by tag (already handled by default)
```

## Technical Notes / 技术说明

- The translation is performed client-side using translate.js
- 翻译在客户端使用 translate.js 执行
- Translation state persists across page navigations
- 翻译状态在页面导航中保持
- SEO-friendly: original content remains in HTML
- SEO 友好：原始内容保留在 HTML 中
- Works with all Hugo Stack theme features
- 与所有 Hugo Stack 主题功能兼容

## Troubleshooting / 故障排除

### Translation not working / 翻译不起作用
1. Check console for errors (F12 → Console)
2. Verify `enable = true` in params.toml
3. Clear browser cache
4. Check if translate.js CDN is accessible

### Floating selector not visible / 浮动选择器不可见
1. Check z-index conflicts with other elements
2. Verify CSS is loading correctly
3. Try different browser

## Credits / 致谢

- Translation powered by [translate.js](https://github.com/xnx3/translate)
- 翻译由 [translate.js](https://github.com/xnx3/translate) 提供支持
- Inspired by [cmpt-translate](https://github.com/hugo-fixit/cmpt-translate)
- 灵感来自 [cmpt-translate](https://github.com/hugo-fixit/cmpt-translate)
