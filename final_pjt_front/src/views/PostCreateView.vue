<template>
    <div>
      <h1>게시글 작성</h1>
      <form @submit.prevent="submit">
        <label for="title">제목</label>
        <input type="text" id="title" v-model="title" required>
        <br>
        <label for="content">내용</label>
        <textarea id="content" v-model="content" required></textarea>
        <br>
        <button type="submit">작성</button>
        <button type="button" @click="cancel">취소</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  
  const title = ref('');
  const content = ref('');
  const router = useRouter();
  
  const submit = () => {
  if (!title.value) {
    alert('제목을 입력하세요.');
  } else if (!content.value) {
    alert('내용을 입력하세요.');
  } else {
    console.log('Title:', title.value);
    console.log('Content:', content.value);
    router.push('/community');
  }
};
  
  const cancel = () => {
    router.push('/community');
  };
  </script>
  
  <style scoped>
  </style>
  