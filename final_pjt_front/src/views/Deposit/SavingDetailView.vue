<template>
  <div class="container">
    <h2><strong>정기 적금 상세</strong></h2>
    <br>
    <div class="info-header">
      <h4>{{ savingdata.fin_prdt_nm }}</h4>
      <div v-if="check">
        <button class="join-button" @click="join">해지하기</button>
      </div>
      <div v-else>
        <div class="join-section">
          <select class="interest-options" v-model="selectedOption">
            <option v-for="option in savingdata.saving_options" :key="option.id" :value="option">
              {{ option.save_trm }}개월 - {{ option.rsrv_type_nm}}
            </option>
          </select>
          <button class="join-button" @click="join">가입하기</button>
        </div>
      </div>
    </div>
    <div class="info">
      <hr>
      <p>공시 제출일: {{ savingdata.dcls_strt_day }}</p>
      <p>은행: {{ savingdata.kor_co_nm }}</p>
      <p v-if="savingdata.max_limit >= 100000000">한도: {{ savingdata.max_limit / 100000000 }}억원</p>
      <p v-else-if="savingdata.max_limit > 10000">한도: {{ savingdata.max_limit / 10000 }}만원</p>
      <p v-else>한도: 없음</p>
      <p>가입 방법: {{ savingdata.join_way }}</p>
      <p>기본 금리: {{ selectedOption?.intr_rate }}%</p>
      <p>우대 금리: {{ selectedOption?.intr_rate2 }}%</p>
    </div>
    <div class="conditions">
      <h4>우대 조건</h4>
      <p>{{ savingdata.spcl_cnd }}</p>
      <p>{{ savingdata.etc_note }}</p>
    </div>
    <div class="button-group">
      <button class="back-button" @click="goBack">목록</button>
      <button class="product-button" @click="goProducts">가입한 상품</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { useRouter, useRoute } from 'vue-router';

const savingdata = ref([]);
const selectedOption = ref(null);
const counterStore = useCounterStore();
const router = useRouter();
const route = useRoute();
const buyUser = ref([]);
const check = ref(false);

onMounted(async () => {
  try {
    await counterStore.getSavingDetail(route.params.id);
    savingdata.value = counterStore.SavingDetails;
    buyUser.value = savingdata.value.buy_user;
    check.value = buyUser.value.includes(parseInt(sessionStorage.user_id));
    if (savingdata.value.saving_options.length > 0) {
      selectedOption.value = savingdata.value.saving_options[0];
    }
  } catch (e) {
    console.log(e);
  }
});
console.log(route.query.banks, route.query.term);

const goBack = () => {
  // URL 쿼리 파라미터를 사용하여 필터 상태 유지
  router.push({
    name: 'SavingList',
    query: {
      banks: route.query.banks,
      term: route.query.term
    }
  });
};

const join = () => {
  if (selectedOption.value) {
    counterStore.buyProduct('saving', savingdata.value.id, selectedOption.value.id);
    router.go(0);
  } else {
    alert('금리 옵션을 선택해주세요.');
  }
};

const goProducts = () => {
  router.push({ name: 'Products' });
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');

* {
  font-family: 'Noto Sans KR', sans-serif; /* 전역 폰트 적용 */
}

.container {
  max-width: 650px;
  margin: 30px auto;
  padding: 20px;
  background-color: #f7f7f7;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  position: relative;
}

h2 {
  color: #1abc9c;
  text-align: center;
  margin-bottom: 20px; /* Add more space below the heading */
}

.info-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px; /* Add more space below the info header */
}

.info-header h4 {
  margin: 0;
}

.join-section {
  display: flex;
  align-items: center;
}

.interest-options {
  margin-right: 20px; /* Increase margin for more space */
  padding: 8px;
  font-size: 14px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.join-button {
  padding: 8px 16px;
  background-color: #1abc9c;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  font-weight: bold;
}

.join-button:hover {
  background-color: #16a085;
}

.info p {
  margin: 10px 0;
  font-size: 16px;
  color: #333;
}

.conditions {
  background-color: #fff;
  border-left: 4px solid #1abc9c;
  padding: 15px;
  margin-top: 20px;
  border-radius: 8px;
}

.conditions p {
  margin: 5px 0;
  font-size: 14px;
  color: #333;
}

.conditions p:first-child {
  font-size: 16px;
  font-weight: bold;
  color: #1abc9c;
}

.button-group {
  margin-top: 20px;
  display: flex;
  justify-content: center;
}

.back-button, .product-button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  font-weight: bold;
  margin-left: 10px;
}

.back-button {
  background-color: #dfdfdf;
  color: #333;
}

.back-button:hover {
  background-color: #bbb;
}

.product-button {
  background-color: #007bff;
  color: white;
  transition: background-color 0.3s ease;
}

.product-button:hover {
  background-color: #0056b3;
}
</style>
