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
                <th class="col-number">번호</th>
                <th class="col-title">제목</th>
                <th class="col-author">글쓴이</th>
                <th class="col-date">날짜</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="post in currentPagePosts" :key="post.id">
                <td>{{ post.id }}</td>
                <td>
                  <RouterLink :to="{ name: 'PostDetail', params: { id: post.id } }" class="text-decoration-none">
                    {{ post.title }}
                  </RouterLink>
                </td>
                <td>{{ post.user.nickname }}</td>
                <td>{{ formatDate(post.created_at) }}</td>
              </tr>
            </tbody>
          </table>
        </div>
        <div class="pagination">
          <button @click="prevPage" :disabled="currentPage === 1">&lt;</button>
          <button v-for="page in totalPages" :key="page" @click="changePage(page)" :class="{ 'active': page === currentPage }">{{ page }}</button>
          <button @click="nextPage" :disabled="currentPage === totalPages">&gt;</button>
        </div>
        
        <div class="text-center mt-4 write-btn-container">
          <button @click.prevent="writePost" class="write-btn">
            글쓰기
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted,watch,computed } from 'vue';
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
  const datePart = datetime.split('T')[0];
  const [year, month, day] = datePart.split('-');
  return `${month}-${day}`;
};

const currentPagePosts = computed(() => {
  const startIndex = (currentPage.value - 1) * perPage;
  const endIndex = startIndex + perPage;
  return posts.value.slice(startIndex, endIndex);
});


const perPage = 10; // 페이지당 게시글 수
let currentPage = ref(1); // 현재 페이지
const totalPages = ref(1); // 총 페이지 수

// 현재 페이지의 게시글 목록을 반환하는 함수
const getCurrentPagePosts = () => {
  const startIndex = (currentPage.value - 1) * perPage;
  const endIndex = startIndex + perPage;
  return posts.value.slice(startIndex, endIndex);
}

// 페이지 변경 시 호출되는 함수
const changePage = (page) => {
  currentPage.value = page;
}

// 이전 페이지로 이동하는 함수
const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
}

// 다음 페이지로 이동하는 함수
const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
  }
}

// 페이지별 게시글 목록을 계산하는 함수
watch(posts, () => {
  totalPages.value = Math.ceil(posts.value.length / perPage);
  currentPage.value = 1;
});
</script>

<style scoped>
.container {
  max-width: 1100px;
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
  color: #000000; /* 민트색 링크 */
  text-decoration: none;
}

.text-decoration-none:hover {
  color: #1abc9c; /* 링크 호버 색상 */
}

.write-btn-container {
  display: flex;
  justify-content: flex-end;
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

.col-number {
  width: 10%;
  text-align: center;
}

.col-title {
  width: 65%;
}

.col-author {
  width: 15%;
  text-align: center;
}

.col-date {
  width: 10%;
  text-align: center;
}

</style>
