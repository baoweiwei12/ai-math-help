<template>
  <div class="course-search">
    <v-card>
      <v-card-title>课程搜索</v-card-title>
      
      <v-card-text>
        <v-form @submit.prevent="searchCourses">
          <v-text-field
            v-model="searchQuery"
            label="搜索课程内容"
            placeholder="输入关键词搜索"
            prepend-inner-icon="mdi-magnify"
            clearable
            @click:clear="clearSearch"
          ></v-text-field>
          
          <v-btn
            color="primary"
            type="submit"
            :loading="loading"
            :disabled="!searchQuery.trim()"
          >
            搜索
          </v-btn>
        </v-form>
        
        <!-- 搜索结果 -->
        <div v-if="loading" class="text-center my-4">
          <v-progress-circular indeterminate color="primary"></v-progress-circular>
          <div class="mt-2">搜索中...</div>
        </div>
        
        <div v-else-if="error" class="mt-4">
          <v-alert type="error" title="搜索失败" :text="error"></v-alert>
        </div>
        
        <div v-else-if="searchPerformed && searchResults.length === 0" class="mt-4">
          <v-alert 
            type="info" 
            title="无搜索结果" 
            :text="'没有找到与\"' + searchQuery + '\"相关的内容'"
          ></v-alert>
        </div>
        
        <div v-else-if="searchResults.length > 0" class="mt-4">
          <v-list>
            <v-list-subheader>搜索结果 ({{ searchResults.length }})</v-list-subheader>
            
            <v-list-item
              v-for="(result, index) in searchResults"
              :key="index"
              :title="result.item.name"
              :subtitle="result.item.description || ''"
              lines="two"
            >
              <template v-slot:prepend>
                <v-icon :color="getIconColor(result.type)">
                  {{ getIconByType(result.type) }}
                </v-icon>
              </template>
              
              <template v-slot:append>
                <v-chip
                  v-for="tag in result.item.tags || []"
                  :key="tag"
                  size="small"
                  class="ml-1"
                  :color="getTagColor(tag)"
                >
                  {{ tag }}
                </v-chip>
              </template>
            </v-list-item>
          </v-list>
        </div>
      </v-card-text>
    </v-card>
  </div>
</template>

<script>
import { courseApi } from '@/api'

export default {
  name: 'CourseSearch',
  
  data() {
    return {
      searchQuery: '',
      searchResults: [],
      loading: false,
      error: null,
      searchPerformed: false
    }
  },
  
  methods: {
    /**
     * 搜索课程
     */
    async searchCourses() {
      if (!this.searchQuery.trim()) return
      
      this.loading = true
      this.error = null
      
      try {
        this.searchResults = await courseApi.search(this.searchQuery)
        this.searchPerformed = true
      } catch (error) {
        this.error = '搜索失败，请稍后重试'
        console.error('搜索失败:', error)
      } finally {
        this.loading = false
      }
    },
    
    /**
     * 清除搜索
     */
    clearSearch() {
      this.searchQuery = ''
      this.searchResults = []
      this.searchPerformed = false
      this.error = null
    },
    
    /**
     * 根据类型获取图标
     * @param {string} type 类型
     * @returns {string} 图标名称
     */
    getIconByType(type) {
      const iconMap = {
        'chapter': 'mdi-book-open-variant',
        'section': 'mdi-bookmark',
        'concept': 'mdi-lightbulb',
        'subtopic': 'mdi-format-list-bulleted'
      }
      
      return iconMap[type] || 'mdi-help-circle'
    },
    
    /**
     * 根据类型获取图标颜色
     * @param {string} type 类型
     * @returns {string} 颜色名称
     */
    getIconColor(type) {
      const colorMap = {
        'chapter': 'primary',
        'section': 'secondary',
        'concept': 'info',
        'subtopic': 'success'
      }
      
      return colorMap[type] || 'grey'
    },
    
    /**
     * 根据标签获取颜色
     * @param {string} tag 标签名称
     * @returns {string} 颜色名称
     */
    getTagColor(tag) {
      const colorMap = {
        '重点': 'red',
        '难点': 'purple',
        '考点': 'orange',
        '概念性': 'blue',
        '程序性': 'green',
        '应用': 'teal',
        '创造': 'deep-purple',
        '元认知': 'indigo',
        '课程思政': 'pink'
      }
      
      return colorMap[tag] || 'grey'
    }
  }
}
</script>

<style scoped>
.course-search {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
}
</style> 