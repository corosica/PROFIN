import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import CommunityView from '@/views/CommunityView.vue'
import PostCreateView from '@/views/PostCreateView.vue'
import PostDetailView from '@/views/PostDetailView.vue'
import DepositView from '@/views/DepositView.vue'
import DepositDetailView from '@/views/DepositDetailView.vue'
import LoginView from '@/views/LoginView.vue';
import SignupView from '@/views/SignupView.vue';
import PostUpdateView from '@/views/PostUpdateView.vue'
import KakaomapView from '@/views/KakaoMapView.vue'
import ExchangeView from '@/views/ExchangeView.vue'

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
      path: '/deposit/deposit_detail', // 나중에 id로 경로 수정해야함
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
      path: '/Exchange',
      name: 'Exchange',
      component: ExchangeView,
    }

  
    // 기타 라우트 설정을 여기에 추가할 수 있습니다.
  ]
})

export default router
