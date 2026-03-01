# API 参考

## 目录

- [核心类](#核心类)
  - [DocumentReader](#documentreader)
  - [DocxReader](#docxreader)
  - [PdfReader](#pdfreader)
  - [ExcelReader](#excelreader)
  - [TxtReader](#txtreader)
- [工厂类](#工厂类)
  - [DocumentReaderFactory](#documentreaderfactory)
- [MCP 工具](#mcp-工具)
  - [read_document](#read_document)

---

## 核心类

### DocumentReader

所有文档读取器的抽象基类。

```python
from mcp_documents_reader import DocumentReader

class MyReader(DocumentReader):
    def read(self, file_path: str) -> str:
        # 实现读取逻辑
        return "content"
```

**方法：**

| 方法 | 描述 |
|------|------|
| `read(file_path: str) -> str` | 读取并提取文档文本 |

---

### DocxReader

读取 DOCX（Microsoft Word）文档。

```python
from mcp_documents_reader import DocxReader

reader = DocxReader()
content = reader.read("/path/to/document.docx")
```

**支持扩展名：** `.docx`

**特性：**
- 文本提取
- 表格提取
- 段落格式

---

### PdfReader

读取 PDF 文档。

```python
from mcp_documents_reader import PdfReader

reader = PdfReader()
content = reader.read("/path/to/document.pdf")
```

**支持扩展名：** `.pdf`

**特性：**
- 从 PDF 页面提取文本
- 多页支持

---

### ExcelReader

读取 Excel 电子表格。

```python
from mcp_documents_reader import ExcelReader

reader = ExcelReader()
content = reader.read("/path/to/spreadsheet.xlsx")
```

**支持扩展名：** `.xlsx`, `.xls`

**特性：**
- 多工作表支持
- 单元格数据提取
- 工作表名称列表

---

### TxtReader

读取纯文本文件，自动检测编码。

```python
from mcp_documents_reader import TxtReader

reader = TxtReader()
content = reader.read("/path/to/file.txt")
```

**支持扩展名：** `.txt`

**特性：**
- 自动编码检测（UTF-8、GBK 等）
- Latin-1 回退处理二进制文件

---

## 工厂类

### DocumentReaderFactory

根据文件扩展名创建适当读取器的工厂类。

```python
from mcp_documents_reader import DocumentReaderFactory

# 获取文件读取器
reader = DocumentReaderFactory.get_reader("document.pdf")

# 检查格式是否支持
is_supported = DocumentReaderFactory.is_supported("document.pdf")

# 获取支持的扩展名列表
readers_map = DocumentReaderFactory._readers
```

**方法：**

| 方法 | 描述 |
|------|------|
| `get_reader(file_path: str) -> DocumentReader` | 获取适合文件的读取器 |
| `is_supported(file_path: str) -> bool` | 检查文件格式是否支持 |

**支持的扩展名：**

| 扩展名 | 读取器类 |
|--------|----------|
| `.txt` | TxtReader |
| `.docx` | DocxReader |
| `.pdf` | PdfReader |
| `.xlsx` | ExcelReader |
| `.xls` | ExcelReader |

---

## MCP 工具

### read_document

使用统一接口读取任何支持的文档类型。

**参数：**

| 参数 | 类型 | 必需 | 描述 |
|------|------|------|------|
| `filename` | string | 是 | 文档文件路径（绝对路径或相对路径） |

**返回：** 从文档中提取的文本内容。

**示例：**

```python
# 读取 DOCX 文件
content = read_document(filename="report.docx")

# 读取 PDF 文件
content = read_document(filename="paper.pdf")

# 读取 Excel 文件
content = read_document(filename="data.xlsx")

# 读取文本文件
content = read_document(filename="notes.txt")
```

**错误处理：**

- 文件不存在时返回错误信息
- 不支持的格式返回错误信息
- 损坏的文件返回错误信息
