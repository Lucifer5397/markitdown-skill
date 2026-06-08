# MarkItDown Converter — Claude Code Skill

[![AgentSkill](https://img.shields.io/badge/AgentSkill-compatible-blue)](https://agentskills.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

一个 Claude Code / OpenClaw / Codex / Cursor 通用的 Agent Skill，基于微软 [MarkItDown](https://github.com/microsoft/markitdown)（131k+ Stars），将任何文件格式一键转换为 Markdown。

## 支持格式

| 类别 | 格式 |
|------|------|
| 文档 | PDF, Word (.docx), PowerPoint (.pptx) |
| 表格 | Excel (.xlsx, .xls) |
| 网页 | HTML, YouTube 视频链接 |
| 数据 | CSV, JSON, XML |
| 图片 | JPG, PNG, GIF, WebP, BMP, TIFF（OCR 提取文字） |
| 音频 | MP3, WAV, FLAC, OGG, M4A（语音转文字） |
| 压缩包 | ZIP（遍历所有内容） |
| 电子书 | EPub |
| 邮件 | .eml |

## 安装

### 1. 安装 Skill

**方式一：直接复制**
```bash
git clone https://github.com/YOUR_USERNAME/markitdown-skill.git ~/.claude/skills/markitdown-converter/
```

**方式二：ClawHub**
```bash
clawhub install markitdown-converter
```

### 2. 安装底层依赖

```bash
pip install "markitdown[all]"
```

### 3. 可选：安装系统依赖

```bash
# OCR（图片转文字）
# Windows: winget install tesseract-ocr
# macOS:   brew install tesseract
# Linux:   sudo apt-get install tesseract-ocr

# 音频转文字
# Windows: winget install ffmpeg
# macOS:   brew install ffmpeg
# Linux:   sudo apt-get install ffmpeg
```

## 使用

安装后直接在 Claude Code 中说：

```
"把这个 PDF 转成 Markdown"
"把这份 Word 文档提取出来"
"把文件夹里所有文档批量转成 md"
"把这张图片里的文字提取出来"
```

Agent 会自动触发 `markitdown-converter` skill 来完成任务。

## Skill 结构

```
markitdown-skill/
├── SKILL.md                        # 主 Skill 文件（AgentSkill 规范）
├── README.md                       # 本文件
├── LICENSE                         # MIT License
├── references/
│   ├── installation.md             # 详细安装指南
│   ├── formats.md                  # 所有格式详细说明
│   ├── advanced.md                 # 高级功能（Azure、插件、RAG）
│   └── troubleshooting.md          # 常见问题排查
├── examples/
│   ├── basic_conversion.py         # 基础转换示例
│   ├── batch_convert.py            # 批量转换脚本
│   └── pipeline_example.py         # 完整 RAG pipeline
└── scripts/
    └── batch_convert.py            # 独立批量转换工具
```

## 兼容性

| AI Agent | 支持 |
|----------|------|
| Claude Code | Yes |
| OpenClaw | Yes |
| Codex (OpenAI) | Yes |
| Gemini CLI | Yes |
| Cursor | Yes |
| VS Code Copilot | Yes |

## License

MIT — 开源，随便用。
