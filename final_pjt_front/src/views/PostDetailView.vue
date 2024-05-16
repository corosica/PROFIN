<template>
    <div>
        {{ post.content }}
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRoute } from 'vue-router';
  
  const route = useRoute();
  const post = ref({});
  
  const posts = [
    { id: 1, title: '첫 번째 게시글', content: '첫 번째 게시글 내용' },
    { id: 2, title: '두 번째 게시글', content: '두 번째 게시글 내용' },
    // 추가 게시글 데이터를 여기에 작성할 수 있습니다.
  ];
  
  post.value = posts.find(p => p.id === Number(route.params.id));
  </script>
  
  <style scoped>
  /* 최소한의 스타일링만 추가 */
  </style>
  