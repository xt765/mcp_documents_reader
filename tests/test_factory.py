"""DocumentReaderFactory 工厂类测试。

测试内容：
- get_reader 方法测试
- is_supported 方法测试
- 支持的文件类型验证
- 不支持的文件类型处理
"""

import pytest

from mcp_documents_reader import (
    DocxReader,
    DocumentReaderFactory,
    ExcelReader,
    PdfReader,
    TxtReader,
)


class TestDocumentReaderFactory:
    """DocumentReaderFactory 工厂类测试类。"""

    # ==================== get_reader 方法测试 ====================

    @pytest.mark.parametrize(
        "file_path,expected_reader",
        [
            ("test.txt", TxtReader),
            ("test.TXT", TxtReader),
            ("document.docx", DocxReader),
            ("document.DOCX", DocxReader),
            ("report.pdf", PdfReader),
            ("report.PDF", PdfReader),
            ("data.xlsx", ExcelReader),
            ("data.XLSX", ExcelReader),
            ("data.xls", ExcelReader),
            ("data.XLS", ExcelReader),
        ],
    )
    def test_get_reader_supported_types(
        self, file_path: str, expected_reader: type
    ) -> None:
        """测试获取支持的文件类型的 Reader。

        Args:
            file_path: 文件路径
            expected_reader: 期望的 Reader 类型
        """
        reader = DocumentReaderFactory.get_reader(file_path)
        assert isinstance(reader, expected_reader)

    def test_get_reader_unsupported_type(self) -> None:
        """测试获取不支持的文件类型应抛出异常。"""
        with pytest.raises(ValueError) as exc_info:
            DocumentReaderFactory.get_reader("test.unknown")

        assert "Unsupported document type" in str(exc_info.value)

    @pytest.mark.parametrize(
        "file_path",
        [
            "test.json",
            "test.xml",
            "test.csv",
            "test.html",
            "test.md",
            "test.rtf",
            "test.odt",
            "test.ods",
            "test",
            "test.",
        ],
    )
    def test_get_reader_various_unsupported_types(self, file_path: str) -> None:
        """测试各种不支持的文件类型。

        Args:
            file_path: 不支持的文件路径
        """
        with pytest.raises(ValueError):
            DocumentReaderFactory.get_reader(file_path)

    def test_get_reader_with_path_containing_dots(self) -> None:
        """测试文件名包含多个点的情况。"""
        reader = DocumentReaderFactory.get_reader("my.document.final.txt")
        assert isinstance(reader, TxtReader)

    def test_get_reader_with_directory_path(self) -> None:
        """测试包含目录路径的文件。"""
        reader = DocumentReaderFactory.get_reader("/path/to/document.pdf")
        assert isinstance(reader, PdfReader)

    def test_get_reader_with_windows_path(self) -> None:
        """测试 Windows 路径格式。"""
        reader = DocumentReaderFactory.get_reader(r"C:\Users\test\document.xlsx")
        assert isinstance(reader, ExcelReader)

    # ==================== is_supported 方法测试 ====================

    @pytest.mark.parametrize(
        "file_path",
        [
            "test.txt",
            "test.TXT",
            "test.docx",
            "test.DOCX",
            "test.pdf",
            "test.PDF",
            "test.xlsx",
            "test.XLSX",
            "test.xls",
            "test.XLS",
        ],
    )
    def test_is_supported_returns_true(self, file_path: str) -> None:
        """测试支持的文件类型返回 True。

        Args:
            file_path: 支持的文件路径
        """
        assert DocumentReaderFactory.is_supported(file_path) is True

    @pytest.mark.parametrize(
        "file_path",
        [
            "test.json",
            "test.xml",
            "test.csv",
            "test.html",
            "test.md",
            "test.unknown",
            "test",
            "test.",
            "",
        ],
    )
    def test_is_supported_returns_false(self, file_path: str) -> None:
        """测试不支持的文件类型返回 False。

        Args:
            file_path: 不支持的文件路径
        """
        assert DocumentReaderFactory.is_supported(file_path) is False

    def test_is_supported_case_insensitive(self) -> None:
        """测试文件扩展名大小写不敏感。"""
        assert DocumentReaderFactory.is_supported("test.TXT") is True
        assert DocumentReaderFactory.is_supported("test.Docx") is True
        assert DocumentReaderFactory.is_supported("test.PdF") is True

    def test_is_supported_with_complex_paths(self) -> None:
        """测试复杂路径的支持检测。"""
        assert DocumentReaderFactory.is_supported("/a/b/c/d/file.txt") is True
        assert DocumentReaderFactory.is_supported(r"C:\Users\test\file.docx") is True
        assert DocumentReaderFactory.is_supported("./relative/path/file.pdf") is True

    # ==================== 返回新实例测试 ====================

    def test_get_reader_returns_new_instance(self) -> None:
        """测试每次调用返回新的 Reader 实例。"""
        reader1 = DocumentReaderFactory.get_reader("test.txt")
        reader2 = DocumentReaderFactory.get_reader("test.txt")

        assert reader1 is not reader2
        assert isinstance(reader1, TxtReader)
        assert isinstance(reader2, TxtReader)

    # ==================== 内部映射测试 ====================

    def test_readers_mapping_contains_expected_types(self) -> None:
        """测试内部映射包含所有预期的文件类型。"""
        readers = DocumentReaderFactory._readers

        assert ".txt" in readers
        assert ".docx" in readers
        assert ".pdf" in readers
        assert ".xlsx" in readers
        assert ".xls" in readers

        assert readers[".txt"] == TxtReader
        assert readers[".docx"] == DocxReader
        assert readers[".pdf"] == PdfReader
        assert readers[".xlsx"] == ExcelReader
        assert readers[".xls"] == ExcelReader
