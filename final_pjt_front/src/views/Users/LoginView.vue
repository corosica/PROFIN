<template>
  <div class="login-container">
    <div class="login-box">
      <div class="logo-container">
        <img src="/PROFIN.png" alt="PROFIN Logo" class="logo">
      </div>
      <form @submit.prevent="login">
        <div class="input-group">
          <label for="username">아이디</label>
          <input type="text" id="username" v-model="username" placeholder="아이디를 입력하세요.">
        </div>
        <div class="input-group">
          <label for="password">비밀번호</label>
          <input type="password" id="password" v-model="password" placeholder="비밀번호를 입력하세요.">
        </div>
        <div class="button-group">
          <button type="submit" class="btn-login">로그인</button>
          <button type="button" class="btn-cancel" @click="cancel">취소</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useCounterStore } from '@/stores/counter';

const counterStore = useCounterStore();
const username = ref('');
const password = ref('');
const router = useRouter();

const login = () => {
  console.log(username.value);
  counterStore.login(username.value, password.value);
};

const cancel = () => {
  router.push('/');
};  
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #ffffff;
 }

.login-box {
  background-color: #fff;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  font-family: 'Roboto', sans-serif;
  max-width: 600px;
  width: 100%;
  text-align: center;
  border: 1px solid #ccc;
}

.logo-container {
  margin-bottom: 20px;
}

.logo {
  max-width: 100px;
}

.input-group {
  margin-bottom: 20px;
  text-align: left;
}

.input-group label {
  display: block;
  font-weight: 700;
  color: #333;
  margin-bottom: 5px;
}

.input-group input {
  width: calc(100% - 20px);
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 1rem;
}

.input-group input::placeholder {
  color: #aaa;
}

.button-group {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}

.button-group button {
  width: 100px; /* 버튼 크기를 동일하게 설정 */
  padding: 10px;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  font-weight: 700;
  cursor: pointer;
}

.btn-login {
  background-color: #1abc9c;
  color: #fff;
}

.btn-cancel {
  background-color: #95a5a6;
  color: #fff;
}

.button-group button:hover {
  opacity: 0.8;
}
</style>
