# Supported Formats — Detailed Breakdown

## Document Formats

### PDF (.pdf)
- Extracts text layer content
- Scanned PDFs without text layer require OCR (Tesseract) or Azure Document Intelligence
- Preserves document structure where possible
- Multi-column layouts may produce non-linear text ordering

### Word (.docx)
- Full text extraction with paragraph structure
- Tables converted to Markdown tables
- Embedded images noted but not OCR'd by default
- Headings mapped to Markdown heading levels

### PowerPoint (.pptx)
- Each slide converted as a section
- Slide titles become Markdown headings
- Text content extracted from all shapes
- Speaker notes included when present
- Tables within slides preserved

### Excel (.xlsx, .xls)
- Each sheet converted to a Markdown table
- Sheet names become section headings
- Cell formatting preserved where possible
- Multi-sheet workbooks: each sheet gets its own section

## Web Formats

### HTML (.html, .htm)
- Strips scripts, styles, and navigation elements
- Preserves headings, paragraphs, lists, links, tables
- Converts relative links to absolute where possible
- Handles most modern HTML5 structures

### YouTube URLs
- Downloads the auto-generated transcript/captions
- Output includes video title and transcript text
- Requires network access
- Some videos may not have captions available

## Data Formats

### CSV (.csv)
- Converted to Markdown tables
- Handles quoted fields and multiline cells
- Auto-detects delimiters

### JSON (.json)
- Pretty-printed and wrapped in code blocks
- Nested structures preserved in indented format
- Large JSON files may produce long output

### XML (.xml)
- Converted to readable structure
- Element hierarchy preserved
- Attributes shown inline

## Media Formats

### Images (JPG, PNG, GIF, WebP, BMP, TIFF)
- Requires Tesseract OCR installed
- Extracts embedded text via OCR
- EXIF metadata extracted and included
- Best results with high-resolution, clear text images
- Handwritten text: accuracy varies

### Audio (MP3, WAV, FLAC, OGG, M4A, WMA)
- Requires ffmpeg installed
- Uses speech-to-text for transcription
- EXIF/metadata extracted
- Best results with clear speech, minimal background noise
- Music/lyrics: transcription may be inaccurate

## Archive Formats

### ZIP (.zip)
- Iterates all contained files
- Each file converted individually
- Output concatenated with file path markers
- Nested ZIPs handled recursively
- Non-convertible files noted but skipped

## E-book Formats

### EPub (.epub)
- Chapter structure preserved
- Images referenced but not extracted
- Metadata (author, title) included in header
- Inline formatting converted to Markdown equivalent

## Text Formats

### Plain Text (.txt), Markdown (.md), RST (.rst), LaTeX (.tex)
- Passed through with minimal processing
- LaTeX: converted to plain text representation
- RST: basic conversion to Markdown
- Encoding auto-detected (UTF-8, Latin-1, etc.)

### Email (.eml)
- Headers (From, To, Subject, Date) extracted
- Body converted to Markdown
- Attachments listed but not converted inline
- HTML emails rendered as Markdown

## Format Auto-Detection

MarkItDown detects formats by:
1. File extension
2. MIME type (when using `-m` flag)
3. Content sniffing (for stdin input with `-x` flag)

If auto-detection fails, explicitly specify with `-x` or `-m`:

```bash
markitdown input.unknown -x .pdf -o output.md
markitdown input.unknown -m application/pdf -o output.md
```
