<template>
  <div>
    <v-card>
      <v-card-title class="text-h4 mb-4">
        9.3 多元复合函数与隐函数求导法则
      </v-card-title>
      <v-card-text>
        <p class="text-body-1">
          在实际问题中，我们经常遇到复合函数和隐函数，本节将讨论这些特殊函数的求导法则。
        </p>
        
        <div class="mt-6">
          <h3 class="text-h5 mb-3">
            多元复合函数求导法则
          </h3>
          <p class="text-body-1">
            设z=f(u,v)，而u=u(x,y)，v=v(x,y)都有一阶连续偏导数，则复合函数z=f[u(x,y),v(x,y)]关于x的偏导数为：
          </p>
          <p class="text-h6 my-4 text-center">
            ∂z/∂x = (∂f/∂u)·(∂u/∂x) + (∂f/∂v)·(∂v/∂x)
          </p>
          <p class="text-body-1">
            同理，关于y的偏导数为：
          </p>
          <p class="text-h6 my-4 text-center">
            ∂z/∂y = (∂f/∂u)·(∂u/∂y) + (∂f/∂v)·(∂v/∂y)
          </p>
        </div>

        <div class="mt-6">
          <h3 class="text-h5 mb-3">
            隐函数求导法则
          </h3>
          <p class="text-body-1">
            设F(x,y,z) = 0确定了z关于x,y的函数z=f(x,y)，且F在点(x₀,y₀,z₀)的某邻域内具有连续的偏导数，且F_z(x₀,y₀,z₀)≠0，则z=f(x,y)在点(x₀,y₀)的邻域内有连续的偏导数，且：
          </p>
          <p class="text-h6 my-4 text-center">
            ∂z/∂x = -F_x/F_z
          </p>
          <p class="text-h6 my-4 text-center">
            ∂z/∂y = -F_y/F_z
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