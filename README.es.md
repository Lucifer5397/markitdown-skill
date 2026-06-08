# MarkItDown Converter — Skill para Claude Code

[![AgentSkill](https://img.shields.io/badge/AgentSkill-compatible-blue)](https://agentskills.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Lucifer5397/markitdown-skill)](https://github.com/Lucifer5397/markitdown-skill)

> **Multi-idioma:** [English](README.md) | [简体中文](README.zh-CN.md) | [Español](README.es.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md)

Un Agent Skill universal para Claude Code, OpenClaw, Codex, Cursor y VS Code Copilot. Basado en Microsoft [MarkItDown](https://github.com/microsoft/markitdown) (131k+ estrellas). Convierte cualquier archivo a Markdown con un solo comando.

## Formatos soportados

| Categoría | Formatos |
|-----------|----------|
| Documentos | PDF, Word (.docx), PowerPoint (.pptx) |
| Hojas de cálculo | Excel (.xlsx, .xls) |
| Web | HTML, URLs de YouTube |
| Datos | CSV, JSON, XML |
| Imágenes | JPG, PNG, GIF, WebP, BMP, TIFF (OCR) |
| Audio | MP3, WAV, FLAC, OGG, M4A (transcripción) |
| Archivos | ZIP (convierte todo el contenido) |
| E-books | EPub |
| Correo | .eml |

## Instalación

### 1. Instalar el Skill

```bash
git clone https://github.com/Lucifer5397/markitdown-skill.git ~/.claude/skills/markitdown-converter/
```

### 2. Instalar el paquete Python

```bash
pip install "markitdown[all]"
```

### 3. Opcional: dependencias del sistema

```bash
# OCR (imagen a texto)
# Windows: winget install tesseract-ocr
# macOS:   brew install tesseract
# Linux:   sudo apt-get install tesseract-ocr

# Transcripción de audio
# Windows: winget install ffmpeg
# macOS:   brew install ffmpeg
# Linux:   sudo apt-get install ffmpeg
```

## Uso

Una vez instalado, solo di en Claude Code:

```
"Convierte este PDF a Markdown"
"Extrae el texto de este documento Word"
"Convierte todos los archivos de esta carpeta a md"
"Extrae el texto de esta imagen"
```

El agente activará automáticamente `markitdown-converter`.

## Estructura del Skill

```
markitdown-skill/
├── SKILL.md                        # Archivo principal (especificación AgentSkill)
├── README.md                       # Este archivo
├── LICENSE                         # Licencia MIT
├── references/
│   ├── installation.md             # Guía completa de instalación
│   ├── formats.md                  # Desglose por formato
│   ├── advanced.md                 # Azure, plugins, pipelines RAG
│   └── troubleshooting.md          # Problemas comunes y soluciones
├── examples/
│   ├── basic_conversion.py         # Ejemplos básicos
│   ├── batch_convert.py            # Conversión por lotes en paralelo
│   └── pipeline_example.py         # Pipeline RAG completo
└── scripts/
    └── batch_convert.py            # Herramienta batch independiente
```

## Compatibilidad

| AI Agent | Soporte |
|----------|:------:|
| Claude Code | Sí |
| OpenClaw | Sí |
| Codex (OpenAI) | Sí |
| Gemini CLI | Sí |
| Cursor | Sí |
| VS Code Copilot | Sí |

## Licencia

MIT — código abierto, úsalo como quieras.
