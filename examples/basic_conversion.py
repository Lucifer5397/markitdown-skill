"""
Basic MarkItDown conversion examples.
"""
from pathlib import Path
from markitdown import MarkItDown

# Initialize converter
md = MarkItDown()

# === Example 1: Convert PDF to Markdown file ===
def convert_pdf(pdf_path: str, output_path: str = None):
    """Convert a PDF to Markdown."""
    result = md.convert(pdf_path)
    if output_path is None:
        output_path = str(Path(pdf_path).with_suffix(".md"))
    Path(output_path).write_text(result.text_content)
    print(f"Converted: {pdf_path} -> {output_path}")
    return result.text_content

# === Example 2: Convert Word document ===
def convert_docx(docx_path: str):
    """Convert a Word document to Markdown."""
    result = md.convert(docx_path)
    return result.text_content

# === Example 3: Convert Excel to Markdown table ===
def convert_excel(xlsx_path: str):
    """Convert Excel to Markdown (tables preserved)."""
    result = md.convert(xlsx_path)
    return result.text_content

# === Example 4: Convert image with OCR ===
def ocr_image(image_path: str):
    """Extract text from an image via OCR."""
    result = md.convert(image_path)
    return result.text_content

# === Example 5: Convert audio to transcript ===
def transcribe_audio(audio_path: str):
    """Transcribe audio file to text."""
    result = md.convert(audio_path)
    return result.text_content

# === Example 6: Convert HTML to Markdown ===
def convert_html(html_path: str):
    """Convert HTML file to Markdown."""
    result = md.convert(html_path)
    return result.text_content

# === Example 7: Convert YouTube video to transcript ===
def youtube_transcript(url: str):
    """Get transcript from a YouTube video."""
    result = md.convert(url)
    return result.text_content

# === Example 8: Convert and include metadata ===
def convert_with_metadata(filepath: str):
    """Convert file and display any available metadata."""
    result = md.convert(filepath)
    meta = result.metadata if hasattr(result, 'metadata') else {}
    print(f"File: {filepath}")
    for key, value in meta.items():
        print(f"  {key}: {value}")
    print(f"  Content length: {len(result.text_content)} chars")
    return result.text_content


if __name__ == "__main__":
    # Demo: convert a file (change the path to test)
    import sys
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        text = md.convert(filepath).text_content
        print(text)
    else:
        print("Usage: python basic_conversion.py <filepath>")
