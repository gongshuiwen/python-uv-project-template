# 使用官方 Python 3.13 slim 镜像作为基础镜像
FROM python:3.13-slim

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV PYTHONPATH=/app/src \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_CACHE_DIR=/app/.uv-cache

# 修改包源
ARG DEB_SOURCE=mirrors.tencent.com
RUN sed -i "s/deb.debian.org/${DEB_SOURCE}/g" /etc/apt/sources.list.d/debian.sources

# 安装必要的运行时依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# 安装 uv 包管理器
ARG PYPI_SOURCE=https://mirrors.tencent.com/pypi/simple
RUN pip install uv -i ${PYPI_SOURCE}

# 复制项目配置文件
COPY pyproject.toml uv.lock ./

# 安装 Python 依赖
RUN uv sync --frozen --no-dev

# 复制源代码
COPY src/ ./

# 创建非 root 用户和组，并设置目录权限
RUN groupadd --system --gid 1001 app && \
    useradd --system --no-log-init \
    --uid 1001 --gid app \
    --create-home --home-dir /app \
    --shell /bin/bash app && \
    mkdir -p /app/.uv-cache && \
    chown -R app:app /app
USER app

# 启动命令
CMD ["/app/.venv/bin/python", "main.py"]
