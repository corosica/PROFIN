<template>
  <div class="profile-container">
    <h1>회원정보 수정</h1>
    <table class="profile-table">
      <tr>
        <th>닉네임</th>
        <td>
          <div class="profile-header">
            <div>
              <input type="text" name="nickname" v-model="nickname">
            </div>
          </div>
        </td>
      </tr>
      <tr>
        <th>이메일</th>
        <td>
          <input type="email" name="email" v-model="email"> 
        </td>
      </tr>
      <tr>
          <th>나이</th>
          <td><input type="number" name="age" id="age" v-model="age"></td>
        </tr>
      <tr>
        <th>성별</th>
        <td>
          <div class="gender-options no-wrap">
            <label class="gender-option">
              <input name="gender" value="남성" type="radio" v-model="gender" :selected="(gender == '남성')">
              남성
            </label>
            <label class="gender-option">
              <input name="gender" value="여성" type="radio" v-model="gender" :selected="(gender == '여성')">
              여성
            </label>
            <label class="gender-option">
              <input name="gender" value="비공개" type="radio" v-model="gender" :selected="(gender == '비공개')">
              비공개
            </label>
          </div>
        </td>
      </tr>
      <tr>
        <th>자산 (만원단위)</th>
        <td><input type="number" name="asset" id="asset" v-model="asset"></td>
      </tr>
      <tr>
        <th>직업</th>
        <td><input type="text" name="job" id="job" v-model="job"></td>
      </tr>
      <tr>
        <th>목적</th>
        <td>
          <select id="goal" v-model="goal" required>
            <option value="무계획" :selected="(gender == '무계획')">무계획</option>
            <option value="안전형" :selected="(gender == '안전형')">안전형</option>
            <option value="수익형" :selected="(gender == '수익형')">수익형</option>
          </select>
        </td>
      </tr>
    </table>
    <div class="button-group">
      <button class="btn btn-primary" @click="editProfile">저장하기</button>
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
const asset = ref(0);
const age = ref(0);
const job = ref('');
const goal = ref('');
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
      age.value = userData.age;
      asset.value = userData.asset;
      job.value = userData.job;
      goal.value = userData.goal;
      console.log('check');
    }
  } catch (error) {
    console.error('Failed to load user data:', error);
  }
});

const editProfile = () => {
  counterStore.changeUserInfo(nickname.value,email.value,age.value,gender.value,asset.value,goal.value,job.value);
};

const goBack = () => {
  router.go(-1);
};
</script>

<style scoped>
.profile-container {
  width: 100%;
  max-width: 800px;
  margin: 50px auto;
  padding: 40px;
  border: 1px solid #dcdcdc;
  border-radius: 8px;
  background-color: #ffffff;
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

.gender-options {
    display: flex;
    gap: 50px;
  }
  
.no-wrap {
  white-space: nowrap;
}

input,
select {
  width: 100%;
  padding: 8px;
  border: 1px solid #dcdcdc;
  border-radius: 4px;
  box-sizing: border-box;
}
</style>
