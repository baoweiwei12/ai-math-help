import json
from openai import OpenAI
from typing import Generator, Iterable, List, Dict, Any, Literal, Union
from openai import OpenAI
from pydantic import BaseModel
from openai.types.chat import (
    ChatCompletionMessageParam,
    ChatCompletionUserMessageParam,
    ChatCompletionContentPartParam,
    ChatCompletionContentPartTextParam,
    ChatCompletionContentPartImageParam,
    ChatCompletionAssistantMessageParam,
    ChatCompletionSystemMessageParam,
)
import tiktoken
import os
from pathlib import Path
import dotenv

class MathAgent:
    def __init__(self, ai: OpenAI, messages_base_path: str = "messages"):
        self.ai = ai
        self.messages_base_path = messages_base_path
        self.current_messages_path = ""
        self.messages = []
        
    def _get_messages_path(self, node_path: str, mode: str = "learn") -> str:
        """
        根据节点路径和模式生成消息文件路径
        
        Args:
            node_path: 节点路径，如 "0.0.1"
            mode: 模式，如 "learn" 或 "quiz"
            
        Returns:
            消息文件的完整路径
        """
        # 确保基础目录存在
        base_dir = Path(self.messages_base_path) / mode
        base_dir.mkdir(parents=True, exist_ok=True)
        
        # 构建消息文件路径
        file_path = base_dir / f"{node_path}.json"
        return str(file_path)
    
    def _load_messages(self, node_path: str, mode: str = "learn") -> List[Dict[str, Any]]:
        """
        加载指定节点的消息历史
        
        Args:
            node_path: 节点路径
            mode: 模式
            
        Returns:
            消息历史列表
        """
        self.current_messages_path = self._get_messages_path(node_path, mode)
        
        try:
            with open(self.current_messages_path, "r", encoding="utf-8") as f:
                self.messages = json.load(f)
                return self.messages
        except (FileNotFoundError, json.JSONDecodeError):
            # 如果文件不存在或为空，返回空列表
            self.messages = []
            return []
            
    def _save_messages(self, messages: List[Dict[str, Any]]):
        """
        保存消息历史到当前消息路径
        
        Args:
            messages: 消息历史列表
        """
        if not self.current_messages_path:
            raise ValueError("消息路径未设置，请先调用 _load_messages")
            
        # 确保目录存在
        os.makedirs(os.path.dirname(self.current_messages_path), exist_ok=True)
        
        with open(self.current_messages_path, "w", encoding="utf-8") as f:
            json.dump(messages, f, ensure_ascii=False)
        
        # 更新当前消息
        self.messages = messages
    
    def get_chat_history(self, node_path: str, mode: str = "learn") -> List[Dict[str, Any]]:
        """
        获取指定节点和模式的聊天历史
        
        Args:
            node_path: 节点路径
            mode: 聊天模式，"learn" 或 "learn"
            
        Returns:
            聊天历史列表
        """
        return self._load_messages(node_path, mode)

    def chat(self, question: str, data: str, node_path: str, mode: str = "learn"):
        """
        与 AI 进行对话，支持学习和测验模式
        
        Args:
            question: 用户问题
            data: 节点数据
            node_path: 节点路径，如 "0.0.1"
            mode: 对话模式，"learn" 或 "quiz"
            
        Returns:
            AI 回复内容
        """
        # 根据模式选择不同的提示词
        if mode == "learn":
            prompt = f"""
            请你作为一位专业的数学老师，辅导学生进行学习。你需要引导学生学习每个知识点，为他们提供清晰、系统的讲解。

            请遵循以下要求：
            1. 使用 Markdown 格式组织你的回答，包括标题、列表、强调等
            2. 数学公式请使用 LaTeX 格式：行内公式用 $...$ 包裹，独立公式用 $$...$$ 包裹
            3. 重要概念和定理应当突出显示
            4. 提供循序渐进的解释，从基础概念到复杂应用
            5. 适当使用例题来帮助理解
            6. 回答应当简洁明了，但不失专业性和完整性
            7. 鼓励学生提问，引导他们思考

            要学习的章节内容：
            {data}
            """
        elif mode == "quiz":
            prompt = f"""
            请你作为一位专业的数学老师，出题考察学生对知识点的掌握情况。

            请遵循以下要求：
            1. 使用 Markdown 格式组织你的回答，包括标题、列表、强调等
            2. 数学公式请使用 LaTeX 格式：行内公式用 $...$ 包裹，独立公式用 $$...$$ 包裹
            3. 如果学生回答了问题：
               - 评估回答的正确性
               - 给出详细的解释和改进建议
               - 指出思路中的优点和不足
               - 提供完整的解题过程
            4. 如果学生没有回答问题：
               - 根据知识点出一道有挑战性但合理的问题
               - 问题应当能够检验学生对概念的理解，而不仅仅是记忆
               - 问题可以包含多个小问，由浅入深
               - 提供适当的引导和提示
            5. 每次交互后，可以根据学生的掌握程度调整问题难度

            相关知识点：
            {data}
            """
        elif mode == "tutor":
            prompt = f"""
            请你作为一位耐心的数学辅导老师，针对学生的具体问题提供个性化的解答和指导。

            请遵循以下要求：
            1. 使用 Markdown 格式组织你的回答，包括标题、列表、强调等
            2. 数学公式请使用 LaTeX 格式：行内公式用 $...$ 包裹，独立公式用 $$...$$ 包裹
            3. 分析学生问题背后的概念困惑
            4. 提供多角度的解释，使用类比和可视化帮助理解
            5. 引导学生自己发现答案，而不是直接给出解决方案
            6. 针对学生的具体困难点提供有针对性的练习
            7. 鼓励学生表达自己的思考过程
            8. 耐心回答学生的所有问题，不管问题看起来多么基础

            相关知识点：
            {data}
            """
        else:
            raise ValueError(f"不支持的模式: {mode}")
            
        # 加载特定节点的消息历史
        history_messages = self._load_messages(node_path, mode)
        
        # 转换为OpenAI API所需的消息格式
        messages_for_api = []
        for msg in history_messages:
            if msg["role"] == "user":
                messages_for_api.append(ChatCompletionUserMessageParam(content=msg["content"], role="user"))
            elif msg["role"] == "assistant":
                messages_for_api.append(ChatCompletionAssistantMessageParam(content=msg["content"], role="assistant"))
        
        # 添加当前用户消息
        user_message = ChatCompletionUserMessageParam(content=question, role="user")
        system_message = ChatCompletionSystemMessageParam(content=prompt, role="system")
        
        # 创建完整的消息列表
        api_messages = [system_message, *messages_for_api, user_message]
        
        # 调用API
        response = self.ai.chat.completions.create(
            model="gpt-4o-mini",
            messages=api_messages,
            temperature=0.7 if mode == "quiz" else 0.3,  # 测验模式使用较高温度以增加创造性，学习模式使用较低温度保证准确性
            max_tokens=2000,  # 确保回答足够详细
        )
        
        content = response.choices[0].message.content
        
        # 保存消息历史
        history_messages.append({"role": "user", "content": question})
        history_messages.append({"role": "assistant", "content": content})
        self._save_messages(history_messages)
        
        return content
    def get_report(self, node_path: str,data:str, mode:Literal["learn","quiz"] = "learn"):
        promot_map ={
            "learn":f"""
            请根据学生的学习历史聊天记录，生成一份学习报告。
            要求:
            1. 使用Markdown格式组织你的回答，包括标题、列表、强调等
            2. 数学公式请使用LaTeX格式：行内公式用$...$包裹，独立公式用$$...$$包裹
            3. 报告应当包括学生的学习情况、掌握程度、存在的问题及改进建议
            4. 报告应当客观、全面，既要看到学生的进步，也要指出存在的问题
            5. 报告应当有针对性，针对学生的薄弱环节给出具体的建议
            6. 报告应当有启发性，能够激发学生的学习兴趣，引导他们主动思考
            7. 报告应当有条理，逻辑清晰，层次分明
            8. 生成综合评分（100分制,并给出理由）
            要学习的章节内容：
            {data}
            """,
            "quiz":f"""
            请根据学生的答题历史，生成一份答题报告。
            要求:
            1. 使用Markdown格式组织你的回答，包括标题、列表、强调等
            2. 数学公式请使用LaTeX格式：行内公式用$...$包裹，独立公式用$$...$$包裹
            3. 报告应当包括学生的答题情况、掌握程度、存在的问题及改进建议
            4. 报告应当客观、全面，既要看到学生的进步，也要指出存在的问题
            5. 报告应当有针对性，针对学生的薄弱环节给出具体的建议
            6. 报告应当有启发性，能够激发学生的学习兴趣，引导他们主动思考
            7. 报告应当有条理，逻辑清晰，层次分明
            8. 生成综合评分（100分制,并给出理由）
            要学习的章节内容：
            {data}
            """
        }
        history_messages = self._load_messages(node_path, mode)
        text = json.dumps(history_messages,ensure_ascii=False)
        api_messages = [
            ChatCompletionSystemMessageParam(content=promot_map[mode],role="system"),
            ChatCompletionUserMessageParam(content=text,role="user")
        ]
        response = self.ai.chat.completions.create(
            model="gpt-4o-mini",
            messages=api_messages,
            temperature=0.8,
            max_tokens=8000
        )
        content = response.choices[0].message.content
        return str(content)
            
        
if __name__ == "__main__":
    # 加载环境变量
    dotenv.load_dotenv()
    
    # 从环境变量获取 API 密钥和基础 URL
    api_key = os.getenv("OPENAI_API_KEY", "")
    base_url = os.getenv("OPENAI_BASE_URL", "https://pro.aiskt.com/v1")
    
    if not api_key:
        raise ValueError("请设置 OPENAI_API_KEY 环境变量")
        
    ai = OpenAI(api_key=api_key, base_url=base_url)
    agent = MathAgent(ai)

