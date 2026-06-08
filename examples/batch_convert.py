"""
Batch convert all supported files in a directory to Markdown.
"""
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from markitdown import MarkItDown

SUPPORTED_EXTENSIONS = {
    ".pdf", ".docx", ".pptx", ".xlsx", ".xls",
    ".html", ".htm", ".csv", ".json", ".xml",
    ".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".tiff",
    ".mp3", ".wav", ".flac", ".ogg", ".m4a", ".wma",
    ".zip", ".epub", ".eml", ".txt", ".md",
}


def convert_file(md: MarkItDown, filepath: Path, output_dir: Path) -> str:
    """Convert a single file. Returns status message."""
    out_path = output_dir / f"{filepath.stem}.md"
    try:
        result = md.convert(str(filepath))
        out_path.write_text(result.text_content, encoding="utf-8")
        return f"OK: {filepath.name} -> {out_path.name}"
    except Exception as e:
        return f"FAIL: {filepath.name} — {e}"


def batch_convert(
    input_dir: str,
    output_dir: str,
    parallel: int = 4,
    recursive: bool = False,
):
    """
    Convert all supported files in input_dir to Markdown.

    Args:
        input_dir: Directory containing source files.
        output_dir: Directory for Markdown output.
        parallel: Number of parallel conversions.
        recursive: Whether to search subdirectories.
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Collect files
    glob_pattern = "**/*" if recursive else "*"
    files = [
        p for p in input_path.glob(glob_pattern)
        if p.is_file() and p.suffix.lower() in SUPPORTED_EXTENSIONS
    ]

    if not files:
        print(f"No supported files found in {input_dir}")
        return

    print(f"Found {len(files)} file(s) to convert")
    print(f"Output directory: {output_path}")
    print("-" * 50)

    md = MarkItDown()
    success, fail = 0, 0

    with ThreadPoolExecutor(max_workers=parallel) as executor:
        futures = {
            executor.submit(convert_file, md, f, output_path): f
            for f in files
        }
        for future in as_completed(futures):
            print(future.result())
            if future.result().startswith("OK"):
                success += 1
            else:
                fail += 1

    print("-" * 50)
    print(f"Done: {success} succeeded, {fail} failed, {len(files)} total")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python batch_convert.py <input_dir> <output_dir> [parallel=4] [--recursive]")
        print("Example: python batch_convert.py ./docs ./output 4 --recursive")
        sys.exit(1)

    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    parallel = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3].isdigit() else 4
    recursive = "--recursive" in sys.argv

    batch_convert(input_dir, output_dir, parallel=parallel, recursive=recursive)
