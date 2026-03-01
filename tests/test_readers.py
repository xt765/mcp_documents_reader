"""DocumentReader 抽象基类及各 Reader 实现测试。

测试内容：
- DocumentReader 抽象基类验证
- DocxReader 单元测试
- PdfReader 单元测试
- TxtReader 单元测试（多种编码）
- ExcelReader 单元测试
"""

from pathlib import Path

import pytest

from mcp_documents_reader import (
    DocumentReader,
    DocxReader,
    ExcelReader,
    PdfReader,
    TxtReader,
)


class TestDocumentReader:
    """DocumentReader 抽象基类测试类。"""

    def test_cannot_instantiate_abstract_class(self) -> None:
        """测试无法直接实例化抽象基类。"""
        with pytest.raises(TypeError):
            DocumentReader()  # type: ignore[abstract]

    def test_subclass_must_implement_read(self) -> None:
        """测试子类必须实现 read 方法。"""

        class IncompleteReader(DocumentReader):
            """不完整的 Reader 实现。"""

            pass

        with pytest.raises(TypeError):
            IncompleteReader()  # type: ignore[abstract]

    def test_subclass_with_read_implementation(self) -> None:
        """测试正确实现 read 方法的子类可以实例化。"""

        class CompleteReader(DocumentReader):
            """完整的 Reader 实现。"""

            def read(self, _file_path: str) -> str:
                """读取文件内容。"""
                return "test content"

        reader = CompleteReader()
        assert reader.read("test.txt") == "test content"


class TestDocxReader:
    """DocxReader 测试类。"""

    def test_read_docx_with_content(self, sample_docx_file: Path) -> None:
        """测试读取包含内容的 DOCX 文件。

        Args:
            sample_docx_file: 示例 DOCX 文件路径
        """
        reader = DocxReader()
        result = reader.read(str(sample_docx_file))

        # 验证提取的内容包含预期文本
        assert "测试文档标题" in result
        assert "第一段文本内容" in result
        assert "第二段文本内容" in result

    def test_read_docx_with_table(self, sample_docx_file: Path) -> None:
        """测试读取包含表格的 DOCX 文件。

        Args:
            sample_docx_file: 示例 DOCX 文件路径
        """
        reader = DocxReader()
        result = reader.read(str(sample_docx_file))

        # 验证表格内容被提取
        assert "姓名" in result
        assert "年龄" in result
        assert "张三" in result
        assert "李四" in result

    def test_read_empty_docx(self, empty_docx_file: Path) -> None:
        """测试读取空的 DOCX 文件。

        Args:
            empty_docx_file: 空 DOCX 文件路径
        """
        reader = DocxReader()
        result = reader.read(str(empty_docx_file))

        # 空文档应返回提示信息
        assert "No text found" in result

    def test_read_corrupted_docx(self, fixtures_dir: Path) -> None:
        """测试读取损坏的 DOCX 文件。

        Args:
            fixtures_dir: fixtures 目录路径
        """
        reader = DocxReader()
        corrupted_file = fixtures_dir / "corrupted.docx"
        result = reader.read(str(corrupted_file))

        # 损坏文件应返回错误信息
        assert "Error reading DOCX" in result

    def test_read_nonexistent_file(self) -> None:
        """测试读取不存在的文件。"""
        reader = DocxReader()
        result = reader.read("/nonexistent/path/file.docx")

        assert "Error reading DOCX" in result


class TestPdfReader:
    """PdfReader 测试类。"""

    def test_read_pdf_with_content(self, sample_pdf_file: Path) -> None:
        """测试读取包含内容的 PDF 文件。

        Args:
            sample_pdf_file: 示例 PDF 文件路径
        """
        reader = PdfReader()
        result = reader.read(str(sample_pdf_file))

        # 验证提取的内容包含预期文本
        assert "test PDF document" in result
        assert "multiple lines" in result

    def test_read_empty_pdf(self, empty_pdf_file: Path) -> None:
        """测试读取空的 PDF 文件。

        Args:
            empty_pdf_file: 空 PDF 文件路径
        """
        reader = PdfReader()
        result = reader.read(str(empty_pdf_file))

        # 空 PDF 应返回提示信息
        assert "No text found" in result

    def test_read_corrupted_pdf(self, fixtures_dir: Path) -> None:
        """测试读取损坏的 PDF 文件。

        Args:
            fixtures_dir: fixtures 目录路径
        """
        reader = PdfReader()
        corrupted_file = fixtures_dir / "corrupted.pdf"
        result = reader.read(str(corrupted_file))

        # 损坏文件应返回错误信息
        assert "Error reading PDF" in result

    def test_read_nonexistent_file(self) -> None:
        """测试读取不存在的文件。"""
        reader = PdfReader()
        result = reader.read("/nonexistent/path/file.pdf")

        assert "Error reading PDF" in result


class TestTxtReader:
    """TxtReader 测试类。"""

    def test_read_utf8_txt(self, sample_txt_file: Path) -> None:
        """测试读取 UTF-8 编码的 TXT 文件。

        Args:
            sample_txt_file: 示例 TXT 文件路径
        """
        reader = TxtReader()
        result = reader.read(str(sample_txt_file))

        # 验证提取的内容
        assert "测试文本文件" in result
        assert "多行内容" in result
        assert "中文" in result

    def test_read_gbk_txt(self, sample_txt_gbk_file: Path) -> None:
        """测试读取 GBK 编码的 TXT 文件。

        Args:
            sample_txt_gbk_file: GBK 编码的示例 TXT 文件路径
        """
        reader = TxtReader()
        result = reader.read(str(sample_txt_gbk_file))

        # 验证 GBK 编码文件被正确读取
        assert "GBK 编码" in result
        assert "中文内容" in result

    def test_read_empty_txt(self, empty_txt_file: Path) -> None:
        """测试读取空的 TXT 文件。

        Args:
            empty_txt_file: 空 TXT 文件路径
        """
        reader = TxtReader()
        result = reader.read(str(empty_txt_file))

        # 空文件应返回提示信息
        assert "No text found" in result

    def test_read_binary_file(self, fixtures_dir: Path) -> None:
        """测试读取二进制文件。

        注意：latin-1 编码可以解码任何字节序列，所以二进制文件
        会被 latin-1 成功读取，返回解码后的内容。

        Args:
            fixtures_dir: fixtures 目录路径
        """
        reader = TxtReader()
        binary_file = fixtures_dir / "binary.txt"
        result = reader.read(str(binary_file))

        # latin-1 可以解码任何字节，所以会返回解码后的内容
        # 验证返回的是解码后的内容，而不是错误信息
        assert result != ""
        assert "Error reading TXT" not in result

    def test_read_nonexistent_file(self) -> None:
        """测试读取不存在的文件。"""
        reader = TxtReader()
        result = reader.read("/nonexistent/path/file.txt")

        # 不存在的文件应返回错误信息
        assert "Error reading TXT" in result


class TestExcelReader:
    """ExcelReader 测试类。"""

    def test_read_excel_with_content(self, sample_excel_file: Path) -> None:
        """测试读取包含内容的 Excel 文件。

        Args:
            sample_excel_file: 示例 Excel 文件路径
        """
        reader = ExcelReader()
        result = reader.read(str(sample_excel_file))

        # 验证提取的内容包含工作表标题
        assert "=== Sheet: Sheet1 ===" in result
        assert "=== Sheet: Sheet2 ===" in result

    def test_read_excel_sheet1_data(self, sample_excel_file: Path) -> None:
        """测试读取 Excel Sheet1 数据。

        Args:
            sample_excel_file: 示例 Excel 文件路径
        """
        reader = ExcelReader()
        result = reader.read(str(sample_excel_file))

        # 验证 Sheet1 数据
        assert "姓名" in result
        assert "年龄" in result
        assert "张三" in result
        assert "李四" in result

    def test_read_excel_sheet2_data(self, sample_excel_file: Path) -> None:
        """测试读取 Excel Sheet2 数据。

        Args:
            sample_excel_file: 示例 Excel 文件路径
        """
        reader = ExcelReader()
        result = reader.read(str(sample_excel_file))

        # 验证 Sheet2 数据
        assert "产品" in result
        assert "价格" in result
        assert "苹果" in result
        assert "香蕉" in result

    def test_read_empty_excel(self, empty_excel_file: Path) -> None:
        """测试读取空的 Excel 文件。

        Args:
            empty_excel_file: 空 Excel 文件路径
        """
        reader = ExcelReader()
        result = reader.read(str(empty_excel_file))

        # 空 Excel 应返回提示信息或工作表标题
        # 由于有空工作表，可能返回工作表标题但没有数据
        assert "Sheet" in result or "No text found" in result

    def test_read_corrupted_excel(self, fixtures_dir: Path) -> None:
        """测试读取损坏的 Excel 文件。

        Args:
            fixtures_dir: fixtures 目录路径
        """
        reader = ExcelReader()
        corrupted_file = fixtures_dir / "corrupted.xlsx"
        result = reader.read(str(corrupted_file))

        # 损坏文件应返回错误信息
        assert "Error reading Excel" in result

    def test_read_nonexistent_file(self) -> None:
        """测试读取不存在的文件。"""
        reader = ExcelReader()
        result = reader.read("/nonexistent/path/file.xlsx")

        assert "Error reading Excel" in result
