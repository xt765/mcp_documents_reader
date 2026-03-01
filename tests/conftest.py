"""pytest 配置文件"""
import pytest
import sys
import os

# 添加项目根目录到 Python 路径
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)


@pytest.fixture
def sample_txt_content():
    """示例 TXT 内容"""
    return "这是示例文本内容\n第二行内容\n第三行内容"


@pytest.fixture
def sample_excel_data():
    """示例 Excel 数据"""
    return {
        "Sheet1": [
            ["姓名", "年龄", "城市"],
            ["张三", "25", "北京"],
            ["李四", "30", "上海"],
            ["王五", "28", "广州"],
        ]
    }


@pytest.fixture
def sample_docx_paragraphs():
    """示例 DOCX 段落"""
    return ["第一段内容", "第二段内容", "第三段内容"]
