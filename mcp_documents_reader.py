import os
from abc import ABC, abstractmethod
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import override

from docx import Document as DocxDocument
from mcp.server.fastmcp import FastMCP
from openpyxl import load_workbook
from PyPDF2 import PdfReader as PyPdfReader

# Directory where documents are stored
DOCUMENT_DIRECTORY = os.getenv("DOCUMENT_DIRECTORY", "./documents")


@dataclass
class AppContext:
    """Application context for lifecycle management."""

    document_directory: str


# Initialize the MCP server (lifespan added below)
mcp = FastMCP("Document Reader")


@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    """Manage application lifecycle with type-safe context"""
    try:
        # Ensure document directory exists
        os.makedirs(DOCUMENT_DIRECTORY, exist_ok=True)
        yield AppContext(document_directory=DOCUMENT_DIRECTORY)
    finally:
        # Cleanup (if needed)
        pass


# Assign lifespan to server
mcp.lifespan = app_lifespan  # type: ignore[reportAttributeAccessIssue]


# ------------------------- Document Reader Architecture -------------------------


class DocumentReader(ABC):
    """Abstract base class for document readers"""

    @abstractmethod
    def read(self, file_path: str) -> str:
        """Read and extract text from a document"""
        pass


class DocxReader(DocumentReader):
    """DOCX document reader implementation"""

    @override
    def read(self, file_path: str) -> str:
        """Read and extract text from DOCX file"""
        try:
            doc = DocxDocument(file_path)
            text = []

            # Extract paragraph text
            for paragraph in doc.paragraphs:
                if paragraph.text:
                    text.append(paragraph.text)

            # Extract table content
            for table in doc.tables:
                for row in table.rows:
                    row_text = []
                    for cell in row.cells:
                        cell_text = " ".join([p.text for p in cell.paragraphs]).strip()
                        if cell_text:
                            row_text.append(cell_text)
                    if row_text:
                        text.append("\t".join(row_text))

            extracted_text = "\n".join(text)
            return extracted_text if extracted_text else "No text found in the DOCX."
        except Exception as e:
            return f"Error reading DOCX: {str(e)}"


class PdfReader(DocumentReader):
    """PDF document reader implementation"""

    @override
    def read(self, file_path: str) -> str:
        """Read and extract text from PDF file"""
        try:
            with open(file_path, "rb") as file:
                pdf_reader = PyPdfReader(file)
                text = []

                # Extract text from each page
                for page in pdf_reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text.append(page_text.strip())

                extracted_text = "\n\n".join(text)
                return extracted_text if extracted_text else "No text found in the PDF."
        except Exception as e:
            return f"Error reading PDF: {str(e)}"


class TxtReader(DocumentReader):
    """TXT document reader implementation"""

    @override
    def read(self, file_path: str) -> str:
        """Read and extract text from TXT file with encoding handling"""
        # Supported encodings in priority order
        encodings = ["utf-8", "gbk", "gb2312", "ansi", "latin-1"]

        for encoding in encodings:
            try:
                with open(file_path, "r", encoding=encoding) as f:
                    text = f.read()
                return text if text else "No text found in the TXT file."
            except UnicodeDecodeError:
                continue
            except Exception as e:
                return f"Error reading TXT: {str(e)}"

        return "Error reading TXT: Could not decode file with any supported encoding."


class ExcelReader(DocumentReader):
    """Excel document reader implementation"""

    @override
    def read(self, file_path: str) -> str:
        """Read and extract text from Excel file"""
        try:
            wb = load_workbook(file_path, read_only=True)
            text = []

            # Extract text from all sheets
            for sheet_name in wb.sheetnames:
                sheet = wb[sheet_name]
                text.append(f"=== Sheet: {sheet_name} ===")

                # Extract cell content
                for row in sheet.iter_rows(values_only=True):
                    row_text = [str(cell) if cell is not None else "" for cell in row]
                    if any(row_text):  # Only add non-empty rows
                        text.append("\t".join(row_text))

                text.append("")  # Add blank line between sheets

            extracted_text = "\n".join(text)
            wb.close()
            return (
                extracted_text if extracted_text else "No text found in the Excel file."
            )
        except Exception as e:
            return f"Error reading Excel: {str(e)}"


class DocumentReaderFactory:
    """Factory for creating document readers based on file extension"""

    # Mapping of file extensions to reader classes
    _readers: dict[str, type[DocumentReader]] = {
        ".txt": TxtReader,
        ".docx": DocxReader,
        ".pdf": PdfReader,
        ".xlsx": ExcelReader,
        ".xls": ExcelReader,
    }

    @classmethod
    def get_reader(cls, file_path: str) -> DocumentReader:
        """Get appropriate reader for the given file"""
        _, ext = os.path.splitext(file_path.lower())
        if ext not in cls._readers:
            raise ValueError(f"Unsupported document type: {ext}")
        return cls._readers[ext]()

    @classmethod
    def is_supported(cls, file_path: str) -> bool:
        """Check if the file type is supported"""
        _, ext = os.path.splitext(file_path.lower())
        return ext in cls._readers


# ------------------------- Tool Functions -------------------------


def _get_document_path(ctx: object, filename: str) -> str:
    """Get full document path from context or environment"""
    try:
        doc_dir = getattr(ctx, "document_directory", DOCUMENT_DIRECTORY)
    except Exception:
        doc_dir = DOCUMENT_DIRECTORY
    return os.path.join(doc_dir, filename)


@mcp.tool()
def read_document(ctx: object, filename: str) -> str:
    """
    Reads and extracts text from a specified document file.
    Supports multiple document types: TXT, DOCX, PDF, Excel (XLSX, XLS).

    :param ctx: FastMCP context
    :param filename: Name of the document file to read
    :return: Extracted text from the document
    """
    doc_path = _get_document_path(ctx, filename)

    if not os.path.exists(doc_path):
        return f"Error: File '{filename}' not found at {doc_path}."

    if not DocumentReaderFactory.is_supported(doc_path):
        return f"Error: Unsupported document type for file '{filename}'."

    try:
        reader = DocumentReaderFactory.get_reader(doc_path)
        return reader.read(doc_path)
    except Exception as e:
        return f"Error reading document: {str(e)}"


# Run the MCP server
def main():
    mcp.run()


if __name__ == "__main__":
    main()
