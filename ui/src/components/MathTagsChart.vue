<template>
  <v-card class="mx-auto my-4" elevation="4">
    <v-card-title class="text-h5 font-weight-bold">
      标签分布
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

// 收集所有标签并统计出现次数
const collectTags = (data) => {
  if (!data) return {}
  
  const tagCounts = {}
  
  const traverse = (items) => {
    items.forEach(item => {
      if (item.tags && item.tags.length > 0) {
        item.tags.forEach(tag => {
          tagCounts[tag] = (tagCounts[tag] || 0) + 1
        })
      }
      
      if (item.children && item.children.length > 0) {
        traverse(item.children)
      }
    })
  }
  
  traverse(data)
  return tagCounts
}

// 初始化图表
const initChart = () => {
  if (!chartRef.value || !mathData.value) return
  
  try {
    // 创建图表实例
    chart = echarts.init(chartRef.value)
    
    const tagCounts = collectTags(mathData.value)
    const tagData = Object.entries(tagCounts).map(([name, value]) => ({ name, value }))
    
    // 如果没有标签数据，显示提示信息
    if (tagData.length === 0) {
      chart.setOption({
        title: {
          text: '没有找到标签数据',
          left: 'center',
          top: 'center'
        }
      })
      return
    }
    
    // 使用柱状图代替词云图，因为词云图需要额外的插件
    const option = {
      tooltip: {
        trigger: 'axis',
        axisPointer: {
          type: 'shadow'
        }
      },
      grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
      },
      xAxis: {
        type: 'category',
        data: tagData.map(item => item.name),
        axisLabel: {
          interval: 0,
          rotate: 30
        }
      },
      yAxis: {
        type: 'value'
      },
      series: [
        {
          name: '出现次数',
          type: 'bar',
          data: tagData.map(item => item.value),
          itemStyle: {
            color: function(params) {
              const colorList = ['#c23531','#2f4554','#61a0a8','#d48265','#91c7ae','#749f83','#ca8622','#bda29a','#6e7074','#546570','#c4ccd3']
              return colorList[params.dataIndex % colorList.length]
            }
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
    console.error('初始化图表时出错:', error)
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