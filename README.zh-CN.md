# MCP 文档读取器

[![GitHub Repository](https://img.shields.io/badge/GitHub-mcp_documents_reader-blue.svg?style=flat&logo=github)](https://github.com/xt765/mcp_documents_reader)
[![Gitee Repository](https://img.shields.io/badge/Gitee-mcp_documents_reader-red.svg?style=flat&logo=gitee)](https://gitee.com/xt765/mcp_documents_reader)
[![GitHub License](https://img.shields.io/github/license/xt765/mcp_documents_reader.svg?style=flat&logo=github)](https://github.com/xt765/mcp_documents_reader/blob/main/LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg?style=flat&logo=python)](https://www.python.org/downloads/)
[![CSDN Blog](https://img.shields.io/badge/CSDN-玄同765-orange.svg?style=flat&logo=csdn)](https://blog.csdn.net/Yunyi_Chi)

MCP（模型上下文协议）文档读取器 - 一个强大的 MCP 工具，用于读取多种格式的文档，使 AI 智能体能够真正"读取"您的文档。

GitHub 仓库：[https://github.com/xt765/mcp_documents_reader](https://github.com/xt765/mcp_documents_reader)
Gitee 仓库：[https://gitee.com/xt765/mcp_documents_reader](https://gitee.com/xt765/mcp_documents_reader)

## 功能特性

- **多格式支持**：支持 4 种主流文档格式：Excel（XLSX/XLS）、DOCX、PDF 和 TXT
- **MCP 协议**：符合 MCP 标准，可作为 AI 助手（如 Trae IDE）的工具使用
- **易于集成**：简单配置即可立即使用
- **可靠性能**：已在 Trae IDE 中成功测试运行
- **文件系统支持**：直接从文件系统读取文档

## 支持的格式

| 格式 | 扩展名 | MIME 类型 | 特性 |
|------|--------|-----------|------|
| Excel | .xlsx, .xls | application/vnd.openxmlformats-officedocument.spreadsheetml.sheet | 工作表和单元格数据提取 |
| DOCX | .docx | application/vnd.openxmlformats-officedocument.wordprocessingml.document | 文本和结构提取 |
| PDF | .pdf | application/pdf | 文本提取 |
| Text | .txt | text/plain | 纯文本读取 |

## 安装

### 前提条件

- Python 3.8 或更高版本
- 支持 MCP 的 AI 工具，如 Trae IDE

### 安装步骤

```bash
# 克隆仓库
git clone https://github.com/xt765/mcp_documents_reader.git
cd mcp_documents_reader

# 安装依赖
pip install -e .
```

## 配置

### 在 Trae IDE 中使用

将以下内容添加到 Trae IDE 的 MCP 配置中：

#### 选项 1：使用 GitHub 仓库（推荐）
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

#### 选项 2：使用 Gitee 仓库
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

### 环境变量

- `DOCUMENT_DIRECTORY` - 存储文档的目录（默认："./documents"）

## 使用方法

### 作为 MCP 工具使用

配置完成后，AI 助手可以直接调用以下工具：

#### read_document（推荐）
使用统一接口读取任何支持的文档类型。

```
read_document(filename="example.docx")
read_document(filename="example.pdf")
read_document(filename="example.xlsx")
read_document(filename="example.txt")
```

## 工具接口详情

### read_document
读取任何支持的文档类型。

**参数：**

| 参数 | 类型 | 必填 | 描述 |
|------|------|------|------|
| filename | string | ✅ | 文档文件路径，支持绝对路径或相对路径 |

## 许可证

MIT
