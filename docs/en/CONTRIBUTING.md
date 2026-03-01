# Contributing Guide

Thank you for your interest in contributing to MCP Document Reader!

## Table of Contents

- [Quick Start](#quick-start)
- [Development Environment Setup](#development-environment-setup)
- [Code Standards](#code-standards)
- [Commit Conventions](#commit-conventions)
- [Testing Requirements](#testing-requirements)
- [Pull Request Process](#pull-request-process)

---

## Quick Start

1. Fork this repository
2. Clone your fork:
   ```bash
   git clone https://github.com/xt765/mcp_documents_reader.git
   cd mcp_documents_reader
   ```
3. Create a branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

---

## Development Environment Setup

### Prerequisites

- Python 3.10+
- uv (recommended) or pip

### Installation Steps

```bash
# Create virtual environment
uv venv .venv --python 3.13

# Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/macOS

# Install dependencies
uv sync --all-extras
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov

# Run specific test
pytest tests/test_readers.py -v
```

### Code Quality Checks

```bash
# Lint check
ruff check mcp_documents_reader.py tests

# Format check
ruff format --check mcp_documents_reader.py tests

# Type check
basedpyright mcp_documents_reader.py
```

---

## Code Standards

### Style Guide

- Follow PEP 8 conventions
- Use Ruff for formatting and linting
- Maximum line length: 88 characters
- All public functions must have type annotations

### Docstrings

- All public modules, classes, and functions must have docstrings
- Use Google-style docstrings:

```python
def read(self, file_path: str) -> str:
    """
    Read and extract text from the document.

    Args:
        file_path: Path to the document file.

    Returns:
        Extracted text content.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
```

### Code Comments

- Use Chinese comments to explain code logic
- Add file-level, class-level, and function-level comments
- Comment complex logic sections

---

## Commit Conventions

### Commit Message Format

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Types

| Type | Description |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only changes |
| `style` | Code style changes |
| `refactor` | Code refactoring |
| `test` | Add/update tests |
| `chore` | Build/config changes |

### Examples

```
feat(reader): add support for RTF files

fix(pdf): fix text extraction for encrypted PDFs

docs(api): update API reference for v1.1.0

test(readers): add edge case tests for Excel reader
```

---

## Testing Requirements

### Test Standards

- All new features must have tests
- Bug fixes must include regression tests
- Maintain test coverage above 90%

### Test Structure

```
tests/
├── conftest.py           # Shared fixtures
├── test_factory.py       # Factory tests
├── test_lifespan.py      # Lifecycle tests
├── test_readers.py       # Reader tests
└── test_tools.py         # MCP tool tests
```

### Writing Tests

```python
import pytest
from mcp_documents_reader import DocxReader

class TestDocxReader:
    """Test DocxReader class."""

    def test_read_docx_with_content(self, sample_docx_file):
        """Test reading DOCX file with content."""
        reader = DocxReader()
        content = reader.read(str(sample_docx_file))

        assert content is not None
        assert len(content) > 0
```

---

## Pull Request Process

1. **Update Documentation**: Update relevant documentation for your changes
2. **Add Tests**: Add tests for new features or bug fixes
3. **Run Quality Checks**: Ensure all checks pass
   ```bash
   ruff check mcp_documents_reader.py tests
   ruff format --check mcp_documents_reader.py tests
   basedpyright mcp_documents_reader.py
   pytest --cov
   ```
4. **Create PR**: Open a Pull Request with a clear description

### PR Checklist

- [ ] Code follows style guide
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] All tests pass
- [ ] Type checking passes
- [ ] Linting passes

---

## Questions?

Feel free to open an Issue for any questions or discussions!
