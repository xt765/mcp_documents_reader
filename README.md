# MCP Enabled Document Reader

This tool is built on the Model Context Protocol (MCP) and supports multiple mainstream formats including Excel (XLSX/XLS), DOCX, PDF, and TXT, allowing AI agents to truly "read" your documents. It has been successfully tested and run in Trae IDE.

GitHub Repository: [https://github.com/xt765/mcp_documents_reader](https://github.com/xt765/mcp_documents_reader)
Gitee Repository: [https://gitee.com/xt765/mcp_documents_reader](https://gitee.com/xt765/mcp_documents_reader)

## Installation

### Prerequisites

- Python 3.8 or higher
- An MCP-enabled AI tool like Trae IDE

### Installation Steps

1. Clone or download this repository
2. Install the dependencies:
   ```bash
   pip install python-docx PyPDF2 openpyxl
   ```

## Configuration

Add the following to your Trae IDE's config.json:

### Option 1: Using GitHub repository (Recommended)
```json
{
    "mcpServers": {
        "mcp-document-reader": {
            "command": "uvx",
            "args": [
                "--from",
                "git+https://github.com/xt765/mcp_documents_reader",
                "mcp_documents_reader"
            ]
        }
    }
}
```

### Option 2: Using Gitee repository
```json
{
    "mcpServers": {
        "mcp-document-reader": {
            "command": "uvx",
            "args": [
                "--from",
                "git+https://gitee.com/xt765/mcp_documents_reader",
                "mcp_documents_reader"
            ]
        }
    }
}
```

## Environment Variables

- `DOCUMENT_DIRECTORY` - Directory where documents are stored (default: "./documents")

## Usage

### Supported Document Types

The server supports reading the following document types:
- DOCX
- PDF
- Excel (XLSX, XLS)
- TXT

### Available Tools

#### read_document (Recommended)
Read any supported document type with a single unified interface.

```
read_document(filename="example.docx")
read_document(filename="example.pdf")
read_document(filename="example.xlsx")
read_document(filename="example.txt")
```

#### read_docx
Read a DOCX document.

```
read_docx(filename="example.docx")
```

#### read_pdf
Read a PDF document.

```
read_pdf(filename="example.pdf")
```

#### read_excel
Read an Excel document.

```
read_excel(filename="example.xlsx")
```

## License

MIT