import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:8000/api',
})

// Função auxiliar para renovar o token
const refreshToken = async () => {
  const refresh = localStorage.getItem('refresh_token')
  try {
    const response = await axios.post('http://localhost:8000/api/token/refresh/', { refresh })
    const access = response.data.access
    localStorage.setItem('access_token', access)
    return access
  } catch (error) {
    localStorage.removeItem('access_token')
    localStorage.removeItem('refresh_token')
    return null
  }
}

// Interceptor de requisição
api.interceptors.request.use(
  async (config) => {
    let access = localStorage.getItem('access_token')
    const refresh = localStorage.getItem('refresh_token')

    if (access) {
      const tokenExp = JSON.parse(atob(access.split('.')[1])).exp
      const now = Math.floor(Date.now() / 1000)

      if (tokenExp < now && refresh) {
        access = await refreshToken()
      }

      if (access) {
        config.headers.Authorization = `Bearer ${access}`
      }
    }

    return config
  },
  (error) => Promise.reject(error)
)

export default api
