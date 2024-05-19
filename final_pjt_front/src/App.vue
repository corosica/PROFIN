<template>

  <header class="header-container">
    <nav class="navbar">
      <div>
      <img src="/PROFIN.png" alt="Logo" class="logo">
      </div>
      <div class="nav-links-wrapper">
        <div class="nav-links">
          <RouterLink class="nav-link-box" :to="{ name: 'Home' }">PROFIN</RouterLink>
          <RouterLink class="nav-link-box" :to="{ name: 'Deposit' }">금융 상품</RouterLink>
          <RouterLink class="nav-link-box" :to="{ name: 'Community' }">커뮤니티</RouterLink>
          <RouterLink class="nav-link-box" :to="{ name: 'Kakaomap' }">카카오맵</RouterLink>
        </div>
      </div>

      <div v-if="islogin">
        <RouterLink :to="{name : 'Login'}"><button @click="Login">로그인</button></RouterLink> I
        <RouterLink :to="{name : 'Signup'}"><button @click="Signup">회원가입</button></RouterLink>
      </div>
      <div v-else>
        <button>회원 정보</button>
        <button @click="logout">로그아웃</button>

          <!-- 회원정보 -> routerlink로 바꾸기 -->
      </div>
    </nav>
  </header>

  <RouterView />

</template>

<script setup>
  import { useCounterStore } from '@/stores/counter';
  import { useRouter,RouterLink, RouterView } from 'vue-router'
  import axios from 'axios'
  import { ref ,onMounted} from 'vue'
  const router = useRouter()
  // import HelloWorld from './components/HelloWorld.vue'
  const islogin = ref(true)
  const isLoggedIn = function () {
    islogin.value = (localStorage.getItem('token')== null)
  }

  
  console.log(localStorage.getItem('token'))
  isLoggedIn()
  console.log(localStorage.getItem('token')== null)
  const logout = function () {
    axios({
      method : 'POST',
      url : 'http://127.0.0.1:8000/accounts/logout/',
      headers : {
        Authorization : localStorage.getItem('token'),
      },
      data : {}
    })
    .then(function(response) {
      localStorage.removeItem('token');
      console.log(response.data);
      router.push({name:'Login'}).then(() => {
        // router.push가 완료된 후 새로고침을 수행
          router.go(0);
        });
    })
    .then(function(error) {
      console.log(error);
    })
    

  }
  const store = useCounterStore();

</script>

<style scoped>
.header-container {
  background-color: #fffdfd; /* 흰색 배경 */
  border: 1px solid #dcdcdc; /* 회색 선 */
  border-radius: 8px; /* 둥근 모서리 */
  padding: 20px;
  margin-bottom: 20px;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-links {
  display: flex;
  gap: 10px;
}

.nav-link-box {
  padding: 10px 20px;
  background-color: #1abc9c; /* 민트색 배경 */
  border-radius: 8px; /* 둥근 모서리 */
  text-decoration: none;
  color: #ffffff; /* 링크 색상 */
  font-weight: bold;
  border: 2px solid #1abc9c;
}

.nav-link-box:hover {
  background-color: #ffffff; /* 링크 호버 배경색 */
  color: #1abc9c; /* 링크 호버 색상 */
  border-color: #1abc9c;
  border: 2px solid
}

.btn-outline-success, .btn-outline-primary, .btn-outline-danger, .btn-outline-info {
  border-color: #00796b; /* 버튼 테두리 색상 */
  color: #00796b; /* 버튼 텍스트 색상 */
}

.btn-outline-success:hover, .btn-outline-primary:hover, .btn-outline-danger:hover, .btn-outline-info:hover {
  background-color: #004d40; /* 버튼 호버 배경색 */
  border-color: #004d40; /* 버튼 호버 테두리 색상 */
  color: #ffffff !important; /* 버튼 호버 텍스트 색상 */
}

.nav-links-wrapper {
  flex-grow: 1;
  display: flex;
  justify-content: center;

}
.nav-links {
  display: flex;
  gap: 200px;
  padding: 10px;
  background-color: #dcdcdc; /* 연한 회색 배경 */
  border: 1px solid #dcdcdc; /* 회색 선 */
  border-radius: 8px; /* 둥근 모서리 */
}

.logo-container {
  display: flex;
  align-items: center;
}

.logo {
  max-height: 100px;
  margin-right: 0px;
}



</style>
