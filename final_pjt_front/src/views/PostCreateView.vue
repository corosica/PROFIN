<template>
  <div class="container mt-4">
    <div class="card">
      <div class="card-body">
        <h1 class="card-title text-center mb-4">게시글 작성</h1>
        <form @submit.prevent="createPost">
        <div class="form-group mb-3">
          <label for="title">제목</label>
          <input type="text" id="title" v-model="title" required>
        </div>
        <br>
        <div class="form-group mb-3">
          <label for="content">내용</label>
          <textarea id="content" v-model="content" required></textarea>
        <br>
        </div>
        <div class="text-center">
          <button type="submit">작성</button>
          <button type="button" @click="cancel">취소</button>
        </div>
      </form>
      </div>
    </div>
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
  
  const createPost = () => {
  if (localStorage.getItem('token') == null) {
  alert('로그인을 해주세요'); // 나중에 before enter로 처리
  router.push('/login');    
} else {
  counterStore.viewArticles()
  counterStore.createArticles(title.value, content.value);
  router.push({name:'Community'});  
}
}
  
  const cancel = () => {
    router.push({name:'Community'});
  };
  </script>
  
<style scoped>
.container {
  max-width: 800px;
}

.card {
  background-color: #ffffff; /* 흰색 배경 */
  border: 1px solid #dcdcdc; /* 회색 선 */
  border-radius: 8px;
  padding: 20px;
}

.card-title {
  color: #333333; /* 제목 색상 */
}

.form-control {
  border: 1px solid #dcdcdc; /* 회색 선 */
}

.btn-primary {
  background-color: #00796b; /* 민트색 버튼 */
  border-color: #00796b;
}

.btn-primary:hover {
  background-color: #004d40; /* 버튼 호버 색상 */
  border-color: #004d40;
}

.btn-secondary {
  background-color: #6c757d; /* secondary 버튼 색상 */
  border-color: #6c757d;
}

.btn-secondary:hover {
  background-color: #5a6268; /* secondary 버튼 호버 색상 */
  border-color: #545b62;
}

</style>
  