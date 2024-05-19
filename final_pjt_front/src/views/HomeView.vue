<template>
    <div>
      <h1>홈페이지</h1>
      <p>여기는 홈페이지입니다. 커뮤니티 페이지로 이동하려면 아래 링크를 클릭하세요.</p>
    </div>
  </template>
  
  <script setup>
  import { onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  const router = useRouter()

</script>
  
  <style scoped>
  /* 최소한의 스타일링만 추가 */
  </style>
  