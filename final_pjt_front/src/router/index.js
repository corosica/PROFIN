import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'

import CommunityView from '@/views/Community/CommunityView.vue'
import PostCreateView from '@/views/Community/PostCreateView.vue'
import PostDetailView from '@/views/Community/PostDetailView.vue'
import PostUpdateView from '@/views/Community/PostUpdateView.vue'

import DepositView from '@/views/Deposit/DepositView.vue'
import DepositDetailView from '@/views/Deposit/DepositDetailView.vue'
import SavingDetailView from '@/views/Deposit/SavingDetailView.vue'

import KakaomapView from '@/views/Convenience/KakaoMapView.vue'
import ExchangeView from '@/views/Convenience/ExchangeView.vue'
import QuestionView from '@/views/Convenience/QuestionView.vue'

import AnswerView from '@/views/Convenience/AnswerView.vue'
import AnswerDetailView from '@/views/Convenience/AnswerDetailView.vue'
import AnswerCreateView from '@/views/Convenience/AnswerCreateView.vue'




import UserProfileUpdateView from '@/views/Users/UserProfileUpdateView.vue'
import UserProfileView from '@/views/Users/UserProfileView.vue'
import LoginView from '@/views/Users/LoginView.vue';
import SignupView from '@/views/Users/SignupView.vue';
import Portfolio from '@/components/Portfolio.vue';
import Products from '@/components/Products.vue';
import Profile from '@/components/Profile.vue';

import DepositList from '@/components/DepositList.vue'
import SavingList from '@/components/SavingList.vue'


const requireAuth = () => (to, from, next) => {
  if (sessionStorage.getItem('token') !== null) {
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
      children : [
        {
          path: 'deposit_list',
          name: 'DepositList',
          component: DepositList,
        },
        {
          path:'saving_list',
          name: 'SavingList',
          component: SavingList,
        }
      ]
    },
    {
      path: '/deposit/:id', // 나중에 id로 경로 수정해야함
      name: 'DepositDetail',
      component: DepositDetailView,
      beforeEnter : requireAuth()
    },
    {
      path: '/saving/:id', // 나중에 id로 경로 수정해야함
      name: 'SavingDetail',
      component: SavingDetailView,
      beforeEnter : requireAuth()
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
      beforeEnter : requireAuth()
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
      path: '/userprofile',
      name: 'UserProfile',
      component: UserProfileView,
      beforeEnter : requireAuth(),
      children : [
          {
            path: '/portfolio',
            name: 'Portfolio',
            component: Portfolio
          },
          {
            path: '/Profile',
            name : 'Profile',
            component : Profile

          },
          {
            path: '/products',
            name : 'Products',
            component : Products
          }
      ]
    },
    {
      path:'/userprofileupdate',
      name: 'UserProfileUpdate',
      component: UserProfileUpdateView,
      beforeEnter : requireAuth()
    },
    {
      path: '/question',
      name: 'Question',
      component: QuestionView,
    },
    {
      path: '/answer',
      name: 'Answer',
      component: AnswerView,
    },
    {
      path: '/answer/:id',
      name: 'AnswerDetail',
      component: AnswerDetailView,
    },
    {
      path: '/answer_create',
      name: 'AnswerCreate',
      component: AnswerCreateView,
    },
    
    // 기타 라우트 설정을 여기에 추가할 수 있습니다.
  ]
})

export default router
