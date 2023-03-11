import { createRouter, createWebHistory } from 'vue-router'
import Home from '../Home.vue'

const routes = [
  {
    path: '/Home',
    name: 'home',
    component: Home
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
