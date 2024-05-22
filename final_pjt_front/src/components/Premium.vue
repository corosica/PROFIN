<template>
  <div class="main-container">
    <div class="header">
      <h1>프리미엄 추천</h1>
    </div>
    <p class="info-text">제공된 추천 정보는 세션 만료시까지 유지됩니다.</p>
    <button @click.prevent="showModal" class="recommend-btn">추천 받기</button>
    <ul class="recommend-list row">
      <li v-for="recommend in recommendedList" :key="recommend.id" class="recommend-item col-6">
        <div class="recommend-info">
          <span class="recommend-name">상품명: {{ recommend.product_name }}</span>
          <span class="recommend-type">은행: {{ recommend.bank }}</span>
          <span class="recommend-type">종류: {{ recommend.type }}</span>
          <span class="recommend-type">기본 금리: {{ recommend.intr_rate }}%</span>
          <span class="recommend-type">최대 우대 금리: {{ recommend.intr_rate2 }}%</span>
          <span class="recommend-type">저축 기간: {{ recommend.save_trm }}개월</span>
        </div>
        <button 
          @click.prevent="router.push({ name: 'DepositDetail', params: { id: recommend.product_code } })"
          v-if="recommend.type === '예금'"
          class="detail-btn"
        >
          상품 보러가기
        </button>
        <button 
          @click.prevent="router.push({ name: 'SavingDetail', params: { id: recommend.product_code } })"
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
const modalMessage = ref('<strong>3000 포인트</strong>가 차감됩니다<br>계속하시겠습니까?');

const showModal = () => {
  isModalVisible.value = true;
};

onMounted(() => {
  recommendedList.value = JSON.parse(sessionStorage.getItem('premiumRecommendList'));
  console.log(recommendedList.value);
});

const handleConfirm = async () => {
  isModalVisible.value = false;
  sessionStorage.removeItem('premiumRecommendList');
  await counterStore.premiumRecommend();
  recommendedList.value = counterStore.premiumRecommendList;
  sessionStorage.setItem('premiumRecommendList', JSON.stringify(counterStore.premiumRecommendList));
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
  right: 10%;
  max-width: 80%;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease;
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

.info-text {
  font-size: smaller;
  color: red;
  text-align: center;
}

.recommend-btn {
  display: block;
  margin: 0 auto 20px auto;
  background-color: #1abc9c;
  border: 2px solid #1abc9c;
  color: #ffffff;
  padding: 10px 20px;
  font-size: 1em;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.recommend-btn:hover {
  background-color: #17a387;
  color: #ffffff;
  border: 1px solid #1abc9c;
}

.recommend-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-wrap: wrap;
}

.recommend-item {
  display: grid;
  grid-template-columns: 1fr auto;
  align-items: center;
  background-color: #ffffff;
  margin: 10px;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s;
  flex: 1 0 48%;
  box-sizing: border-box;
}

.recommend-item:hover {
  transform: translateY(-5px);
}

.recommend-info {
  text-align: left;
  margin-right: 20px;
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
  border: 2px solid #1abc9c;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.detail-btn:hover {
  background-color: #1abc9c;
  color: #ffffff;
}
</style>
