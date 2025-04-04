<template>
  <v-app>
    <!-- 添加导航组件 -->
    <Navigation />
    
    <v-main class="bg-grey-lighten-4">
      <v-container
        fluid
        class="pa-6"
      >
        <v-fade-transition>
          <router-view />
        </v-fade-transition>
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import Navigation from '@/components/Navigation.vue'
</script>

<style>
.v-container {
  max-width: 1280px;
  margin: 0 auto;
}
</style>
