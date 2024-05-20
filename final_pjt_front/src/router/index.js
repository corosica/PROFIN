import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'

import CommunityView from '@/views/Community/CommunityView.vue'
import PostCreateView from '@/views/Community/PostCreateView.vue'
import PostDetailView from '@/views/Community/PostDetailView.vue'
import PostUpdateView from '@/views/Community/PostUpdateView.vue'

import DepositView from '@/views/Deposit/DepositView.vue'
import DepositDetailView from '@/views/Deposit/DepositDetailView.vue'

import KakaomapView from '@/views/Convenience/KakaoMapView.vue'
import ExchangeView from '@/views/Convenience/ExchangeView.vue'

import UserProfileView from '@/views/Users/UserProfileView.vue'
import LoginView from '@/views/Users/LoginView.vue';
import SignupView from '@/views/Users/SignupView.vue';



const requireAuth = () => (to, from, next) => {
  if (localStorage.getItem('token') !== null) {
    return next();
  }
  alert('로그인을 해주세요'); // 나중에 before enter로 처리
  next('/login');
};

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes : [
    {
      path: '/',
      name: 'Home',
      component: HomeView,
    },
    {
      path: '/community',
      name: 'Community',
      component: CommunityView,
    },
    {
      path: '/community/post_create',
      name: 'PostCreate',
      component: PostCreateView,
      beforeEnter : requireAuth()
    },
    {
      path: '/community/:id',
      name: 'PostDetail',
      component: PostDetailView,
    },
    { 
      path: '/deposit',
      name: 'Deposit',
      component: DepositView,
    },
    {
      path: '/deposit/:id', // 나중에 id로 경로 수정해야함
      name: 'DepositDetail',
      component: DepositDetailView,
    },
    {
      path: '/login',
      name: 'Login',
      component: LoginView,
    },
    {
      path: '/signup',
      name: 'Signup',
      component: SignupView,
    },
    {
      path: '/community/post_update/:id',
      name: 'PostUpdate',
      component: PostUpdateView,
    },
    {
      path: '/kakaomap',
      name: 'Kakaomap',
      component: KakaomapView,
    },
    {
      path: '/exchange',
      name: 'Exchange',
      component: ExchangeView,
    },
    {
      path: '/UserProfile',
      name: 'UserProfile',
      component: UserProfileView,
    },
  
    // 기타 라우트 설정을 여기에 추가할 수 있습니다.
  ]
})

export default router
