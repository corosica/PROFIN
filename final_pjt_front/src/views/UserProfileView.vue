<template>
    <div class="profile-container">
      <h1>회원정보</h1>
      <form @submit.prevent="updateProfile" class="profile-form">
        <div class="form-group">
          <label for="username">아이디</label>
          <input type="text" id="username" v-model="username" disabled>
        </div>
        <div class="form-group">
          <label for="nickname">닉네임</label>
          <input type="text" id="nickname" v-model="nickname" disabled>
        </div>
        <div class="form-group">
          <label for="email">이메일</label>
          <input type="email" id="email" v-model="email" disabled>
        </div>
        <div class="form-group">
          <label for="age">나이</label>
          <input type="number" id="age" v-model="age" disabled>
        </div>
        <button type="submit" class="update-button">정보 수정</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import { useCounterStore } from '@/stores/counter';
  
  const username = ref('');
  const email = ref('');
  const nickname = ref('');
  const age = ref('');
  const router = useRouter();
  const counterStore = useCounterStore();
  
  onMounted(async () => {
    try {
      await counterStore.getUserInfo(); // 비동기 호출을 기다림
      const userData = counterStore.userInfos;
      if (userData) {
        username.value = userData.username;
        email.value = userData.email;
        nickname.value = userData.nickname;
        age.value = userData.age;
      }
    } catch (error) {
      console.error('Failed to load user data:', error);
    }
  });
  
  </script>
  
  <style scoped>
    .profile-container {
    max-width: 800px; /* 2배로 증가 */
    margin: 50px auto;
    padding: 40px; /* 2배로 증가 */
    border: 1px solid #dcdcdc;
    border-radius: 8px;
    background-color: #f9f9f9;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 2배로 증가 */
    text-align: center;
    }
  
    h1 {
    color: #333;
    margin-bottom: 40px; /* 2배로 증가 */
    font-size: 3em; /* 폰트 크기 증가 */
    }

    .profile-form {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
  
    .form-group {
    width: 100%;
    margin-bottom: 30px; /* 2배로 증가 */
    }

    .form-group label {
    display: block;
    margin-bottom: 10px; /* 2배로 증가 */
    font-weight: bold;
    color: #555;
    font-size: 1.2em; /* 폰트 크기 증가 */
    }

    .form-group input {
    width: 100%;
    padding: 16px; /* 2배로 증가 */
    border: 1px solid #dcdcdc;
    border-radius: 4px;
    box-sizing: border-box;
    font-size: 1.2em; /* 폰트 크기 증가 */
    }
  
  .update-button {
    padding: 10px 20px;
    border: none;
    background-color: #1abc9c;
    color: #ffffff;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .update-button:hover {
    background-color: #16a085;
  }
  </style>
  