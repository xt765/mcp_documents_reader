# 用户指南

## 目录

- [快速开始](#快速开始)
- [MCP 配置](#mcp-配置)
  - [Trae IDE](#trae-ide)
  - [Claude Desktop](#claude-desktop)
  - [Cherry Studio](#cherry-studio)
- [作为 Python 库使用](#作为-python-库使用)
- [常见问题](#常见问题)

---

## 快速开始

### 安装

```bash
pip install mcp-documents-reader
```

### 基本使用

```python
from mcp_documents_reader import DocumentReaderFactory

# 获取适合的读取器
reader = DocumentReaderFactory.get_reader("document.docx")
content = reader.read("/path/to/document.docx")
print(content)
```

---

## MCP 配置

### Trae IDE

添加到 MCP 配置文件：

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

在 Cherry Studio 设置中添加相同的 MCP 服务器配置。

---

## 作为 Python 库使用

### 基本读取

```python
from mcp_documents_reader import (
    DocumentReaderFactory,
    DocxReader,
    PdfReader,
    ExcelReader,
    TxtReader,
)

# 使用工厂类（推荐）
reader = DocumentReaderFactory.get_reader("document.pdf")
content = reader.read("/path/to/document.pdf")

# 直接使用特定读取器
docx_reader = DocxReader()
content = docx_reader.read("/path/to/document.docx")

# 检查格式是否支持
if DocumentReaderFactory.is_supported("file.xlsx"):
    reader = DocumentReaderFactory.get_reader("file.xlsx")
    content = reader.read("/path/to/file.xlsx")
```

### 错误处理

```python
from mcp_documents_reader import DocumentReaderFactory

try:
    reader = DocumentReaderFactory.get_reader("document.docx")
    content = reader.read("/path/to/document.docx")
except ValueError as e:
    print(f"不支持的格式: {e}")
except FileNotFoundError:
    print("文件不存在")
except Exception as e:
    print(f"读取文件错误: {e}")
```

### 批量处理

```python
from pathlib import Path
from mcp_documents_reader import DocumentReaderFactory

# 读取目录下所有支持的文档
for file_path in Path("documents").iterdir():
    if DocumentReaderFactory.is_supported(file_path.name):
        reader = DocumentReaderFactory.get_reader(file_path.name)
        content = reader.read(str(file_path))
        print(f"已读取 {file_path}: {len(content)} 个字符")
```

---

## 常见问题

### Q: 支持哪些格式？

**A:** 读取器支持 4 种文档格式：
- **Excel:** .xlsx, .xls
- **DOCX:** .docx
- **PDF:** .pdf
- **文本:** .txt

### Q: 如何处理文本文件的编码问题？

**A:** TxtReader 使用 chardet 自动检测编码，支持 UTF-8、GBK 等常见编码。

```python
from mcp_documents_reader import TxtReader

reader = TxtReader()
# 自动检测编码
content = reader.read("chinese_text.txt")
```

### Q: 能否读取加密文件？

**A:** 不能，读取器不支持加密文件。需要先移除密码保护。

### Q: 在 Windows 上能正常工作吗？

**A:** 是的，读取器支持 Windows、macOS 和 Linux。

### Q: 如何处理损坏的文件？

**A:** 读取器在读取损坏文件时会抛出异常，使用 try-except 处理：

```python
try:
    content = reader.read("potentially_corrupted.docx")
except Exception as e:
    print(f"读取文件失败: {e}")
```

### Q: 能否从 URL 读取文件？

**A:** 不能，读取器只支持本地文件路径。如果需要从 URL 读取，请先下载文件。

### Q: 最大文件大小是多少？

**A:** 没有硬性限制，但非常大的文件可能会导致内存问题。对于大型 Excel 文件，建议只读取特定工作表。
