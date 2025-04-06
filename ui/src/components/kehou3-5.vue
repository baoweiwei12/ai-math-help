<!-- eslint-disable vue/no-parsing-error -->
<template>
  <div>
    <v-card class="mb-4">
      <v-card-title class="text-h4 mb-4">
        3.5 极值与最值
      </v-card-title>
      <v-card-text>
        <p class="text-body-1">
          极值与最值是微分学中的重要概念，它们描述了函数在某点附近或整个定义域上的最大值和最小值。
        </p>
      </v-card-text>
    </v-card>
  
    <!-- 左侧：题目完成情况 -->
    <v-row>
      <v-col
        cols="12"
        md="6"
      >
        <v-card class="mb-4">
          <v-card-title class="text-h5">
            题目完成情况
          </v-card-title>
          <v-card-text>
            <div class="d-flex justify-space-between align-center py-2">
              <div class="font-weight-medium">
                3.5.1 极值的定义
              </div>
              <div class="text-right">
                137
              </div>
            </div>
            <div class="d-flex justify-space-between align-center py-2">
              <div class="font-weight-medium">
                3.5.2 极值与最值的区分
              </div>
              <div class="text-right">
                153
              </div>
            </div>
            <div class="d-flex justify-space-between align-center py-2">
              <div class="font-weight-medium">
                3.5.3 极值的必要条件
              </div>
              <div class="text-right">
                148
              </div>
            </div>
            <div class="d-flex justify-space-between align-center py-2">
              <div class="font-weight-medium">
                3.5.4 极值计算：第一充分条件
              </div>
              <div class="text-right">
                160
              </div>
            </div>
            <div class="d-flex justify-space-between align-center py-2">
              <div class="font-weight-medium">
                3.5.5 极值计算：第二充分条件
              </div>
              <div class="text-right">
                157
              </div>
            </div>
            <div class="d-flex justify-end mt-4">
              <span class="font-weight-bold">总计</span>
              <span class="ml-6">263</span>
            </div>
            
            <!-- 题目完成情况折线图 -->
            <div class="mt-4">
              <v-chart
                class="chart"
                :option="lineChartOption"
                autoresize
              />
            </div>
          </v-card-text>
        </v-card>
      </v-col>
  
      <!-- 右侧：任务完成情况 -->
      <v-col
        cols="12"
        md="6"
      >
        <v-card class="mb-4">
          <v-card-title class="text-h5">
            任务完成情况
          </v-card-title>
          <v-card-text>
            <div class="mb-4">
              <div class="text-subtitle-1 mb-2">
                慕课完成情况
              </div>
              <v-progress-linear
                model-value="98.1"
                height="25"
                striped
                color="primary"
              >
                <template #default="{ value }">
                  <span class="white--text">{{ Math.ceil(value) }}%</span>
                </template>
              </v-progress-linear>
              <div class="d-flex justify-space-between mt-1">
                <span>159通过</span>
                <span>3未完成</span>
              </div>
            </div>
  
            <div class="mb-4">
              <div class="text-subtitle-1 mb-2">
                正确执行情况
              </div>
              <v-progress-linear
                model-value="76.5"
                height="25"
                striped
                color="success"
              >
                <template #default="{ value }">
                  <span class="white--text">{{ Math.ceil(value) }}%</span>
                </template>
              </v-progress-linear>
              <div class="d-flex justify-space-between mt-1">
                <span>定力加分92</span>
                <span>错误扣70</span>
              </div>
            </div>
  
            <div class="mb-4">
              <div class="text-subtitle-1 mb-2">
                数学软件使用情况
              </div>
              <v-chart
                class="chart"
                :option="pieChartOption"
                autoresize
              />
            </div>
  
            <div>
              <div class="text-subtitle-1 mb-2">
                心得感悟
              </div>
              <v-chart
                class="chart"
                :option="radarChartOption"
                autoresize
              />
              <div class="caption mt-2 text-center">
                思政元素分析雷达图
              </div>
            </div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>
  
<script setup>
import { ref, onMounted } from 'vue';
import { use } from 'echarts/core';
import { CanvasRenderer } from 'echarts/renderers';
import { BarChart, PieChart, RadarChart, LineChart } from 'echarts/charts';
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent
} from 'echarts/components';
import VChart from 'vue-echarts';

use([
  CanvasRenderer,
  BarChart,
  PieChart,
  RadarChart,
  LineChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent
]);

// 题目完成情况折线图
const lineChartOption = ref({
  tooltip: {
    trigger: 'axis'
  },
  xAxis: {
    type: 'category',
    data: ['3.5.1', '3.5.2', '3.5.3', '3.5.4', '3.5.5']
  },
  yAxis: {
    type: 'value',
    name: '完成人数'
  },
  series: [
    {
      data: [137, 153, 148, 160, 157],
      type: 'line',
      smooth: true,
      lineStyle: {
        color: '#4CAF50',
        width: 3
      },
      symbolSize: 8
    }
  ]
});

// 数学软件使用情况饼图
const pieChartOption = ref({
  tooltip: {
    trigger: 'item',
    formatter: '{b}: {c}%'
  },
  legend: {
    orient: 'vertical',
    left: 'left',
  },
  series: [
    {
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
          fontSize: '16',
          fontWeight: 'bold'
        }
      },
      labelLine: {
        show: false
      },
      data: [
        { value: 53, name: 'Matlab' },
        { value: 18, name: 'R' },
        { value: 23, name: 'Python' },
        { value: 5, name: 'Mathematics' },
        { value: 1, name: 'Mworks' }
      ]
    }
  ]
});

// 思政元素雷达图
const radarChartOption = ref({
  tooltip: {},
  radar: {
    indicator: [
      { name: '工匠精神', max: 150 },
      { name: '科研精神', max: 150 },
      { name: '家国情怀', max: 150 },
      { name: '生产力', max: 150 }
    ]
  },
  series: [
    {
      type: 'radar',
      data: [
        {
          value: [121, 87, 48, 21],
          name: '思政元素',
          areaStyle: {
            color: 'rgba(76, 175, 80, 0.6)'
          },
          lineStyle: {
            width: 2
          }
        }
      ]
    }
  ]
});

onMounted(() => {
  // 初始化页面逻辑
});
</script>
  
<style scoped>
.chart {
  height: 300px;
}
</style>
  