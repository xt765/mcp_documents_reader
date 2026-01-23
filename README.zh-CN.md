# MCP 文档阅读器

模型上下文协议（MCP）服务器提供读取多种文档类型的工具，包括 DOCX、PDF、Excel 和 TXT。

## 安装

### 前提条件

- Python 3.8 或更高版本
- 支持 MCP 的 AI 工具，如 Trae Desktop

### 安装步骤

1. 克隆或下载此仓库
2. 安装依赖：
   ```bash
   pip install python-docx PyPDF2 openpyxl
   ```

## 配置

将以下内容添加到 Trae 的 config.json 中：

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

## 环境变量

- `DOCUMENT_DIRECTORY` - 文档存储目录（默认："./documents"）

## 使用方法

### 支持的文档类型

服务器支持读取以下文档类型：

- DOCX
- PDF
- Excel（XLSX, XLS）
- TXT

### 可用工具

#### read_document（推荐）

使用统一接口读取任何支持的文档类型。

```
read_document(filename="example.docx")
read_document(filename="example.pdf")
read_document(filename="example.xlsx")
read_document(filename="example.txt")
```

#### read_docx

读取 DOCX 文档。

```
read_docx(filename="example.docx")
```

#### read_pdf

读取 PDF 文档。

```
read_pdf(filename="example.pdf")
```

#### read_excel

读取 Excel 文档。

```
read_excel(filename="example.xlsx")
```

## 许可证

MIT