# Python UV Project Template

一个基于现代 Python 开发工具链的项目模板，使用 `uv` 包管理器和最佳实践配置。

## 🚀 特性

- **现代包管理**: 使用 [uv](https://github.com/astral-sh/uv) 进行快速依赖管理
- **Python 3.13**: 支持最新的 Python 版本
- **完整测试套件**: 集成 pytest、pytest-cov、pytest-mock
- **代码质量工具**: ruff (linting + formatting) + basedpyright (类型检查)
- **容器化支持**: 包含优化的 Dockerfile 配置
- **开发工具**: EditorConfig、pre-commit hooks、CI/CD 配置

## 🛠️ 快速开始

### 1. 克隆项目

```bash
git clone <your-repo-url>
cd python-uv-project-template
```

### 2. 安装依赖

```bash
# 安装 uv (如果尚未安装)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 创建虚拟环境并安装依赖
uv sync
```

### 3. 运行项目

```bash
uv run python src/main.py
```

## 🧪 测试

```bash
# 运行所有测试
uv run pytest

# 运行测试并生成覆盖率报告
uv run pytest --cov=src --cov-report=html

# 查看覆盖率报告
open htmlcov/index.html  # macOS
start htmlcov/index.html # Windows
```

## 🔧 开发工具

### 代码检查和格式化

```bash
# 运行 ruff 检查
uv run ruff check .

# 自动修复可修复的问题
uv run ruff check --fix .

# 格式化代码
uv run ruff format .
```

### 类型检查

```bash
# 使用 basepyright 进行类型检查
uv run basepyright
```

## 🐳 Docker 支持

### 构建镜像

```bash
docker build -t python-uv-project-template .
```

### 运行容器

```bash
docker run --rm python-uv-project-template
```

## ⚙️ 配置说明

### pyproject.toml

项目使用 `pyproject.toml` 进行配置管理，包含：

- **项目元数据**: 名称、版本、描述等
- **依赖管理**: 生产依赖和开发依赖分组
- **工具配置**: pytest、ruff、coverage 等工具的配置

### 依赖分组

- `dev`: 开发依赖组，包含 lint, type 和 test 组
- `lint`: 代码检查工具 (ruff)
- `type`: 类型检查工具 (basedpyright)
- `test`: 测试相关工具 (pytest, pytest-cov, pytest-mock)

## 🔄 开发工作流

1. **创建功能分支**: `git checkout -b feature/your-feature`
2. **编写代码**: 在 `src/` 目录下编写代码
3. **编写测试**: 在 `test/` 目录下编写对应测试
4. **运行测试**: `uv run pytest`
5. **代码检查**: `uv run ruff check .`
6. **类型检查**: `npx pyright`
7. **提交代码**: `git commit -m "feat: your feature"`
8. **推送分支**: `git push origin feature/your-feature`

## 📝 环境变量

复制 `.env.sample` 为 `.env` 并根据需要修改配置：

```bash
cp .env.sample .env
```

## 🤝 贡献指南

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🔗 相关链接

- [uv 文档](https://docs.astral.sh/uv/)
- [ruff 文档](https://docs.astral.sh/ruff/)
- [basedpyright 文档](https://microsoft.github.io/pyright/)
- [pytest 文档](https://docs.pytest.org/)
- [coverage 文档](https://coverage.readthedocs.io)
