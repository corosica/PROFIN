<template>
  <div class="app-container">
    <header class="header-container">
      <nav class="navbar">
        <div class="logo-container">
          <router-link :to="{ name: 'Home' }">
            <img src="/PROFIN.png" alt="Logo" class="logo">
          </router-link>
        </div>
        <div class="nav-links-wrapper">
          <ul class="nav-links">
            <li class="nav-item dropdown-container">
              <button class="nav-link-box">PROFIN</button>
              <ul class="dropdown">
                <li><RouterLink class="dropdown-link" :to="{ name: 'Home' }">인삿말</RouterLink></li>
              </ul>
            </li>
            <li class="nav-item dropdown-container">
              <button class="nav-link-box">금융 상품</button>
              <ul class="dropdown">
                <li><RouterLink class="dropdown-link" :to="{ name: 'Deposit' }">예적금 상품</RouterLink></li>
              </ul>
            </li>
            <li class="nav-item dropdown-container">
              <button class="nav-link-box">이용자 서비스</button>
              <ul class="dropdown">
                <li><RouterLink class="dropdown-link" :to="{ name: 'Exchange' }">환율 계산기</RouterLink></li>
                <li><RouterLink class="dropdown-link" :to="{ name: 'Kakaomap' }">근처 은행 검색</RouterLink></li>
                <li><RouterLink class="dropdown-link" :to="{ name: 'Community' }">커뮤니티</RouterLink></li>
              </ul>
            </li>
            <li class="nav-item dropdown-container">
              <button class="nav-link-box">고객 센터</button>
              <ul class="dropdown">
                <li><RouterLink class="dropdown-link" :to="{ name: 'Question' }">FAQ</RouterLink></li>
                <li><RouterLink class="dropdown-link" :to="{ name: 'Answer' }">문의하기</RouterLink></li>
              </ul>
            </li>
          </ul>
        </div>
        <div v-if="!islogin">
          <RouterLink :to="{ name: 'Login' }"><button class="btn-profile">로그인</button></RouterLink> I
          <RouterLink :to="{ name: 'Signup' }"><button class="btn-logout">회원가입</button></RouterLink>
        </div>
        <div v-else>
          <button type="button" class="btn-profile" @click="profile">회원 정보</button> I
          <button type="button" class="btn-logout" @click="logout">로그아웃</button>
        </div>
      </nav>
    </header>
    <main class="main-content">
      <RouterView />
    </main>
    <AttendanceCheck />
    <Footers />
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { useRouter, RouterLink, RouterView } from 'vue-router';
import axios from 'axios';
import { ref, onMounted } from 'vue';
import AttendanceCheck from '@/components/AttendanceCheck.vue';
import Footers from '@/components/Footer.vue'; // Footer 컴포넌트를 가져옵니다.

const router = useRouter();
const islogin = ref(false);

const isLoggedIn = () => {
  islogin.value = sessionStorage.getItem('token') !== null;
};

isLoggedIn();

const logout = () => {
  axios({
    method: 'POST',
    url: 'http://127.0.0.1:8000/accounts/logout/',
    headers: {
      Authorization: sessionStorage.getItem('token'),
    },
    data: {},
  })
    .then((response) => {
      sessionStorage.removeItem('token');
      sessionStorage.removeItem('username');
      router.push({ name: 'Login' }).then(() => {
        router.go(0);
      });
    })
    .catch((error) => {
      console.log(error);
      sessionStorage.removeItem('token');
      sessionStorage.removeItem('username');
      router.go(0);
    });
};

const store = useCounterStore();

const profile = () => {
  router.push({ name: 'Profile' });
};
</script>

<style scoped>
.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.header-container {
  background-color: #fffdfd;
  border: 1px solid #dcdcdc;
  border-radius: 20px;
  padding: 20px;
  margin-bottom: 20px;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-links-wrapper {
  flex-grow: 1;
  display: flex;
  justify-content: center;
}

.nav-links {
  list-style: none; /* 기본 리스트 스타일 제거 */
  display: flex;
  justify-content: space-around;
  width: 100%;
  max-width: 1300px;
  padding: 10px;
  background-color: #ffffff;
  border: 1px solid #ffffff;
  border-radius: 8px;
  margin-right: 100px;
}

.nav-link-box {
  padding: 8px 30px;
  background-color: #1fcba9;
  border-radius: 20px;
  text-decoration: none;
  color: #ffffff;
  font-weight: bold;
  border: 2px solid #1fcba9;
  cursor: pointer; /* 버튼 스타일 일관성 */
}

.nav-link-box:hover {
  background-color: #ffffff;
  color: #1abc9c;
  border-color: #1abc9c;
  transition: background-color 0.3s, color 0.3s;
}

.logo-container {
  display: flex;
  align-items: center;
  transition: 0.3s;
}

.logo {
  max-height: 100px;
  margin-left: 200px;
}

/* 드롭다운 메뉴 스타일 */
.dropdown-container {
  position: relative;
  display: inline-block;
}

.dropdown-container:hover .dropdown {
  display: block;
}

.dropdown {
  display: none;
  position: absolute;
  background-color: #ffffff; /* 드롭다운 배경색 통일 */
  width: 100%;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
  border-radius: 8px;
  padding: 0;
  text-align: center;
  list-style: none; /* 기본 리스트 스타일 제거 */
}

.dropdown li {
  list-style: none; /* 리스트 스타일 제거 */
}

.dropdown li a {
  color: #1abc9c; /* 드롭다운 링크 색상 통일 */
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  border-bottom: 1px solid #1abc9c;
}

.dropdown li a:hover {
  background-color: #1fcba9; /* 드롭다운 호버 색상 통일 */
  color: #ffffff; /* 호버 시 글자 색상 통일 */
  border-radius: 8px;
}

/* 버튼 스타일 */
.btn-profile {
  padding: 8px 12px;
  background-color: #ffffff;
  border-radius: 8px;
  border: 2px solid #6c6b6b;
  color: #6c6b6b;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
}

.btn-profile:hover {
  background-color: #b1b1b1;
  border-color: #b1b1b1;
  color: #ffffff;
}

.btn-logout {
  padding: 8px 12px;
  background-color: transparent;
  border-radius: 8px;
  border: 2px solid #1abc9c;
  color: #1abc9c;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
}

.btn-logout:hover {
  background-color: #1abc9c;
  color: #ffffff;
}

.main-content {
  flex-grow: 1;
}
</style>
