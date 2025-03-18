<template>
  <v-card
    class="mx-auto my-4"
    elevation="4"
  >
    <v-card-title class="text-h5 font-weight-bold">
      数学章节结构图
    </v-card-title>
    <v-card-text>
      <div
        ref="chartRef"
        style="width: 100%; height: 600px;"
      />
    </v-card-text>
  </v-card>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'
import { useRouter } from 'vue-router'
import * as echarts from 'echarts'
import { useCourseStore } from '@/stores/courseStore'

const chartRef = ref(null)
let chart = null
const router = useRouter()
const { mathData } = useCourseStore()

// 将数据转换为ECharts树图所需的格式
const convertData = (data, parentPath = '') => {
  if (!data) return []
  
  return data.map((item, index) => {
    // 构建当前节点的路径
    const currentPath = parentPath ? `${parentPath}.${index}` : `${index}`
    
    const result = {
      name: item.name,
      value: item.type,
      nodePath: currentPath, // 保存节点路径用于点击跳转
      itemStyle: getItemStyle(item.type, item.completed),
      tooltip: {
        formatter: (params) => {
          let result = `<div style="font-weight: bold;">${params.name}</div>`
          if (item.description) {
            result += `<div>${item.description}</div>`
          }
          if (item.tags) {
            result += `<div>标签: ${item.tags.join(', ')}</div>`
          }
          result += `<div>学习状态: ${item.completed ? '已完成' : '未完成'}</div>`
          result += `<div style="color:#409EFF;margin-top:5px;">点击节点查看详情</div>`
          return result
        }
      },
    }
    
    if (item.children && item.children.length > 0) {
      result.children = convertData(item.children, currentPath)
    }
    
    return result
  })
}

// 根据节点类型和完成状态设置不同的样式
const getItemStyle = (type, completed) => {
  const colorMap = {
    'chapter': '#5470c6',
    'section': '#91cc75',
    'topic': '#fac858',
    'subtopic': '#ee6666',
    'concept': '#73c0de'
  }
  
  // 如果已完成，使用正常颜色，否则使用淡色
  const baseColor = colorMap[type] || '#9a60b4'
  
  if (completed) {
    return {
      color: baseColor,
      borderColor: '#fff',
      borderWidth: 2
    }
  } else {
    // 未完成的节点使用淡色并添加虚线边框
    return {
      color: baseColor,
      opacity: 0.5,
      borderColor: '#999',
      borderWidth: 1,
      borderType: 'dashed'
    }
  }
}

// 处理节点点击事件
const handleNodeClick = (params) => {
  if (params.data && params.data.nodePath) {
    router.push({
      path: '/node-detail',
      query: {
        path: params.data.nodePath
      }
    })
  }
}

// 初始化图表
const initChart = () => {
  if (!chartRef.value || !mathData.value) return
  
  try {
    // 创建图表实例
    chart = echarts.init(chartRef.value)
    
    const option = {
      tooltip: {
        trigger: 'item',
        triggerOn: 'mousemove'
      },
      series: [
        {
          type: 'tree',
          data: convertData(mathData.value),
          top: '1%',
          left: '7%',
          bottom: '1%',
          right: '20%',
          symbolSize: 10,
          label: {
            position: 'left',
            verticalAlign: 'middle',
            align: 'right',
            fontSize: 12
          },
          leaves: {
            label: {
              position: 'right',
              verticalAlign: 'middle',
              align: 'left'
            }
          },
          emphasis: {
            focus: 'descendant'
          },
          expandAndCollapse: true,
          animationDuration: 550,
          animationDurationUpdate: 750
        }
      ]
    }
    
    chart.setOption(option)
    
    // 添加点击事件监听
    chart.on('click', 'series', handleNodeClick)
    
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
    // 移除事件监听
    chart.off('click')
    chart.dispose()
    window.removeEventListener('resize', chart.resize)
  }
})
</script>

<style scoped>
/* 可以添加自定义样式 */
</style> 