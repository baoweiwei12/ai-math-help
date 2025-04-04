<template>
  <div>
    <v-card
      class="mb-6 rounded-lg"
      elevation="2"
    >
      <v-img
        height="180"
        src="https://img.freepik.com/free-vector/gradient-geometric-science-education-twitter-header_23-2149486798.jpg?w=1380&t=st=1708956636~exp=1708957236~hmac=adc92d8d0e88cd04e1fc67b8b3fb3b8d8abedfa1f9af50fe84c4dac5ebf90688"
        cover
        class="bg-blue"
      >
        <div class="d-flex flex-column fill-height justify-end pa-6 bg-black bg-opacity-30">
          <h1 class="text-h3 text-white font-weight-bold mb-2">
            高等数学课程导航
          </h1>
          <p class="text-white text-subtitle-1">
            探索数学的奥秘，掌握高等数学的核心概念
          </p>
        </div>
      </v-img>
      <v-card-text class="pa-6">
        <p class="text-body-1">
          欢迎使用高等数学课程导航系统。请从左侧导航栏选择您想要学习的章节内容。
        </p>
        <p class="text-body-1 mt-4">
          本系统涵盖了高等数学的主要内容，包括向量代数、多元函数微分学、重积分、曲线积分和曲面积分以及无穷级数等内容。
        </p>
      </v-card-text>
    </v-card>

    <v-row>
      <v-col
        cols="12"
        sm="6"
        lg="4"
      >
        <v-card
          height="100%"
          class="rounded-lg"
          elevation="1"
          to="/study"
          link
        >
          <v-img
            height="140"
            src="https://img.freepik.com/free-vector/business-data-analysis-concept_23-2148201652.jpg?w=1380&t=st=1708956839~exp=1708957439~hmac=62f28d145e6981632e6931fc173f41fd70ed5f2b207da2ca0b3f42b8b96a76ab"
            class="bg-blue-grey-darken-1"
            cover
          >
            <div class="d-flex fill-height align-end pa-4 bg-black bg-opacity-30">
              <h3 class="text-h5 text-white font-weight-bold">
                学习统计分析
              </h3>
            </div>
          </v-img>
          <v-card-text>
            <p class="text-body-2">
              查看您的学习数据统计、进度分析和知识图谱。通过数据可视化了解您的学习情况，制定更有效的学习计划。
            </p>
          </v-card-text>
          <v-card-actions>
            <v-btn
              variant="text"
              color="primary"
              to="/study"
              class="ml-auto"
            >
              查看详情
              <v-icon end>
                mdi-arrow-right
              </v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
      
      <v-col
        cols="12"
        sm="6"
        lg="4"
      >
        <v-card
          height="100%"
          class="rounded-lg"
          elevation="1"
        >
          <v-card-title class="text-primary d-flex align-center">
            <v-icon
              class="mr-2"
              icon="mdi-history"
              size="small"
            />
            最近学习
          </v-card-title>
          <v-divider />
          <v-card-text>
            <v-list lines="two">
              <v-list-item
                title="9.5 方向导数和梯度"
                subtitle="学习如何计算函数在各个方向上的变化率"
                to="/chapter9/9.5"
                prepend-icon="mdi-book-open-page-variant"
                append-icon="mdi-chevron-right"
                class="rounded-lg mb-2"
              />
            </v-list>
          </v-card-text>
        </v-card>
      </v-col>
      
      <v-col
        cols="12"
        sm="6"
        lg="4"
      >
        <v-card
          height="100%"
          class="rounded-lg"
          elevation="1"
        >
          <v-card-title class="text-primary d-flex align-center">
            <v-icon
              class="mr-2"
              icon="mdi-star"
              size="small"
            />
            推荐学习
          </v-card-title>
          <v-divider />
          <v-card-text>
            <v-list lines="two">
              <v-list-item
                title="9.1 多元函数的基本概念"
                subtitle="多元函数的定义与几何意义"
                to="/chapter9/9.1"
                prepend-icon="mdi-book-open-page-variant"
                append-icon="mdi-chevron-right"
                class="rounded-lg mb-2"
              />
              <v-list-item
                title="9.2 偏导数与全微分"
                subtitle="学习偏导数和全微分的基本概念"
                to="/chapter9/9.2"
                prepend-icon="mdi-book-open-page-variant"
                append-icon="mdi-chevron-right"
                class="rounded-lg"
              />
            </v-list>
          </v-card-text>
        </v-card>
      </v-col>
      
      <v-col
        cols="12"
        sm="6"
        lg="6"
      >
        <v-card
          height="100%"
          class="rounded-lg"
          elevation="1"
        >
          <v-card-title class="text-primary d-flex align-center">
            <v-icon
              class="mr-2"
              icon="mdi-chart-arc"
              size="small"
            />
            学习进度
          </v-card-title>
          <v-divider />
          <v-card-text>
            <div class="text-center py-6">
              <v-progress-circular
                :model-value="30"
                :size="100"
                :width="12"
                color="primary"
                class="mb-4"
              >
                30%
              </v-progress-circular>
              <h3 class="text-h6 font-weight-bold">
                已完成 3/10 章节
              </h3>
              <p class="text-subtitle-2 text-medium-emphasis mt-2">
                继续努力，坚持学习！
              </p>
            </div>
          </v-card-text>
        </v-card>
      </v-col>

      <v-col
        cols="12"
        sm="6"
        lg="6"
      >
        <v-card
          class="rounded-lg"
          elevation="1"
        >
          <v-card-title class="text-primary d-flex align-center">
            <v-icon
              class="mr-2"
              icon="mdi-calendar-check"
              size="small"
            />
            学习计划
          </v-card-title>
          <v-divider />
          <v-card-text>
            <v-timeline
              density="compact"
              align="start"
            >
              <v-timeline-item
                dot-color="primary"
                size="small"
              >
                <div class="mb-4">
                  <div class="text-subtitle-1 font-weight-bold">
                    第八章 向量代数与空间解析几何
                  </div>
                  <div class="text-body-2">
                    完成日期: 2023-03-15
                  </div>
                </div>
              </v-timeline-item>
              
              <v-timeline-item
                dot-color="primary"
                size="small"
              >
                <div class="mb-4">
                  <div class="text-subtitle-1 font-weight-bold">
                    第九章 多元函数的微分法及其应用
                  </div>
                  <div class="text-body-2">
                    计划日期: 2023-04-01
                  </div>
                </div>
              </v-timeline-item>
              
              <v-timeline-item
                dot-color="grey"
                size="small"
              >
                <div class="mb-4">
                  <div class="text-subtitle-1 font-weight-bold">
                    第十章 重积分
                  </div>
                  <div class="text-body-2">
                    计划日期: 2023-04-15
                  </div>
                </div>
              </v-timeline-item>
            </v-timeline>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script setup>

</script>

<style scoped>
.v-list-item {
  transition: background-color 0.2s;
}
.v-list-item:hover {
  background-color: rgba(25, 118, 210, 0.05);
}
</style>
