<template>
  <div class="container mt-4">
    <div class="card">
      <div class="card-body">
        <h1 class="card-title text-center mb-4">게시글 목록</h1>
        <div v-if="loading" class="text-center">
          <p class="text-muted">Loading 중...</p>
        </div>
        <div v-else>
          <ul class="list-group">
            <li v-for="post in posts" :key="post.id" class="list-group-item mb-3">
              <p>글 번호: {{ post.id }}</p>
              <RouterLink :to="{ name: 'PostDetail', params: { id: post.id } }" class="text-decoration-none">
                <h5 class="mb-0">{{ post.title }}</h5>
              </RouterLink>
            </li>
          </ul>
        </div>
        <div class="text-center mt-4">
          <button @click.prevent="writePost" class="write-btn">
            글쓰기
          <!-- <RouterLink :to="{ name: 'PostCreate' }">게시글 작성</RouterLink> -->
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router';

const counterStore = useCounterStore();
const posts = ref([]);
const loading = ref(true);

const router = useRouter()
onMounted(async () => {
  try {
    await counterStore.viewArticles();
    posts.value = counterStore.articleList;
  } catch (error) {
    console.error('failed to view articles', error);
  } finally {
    loading.value = false;
    console.log(counterStore.articleList);
  }
});

const writePost = function () {
  router.push({ name: 'PostCreate' })
}
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

.list-group-item {
  border: 1px solid #dcdcdc; /* 회색 선 */
  border-radius: 8px;
}

.text-decoration-none {
  color: #058677; /* 민트색 링크 */
}

.text-decoration-none:hover {
  color: #034e35; /* 링크 호버 색상 */
}

.btn-primary {
  background-color: #00796b; /* 민트색 버튼 */
  border-color: #00796b;
}

.btn-primary:hover {
  background-color: #004d40; /* 버튼 호버 색상 */
  border-color: #004d40;
}

.write-btn {
    display: block;
    margin-left: auto;
    padding: 10px 20px;
    border: none;
    background-color: #1abc9c;
    color: #ffffff;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.write-btn:hover {
    background-color: #16a085;
}

</style>
