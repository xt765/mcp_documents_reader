# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
