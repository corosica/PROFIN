<template>
  <div class="container mt-4">
    <div class="card">
      <div class="card-body">
        <h1 class="card-title text-center mb-4">게시판</h1>
        <div class="board-header">
          <select class="category">
            <option>검색</option>
          </select>
          <input type="text" placeholder="검색어를 입력하세요" class="search-input">
        </div>
        <div v-if="loading" class="text-center">
          <p class="text-muted">Loading 중...</p>
        </div>
        <div v-else>
          <table class="board-table">
            <thead>
              <tr>
                <th>번호</th>
                <th>제목</th>
                <th>글쓴이</th>
                <th>날짜</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="post in posts" :key="post.id">
                <td>{{ post.id }}</td>
                <td>
                  <RouterLink :to="{ name: 'PostDetail', params: { id: post.id } }" class="text-decoration-none">
                    {{ post.title }}
                  </RouterLink>
                </td>
                <td>{{ post.user_id }}</td>
                <td>{{ formatDate(post.created_at) }}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="pagination">
          <button>&lt;</button>
          <button class="active">1</button>
          <button>2</button>
          <button>3</button>
          <button>4</button>
          <button>&gt;</button>
        </div>
        <div class="text-center mt-4">
          <button @click.prevent="writePost" class="write-btn">
            글쓰기
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

const router = useRouter();
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
  router.push({ name: 'PostCreate' });
}

const formatDate = (datetime) => {
  return datetime.split('T')[0];
};

</script>

<style scoped>
.container {
  max-width: 1000px;
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

.board-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.category, .search-input {
  padding: 5px;
  border: 1px solid #dcdcdc;
  border-radius: 4px;
}

.search-input {
  flex-grow: 1;
  margin-left: 10px;
}

.board-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
}

.board-table th, .board-table td {
  border: 1px solid #dcdcdc;
  padding: 10px;
  text-align: left;
}

.board-table th {
  background-color: #f2f2f2;
}

.text-decoration-none {
  color: #058677; /* 민트색 링크 */
  text-decoration: none;
}

.text-decoration-none:hover {
  color: #034e35; /* 링크 호버 색상 */
}

.write-btn {
  display: inline-block;
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

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 5px;
  margin-bottom: 20px;
}

.pagination button {
  padding: 5px 10px;
  border: 1px solid #dcdcdc;
  background-color: #ffffff;
  cursor: pointer;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.pagination button.active, .pagination button:hover {
  background-color: #1abc9c;
  color: #ffffff;
}
</style>
