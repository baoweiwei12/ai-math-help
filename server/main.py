from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Union, Dict, Any
import json
import os
from pathlib import Path
from ai_agent import MathAgent
from openai import OpenAI

app = FastAPI(
    title="数学课程API",
    description="提供数学课程数据的API接口",
    version="1.0.0"
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应该限制为前端域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 定义数据模型
class SubTopic(BaseModel):
    name: str
    type: Literal["subtopic"]
    tags: Optional[List[str]] = None
    description: Optional[str] = None
    completed: bool = False

class Section(BaseModel):
    name: str
    type: Literal["section"]
    tags: Optional[List[str]] = None
    description: Optional[str] = None
    completed: bool = False
    children: Optional[List[SubTopic]] = None

class Concept(BaseModel):
    name: str
    type: Literal["concept"]
    description: Optional[str] = None
    completed: bool = False

class Chapter(BaseModel):
    name: str
    type: Literal["chapter"]
    completed: bool = False
    children: List[Union[Section, Concept]]

# 新增请求模型
class NodeStatusUpdate(BaseModel):
    path: str
    completed: bool

class ChatMessage(BaseModel):
    path: str
    message: str
    mode: str  # "learn" 或 "quiz"

# 数据加载函数
def load_course_data() -> List[Dict[str, Any]]:
    try:
        data_file =  "data.json"
        with open(data_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"加载数据失败: {e}")
        return []

# 数据保存函数
def save_course_data(data: List[Dict[str, Any]]) -> bool:
    try:
        data_file ="data.json"
        with open(data_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"保存数据失败: {e}")
        return False

# 根据路径查找节点
def find_node_by_path(data: List[Dict[str, Any]], path: str) -> Optional[Dict[str, Any]]:
    if not path:
        return None
    
    path_parts = path.split(".")
    current = data
    
    # 第一级是数组，需要特殊处理
    if len(path_parts) > 0:
        chapter_idx = int(path_parts[0])
        if 0 <= chapter_idx < len(current):
            current = current[chapter_idx]
        else:
            return None
    
    # 从第二级开始遍历
    for i in range(1, len(path_parts)):
        if not current or "children" not in current:
            return None
        
        section_idx = int(path_parts[i])
        if 0 <= section_idx < len(current["children"]): # type: ignore
            current = current["children"][section_idx] # type: ignore
        else:
            return None
    
    return current # type: ignore

# 更新节点状态
def update_node_status(data: List[Dict[str, Any]], path: str, completed: bool) -> Optional[Dict[str, Any]]:
    if not path:
        return None
    
    path_parts = path.split(".")
    
    # 如果是顶级章节
    if len(path_parts) == 1:
        chapter_idx = int(path_parts[0])
        if 0 <= chapter_idx < len(data):
            data[chapter_idx]["completed"] = completed
            return data[chapter_idx]
        return None
    
    # 构建引用路径
    refs = [data]
    current = data
    
    # 第一级是数组，需要特殊处理
    chapter_idx = int(path_parts[0])
    if 0 <= chapter_idx < len(current):
        current = current[chapter_idx]
        refs.append(current) # type: ignore
    else:
        return None
    
    # 从第二级开始遍历
    for i in range(1, len(path_parts)):
        if not current or "children" not in current:
            return None
        
        section_idx = int(path_parts[i])
        if 0 <= section_idx < len(current["children"]):
            current = current["children"][section_idx]
            refs.append(current)
        else:
            return None
    
    # 更新状态
    current["completed"] = completed
    
    # 保存数据
    if save_course_data(data):
        return current
    else:
        raise HTTPException(status_code=500, detail="保存数据失败")

# API路由
@app.get("/")
def root():
    return {"message": "欢迎使用数学课程API"}

@app.get("/api/chapters", response_model=List[Chapter])
def get_chapters():
    data = load_course_data()
    return data

@app.get("/api/chapters/{chapter_index}", response_model=Chapter)
def get_chapter(chapter_index: int):
    data = load_course_data()
    if 0 <= chapter_index < len(data):
        return data[chapter_index]
    raise HTTPException(status_code=404, detail="章节不存在")

@app.get("/api/chapters/{chapter_index}/sections", response_model=List[Union[Section, Concept]])
def get_sections(chapter_index: int):
    data = load_course_data()
    if 0 <= chapter_index < len(data):
        return data[chapter_index].get("children", [])
    raise HTTPException(status_code=404, detail="章节不存在")

@app.get("/api/chapters/{chapter_index}/sections/{section_index}", response_model=Union[Section, Concept])
def get_section(chapter_index: int, section_index: int):
    data = load_course_data()
    if 0 <= chapter_index < len(data):
        children = data[chapter_index].get("children", [])
        if 0 <= section_index < len(children):
            return children[section_index]
    raise HTTPException(status_code=404, detail="章节或小节不存在")

@app.get("/api/node")
def get_node_by_path(path: str):
    data = load_course_data()
    node = find_node_by_path(data, path)
    if node:
        return node
    raise HTTPException(status_code=404, detail="节点不存在")

@app.patch("/api/node/status")
def update_node_completion_status(update: NodeStatusUpdate):
    data = load_course_data()
    updated_node = update_node_status(data, update.path, update.completed)
    if updated_node:
        return updated_node
    raise HTTPException(status_code=404, detail="节点不存在")

@app.get("/api/search")
def search_content(q: str):
    data = load_course_data()
    results = []
    
    for chapter_idx, chapter in enumerate(data):
        # 搜索章节名称
        if q.lower() in chapter["name"].lower():
            results.append({
                "type": "chapter",
                "chapter_index": chapter_idx,
                "item": chapter
            })
        
        # 搜索小节和概念
        for section_idx, section in enumerate(chapter.get("children", [])):
            if q.lower() in section["name"].lower() or q.lower() in section.get("description", "").lower():
                results.append({
                    "type": section["type"],
                    "chapter_index": chapter_idx,
                    "section_index": section_idx,
                    "item": section
                })
            
            # 搜索子主题
            if section["type"] == "section":
                for subtopic_idx, subtopic in enumerate(section.get("children", [])):
                    if q.lower() in subtopic["name"].lower() or q.lower() in subtopic.get("description", "").lower():
                        results.append({
                            "type": "subtopic",
                            "chapter_index": chapter_idx,
                            "section_index": section_idx,
                            "subtopic_index": subtopic_idx,
                            "item": subtopic
                        })
    
    return results

@app.get("/api/path-names")
def get_path_names(path: str):
    data = load_course_data()
    path_parts = path.split(".")
    result = []
    
    # 处理每一级路径
    current_path = ""
    current = data
    
    for i, part in enumerate(path_parts):
        idx = int(part)
        
        # 构建当前路径
        if i == 0:
            current_path = part
        else:
            current_path = f"{current_path}.{part}"
        
        # 获取当前节点
        if i == 0:
            # 第一级是章节
            if 0 <= idx < len(current):
                node = current[idx] # type: ignore
                result.append({
                    "name": node["name"],
                    "path": current_path
                })
                current = node
            else:
                raise HTTPException(status_code=404, detail=f"路径 {current_path} 不存在")
        else:
            # 其他级别
            if "children" in current and 0 <= idx < len(current["children"]): # type: ignore
                node = current["children"][idx] # type: ignore
                result.append({
                    "name": node["name"],
                    "path": current_path
                })
                current = node
            else:
                raise HTTPException(status_code=404, detail=f"路径 {current_path} 不存在")
    
    return result

# 获取聊天历史记录
@app.get("/api/chat/history")
def get_chat_history(path: str, mode: str):
    """
    获取特定节点和模式的聊天历史记录
    
    Args:
        path: 节点路径
        mode: 聊天模式，"learn" 或 "quiz"
    """
    # 创建 AI 代理
    ai = OpenAI(api_key="sk-6tg5gVdYiWQ7SaoBB2B73bAe339a405fB1C575AdE50042Fa",base_url="https://pro.aiskt.com/v1")
    agent = MathAgent(ai)
    
    # 获取聊天历史
    history = agent.get_chat_history(path, mode)
    
    # 转换为前端友好的格式
    messages = []
    for msg in history:
        if msg["role"] in ["user", "assistant"]:
            messages.append({
                "role": msg["role"],
                "content": msg["content"],
                "time": ""  # 历史记录中没有时间，前端会处理
            })
    
    return messages

# 统一的聊天API
@app.post("/api/chat")
def send_chat_message(message: ChatMessage):
    """
    处理聊天消息，支持学习和问答模式
    """
    # 获取节点数据
    data = load_course_data()
    node = find_node_by_path(data, message.path)
    if not node:
        raise HTTPException(status_code=404, detail="节点不存在")
    
    # 创建 AI 代理
    ai = OpenAI(api_key="sk-6tg5gVdYiWQ7SaoBB2B73bAe339a405fB1C575AdE50042Fa",base_url="https://pro.aiskt.com/v1")
    agent = MathAgent(ai)
    
    # 准备节点数据
    node_data = str(node)
    
    # 调用 AI 代理进行聊天
    response = agent.chat(message.message, node_data, message.path, mode=message.mode)
    
    return {
        "content": response
    }

# 运行服务器
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
