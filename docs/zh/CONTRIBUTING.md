# 贡献指南

感谢您有兴趣为 MCP Document Reader 做出贡献！

## 目录

- [快速开始](#快速开始)
- [开发环境设置](#开发环境设置)
- [代码规范](#代码规范)
- [提交规范](#提交规范)
- [测试要求](#测试要求)
- [Pull Request 流程](#pull-request-流程)

---

## 快速开始

1. Fork 本仓库
2. 克隆您的 Fork：
   ```bash
   git clone https://github.com/xt765/mcp_documents_reader.git
   cd mcp_documents_reader
   ```
3. 创建分支：
   ```bash
   git checkout -b feature/your-feature-name
   ```

---

## 开发环境设置

### 前置要求

- Python 3.10+
- uv（推荐）或 pip

### 安装步骤

```bash
# 创建虚拟环境
uv venv .venv --python 3.13

# 激活虚拟环境
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/macOS

# 安装依赖
uv sync --all-extras
```

### 运行测试

```bash
# 运行所有测试
pytest

# 带覆盖率运行
pytest --cov

# 运行特定测试
pytest tests/test_readers.py -v
```

### 代码质量检查

```bash
# 代码检查
ruff check mcp_documents_reader.py tests

# 格式检查
ruff format --check mcp_documents_reader.py tests

# 类型检查
basedpyright mcp_documents_reader.py
```

---

## 代码规范

### 风格指南

- 遵循 PEP 8 规范
- 使用 Ruff 进行格式化和代码检查
- 最大行长度：88 字符
- 所有公共函数必须添加类型注解

### 文档注释

- 所有公共模块、类和函数必须添加文档字符串
- 使用 Google 风格的文档字符串：

```python
def read(self, file_path: str) -> str:
    """
    读取并提取文档文本。

    Args:
        file_path: 文档文件路径。

    Returns:
        提取的文本内容。

    Raises:
        FileNotFoundError: 文件不存在时抛出。
    """
```

### 代码注释

- 使用中文注释解释代码逻辑
- 添加文件级、类级、函数级注释
- 对复杂逻辑部分进行注释说明

---

## 提交规范

### 提交消息格式

```
<type>(<scope>): <description>

[可选的正文]

[可选的页脚]
```

### 类型

| 类型 | 描述 |
|------|------|
| `feat` | 新功能 |
| `fix` | Bug 修复 |
| `docs` | 仅文档更改 |
| `style` | 代码风格更改 |
| `refactor` | 代码重构 |
| `test` | 添加/更新测试 |
| `chore` | 构建/配置更改 |

### 示例

```
feat(reader): 添加 RTF 文件支持

fix(pdf): 修复加密 PDF 的文本提取问题

docs(api): 更新 v1.1.0 的 API 参考

test(readers): 添加 Excel 读取器边缘情况测试
```

---

## 测试要求

### 测试规范

- 所有新功能必须有测试
- Bug 修复必须包含回归测试
- 保持测试覆盖率在 90% 以上

### 测试结构

```
tests/
├── conftest.py           # 共享 fixtures
├── test_factory.py       # 工厂类测试
├── test_lifespan.py      # 生命周期测试
├── test_readers.py       # 读取器测试
└── test_tools.py         # MCP 工具测试
```

### 编写测试

```python
import pytest
from mcp_documents_reader import DocxReader

class TestDocxReader:
    """测试 DocxReader 类。"""

    def test_read_docx_with_content(self, sample_docx_file):
        """测试读取包含内容的 DOCX 文件。"""
        reader = DocxReader()
        content = reader.read(str(sample_docx_file))

        assert content is not None
        assert len(content) > 0
```

---

## Pull Request 流程

1. **更新文档**：为您的更改更新相关文档
2. **添加测试**：为新功能或 Bug 修复添加测试
3. **运行质量检查**：确保所有检查通过
   ```bash
   ruff check mcp_documents_reader.py tests
   ruff format --check mcp_documents_reader.py tests
   basedpyright mcp_documents_reader.py
   pytest --cov
   ```
4. **创建 PR**：打开一个包含清晰描述的 Pull Request

### PR 检查清单

- [ ] 代码遵循风格指南
- [ ] 文档已更新
- [ ] 测试已添加/更新
- [ ] 所有测试通过
- [ ] 类型检查通过
- [ ] 代码检查通过

---

## 有问题？

如有任何问题或讨论，请随时开一个 Issue！
