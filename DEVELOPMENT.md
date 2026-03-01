# 开发指南

## 环境设置

### 使用 uv 设置开发环境

```bash
# 克隆仓库
git clone https://github.com/xt765/mcp_documents_reader.git
cd mcp_documents_reader

# 创建虚拟环境
uv venv

# 激活虚拟环境
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# Linux/Mac:
source .venv/bin/activate

# 安装开发依赖
uv pip install -e .
uv pip install pytest pytest-asyncio pytest-cov reportlab ruff basedpyright
```

## 运行测试

```bash
# 运行所有测试
uv run pytest tests/ -v

# 运行测试并生成覆盖率报告
uv run pytest tests/ -v --cov=mcp_documents_reader --cov-report=html

# 查看覆盖率报告
# 打开 htmlcov/index.html

# 或使用测试运行脚本
uv run python scripts/run_tests.py --html

# 运行特定测试文件
uv run pytest tests/test_readers.py -v

# 运行特定测试类
uv run pytest tests/test_readers.py::TestDocxReader -v

# 运行特定测试函数
uv run pytest tests/test_readers.py::TestDocxReader::test_read_simple_docx -v
```

## 代码质量检查

```bash
# 运行 linter
uv run ruff check .

# 自动修复问题
uv run ruff check . --fix

# 运行格式化检查
uv run ruff format --check .

# 格式化代码
uv run ruff format .

# 运行类型检查
uv run basedpyright .
```

## 构建项目

```bash
# 安装构建工具
uv pip install build

# 构建分发包
python -m build

# 查看生成的文件
ls dist/
```

## 本地测试 MCP 服务器

```bash
# 启动 MCP 服务器
uv run mcp-documents-reader

# 或者使用模块方式
uv run python -m mcp_documents_reader
```

## 添加新测试

在 `tests/` 目录下添加新的测试文件：

```python
"""新功能的测试"""
import pytest
from mcp_documents_reader import YourNewFeature


class TestYourNewFeature:
    """新功能测试类"""
    
    def test_basic_functionality(self):
        """测试基本功能"""
        # 测试代码
        pass
    
    def test_edge_cases(self):
        """测试边界情况"""
        # 测试代码
        pass
```

## 添加新文件格式支持

1. 创建新的读取器类，继承自 `DocumentReader`
2. 实现 `read()` 方法
3. 在 `DocumentReaderFactory._readers` 中注册新的文件扩展名
4. 添加相应的测试

示例：

```python
class NewFormatReader(DocumentReader):
    """新格式读取器"""
    
    def read(self, file_path: str) -> str:
        """读取新格式文件"""
        # 实现读取逻辑
        pass

# 在 DocumentReaderFactory 中注册
_readers = {
    '.txt': TxtReader,
    '.newformat': NewFormatReader,  # 添加新格式
}
```

## 调试技巧

### 使用 pytest 调试

```bash
# 使用 -s 显示 print 输出
uv run pytest tests/test_file.py -v -s

# 使用 -pdb 在失败时进入调试器
uv run pytest tests/test_file.py -v --pdb

# 设置断点
import pdb; pdb.set_trace()
```

### 日志记录

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("调试信息")
logger.info("一般信息")
logger.warning("警告信息")
logger.error("错误信息")
```

## 性能优化建议

1. **使用 read_only 模式**：读取大型 Excel 文件时使用 `read_only=True`
2. **及时关闭资源**：使用 `with` 语句或显式调用 `close()`
3. **批量处理**：避免逐行处理大文件
4. **使用生成器**：处理大量数据时使用生成器

## 常见问题

### Q: 如何处理编码问题？
A: `TxtReader` 已经内置了多种编码支持，会按优先级尝试：utf-8 > gbk > gb2312 > ansi > latin-1

### Q: 如何测试未实现的特性？
A: 使用 `pytest.mark.skip` 或 `pytest.mark.xfail` 标记测试

```python
@pytest.mark.skip(reason="功能尚未实现")
def test_future_feature():
    pass

@pytest.mark.xfail
def test_expected_to_fail():
    pass
```

### Q: 如何并行运行测试？
A: 安装 pytest-xdist 并使用 `-n` 参数

```bash
uv pip install pytest-xdist
uv run pytest tests/ -n auto
```

## 贡献代码

1. Fork 仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 代码风格

- 遵循 PEP 8 规范
- 使用 ruff 进行代码检查
- 使用 basedpyright 进行类型检查
- 函数控制在 50 行以内
- 添加有意义的注释和文档字符串

## 发布流程

详见 [RELEASE.md](RELEASE.md)
