# Advanced Features

## Azure Document Intelligence

For higher-quality PDF extraction (especially scanned documents, forms, and complex layouts), MarkItDown can use Azure's Document Intelligence service:

```bash
markitdown scan.pdf -d -e "https://your-resource.cognitiveservices.azure.com/" -o output.md
```

Requirements:
- Azure account with Document Intelligence resource
- `AZURE_DOCUMENT_INTELLIGENCE_KEY` set in environment, or passed via `--azure-document-intelligence-key`

## Custom Plugins

MarkItDown supports third-party plugins for extending format support. Enable with:

```bash
markitdown input.xyz --use-plugins -o output.md
```

Plugins are discovered automatically from installed Python packages that register `markitdown` entry points.

## Python API — Advanced Usage

### Configure with custom options

```python
from markitdown import MarkItDown

md = MarkItDown(
    enable_plugins=True,      # Enable third-party converters
    keep_data_uris=False,     # Strip inline data URIs to save tokens
)
result = md.convert("input.pdf")
print(result.text_content)
```

### Get metadata alongside text

```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("document.docx")

# Access metadata
print(f"Title: {result.metadata.get('title', 'N/A')}")
print(f"Author: {result.metadata.get('author', 'N/A')}")

# The main content
print(result.text_content)
```

### Stream large files

For very large documents, you can process in chunks:

```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("large_document.pdf")

# Write incrementally to avoid memory issues
with open("output.md", "w") as f:
    f.write(result.text_content)
```

## Using in AI/LLM Pipelines

### RAG (Retrieval-Augmented Generation)

```python
from pathlib import Path
from markitdown import MarkItDown

def build_rag_corpus(input_dir: str, output_dir: str):
    """Convert all documents in input_dir to Markdown for RAG."""
    md = MarkItDown(enable_plugins=True)
    out = Path(output_dir)
    out.mkdir(exist_ok=True)

    for path in Path(input_dir).iterdir():
        if path.suffix.lower() in supported_formats:
            try:
                result = md.convert(str(path))
                (out / f"{path.stem}.md").write_text(
                    f"# {path.stem}\n\n{result.text_content}"
                )
            except Exception as e:
                print(f"Failed: {path.name} — {e}")

# Usage
build_rag_corpus("./docs", "./corpus")
```

### Context Injection for LLM

```python
from markitdown import MarkItDown

def document_to_context(filepath: str, max_chars: int = 50000) -> str:
    """Convert document to LLM-ready context, truncating if needed."""
    md = MarkItDown()
    result = md.convert(filepath)
    content = result.text_content

    if len(content) > max_chars:
        # Keep the first max_chars, add truncation note
        content = content[:max_chars] + "\n\n[Document truncated...]"

    return content

# Use the content as context for an LLM call
context = document_to_context("report.pdf")
```

## Converting Password-Protected Files

MarkItDown cannot natively handle encrypted files. Pre-process them first:

### PDF
```bash
# Remove password with qpdf
qpdf --password=SECRET --decrypt protected.pdf unprotected.pdf
markitdown unprotected.pdf -o output.md
```

### DOCX/XLSX/PPTX
These are ZIP-based formats. Remove protection via the native application (Word, Excel, PowerPoint) or use Python libraries like `msoffcrypto-tool`:

```bash
pip install msoffcrypto-tool
```

```python
import msoffcrypto
from pathlib import Path

# Decrypt first
decrypted = Path("decrypted.docx")
with open("protected.docx", "rb") as f:
    office_file = msoffcrypto.Open(f)
    office_file.load_key("password")
    with open(decrypted, "wb") as out:
        office_file.decrypt(out)

# Then convert
from markitdown import MarkItDown
md = MarkItDown()
result = md.convert(str(decrypted))
```

## Performance Tips

1. **Batch processing**: Convert files in parallel using `concurrent.futures` for multi-file workflows
2. **Selective install**: Only `pip install markitdown` (without `[all]`) if you only need document formats
3. **Memory**: Large PDFs (100MB+) need significant RAM; process sequentially
4. **Caching**: Cache converted results if you re-process the same files frequently
