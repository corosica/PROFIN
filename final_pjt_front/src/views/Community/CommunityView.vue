<template>
  <div class="container mt-4">
    <div class="card">
      <div class="card-body">
        <h1 class="card-title text-center mb-4">게시판</h1>
        <div class="board-header">
          <select v-model="searchCriteria" class="category">
            <option value="title">제목</option>
            <option value="content">내용</option>
            <option value="author">글쓴이</option>
          </select>
          <input
            type="text"
            v-model="searchQuery"
            placeholder="검색어를 입력하세요"
            class="search-input"
            @keyup.enter="searchPosts"
          />
          <button @click="searchPosts" class="search-button">검색</button>
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
          <button
            v-for="page in totalPages"
            :key="page"
            @click="changePage(page)"
            :class="{ active: page === currentPage }"
          >{{ page }}</button>
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
import { ref, onMounted, computed } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router';

const counterStore = useCounterStore();
const posts = ref([]);
const filteredPosts = ref([]);
const loading = ref(true);
const searchQuery = ref('');
const searchCriteria = ref('title');
const currentPage = ref(1);
const perPage = 10;
const totalPages = ref(1);

const router = useRouter();

onMounted(async () => {
  try {
    await counterStore.viewArticles('community');
    posts.value = counterStore.articleList.slice().reverse(); // 게시글을 역순으로 정렬
    filteredPosts.value = posts.value;
    totalPages.value = Math.ceil(filteredPosts.value.length / perPage);
  } catch (error) {
    console.error('failed to view articles', error);
  } finally {
    loading.value = false;
    console.log(counterStore.articleList);
  }
});

const writePost = () => {
  router.push({ name: 'PostCreate' });
};

const formatDate = (datetime) => {
  const datePart = datetime.split('T')[0];
  const [year, month, day] = datePart.split('-');
  return `${month}-${day}`;
};

const currentPagePosts = computed(() => {
  const startIndex = (currentPage.value - 1) * perPage;
  const endIndex = startIndex + perPage;
  return filteredPosts.value.slice(startIndex, endIndex);
});

const searchPosts = () => {
  if (!searchQuery.value) {
    filteredPosts.value = posts.value.slice().reverse(); // 원래 게시글 목록 역순으로 정렬
  } else {
    filteredPosts.value = posts.value.filter(post => {
      if (searchCriteria.value === 'title') {
        return post.title.toLowerCase().includes(searchQuery.value.toLowerCase());
      } else if (searchCriteria.value === 'content') {
        return post.content.toLowerCase().includes(searchQuery.value.toLowerCase());
      } else if (searchCriteria.value === 'author') {
        return post.user.nickname.toLowerCase().includes(searchQuery.value.toLowerCase());
      }
    });
  }
  currentPage.value = 1; // 검색 결과가 바뀌면 첫 페이지로 이동
  totalPages.value = Math.ceil(filteredPosts.value.length / perPage);
};

const changePage = (page) => {
  currentPage.value = page;
};

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
};

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
  }
};
</script>


<style scoped>

.container {
  max-width: 1100px;
}

.card {
  background-color: #ffffff;
  border: 1px solid #dcdcdc;
  border-radius: 8px;
  padding: 20px;
}

.card-title {
  color: #333333;
}

.board-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.category, .search-input, .search-button {
  padding: 5px;
  border: 1px solid #dcdcdc;
  border-radius: 4px;
}

.search-input {
  flex-grow: 1;
  margin-left: 10px;
}

.search-button {
  margin-left: 10px;
  background-color: #1abc9c;
  color: #ffffff;
  cursor: pointer;
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
  color: #000000;
  text-decoration: none;
}

.text-decoration-none:hover {
  color: #1abc9c;
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
