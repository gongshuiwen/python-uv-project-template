#!/usr/bin/env python3
"""
项目设置脚本
用于初始化开发环境和配置
"""

import os
import subprocess
import sys
from pathlib import Path


def run_command(command: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    """运行命令并返回结果"""
    print(f"执行命令: {command}")
    result = subprocess.run(
        command, shell=True, capture_output=True, text=True, check=check
    )
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    return result


def check_uv_installed() -> bool:
    """检查 uv 是否已安装"""
    try:
        result = run_command("uv --version", check=False)
        return result.returncode == 0
    except FileNotFoundError:
        return False


def install_uv():
    """安装 uv 包管理器"""
    print("正在安装 uv 包管理器...")
    if os.name == "nt":  # Windows
        run_command('powershell -c "irm https://astral.sh/uv/install.ps1 | iex"')
    else:  # Unix-like systems
        run_command("curl -LsSf https://astral.sh/uv/install.sh | sh")


def setup_project():
    """设置项目环境"""
    print("正在设置项目环境...")

    # 检查并安装 uv
    if not check_uv_installed():
        install_uv()

    # 安装项目依赖
    print("正在安装项目依赖...")
    run_command("uv sync --all-extras --dev")

    # 安装 pre-commit hooks
    print("正在安装 pre-commit hooks...")
    run_command("uv run pre-commit install")
    run_command("uv run pre-commit install --hook-type commit-msg")

    # 创建 .env 文件（如果不存在）
    env_file = Path(".env")
    env_sample = Path(".env.sample")
    if not env_file.exists() and env_sample.exists():
        print("正在创建 .env 文件...")
        env_file.write_text(env_sample.read_text())

    print("✅ 项目环境设置完成！")
    print("\n下一步:")
    print("1. 编辑 .env 文件配置环境变量")
    print("2. 运行 'make test' 验证环境")
    print("3. 运行 'make run' 启动项目")


if __name__ == "__main__":
    setup_project()
