<template>
  <v-card
    class="mx-auto my-4"
    elevation="4"
  >
    <v-card-title class="text-h5 font-weight-bold">
      内容类型分布
    </v-card-title>
    <v-card-text>
      <div
        ref="chartRef"
        style="width: 100%; height: 400px;"
      />
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

// 统计不同类型的节点数量和完成状态
const countTypes = (data) => {
  if (!data) return { completed: {}, incomplete: {} }
  
  const counts = {
    completed: {},
    incomplete: {}
  }
  
  const traverse = (items) => {
    items.forEach(item => {
      if (item.completed) {
        counts.completed[item.type] = (counts.completed[item.type] || 0) + 1
      } else {
        counts.incomplete[item.type] = (counts.incomplete[item.type] || 0) + 1
      }
      
      if (item.children && item.children.length > 0) {
        traverse(item.children)
      }
    })
  }
  
  traverse(data)
  return counts
}

// 初始化图表
const initChart = () => {
  if (!chartRef.value || !mathData.value) return
  
  try {
    // 创建图表实例
    chart = echarts.init(chartRef.value)
    
    const typeCounts = countTypes(mathData.value)
    
    // 准备饼图数据
    const completedData = Object.entries(typeCounts.completed).map(([name, value]) => ({
      name: `${name} (已完成)`,
      value,
      itemStyle: {
        color: getTypeColor(name)
      }
    }))
    
    const incompleteData = Object.entries(typeCounts.incomplete).map(([name, value]) => ({
      name: `${name} (未完成)`,
      value,
      itemStyle: {
        color: getTypeColor(name, 0.4) // 使用较淡的颜色
      }
    }))
    
    const option = {
      tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b}: {c} ({d}%)'
      },
      legend: {
        type: 'scroll',
        orient: 'vertical',
        right: 10,
        top: 20,
        bottom: 20,
        data: [...completedData, ...incompleteData].map(item => item.name)
      },
      series: [
        {
          name: '内容类型',
          type: 'pie',
          radius: ['40%', '70%'],
          avoidLabelOverlap: false,
          itemStyle: {
            borderRadius: 10,
            borderColor: '#fff',
            borderWidth: 2
          },
          label: {
            show: false,
            position: 'center'
          },
          emphasis: {
            label: {
              show: true,
              fontSize: 16,
              fontWeight: 'bold'
            }
          },
          labelLine: {
            show: false
          },
          data: [...completedData, ...incompleteData]
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

// 根据类型获取颜色
const getTypeColor = (type, opacity = 1) => {
  const colorMap = {
    'chapter': '#5470c6',
    'section': '#91cc75',
    'topic': '#fac858',
    'subtopic': '#ee6666',
    'concept': '#73c0de'
  }
  
  const color = colorMap[type] || '#9a60b4'
  
  // 如果需要透明度
  if (opacity < 1) {
    // 将十六进制颜色转换为rgba
    const r = parseInt(color.slice(1, 3), 16)
    const g = parseInt(color.slice(3, 5), 16)
    const b = parseInt(color.slice(5, 7), 16)
    return `rgba(${r}, ${g}, ${b}, ${opacity})`
  }
  
  return color
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