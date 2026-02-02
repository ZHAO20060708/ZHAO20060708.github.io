# 网页其他Bug检查报告 / Additional Website Bugs Report

## 报告日期 / Report Date: 2026-02-02

本报告记录了除已发现的3个本地化配置bug外的其他网页问题。
This report documents additional website bugs beyond the 3 localization configuration bugs already identified.

---

## Bug #4: 自定义HTML模板 - 错误的资源加载方式 / Custom HTML Template - Incorrect Resource Loading

**文件 / File**: `layouts/partials/head/custom.html`  
**严重性 / Severity**: 🔴 高 / High

### 问题 1: MathJax JavaScript 文件使用错误的标签 / MathJax JavaScript File Using Wrong Tag
**位置 / Location**: Line 5

```html
<!-- ❌ 错误 / WRONG -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
```

**问题描述 / Issue**:
- MathJax.js 是 JavaScript 文件，不是 CSS 样式表
- 使用 `<link rel="stylesheet">` 标签会导致加载失败
- 浏览器会尝试将其解析为CSS，导致数学公式渲染功能无法工作

**正确写法 / Correct**:
```html
<!-- ✅ 正确 / CORRECT -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML"></script>
```

**影响 / Impact**:
- 数学公式可能无法正确渲染
- 控制台会显示资源加载错误

---

### 问题 2: 字体文件使用错误的加载方式 / Font File Using Wrong Loading Method
**位置 / Location**: Line 6

```html
<!-- ❌ 错误 / WRONG -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/fonts/HTML-CSS/STIX-Web/font/STIXTwoMath-Regular.woff2">
```

**问题描述 / Issue**:
- WOFF2 是字体文件格式，不是CSS样式表
- 应该使用 CSS `@font-face` 规则来加载
- 直接使用 `<link rel="stylesheet">` 无法正确加载字体

**正确写法 / Correct**:
```html
<!-- ✅ 正确 / CORRECT -->
<style>
  @font-face {
    font-family: 'STIX Two Math';
    src: url('https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/fonts/HTML-CSS/STIX-Web/font/STIXTwoMath-Regular.woff2') format('woff2');
    font-weight: normal;
    font-style: normal;
  }
</style>
```

**影响 / Impact**:
- 数学字体无法正确加载
- 数学公式显示可能回退到系统默认字体

---

## Bug #5: 语言配置文件 - 属性名拼写错误 / Language Config - Property Name Typo

**文件 / File**: `config/_default/_languages.toml`  
**严重性 / Severity**: 🟡 中 / Medium

**位置 / Location**: Line 4

```toml
# ❌ 错误 / WRONG
languagedirection = "ltr"

# ✅ 正确 / CORRECT  
languageDirection = "ltr"
```

**问题描述 / Issue**:
- Hugo 期望使用驼峰命名法 `languageDirection`
- 当前使用全小写 `languagedirection` 可能会被忽略
- 这会导致语言方向设置失效（虽然对LTR语言影响较小）

**影响 / Impact**:
- 语言方向设置可能不生效
- 对于需要RTL（从右到左）的语言可能会有显示问题

---

## Bug #6: 评论系统配置 - 硬编码语言设置 / Comment System - Hardcoded Language

**文件 / File**: `config/_default/params.toml`  
**严重性 / Severity**: 🟡 中 / Medium

**位置 / Location**: Line 137

```toml
[comments.giscus]
# ... 其他配置 ...
lang="zh-CN"  # ⚠️ 硬编码为中文
```

**问题描述 / Issue**:
- Giscus 评论系统语言被硬编码为 "zh-CN"（简体中文）
- 当网站启用多语言支持后，评论界面仍然只显示中文
- 即使用户选择英文版本，评论界面也是中文的

**影响 / Impact**:
- 多语言支持不完整
- 英文页面显示中文评论界面，用户体验差

**建议修复 / Suggested Fix**:
使用动态语言变量或根据页面语言设置不同的值

---

## Bug #7: GitHub Actions 工作流 - Hugo版本配置不一致 / Workflow - Hugo Version Inconsistency

**文件 / File**: `.github/workflows/deploy.yml`  
**严重性 / Severity**: 🟢 低 / Low

**位置 / Location**: Lines 24 & 57

```yaml
# Line 24: 环境变量中定义了 Hugo 版本
env:
  HUGO_VERSION: 0.154.2

# Line 57: 但实际使用的是 'latest'
- name: Setup Hugo
  uses: peaceiris/actions-hugo@v3
  with:
    hugo-version: 'latest'  # ⚠️ 未使用环境变量
```

**问题描述 / Issue**:
- 定义了 `HUGO_VERSION` 环境变量但未使用
- 实际使用 `latest` 可能导致构建不可预测
- 版本不一致可能导致构建在不同时间产生不同结果

**建议修复 / Suggested Fix**:
```yaml
- name: Setup Hugo
  uses: peaceiris/actions-hugo@v3
  with:
    hugo-version: ${{ env.HUGO_VERSION }}
    extended: true
```

**影响 / Impact**:
- 构建可重现性差
- 可能因Hugo新版本引入破坏性更改导致构建失败

---

## Bug #8: 主菜单配置 - 完全被注释 / Main Menu - Completely Commented Out

**文件 / File**: `config/_default/menu.toml`  
**严重性 / Severity**: 🟡 中 / Medium

**位置 / Location**: Lines 2-8

```toml
# Configure main menu and social menu
#[[main]]
#identifier = "home"
#name = "Home"
#url = "/"
#[main.params]
#icon = "home"
#newtab = true
```

**问题描述 / Issue**:
- 主菜单完全被注释掉
- 网站没有主导航菜单
- 用户只能通过社交链接或其他方式导航

**影响 / Impact**:
- 网站导航功能不完整
- 用户体验差，无法快速访问主要页面
- 可能是有意为之，但通常网站需要主菜单

---

## Bug #9: 资源配置 - 临时缓存路径被提交 / Assets - Temporary Cache Path Committed

**文件 / File**: `assets/jsconfig.json`  
**严重性 / Severity**: 🟡 中 / Medium

**位置 / Location**: Lines 5-7

```json
{
 "compilerOptions": {
  "baseUrl": ".",
  "paths": {
   "*": [
    "../../../../../../tmp/hugo_cache_runner/modules/filecache/modules/pkg/mod/github.com/!cai!jimmy/hugo-theme-stack/v4@v4.0.0-beta.5/assets/*"
   ]
  }
 }
}
```

**问题描述 / Issue**:
- 路径指向 `/tmp/hugo_cache_runner/...` 这是CI构建时的临时缓存目录
- 在本地开发环境中此路径不存在，会导致路径解析失败
- 这个文件通常是 Hugo 自动生成的，不应该被提交到版本控制

**影响 / Impact**:
- 本地开发时可能出现路径解析问题
- IDE 智能提示可能无法工作
- 其他开发者无法正常使用

**建议修复 / Suggested Fix**:
将 `assets/jsconfig.json` 添加到 `.gitignore` 文件中：
```
# .gitignore
assets/jsconfig.json
```

---

## Bug #10: 自定义HTML - 使用区域特定CDN / Custom HTML - Region-Specific CDN

**文件 / File**: `layouts/partials/head/custom.html`  
**严重性 / Severity**: 🟡 中 / Medium

**位置 / Location**: Lines 31-33

```javascript
const customFonts = [
  "https://fonts.googleapis.cn/css2?family=Source+Serif+4:wght@400;700&display=swap",
  "https://fonts.googleapis.cn/css2?family=Noto+Serif+SC:wght@400;700&display=swap",
  "https://fonts.googleapis.cn/css2?family=Source+Code+Pro:wght@400;700&display=swap"
];
```

**问题描述 / Issue**:
- 使用 `fonts.googleapis.cn`（中国专用域名）
- 在中国大陆以外的地区可能无法访问或速度慢
- 应使用标准的 `fonts.googleapis.com` 以获得全球可访问性

**影响 / Impact**:
- 国际访客可能无法加载字体
- 字体加载失败会影响页面排版和可读性

**建议修复 / Suggested Fix**:
```javascript
const customFonts = [
  "https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@400;700&display=swap",
  "https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;700&display=swap",
  "https://fonts.googleapis.com/css2?family=Source+Code+Pro:wght@400;700&display=swap"
];
```

或者使用CDN备用方案：
```javascript
const customFonts = [
  {
    primary: "https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@400;700&display=swap",
    fallback: "https://fonts.googleapis.cn/css2?family=Source+Serif+4:wght@400;700&display=swap"
  }
];
```

---

## 总结 / Summary

### Bug 统计 / Bug Statistics

| 严重性 / Severity | 数量 / Count | Bug编号 / Bug IDs |
|------------------|-------------|------------------|
| 🔴 高 / High | 1 | #4 |
| 🟡 中 / Medium | 5 | #5, #6, #8, #9, #10 |
| 🟢 低 / Low | 1 | #7 |
| **总计 / Total** | **7** | **#4 - #10** |

### 按类型分类 / By Category

1. **HTML/模板问题 / HTML/Template Issues** (2): Bug #4, #10
2. **配置错误 / Configuration Errors** (3): Bug #5, #6, #8
3. **构建/部署问题 / Build/Deploy Issues** (2): Bug #7, #9

### 优先修复建议 / Priority Fix Recommendations

**高优先级 / High Priority**:
- Bug #4: 修复MathJax和字体加载（影响核心功能）

**中优先级 / Medium Priority**:
- Bug #6: 评论系统语言配置（影响多语言体验）
- Bug #9: 移除临时配置文件（影响本地开发）
- Bug #10: 修复CDN域名（影响国际访问）

**低优先级 / Low Priority**:
- Bug #5: 修复属性名拼写
- Bug #7: 统一Hugo版本配置
- Bug #8: 评估是否需要主菜单（可能是有意设计）

---

## 相关文档 / Related Documentation

- 之前发现的3个本地化Bug请参考: `LOCALIZATION_REPORT.md`
- 快速参考（中文）: `SUMMARY_CN.md`

---

**报告生成时间 / Report Generated**: 2026-02-02  
**检查者 / Checked by**: GitHub Copilot  
**仓库 / Repository**: ZHAO20060708/ZHAO20060708.github.io
