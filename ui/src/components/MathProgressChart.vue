<template>
  <v-card class="mx-auto my-4" elevation="4">
    <v-card-title class="text-h5 font-weight-bold">
      学习进度
    </v-card-title>
    <v-card-text>
      <div ref="chartRef" style="width: 100%; height: 400px;"></div>
    </v-card-text>
  </v-card>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'
import * as echarts from 'echarts'
import { useCourseStore } from '@/stores/courseStore'

const chartRef = ref(null)
let chart = null
const { mathData } = useCourseStore()

// 统计学习进度
const calculateProgress = (data) => {
  if (!data) return { categories: [], completed: [], total: [] }
  
  const result = {
    categories: [],
    completed: [],
    total: []
  }
  
  // 只处理第一层的章节数据
  data.forEach(chapter => {
    if (chapter.children) {
      chapter.children.forEach(section => {
        if (section.type === 'section') {
          result.categories.push(section.name)
          
          // 计算该部分的总节点数和已完成节点数
          let totalCount = 0
          let completedCount = 0
          
          const countNodes = (node) => {
            totalCount++
            if (node.completed) {
              completedCount++
            }
            
            if (node.children && node.children.length > 0) {
              node.children.forEach(countNodes)
            }
          }
          
          countNodes(section)
          
          result.completed.push(completedCount)
          result.total.push(totalCount)
        }
      })
    }
  })
  
  return result
}

// 初始化图表
const initChart = () => {
  if (!chartRef.value || !mathData.value) return
  
  try {
    // 创建图表实例
    chart = echarts.init(chartRef.value)
    
    const progressData = calculateProgress(mathData.value)
    
    const option = {
      tooltip: {
        trigger: 'axis',
        axisPointer: {
          type: 'shadow'
        },
        formatter: function(params) {
          const categoryIndex = params[0].dataIndex
          const completed = progressData.completed[categoryIndex]
          const total = progressData.total[categoryIndex]
          const percentage = Math.round((completed / total) * 100)
          
          return `${params[0].name}<br/>
                 完成: ${completed}/${total}<br/>
                 进度: ${percentage}%`
        }
      },
      legend: {
        data: ['已完成', '总计']
      },
      grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
      },
      xAxis: {
        type: 'value',
        boundaryGap: [0, 0.01]
      },
      yAxis: {
        type: 'category',
        data: progressData.categories,
        axisLabel: {
          interval: 0,
          width: 100,
          overflow: 'break'
        }
      },
      series: [
        {
          name: '已完成',
          type: 'bar',
          data: progressData.completed,
          itemStyle: {
            color: '#91cc75'
          },
          stack: 'total',
          emphasis: {
            focus: 'series'
          }
        },
        {
          name: '未完成',
          type: 'bar',
          data: progressData.total.map((total, index) => total - progressData.completed[index]),
          itemStyle: {
            color: '#ee6666',
            opacity: 0.5
          },
          stack: 'total',
          emphasis: {
            focus: 'series'
          }
        }
      ]
    }
    
    chart.setOption(option)
    
    // 响应窗口大小变化
    window.addEventListener('resize', () => {
      chart && chart.resize()
    })
  } catch (error) {
    console.error('初始化图表失败:', error)
  }
}

// 监听数据和DOM变化
watch([() => mathData.value, () => chartRef.value], ([newData, newRef]) => {
  if (newData && newRef) {
    // 当数据和DOM都准备好时，初始化图表
    initChart()
  }
})

onMounted(() => {
  // 如果数据已经加载，则初始化图表
  if (mathData.value && chartRef.value) {
    initChart()
  }
})

onUnmounted(() => {
  if (chart) {
    chart.dispose()
    window.removeEventListener('resize', chart.resize)
  }
})
</script>

<style scoped>
/* 可以添加自定义样式 */
</style> 