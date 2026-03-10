# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.0] - 2025-03-10

### Changed

- **Flexible File Path Access**: Removed `DOCUMENT_DIRECTORY` restriction, now supports absolute and relative paths
  - Removed `DOCUMENT_DIRECTORY` environment variable dependency
  - Removed `AppContext` dataclass and `app_lifespan` function
  - Removed `_get_document_path()` security function
  - `read_document()` now directly uses `Path(filename)` for path handling
- **Simplified Architecture**: Removed FastMCP lifespan configuration for cleaner code
- **Test Suite Optimization**: Removed `test_lifespan.py`, updated `test_tools.py` with new path handling tests

### Removed

- `DOCUMENT_DIRECTORY` environment variable support
- `AppContext` dataclass
- `app_lifespan` async context manager
- `_get_document_path()` helper function

## [1.2.1] - 2025-03-02

### Security Fixes

- **pypdf Security Vulnerabilities**: Upgraded pypdf>=6.7.4, fixing 3 CVEs
  - CVE-2026-28351: RunLengthDecode streams can exhaust RAM
  - CVE-2026-27888: FlateDecode XFA streams can exhaust RAM
  - CVE-2026-27628: Circular references cause infinite loop
- **MCP SDK Upgrade**: Upgraded mcp>=1.26.0
- **Test Code Security**: Refactored path traversal test code to avoid static analysis false positives

### Changed

- **Dependency Upgrades**:
  - mcp>=1.23.0 → mcp>=1.26.0
  - pypdf>=6.7.1 → pypdf>=6.7.4
  - typing_extensions>=4.12.0 → typing_extensions>=4.15.0

## [1.2.0] - 2025-03-02

### Security Fixes

- **MCP SDK Security Vulnerabilities**: Upgraded mcp>=1.23.0, fixed 3 high-severity CVEs
  - CVE-2025-53365: Unhandled exception in Streamable HTTP Transport leading to DoS
  - CVE-2025-53366: FastMCP Server validation error leading to DoS
  - CVE-2025-66416: DNS rebinding protection not enabled by default
- **PyPDF2 Security Vulnerability**: Replaced with pypdf>=6.7.1, fixed CVE-2023-36464
- **Path Traversal Protection**: Added explicit path validation to prevent arbitrary file read attacks
- **Error Message Sanitization**: Removed full paths from error messages to prevent information disclosure

### Added

- **PyPI Package Metadata**: Added project.urls linking to GitHub repository

### Changed

- **Dependency Upgrades**:
  - mcp>=0.1.0 → mcp>=1.23.0
  - PyPDF2>=3.0.1 → pypdf>=6.7.1
  - python-docx>=0.8.11 → python-docx>=1.2.0
  - openpyxl>=3.0.10 → openpyxl>=3.1.5
  - typing_extensions>=4.0.0 → typing_extensions>=4.12.0
- **CI/CD Migration**: Migrated from pip to uv for faster builds

## [1.1.0] - 2025-03-01

### Fixed

- **Python Compatibility**: Use `typing_extensions.override` instead of `typing.override` for Python 3.10+ compatibility
- **Type Checking**: Fixed Basedpyright type errors
  - Fixed `openpyxl.Workbook.active` optional type checking
  - Fixed method override parameter name matching
- **Encoding Handling**: Removed invalid `ansi` encoding (not supported by Python standard library)
- **Test Fix**: Fixed path traversal test case

## [1.0.3] - 2025-03-01

### Added

- **CI/CD Workflows**: Added GitHub Actions workflows for automated testing and release
  - CI workflow: Ruff, Basedpyright, Pytest
  - Release workflow: Publish to PyPI and MCP Registry
  - Support for Python 3.10-3.14

- **Test Suite**: Test coverage improved to 95%
  - 102 test cases covering all core modules
  - Unit tests for all readers
  - Integration tests for MCP tools

- **Documentation**: Added complete documentation structure
  - API Reference
  - User Guide
  - Contributing Guide

### Changed

- **Type Checking**: Switched to Basedpyright for better type inference
- **Code Formatting**: Using Ruff format instead of Black
- **Development Dependencies**: Updated development toolchain

### Fixed

- **Type Safety**: Fixed all Basedpyright type errors
- **Code Quality**: Fixed all Ruff linting issues

## [1.0.2] - 2025-02-28

### Added

- **MCP Tools**: Added complete MCP tool interface
  - `read_document`: Main reading tool
  - Unified interface for all document types

- **Error Handling**: Improved error messages and exception handling
  - Better error messages for unsupported formats
  - Graceful handling of corrupted files

### Changed

- **Architecture**: Improved reader architecture with factory pattern
- **Encoding Detection**: Better automatic encoding detection for text files

## [1.0.1] - 2025-02-27

### Added

- **Excel Support**: Added Excel reader for .xlsx and .xls files
  - Multi-sheet support
  - Cell data extraction

- **PDF Support**: Added PDF reader
  - Text extraction from PDF pages
  - Multi-page support

### Fixed

- **Encoding**: Improved encoding detection for text files
- **Error Messages**: More descriptive error messages

## [1.0.0] - 2025-02-25

### Added

- **Initial Release**: First public release of MCP Document Reader
  - Abstract base class for document readers
  - DOCX reader using python-docx
  - PDF reader using PyPDF2
  - Excel reader using openpyxl
  - Text reader with encoding detection
  - Factory pattern for reader selection
  - MCP protocol support for AI assistants

- **Supported Formats**:
  - Input: DOCX, PDF, Excel (XLSX/XLS), Text

- **Features**:
  - Automatic format detection
  - Encoding detection for text files
  - Error handling for corrupted files
  - MCP tool interface for AI assistants
