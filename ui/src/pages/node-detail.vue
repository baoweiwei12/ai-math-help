<template>
  <v-container>
    <!-- 添加面包屑导航 -->
    <v-row>
      <v-col cols="12">
        <v-breadcrumbs :items="breadcrumbs" class="pa-0 mb-4">
          <template v-slot:divider>
            <v-icon icon="mdi-chevron-right"></v-icon>
          </template>
          <template v-slot:title="{ item }">
            <v-btn
              variant="text"
              :color="item.disabled ? '' : 'primary'"
              :disabled="item.disabled"
              @click="navigateToNode(item.path)"
            >
              {{ item.title }}
            </v-btn>
          </template>
        </v-breadcrumbs>
      </v-col>
    </v-row>
    
    <v-row v-if="isLoading">
      <v-col cols="12" class="d-flex justify-center align-center" style="height: 300px;">
        <v-progress-circular indeterminate color="primary" size="64"></v-progress-circular>
      </v-col>
    </v-row>
    
    <v-row v-else>
      <v-col cols="12">
        <v-card class="mx-auto my-4" elevation="4">
          <v-card-title class="text-h4 font-weight-bold d-flex align-center">
            {{ nodeData ? nodeData.name : '节点详情' }}
            <v-chip
              v-if="nodeData && nodeData.completed !== undefined"
              :color="nodeData.completed ? 'success' : 'error'"
              class="ml-4"
            >
              {{ nodeData.completed ? '已完成学习' : '未完成学习' }}
            </v-chip>
            <v-spacer></v-spacer>
            <v-btn-toggle
              v-model="activeMode"
              mandatory
              color="primary"
              rounded="pill"
              density="comfortable"
            >
              <v-btn value="info">
                <v-icon left>mdi-information-outline</v-icon>
                信息
              </v-btn>
              <v-btn value="learn">
                <v-icon left>mdi-book-open-variant</v-icon>
                学习
              </v-btn>
              <v-btn value="quiz">
                <v-icon left>mdi-help-circle-outline</v-icon>
                答题
              </v-btn>
            </v-btn-toggle>
          </v-card-title>
          
          <v-card-subtitle v-if="nodeData && nodeData.type">
            类型: {{ nodeData.type }}
            <span v-if="nodeData.tags && nodeData.tags.length > 0" class="ml-4">
              标签:
              <v-chip
                v-for="(tag, index) in nodeData.tags"
                :key="index"
                size="x-small"
                color="primary"
                variant="outlined"
                class="ml-1"
              >
                {{ tag }}
              </v-chip>
            </span>
          </v-card-subtitle>
          
          <v-card-text>
            <v-alert
              v-if="!nodeData"
              type="warning"
              text="未找到节点数据"
            ></v-alert>
            
            <div v-else>
              <!-- 信息模式 -->
              <div v-if="activeMode === 'info'">
                <div v-if="nodeData.description" class="my-4">
                  <div class="text-h6">描述:</div>
                  <div>{{ nodeData.description }}</div>
                </div>
                
                <div v-if="nodeData.children && nodeData.children.length > 0" class="my-4">
                  <div class="text-h6">子节点:</div>
                  <v-list>
                    <v-list-item
                      v-for="(child, index) in nodeData.children"
                      :key="index"
                      :title="child.name"
                      :subtitle="child.type"
                      :prepend-icon="getNodeIcon(child.type)"
                      :append-icon="'mdi-arrow-right'"
                      @click="navigateToNode(getChildPath(index))"
                      class="my-1"
                      rounded="lg"
                      :color="child.completed ? 'success-lighten-4' : 'error-lighten-4'"
                    >
                      <template v-slot:append>
                        <v-chip
                          size="small"
                          :color="child.completed ? 'success' : 'error'"
                          variant="outlined"
                        >
                          {{ child.completed ? '已完成' : '未完成' }}
                        </v-chip>
                      </template>
                    </v-list-item>
                  </v-list>
                </div>
              </div>
              
              <!-- 学习模式 -->
              <div v-else-if="activeMode === 'learn'" class="chat-container">
                <div class="chat-messages" ref="chatMessagesRef">
                  <div 
                    v-for="(message, index) in chatMessages" 
                    :key="index" 
                    :class="['message', message.role === 'user' ? 'user-message' : 'ai-message']"
                  >
                    <div class="message-avatar">
                      <v-avatar :color="message.role === 'user' ? 'primary' : 'success'" size="36">
                        <v-icon color="white">{{ message.role === 'user' ? 'mdi-account' : 'mdi-robot' }}</v-icon>
                      </v-avatar>
                    </div>
                    <div class="message-content">
                      <div class="message-text" v-html="message.role === 'user' ? message.content : renderMarkdown(message.content)"></div>
                      <div class="message-time">{{ message.time }}</div>
                    </div>
                  </div>
                  <div v-if="isAiTyping" class="message ai-message">
                    <div class="message-avatar">
                      <v-avatar color="success" size="36">
                        <v-icon color="white">mdi-robot</v-icon>
                      </v-avatar>
                    </div>
                    <div class="message-content">
                      <div class="message-text typing-indicator">
                        <span></span>
                        <span></span>
                        <span></span>
                      </div>
                    </div>
                  </div>
                </div>
                
                <div class="chat-input">
                  <v-textarea
                    v-model="userInput"
                    placeholder="输入您的问题..."
                    rows="1"
                    auto-grow
                    hide-details
                    density="comfortable"
                    @keydown.enter.prevent="sendMessage"
                    class="chat-textarea"
                    color="primary"
                  ></v-textarea>
                  <v-btn 
                    color="primary" 
                    :disabled="!userInput.trim() || isAiTyping" 
                    @click="sendMessage"
                    class="ml-2"
                  >
                    <v-icon>mdi-send</v-icon>
                  </v-btn>
                </div>
              </div>
              
              <!-- 答题模式 -->
              <div v-else-if="activeMode === 'quiz'" class="chat-container">
                <div class="chat-messages" ref="quizMessagesRef">
                  <div 
                    v-for="(message, index) in quizMessages" 
                    :key="index" 
                    :class="['message', message.role === 'user' ? 'user-message' : 'ai-message']"
                  >
                    <div class="message-avatar">
                      <v-avatar :color="message.role === 'user' ? 'primary' : 'error'" size="36">
                        <v-icon color="white">{{ message.role === 'user' ? 'mdi-account' : 'mdi-school' }}</v-icon>
                      </v-avatar>
                    </div>
                    <div class="message-content">
                      <div class="message-text" v-html="message.role === 'user' ? message.content : renderMarkdown(message.content)"></div>
                      <div class="message-time">{{ message.time }}</div>
                    </div>
                  </div>
                  <div v-if="isQuizTyping" class="message ai-message">
                    <div class="message-avatar">
                      <v-avatar color="error" size="36">
                        <v-icon color="white">mdi-school</v-icon>
                      </v-avatar>
                    </div>
                    <div class="message-content">
                      <div class="message-text typing-indicator">
                        <span></span>
                        <span></span>
                        <span></span>
                      </div>
                    </div>
                  </div>
                </div>
                
                <div class="chat-input">
                  <v-textarea
                    v-model="quizInput"
                    placeholder="输入您的答案..."
                    rows="1"
                    auto-grow
                    hide-details
                    density="comfortable"
                    @keydown.enter.prevent="submitAnswer"
                    class="chat-textarea"
                    color="error"
                  ></v-textarea>
                  <v-btn 
                    color="error" 
                    :disabled="!quizInput.trim() || isQuizTyping" 
                    @click="submitAnswer"
                    class="ml-2"
                  >
                    <v-icon>mdi-send</v-icon>
                  </v-btn>
                </div>
              </div>
              
              <div class="d-flex justify-end mt-6">
                <v-btn
                  color="primary"
                  @click="goBack"
                >
                  返回
                </v-btn>
                
                <v-btn
                  class="ml-4"
                  :color="nodeData.completed ? 'error' : 'success'"
                  @click="toggleCompleted"
                  :loading="isUpdating"
                >
                  {{ nodeData.completed ? '标记为未完成' : '标记为已完成' }}
                </v-btn>
              </div>
            </div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, onMounted, computed, watch, nextTick } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import courseApi from '../api/course'
import { useCourseStore } from '@/stores/courseStore'
import { marked } from 'marked'
import katex from 'katex'
import 'katex/dist/katex.min.css'

const route = useRoute()
const router = useRouter()
const nodeData = ref(null)
const nodePath = ref('')
const isLoading = ref(false)
const isUpdating = ref(false)
const pathNames = ref([])
const { refreshData } = useCourseStore()

// 聊天相关
const activeMode = ref('info') // 'info', 'learn', 'quiz'
const userInput = ref('')
const quizInput = ref('')
const chatMessages = ref([])
const quizMessages = ref([])
const isAiTyping = ref(false)
const isQuizTyping = ref(false)
const chatMessagesRef = ref(null)
const quizMessagesRef = ref(null)

// 添加 KaTeX 渲染器
const renderMathInElement = (element) => {
  const mathElements = element.querySelectorAll('.math')
  for (const mathElement of mathElements) {
    try {
      const display = mathElement.classList.contains('display')
      const math = mathElement.textContent
      katex.render(math, mathElement, {
        displayMode: display,
        throwOnError: false
      })
    } catch (error) {
      console.error('KaTeX 渲染错误:', error)
    }
  }
}

// 添加 KaTeX 扩展
const mathExtension = {
  name: 'math',
  level: 'inline',
  start(src) { return src.indexOf('$') },
  tokenizer(src) {
    // 行内公式: $...$
    const inlineMath = /^\$([^$\n]+?)\$/
    // 块级公式: $$...$$
    const blockMath = /^\$\$([^$]+?)\$\$/

    if (blockMath.test(src)) {
      const match = blockMath.exec(src)
      if (match) {
        return {
          type: 'math',
          raw: match[0],
          text: match[1].trim(),
          display: true
        }
      }
    }

    if (inlineMath.test(src)) {
      const match = inlineMath.exec(src)
      if (match) {
        return {
          type: 'math',
          raw: match[0],
          text: match[1].trim(),
          display: false
        }
      }
    }

    return undefined
  },
  renderer(token) {
    return `<span class="math ${token.display ? 'display' : ''}">${token.text}</span>`
  }
}

// 注册 KaTeX 扩展
marked.use({ 
  extensions: [mathExtension],
  breaks: true, // 启用换行符转换为<br>
  gfm: true,    // 启用GitHub风格的Markdown
  headerIds: false, // 禁用标题ID生成
  mangle: false, // 禁用电子邮件地址混淆
  sanitize: false // 允许HTML标签
})

// 将Markdown转换为HTML
const renderMarkdown = (text) => {
  if (!text) return ''
  const html = marked(text)
  
  // 使用 DOM 解析器处理 HTML
  const parser = new DOMParser()
  const doc = parser.parseFromString(html, 'text/html')
  
  // 渲染数学公式
  renderMathInElement(doc.body)
  
  return doc.body.innerHTML
}

// 计算面包屑导航
const breadcrumbs = computed(() => {
  if (!nodePath.value) return [{ title: '首页', disabled: false, path: '' }]
  
  const result = [{ title: '首页', disabled: false, path: '' }]
  
  // 使用从API获取的路径名称
  if (pathNames.value && pathNames.value.length > 0) {
    pathNames.value.forEach((item, index) => {
      result.push({
        title: item.name,
        disabled: index === pathNames.value.length - 1,
        path: item.path
      })
    })
  }
  
  return result
})

// 获取路径上所有节点的名称
const fetchPathNames = async () => {
  if (!nodePath.value) return
  
  try {
    pathNames.value = await courseApi.getPathNames(nodePath.value)
  } catch (error) {
    console.error('获取路径名称失败:', error)
  }
}

// 获取节点数据
const fetchNodeData = async () => {
  if (!nodePath.value) return
  
  isLoading.value = true
  try {
    const data = await courseApi.getNodeByPath(nodePath.value)
    nodeData.value = data
    
    // 获取路径上所有节点的名称
    await fetchPathNames()
    
    // 初始化聊天
    initializeChat()
  } catch (error) {
    console.error('获取节点数据失败:', error)
  } finally {
    isLoading.value = false
  }
}

// 初始化聊天
const initializeChat = async () => {
  // 清空聊天记录
  chatMessages.value = []
  quizMessages.value = []
  
  if (nodeData.value) {
    try {
      // 加载学习模式的聊天历史
      const learnHistory = await courseApi.getChatHistory(nodePath.value, "learn")
      if (learnHistory && learnHistory.length > 0) {
        // 为历史消息添加时间戳
        learnHistory.forEach(msg => {
          msg.time = msg.time || formatTime(new Date())
        })
        chatMessages.value = learnHistory
      } else {
        // 如果没有历史记录，添加欢迎消息
        const welcomeMessage = {
          role: 'assistant',
          content: `欢迎学习"${nodeData.value.name}"！我是您的AI助手，有任何问题都可以向我提问。`,
          time: formatTime(new Date())
        }
        chatMessages.value.push(welcomeMessage)
      }
      
      // 加载问答模式的聊天历史
      const quizHistory = await courseApi.getChatHistory(nodePath.value, "quiz")
      if (quizHistory && quizHistory.length > 0) {
        // 为历史消息添加时间戳
        quizHistory.forEach(msg => {
          msg.time = msg.time || formatTime(new Date())
        })
        quizMessages.value = quizHistory
      } else {
        // 如果没有历史记录，添加欢迎消息
        const quizWelcomeMessage = {
          role: 'assistant',
          content: `欢迎来到"${nodeData.value.name}"的答题环节！我会提出一些问题来测试您的理解。`,
          time: formatTime(new Date())
        }
        quizMessages.value.push(quizWelcomeMessage)
        
      }
    } catch (error) {
      console.error('加载聊天历史失败:', error)
      
      // 添加默认欢迎消息
      const welcomeMessage = {
        role: 'assistant',
        content: `欢迎学习"${nodeData.value.name}"！我是您的AI助手，有任何问题都可以向我提问。`,
        time: formatTime(new Date())
      }
      chatMessages.value.push(welcomeMessage)
      
      const quizWelcomeMessage = {
        role: 'assistant',
        content: `欢迎来到"${nodeData.value.name}"的答题环节！我会提出一些问题来测试您的理解。`,
        time: formatTime(new Date())
      }
      quizMessages.value.push(quizWelcomeMessage)
      
    }
  }
  
  // 滚动到底部
  nextTick(() => {
    if (activeMode.value === 'learn') {
      scrollToBottom(chatMessagesRef.value)
    } else if (activeMode.value === 'quiz') {
      scrollToBottom(quizMessagesRef.value)
    }
  })
}

// 发送消息
const sendMessage = async () => {
  if (!userInput.value.trim() || isAiTyping.value) return
  
  // 添加用户消息
  const userMessage = {
    role: 'user',
    content: userInput.value.trim(),
    time: formatTime(new Date())
  }
  chatMessages.value.push(userMessage)
  
  // 清空输入框
  userInput.value = ''
  
  // 滚动到底部
  await nextTick()
  scrollToBottom(chatMessagesRef.value)
  
  // 显示AI正在输入
  isAiTyping.value = true
  
  try {
    // 调用API获取AI回复
    const response = await courseApi.sendChatMessage(nodePath.value, userMessage.content, "learn")
    
    // 添加AI回复
    setTimeout(() => {
      isAiTyping.value = false
      
      const aiMessage = {
        role: 'assistant',
        content: response.content,
        time: formatTime(new Date())
      }
      chatMessages.value.push(aiMessage)
      
      // 滚动到底部
      nextTick(() => {
        scrollToBottom(chatMessagesRef.value)
      })
    }, 500 + Math.random() * 1000) // 随机延迟，模拟打字效果
  } catch (error) {
    console.error('获取AI回复失败:', error)
    isAiTyping.value = false
    
    // 添加错误消息
    const errorMessage = {
      role: 'assistant',
      content: '抱歉，我遇到了一些问题，无法回答您的问题。请稍后再试。',
      time: formatTime(new Date())
    }
    chatMessages.value.push(errorMessage)
    
    // 滚动到底部
    nextTick(() => {
      scrollToBottom(chatMessagesRef.value)
    })
  }
}

// 提交答案
const submitAnswer = async () => {
  if (!quizInput.value.trim() || isQuizTyping.value) return
  
  // 添加用户答案
  const userAnswer = {
    role: 'user',
    content: quizInput.value.trim(),
    time: formatTime(new Date())
  }
  quizMessages.value.push(userAnswer)
  
  // 清空输入框
  quizInput.value = ''
  
  // 滚动到底部
  await nextTick()
  scrollToBottom(quizMessagesRef.value)
  
  // 显示AI正在输入
  isQuizTyping.value = true
  
  try {
    // 调用API检查答案
    const response = await courseApi.sendChatMessage(nodePath.value, userAnswer.content, "quiz")
    
    // 简单判断是否正确
    const isCorrect = response.content.includes("正确") || 
                      response.content.includes("很好") || 
                      response.content.includes("对")
    
    // 添加反馈
    setTimeout(() => {
      isQuizTyping.value = false
      
      // 更新用户答案，添加反馈
      const lastUserMessage = quizMessages.value[quizMessages.value.length - 1]
      lastUserMessage.feedback = response.content
      lastUserMessage.isCorrect = isCorrect
      
      // 添加AI回复
      const aiMessage = {
        role: 'assistant',
        content: response.content,
        time: formatTime(new Date())
      }
      quizMessages.value.push(aiMessage)
      
      // 滚动到底部
      nextTick(() => {
        scrollToBottom(quizMessagesRef.value)
      })
      

    }, 500 + Math.random() * 1000) // 随机延迟，模拟打字效果
  } catch (error) {
    console.error('检查答案失败:', error)
    isQuizTyping.value = false
    
    // 添加错误消息
    const errorMessage = {
      role: 'assistant',
      content: '抱歉，我遇到了一些问题，无法检查您的答案。请稍后再试。',
      time: formatTime(new Date())
    }
    quizMessages.value.push(errorMessage)
    
    // 滚动到底部
    nextTick(() => {
      scrollToBottom(quizMessagesRef.value)
    })
  }
}

// 发送测验问题
const sendQuizQuestion = async () => {
  isQuizTyping.value = true
  
  try {
    // 调用API获取问题
    const response = await courseApi.sendChatMessage(
      nodePath.value, 
      "请为我出一道关于这个知识点的测验题", 
      "quiz"
    )
    
    // 添加问题
    setTimeout(() => {
      isQuizTyping.value = false
      
      const questionMessage = {
        role: 'assistant',
        content: response.content,
        time: formatTime(new Date())
      }
      quizMessages.value.push(questionMessage)
      
      // 滚动到底部
      nextTick(() => {
        scrollToBottom(quizMessagesRef.value)
      })
    }, 500 + Math.random() * 1000) // 随机延迟，模拟打字效果
  } catch (error) {
    console.error('获取问题失败:', error)
    isQuizTyping.value = false
    
    // 添加错误消息
    const errorMessage = {
      role: 'assistant',
      content: '抱歉，我遇到了一些问题，无法生成问题。请稍后再试。',
      time: formatTime(new Date())
    }
    quizMessages.value.push(errorMessage)
    
    // 滚动到底部
    nextTick(() => {
      scrollToBottom(quizMessagesRef.value)
    })
  }
}

// 格式化时间
const formatTime = (date) => {
  const hours = date.getHours().toString().padStart(2, '0')
  const minutes = date.getMinutes().toString().padStart(2, '0')
  return `${hours}:${minutes}`
}

// 滚动到底部
const scrollToBottom = (element) => {
  if (element) {
    element.scrollTop = element.scrollHeight
  }
}

// 返回上一页
const goBack = () => {
  router.push('/')
}

// 切换完成状态
const toggleCompleted = async () => {
  if (!nodeData.value) return
  
  isUpdating.value = true
  try {
    const newStatus = !nodeData.value.completed
    const updatedNode = await courseApi.updateNodeStatus(nodePath.value, newStatus)
    nodeData.value = updatedNode
    
    // 更新全局数据，以便图表能够显示最新状态
    await refreshData()
  } catch (error) {
    console.error('更新节点状态失败:', error)
  } finally {
    isUpdating.value = false
  }
}

// 获取子节点的路径
const getChildPath = (childIndex) => {
  return `${nodePath.value}.${childIndex}`
}

// 导航到指定节点
const navigateToNode = (path) => {
  if (path === '') {
    router.push('/')
    return
  }
  
  router.push({
    path: '/node-detail',
    query: {
      path: path
    }
  })
}

// 根据节点类型获取图标
const getNodeIcon = (type) => {
  const iconMap = {
    'chapter': 'mdi-book-open-variant',
    'section': 'mdi-file-document-outline',
    'topic': 'mdi-format-list-bulleted',
    'subtopic': 'mdi-format-list-text',
    'concept': 'mdi-lightbulb-outline'
  }
  
  return iconMap[type] || 'mdi-circle-small'
}

// 监听路由参数变化
watch(
  () => route.query.path,
  (newPath) => {
    if (newPath) {
      nodePath.value = newPath
      fetchNodeData()
    }
  }
)

// 监听模式变化，滚动到底部
watch(activeMode, () => {
  nextTick(() => {
    if (activeMode.value === 'learn') {
      scrollToBottom(chatMessagesRef.value)
    } else if (activeMode.value === 'quiz') {
      scrollToBottom(quizMessagesRef.value)
    }
  })
})

onMounted(() => {
  const path = route.query.path
  if (path) {
    nodePath.value = path
    fetchNodeData()
  }
})
</script>

<style scoped>
pre {
  white-space: pre-wrap;
  word-wrap: break-word;
  background-color: #2d2d2d;
  color: #f8f8f2;
  border-radius: 4px;
  padding: 16px;
  overflow-x: auto;
  font-family: 'Courier New', Courier, monospace;
  font-size: 14px;
  line-height: 1.5;
}

/* 数学公式样式 */
:deep(.math) {
  font-size: 1.1em;
}

:deep(.math.display) {
  display: block;
  text-align: center;
  margin: 1em 0;
}

.json-card {
  background-color: #2d2d2d;
  border: 1px solid #444;
}

.chat-container {
  display: flex;
  flex-direction: column;
  height: 700px;
  border-radius: 8px;
  overflow: hidden;
  background-color: #f5f5f5;
}

.chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 16px;
  display: flex;
  flex-direction: column;
}

.message {
  display: flex;
  margin-bottom: 16px;
  max-width: 80%;
}

.user-message {
  align-self: flex-end;
  flex-direction: row-reverse;
}

.ai-message {
  align-self: flex-start;
}

.message-avatar {
  margin: 0 8px;
}

.message-content {
  display: flex;
  flex-direction: column;
}

.message-text {
  padding: 12px;
  border-radius: 12px;
  position: relative;
  word-break: break-word;
}

.user-message .message-text {
  background-color: #1976d2;
  color: white;
  border-top-right-radius: 0;
}

.ai-message .message-text {
  background-color: white;
  color: #333;
  border-top-left-radius: 0;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.message-time {
  font-size: 0.7rem;
  color: #888;
  margin-top: 4px;
  align-self: flex-end;
}

.user-message .message-time {
  margin-right: 12px;
}

.ai-message .message-time {
  margin-left: 12px;
}

.message-feedback {
  margin-top: 4px;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 0.8rem;
}

.correct-feedback {
  background-color: rgba(76, 175, 80, 0.1);
  color: #4caf50;
}

.incorrect-feedback {
  background-color: rgba(244, 67, 54, 0.1);
  color: #f44336;
}

.chat-input {
  display: flex;
  padding: 8px;
  background-color: white;
  border-top: 1px solid #e0e0e0;
}

.chat-textarea {
  background-color: #f5f5f5;
  border-radius: 8px;
}

.chat-textarea :deep(.v-field__input) {
  color: #333 !important;
  padding: 8px;
}

.chat-textarea :deep(.v-field__outline) {
  border-color: #ddd;
}

.chat-textarea :deep(.v-field) {
  border-radius: 8px;
}

.chat-textarea :deep(.v-field--focused) {
  background-color: #fff;
}

.typing-indicator {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 8px 16px !important;
}

.typing-indicator span {
  height: 8px;
  width: 8px;
  margin: 0 2px;
  background-color: #888;
  border-radius: 50%;
  display: inline-block;
  animation: typing 1.4s infinite ease-in-out both;
}

.typing-indicator span:nth-child(1) {
  animation-delay: 0s;
}

.typing-indicator span:nth-child(2) {
  animation-delay: 0.2s;
}

.typing-indicator span:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes typing {
  0% {
    transform: scale(1);
    opacity: 0.4;
  }
  20% {
    transform: scale(1.2);
    opacity: 1;
  }
  100% {
    transform: scale(1);
    opacity: 0.4;
  }
}

/* 添加Markdown样式 */
.message-text :deep(h1) {
  font-size: 1.5rem;
  margin-top: 0.5rem;
  margin-bottom: 0.5rem;
}

.message-text :deep(h2) {
  font-size: 1.3rem;
  margin-top: 0.5rem;
  margin-bottom: 0.5rem;
}

.message-text :deep(h3) {
  font-size: 1.1rem;
  margin-top: 0.5rem;
  margin-bottom: 0.5rem;
}

.message-text :deep(p) {
  margin-bottom: 0.5rem;
}

.message-text :deep(ul), .message-text :deep(ol) {
  padding-left: 1.5rem;
  margin-bottom: 0.5rem;
}

.message-text :deep(li) {
  margin-bottom: 0.25rem;
}

.message-text :deep(code) {
  font-family: 'Courier New', Courier, monospace;
  background-color: rgba(0, 0, 0, 0.05);
  padding: 0.1rem 0.3rem;
  border-radius: 3px;
  font-size: 0.9em;
}

.message-text :deep(pre) {
  margin: 0.5rem 0;
  padding: 0.5rem;
  background-color: #2d2d2d;
  border-radius: 4px;
  overflow-x: auto;
}

.message-text :deep(pre code) {
  background-color: transparent;
  padding: 0;
  color: #f8f8f2;
  font-size: 0.9em;
  line-height: 1.4;
}

.message-text :deep(blockquote) {
  border-left: 4px solid #ddd;
  padding-left: 1rem;
  margin-left: 0;
  margin-right: 0;
  font-style: italic;
}

.message-text :deep(table) {
  border-collapse: collapse;
  width: 100%;
  margin: 0.5rem 0;
}

.message-text :deep(th), .message-text :deep(td) {
  border: 1px solid #ddd;
  padding: 0.5rem;
}

.message-text :deep(th) {
  background-color: #f5f5f5;
}

.message-text :deep(a) {
  color: #1976d2;
  text-decoration: none;
}

.message-text :deep(a:hover) {
  text-decoration: underline;
}

.message-text :deep(img) {
  max-width: 100%;
  height: auto;
  border-radius: 4px;
}

/* 调整用户消息中的Markdown样式 */
.user-message .message-text :deep(a) {
  color: #ffffff;
  text-decoration: underline;
}

.user-message .message-text :deep(code) {
  background-color: rgba(255, 255, 255, 0.2);
  color: #ffffff;
}
</style> 