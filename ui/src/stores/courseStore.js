import { ref } from 'vue'
import courseApi from '../api/course'

// 创建一个简单的响应式存储
const mathData = ref(null)
const loading = ref(false)
const error = ref(null)
const initialized = ref(false)

// 加载数据
const loadData = async () => {
  // 如果数据已经加载过，则不再重复加载
  if (initialized.value) return { mathData, loading, error }
  
  try {
    loading.value = true
    error.value = null
    
    // 从API获取数据
    mathData.value = await courseApi.getChapters()
    initialized.value = true
  } catch (err) {
    console.error('加载课程数据失败:', err)
    error.value = err.message || '加载数据失败'
  } finally {
    loading.value = false
  }
  
  return { mathData, loading, error }
}

// 重新加载数据（强制刷新）
const refreshData = async () => {
  initialized.value = false
  return await loadData()
}

// 导出存储
export const useCourseStore = () => {
  return {
    mathData,
    loading,
    error,
    loadData,
    refreshData
  }
} 