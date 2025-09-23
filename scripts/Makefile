.PHONY: help install dev test lint format type-check security clean build docker-build docker-run pre-commit

# 默认目标
help: ## 显示帮助信息
	@echo "可用的命令:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# 环境设置
install: ## 安装项目依赖
	uv sync

dev: ## 安装开发依赖
	uv sync --all-extras --dev

# 代码质量
lint: ## 运行代码检查
	uv run ruff check .

lint-fix: ## 运行代码检查并自动修复
	uv run ruff check --fix .

format: ## 格式化代码
	uv run ruff format .

format-check: ## 检查代码格式
	uv run ruff format --check .

type-check: ## 运行类型检查
	npx pyright

security: ## 运行安全检查
	uv run bandit -r src/

# 测试
test: ## 运行测试
	uv run pytest

test-cov: ## 运行测试并生成覆盖率报告
	uv run pytest --cov=src --cov-report=html --cov-report=term

test-watch: ## 监视文件变化并自动运行测试
	uv run pytest-watch

# 代码质量检查套件
check: lint format-check type-check security test ## 运行所有代码质量检查

# 清理
clean: ## 清理生成的文件
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete

# 构建
build: ## 构建项目
	uv build

# Docker
docker-build: ## 构建 Docker 镜像
	docker build -t python-uv-project-template .

docker-run: ## 运行 Docker 容器
	docker run --rm python-uv-project-template

# Pre-commit
pre-commit-install: ## 安装 pre-commit hooks
	uv run pre-commit install
	uv run pre-commit install --hook-type commit-msg

pre-commit-run: ## 运行 pre-commit 检查
	uv run pre-commit run --all-files

pre-commit-update: ## 更新 pre-commit hooks
	uv run pre-commit autoupdate

# 运行项目
run: ## 运行主程序
	uv run python src/main.py

# 开发服务器 (如果是 web 应用)
# serve: ## 启动开发服务器
# 	uv run python -m uvicorn src.main:app --reload

# 数据库相关 (如果需要)
# db-init: ## 初始化数据库
# 	uv run python -m src.database.init

# db-migrate: ## 运行数据库迁移
# 	uv run alembic upgrade head

# 文档生成 (如果需要)
# docs: ## 生成文档
# 	uv run mkdocs build

# docs-serve: ## 启动文档服务器
# 	uv run mkdocs serve
