# Task API

基于 Flask 的任务管理 REST API，作为 Git 教程的演示项目。

## 快速开始

```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 运行
python src/app.py

# 测试
pytest tests/ -v
```

## API 接口

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/tasks` | 获取所有任务 |
| POST | `/api/tasks` | 创建任务 |
| GET | `/api/tasks/<id>` | 获取单个任务 |
| PUT | `/api/tasks/<id>` | 更新任务 |
| DELETE | `/api/tasks/<id>` | 删除任务 |

## 使用示例

```bash
# 创建任务
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "写博客", "description": "完成 Git 教程"}'

# 获取任务列表
curl http://localhost:5000/api/tasks
```

## 开发说明

本项目遵循 Angular 提交规范：

- `feat:` 新功能
- `fix:` 修复 bug
- `docs:` 文档变更
- `style:` 代码格式调整
- `refactor:` 重构
- `test:` 测试相关
- `chore:` 构建过程或辅助工具变动
