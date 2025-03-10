// axios配置文件
import axios from 'axios'

// 创建axios实例
const instance = axios.create({
  baseURL: 'http://localhost:8000',
  timeout: 1000*60*3,
  headers: {
    'Content-Type': 'application/json'
  }
})

// 请求拦截器
instance.interceptors.request.use(
  config => {
    // 在发送请求之前做些什么
    return config
  },
  error => {
    // 对请求错误做些什么
    console.error('请求错误:', error)
    return Promise.reject(error)
  }
)

// 响应拦截器
instance.interceptors.response.use(
  response => {
    // 对响应数据做点什么
    return response.data
  },
  error => {
    // 对响应错误做点什么
    if (error.response) {
      // 服务器返回了错误状态码
      console.error('响应错误:', error.response.status, error.response.data)
    } else if (error.request) {
      // 请求已发出，但没有收到响应
      console.error('请求无响应:', error.request)
    } else {
      // 请求配置出错
      console.error('请求配置错误:', error.message)
    }
    return Promise.reject(error)
  }
)

export default instance 