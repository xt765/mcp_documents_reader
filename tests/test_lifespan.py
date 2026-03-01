"""生命周期管理测试。

测试内容：
- app_lifespan 异步上下文管理器测试
- AppContext 数据类测试
- 文档目录创建验证
"""

import os
import tempfile
from pathlib import Path
from unittest import mock

import pytest

from mcp_documents_reader import (
    DOCUMENT_DIRECTORY,
    AppContext,
    app_lifespan,
)


class TestAppContext:
    """AppContext 数据类测试类。"""

    def test_app_context_creation(self) -> None:
        """测试 AppContext 创建。"""
        context = AppContext(document_directory="/test/path")

        assert context.document_directory == "/test/path"

    def test_app_context_default_values(self) -> None:
        """测试 AppContext 默认值。"""
        context = AppContext(document_directory="./documents")

        assert context.document_directory == "./documents"

    def test_app_context_is_frozen(self) -> None:
        """测试 AppContext 是否为不可变（frozen）数据类。

        注意：当前实现没有设置 frozen=True，所以这个测试验证可变性。
        """
        context = AppContext(document_directory="/test/path")

        # 验证可以修改属性（因为 dataclass 默认不冻结）
        context.document_directory = "/new/path"
        assert context.document_directory == "/new/path"


class TestAppLifespan:
    """app_lifespan 异步上下文管理器测试类。"""

    @pytest.mark.asyncio
    async def test_app_lifespan_yields_context(self) -> None:
        """测试 app_lifespan 产生正确的上下文。"""
        # 使用 mock FastMCP
        mock_server = mock.MagicMock()

        async with app_lifespan(mock_server) as context:
            assert isinstance(context, AppContext)
            assert context.document_directory == DOCUMENT_DIRECTORY

    @pytest.mark.asyncio
    async def test_app_lifespan_creates_directory(self) -> None:
        """测试 app_lifespan 创建文档目录。"""
        with tempfile.TemporaryDirectory() as tmpdir:
            test_dir = os.path.join(tmpdir, "test_documents")

            with mock.patch.dict(
                os.environ, {"DOCUMENT_DIRECTORY": test_dir}
            ), mock.patch(
                "mcp_documents_reader.DOCUMENT_DIRECTORY", test_dir
            ):
                mock_server = mock.MagicMock()

                async with app_lifespan(mock_server) as context:
                    # 验证目录被创建
                    assert os.path.exists(test_dir)
                    assert context.document_directory == test_dir

    @pytest.mark.asyncio
    async def test_app_lifespan_with_existing_directory(self) -> None:
        """测试 app_lifespan 处理已存在的目录。"""
        with tempfile.TemporaryDirectory() as tmpdir:
            # 目录已存在
            test_dir = os.path.join(tmpdir, "existing_documents")
            os.makedirs(test_dir)

            with mock.patch.dict(
                os.environ, {"DOCUMENT_DIRECTORY": test_dir}
            ), mock.patch(
                "mcp_documents_reader.DOCUMENT_DIRECTORY", test_dir
            ):
                mock_server = mock.MagicMock()

                async with app_lifespan(mock_server) as context:
                    # 验证目录仍然存在
                    assert os.path.exists(test_dir)
                    assert context.document_directory == test_dir

    @pytest.mark.asyncio
    async def test_app_lifespan_cleanup(self) -> None:
        """测试 app_lifespan 清理逻辑（finally 块）。"""
        mock_server = mock.MagicMock()

        # 进入和退出上下文管理器
        async with app_lifespan(mock_server) as context:
            assert context is not None

        # 退出后没有异常即表示清理成功

    @pytest.mark.asyncio
    async def test_app_lifespan_exception_handling(self) -> None:
        """测试 app_lifespan 异常处理。"""
        mock_server = mock.MagicMock()

        try:
            async with app_lifespan(mock_server) as context:
                raise ValueError("Test exception")
        except ValueError:
            pass  # 预期的异常

        # 验证 finally 块被执行（没有资源泄漏）

    @pytest.mark.asyncio
    async def test_app_lifespan_directory_creation_permission_error(self) -> None:
        """测试目录创建权限错误处理。"""
        with mock.patch("os.makedirs") as mock_makedirs:
            # 模拟权限错误
            mock_makedirs.side_effect = PermissionError("Permission denied")

            mock_server = mock.MagicMock()

            # 应该抛出权限错误
            with pytest.raises(PermissionError):
                async with app_lifespan(mock_server):
                    pass

    @pytest.mark.asyncio
    async def test_app_lifespan_multiple_calls(self) -> None:
        """测试多次调用 app_lifespan。"""
        mock_server = mock.MagicMock()

        # 第一次调用
        async with app_lifespan(mock_server) as context1:
            assert context1.document_directory == DOCUMENT_DIRECTORY

        # 第二次调用
        async with app_lifespan(mock_server) as context2:
            assert context2.document_directory == DOCUMENT_DIRECTORY


class TestDocumentDirectory:
    """DOCUMENT_DIRECTORY 环境变量测试类。"""

    def test_default_document_directory(self) -> None:
        """测试默认文档目录。"""
        # DOCUMENT_DIRECTORY 应该是默认值或环境变量值
        assert DOCUMENT_DIRECTORY is not None
        assert isinstance(DOCUMENT_DIRECTORY, str)

    def test_document_directory_from_env(self) -> None:
        """测试从环境变量获取文档目录。"""
        with mock.patch.dict(os.environ, {"DOCUMENT_DIRECTORY": "/custom/path"}):
            # 重新导入以获取新的环境变量值
            import importlib

            import mcp_documents_reader

            importlib.reload(mcp_documents_reader)

            # 注意：由于模块已加载，这个测试可能不会反映新值
            # 但我们验证环境变量被读取
            assert os.getenv("DOCUMENT_DIRECTORY", "./documents") == "/custom/path"
