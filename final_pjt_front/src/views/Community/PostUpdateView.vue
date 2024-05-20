<template>
  <div class="container mt-4">
    <div class="card shadow-sm">
      <div class="card-body">
        <h3 class="card-title text-center mb-4">게시글 수정</h3>
        <form @submit.prevent="createPost">
          <div class="form-group mb-3">
            <label for="title">제목</label>
            <input type="text" id="title" class="form-control" v-model="title" placeholder="제목을 입력해주세요" required>
          </div>
          <div class="form-group mb-3">
            <label for="content">내용</label>
            <textarea id="content" class="form-control" rows="5" v-model="content" placeholder="내용을 입력해주세요" required></textarea>
          </div>

          <div class="text-end">
            <button type="submit" class="btn btn-primary me-2">작성</button>
            <button type="button" class="btn btn-secondary" @click="cancel">취소</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

  
  <script setup>
  import { onMounted, ref } from 'vue'
  import { useRouter, useRoute } from 'vue-router'
  import { useCounterStore } from '@/stores/counter'
  
  const router = useRouter()
  const route = useRoute()
  const counterStore = useCounterStore()
  const title = ref('')
  const content = ref('')
  title.value = counterStore.title 
  content.value = counterStore.content

  
  const updatePost = async () => {
    try {
      await counterStore.updateArticle(route.params.id,title.value,content.value)
      alert('게시글이 수정되었습니다.')
      router.push({ name:'PostDetail', params: { id: route.params.id }})
    }  catch (error) {
      console.error('Failed to update post:', error)
      alert('게시글 수정에 실패했습니다.')
    }
  }
  const cancel = () => {
    router.push({ name:'PostDetail', params: { id: route.params.id }});
  };
  </script>
  <style scoped>
  .container {
    max-width: 800px;
    margin: auto;
  }
  
  .card {
    background-color: #ffffff; /* 흰색 배경 */
    border: 1px solid #dcdcdc; /* 회색 선 */
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 그림자 효과 */
  }
  
  .card-title {
    color: #333333; /* 제목 색상 */
    font-weight: bold;
  }
  
  .form-group label {
    font-weight: bold;
    color: #555555; /* 라벨 색상 */
  }
  
  .form-control {
    border: 1px solid #dcdcdc; /* 회색 선 */
    border-radius: 4px;
    padding: 10px;
  }
  
  .form-control-file {
    border: none;
  }
  
  .btn {
    padding: 10px 20px;
    border-radius: 4px;
  }
  
  .btn-primary {
    background-color: #04bea8; /* 민트색 버튼 */
    border-color: #04bea8;
  }
  
  .btn-primary:hover {
    background-color: #02a78b; /* 버튼 호버 색상 */
    border-color: #02a78b;
  }
  
  .btn-secondary {
    background-color: #bcc1c5; /* secondary 버튼 색상 */
    border-color: #bcc1c5;
  }
  
  .btn-secondary:hover {
    background-color: #a3a7a9; /* secondary 버튼 호버 색상 */
    border-color: #a3a7a9;
  }
  </style>
  