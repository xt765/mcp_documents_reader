# PyPI 发布配置说明

## 自动发布流程

本项目配置了自动化的 PyPI 发布流程。当推送版本标签时，会自动执行以下步骤：

1. **验证**：运行测试、代码质量检查
2. **构建**：构建源码和 wheel 分发包
3. **发布**：自动发布到 PyPI
4. **创建 Release**：在 GitHub 创建 Release

## 发布步骤

### 1. 配置 PyPI 信任发布

在 GitHub 仓库中配置受信任的发布：

1. 进入仓库 Settings → Environments
2. 创建新环境，命名为 `pypi`
3. 配置部署保护规则（可选）
4. PyPI 会自动识别 `id-token: write` 权限，无需配置 API Token

### 2. 准备发布

确保项目版本已更新：

```bash
# 更新 pyproject.toml 中的版本号
version = "1.0.4"  # 更新版本号
```

### 3. 创建并提交标签

```bash
# 提交所有更改
git add .
git commit -m "chore: prepare release v1.0.4"

# 创建版本标签（使用语义化版本）
git tag v1.0.4

# 推送代码和标签到远程仓库
git push origin main
git push origin v1.0.4
```

### 4. 自动发布

推送标签后，GitHub Actions 会自动：
- 运行所有测试
- 执行代码质量检查
- 构建分发包
- 发布到 PyPI
- 创建 GitHub Release

### 5. 手动触发发布（可选）

如果需要手动触发发布：

1. 进入 Actions → Release and Publish
2. 点击 "Run workflow"
3. 选择是否发布到 PyPI
4. 点击运行

## 本地测试构建

在发布前，建议本地测试构建：

```bash
# 安装构建工具
uv pip install build

# 构建分发包
python -m build

# 查看生成的文件
ls dist/
# 应该看到：
# - mcp_documents_reader-1.0.4-py3-none-any.whl
# - mcp_documents_reader-1.0.4.tar.gz
```

## 版本管理

遵循语义化版本规范（Semantic Versioning）：

- **MAJOR.MINOR.PATCH** (主版本号。次版本号。修订号)
- 例如：`v1.0.4`
  - `1`: 主版本号（不兼容的 API 变更）
  - `0`: 次版本号（向后兼容的功能新增）
  - `4`: 修订号（向后兼容的问题修复）

## 注意事项

1. **不要重复发布同一版本**：PyPI 不允许上传同名的文件
2. **使用预发布版本**：如需测试，可使用 `v1.0.4a1` (alpha)、`v1.0.4b1` (beta)、`v1.0.4rc1` (release candidate)
3. **检查 PyPI 页面**：发布后访问 https://pypi.org/project/mcp-documents-reader/ 确认

## 故障排除

### 发布失败

1. 检查 GitHub Actions 日志
2. 确认版本号是否正确
3. 确认是否已存在相同版本

### 本地测试

```bash
# 使用 twine 检查分发包
uv pip install twine
twine check dist/*

# 测试上传到 TestPyPI
twine upload --repository testpypi dist/*
```

## 相关配置

- CI 工作流：`.github/workflows/ci.yml`
- 发布工作流：`.github/workflows/release.yml`
- 安全扫描：`.github/workflows/security.yml`
- 项目配置：`pyproject.toml`
