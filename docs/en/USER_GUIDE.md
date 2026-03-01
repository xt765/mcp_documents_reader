# User Guide

## Table of Contents

- [Quick Start](#quick-start)
- [MCP Configuration](#mcp-configuration)
  - [Trae IDE](#trae-ide)
  - [Claude Desktop](#claude-desktop)
  - [Cherry Studio](#cherry-studio)
- [Using as Python Library](#using-as-python-library)
- [FAQ](#faq)

---

## Quick Start

### Installation

```bash
pip install mcp-documents-reader
```

### Basic Usage

```python
from mcp_documents_reader import DocumentReaderFactory

# Get reader for a specific file type
reader = DocumentReaderFactory.get_reader("document.docx")
content = reader.read("/path/to/document.docx")
print(content)
```

---

## MCP Configuration

### Trae IDE

Add to your MCP configuration file:

```json
{
  "mcpServers": {
    "mcp-document-reader": {
      "command": "uvx",
      "args": ["mcp-documents-reader"]
    }
  }
}
```

### Claude Desktop

```json
{
  "mcpServers": {
    "mcp-document-reader": {
      "command": "uvx",
      "args": ["mcp-documents-reader"]
    }
  }
}
```

### Cherry Studio

Add the MCP server configuration in Cherry Studio settings with the same configuration as above.

---

## Using as Python Library

### Basic Reading

```python
from mcp_documents_reader import (
    DocumentReaderFactory,
    DocxReader,
    PdfReader,
    ExcelReader,
    TxtReader,
)

# Using factory (recommended)
reader = DocumentReaderFactory.get_reader("document.pdf")
content = reader.read("/path/to/document.pdf")

# Using specific reader directly
docx_reader = DocxReader()
content = docx_reader.read("/path/to/document.docx")

# Check if format is supported
if DocumentReaderFactory.is_supported("file.xlsx"):
    reader = DocumentReaderFactory.get_reader("file.xlsx")
    content = reader.read("/path/to/file.xlsx")
```

### Error Handling

```python
from mcp_documents_reader import DocumentReaderFactory

try:
    reader = DocumentReaderFactory.get_reader("document.docx")
    content = reader.read("/path/to/document.docx")
except ValueError as e:
    print(f"Unsupported format: {e}")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"Error reading file: {e}")
```

### Batch Processing

```python
from pathlib import Path
from mcp_documents_reader import DocumentReaderFactory

# Read all supported documents in a directory
for file_path in Path("documents").iterdir():
    if DocumentReaderFactory.is_supported(file_path.name):
        reader = DocumentReaderFactory.get_reader(file_path.name)
        content = reader.read(str(file_path))
        print(f"Read {file_path}: {len(content)} characters")
```

---

## FAQ

### Q: What formats are supported?

**A:** The reader supports 4 document formats:
- **Excel:** .xlsx, .xls
- **DOCX:** .docx
- **PDF:** .pdf
- **Text:** .txt

### Q: How to handle encoding issues with text files?

**A:** The TxtReader automatically detects encoding using chardet. It supports UTF-8, GBK, and other common encodings.

```python
from mcp_documents_reader import TxtReader

reader = TxtReader()
# Automatically detects encoding
content = reader.read("chinese_text.txt")
```

### Q: Can I read password-protected files?

**A:** No, the reader does not support password-protected files. You need to remove the password protection first.

### Q: Does it work on Windows?

**A:** Yes, the reader supports Windows, macOS, and Linux.

### Q: How to handle corrupted files?

**A:** The reader will raise an exception when reading corrupted files. Handle it with try-except:

```python
try:
    content = reader.read("potentially_corrupted.docx")
except Exception as e:
    print(f"Failed to read file: {e}")
```

### Q: Can I read files from URLs?

**A:** No, the reader only supports local file paths. Download the file first if you need to read from a URL.

### Q: What is the maximum file size?

**A:** There's no hard limit, but very large files may cause memory issues. For large Excel files, consider reading specific sheets only.
