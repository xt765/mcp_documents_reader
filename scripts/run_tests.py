#!/usr/bin/env python3
"""
测试运行脚本

使用方法:
    python scripts/run_tests.py              # 运行所有测试
    python scripts/run_tests.py --verbose    # 详细输出
    python scripts/run_tests.py --no-cov     # 不生成覆盖率报告
    python scripts/run_tests.py --html       # 生成 HTML 覆盖率报告
"""
import subprocess
import sys
import argparse
from pathlib import Path


def run_command(cmd: list[str], check: bool = True) -> int:
    """运行命令并返回退出码"""
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    if check and result.returncode != 0:
        print(f"❌ Command failed: {' '.join(cmd)}")
        sys.exit(result.returncode)
    return result.returncode


def main():
    parser = argparse.ArgumentParser(description="运行测试套件")
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="显示详细输出"
    )
    parser.add_argument(
        "--no-cov",
        action="store_true",
        help="不生成覆盖率报告"
    )
    parser.add_argument(
        "--html",
        action="store_true",
        help="生成 HTML 覆盖率报告"
    )
    parser.add_argument(
        "-k",
        type=str,
        help="只运行匹配特定模式的测试"
    )

    args = parser.parse_args()

    # 构建 pytest 命令
    cmd = [sys.executable, "-m", "pytest", "tests/"]

    if args.verbose:
        cmd.append("-v")

    if not args.no_cov:
        cmd.extend([
            "--cov=mcp_documents_reader",
            "--cov-report=term-missing",
        ])

        if args.html:
            cmd.append("--cov-report=html")

    if args.k:
        cmd.extend(["-k", args.k])

    # 运行测试
    print("=" * 60)
    print("🧪 运行测试套件")
    print("=" * 60)
    run_command(cmd)

    print("\n" + "=" * 60)
    print("✅ 测试完成!")
    print("=" * 60)

    if not args.no_cov:
        print("\n📊 覆盖率报告已生成:")
        print("   - Terminal: 已显示")
        if args.html:
            print("   - HTML: htmlcov/index.html")


if __name__ == "__main__":
    main()
