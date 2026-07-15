# Git 实战教程：从入门到进阶

> 一套完整的 Git 学习教程，包含 7 大模块，配套实战 Demo 与可视化图表。

## 📚 教程目录

| 篇目 | 标题 | 核心内容 |
|------|------|----------|
| 第1篇 | [基础操作篇](blogs/01-基础操作篇.md) | add / commit / status / log / push / clone / .gitignore |
| 第2篇 | [远程协作篇](blogs/02-远程协作篇.md) | GitHub / PR / fetch / pull / 冲突解决 / SSH |
| 第3篇 | [分支与合并篇](blogs/03-分支与合并篇.md) | 分支操作 / merge / rebase / 冲突解决 / 三种合并方式 |
| 第4篇 | [版本控制进阶篇](blogs/04-版本控制进阶篇.md) | reset / revert / restore / stash / tag / hooks / 撤销操作 |
| 第5篇 | [分支策略高级篇](blogs/05-分支策略高级篇.md) | Git Flow / GitHub Flow / Trunk-Based / Monorepo |
| 第6篇 | [底层原理篇](blogs/06-底层原理篇.md) | blob / tree / commit / HEAD / reflog / packfile / LFS |
| 第7篇 | [项目实战篇](blogs/07-项目实战篇.md) | 完整项目搭建 / CI/CD / 团队协作全流程 / 避坑指南 |

## 🚀 快速开始

```bash
# 克隆本仓库
git clone git@github.com:zhangshuo-byte/git-tutorial-demo.git
cd git-tutorial-demo

# 查看各个章节
code blogs/01-基础操作篇.md
```

## 📂 仓库结构

```
git-tutorial-demo/
├── README.md              # 项目说明
├── task-manager/          # 第1-6篇实战 Demo 项目
│   ├── .gitignore
│   ├── README.md
│   ├── task_manager.py
│   └── .git/              # 独立 Git 仓库
├── task-api/              # 第7篇实战 Demo：完整的 API 项目
│   ├── .github/workflows/ # GitHub Actions CI
│   │   └── ci.yml
│   ├── src/               # Python 项目源码
│   │   ├── __init__.py
│   │   ├── app.py         # Flask 应用入口
│   │   ├── models.py      # 数据模型
│   │   └── routes.py      # 路由（含认证）
│   ├── tests/             # 单元测试
│   │   ├── __init__.py
│   │   └── test_app.py
│   ├── .gitignore
│   ├── requirements.txt
│   ├── README.md
│   └── LICENSE
└── blogs/                 # 博客文章 Markdown（7 篇）
    ├── 01-基础操作篇.md
    ├── 02-远程协作篇.md
    ├── 03-分支与合并篇.md
    ├── 04-版本控制进阶篇.md
    ├── 05-分支策略高级篇.md
    ├── 06-底层原理篇.md
    └── 07-项目实战篇.md
```

## 🎯 适用人群

- 🟢 零基础 Git 新手
- 🟡 想系统掌握 Git 的程序员
- 🟠 需要团队协作规范的开发团队
- 🔴 面试前 Git 知识梳理

## ✨ 教程特色

- ✅ 每篇配 **Mermaid 流程图**（GitHub 原生渲染）
- ✅ 大量 **命令行实战演示**（可直接复制运行）
- ✅ 覆盖 **团队协作完整工作流**
- ✅ 包含 **避坑指南与最佳实践**
- ✅ 提供 **可直接运行的示例代码**
- ✅ 从入门到精通，**7 篇递进式学习路径**

## 📊 学习路径

```mermaid
graph LR
    A[第1篇<br/>基础操作] --> B[第2篇<br/>远程协作]
    B --> C[第3篇<br/>分支合并]
    C --> D[第4篇<br/>进阶控制]
    D --> E[第5篇<br/>分支策略]
    E --> F[第6篇<br/>底层原理]
    F --> G[第7篇<br/>项目实战]
    
    style A fill:#e3f2fd
    style G fill:#c8e6c9
```

## 📝 学习建议

1. **按顺序学习** — 每篇都有前置知识依赖
2. **边看边练** — 在本地实际执行每个命令
3. **完成练习** — 每篇末尾的实战演练
4. **使用 Demo** — 配合 Demo 项目亲手操作
5. **做笔记** — 把常用命令整理成自己的速查表

## 🤝 贡献

发现 typo、想补充内容、或有任何建议？欢迎提交 Issue 或 PR！

## 📄 许可

MIT License — 可自由使用、修改和分发。

---

如果这套教程帮到你，请给个 ⭐ Star 支持一下！ 🎉
