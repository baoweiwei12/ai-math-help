<!-- eslint-disable vue/no-parsing-error -->
<template>
  <div>
    <v-card>
      <v-card-title class="text-h4 mb-4">
        9.4 多元函数极值及其应用
      </v-card-title>
      <v-card-text>
        <p class="text-body-1">
          多元函数的极值问题是微分学的重要应用之一，本节将介绍多元函数极值的求法及其在实际问题中的应用。
        </p>
        
        <div class="mt-6">
          <h3 class="text-h5 mb-3">
            多元函数极值的必要条件
          </h3>
          <p class="text-body-1">
            设二元函数z=f(x,y)在点(x0,y0)处可微，如果z=f(x,y)在点(x0,y0)处取得极值，则：
          </p>
          <p class="text-h6 my-4 text-center">
            f_x(x0,y0) = 0, f_y(x0,y0) = 0
          </p>
          <p class="text-body-1">
            满足上述条件的点称为函数的驻点或稳定点。
          </p>
        </div>

        <div class="mt-6">
          <h3 class="text-h5 mb-3">
            多元函数极值的充分条件
          </h3>
          <p class="text-body-1">
            设二元函数z=f(x,y)在点(x0,y0)的某邻域内有二阶连续偏导数，且在点(x0,y0)处：
          </p>
          <p class="text-body-1">
            f_x(x0,y0) = 0, f_y(x0,y0) = 0
          </p>
          <p class="text-body-1 mt-2">
            令 A = f_xx(x0,y0), B = f_xy(x0,y0), C = f_yy(x0,y0)，记判别式 Δ = AC - B<sup>2</sup>，则：
          </p>
          <ul class="ml-6 mt-2">
            <li>若Δ > 0且A < 0，则f(x,y)在点(x0,y0)处取得极大值</li>
            <li>若Δ > 0且A > 0，则f(x,y)在点(x0,y0)处取得极小值</li>
            <li>若Δ < 0，则f(x,y)在点(x0,y0)处不取得极值</li>
            <li>若Δ = 0，则需要进一步讨论</li>
          </ul>
        </div>

        <div class="mt-6">
          <h3 class="text-h5 mb-3">
            条件极值
          </h3>
          <p class="text-body-1">
            多元函数在满足一定约束条件下的极值问题，可以通过拉格朗日乘数法求解。设求函数z=f(x,y)在约束条件φ(x,y)=0下的极值，可构造拉格朗日函数：
          </p>
          <p class="text-h6 my-4 text-center">
            L(x,y,λ) = f(x,y) - λφ(x,y)
          </p>
          <p class="text-body-1">
            则所求极值点为方程组：
          </p>
          <p class="text-h6 my-4 text-center">
            ∂L/∂x = 0, ∂L/∂y = 0, ∂L/∂λ = 0
          </p>
          <p class="text-body-1">
            的解。
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