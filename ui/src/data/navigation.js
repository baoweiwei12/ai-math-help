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