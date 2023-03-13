import { createRouter, createWebHistory } from 'vue-router'
// import Home from '../views/Home.vue'

const path = (path, name, componentPath = {}, args = {}) => {
  return { path, name, component: () => import(`../views/${componentPath}`), ...args };
};


const routes = [  
  path('/','Home', 'Home.vue' ),
  path('/about', 'about', 'AboutView.vue'),
  path('/Post', 'Post','posts/Posts.vue'),
  path('/Post/:id' , 'PostDetails', 'posts/PostDetails.vue'),
  path('/DeletePost','DelPost','delete/DeletePost.vue'),
  path('/DeletePost/:id', 'delaction','delete/deleteaction.vue'),
  path('/Upload','Upload','Upload/Upload.vue')
  // {
  //   path: '/',
  //   name: 'Home',
  //   component: Home
  // },
  // {
  //   path: '/about',
  //   name: 'about',
  //   component: AboutView
  // },{
  //   path:'/Post',
  //   name:'Post',
  //   component: Posts
  // },
  // {
  //   path: '/Post/:id',
  //   name: 'PostDetails',
  //   component: PostDetails
  // }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
