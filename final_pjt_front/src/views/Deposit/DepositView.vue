<template>
  <div class="main-container">
    <div class="button-container">
      <RouterLink :to="{ name: 'DepositList' }" class="btn">예금 상품</RouterLink>
      <RouterLink :to="{ name: 'SavingList' }" class="btn">적금 상품</RouterLink>
    </div>
    <div class="container border">
      <RouterView />
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.main-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.button-container {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.btn {
  padding: 10px 20px;
  background-color: white; /* 기본 배경색을 흰색으로 설정 */
  color: #1abc9c; /* 기본 텍스트 색상을 초록색으로 설정 */
  text-decoration: none;
  border: 2px solid #1abc9c; /* 초록색 테두리 추가 */
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s, color 0.3s;
}

.btn:hover {
  background-color: #1abc9c; /* 호버 시 배경색을 초록색으로 변경 */
  color: white; /* 호버 시 텍스트 색상을 흰색으로 변경 */
}

.container.border {
  width: 100%;
  max-width: 1500px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  background-color: #f9f9f9;
}
</style>
