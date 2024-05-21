<template>
  <footer class="footer">
    <div class="footer-top">
      <div class="footer-links">
        <RouterLink to="/">소개</RouterLink>
        <RouterLink to="/question">자주 묻는 질문</RouterLink>
        <RouterLink to="/contact">문의하기</RouterLink>
      </div>
    </div>
    <div class="footer-bottom">
      <p>Copyright &copy; 2024 SSAFY by 부울경 2반 정진우 정유진</p>
    </div>
  </footer>
</template>

<script setup>
</script>

<style scoped>
.footer {
  background-color: #f9f9f9;
  padding: 10px; 
  color: #333;
  font-family: Arial, sans-serif;
  font-size: 0.8rem; 
}

.footer-top {
  display: flex;
  justify-content: space-between;
  border-bottom: 1px solid #ddd;
  padding-bottom: 7px; 
  margin-bottom: 7px; 
}

.footer-links {
  display: flex;
  gap: 20px; /* 간격을 줄여서 크기를 70%로 만듭니다 */
}

.footer-links a {
  text-decoration: none;
  color: #333;
}

.footer-links a:hover {
  text-decoration: underline;
}

.footer-bottom {
  font-size: 0.7rem; 
  line-height:1; 
}
</style>
