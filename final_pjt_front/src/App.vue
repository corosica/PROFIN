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
              <button class="nav-link-box"><strong>PROFIN</strong></button>
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
        <div class="auth-buttons">
          <div v-if="!islogin" class="auth-buttons-group">
            <RouterLink :to="{ name: 'Login' }"><button class="btn-profile">로그인</button></RouterLink>
            <RouterLink :to="{ name: 'Signup' }"><button class="btn-logout">회원가입</button></RouterLink>
          </div>
          <div v-else class="auth-buttons-group">
            <button type="button" class="btn-profile" @click="profile">회원 정보</button>
            <button type="button" class="btn-logout" @click="logout">로그아웃</button>
          </div>
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
      sessionStorage.removeItem('user_id');
      router.push({ name: 'Login' }).then(() => {
        router.go(0);
      });
    })
    .catch((error) => {
      console.log(error);
      sessionStorage.removeItem('token');
      sessionStorage.removeItem('username');
      sessionStorage.removeItem('user_id');
      router.go(0);
    });
};

const store = useCounterStore();

const profile = () => {
  router.push({ name: 'Profile' });
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');

* {
  font-family: 'Noto Sans KR', sans-serif; /* 전역 폰트 적용 */
}

.app-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.header-container {
  background-color: #fffdfd;
  border: 1px solid #dcdcdc;
  border-radius: 20px;
  padding: 15px;
  margin-bottom: 20px;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
}

.nav-links-wrapper {
  flex-grow: 1;
  display: flex;
  justify-content: center;
}

.nav-links {
  list-style: none;
  display: flex;
  justify-content: space-around;
  width: 100%;
  max-width: 1300px;
  background-color: #ffffff;
  border: 1px solid #ffffff;
  border-radius: 8px;
}

.nav-link-box {
  padding: 10px 20px;
  background-color: #1fcba9;
  border-radius: 20px;
  margin: 20px;
  text-decoration: none;
  color: #ffffff;
  font-size: 20px;
  border: 2px solid #1fcba9;
  margin-left: 5%;
  width: 100%;
  cursor: pointer;
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
  margin-left: 8%;
  transition: 0.3s;
}

.logo {
  max-height: 100px;
  width: auto;
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
  background-color: #ffffff;
  width: 100%;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
  border-radius: 8px;
  padding: 0;
  text-align: center;
}

.dropdown li {
  list-style: none;
}

.dropdown li a {
  color: #1abc9c;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  border-bottom: 1px solid #1abc9c;
}

.dropdown li a:hover {
  background-color: #1fcba9;
  color: #ffffff;
  border-radius: 8px;
}

/* 버튼 스타일 */
.auth-buttons {
  display: flex;
  align-items: center;
  margin-right: 5%;
}

.auth-buttons-group {
  display: flex;
  align-items: center;
}

.btn-profile,
.btn-logout {
  padding: 8px 12px;
  border-radius: 8px;
  font-weight: 500;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
  margin-left: 10px; /* 버튼 간의 간격을 동일하게 설정 */
}

.btn-profile {
  background-color: #ffffff;
  border: 2px solid #6c6b6b;
  color: #6c6b6b;
}

.btn-profile:hover {
  background-color: #b1b1b1;
  border-color: #b1b1b1;
  color: #ffffff;
}

.btn-logout {
  background-color: transparent;
  border: 2px solid #1abc9c;
  color: #1abc9c;
}

.btn-logout:hover {
  background-color: #1abc9c;
  color: #ffffff;
}

.main-content {
  flex-grow: 1;
}

/* 반응형 웹 디자인 */
@media (max-width: 768px) {
  .nav-links {
    flex-direction: column;
    align-items: center;
    margin-right: 0;
  }

  .nav-link-box {
    margin-bottom: 10px;
  }

  .logo-container {
    margin-left: 0;
    justify-content: center;
    width: 100%;
  }

  .navbar {
    justify-content: center;
  }

  .auth-buttons {
    margin-right: 0;
    justify-content: center;
  }

  .btn-profile,
  .btn-logout {
    margin-left: 5px; /* 모바일 환경에서는 간격을 조금 더 좁게 설정 */
  }
}

@media (max-width: 480px) {
  .nav-link-box {
    padding: 8px 20px;
  }

  .btn-profile,
  .btn-logout {
    padding: 6px 10px;
  }
}
</style>
