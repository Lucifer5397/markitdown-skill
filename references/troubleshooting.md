# Troubleshooting

## Common Issues

### "command not found: markitdown"

MarkItDown CLI is not installed or not in PATH.

**Fix:**
```bash
pip install "markitdown[all]"
```
Or use `python -m markitdown` instead of `markitdown`.

### PDF output is empty or scrambled

The PDF likely contains only scanned images (no text layer).

**Fixes:**
1. Install Tesseract for local OCR: `brew install tesseract` / `apt-get install tesseract-ocr`
2. Use Azure Document Intelligence: `markitdown scan.pdf -d -e "..." -o output.md`
3. Try a different PDF extraction tool first (e.g., `pymupdf`)

### "Tesseract not found" error

Tesseract OCR is referenced but not installed on the system.

**Fix:** Install Tesseract (see [Installation Guide](installation.md)) or ensure it's in your PATH.

### Audio transcription returns empty

Possible causes:
1. No speech detected (music-only file, instrumental)
2. ffmpeg not installed
3. File format not supported

**Fix:**
```bash
# Verify ffmpeg is installed
ffmpeg -version

# Check the audio file is valid
ffmpeg -i recording.mp3
```

### Excel tables look wrong

Complex spreadsheets with merged cells, multi-level headers, or embedded charts may not convert cleanly.

**Workaround:** Export Excel to CSV first, then convert the CSV.

### "ModuleNotFoundError: No module named 'markitdown'"

The Python package is not installed in the current environment.

**Fix:**
```bash
pip install "markitdown[all]"
```

If using a virtual environment, ensure it's activated first.

### Very slow conversion on large PDFs

Large PDFs (100MB+, 500+ pages) take time to process.

**Tips:**
- Split PDF into smaller chunks first
- Use `pdftotext` for text-only extraction as a faster alternative
- Consider Azure Document Intelligence for server-side processing

### ZIP conversion produces incomplete output

Some files within the ZIP may fail to convert while others succeed. Each failure is non-fatal.

**Check:** Look for "Skipped" or "Failed" messages in the output. These indicate specific files that couldn't be processed.

### "Permission denied" when writing output

The output directory or file is not writable.

**Fix:**
```bash
# Check write permissions
ls -la output/

# Write to a different location
markitdown input.pdf -o /tmp/output.md
```

### YouTube URL fails

**Possible causes:**
1. Video has captions disabled
2. Video is private/age-restricted
3. Network connectivity issues
4. YouTube API rate limiting

**Workaround:** Download captions manually via youtube-dl/yt-dlp first.

## Getting Help

If these solutions don't work:
- Open an issue: https://github.com/microsoft/markitdown/issues
- Search existing issues for similar problems
- Include: OS, Python version, markitdown version, and the exact command you ran
