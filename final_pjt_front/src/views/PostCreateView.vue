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
  import { useCounterStore } from '@/stores/counter';
  const counterStore = useCounterStore()
  const title = ref('');
  const content = ref('');
  const router = useRouter();
  
  const submit = () => {
  if (counterStore.token == null) {
  alert('로그인을 해주세요'); // 나중에 before enter로 처리
  router.push('/login');    
} else {
  counterStore.createArticles(title.value, content.value);
  router.push({name:'Community'});  
}
}
  
  const cancel = () => {
    router.push('/community');
  };
  </script>
  
  <style scoped>
  </style>
  