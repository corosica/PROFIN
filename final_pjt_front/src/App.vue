<template>
  <header>
      <nav>
        <RouterLink :to="{name : 'Home'}">홈</RouterLink> I
        <RouterLink :to="{name : 'Deposit'}">금융 상품</RouterLink> I
        <RouterLink :to="{name : 'Community'}">커뮤니티</RouterLink>
        <br>
        <RouterLink :to="{name : 'Login'}"><button @click="Login">로그인</button></RouterLink> I
        <RouterLink :to="{name : 'Signup'}"><button @click="Signup">회원가입</button></RouterLink>

      </nav>
  </header>

  <RouterView />
</template>

<script setup>
  import { useCounterStore } from '@/stores/counter';
  import { RouterLink, RouterView } from 'vue-router'
  // import HelloWorld from './components/HelloWorld.vue'

  const store = useCounterStore();

</script>

<style scoped>
</style>
