<template>
    <div>
      <h1>회원가입</h1>
      <form @submit.prevent="signup">
        <label for="username">아이디: </label>
        <input type="text" id="username" v-model="username" required>
        <br>
        <label for="password">비밀번호: </label>
        <input type="password" id="password" v-model="password" required>
        <br>
        <label for="confirmPassword">비밀번호 확인: </label>
        <input type="password" id="confirmPassword" v-model="confirmPassword" required>
        <br>
        <label for="email">이메일: </label>
        <input type="email" id="email" v-model="email" required>
        <br>
        <button type="submit">회원가입</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  
  const email = ref('');
  const password = ref('');
  const confirmPassword = ref('');
  const router = useRouter();
  
  const signup = () => {
    if (password.value !== confirmPassword.value) {
      alert('비밀번호가 일치하지 않습니다.');
      return;
    }
    if (email.value && password.value) {
      // 실제 회원가입 로직을 여기에 추가하세요.
      console.log('Email:', email.value);
      console.log('Password:', password.value);
      router.push('/login');
    } else {
      alert('이메일과 비밀번호를 입력하세요.');
    }
  };
  </script>
  
  <style scoped>
  /* 최소한의 스타일링만 추가 */
  </style>
  