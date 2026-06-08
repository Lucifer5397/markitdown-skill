# محول MarkItDown — سكيل Claude Code

[![AgentSkill](https://img.shields.io/badge/AgentSkill-compatible-blue)](https://agentskills.io)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-red.svg)](LICENSE)
[![Non-Commercial](https://img.shields.io/badge/الاستخدام_التجاري_ممنوع-red)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Lucifer5397/markitdown-skill)](https://github.com/Lucifer5397/markitdown-skill)

> **متعدد اللغات:** [English](README.md) | [简体中文](README.zh-CN.md) | [Español](README.es.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md)

سكيل وكيل عالمي لـ Claude Code و OpenClaw و Codex و Cursor و VS Code Copilot. مدعوم من Microsoft [MarkItDown](https://github.com/microsoft/markitdown) (131 ألف+ نجمة). أمر واحد لتحويل أي ملف إلى Markdown.

## الصيغ المدعومة

| الفئة | الصيغ |
|-------|-------|
| المستندات | PDF, Word (.docx), PowerPoint (.pptx) |
| جداول البيانات | Excel (.xlsx, .xls) |
| الويب | HTML, روابط YouTube |
| البيانات | CSV, JSON, XML |
| الصور | JPG, PNG, GIF, WebP, BMP, TIFF (OCR) |
| الصوت | MP3, WAV, FLAC, OGG, M4A (نسخ صوتي) |
| الأرشيف | ZIP (يحول جميع المحتويات) |
| الكتب الإلكترونية | EPub |
| البريد | .eml |

## التثبيت

### 1. تثبيت السكيل

```bash
git clone https://github.com/Lucifer5397/markitdown-skill.git ~/.claude/skills/markitdown-converter/
```

### 2. تثبيت حزمة Python

```bash
pip install "markitdown[all]"
```

### 3. اختياري: تبعيات النظام

```bash
# دعم OCR (صورة إلى نص)
# Windows: winget install tesseract-ocr
# macOS:   brew install tesseract
# Linux:   sudo apt-get install tesseract-ocr

# النسخ الصوتي
# Windows: winget install ffmpeg
# macOS:   brew install ffmpeg
# Linux:   sudo apt-get install ffmpeg
```

## الاستخدام

بعد التثبيت، قل ببساطة في Claude Code:

```
"حول هذا الـ PDF إلى Markdown"
"استخرج النص من مستند Word هذا"
"حول جميع الملفات في هذا المجلد إلى md"
"استخرج النص من هذه الصورة"
```

سيقوم الوكيل تلقائياً بتشغيل `markitdown-converter` لإنجاز المهمة.

## هيكل السكيل

```
markitdown-skill/
├── SKILL.md                        # ملف السكيل الرئيسي (مواصفة AgentSkill)
├── README.md                       # هذا الملف
├── LICENSE                         # رخصة MIT
├── references/
│   ├── installation.md             # دليل التثبيت الكامل
│   ├── formats.md                  # تفصيل كل صيغة
│   ├── advanced.md                 # Azure، الإضافات، خطوط RAG
│   └── troubleshooting.md          # المشاكل الشائعة والحلول
├── examples/
│   ├── basic_conversion.py         # أمثلة تحويل أساسية
│   ├── batch_convert.py            # محول دفعات متوازي
│   └── pipeline_example.py         # خط أنابيب RAG كامل
└── scripts/
    └── batch_convert.py            # أداة دفعات مستقلة
```

## التوافق

| الوكيل الذكي | الدعم |
|-------------|:-----:|
| Claude Code | نعم |
| OpenClaw | نعم |
| Codex (OpenAI) | نعم |
| Gemini CLI | نعم |
| Cursor | نعم |
| VS Code Copilot | نعم |

## الرخصة

CC BY-NC 4.0 — مجاني للاستخدام الشخصي والتعليمي والبحثي. **الاستخدام التجاري ممنوع.**
