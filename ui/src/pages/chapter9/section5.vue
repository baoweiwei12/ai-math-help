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
                        9.5.1 方向导数的定义
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
                        9.5.2 梯度的定义
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
                        9.5.3 方向导数与偏导数区分
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
                        9.5.4 方向导数的计算
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
                        9.5.5 梯度的计算
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
                  基本理解方向导数梯度的定义
                </li>
                <li class="mb-2">
                  基本可以利用方向导数和梯度的公式进行简单计算
                </li>
                <li class="mb-2 red--text">
                  较多学生出现将偏导数和方向导数定义混淆的问题
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
                  数学软件使用情况如右图所示
                </li>
              </ul>
            </v-card>
          </v-col>
          <v-col
            cols="12"
            md="5"
          >
            <v-card class="pa-3">
              <div class="text-subtitle-1 mb-4">
                数学软件使用情况
              </div>
              <v-chart
                class="chart"
                :option="pieChartOption"
                autoresize
              />
            </v-card>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>

    <!-- 思政元素分析 -->
    <v-card class="mb-4">
      <v-card-title class="text-h5">
        思政元素分析
      </v-card-title>
      <v-card-text>
        <v-row>
          <v-col cols="12">
            <div class="text-body-1 mb-3">
              通过与AI的交互，涉及的思政元素主要包含：
            </div>
          </v-col>
          <v-col cols="12">
            <v-chart
              class="chart"
              style="height: 400px"
              :option="radarChartOption"
              autoresize
            />
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>

    <!-- 教学优化建议 -->
    <v-card>
      <v-card-title class="text-h5">
        教学优化建议
      </v-card-title>
      <v-card-text>
        <v-row>
          <v-col cols="12">
            <v-card
              class="pa-4"
              color="light-blue-lighten-5"
            >
              <div class="text-h6 mb-3">
                知识点讲解优化
              </div>
              <ul class="ml-3">
                <li class="mb-2">
                  加强方向导数与偏导数的区分，通过更直观的几何解释帮助学生理解两者的本质区别
                </li>
                <li class="mb-2">
                  增加梯度的物理意义解释，将抽象概念与具体实际问题结合
                </li>
                <li class="mb-2">
                  针对习题9.5.3的低完成率，设计更多的辨析题帮助学生巩固概念
                </li>
              </ul>

              <div class="text-h6 mb-3 mt-4">
                案例教学改进
              </div>
              <ul class="ml-3">
                <li class="mb-2">
                  围绕方向导数在物理、经济等领域的应用设计更多直观案例
                </li>
                <li class="mb-2">
                  增加Matlab软件实践环节，帮助学生可视化理解梯度场和方向导数
                </li>
                <li class="mb-2">
                  引导学生将Python和R等软件应用到方向导数计算中，提高计算能力
                </li>
              </ul>

              <div class="text-h6 mb-3 mt-4">
                思政元素融入
              </div>
              <ul class="ml-3">
                <li class="mb-2">
                  结合新质生产力的主题，可以设计更多的智能制造相关案例，展示方向导数和梯度在优化算法中的应用
                </li>
                <li class="mb-2">
                  结合家国情怀元素，增加国产数学软件的应用示例，培养学生的民族自信
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
import { ref, onMounted } from 'vue';
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
    data: ['9.5.1', '9.5.2', '9.5.3', '9.5.4', '9.5.5'],
    axisLabel: {
      interval: 0
    }
  },
  yAxis: {
    type: 'value',
    name: '完成人数'
  },
  series: [
    {
      data: [151, 146, 56, 85, 99],
      type: 'bar',
      itemStyle: {
        color: function (params) {
          // 根据数值设置不同颜色
          const colorList = ['#4CAF50', '#4CAF50', '#FF5722', '#2196F3', '#FF9800'];
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
        { value: 53, name: 'Matlab' },
        { value: 18, name: 'R' },
        { value: 23, name: 'Python' },
        { value: 5, name: 'Mathematics' },
        { value: 1, name: 'Mworks' }
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

// 思政元素雷达图
const radarChartOption = ref({
  tooltip: {
    trigger: 'item'
  },
  radar: {
    indicator: [
      { name: '新质生产力', max: 150 },
      { name: '家国情怀', max: 150 },
      { name: '追求真理', max: 150 },
      { name: '生态保护意识', max: 150 }
    ],
    radius: 130
  },
  series: [
    {
      type: 'radar',
      data: [
        {
          value: [121, 87, 48, 21],
          name: '思政元素覆盖',
          areaStyle: {
            color: 'rgba(76, 175, 80, 0.6)'
          },
          lineStyle: {
            color: '#4CAF50'
          },
          itemStyle: {
            color: '#4CAF50'
          }
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
