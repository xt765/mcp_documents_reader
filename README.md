# MCP Document Reader

<!-- mcp-name: io.github.xt765/mcp_documents_reader -->

[![CSDN Blog](https://img.shields.io/badge/CSDN-玄同765-orange.svg?style=flat&logo=csdn)](https://blog.csdn.net/Yunyi_Chi)
[![GitHub Repository](https://img.shields.io/badge/GitHub-mcp_documents_reader-black.svg?style=flat&logo=github)](https://github.com/xt765/mcp_documents_reader)
[![Gitee Repository](https://img.shields.io/badge/Gitee-mcp_documents_reader-red.svg?style=flat&logo=gitee)](https://gitee.com/xt765/mcp_documents_reader)
[![GitHub License](https://img.shields.io/github/license/xt765/mcp_documents_reader.svg?style=flat&logo=github)](https://github.com/xt765/mcp_documents_reader/blob/main/LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg?style=flat&logo=python)](https://www.python.org/downloads/)

MCP (Model Context Protocol) Document Reader - A powerful MCP tool for reading documents in multiple formats, enabling AI agents to truly "read" your documents.

GitHub Repository: [https://github.com/xt765/mcp_documents_reader](https://github.com/xt765/mcp_documents_reader)
Gitee Repository: [https://gitee.com/xt765/mcp_documents_reader](https://gitee.com/xt765/mcp_documents_reader)

## Features

- **Multi-format Support**: Supports 4 mainstream document formats: Excel (XLSX/XLS), DOCX, PDF, and TXT
- **MCP Protocol**: Compliant with MCP standards, can be used as a tool for AI assistants like Trae IDE
- **Easy Integration**: Simple configuration for immediate use
- **Reliable Performance**: Successfully tested and running in Trae IDE
- **File System Support**: Reads documents directly from the file system

## Supported Formats

| Format | Extensions | MIME Type | Features |
|--------|------------|-----------|----------|
| Excel | .xlsx, .xls | application/vnd.openxmlformats-officedocument.spreadsheetml.sheet | Sheet and cell data extraction |
| DOCX | .docx | application/vnd.openxmlformats-officedocument.wordprocessingml.document | Text and structure extraction |
| PDF | .pdf | application/pdf | Text extraction |
| Text | .txt | text/plain | Plain text reading |

## Installation

### Prerequisites

- Python 3.8 or higher
- MCP-enabled AI tool such as Trae IDE

### Installation Steps

```bash
# Clone the repository
git clone https://github.com/xt765/mcp_documents_reader.git
cd mcp_documents_reader

# Install dependencies
pip install -e .
```

## Configuration

### Using in Trae IDE

Add the following to your Trae IDE's MCP configuration:

#### Option 1: Using GitHub repository (Recommended)
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

#### Option 2: Using Gitee repository
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

### Environment Variables

- `DOCUMENT_DIRECTORY` - Directory where documents are stored (default: "./documents")

## Usage

### As an MCP Tool

After configuration, AI assistants can directly call the following tool:

#### read_document (Recommended)
Read any supported document type with a unified interface.

```
read_document(filename="example.docx")
read_document(filename="example.pdf")
read_document(filename="example.xlsx")
read_document(filename="example.txt")
```

## Tool Interface Details

### read_document
Read any supported document type.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| filename | string | ✅ | Document file path, supports absolute or relative paths |

## License

MIT