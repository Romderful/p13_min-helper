import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Login from '../views/Login.vue'
import Signup from '../views/Signup.vue'
import AnimeList from "../views/AnimeList.vue"
import AnimeDetail from "../views/AnimeDetail.vue"


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/log-in',
    name: 'Login',
    component: Login
  },
  {
    path: '/sign-up',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/animes/:data?',
    name: 'AnimeList',
    component: AnimeList,
  },
  {
    path: '/animes/:genre?/:score?',
    name: 'AnimeFilter',
    component: AnimeList,
  },
  {
    path: '/animes/:data?/page/:page',
    name: 'Pagination',
    component: AnimeList,
  },
  {
    path: '/animes/:id',
    name: 'AnimeDetail',
    component: AnimeDetail,
    props: true,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
