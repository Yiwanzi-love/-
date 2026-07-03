<div align="center">
  <h1>个人知识库</h1>
  <p>互联网广告行业运营方法论的沉淀与分享</p>
</div>

## 项目结构

├── docs/              # Markdown 内容源（Obsidian Vault）
├── assets/            # 静态资源（CSS / SVG 简笔画）
├── pages/             # 构建产物（自动生成）
├── index.html         # 首页
├── build.py           # 内容构建脚本
├── update.py          # 首页和资源部署脚本
└── .github/workflows/ # GitHub Actions 自动部署

## 本地开发

### 前置依赖
pip install markdown pyyaml pymdown-extensions

### 预览
python -m http.server 8000
浏览器打开 http://127.0.0.1:8000

### 更新内容
在 docs/ 下编辑 Markdown 文件后：
python build.py && python update.py
然后刷新浏览器。

## 部署到 GitHub Pages

1. 在 GitHub 创建一个公开仓库
2. 在本地运行以下命令推送代码：
   git remote add origin https://github.com/你的用户名/你的仓库名.git
   git branch -M main
   git push -u origin main
3. 在 GitHub 仓库页面进入 Settings > Pages，Source 选择 "GitHub Actions"
4. 以后每次推送到 main 分支，GitHub Actions 会自动构建和部署
5. 部署完成后，你的知识库就会在 https://你的用户名.github.io/你的仓库名 上线

部署好之后，你在 Obsidian 里写新内容 → 推送到 GitHub → 网站自动更新。全程无需手动操作。