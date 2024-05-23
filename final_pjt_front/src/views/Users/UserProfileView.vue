<template>
  <div class="d-flex row">
    <div class="sidebar col-2">
      <p @click="navigate('Profile')">내 정보</p>
      <p @click="navigate('Attendance')">출석 체크</p>
      <p @click="navigate('Products')">가입한 상품</p>
      <p @click="navigate('Portfolio')">포트폴리오</p>

    </div>
    <div class="container col">
      <RouterView />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const navigate = (parameter) => {
  router.push({ name: parameter });
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');

* {
  font-family: 'Noto Sans KR', sans-serif; /* 전역 폰트 적용 */
}

.sidebar {
  padding: 20px;
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
}

.profile-container {
  width: 100%;
  max-width: 800px;
  padding: 40px;
  border: 1px solid #e0e0e0;
  border-radius: 10px;
  background-color: #ffffff;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  text-align: center;
  margin-bottom: 20px;
}

h1 {
  color: #333;
  margin-bottom: 30px;
  font-size: 2rem;
  font-weight: bold;
}

.profile-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 30px;
}

.profile-table th,
.profile-table td {
  border: 1px solid #e0e0e0;
  padding: 12px 15px;
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
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
}

.btn-primary {
  background-color: #007bff;
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
  background-color: #343a40;
  color: #ffffff;
}
</style>