# MarkItDown Converter — Claude Code Skill

[![AgentSkill](https://img.shields.io/badge/AgentSkill-compatible-blue)](https://agentskills.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Lucifer5397/markitdown-skill)](https://github.com/Lucifer5397/markitdown-skill)

> **Multi-language:** [English](README.md) | [简体中文](README.zh-CN.md) | [Español](README.es.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md)

A universal Agent Skill for Claude Code, OpenClaw, Codex, Cursor, and VS Code Copilot. Powered by Microsoft [MarkItDown](https://github.com/microsoft/markitdown) (131k+ Stars). One command to convert any file to Markdown.

## Supported Formats

| Category | Formats |
|----------|---------|
| Documents | PDF, Word (.docx), PowerPoint (.pptx) |
| Spreadsheets | Excel (.xlsx, .xls) |
| Web | HTML, YouTube URLs |
| Data | CSV, JSON, XML |
| Images | JPG, PNG, GIF, WebP, BMP, TIFF (OCR) |
| Audio | MP3, WAV, FLAC, OGG, M4A (transcription) |
| Archives | ZIP (iterates all contents) |
| E-books | EPub |
| Email | .eml |

## Installation

### 1. Install the Skill

```bash
git clone https://github.com/Lucifer5397/markitdown-skill.git ~/.claude/skills/markitdown-converter/
```

### 2. Install the Python Package

```bash
pip install "markitdown[all]"
```

### 3. Optional: System Dependencies

```bash
# OCR support (image to text)
# Windows: winget install tesseract-ocr
# macOS:   brew install tesseract
# Linux:   sudo apt-get install tesseract-ocr

# Audio transcription
# Windows: winget install ffmpeg
# macOS:   brew install ffmpeg
# Linux:   sudo apt-get install ffmpeg
```

## Usage

Once installed, simply say in Claude Code:

```
"Convert this PDF to Markdown"
"Extract text from this Word document"
"Convert all files in this folder to md"
"Extract text from this image"
```

The agent will auto-trigger `markitdown-converter` to handle the task.

## Skill Structure

```
markitdown-skill/
├── SKILL.md                        # Main skill file (AgentSkill spec)
├── README.md                       # This file
├── LICENSE                         # MIT License
├── references/
│   ├── installation.md             # Full installation guide
│   ├── formats.md                  # Format-by-format breakdown
│   ├── advanced.md                 # Azure, plugins, RAG pipelines
│   └── troubleshooting.md          # Common issues and fixes
├── examples/
│   ├── basic_conversion.py         # Basic conversion examples
│   ├── batch_convert.py            # Parallel batch converter
│   └── pipeline_example.py         # Full RAG pipeline
└── scripts/
    └── batch_convert.py            # Standalone batch tool
```

## Compatibility

| AI Agent | Support |
|----------|:------:|
| Claude Code | Yes |
| OpenClaw | Yes |
| Codex (OpenAI) | Yes |
| Gemini CLI | Yes |
| Cursor | Yes |
| VS Code Copilot | Yes |

## License

MIT — open source, do whatever you want.
