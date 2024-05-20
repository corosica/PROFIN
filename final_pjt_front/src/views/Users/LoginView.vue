<template>
    <div>
      <h1>로그인</h1>
      <form @submit.prevent="login">
        <label for="username">아이디: </label>
        <input type="text" id="username" v-model="username">
        <br>
        <label for="password">비밀번호: </label>
        <input type="password" id="password" v-model="password">
        <br>
        <button type="submit">로그인</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  import {useCounterStore} from '@/stores/counter';
  const counterStore = useCounterStore()
  const username = ref('');
  const email = ref('');
  const password = ref('');
  const router = useRouter();
  const login = () => {
    console.log(username.value);
    counterStore.login(username.value,password.value)
  };
  </script>
  
  <style scoped>
  /* 최소한의 스타일링만 추가 */
  </style>
  