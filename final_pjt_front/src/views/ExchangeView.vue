<template>
  <div class="exchange-wrapper">
    <div class="exchange-container">
      <h1 class="title">환율 계산기</h1>
      <div class="currency-selector">
        <div class="currency-block">
          <label for="currency1">나라1: </label>
          <select id="currency1" v-model="selectedCurrency1" @change="calculateExchangeRate('input1')">
            <option v-for="currency in exchanges" :key="currency.cur_unit" :value="currency.cur_unit">
              {{ currency.cur_nm }}
            </option>
          </select>
          <input type="number" v-model.number="input1" @input="calculateExchangeRate('input1')" />
        </div>
        <div class="currency-block">
          <label for="currency2">나라2:</label>
          <select id="currency2" v-model="selectedCurrency2" @change="calculateExchangeRate('input2')">
            <option v-for="currency in exchanges" :key="currency.cur_unit" :value="currency.cur_unit">
              {{ currency.cur_nm }}
            </option>
          </select>
          <input type="number" v-model.number="input2" @input="calculateExchangeRate('input2')" />
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
const exchanges = ref([]);

const router = useRouter();
const selectedCurrency1 = ref('');
const input1 = ref(0);
const selectedCurrency2 = ref('');
const input2 = ref(0);

onMounted(async () => {
  try {
    await counterStore.getExchange();
    exchanges.value = counterStore.ExchangeInfos;
  } catch (error) {
    console.error('failed to view articles', error);
  }
});

const getExchangeRate = (currency) => {
  const foundCurrency = exchanges.value.find(c => c.cur_unit === currency);
  return foundCurrency ? parseFloat(foundCurrency.deal_bas_r) : 1;
};

const calculateExchangeRate = (source) => {
  if (source === "input1") {
    const rate1 = getExchangeRate(selectedCurrency1.value);
    const rate2 = getExchangeRate(selectedCurrency2.value);
    input2.value = (input1.value * rate2) / rate1;
  } else if (source === "input2") {
    const rate1 = getExchangeRate(selectedCurrency1.value);
    const rate2 = getExchangeRate(selectedCurrency2.value);
    input1.value = (input2.value * rate1) / rate2;
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

.exchange-wrapper {
  display: flex;
  justify-content: center;
  padding-top: 50px; /* 세로 위치 조정을 위한 패딩 추가 */
  background-color: #ffffff;
}

.exchange-container {
  display: flex;
  max-width: 1000px;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  font-family: 'Roboto', sans-serif;
}

.title {
  font-size: 2rem;
  font-weight: 700;
  color: #333;
  margin-bottom: 20px;
}

.currency-selector {
  display: flex;
  justify-content: space-between;
  gap: 20px;
}

.currency-block {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  background-color: #ffffff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.currency-block label {
  font-weight: 500;
  color: #555;
  margin-bottom: 10px;
}

.currency-block select,
.currency-block input {
  width: 200px;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 1rem;
}

.currency-block select:focus,
.currency-block input:focus {
  border-color: #1abc9c;
  outline: none;
  box-shadow: 0 0 4px rgba(26, 188, 156, 0.3);
}

.currency-block input[type="number"] {
  appearance: textfield;
}

.currency-block input[type="number"]::-webkit-outer-spin-button,
.currency-block input[type="number"]::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
</style>
