<template>
  <div class="container">
    <h1 class="text-center">금융 상품 조회</h1>
    <p>예금 상품</p>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">
            공시 제출일
            <button @click="sortByDate">
              <span v-if="!sortDescending.date">▲</span>
              <span v-else>▼</span>
            </button>
          </th>
          <th scope="col">은행 명</th>
          <th scope="col">상품명</th>
          <template v-for="(month, index) in months" :key="`column_${month}`">
            <th scope="col" v-for="(prefer, preferIndex) in preferred" :key="`interest_${month}_${preferIndex}`">
              {{ month }}개월{{ prefer ? ' 우대금리' : '' }}
              <button @click="sortBy(month, prefer)">
                <span v-if="!sortDescending[month][prefer]">▲</span>
                <span v-else>▼</span>
              </button>
            </th>
          </template>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(deposit, depositIndex) in deposits" :key="depositIndex" @click="goDetail(deposit.id)" @mouseover="highlightRow(depositIndex)" @mouseleave="unhighlightRow(depositIndex)">
          <td>{{ deposit.dcls_strt_day }}</td>
          <td>{{ deposit.kor_co_nm }}</td>
          <td>{{ deposit.fin_prdt_nm }}</td>
          <template v-for="(month, monthIndex) in months">
            <template v-for="(prefer, preferIndex) in preferred">
              <td class="rate-cell">
                <template v-if="hasOption(deposit, month)">
                  {{ prefer ? getPreferredRate(deposit, month) : getInterestRate(deposit, month) }}%
                </template>
                <template v-else>
                  {{ sortDescending[month][prefer] ? '999' : '-' }}
                </template>
              </td>
            </template>
          </template>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router';

const deposits = ref([]);
const counterStore = useCounterStore();
const router = useRouter();
const months = [1, 3, 6, 12, 24, 36];
const preferred = [false, true]; // false: 금리, true: 우대금리
const sortDescending = {
  date: false,
  ...Object.fromEntries(months.map(month => [month, Object.fromEntries(preferred.map(p => [p, false]))])),
};

let lastSortMonth = null;
let lastSortPrefer = null;

onMounted(async () => {
  try {
    await counterStore.getDeposit();
    if (counterStore.DepositInfos && counterStore.DepositInfos.length > 0) {
      deposits.value = counterStore.DepositInfos.map(deposit => ({
        ...deposit,
        options: deposit.deposit_options ? Object.fromEntries(deposit.deposit_options.map(option => [option.save_trm, option])) : {}
      }));
    } else {
      deposits.value = [];
    }
  } catch (error) {
    console.log(error);
  }
});

const goDetail = (id) => {
  router.push({ name: 'DepositDetail', params: { id: id } });
};

const hasOption = (deposit, month) => {
  return deposit.options && deposit.options[month];
};

const getInterestRate = (deposit, month) => {
  return hasOption(deposit, month) ? deposit.options[month].intr_rate : null;
};

const getPreferredRate = (deposit, month) => {
  return hasOption(deposit, month) ? deposit.options[month].intr_rate2 : null;
};

const sortBy = (month, prefer) => {
  if (lastSortMonth !== month || lastSortPrefer !== prefer) {
    Object.keys(sortDescending[month]).forEach(p => {
      sortDescending[month][p] = false; // 다른 버튼의 토글 초기화
    });
    sortDescending[month][prefer] = !sortDescending[month][prefer]; // 현재 버튼 토글 변경
  } else {
    sortDescending[month][prefer] = !sortDescending[month][prefer]; // 같은 버튼이 클릭된 경우 토글만 변경
  }
  lastSortMonth = month;
  lastSortPrefer = prefer;
  deposits.value.sort((a, b) => {
    const rateA = prefer ? getPreferredRate(a, month) : getInterestRate(a, month);
    const rateB = prefer ? getPreferredRate(b, month) : getInterestRate(b, month);
    if (rateA === '-' && rateB === '-') return 0;
    if (rateA === '-') return sortDescending[month][prefer] ? 999 : -1;
    if (rateB === '-') return sortDescending[month][prefer] ? -1 : 999;
    return sortDescending[month][prefer] ? rateB - rateA : rateA - rateB;
  });
};

const sortByDate = () => {
  sortDescending.date = !sortDescending.date;
  deposits.value = [...deposits.value].sort((a, b) => {
    if (sortDescending.date) {
      return b.dcls_strt_day.localeCompare(a.dcls_strt_day);
    } else {
      return a.dcls_strt_day.localeCompare(b.dcls_strt_day);
    }
  });
};

const highlightRow = (index) => {
  document.querySelectorAll('.container .table tbody tr')[index].classList.add('highlighted');
};

const unhighlightRow = (index) => {
  document.querySelectorAll('.container .table tbody tr')[index].classList.remove('highlighted');
};
</script>

<style scoped>
.table {
  width: 100%;
  border-collapse: collapse;
}

.table th,
.table td {
  border: 1px solid #dee2e6;
  padding: 8px;
  text-align: center;
}

.table th {
  background-color: #f5f5f5;
}

.rate-cell {
  font-weight: bold;
}

.container {
  margin-top: 20px;
}

.text-center {
  text-align: center;
}

.highlighted {
  background-color: red;
}
</style>
