# MCP 文档阅读器

该工具基于 MCP 协议开发，支持 Excel（XLSX/XLS）、DOCX、PDF、TXT 等多种主流格式，让AI智能体真正 “读懂” 你的文档，现已成功在Trae IDE测试运行。

项目GitHub代码仓库：[https://github.com/xt765/mcp_documents_reader](https://github.com/xt765/mcp_documents_reader)
项目Gitee代码仓库：[https://gitee.com/xt765/mcp_documents_reader](https://gitee.com/xt765/mcp_documents_reader)

## 安装

### 前提条件

- Python 3.8 或更高版本
- 支持 MCP 的 AI 工具，如 Trae IDE

### 安装步骤

1. 克隆或下载此仓库
2. 安装依赖：
   ```bash
   pip install python-docx PyPDF2 openpyxl
   ```

## 配置

将以下内容添加到 Trae IDE的 config.json 中：

### 选项1：使用GitHub仓库（推荐）
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

### 选项2：使用Gitee仓库
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
