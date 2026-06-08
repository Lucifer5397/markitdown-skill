---
name: markitdown-converter
description: Convert ANY file to Markdown — PDF, Word (.docx), PowerPoint (.pptx), Excel (.xlsx/.xls), images (OCR), audio (transcription), HTML, CSV, JSON, XML, ZIP, YouTube URLs, EPub, and more. Use when the user asks to convert, extract, or transform a file/document into Markdown; when they mention "markitdown", "convert to md", "extract text from PDF/Word/Excel", "document to markdown", or need document content for AI processing.
license: MIT
metadata:
  author: open-source
  version: "1.0.0"
  homepage: "https://github.com/microsoft/markitdown"
  requires_python: ">=3.8"
  requires_package: "markitdown[all]"
compatibility: Requires Python 3.8+, pip. Optional: tesseract (OCR), ffmpeg (audio).
---

# MarkItDown — Universal Document to Markdown Converter

Converts virtually any file format to clean, structured Markdown using Microsoft's [MarkItDown](https://github.com/microsoft/markitdown) library. Perfect for RAG pipelines, AI context injection, documentation workflows, and making any document AI-readable.

**This skill wraps `markitdown[all]` — the complete package with all optional converters.**

## Quick Start

If markitdown is not yet installed:

```bash
pip install "markitdown[all]"
```

For OCR support on images, also install the system dependency:

```bash
# Windows
winget install tesseract-ocr

# macOS
brew install tesseract

# Linux
sudo apt-get install tesseract-ocr
```

For audio transcription support:

```bash
# Windows — ffmpeg
winget install ffmpeg

# macOS
brew install ffmpeg

# Linux
sudo apt-get install ffmpeg
```

## Supported Formats

| Category | Formats |
|----------|---------|
| **Documents** | PDF (.pdf), Word (.docx), PowerPoint (.pptx) |
| **Spreadsheets** | Excel (.xlsx, .xls) |
| **Web** | HTML (.html, .htm), YouTube URLs |
| **Data** | CSV, JSON, XML |
| **Images** | JPG, PNG, GIF, WebP, BMP, TIFF (with OCR) |
| **Audio** | MP3, WAV, FLAC, OGG, M4A, WMA (with transcription) |
| **Archives** | ZIP (iterates and converts all contents) |
| **E-books** | EPub (.epub) |
| **Text** | Plain text, Markdown, RST, LaTeX |
| **Email** | .eml |

## CLI Usage

### Basic conversion — file to Markdown file

```bash
markitdown input.pdf -o output.md
```

### Convert and print to stdout

```bash
markitdown document.docx
```

### Convert from stdin with type hint

```bash
cat document | markitdown -x .pdf -o output.md
```

### Convert with MIME type hint

```bash
markitdown input.bin -m application/pdf -o output.md
```

### Convert Excel (preserves table structure)

```bash
markitdown data.xlsx -o data.md
```

### Convert PowerPoint (preserves slide structure)

```bash
markitdown presentation.pptx -o slides.md
```

### Convert image with OCR

```bash
markitdown photo.jpg -o text.md
```

### Convert audio with speech-to-text

```bash
markitdown recording.mp3 -o transcript.md
```

### Convert ZIP archive (converts all contents)

```bash
markitdown bundle.zip -o extracted.md
```

### Convert YouTube video (gets transcript)

```bash
markitdown "https://www.youtube.com/watch?v=VIDEO_ID" -o transcript.md
```

### Batch convert all files matching a pattern

```bash
markitdown *.pdf -o output/
```

## Python API Usage

When you need more control or want to integrate into a pipeline, use the Python API:

### Basic conversion

```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("document.pdf")
print(result.text_content)
```

### With OCR enabled

```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("scan.jpg")  # OCR auto-detected for images
print(result.text_content)
```

### Convert from URL

```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("https://example.com/document.pdf")
print(result.text_content)
```

### Write to file

```python
from markitdown import MarkItDown
from pathlib import Path

md = MarkItDown()
result = md.convert("input.docx")
Path("output.md").write_text(result.text_content)
```

### Batch conversion script

```python
from pathlib import Path
from markitdown import MarkItDown

md = MarkItDown()
input_dir = Path("./documents")
output_dir = Path("./markdown_output")
output_dir.mkdir(exist_ok=True)

for file_path in input_dir.iterdir():
    if file_path.suffix.lower() in {
        ".pdf", ".docx", ".pptx", ".xlsx", ".xls",
        ".html", ".htm", ".csv", ".json", ".xml",
        ".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".tiff",
        ".mp3", ".wav", ".flac", ".ogg", ".m4a", ".wma",
        ".zip", ".epub", ".eml", ".txt", ".md",
    }:
        try:
            result = md.convert(str(file_path))
            out_path = output_dir / f"{file_path.stem}.md"
            out_path.write_text(result.text_content)
            print(f"OK: {file_path.name} -> {out_path.name}")
        except Exception as e:
            print(f"FAIL: {file_path.name} — {e}")
```

## Pre-built scripts

This skill includes ready-to-run scripts in `scripts/`.

### Batch converter

```bash
python scripts/batch_convert.py ./input_folder ./output_folder
```

## Common Patterns

### Pattern: Feed document into AI context

```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("report.docx")
markdown_content = result.text_content

# Now markdown_content can be used as context for AI
print(f"Document length: {len(markdown_content)} chars")
```

### Pattern: Convert and save alongside original

```python
from pathlib import Path
from markitdown import MarkItDown

md = MarkItDown()
source = Path("document.pdf")
result = md.convert(str(source))
source.with_suffix(".md").write_text(result.text_content)
```

### Pattern: Build RAG pipeline documents

```python
from pathlib import Path
from markitdown import MarkItDown

md = MarkItDown()
docs_dir = Path("./raw_documents")
rag_dir = Path("./rag_corpus")
rag_dir.mkdir(exist_ok=True)

for f in docs_dir.glob("*"):
    try:
        result = md.convert(str(f))
        (rag_dir / f"{f.stem}.md").write_text(result.text_content)
        print(f"Indexed: {f.name}")
    except Exception as e:
        print(f"Skipped: {f.name} ({e})")
```

## Edge Cases & Troubleshooting

### PDF returns empty or garbled text
The PDF may be scanned images without text layer. Use `-d` flag for Azure Document Intelligence (requires Azure account), or install Tesseract for local OCR:
```bash
# With Azure
markitdown scan.pdf -d -e "https://your-resource.cognitiveservices.azure.com/" -o output.md
```

### Large files timeout
For very large files (100MB+), process in chunks or increase system memory.

### Encrypted/protected files
Password-protected PDFs, DOCX, XLSX cannot be read. Remove protection first.

### YouTube requires network
YouTube conversion downloads the transcript via the YouTube API; network access required.

## Reference Docs

For detailed information on specific topics, see:
- [Installation Guide](references/installation.md) — Full install steps for all platforms
- [Supported Formats](references/formats.md) — Detailed format-by-format breakdown
- [Advanced Features](references/advanced.md) — Azure integration, plugins, custom converters
- [Troubleshooting](references/troubleshooting.md) — Common issues and fixes
