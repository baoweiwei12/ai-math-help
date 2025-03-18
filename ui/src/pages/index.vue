<template>
  <v-container>
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
          <MathTreeChart />
        </v-col>
      </v-row>
      <v-row>
        <v-col
          cols="12"
          md="6"
        >
          <MathPieChart />
        </v-col>
        <v-col
          cols="12"
          md="6"
        >
          <MathTagsChart />
        </v-col>
      </v-row>
      
      <v-row>
        <v-col cols="12">
          <MathProgressChart />
        </v-col>
      </v-row>
    </template>
  </v-container>
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
/* 可以添加自定义样式 */
</style>
