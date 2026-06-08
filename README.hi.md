# MarkItDown कन्वर्टर — Claude Code स्किल

[![AgentSkill](https://img.shields.io/badge/AgentSkill-compatible-blue)](https://agentskills.io)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-red.svg)](LICENSE)
[![Non-Commercial](https://img.shields.io/badge/व्यावसायिक_उपयोग_निषिद्ध-red)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Lucifer5397/markitdown-skill)](https://github.com/Lucifer5397/markitdown-skill)

> **बहुभाषी:** [English](README.md) | [简体中文](README.zh-CN.md) | [Español](README.es.md) | [हिन्दी](README.hi.md) | [العربية](README.ar.md)

Claude Code, OpenClaw, Codex, Cursor और VS Code Copilot के लिए एक यूनिवर्सल एजेंट स्किल। Microsoft [MarkItDown](https://github.com/microsoft/markitdown) (131k+ स्टार्स) द्वारा संचालित। किसी भी फाइल को एक कमांड से Markdown में बदलें।

## समर्थित प्रारूप

| श्रेणी | प्रारूप |
|--------|---------|
| दस्तावेज़ | PDF, Word (.docx), PowerPoint (.pptx) |
| स्प्रेडशीट | Excel (.xlsx, .xls) |
| वेब | HTML, YouTube URL |
| डेटा | CSV, JSON, XML |
| इमेज | JPG, PNG, GIF, WebP, BMP, TIFF (OCR) |
| ऑडियो | MP3, WAV, FLAC, OGG, M4A (ट्रांसक्रिप्शन) |
| आर्काइव | ZIP (सभी सामग्री को कन्वर्ट करता है) |
| ई-बुक | EPub |
| ईमेल | .eml |

## इंस्टॉलेशन

### 1. स्किल इंस्टॉल करें

```bash
git clone https://github.com/Lucifer5397/markitdown-skill.git ~/.claude/skills/markitdown-converter/
```

### 2. Python पैकेज इंस्टॉल करें

```bash
pip install "markitdown[all]"
```

### 3. वैकल्पिक: सिस्टम निर्भरताएँ

```bash
# OCR समर्थन (इमेज से टेक्स्ट)
# Windows: winget install tesseract-ocr
# macOS:   brew install tesseract
# Linux:   sudo apt-get install tesseract-ocr

# ऑडियो ट्रांसक्रिप्शन
# Windows: winget install ffmpeg
# macOS:   brew install ffmpeg
# Linux:   sudo apt-get install ffmpeg
```

## उपयोग

इंस्टॉल होने के बाद, Claude Code में बस कहें:

```
"इस PDF को Markdown में बदलो"
"इस Word डॉक्यूमेंट से टेक्स्ट निकालो"
"इस फोल्डर की सभी फाइलों को md में कन्वर्ट करो"
"इस इमेज से टेक्स्ट निकालो"
```

एजेंट अपने आप `markitdown-converter` को ट्रिगर करेगा।

## स्किल संरचना

```
markitdown-skill/
├── SKILL.md                        # मुख्य स्किल फाइल (AgentSkill स्पेसिफिकेशन)
├── README.md                       # यह फाइल
├── LICENSE                         # MIT लाइसेंस
├── references/
│   ├── installation.md             # पूर्ण इंस्टॉलेशन गाइड
│   ├── formats.md                  # प्रत्येक प्रारूप का विवरण
│   ├── advanced.md                 # Azure, प्लगइन्स, RAG पाइपलाइन
│   └── troubleshooting.md          # सामान्य समस्याएं और समाधान
├── examples/
│   ├── basic_conversion.py         # बुनियादी रूपांतरण उदाहरण
│   ├── batch_convert.py            # समानांतर बैच कन्वर्टर
│   └── pipeline_example.py         # पूर्ण RAG पाइपलाइन
└── scripts/
    └── batch_convert.py            # स्टैंडअलोन बैच टूल
```

## संगतता

| AI एजेंट | समर्थन |
|----------|:------:|
| Claude Code | हाँ |
| OpenClaw | हाँ |
| Codex (OpenAI) | हाँ |
| Gemini CLI | हाँ |
| Cursor | हाँ |
| VS Code Copilot | हाँ |

## लाइसेंस

CC BY-NC 4.0 — व्यक्तिगत, शैक्षिक और अनुसंधान उपयोग के लिए निःशुल्क। **व्यावसायिक उपयोग निषिद्ध।**
