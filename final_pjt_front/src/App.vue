<template>
  <header>
      <nav>
        <RouterLink :to="{name : 'Home'}">홈</RouterLink> I
        <RouterLink :to="{name : 'Deposit'}">금융 상품</RouterLink> I
        <RouterLink :to="{name : 'Community'}">커뮤니티</RouterLink>
        <br>
        <div v-if="islogin">
          <RouterLink :to="{name : 'Login'}"><button @click="Login">로그인</button></RouterLink> I
          <RouterLink :to="{name : 'Signup'}"><button @click="Signup">회원가입</button></RouterLink>
        </div>
        <div v-else>
          <button @click="logout">로그아웃</button>
          <button>회원 정보</button>
          <!-- 회원정보 -> routerlink로 바꾸기 -->

        </div>

      </nav>
  </header>

  <RouterView />
</template>

<script setup>
  import { useCounterStore } from '@/stores/counter';
  import { RouterLink, RouterView } from 'vue-router'
  import axios from 'axios'
  import { ref ,onMounted} from 'vue'
  // import HelloWorld from './components/HelloWorld.vue'
  const islogin = ref(true)
  const isLoggedIn = function () {
    islogin.value = (localStorage.getItem('token')== null)
  }

  
  console.log(localStorage.getItem('token'))
  isLoggedIn()
  console.log(localStorage.getItem('token')== null)
  const logout = function () {
    localStorage.removeItem('token');
    axios({
      method : 'POST',
      url : 'http://127.0.0.1:8000/accounts/logout',
    })
    .then(function(response) {
      console.log(response.data);
      location.reload();
    })
    .then(function(error) {
      console.log(error);
    })
    

  }
  const store = useCounterStore();

</script>

<style scoped>
</style>
