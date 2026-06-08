"""
Standalone batch converter script — run directly without any dependencies beyond markitdown.

Usage:
    python scripts/batch_convert.py ./input_folder ./output_folder
    python scripts/batch_convert.py ./input_folder ./output_folder 8        # 8 parallel workers
    python scripts/batch_convert.py ./input_folder ./output_folder 4 --recursive
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
    out_path = output_dir / f"{filepath.stem}.md"
    try:
        result = md.convert(str(filepath))
        out_path.write_text(result.text_content, encoding="utf-8")
        return f"OK  {filepath.name} -> {out_path.name}"
    except Exception as e:
        return f"ERR {filepath.name}: {e}"


def main():
    if len(sys.argv) < 3:
        print("Usage: python batch_convert.py <input_dir> <output_dir> [parallel=4] [--recursive]")
        sys.exit(1)

    input_dir = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])
    max_workers = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3].isdigit() else 4
    recursive = "--recursive" in sys.argv

    if not input_dir.exists():
        print(f"Error: input directory '{input_dir}' does not exist")
        sys.exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)

    glob_pattern = "**/*" if recursive else "*"
    files = [
        p for p in input_dir.glob(glob_pattern)
        if p.is_file() and p.suffix.lower() in SUPPORTED_EXTENSIONS
    ]

    if not files:
        print(f"No supported files found in {input_dir}")
        sys.exit(0)

    print(f"Converting {len(files)} file(s) from {input_dir} to {output_dir}")
    print(f"Workers: {max_workers} | Recursive: {recursive}")
    print("-" * 60)

    md = MarkItDown()
    ok, fail = 0, 0

    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        futures = {ex.submit(convert_file, md, f, output_dir): f for f in files}
        for future in as_completed(futures):
            msg = future.result()
            print(msg)
            if msg.startswith("OK"):
                ok += 1
            else:
                fail += 1

    print("-" * 60)
    print(f"Done: {ok} ok, {fail} failed, {len(files)} total")


if __name__ == "__main__":
    main()
