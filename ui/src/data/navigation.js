import { reactive } from 'vue'

export const navigationData = reactive([
  {
    title: '首页',
    key: 'home',
    isOpen: false,
    icon: 'mdi-home',
    to: '/'
  },
  {
    title: '学习统计',
    key: 'study',
    isOpen: false,
    icon: 'mdi-chart-box',
    to: '/study'
  },
  {
    title: '第一章 函数与极限',
    key: 'chapter1',
    isOpen: false,
    icon: 'mdi-function',
    children: []
  },
  {
    title: '第二章 导数与微分',
    key: 'chapter2',
    isOpen: false,
    icon: 'mdi-source-branch',
    children: []
  },
  {
    title: '第三章 微分中值定理与导数的应用',
    key: 'chapter3',
    isOpen: false,
    icon: 'mdi-math-norm',
    children: [
      {
        title: '3.1 微分中值定理',
        key: '3.1',
        to: '/chapter3/section1'
      },
      {
        title: '3.2 洛必达法则',
        key: '3.2',
        to: '/chapter3/section2'
      },
      {
        title: '3.3 泰勒公式',
        key: '3.3',
        to: '/chapter3/section3'
      },
      {
        title: '3.4 函数的单调性与曲线的凹凸性',
        key: '3.4',
        to: '/chapter3/section4'
      },
      {
        title: '3.5 函数的极值',
        key: '3.5',
        to: '/chapter3/section5'
      },
      {
        title: '3.6 函数图形的秒回',
        key: '3.6',
        to: '/chapter3/section6'
      },
      {
        title: '3.7 弧微分与曲率',
        key: '3.7',
        to: '/chapter3/section7'
      }
    ]
  },
  {
    title: '第四章 不定积分',
    key: 'chapter4',
    isOpen: false,
    icon: 'mdi-math-integral',
    children: []
  },
  {
    title: '第五章 定积分',
    key: 'chapter5',
    isOpen: false,
    icon: 'mdi-integral-box',
    children: []
  },
  {
    title: '第六章 定积分的应用',
    key: 'chapter6',
    isOpen: false,
    icon: 'mdi-chart-arc',
    children: [
      {
        title: '6.1 定积分的元素法',
        key: '6.1',
        to: '/chapter6/section1'
      },
      {
        title: '6.2 定积分在几何上的应用',
        key: '6.2',
        to: '/chapter6/section2'
      },
      {
        title: '6.3 定积分在物理上的应用',
        key: '6.3',
        to: '/chapter6/section3'
      }
    ]
  },
  {
    title: '第七章 微分方程的基本概念',
    key: 'chapter7',
    isOpen: false,
    icon: 'mdi-math-compass',
    children: []
  },
  {
    title: '第八章 向量代数与空间解析几何',
    key: 'chapter8',
    isOpen: true,
    icon: 'mdi-vector-polygon',
    children: []
  },
  {
    title: '第九章 多元函数的微分法及其应用',
    key: 'chapter9',
    isOpen: true,
    icon: 'mdi-function-variant',
    children: [
      {
        title: '9.1 多元函数的基本概念',
        key: '9.1',
        to: '/chapter9/section1'
      },
      {
        title: '9.2 偏导数与全微分',
        key: '9.2',
        to: '/chapter9/section2'
      },
      {
        title: '9.3 多元复合函数与隐函数求导法则',
        key: '9.3',
        to: '/chapter9/section3'
      },
      {
        title: '9.4 多元函数极值及其应用',
        key: '9.4',
        to: '/chapter9/section4'
      },
      {
        title: '9.5 方向导数和梯度',
        key: '9.5',
        to: '/chapter9/section5'
      },
      {
        title: '9.6 多元函数微分学的应用',
        key: '9.6',
        to: '/chapter9/section6'
      }
    ]
  },
  {
    title: '第十章 重积分',
    key: 'chapter10',
    isOpen: false,
    icon: 'mdi-math-integral-box',
    children: []
  },
  {
    title: '第十一章 曲线积分和曲面积分',
    key: 'chapter11',
    isOpen: false,
    icon: 'mdi-chart-bell-curve-cumulative',
    children: []
  },
  {
    title: '第十二章 无穷级数',
    key: 'chapter12',
    isOpen: false,
    icon: 'mdi-sigma',
    children: []
  }
]) 