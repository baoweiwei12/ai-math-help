<!-- eslint-disable vue/no-parsing-error -->
<template>
  <div>
    <v-card class="mb-4">
      <v-card-title class="text-h4 mb-4">
        9.5 方向导数与梯度
      </v-card-title>
      <v-card-text>
        <p class="text-body-1">
          方向导数与梯度是多元微分学中的重要概念，它们描述了多元函数在各个方向上的变化率及变化最快的方向。
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
                9.5.1 方向导数的定义
              </div>
              <div class="text-right">
                137
              </div>
            </div>
            <div class="d-flex justify-space-between align-center py-2">
              <div class="font-weight-medium">
                9.5.2 方向导数的简单计算
              </div>
              <div class="text-right">
                153
              </div>
            </div>
            <div class="d-flex justify-space-between align-center py-2">
              <div class="font-weight-medium">
                9.5.3 方向导数的复杂计算
              </div>
              <div class="text-right">
                148
              </div>
            </div>
            <div class="d-flex justify-space-between align-center py-2">
              <div class="font-weight-medium">
                9.5.4 方向导数与梯度偏导数的关系
              </div>
              <div class="text-right">
                160
              </div>
            </div>
            <div class="d-flex justify-space-between align-center py-2">
              <div class="font-weight-medium">
                9.5.5 梯度的定义
              </div>
              <div class="text-right">
                157
              </div>
            </div>
            <div class="d-flex justify-space-between align-center py-2">
              <div class="font-weight-medium">
                9.5.6 梯度的简单计算
              </div>
              <div class="text-right">
                155
              </div>
            </div>
            <div class="d-flex justify-space-between align-center py-2">
              <div class="font-weight-medium">
                9.5.7 梯度的复杂计算
              </div>
              <div class="text-right">
                149
              </div>
            </div>
            <div class="d-flex justify-space-between align-center py-2">
              <div class="font-weight-medium">
                9.5.8 梯度与梯度的复合的求导方法
              </div>
              <div class="text-right">
                140
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
                <span>160通过</span>
                <span>2未完成</span>
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
    data: ['9.5.1', '9.5.2', '9.5.3', '9.5.4', '9.5.5', '9.5.6', '9.5.7', '9.5.8']
  },
  yAxis: {
    type: 'value',
    name: '完成人数'
  },
  series: [
    {
      data: [137, 153, 148, 160, 157, 155, 149, 140],
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
   formatter: '{b}: {c} ({d}%)'
  },
  legend: {
   orient: 'vertical',
   left: 'left',
  },
  series: [
   {
    name: '软件使用情况',
    type: 'pie',
    radius: '70%',
    data: [
     { value: 50, name: 'Matlab' },
     { value: 11, name: 'R' },
     { value: 30, name: 'Python' },
     { value: 5, name: 'Mathematics' },
     { value: 4, name: 'Mworks' }
    ],
    emphasis: {
     itemStyle: {
      shadowBlur: 10,
      shadowOffsetX: 0,
      shadowColor: 'rgba(0, 0, 0, 0.5)'
     }
    }
   }
  ]
 });


// 心得感悟雷达图
const radarChartOption = ref({
  tooltip: {
    trigger: 'item'
  },
  radar: {
    indicator: [
      { name: '生态文明建设', max: 150 },
      { name: '勇攀高峰', max: 150 },
      { name: '不破不立', max: 150 },
      { name: '新质生产力', max: 150 },
      { name: '谋定后动', max: 150 }
    ],
    radius: 120
  },
  series: [
    {
      type: 'radar',
      data: [
        {
          value: [138, 142, 138, 119, 87],
          name: '思政元素覆盖',
          areaStyle: {
            color: 'rgba(76, 175, 80, 0.6)'
          },
          lineStyle: {
            color: '#4CAF50',
            width: 2
          },
          symbolSize: 6
        }
      ]
    }
  ]
});

onMounted(() => {
  // 页面加载时的逻辑
});
</script>
  
<style scoped>
.chart {
  height: 300px;
}
</style>
  