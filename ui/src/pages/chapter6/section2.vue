<template>
  <div>
    <v-card>
      <v-card-title class="text-h4 mb-4">
        9.2 偏导数与全微分
      </v-card-title>
      <v-card-text>
        <p class="text-body-1">
          在多元函数微分学中，偏导数和全微分是重要的基本概念。通过这些概念，我们可以研究多元函数的局部性质。
        </p>
        
        <div class="mt-6">
          <h3 class="text-h5 mb-3">
            偏导数的定义
          </h3>
          <p class="text-body-1">
            对于二元函数z=f(x,y)，当y固定而x变化时，z就是x的一元函数，这时得到的导数叫做函数f关于x的偏导数，记作f_x或∂f/∂x或∂z/∂x；
            类似地，当x固定而y变化时，得到的导数叫做函数f关于y的偏导数，记作f_y或∂f/∂y或∂z/∂y。
          </p>
          <p class="text-h6 my-4 text-center">
            f_x(x₀,y₀) = lim[h→0] [f(x₀+h,y₀) - f(x₀,y₀)]/h
          </p>
          <p class="text-h6 my-4 text-center">
            f_y(x₀,y₀) = lim[h→0] [f(x₀,y₀+h) - f(x₀,y₀)]/h
          </p>
        </div>

        <div class="mt-6">
          <h3 class="text-h5 mb-3">
            全微分的定义
          </h3>
          <p class="text-body-1">
            设函数z=f(x,y)在点(x,y)的某邻域内有定义，若函数的全增量Δz=f(x+Δx,y+Δy)-f(x,y)可以表示为：
          </p>
          <p class="text-h6 my-4 text-center">
            Δz = A·Δx + B·Δy + o(ρ)
          </p>
          <p class="text-body-1">
            其中ρ=√[(Δx)² + (Δy)²]，且A,B仅与x,y有关，而与Δx,Δy无关，则称函数f(x,y)在点(x,y)处可微，并称A·Δx+B·Δy为函数在该点的全微分，记作df或dz。
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