# 更新日志

本项目的所有重要变更都将记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [1.3.0] - 2025-03-10

### 变更

- **灵活的文件路径访问**：移除 `DOCUMENT_DIRECTORY` 限制，现支持绝对路径和相对路径
  - 移除 `DOCUMENT_DIRECTORY` 环境变量依赖
  - 移除 `AppContext` dataclass 和 `app_lifespan` 函数
  - 移除 `_get_document_path()` 安全函数
  - `read_document()` 现直接使用 `Path(filename)` 处理路径
- **简化架构**：移除 FastMCP lifespan 配置，代码更简洁
- **测试套件优化**：删除 `test_lifespan.py`，更新 `test_tools.py` 添加新路径处理测试

### 移除

- `DOCUMENT_DIRECTORY` 环境变量支持
- `AppContext` dataclass
- `app_lifespan` 异步上下文管理器
- `_get_document_path()` 辅助函数

## [1.2.1] - 2025-03-02

### 安全修复

- **pypdf 安全漏洞**：升级 pypdf>=6.7.4，修复 3 个 CVE
  - CVE-2026-28351: RunLengthDecode 流可耗尽 RAM
  - CVE-2026-27888: FlateDecode XFA 流可耗尽 RAM
  - CVE-2026-27628: 循环引用导致无限循环
- **MCP SDK 升级**：升级 mcp>=1.26.0
- **测试代码安全**：重构路径遍历测试代码，避免静态分析误报

### 变更

- **依赖升级**：
  - mcp>=1.23.0 → mcp>=1.26.0
  - pypdf>=6.7.1 → pypdf>=6.7.4
  - typing_extensions>=4.12.0 → typing_extensions>=4.15.0

## [1.2.0] - 2025-03-02

### 安全修复

- **MCP SDK 安全漏洞**：升级 mcp>=1.23.0，修复 3 个高危 CVE
  - CVE-2025-53365: Streamable HTTP Transport 未处理异常导致 DoS
  - CVE-2025-53366: FastMCP Server 验证错误导致 DoS
  - CVE-2025-66416: DNS rebinding 保护默认未启用
- **PyPDF2 安全漏洞**：替换为 pypdf>=6.7.1，修复 CVE-2023-36464
- **路径遍历防护**：添加显式路径验证，防止任意文件读取攻击
- **错误信息脱敏**：移除错误信息中的完整路径，防止信息泄露

### 新增

- **PyPI 包元数据**：添加 project.urls，链接到 GitHub 仓库

### 变更

- **依赖升级**：
  - mcp>=0.1.0 → mcp>=1.23.0
  - PyPDF2>=3.0.1 → pypdf>=6.7.1
  - python-docx>=0.8.11 → python-docx>=1.2.0
  - openpyxl>=3.0.10 → openpyxl>=3.1.5
  - typing_extensions>=4.0.0 → typing_extensions>=4.12.0
- **CI/CD 迁移**：从 pip 迁移到 uv，提升构建速度

## [1.1.0] - 2025-03-01

### 修复

- **Python 兼容性**：使用 `typing_extensions.override` 替代 `typing.override`，兼容 Python 3.10+
- **类型检查**：修复 Basedpyright 类型错误
  - 修复 `openpyxl.Workbook.active` 可选类型检查
  - 修复方法覆写参数名匹配问题
- **编码处理**：移除无效的 `ansi` 编码（Python 标准库不支持）
- **测试修复**：修复路径遍历测试用例

## [1.0.3] - 2025-03-01

### 新增

- **CI/CD 工作流**：添加 GitHub Actions 工作流用于自动化测试和发布
  - CI 工作流：Ruff、Basedpyright、Pytest
  - Release 工作流：发布到 PyPI 和 MCP Registry
  - 支持 Python 3.10-3.14

- **测试套件**：测试覆盖率提升至 95%
  - 102 个测试用例覆盖所有核心模块
  - 所有读取器的单元测试
  - MCP 工具的集成测试

- **文档**：添加完整的文档结构
  - API 参考
  - 用户指南
  - 贡献指南

### 变更

- **类型检查**：切换到 Basedpyright，获得更好的类型推断
- **代码格式化**：使用 Ruff format 替代 Black
- **开发依赖**：更新开发工具链

### 修复

- **类型安全**：修复所有 Basedpyright 类型错误
- **代码质量**：修复所有 Ruff 代码检查问题

## [1.0.2] - 2025-02-28

### 新增

- **MCP 工具**：添加完整的 MCP 工具接口
  - `read_document`：主读取工具
  - 所有文档类型的统一接口

- **错误处理**：改进错误消息和异常处理
  - 不支持格式的更好错误消息
  - 损坏文件的优雅处理

### 变更

- **架构**：使用工厂模式改进读取器架构
- **编码检测**：改进文本文件的自动编码检测

## [1.0.1] - 2025-02-27

### 新增

- **Excel 支持**：添加 Excel 读取器，支持 .xlsx 和 .xls 文件
  - 多工作表支持
  - 单元格数据提取

- **PDF 支持**：添加 PDF 读取器
  - 从 PDF 页面提取文本
  - 多页支持

### 修复

- **编码**：改进文本文件的编码检测
- **错误消息**：更详细的错误消息

## [1.0.0] - 2025-02-25

### 新增

- **首次发布**：MCP Document Reader 首次公开发布
  - 文档读取器抽象基类
  - 使用 python-docx 的 DOCX 读取器
  - 使用 PyPDF2 的 PDF 读取器
  - 使用 openpyxl 的 Excel 读取器
  - 带编码检测的文本读取器
  - 用于读取器选择的工厂模式
  - 支持 AI 助手的 MCP 协议

- **支持的格式**：
  - 输入：DOCX、PDF、Excel（XLSX/XLS）、文本

- **功能特性**：
  - 自动格式检测
  - 文本文件编码检测
  - 损坏文件错误处理
  - AI 助手的 MCP 工具接口
