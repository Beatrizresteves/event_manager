import { createRouter, createWebHistory } from 'vue-router'
import EventPage from '../views/EventPage.vue'
import LoginView from '../views/LoginView.vue'

const routes = [
  {
	path: '/',
	name: 'Login',
	component: LoginView
  },
  {
    path: '/eventos',
    name: 'Eventos',
    component: EventPage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
