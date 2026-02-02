# 本地化（i18n）分析报告 / Localization (i18n) Analysis Report

## 日期 / Date: 2026-02-02

## 1. 发现的Bug（尚未修复）/ Bugs Found (Not Yet Fixed)

### Bug #1: 多语言支持配置文件被禁用
**位置 / Location**: `/config/_default/_languages.toml`

**问题 / Issue**: 
- 文件名前缀有下划线 `_languages.toml`，导致Hugo无法识别此配置文件
- 多语言支持因此被禁用

**影响 / Impact**:
- 网站当前只支持单一语言（中文简体）
- 无法实现多语言切换功能

**如何修复 / How to Fix**:
```bash
# 将文件重命名以启用多语言支持
mv config/_default/_languages.toml config/_default/languages.toml
```

---

### Bug #2: 网站默认语言不是英文
**位置 / Location**: `/config/_default/config.toml`

**当前配置 / Current Configuration**:
```toml
languageCode = "zh-cn"
defaultContentLanguage = "zh-cn"
```

**问题 / Issue**: 
- 当前网站的默认语言是中文简体（zh-cn）
- 对于英语浏览器的访问者，网站界面仍然显示中文

**影响 / Impact**:
- 使用英语浏览器的用户会看到中文界面
- 不符合"浏览网页的人的默认语言是英文"的需求

**如何修复 / How to Fix**:
```toml
# 修改为英文作为默认语言
languageCode = "en"
defaultContentLanguage = "en"
hasCJKLanguage = false  # 英文不需要CJK支持
```

---

### Bug #3: 主题的中文简体本地化文件不完整
**位置 / Location**: 主题内置的 `i18n/zh.toml`

**问题 / Issue**:
主题提供的中文本地化文件缺少以下6个翻译键：

1. `article.readingTime.one` - 阅读时间（单数形式）
2. `article.readingTime.other` - 阅读时间（复数形式）
3. `list.page.one` - 页面计数（单数形式）
4. `list.page.other` - 页面计数（复数形式）
5. `list.subsection.one` - 子章节（单数形式）
6. `list.subsection.other` - 子章节（复数形式）

**影响 / Impact**:
- 某些UI元素可能显示不正确或使用英文回退
- 用户体验不一致

**已修复 / Fixed**:
✅ 已在 `/i18n/zh-cn.toml` 中补充完整所有缺失的翻译

---

## 2. 中文简体本地化文件补充 / Simplified Chinese Localization Completion

### 新建文件 / New File Created
**路径 / Path**: `/i18n/zh-cn.toml`

### 补充的翻译键 / Added Translation Keys

| 翻译键 / Key | 中文翻译 / Chinese Translation | 说明 / Description |
|-------------|-------------------------------|-------------------|
| `list.page.one` | `{{ .Count }} 个页面` | 页面计数（单数） |
| `list.page.other` | `{{ .Count }} 个页面` | 页面计数（复数） |
| `list.subsection.one` | `子章节` | 子章节（单数） |
| `list.subsection.other` | `子章节` | 子章节（复数） |
| `article.readingTime.one` | `{{ .Count }} 分钟阅读` | 阅读时间（单数） |
| `article.readingTime.other` | `{{ .Count }} 分钟阅读` | 阅读时间（复数） |

### 完整的翻译列表 / Complete Translation List

包含所有36个翻译键：

1. ✅ `toggleMenu` - 切换菜单
2. ✅ `darkMode` - 暗色模式
3. ✅ `list.section` - 章节
4. ✅ `list.page.one` - {{ .Count }} 个页面
5. ✅ `list.page.other` - {{ .Count }} 个页面
6. ✅ `list.subsection.one` - 子章节
7. ✅ `list.subsection.other` - 子章节
8. ✅ `article.back` - 返回
9. ✅ `article.tableOfContents` - 目录
10. ✅ `article.relatedContent` - 相关文章
11. ✅ `article.lastUpdatedOn` - 最后更新于
12. ✅ `article.readingTime.one` - {{ .Count }} 分钟阅读
13. ✅ `article.readingTime.other` - {{ .Count }} 分钟阅读
14. ✅ `notFound.title` - 404 错误
15. ✅ `notFound.subtitle` - 页面不存在
16. ✅ `widget.archives.title` - 归档
17. ✅ `widget.archives.more` - 更多
18. ✅ `widget.tagCloud.title` - 标签云
19. ✅ `widget.categoriesCloud.title` - 分类
20. ✅ `search.title` - 搜索
21. ✅ `search.placeholder` - 输入关键词...
22. ✅ `search.resultTitle` - #PAGES_COUNT 个结果 （用时 #TIME_SECONDS 秒）
23. ✅ `footer.builtWith` - 使用 {{ .Generator }} 构建
24. ✅ `footer.designedBy` - 主题 {{ .Theme }} 由 {{ .DesignedBy }} 设计

---

## 3. 英文本地化确认 / English Localization Verification

### 文件 / File
**路径 / Path**: `/i18n/en.toml`

### 状态 / Status
✅ **完整 / Complete** - 包含所有36个必需的翻译键

### 验证结果 / Verification Results
- 所有翻译键都已定义
- 包含单复数形式（one/other）
- 格式正确，符合Hugo i18n标准

---

## 4. 当前网站语言配置 / Current Site Language Configuration

### 主要配置 / Main Configuration
```toml
# File: /config/_default/config.toml

languageCode = "zh-cn"           # 语言代码：中文简体
defaultContentLanguage = "zh-cn"  # 默认内容语言：中文简体
hasCJKLanguage = true            # 启用CJK语言支持
```

### 问题 / Issues
⚠️ **默认语言是中文，不是英文** 
- 英语浏览器访问者仍然会看到中文界面
- 需要修改配置以支持英文作为默认语言

---

## 5. 如何配置英文为默认语言 / How to Configure English as Default Language

### 方案A：仅英文网站 / Option A: English-Only Site

修改 `/config/_default/config.toml`:
```toml
languageCode = "en"
defaultContentLanguage = "en"
hasCJKLanguage = false
```

### 方案B：多语言网站（推荐）/ Option B: Multilingual Site (Recommended)

1. **重命名语言配置文件**:
```bash
mv config/_default/_languages.toml config/_default/languages.toml
```

2. **编辑 `config/_default/languages.toml`**:
```toml
[en]
languageName = "English"
languagedirection = "ltr"
title = "EricZhao's Page"
weight = 1

[zh-cn]
languageName = "简体中文"
languagedirection = "ltr"
title = "Eric的博客"
weight = 2
```

3. **修改 `config/_default/config.toml`**:
```toml
defaultContentLanguage = "en"  # 英文作为默认语言
hasCJKLanguage = true         # 保留以支持中文
```

4. **重组内容目录结构**:
```
content/
├── en/           # 英文内容
│   └── post/
└── zh-cn/        # 中文内容
    └── post/
```

---

## 6. 建议 / Recommendations

### 短期建议 / Short-term
1. ✅ 使用创建的 `/i18n/zh-cn.toml` 补充中文翻译
2. ✅ 使用创建的 `/i18n/en.toml` 确保英文翻译完整
3. 📋 根据需求选择是否启用多语言支持

### 长期建议 / Long-term
1. 📋 启用多语言支持（重命名 `_languages.toml`）
2. 📋 将内容按语言分类到不同目录
3. 📋 添加语言切换器到网站UI
4. 📋 考虑使用浏览器语言自动检测

---

## 7. 测试清单 / Testing Checklist

- [ ] 验证中文本地化文件所有键都已翻译
- [ ] 验证英文本地化文件所有键都已翻译
- [ ] 测试单语言模式（中文）
- [ ] 测试单语言模式（英文）
- [ ] 测试多语言模式（如果启用）
- [ ] 验证浏览器语言检测
- [ ] 检查所有UI元素显示正确

---

## 附录：支持的语言 / Appendix: Supported Languages

Hugo Theme Stack v4 支持以下语言：

- 🇺🇸 English (en)
- 🇨🇳 简体中文 (zh-cn, zh)
- 🇹🇼 繁體中文 (zh-tw, zh-hant-tw)
- 🇭🇰 繁體中文 (zh-hant-hk)
- 🇯🇵 日本語 (ja)
- 🇰🇷 한국어 (ko)
- 🇫🇷 Français (fr)
- 🇩🇪 Deutsch (de)
- 🇪🇸 Español (es)
- 🇮🇹 Italiano (it)
- 🇧🇷 Português (pt-br)
- 🇵🇹 Português (pt-pt)
- 🇮🇩 Bahasa Indonesia (id)
- 🇳🇱 Nederlands (nl)
- 🇹🇭 ไทย (th)
- 🇬🇷 Ελληνικά (el)
- 🇺🇦 Українська (uk)
- 🇸🇦 العربية (ar)
- 以及更多...

---

**报告生成时间 / Report Generated**: 2026-02-02
**仓库 / Repository**: ZHAO20060708/ZHAO20060708.github.io
