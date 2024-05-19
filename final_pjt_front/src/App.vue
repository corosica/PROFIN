<template>
  <header class="header-container">
    <nav class="navbar">
      <div class="logo-container">
        <router-link :to="{ name: 'Home' }">
          <img src="/PROFIN.png" alt="Logo" class="logo">
        </router-link>
      </div>
      <div class="nav-links-wrapper">
        <div class="nav-links">
          <RouterLink class="nav-link-box" :to="{ name: 'Home' }">PROFIN</RouterLink>
          <RouterLink class="nav-link-box" :to="{ name: 'Deposit' }">금융 상품</RouterLink>
          <RouterLink class="nav-link-box" :to="{ name: 'Community' }">커뮤니티</RouterLink>
          <RouterLink class="nav-link-box" :to="{ name: 'Kakaomap' }">카카오맵</RouterLink>
        </div>
      </div>
      <div v-if="!islogin">
        <RouterLink :to="{ name: 'Login' }"><button class="nav-button">로그인</button></RouterLink>
        <RouterLink :to="{ name: 'Signup' }"><button class="nav-button">회원가입</button></RouterLink>
      </div>
      <div v-else>
        <button type="button" class="btn-profile" @click="profile">회원 정보</button> I
        <button type="button" class="btn-logout" @click="logout">로그아웃</button>
      </div>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { useRouter, RouterLink, RouterView } from 'vue-router';
import axios from 'axios';
import { ref, onMounted } from 'vue';

const router = useRouter();
const islogin = ref(false);

const isLoggedIn = () => {
  islogin.value = localStorage.getItem('token') !== null;
};

console.log(localStorage.getItem('token'));
isLoggedIn();
console.log(localStorage.getItem('token') === null);

const logout = () => {
  axios({
    method: 'POST',
    url: 'http://127.0.0.1:8000/accounts/logout/',
    headers: {
      Authorization: localStorage.getItem('token'),
    },
    data: {},
  })
    .then((response) => {
      localStorage.removeItem('token');
      console.log(response.data);
      router.push({ name: 'Login' }).then(() => {
        router.go(0);
      });
    })
    .catch((error) => {
      console.log(error);
    });
};

const store = useCounterStore();

const profile = () => {
  router.push({ name: 'UserProfile' });
};
</script>

<style scoped>
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
  display: flex;
  justify-content: space-around; /* 링크 사이의 간격을 균등하게 조정 */
  width: 100%;
  max-width: 1300px; /* 링크 컨테이너의 최대 너비를 설정 */
  padding: 10px;
  background-color: #ebeaea;
  border: 1px solid #ebeaea;
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
}

.nav-link-box:hover {
  background-color: #ffffff;
  color: #1abc9c;
  border-color: #1abc9c;
}

.logo-container {
  display: flex;
  align-items: center;
}

.logo {
  max-height: 100px;
  margin-left: 200px;
}

.nav-button {
  padding: 10px 20px;
  background-color: #1abc9c;
  border-radius: 8px;
  border: 2px solid #1abc9c;
  color: #ffffff;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
}

.nav-button:hover {
  background-color: #ffffff;
  color: #1abc9c;
  border-color: #1abc9c;
}

/* Custom styles for Bootstrap-like buttons */
.btn-profile {
  padding:  8px 12px;
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
</style>
