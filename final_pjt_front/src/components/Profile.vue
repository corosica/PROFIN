<template>
    <div class="main-container">
      <div class="profile-container">
        <h1>회원정보</h1>
        <table class="profile-table">
          <tr>
            <th>프로필</th>
            <td>
              <div class="profile-header">
                <div>
                  <p>{{ nickname }}님 환영합니다</p>
                  <p>보유 포인트: <span class="points">{{ formatPoints(points) }}  p</span> <button class="btn-recharge" @click.prevent="AddPoint">충전하기</button></p>
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
          <button class="btn btn-primary" @click="editProfile">회원정보 수정</button>
          <button class="btn btn-outline-dark" @click="goBack">뒤로가기</button>
        </div>
      </div>
    </div>
    </template>
    
    <script setup>
    import { ref, onMounted } from 'vue';
    import { useRouter } from 'vue-router';
    import { useCounterStore } from '@/stores/counter';
    import axios from 'axios';
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
        console.log(userData);
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
    
    const AddPoint = async () => {
      await axios ({
        method : 'PATCH',
        url : 'http://127.0.0.1:8000/accounts/user/',
        headers: {
          Authorization: sessionStorage.getItem('token'),
        },
        data: {
        points : points.value + 10000,
        }
      }).then((response) => {
        router.go(0);
      }).catch((err) => {
        console.error('Failed to fetch userInfo:', err);
      })
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
    
    .sidebar {
      padding: 20px;
      position: fixed;
      width: 400px;
      text-align: left;
      padding-left: 200px;
    }
    
    .sidebar p {
      font-size: 24px;
      color: #333;
      font-weight: bold;
      margin-bottom: 25px;
      cursor: pointer;
      transition: color 0.3s;
      padding-left: 10px; /* 글자를 더 왼쪽으로 이동 */
    }
    
    .sidebar p:hover {
      color: #1abc9c;
    }
    
    .main-container {
      padding: 20px;
      flex: 1;
      display: flex;
      justify-content: center;
      margin-right: 20%;
    }
    
    .profile-container {
      width: 100%;
      max-width: 800px;
      margin: 20px auto;
      padding: 40px;
      border: 1px solid #dcdcdc;
      border-radius: 10px;
      background-color: #ffffff;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      text-align: center;
    }
    
    h1 {
      color: #333;
      margin-bottom: 30px;
      font-size: 2rem;
    }
    
    .profile-table {
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 30px;
    }
    
    .profile-table th,
    .profile-table td {
      border: 1px solid #e0e0e0;
      padding: 15px;
      text-align: left;
      font-size: 16px;
    }
    
    .profile-table th {
      background-color: #f9f9f9;
      width: 150px;
    }
    
    .profile-header {
      display: flex;
      align-items: center;
    }
    
    .points {
      color: #1abc9c;
      font-weight: bold;
    }
    
    .btn-recharge {
      background-color: #1abc9c;
      border: none;
      color: white;
      padding: 5px 10px;
      margin-left: 10px;
      cursor: pointer;
      border-radius: 4px;
      transition: background-color 0.3s;
    }
    
    .btn-recharge:hover {
      background-color: #16a085;
    }
    
    .button-group {
      display: flex;
      justify-content: center;
      gap: 15px;
      margin-top: 20px;
    }
    
    .btn {
      padding: 10px 20px;
      border-radius: 5px;
      font-weight: bold;
      cursor: pointer;
      transition: background-color 0.3s, color 0.3s;
    }
    
    .btn-primary {
      background-color: #007bff;
      font-weight: 500;
      border: none;
      color: #ffffff;
    }
    
    .btn-primary:hover {
      background-color: #0056b3;
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
      