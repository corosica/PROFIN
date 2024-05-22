<template>
  <div class="main-container">
    <div class="header">
      <h1>기본 추천</h1>
    </div>
    <p style="font-size: smaller; color: red;">제공된 추천 정보는 세션 만료시까지 유지됩니다.</p>
    <button @click.prevent="showModal" class="recommend-btn">추천 받기</button>
    <ul class="recommend-list">
      <li v-for="recommend in recommendedList" :key="recommend.id" class="recommend-item">
        <div class="recommend-info">
          <span class="recommend-name">상품명: {{ recommend.name }}</span>
          <span class="recommend-type">종류: {{ recommend.type }}</span>
        </div>
        <button 
          @click.prevent="router.push({ name: 'DepositDetail', params: { id: recommend.id } })"
          v-if="recommend.type === '예금'"
          class="detail-btn"
        >
          상품 보러가기
        </button>
        <button 
          @click.prevent="router.push({ name: 'SavingDetail', params: { id: recommend.id } })"
          v-else
          class="detail-btn"
        >
          상품 보러가기
        </button>
      </li>
    </ul>
    <Modal :visible="isModalVisible" :message="modalMessage" @confirm="handleConfirm" @cancel="handleCancel" />
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import Modal from '@/components/Modal.vue';

const router = useRouter();
const counterStore = useCounterStore();
const recommendedList = ref([]);
const isModalVisible = ref(false);
const modalMessage = ref('<strong>100 포인트</strong>가 차감됩니다<br>계속하시겠습니까?');

const showModal = () => {
  isModalVisible.value = true;
};
onMounted(() => {
  recommendedList.value = JSON.parse(sessionStorage.getItem('normalRecommendList'));
  console.log(recommendedList.value);
})
const handleConfirm = async () => {
  isModalVisible.value = false;
  sessionStorage.removeItem('normalRecommendList');
  await counterStore.normalRecommend();
  recommendedList.value = counterStore.normalRecommendList;
  sessionStorage.setItem('normalRecommendList', JSON.stringify(counterStore.normalRecommendList));
  console.log(recommendedList.value);
};

const handleCancel = () => {
  isModalVisible.value = false;
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');

* {
  font-family: 'Noto Sans KR', sans-serif; /* 전역 폰트 적용 */
}

.main-container {
  position: relative;
  right: 10.5%; /* 화면 왼쪽에서 10.5% 위치 조정 */
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  font-family: Arial, sans-serif;
}

.header {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
}

h1 {
  color: #333;
  font-size: 2em;
  margin: 0;
}

.recommend-btn {
  display: block;
  margin: 0 auto 20px auto;
  background-color: #1abc9c;
  border: 1px solid #1abc9c;
  color: #ffffff;
  padding: 10px 20px;
  font-size: 1em;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.recommend-btn:hover {
  background-color: #17a387;
  color: #ffffff;
  border: 1px solid #1abc9c;
}

.recommend-list {
  list-style: none;
  padding: 10px;
  margin: 10px;
}

.recommend-item {
  display: flex;
  grid-template-columns: 1fr auto;
  justify-content: space-between;
  align-items: center;
  background-color: #ffffff;
  margin-bottom: 10px;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s;
  box-sizing: border-box;
}

.recommend-item:hover {
  transform: translateY(-5px);
}

.recommend-info {
  text-align: left;
  width: 400px;
}

.recommend-name, .recommend-type {
  display: block;
  color: #333;
  font-size: 1em;
  margin-bottom: 5px;
}

.detail-btn {
  background-color: #ffffff;
  color: #1abc9c;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease, color 0.3s ease;
  border: 2px solid #1abc9c;
}

.detail-btn:hover {
  background-color: #1abc9c;
  color: #ffffff;
}
</style>
