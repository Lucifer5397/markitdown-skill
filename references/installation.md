# Installation Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Step 1: Install MarkItDown

```bash
pip install "markitdown[all]"
```

The `[all]` extra installs all optional converters: OCR, audio transcription, YouTube, etc.

If you only need basic document conversion (PDF, DOCX, PPTX, XLSX):

```bash
pip install markitdown
```

## Step 2: Install System Dependencies (Optional)

### OCR Support (for images)

OCR allows extracting text from images. Requires Tesseract.

**Windows:**
```bash
winget install tesseract-ocr
```
Or download from: https://github.com/UB-Mannheim/tesseract/wiki

**macOS:**
```bash
brew install tesseract
```

**Linux (Debian/Ubuntu):**
```bash
sudo apt-get install tesseract-ocr
```

**Linux (Fedora/RHEL):**
```bash
sudo dnf install tesseract
```

### Audio Transcription Support

Transcribes speech from audio files to text.

**Windows:**
```bash
winget install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Debian/Ubuntu):**
```bash
sudo apt-get install ffmpeg
```

**Linux (Fedora/RHEL):**
```bash
sudo dnf install ffmpeg
```

## Step 3: Verify Installation

```bash
markitdown --help
```

Or via Python:

```python
from markitdown import MarkItDown
md = MarkItDown()
print("MarkItDown installed successfully")
```

## Docker Alternative

If you prefer not to install Python dependencies locally:

```bash
# Build the image
docker build -t markitdown https://github.com/microsoft/markitdown.git

# Run conversion
docker run -v $(pwd):/data markitdown /data/input.pdf -o /data/output.md
```

## Platform-Specific Notes

### Windows
- Ensure Python is in your PATH
- Run terminal as Administrator for `winget` installs
- Tesseract: note the install path (usually `C:\Program Files\Tesseract-OCR\`)

### macOS
- Xcode Command Line Tools required: `xcode-select --install`
- Homebrew recommended for system deps

### Linux
- Use system package manager for tesseract and ffmpeg
- For headless servers: tesseract works without GUI, ffmpeg too
