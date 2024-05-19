<template>
    <div>
    <div>
      <label for="currency1">Currency 1:</label>
      <select id="currency1" v-model="selectedCurrency1" @change="calculateExchangeRate('input1')">
        <option v-for="currency in exchanges" :key="currency.cur_unit" :value="currency.cur_unit">
          {{ currency.cur_nm }}
        </option>
      </select>
      <input type="number" v-model.number="input1" @input="calculateExchangeRate('input1')" />
    </div>

    <div>
      <label for="currency2">Currency 2:</label>
      <select id="currency2" v-model="selectedCurrency2" @change="calculateExchangeRate('input2')">
        <option v-for="currency in exchanges" :key="currency.cur_unit" :value="currency.cur_unit">
          {{ currency.cur_nm }}
        </option>
      </select>
      <input type="number" v-model.number="input2" @input="calculateExchangeRate('input2')" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted,reactive, toRefs } from 'vue';
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
  } finally {
    console.log(counterStore.ExchangeInfos);
    console.log('hi');
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

</style>