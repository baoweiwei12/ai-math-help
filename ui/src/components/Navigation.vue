<template>
  <v-navigation-drawer
    v-model="drawer"
    :rail="rail"
    permanent
    :width="280"
    class="navigation-drawer"
    @click="rail = false"
  >
    <!-- 导航栏顶部 -->
    <div class="nav-header d-flex align-center">
      <v-avatar
        color="white"
        class="nav-logo mr-2"
        size="32"
      >
        <v-icon color="primary">
          mdi-school
        </v-icon>
      </v-avatar>
      <span
        v-if="!rail"
        class="nav-title"
      >课程目录</span>
      <v-spacer />
      <v-btn
        v-if="!rail"
        icon
        variant="text"
        color="white"
        @click.stop="rail = !rail"
      >
        <v-icon>mdi-chevron-left</v-icon>
      </v-btn>
    </div>
    
    <v-divider />

    <!-- 导航菜单 -->
    <v-list
      density="compact"
      nav
    >
      <!-- 对于没有子菜单的直接导航项 -->
      <v-list-item
        v-for="item in navItems.filter(item => item.to && !item.children?.length)"
        :key="item.key"
        :to="item.to"
        :title="item.title"
        :prepend-icon="item.icon"
        class="main-nav-title"
        :class="{ 'active-item': isActive(item.to) }"
      />

      <!-- 对于有子菜单的导航项 -->
      <template
        v-for="item in navItems.filter(item => item.children?.length > 0 || !item.to)"
        :key="item.key"
      >
        <!-- 主导航项 -->
        <v-list-group
          v-model="item.isOpen"
          :value="item.isOpen"
          class="main-nav-item"
        >
          <template #activator="{ props }">
            <v-list-item
              v-bind="props"
              :title="item.title"
              :prepend-icon="item.icon || 'mdi-book-open-variant'"
              class="main-nav-title"
              :class="{ 'active-chapter': activeChapter === item.key }"
              :to="item.to"
              @click="toggleChapter(item)"
            />
          </template>

          <!-- 子导航项 -->
          <v-list-item
            v-for="child in item.children"
            :key="child.key"
            :to="child.to"
            :title="child.title"
            class="sub-nav-item"
            :class="{ 'active-item': isActive(child.to) }"
            density="compact"
          />
        </v-list-group>
      </template>
    </v-list>
  </v-navigation-drawer>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import { navigationData } from '@/data/navigation'

const route = useRoute()
const rail = ref(false)
const drawer = ref(true)
const activeChapter = ref('')

// 创建一个本地响应式副本用于UI交互
const navItems = computed(() => {
  return navigationData.map(item => ({...item}))
})

// 检查当前路由是否激活
const isActive = (path) => {
  return route.path === path
}

// 根据当前路由确定激活的章节
const determineActiveChapter = () => {
  const path = route.path
  for (const item of navigationData) {
    // 检查当前路由是否匹配这个父项
    if (item.to && path === item.to) {
      activeChapter.value = item.key
      return
    }
    
    // 检查子项
    if (item.children && item.children.length > 0) {
      for (const child of item.children) {
        if (child.to === path) {
          activeChapter.value = item.key
          item.isOpen = true
          return
        }
      }
    }
  }
}

// 切换章节的展开/收起状态
const toggleChapter = (item) => {
  activeChapter.value = item.key
  // 如果有to属性但没有点击to，就切换展开状态
  if (!item.to) {
    item.isOpen = !item.isOpen
  }
}

// 初始化时确定激活的章节
determineActiveChapter()
</script>

<style scoped>
.navigation-drawer {
  background-color: #1565C0;
  color: white;
}

.nav-header {
  padding: 16px;
  background-color: rgba(0, 0, 0, 0.1);
}

.nav-title {
  font-size: 1.2rem;
  font-weight: bold;
  color: white;
}

.nav-logo {
  min-width: 32px;
}

.main-nav-title {
  color: white !important;
  font-weight: bold;
  font-size: 1rem;
}

.active-chapter {
  background-color: rgba(255, 255, 255, 0.1);
}

.sub-nav-item {
  padding-left: 20px;
  color: rgba(255, 255, 255, 0.9) !important;
  transition: all 0.3s ease;
}

.sub-nav-item:hover {
  background-color: rgba(255, 255, 255, 0.15) !important;
}

.active-item {
  background-color: white !important;
  color: #1565C0 !important;
  font-weight: bold;
  border-radius: 0 20px 20px 0;
}

.v-list-group__items .v-list-item {
  padding-left: 40px !important;
}
</style> 