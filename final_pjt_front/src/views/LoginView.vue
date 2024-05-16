<template>
    <div>
      <h1>로그인</h1>
      <form @submit.prevent="login">
        <label for="username">아이디: </label>
        <input type="text" id="username" v-model="username" required>
        <br>
        <label for="password">비밀번호: </label>
        <input type="password" id="password" v-model="password" required>
        <br>
        <button type="submit">로그인</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  
  const email = ref('');
  const password = ref('');
  const router = useRouter();
  
  const login = () => {
    if (email.value && password.value) {
      // 실제 로그인 로직을 여기에 추가하세요.
      console.log('Email:', email.value);
      console.log('Password:', password.value);
      router.push('/');
    } else {
      alert('이메일과 비밀번호를 입력하세요.');
    }
  };
  </script>
  
  <style scoped>
  /* 최소한의 스타일링만 추가 */
  </style>
  