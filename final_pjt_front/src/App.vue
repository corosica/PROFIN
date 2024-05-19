<template>

  <header>
      <nav>
        <RouterLink :to="{name : 'Home'}">홈</RouterLink> I
        <RouterLink :to="{name : 'Deposit'}">금융 상품</RouterLink> I
        <RouterLink :to="{name : 'Community'}">커뮤니티</RouterLink>
        <RouterLink :to="{name : 'Kakaomap'}">카카오맵</RouterLink>
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
</style>
