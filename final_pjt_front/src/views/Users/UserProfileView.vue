<template>
    <div class="profile-container">
      <h1>회원정보</h1>
      <table class="profile-table">
        <tr>
          <th>프로필</th>
          <td>
            <div class="profile-header">
              <div>
                <p>{{ nickname }}님 환영합니다</p>
                <p>보유 포인트: <span class="points">{{ formatPoints(points) }}  p</span> <button class="btn-recharge">충전하기</button></p>
              </div>
            </div>
          </td>
        </tr>
        <tr>
          <th>이메일</th>
          <td>{{ email }}</td>
        </tr>
        <tr>
          <th>나이</th>
          <td>{{ age }} 살</td>
        </tr>
        <tr>
          <th>성별</th>
          <td>{{ gender }}</td>
        </tr>
        <tr>
          <th>자산</th>
          <td>{{ asset }} 만원</td>
        </tr>
        <tr>
          <th>직업</th>
          <td>{{ job }}</td>
        </tr>
        <tr>
          <th>목적</th>
          <td>{{ goal }}</td>
        </tr>
      </table>
      <div class="button-group">
        <button class="btn btn-secondary" @click="changePassword">비밀번호 변경</button>
        <button class="btn btn-primary" @click="editProfile">회원정보 수정</button>
        <button class="btn btn-outline-dark" @click="goBack">뒤로가기</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import { useCounterStore } from '@/stores/counter';
  
  const username = ref('');
  const email = ref('');
  const nickname = ref('');
  const gender = ref('');
  const asset = ref('');
  const age = ref(0);
  const job = ref('');
  const goal = ref('');
  const points = ref(0);
  const router = useRouter();
  const counterStore = useCounterStore();
  
  onMounted(async () => {
    try {
      await counterStore.getUserInfo();
      const userData = counterStore.userInfos;
      if (userData) {
        username.value = userData.username;
        email.value = userData.email;
        nickname.value = userData.nickname;
        gender.value = userData.gender;
        asset.value = userData.asset;
        job.value = userData.job;
        goal.value = userData.goal;
        age.value = userData.age;
        points.value = userData.points;
      }
    } catch (error) {
      console.error('Failed to load user data:', error);
    }
  });
  
  const changePassword = () => {
    // 비밀번호 변경 로직
  };
  function formatPoints(value) {
      return value.toLocaleString();
    }
  const editProfile = () => {
    router.push({name:'UserProfileUpdate'})
  };
  
  const goBack = () => {
    router.go(-1);
  };
  </script>
  
  <style scoped>
  .profile-container {
    max-width: 800px;
    margin: 50px auto;
    padding: 40px;
    border: 1px solid #dcdcdc;
    border-radius: 8px;
    background-color: #f9f9f9;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: center;
  }
  
  h1 {
    color: #333;
    margin-bottom: 40px;
    font-size: 2em;
  }
  
  .profile-table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 30px;
  }
  
  .profile-table th,
  .profile-table td {
    border: 1px solid #dcdcdc;
    padding: 15px;
    text-align: left;
  }
  
  .profile-table th {
    background-color: #f0f0f0;
    width: 150px;
  }
  
  .profile-header {
    display: flex;
    align-items: center;
  }
  
  .profile-img {
    width: 70px;
    height: 70px;
    margin-right: 20px;
  }
  
  .profile-image {
    width: 100%;
    height: 100%;
    border-radius: 50%;
  }
  
  .points {
    color: #1abc9c;
    font-weight: bold;
  }
  
  .btn-recharge {
    background-color: #dcdcdc;
    border: none;
    padding: 5px 10px;
    margin-left: 10px;
    cursor: pointer;
    border-radius: 4px;
  }
  
  .btn-recharge:hover {
    background-color: #c0c0c0;
  }
  
  .button-group {
    display: flex;
    justify-content: space-around;
    margin-top: 20px;
  }
  
  .btn {
    padding: 10px 20px;
    border-radius: 4px;
    font-weight: bold;
    cursor: pointer;
    transition: background-color 0.3s, color 0.3s;
  }
  
  .btn-secondary {
    background-color: #6c757d;
    border: 1px solid #6c757d;
    color: #ffffff;
  }
  
  .btn-secondary:hover {
    background-color: #5a6268;
    border-color: #5a6268;
    color: #ffffff;
  }
  
  .btn-primary {
    background-color: #007bff;
    border: 1px solid #007bff;
    color: #ffffff;
  }
  
  .btn-primary:hover {
    background-color: #0056b3;
    border-color: #0056b3;
    color: #ffffff;
  }
  
  .btn-outline-dark {
    background-color: transparent;
    border: 1px solid #343a40;
    color: #343a40;
  }
  
  .btn-outline-dark:hover {
    background-color: #a8a8a8;
    color: #ffffff;
    border: 1px solid #a8a8a8;
  }
  </style>
  