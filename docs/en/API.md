# API Reference

## Table of Contents

- [Core Classes](#core-classes)
  - [DocumentReader](#documentreader)
  - [DocxReader](#docxreader)
  - [PdfReader](#pdfreader)
  - [ExcelReader](#excelreader)
  - [TxtReader](#txtreader)
- [Factory Class](#factory-class)
  - [DocumentReaderFactory](#documentreaderfactory)
- [MCP Tools](#mcp-tools)
  - [read_document](#read_document)

---

## Core Classes

### DocumentReader

Abstract base class for all document readers.

```python
from mcp_documents_reader import DocumentReader

class MyReader(DocumentReader):
    def read(self, file_path: str) -> str:
        # Implement reading logic
        return "content"
```

**Methods:**

| Method | Description |
|--------|-------------|
| `read(file_path: str) -> str` | Read and extract text from the document |

---

### DocxReader

Reads DOCX (Microsoft Word) documents.

```python
from mcp_documents_reader import DocxReader

reader = DocxReader()
content = reader.read("/path/to/document.docx")
```

**Supported Extensions:** `.docx`

**Features:**
- Text extraction
- Table extraction
- Paragraph formatting

---

### PdfReader

Reads PDF documents.

```python
from mcp_documents_reader import PdfReader

reader = PdfReader()
content = reader.read("/path/to/document.pdf")
```

**Supported Extensions:** `.pdf`

**Features:**
- Text extraction from PDF pages
- Multi-page support

---

### ExcelReader

Reads Excel spreadsheets.

```python
from mcp_documents_reader import ExcelReader

reader = ExcelReader()
content = reader.read("/path/to/spreadsheet.xlsx")
```

**Supported Extensions:** `.xlsx`, `.xls`

**Features:**
- Multi-sheet support
- Cell data extraction
- Sheet name listing

---

### TxtReader

Reads plain text files with automatic encoding detection.

```python
from mcp_documents_reader import TxtReader

reader = TxtReader()
content = reader.read("/path/to/file.txt")
```

**Supported Extensions:** `.txt`

**Features:**
- Automatic encoding detection (UTF-8, GBK, etc.)
- Latin-1 fallback for binary files

---

## Factory Class

### DocumentReaderFactory

Factory class for creating appropriate readers based on file extension.

```python
from mcp_documents_reader import DocumentReaderFactory

# Get reader for a file
reader = DocumentReaderFactory.get_reader("document.pdf")

# Check if format is supported
is_supported = DocumentReaderFactory.is_supported("document.pdf")

# Get list of supported extensions
readers_map = DocumentReaderFactory._readers
```

**Methods:**

| Method | Description |
|--------|-------------|
| `get_reader(file_path: str) -> DocumentReader` | Get appropriate reader for the file |
| `is_supported(file_path: str) -> bool` | Check if the file format is supported |

**Supported Extensions:**

| Extension | Reader Class |
|-----------|--------------|
| `.txt` | TxtReader |
| `.docx` | DocxReader |
| `.pdf` | PdfReader |
| `.xlsx` | ExcelReader |
| `.xls` | ExcelReader |

---

## MCP Tools

### read_document

Read any supported document type with a unified interface.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `filename` | string | Yes | Document file path (absolute or relative) |

**Returns:** Extracted text content from the document.

**Example:**

```python
# Read a DOCX file
content = read_document(filename="report.docx")

# Read a PDF file
content = read_document(filename="paper.pdf")

# Read an Excel file
content = read_document(filename="data.xlsx")

# Read a text file
content = read_document(filename="notes.txt")
```

**Error Handling:**

- Returns error message if file not found
- Returns error message for unsupported formats
- Returns error message for corrupted files
