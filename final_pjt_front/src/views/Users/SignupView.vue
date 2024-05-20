<template>
  <div class="signup-container">
    <h1>회원가입</h1>
    <br>
    <form @submit.prevent="signup" class="signup-form">
      <div class="form-group">
        <label for="username">아이디: </label>
        <input type="text" id="username" v-model="username" required>
      </div>
      <div class="form-group">
        <label for="password">비밀번호: </label>
        <input type="password" id="password" v-model="password" required>
      </div>
      <div class="form-group">
        <label for="confirmPassword">비밀번호 확인: </label>
        <input type="password" id="confirmPassword" v-model="confirmPassword" required>
      </div>
      <div class="form-group">
        <label for="nickname">닉네임: </label>
        <input type="text" id="nickname" v-model="nickname">
      </div>
      <div class="form-group">
        <label for="email">이메일: </label>
        <input type="email" id="email" v-model="email" required>
      </div>
      <div class="form-group">
        <label for="age">나이: </label>
        <input type="number" id="age" v-model="age" required>
      </div>
      <br>
      <button type="submit" class="signup-button">회원가입</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useCounterStore } from '@/stores/counter';

const username = ref('');
const email = ref('');
const password = ref('');
const nickname = ref('');
const age = ref('');
const confirmPassword = ref('');
const router = useRouter();
const counterStore = useCounterStore();

const signup = () => {
  if (!(username.value && password.value && confirmPassword.value && email.value && age.value)) {
    alert('필수 입력사항을 확인하세요.');
  }
  else if (password.value !== confirmPassword.value) {
    alert('비밀번호가 일치하지 않습니다.');
    return;
  }
  else {
    counterStore.signup(username.value, password.value, confirmPassword.value, email.value, nickname.value, age.value);
    router.push('/login');
  }
};
</script>

<style scoped>
.signup-container {
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
  border: 1px solid #dcdcdc;
  border-radius: 8px;
  background-color: #f9f9f9;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.signup-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-group input {
  width: 100%;
  padding: 8px;
  border: 1px solid #dcdcdc;
  border-radius: 4px;
  box-sizing: border-box;
}

.signup-button {
  padding: 10px 15px;
  border: none;
  background-color: #1abc9c;
  color: #ffffff;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.signup-button:hover {
  background-color: #16a085;
}
</style>
