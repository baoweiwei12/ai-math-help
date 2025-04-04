<template>
  <div>
    <v-card>
      <v-card-title class="text-h4 mb-4">
        9.6 多元函数微分学的应用
      </v-card-title>
      <v-card-text>
        <p class="text-body-1">
          多元函数微分学在科学和工程中有广泛的应用，本节将介绍多元函数微分学在各个领域中的典型应用。
        </p>
        
        <div class="mt-6">
          <h3 class="text-h5 mb-3">
            几何应用
          </h3>
          <p class="text-body-1">
            多元函数微分学可以用来研究空间曲面的性质，例如切平面、法线、曲率等。
          </p>
          <p class="text-body-2 mt-2">
            <strong>切平面方程：</strong> 设曲面z=f(x,y)在点P(x0,y0,z0)处有连续的偏导数，则曲面在该点的切平面方程为：
          </p>
          <p class="text-h6 my-4 text-center">
            z - z0 = f_x(x0,y0)(x - x0) + f_y(x0,y0)(y - y0)
          </p>
          <p class="text-body-2 mt-2">
            <strong>法线方程：</strong> 曲面z=f(x,y)在点P(x0,y0,z0)处的法线方程为：
          </p>
          <p class="text-h6 my-4 text-center">
            (x - x0)/f_x(x0,y0) = (y - y0)/f_y(x0,y0) = (z - z0)/(-1)
          </p>
        </div>

        <div class="mt-6">
          <h3 class="text-h5 mb-3">
            物理应用
          </h3>
          <p class="text-body-1">
            在物理学中，多元函数微分学用于描述各种物理量的变化率和运动规律。
          </p>
          <p class="text-body-2 mt-2">
            <strong>温度梯度：</strong> 温度场T(x,y,z)的梯度grad T给出了温度变化最快的方向和变化率。
          </p>
          <p class="text-body-2 mt-2">
            <strong>电场强度：</strong> 电势函数φ(x,y,z)的负梯度-grad φ给出了电场强度的方向和大小。
          </p>
        </div>

        <div class="mt-6">
          <h3 class="text-h5 mb-3">
            经济学应用
          </h3>
          <p class="text-body-1">
            在经济学中，多元函数微分学用于分析生产函数、效用函数等。
          </p>
          <p class="text-body-2 mt-2">
            <strong>生产函数：</strong> 设Q=f(K,L)为生产函数，其中K表示资本，L表示劳动力，Q表示产量。则偏导数∂Q/∂K表示资本的边际产量，∂Q/∂L表示劳动力的边际产量。
          </p>
          <p class="text-body-2 mt-2">
            <strong>效用函数：</strong> 设U=U(x,y)为消费者的效用函数，其中x,y表示两种商品的消费量。则偏导数∂U/∂x和∂U/∂y表示边际效用。
          </p>
        </div>

        <div class="mt-6">
          <h3 class="text-h5 mb-3">
            优化问题
          </h3>
          <p class="text-body-1">
            多元函数微分学为解决各种优化问题提供了理论基础和方法。例如：
          </p>
          <p class="text-body-2 mt-2">
            <strong>无约束优化：</strong> 求函数f(x,y)的极值，可通过求解方程组f_x=0, f_y=0，再利用二阶导数判别。
          </p>
          <p class="text-body-2 mt-2">
            <strong>约束优化：</strong> 求函数f(x,y)在约束条件g(x,y)=0下的极值，可使用拉格朗日乘数法。
          </p>
        </div>
      </v-card-text>
    </v-card>
  </div>
</template>

<script setup>
// 页面逻辑
</script>

<style scoped>
/* 页面样式 */
</style> 