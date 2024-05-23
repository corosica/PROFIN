<template>
    <div class="attendance-container">
      <AttendanceCheck />
      <button class="attendance-button" @click="checkAttendance">출석체크</button>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  import AttendanceCheck from '@/components/AttendanceCheck.vue';
  import axios from 'axios';
  
  const router = useRouter();
  const message = ref('');
  
  const checkAttendance = async () => {
    try {
      const response = await axios({
        method: 'POST',
        url: 'http://127.0.0.1:8000/api/v1/outerapi/attendance/',
        headers: {
          Authorization: sessionStorage.getItem('token'),
        },
      });
      message.value = response.data.message;
    } catch (error) {
      if (error.response) {
        message.value = error.response.data.message;
      } else {
        message.value = 'An error occurred.';
      }
    } finally {
      alert(message.value);
    }
  };
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');
  
  * {
    font-family: 'Noto Sans KR', sans-serif; /* 전역 폰트 적용 */
  }
  
  .attendance-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
  }
  
  .attendance-button {
    margin:0 200px 60px 0px;
    padding: 10px 20px;
    background-color: #1abc9c;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 18px;
    transition: background-color 0.3s, color 0.3s;
  }
  
  .attendance-button:hover {
    background-color: #16a085;
  }
  </style>
  