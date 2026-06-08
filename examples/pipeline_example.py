"""
Complete pipeline: download, convert, and feed to AI context.

Demonstrates a full RAG-style workflow:
1. Convert all documents to Markdown
2. Combine into a single context
3. Track metadata for each document
"""
import json
from pathlib import Path
from datetime import datetime
from markitdown import MarkItDown


def build_knowledge_base(
    input_dir: str,
    output_dir: str,
    index_file: str = "index.json",
):
    """
    Convert all documents and build a searchable knowledge base.

    Args:
        input_dir: Directory with source documents.
        output_dir: Directory for converted Markdown files.
        index_file: JSON index file tracking all documents.

    Returns:
        List of dicts with path, metadata, and content for each document.
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    md = MarkItDown()
    index = []
    documents = []

    supported = {
        ".pdf", ".docx", ".pptx", ".xlsx", ".xls",
        ".html", ".htm", ".csv", ".json", ".xml",
        ".txt", ".md", ".epub", ".eml",
    }

    for filepath in input_path.iterdir():
        if filepath.suffix.lower() not in supported:
            continue

        try:
            result = md.convert(str(filepath))

            # Write individual Markdown file
            md_path = output_path / f"{filepath.stem}.md"
            md_path.write_text(result.text_content, encoding="utf-8")

            # Build index entry with metadata
            entry = {
                "source": str(filepath),
                "markdown": str(md_path),
                "stem": filepath.stem,
                "format": filepath.suffix.lower(),
                "size_bytes": filepath.stat().st_size,
                "content_length": len(result.text_content),
                "converted_at": datetime.now().isoformat(),
                "metadata": getattr(result, "metadata", {}),
            }
            index.append(entry)
            documents.append(entry)
            print(f"Converted: {filepath.name} ({entry['content_length']} chars)")
        except Exception as e:
            print(f"Failed: {filepath.name} — {e}")

    # Write index
    with open(output_path / index_file, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    print(f"\nKnowledge base: {len(index)} documents indexed")
    print(f"Index file: {output_path / index_file}")

    return documents


def merge_as_context(documents: list, max_total_chars: int = 100000) -> str:
    """
    Merge all converted documents into a single AI-ready context string.

    Args:
        documents: List of dicts from build_knowledge_base.
        max_total_chars: Limit total output length.

    Returns:
        Single Markdown string ready for AI context injection.
    """
    parts = ["# Combined Document Context\n"]

    total = 0
    for doc in documents:
        content = Path(doc["markdown"]).read_text(encoding="utf-8")
        header = f"\n## {doc['stem']}\n"
        block = header + content + "\n"

        if total + len(block) > max_total_chars:
            remaining = max_total_chars - total
            if remaining > len(header):
                parts.append(header + content[:remaining - len(header)])
                parts.append("\n\n[Remaining content truncated...]\n")
            break

        parts.append(block)
        total += len(block)

    result = "".join(parts)
    print(f"Merged context: {len(result)} chars from {len(documents)} documents")
    return result


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: python pipeline_example.py <input_dir> <output_dir>")
        print("Example: python pipeline_example.py ./raw_docs ./kb_output")
        sys.exit(1)

    docs = build_knowledge_base(sys.argv[1], sys.argv[2])
    context = merge_as_context(docs)
    context_path = Path(sys.argv[2]) / "merged_context.md"
    Path(context_path).write_text(context, encoding="utf-8")
    print(f"Merged context: {context_path}")
