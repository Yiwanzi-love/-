 # 个人知识库
 
 互联网广告行业运营方法论的沉淀与分享。
 
 ## 项目结构
 
 ```
 knowledge-base/
 ├── docs/                    # 知识库内容（Markdown 源文件）
 │   ├── index.md            # 首页
 │   ├── tags.md             # 标签索引
 │   ├── 创意生产方法论/     # 模块一
 │   ├── 创意策略-平台素材生态方向/ # 模块二
 │   └── 个人工具库.md        # 模块三
 ├── mkdocs.yml              # 站点配置
 ├── .gitignore
 └── README.md
 ```
 
 ## 工作流
 
 1. **编写**：用 Obsidian 打开 `docs/` 目录，编辑 Markdown 文件
 2. **预览**：运行 `mkdocs serve`，在 `http://127.0.0.1:8000` 实时查看
 3. **构建**：运行 `mkdocs build`，生成静态文件到 `site/` 目录
 4. **发布**：推送到 GitHub，Cloudflare Pages 自动部署
 
 ## 前置依赖
 
 - Python 3.x
 - pip install mkdocs-material
 
 ## 本地预览
 
 ```bash
 mkdocs serve
 ```
 
 打开浏览器访问 `http://127.0.0.1:8000`
 
 ## 构建静态站点
 
 ```bash
 mkdocs build
 ```
 
 构建产物在 `site/` 目录下，可直接部署到任意静态托管服务。
 
