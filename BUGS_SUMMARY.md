# Bug检查摘要 / Bug Check Summary

## 新发现的Bug / Newly Discovered Bugs: 7个

### 🔴 高严重性 / High Severity (1)

**Bug #4**: 自定义HTML模板 - 错误的资源加载
- MathJax.js 使用 `<link>` 标签而非 `<script>` 标签
- 字体文件 .woff2 使用 `<link rel="stylesheet">` 而非 `@font-face`
- 文件: `layouts/partials/head/custom.html`

### 🟡 中等严重性 / Medium Severity (5)

**Bug #5**: 语言配置 - 属性名拼写错误
- `languagedirection` 应为 `languageDirection`
- 文件: `config/_default/_languages.toml`

**Bug #6**: 评论系统 - 语言硬编码
- Giscus 评论语言固定为 `zh-CN`，不支持多语言
- 文件: `config/_default/params.toml`

**Bug #8**: 主菜单完全被注释
- 网站无主导航菜单
- 文件: `config/_default/menu.toml`

**Bug #9**: 临时缓存路径被提交
- `jsconfig.json` 包含CI临时路径，本地开发无法使用
- 文件: `assets/jsconfig.json`

**Bug #10**: 使用区域特定CDN
- 使用 `fonts.googleapis.cn` 而非全球可用的 `.com` 域名
- 文件: `layouts/partials/head/custom.html`

### 🟢 低严重性 / Low Severity (1)

**Bug #7**: Hugo版本配置不一致
- 环境变量定义了版本但未使用
- 文件: `.github/workflows/deploy.yml`

---

## 之前发现的Bug / Previously Discovered Bugs: 3个

1. 多语言配置文件被禁用 (`_languages.toml`)
2. 默认语言是中文而非英文
3. 主题中文翻译不完整

详见: `LOCALIZATION_REPORT.md`

---

## 总Bug数 / Total Bugs: 10个

完整详情请查看: `ADDITIONAL_BUGS_REPORT.md`
