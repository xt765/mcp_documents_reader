"""辅助函数和 MCP 工具测试。

测试内容：
- _get_document_path 辅助函数测试
- read_document MCP 工具函数测试
"""

import os
from pathlib import Path
from unittest import mock

from mcp_documents_reader import (
    _get_document_path,
    read_document,
)


class TestGetDocumentPath:
    """_get_document_path 辅助函数测试类。"""

    def test_get_document_path_with_context(self, mock_context: object) -> None:
        """测试从上下文获取文档路径。

        Args:
            mock_context: 模拟的上下文对象
        """
        result = _get_document_path(mock_context, "test.txt")

        # 验证路径正确拼接
        expected = os.path.join(str(Path(__file__).parent / "fixtures"), "test.txt")
        assert result == expected

    def test_get_document_path_without_context_attr(
        self, mock_context_no_attr: object
    ) -> None:
        """测试上下文没有 document_directory 属性时使用默认值。

        Args:
            mock_context_no_attr: 没有 document_directory 属性的模拟上下文
        """
        result = _get_document_path(mock_context_no_attr, "test.txt")

        # 验证路径包含文件名
        assert result.endswith("test.txt")

    def test_get_document_path_with_none_context(self) -> None:
        """测试上下文为 None 时使用默认值。"""
        result = _get_document_path(None, "test.txt")  # type: ignore[arg-type]

        # 验证路径包含文件名
        assert result.endswith("test.txt")

    def test_get_document_path_with_empty_filename(self, mock_context: object) -> None:
        """测试空文件名。

        Args:
            mock_context: 模拟的上下文对象
        """
        result = _get_document_path(mock_context, "")

        # 应返回目录路径
        assert result.endswith("fixtures") or result.endswith("fixtures" + os.sep)

    def test_get_document_path_with_subdirectory(self, mock_context: object) -> None:
        """测试包含子目录的文件名。

        Args:
            mock_context: 模拟的上下文对象
        """
        result = _get_document_path(mock_context, "subdir/test.txt")

        assert "subdir" in result
        assert "test.txt" in result


class TestReadDocument:
    """read_document MCP 工具函数测试类。"""

    def test_read_document_txt_file(self, mock_context: object) -> None:
        """测试读取 TXT 文档。

        Args:
            mock_context: 模拟的上下文对象
        """
        result = read_document(mock_context, "sample.txt")

        assert "测试文本文件" in result
        assert "多行内容" in result

    def test_read_document_docx_file(self, mock_context: object) -> None:
        """测试读取 DOCX 文档。

        Args:
            mock_context: 模拟的上下文对象
        """
        result = read_document(mock_context, "sample.docx")

        assert "测试文档标题" in result

    def test_read_document_pdf_file(self, mock_context: object) -> None:
        """测试读取 PDF 文档。

        Args:
            mock_context: 模拟的上下文对象
        """
        result = read_document(mock_context, "sample.pdf")

        assert "test PDF document" in result

    def test_read_document_excel_file(self, mock_context: object) -> None:
        """测试读取 Excel 文档。

        Args:
            mock_context: 模拟的上下文对象
        """
        result = read_document(mock_context, "sample.xlsx")

        assert "Sheet" in result
        assert "姓名" in result

    def test_read_document_file_not_found(self, mock_context: object) -> None:
        """测试读取不存在的文件。

        Args:
            mock_context: 模拟的上下文对象
        """
        result = read_document(mock_context, "nonexistent.txt")

        assert "Error:" in result
        assert "not found" in result

    def test_read_document_unsupported_type(self, mock_context: object) -> None:
        """测试读取不支持的文件类型。

        Args:
            mock_context: 模拟的上下文对象
        """
        # 先创建一个不支持的文件类型
        fixtures_dir = Path(__file__).parent / "fixtures"
        unsupported_file = fixtures_dir / "test.unsupported"
        unsupported_file.write_text("test content")

        try:
            result = read_document(mock_context, "test.unsupported")

            assert "Error:" in result
            assert "Unsupported document type" in result
        finally:
            # 清理测试文件
            unsupported_file.unlink()

    def test_read_document_empty_file(self, mock_context: object) -> None:
        """测试读取空文件。

        Args:
            mock_context: 模拟的上下文对象
        """
        result = read_document(mock_context, "empty.txt")

        assert "No text found" in result

    def test_read_document_with_corrupted_file(self, mock_context: object) -> None:
        """测试读取损坏的文件。

        Args:
            mock_context: 模拟的上下文对象
        """
        result = read_document(mock_context, "corrupted.docx")

        # 损坏文件应返回错误信息
        assert "Error reading DOCX" in result

    def test_read_document_with_gbk_encoding(self, mock_context: object) -> None:
        """测试读取 GBK 编码的文件。

        Args:
            mock_context: 模拟的上下文对象
        """
        result = read_document(mock_context, "sample_gbk.txt")

        assert "GBK 编码" in result
        assert "中文内容" in result

    def test_read_document_with_path_traversal(
        self, mock_context_with_temp_dir: object
    ) -> None:
        """测试路径遍历安全性（文件不存在）。

        Args:
            mock_context_with_temp_dir: 带有临时目录的模拟上下文
        """
        # 尝试路径遍历攻击
        result = read_document(mock_context_with_temp_dir, "../../../etc/passwd")

        # 应返回文件不存在的错误
        assert "Error:" in result
        assert "not found" in result

    def test_read_document_with_special_characters_in_filename(
        self, mock_context_with_temp_dir: object, temp_document_dir: str
    ) -> None:
        """测试文件名包含特殊字符。

        Args:
            mock_context_with_temp_dir: 带有临时目录的模拟上下文
            temp_document_dir: 临时目录路径
        """
        # 创建包含特殊字符的文件
        special_file = Path(temp_document_dir) / "test file (1).txt"
        special_file.write_text("special content", encoding="utf-8")

        result = read_document(mock_context_with_temp_dir, "test file (1).txt")

        assert "special content" in result


class TestReadDocumentWithMockedFilesystem:
    """使用 mock 文件系统的 read_document 测试类。"""

    @mock.patch("mcp_documents_reader.os.path.exists")
    @mock.patch("mcp_documents_reader.DocumentReaderFactory.is_supported")
    @mock.patch("mcp_documents_reader.DocumentReaderFactory.get_reader")
    def test_read_document_calls_reader_correctly(
        self,
        mock_get_reader: mock.MagicMock,
        mock_is_supported: mock.MagicMock,
        mock_exists: mock.MagicMock,
    ) -> None:
        """测试 read_document 正确调用 Reader。

        Args:
            mock_get_reader: 模拟的 get_reader 方法
            mock_is_supported: 模拟的 is_supported 方法
            mock_exists: 模拟的 exists 方法
        """
        # 设置 mock
        mock_exists.return_value = True
        mock_is_supported.return_value = True
        mock_reader = mock.MagicMock()
        mock_reader.read.return_value = "test content"
        mock_get_reader.return_value = mock_reader

        result = read_document(object(), "test.txt")

        # 验证调用
        mock_exists.assert_called_once()
        mock_is_supported.assert_called_once()
        mock_get_reader.assert_called_once()
        mock_reader.read.assert_called_once()

        assert result == "test content"

    @mock.patch("mcp_documents_reader.os.path.exists")
    def test_read_document_file_not_exists_mock(
        self, mock_exists: mock.MagicMock
    ) -> None:
        """测试文件不存在的情况（使用 mock）。

        Args:
            mock_exists: 模拟的 exists 方法
        """
        mock_exists.return_value = False

        result = read_document(object(), "test.txt")

        assert "Error:" in result
        assert "not found" in result

    @mock.patch("mcp_documents_reader.os.path.exists")
    @mock.patch("mcp_documents_reader.DocumentReaderFactory.is_supported")
    def test_read_document_unsupported_type_mock(
        self, mock_is_supported: mock.MagicMock, mock_exists: mock.MagicMock
    ) -> None:
        """测试不支持的文件类型（使用 mock）。

        Args:
            mock_is_supported: 模拟的 is_supported 方法
            mock_exists: 模拟的 exists 方法
        """
        mock_exists.return_value = True
        mock_is_supported.return_value = False

        result = read_document(object(), "test.xyz")

        assert "Error:" in result
        assert "Unsupported document type" in result

    @mock.patch("mcp_documents_reader.os.path.exists")
    @mock.patch("mcp_documents_reader.DocumentReaderFactory.is_supported")
    @mock.patch("mcp_documents_reader.DocumentReaderFactory.get_reader")
    def test_read_document_reader_exception(
        self,
        mock_get_reader: mock.MagicMock,
        mock_is_supported: mock.MagicMock,
        mock_exists: mock.MagicMock,
    ) -> None:
        """测试 Reader 抛出异常的情况。

        Args:
            mock_get_reader: 模拟的 get_reader 方法
            mock_is_supported: 模拟的 is_supported 方法
            mock_exists: 模拟的 exists 方法
        """
        mock_exists.return_value = True
        mock_is_supported.return_value = True
        mock_get_reader.side_effect = Exception("Reader error")

        result = read_document(object(), "test.txt")

        assert "Error reading document" in result
