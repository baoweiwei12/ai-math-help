<template>
  <div>
    <v-card
      class="mb-6 rounded-lg"
      elevation="2"
    >
      <v-card-title class="text-h4 d-flex align-center">
        <v-icon
          class="mr-3"
          icon="mdi-chart-box"
          size="large"
        />
        学习统计分析
        <v-spacer />
        <v-btn 
          color="primary" 
          prepend-icon="mdi-refresh"
          :loading="loading"
          @click="loadData"
        >
          刷新数据
        </v-btn>
      </v-card-title>
      <v-card-subtitle class="ml-12 text-body-1 mt-1">
        通过数据可视化了解您的学习情况，制定更有效的学习计划
      </v-card-subtitle>
    </v-card>

    <v-alert
      v-if="error"
      type="error"
      closable
      class="mb-4"
    >
      {{ error }}
    </v-alert>
    
    <v-row v-if="loading">
      <v-col
        cols="12"
        class="d-flex justify-center align-center"
        style="height: 300px;"
      >
        <v-progress-circular
          indeterminate
          color="primary"
          size="64"
        />
      </v-col>
    </v-row>
    
    <template v-else>
      <v-row>
        <v-col cols="12">
          <v-card
            class="rounded-lg"
            elevation="1"
          >
            <v-card-title class="text-primary d-flex align-center">
              <v-icon
                class="mr-2"
                icon="mdi-graph"
                size="small"
              />
              知识图谱
            </v-card-title>
            <v-divider />
            <v-card-text class="pa-4">
              <MathTreeChart />
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
      
      <v-row>
        <v-col
          cols="12"
          md="6"
        >
          <v-card
            class="rounded-lg"
            elevation="1"
            height="100%"
          >
            <v-card-title class="text-primary d-flex align-center">
              <v-icon
                class="mr-2"
                icon="mdi-chart-pie"
                size="small"
              />
              学习分布
            </v-card-title>
            <v-divider />
            <v-card-text class="pa-4">
              <MathPieChart />
            </v-card-text>
          </v-card>
        </v-col>
        
        <v-col
          cols="12"
          md="6"
        >
          <v-card
            class="rounded-lg"
            elevation="1"
            height="100%"
          >
            <v-card-title class="text-primary d-flex align-center">
              <v-icon
                class="mr-2"
                icon="mdi-tag-multiple"
                size="small"
              />
              知识点掌握情况
            </v-card-title>
            <v-divider />
            <v-card-text class="pa-4">
              <MathTagsChart />
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
      
      <v-row>
        <v-col cols="12">
          <v-card
            class="rounded-lg"
            elevation="1"
          >
            <v-card-title class="text-primary d-flex align-center">
              <v-icon
                class="mr-2"
                icon="mdi-trending-up"
                size="small"
              />
              学习进度趋势
            </v-card-title>
            <v-divider />
            <v-card-text class="pa-4">
              <MathProgressChart />
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </template>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import MathTreeChart from '@/components/MathTreeChart.vue'
import MathPieChart from '@/components/MathPieChart.vue'
import MathTagsChart from '@/components/MathTagsChart.vue'
import MathProgressChart from '@/components/MathProgressChart.vue'
import { useCourseStore } from '@/stores/courseStore'

// 获取课程数据存储
const { loading, error, loadData } = useCourseStore()

// 在组件挂载时加载数据
onMounted(() => {
  loadData()
})
</script>

<style scoped>
.v-card {
  transition: transform 0.3s, box-shadow 0.3s;
}
.v-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1) !important;
}
</style>
