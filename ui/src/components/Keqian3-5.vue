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
  
    <!-- 任务完成情况 -->
    <v-card class="mb-4">
      <v-card-title class="text-h5">
        任务完成情况
      </v-card-title>
      <v-card-text>
        <v-row>
          <v-col
            cols="12"
            md="6"
          >
            <v-card class="pa-3">
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
                  <span class="white--text">{{ Math.ceil(value) }}% (159/162)</span>
                </template>
              </v-progress-linear>
              <div class="caption mt-2">
                159完成，3未完成
              </div>
            </v-card>
          </v-col>
          <v-col
            cols="12"
            md="6"
          >
            <v-card class="pa-3">
              <div class="text-subtitle-1 mb-2">
                任务点完成情况
              </div>
              <v-progress-linear
                model-value="92"
                height="25"
                striped
                color="success"
              >
                <template #default="{ value }">
                  <span class="white--text">{{ Math.ceil(value) }}% (149/162)</span>
                </template>
              </v-progress-linear>
              <div class="caption mt-2">
                149完成，13未完成
              </div>
            </v-card>
          </v-col>
        </v-row>
  
        <v-row class="mt-4">
          <v-col
            cols="12"
            md="6"
          >
            <v-card class="pa-3">
              <div class="text-subtitle-1 mb-2">
                案例解析过程上传
              </div>
              <v-progress-linear
                model-value="76.5"
                height="25"
                striped
                color="info"
              >
                <template #default="{ value }">
                  <span class="white--text">{{ Math.ceil(value) }}% (124/162)</span>
                </template>
              </v-progress-linear>
              <div class="caption mt-2">
                124上传，38未上传
              </div>
            </v-card>
          </v-col>
          <v-col
            cols="12"
            md="6"
          >
            <v-card class="pa-3">
              <div class="text-subtitle-1 mb-2">
                思政交互情况
              </div>
              <v-progress-linear
                model-value="74.1"
                height="25"
                striped
                color="deep-purple"
              >
                <template #default="{ value }">
                  <span class="white--text">{{ Math.ceil(value) }}% (120/162)</span>
                </template>
              </v-progress-linear>
              <div class="caption mt-2">
                120交互，42未交互
              </div>
            </v-card>
          </v-col>
        </v-row>
        <v-row>
          <v-col
            cols="12"
            md="4"
          >
            <v-card class="pa-3">
              <div class="text-subtitle-1 mb-2">
                习题完成情况
              </div>
              <v-row>
                <v-col cols="12">
                  <v-sheet class="pa-2 mb-2">
                    <div class="d-flex align-center">
                      <div class="font-weight-medium flex-grow-1">
                        3.5.1 极值的定义
                      </div>
                      <v-chip
                        color="primary"
                        size="small"
                      >
                        完成率: 93%
                      </v-chip>
                    </div>
                  </v-sheet>
                  <v-sheet class="pa-2 mb-2">
                    <div class="d-flex align-center">
                      <div class="font-weight-medium flex-grow-1">
                        3.5.2 极值与最值的区分
                      </div>
                      <v-chip
                        color="primary"
                        size="small"
                      >
                        完成率: 90%
                      </v-chip>
                    </div>
                  </v-sheet>
                  <v-sheet class="pa-2 mb-2">
                    <div class="d-flex align-center">
                      <div class="font-weight-medium flex-grow-1">
                        3.5.3 极值的必要条件
                      </div>
                      <v-chip
                        color="warning"
                        size="small"
                      >
                        完成率: 35%
                      </v-chip>
                    </div>
                  </v-sheet>
                  <v-sheet class="pa-2 mb-2">
                    <div class="d-flex align-center">
                      <div class="font-weight-medium flex-grow-1">
                        3.5.4 极值计算：第一充分条件
                      </div>
                      <v-chip
                        color="info"
                        size="small"
                      >
                        完成率: 52%
                      </v-chip>
                    </div>
                  </v-sheet>
                  <v-sheet class="pa-2">
                    <div class="d-flex align-center">
                      <div class="font-weight-medium flex-grow-1">
                        3.5.5 极值计算：第二充分条件
                      </div>
                      <v-chip
                        color="info"
                        size="small"
                      >
                        完成率: 61%
                      </v-chip>
                    </div>
                  </v-sheet>
                </v-col>
              </v-row>
            </v-card>
          </v-col>
          <v-col
            cols="12"
            md="8"
          >
            <v-card class="pa-3">
              <div class="text-subtitle-1 mb-4">
                习题完成情况
              </div>
              <v-chart
                class="chart"
                :option="barChartOption"
                autoresize
              />
            </v-card>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  
    <!-- 学习情况分析 -->
    <v-card class="mb-4">
      <v-card-title class="text-h5">
        学习情况分析
      </v-card-title>
      <v-card-text>
        <v-row>
          <v-col
            cols="12"
            md="7"
          >
            <v-card class="pa-4">
              <div class="text-h6 mb-3">
                知识掌握情况
              </div>
              <ul class="ml-3">
                <li class="mb-2">
                  基本理解极值的定义，但有较多学生无法区分极值和最值
                </li>
                <li class="mb-2">
                  基本可以掌握求极值的简单计算问题
                </li>
                <li class="mb-2 red--text">
                  对第一、二充分条件理解不深刻，认为求导就是求极值的方法
                </li>
              </ul>
  
              <div class="text-h6 mb-3 mt-4">
                能力培养分析
              </div>
              <ul class="ml-3">
                <li class="mb-2 orange--text">
                  案例准确率较低
                </li>
                <li class="mb-2">
                  数学软件使用情况见饼状图
                </li>
              </ul>
              
              <div class="text-h6 mb-3 mt-4">
                思政情况
              </div>
              <p>通过与AI的交互，涉及的思政元素主要包含：</p>
              <ul class="ml-3">
                <li class="mb-2">
                  工匠精神 121
                </li>
                <li class="mb-2">
                  科研精神 87
                </li>
                <li class="mb-2">
                  家国情怀 48
                </li>
                <li class="mb-2">
                  生产力 21
                </li>
              </ul>
              <div class="mt-4">
                <v-chart
                  class="chart"
                  :option="radarChartOption"
                  autoresize
                />
                <div class="caption mt-2 text-center">
                  思政元素分析雷达图
                </div>
              </div>
            </v-card>
          </v-col>
          <v-col
            cols="12"
            md="5"
          >
            <v-card class="pa-4">
              <div class="text-h6 mb-3">
                数学软件使用情况
              </div>
              <v-chart
                class="chart"
                :option="pieChartOption"
                autoresize
              />
              <div class="caption mt-4 text-center">
                软件使用情况统计
              </div>
  
              <div class="text-h6 mb-3 mt-6">
                教学优化建议
              </div>
              <ul class="ml-3">
                <li class="mb-2">
                  加强极值与最值概念的区分练习
                </li>
                <li class="mb-2">
                  增加第一、二充分条件的应用案例
                </li>
                <li class="mb-2">
                  提供更多实际应用中的极值问题
                </li>
              </ul>
            </v-card>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </div>
</template>
  
<script setup>
import { ref } from 'vue';
import { use } from 'echarts/core';
import { CanvasRenderer } from 'echarts/renderers';
import { BarChart, PieChart, RadarChart } from 'echarts/charts';
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
  TitleComponent,
  TooltipComponent,
  LegendComponent,
  GridComponent
]);

// 习题完成情况柱状图
const barChartOption = ref({
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    }
  },
  xAxis: {
    type: 'category',
    data: ['第1章', '第2章', '第3章', '第4章', '第5章'],
    axisLabel: {
      interval: 0
    }
  },
  yAxis: {
    type: 'value',
    name: '完成数量'
  },
  series: [
    {
      data: [151, 85, 56, 87, 43],
      type: 'bar',
      barWidth: '40%',
      itemStyle: {
        color: function(params) {
          const colorList = ['#4CAF50', '#2196F3', '#FF9800', '#9C27B0', '#F44336'];
          return colorList[params.dataIndex];
        }
      }
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
</script>
  
<style scoped>
.chart {
  height: 300px;
}
</style>
  