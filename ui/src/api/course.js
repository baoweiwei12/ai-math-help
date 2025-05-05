// 课程API服务
import http from './axios'

/**
 * 课程API服务
 */
const courseApi = {
  /**
   * 获取所有章节
   * @returns {Promise<Array>} 章节列表
   */
  async getChapters() {
    try {
      return await http.get('/api/chapters')
    } catch (error) {
      console.error('获取章节列表失败:', error)
      throw error
    }
  },

  /**
   * 获取特定章节
   * @param {number} chapterIndex 章节索引
   * @returns {Promise<Object>} 章节信息
   */
  async getChapter(chapterIndex) {
    try {
      return await http.get(`/api/chapters/${chapterIndex}`)
    } catch (error) {
      console.error(`获取章节 ${chapterIndex} 失败:`, error)
      throw error
    }
  },

  /**
   * 获取特定章节的所有小节
   * @param {number} chapterIndex 章节索引
   * @returns {Promise<Array>} 小节列表
   */
  async getSections(chapterIndex) {
    try {
      return await http.get(`/api/chapters/${chapterIndex}/sections`)
    } catch (error) {
      console.error(`获取章节 ${chapterIndex} 的小节列表失败:`, error)
      throw error
    }
  },

  /**
   * 获取特定小节
   * @param {number} chapterIndex 章节索引
   * @param {number} sectionIndex 小节索引
   * @returns {Promise<Object>} 小节信息
   */
  async getSection(chapterIndex, sectionIndex) {
    try {
      return await http.get(`/api/chapters/${chapterIndex}/sections/${sectionIndex}`)
    } catch (error) {
      console.error(`获取章节 ${chapterIndex} 的小节 ${sectionIndex} 失败:`, error)
      throw error
    }
  },

  /**
   * 搜索内容
   * @param {string} query 搜索关键词
   * @returns {Promise<Array>} 搜索结果
   */
  async search(query) {
    try {
      return await http.get('/api/search', { params: { q: query } })
    } catch (error) {
      console.error(`搜索 "${query}" 失败:`, error)
      throw error
    }
  },

  /**
   * 根据路径获取节点数据
   * @param {string} path 节点路径，格式如 "0.1.2"
   * @returns {Promise<Object>} 节点数据
   */
  async getNodeByPath(path) {
    try {
      return await http.get(`/api/node`, { params: { path } })
    } catch (error) {
      console.error(`获取路径 ${path} 的节点数据失败:`, error)
      throw error
    }
  },

  /**
   * 更新节点的完成状态
   * @param {string} path 节点路径，格式如 "0.1.2"
   * @param {boolean} completed 完成状态
   * @returns {Promise<Object>} 更新后的节点数据
   */
  async updateNodeStatus(path, completed) {
    try {
      return await http.patch(`/api/node/status`, { path, completed })
    } catch (error) {
      console.error(`更新路径 ${path} 的节点状态失败:`, error)
      throw error
    }
  },

  /**
   * 获取路径上所有节点的名称
   * @param {string} path 节点路径，格式如 "0.1.2"
   * @returns {Promise<Array>} 路径上所有节点的名称
   */
  async getPathNames(path) {
    try {
      return await http.get(`/api/path-names`, { params: { path } })
    } catch (error) {
      console.error(`获取路径 ${path} 上的节点名称失败:`, error)
      throw error
    }
  },

  /**
   * 获取聊天历史记录
   * @param {string} path 节点路径，格式如 "0.1.2"
   * @param {string} mode 聊天模式，"learn" 或 "quiz"
   * @returns {Promise<Array>} 聊天历史记录
   */
  async getChatHistory(path, mode) {
    try {
      return await http.get(`/api/chat/history`, { params: { path, mode } })
    } catch (error) {
      console.error(`获取聊天历史记录失败:`, error)
      throw error
    }
  },

  /**
   * 发送聊天消息
   * @param {string} path 节点路径，格式如 "0.1.2"
   * @param {string} message 用户消息
   * @param {string} mode 聊天模式，"learn" 或 "quiz"
   * @returns {Promise<Object>} AI回复
   */
  async sendChatMessage(path, message, mode) {
    try {
      return await http.post(`/api/chat`, { path, message, mode })
    } catch (error) {
      console.error(`发送聊天消息失败:`, error)
      throw error
    }
  },

    /**
   * 生成学习或测验报告
   * @param {string} path 节点路径，格式如 "0.1.2"
   * @param {string} mode 报告模式，"learn" 或 "quiz"
   * @returns {Promise<Object>} 报告内容
   */
    async generateReport(path, mode) {
      try {
        return await http.get(`/api/report`, { params: { path, mode } })
      } catch (error) {
        console.error(`生成${mode === 'learn' ? '学习' : '测验'}报告失败:`, error)
        throw error
      }
    }
}

export default courseApi