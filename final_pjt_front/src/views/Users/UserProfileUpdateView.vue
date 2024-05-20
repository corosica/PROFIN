<template>
    <div class="signup-container">
      <h1>회원정보 수정</h1>
      <br>
      <form @submit.prevent="signup" class="signup-form">
        <div class="form-group">
          <label for="username">아이디: </label>
          <input type="text" id="username" v-model="username" required>
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
        <div class="form-group">
          <label>성별: </label>
          <div class="gender-options no-wrap">
            <label class="gender-option">
              <input name="gender" value="남성" type="radio" v-model="gender">
              남성
            </label>
            <label class="gender-option">
              <input name="gender" value="여성" type="radio" v-model="gender">
              여성
            </label>
            <label class="gender-option">
              <input name="gender" value="비공개" type="radio" v-model="gender">
              비공개
            </label>
          </div>
        </div>
        <div class="form-group">
          <label for="asset">자산: </label>
          <input type="number" id="asset" v-model="asset">
        </div>
        <div class="form-group">
          <label for="goal">목표: </label>
          <select id="goal" v-model="goal" required>
            <option value="" disabled selected>목표를 선택하세요</option>
            <option value="무계획">무계획</option>
            <option value="안정형">안정형</option>
            <option value="수익형">수익형</option>
          </select>
        </div>
        <div class="form-group">
          <label for="job">직업: </label>
          <input type="text" id="job" v-model="job">
        </div>
        <br>
        <div class="form-group form-buttons">
          <button type="submit" class="save-button">저장</button>
        </div>
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
  const confirmPassword = ref('');
  const nickname = ref('');
  const age = ref('');
  const gender = ref('male'); // 성별 선택을 위한 변수
  const asset = ref('');
  const goal = ref('무계획'); // 드롭다운 기본값 설정
  const job = ref('');
  const router = useRouter();
  const counterStore = useCounterStore();
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
  
  .form-group input,
  .form-group select {
    width: 100%;
    padding: 8px;
    border: 1px solid #dcdcdc;
    border-radius: 4px;
    box-sizing: border-box;
  }
  
  .gender-options {
    display: flex;
    gap: 50px;
  }
  
  .no-wrap {
    white-space: nowrap;
  }

  .form-buttons {
    display: flex;
    justify-content: center; /* 버튼을 가운데 정렬 */
  }
  
  .save-button {
    width: 100px;
    padding: 10px 15px;
    border: none;
    background-color: #1abc9c;
    color: #ffffff;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .save-button:hover {
    background-color: #16a085;
  }
  </style>
  