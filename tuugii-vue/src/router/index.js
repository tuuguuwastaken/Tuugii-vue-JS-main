import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import AboutView from '../views/AboutView.vue'
import Posts from '../views/posts/Posts.vue'
import PostDetails from '../views/posts/PostDetails.vue'
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },{
    path:'/Post',
    name:'Post',
    component: Posts
  },
  {
    path: '/Post/:id',
    name: 'PostDetails',
    component: PostDetails
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
