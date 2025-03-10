# 数学课程API服务器

这是一个使用FastAPI构建的数学课程数据API服务器。

## 功能特点

- 提供课程章节、小节和子主题的数据
- 支持按章节和小节查询
- 提供搜索功能
- 使用JSON文件作为数据源
- 支持CORS跨域请求

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行服务器

```bash
# 进入server目录
cd server

# 运行服务器
python main.py
```

服务器将在 http://localhost:8000 上运行。

## API文档

启动服务器后，可以访问以下URL查看自动生成的API文档：

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API端点

- `GET /` - 欢迎信息
- `GET /api/chapters` - 获取所有章节
- `GET /api/chapters/{chapter_index}` - 获取特定章节
- `GET /api/chapters/{chapter_index}/sections` - 获取特定章节的所有小节
- `GET /api/chapters/{chapter_index}/sections/{section_index}` - 获取特定小节
- `GET /api/search?q={query}` - 搜索内容

## 数据模型

API使用以下数据模型：

- Chapter (章节)
- Section (小节)
- Concept (概念)
- SubTopic (子主题)

每个模型都有特定的字段，如名称、类型、描述、标签和完成状态。 