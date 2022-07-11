import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/deposit',
      name: 'deposit',
      component: () => import('../views/DepositView.vue')
    },
    {
      path: '/withdraw',
      name: 'withdraw',
      component: () => import('../views/WithdrawView.vue')
    },
    {
      path: '/tranfer',
      name: 'tranfer',
      component: () => import('../views/TranferView.vue')
    },
    {
      path: '/create',
      name: 'create',
      props: true,
      component: () => import('../views/CreateAccountView.vue')
    },
    {
      path: '/multi-tranfer',
      name: 'multi-tranfer',
      component: () => import('../views/MultiTranferView.vue')
    }
    
  ]
})

export default router
