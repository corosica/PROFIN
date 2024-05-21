<template>
  <div>
    <h1 class="text-center">적금 상품 조회</h1>
    <!-- 필터링 섹션 시작 -->
    <div class="filter-container">
      <div class="filter-section">
        <div class="dropdown">
          <label for="banks">은행:</label>
          <button class="dropdown-toggle" type="button" id="selectedBanks" data-bs-toggle="dropdown" aria-expanded="false">
            선택
          </button>
          <ul class="dropdown-menu" aria-labelledby="selectedBanks">
            <li>
              <input type="checkbox" id="selectAllBanks" v-model="selectAllBanks" @change="selectAllBanksChanged">
              <label for="selectAllBanks">전체 선택</label>
            </li>
            <li v-for="(bank, index) in banks" :key="index">
              <input type="checkbox" :id="bank" :value="bank" v-model="selectedBanks">
              <label :for="bank">{{ bank }}</label>
            </li>
          </ul>
        </div>
      </div>
      <div class="filter-section">
        <div>
        <label for="term">예치 기간:</label>
        <select id="term" v-model="selectedTerm" @change="applyFilters">
          <option value="">전체</option>
          <option v-for="(term, index) in terms" :key="index" :value="term">{{ term }}개월</option>
        </select>
      </div>
    </div>
  </div>
    <!-- 필터링 섹션 끝 -->
    <p>적금 상품</p>
    <table class="table">
      <thead>
        <tr>
          <th scope="col" @click="sortByDate">
            공시 제출일
            <span v-if="!sortDescending.date">▲</span>
            <span v-else>▼</span>
          </th>
          <th scope="col">은행</th>
          <th scope="col">상품명</th>
          <template v-for="(month, index) in months" :key="`column_${month}`">
            <template v-if="shouldShowColumn(month)">
              <th scope="col" v-for="(prefer, preferIndex) in preferred" :key="`interest_${month}_${preferIndex}`" @click="sortBy(month, prefer)">
                {{ month }}개월{{ prefer ? ' 우대금리' : '' }}
                <span v-if="!sortDescending[month][prefer]">▲</span>
                <span v-else>▼</span>
              </th>
            </template>
          </template>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(deposit, depositIndex) in filteredDeposits" :key="depositIndex" @click="goDetail(deposit.id)" @mouseover="highlightRow(depositIndex)" @mouseleave="unhighlightRow(depositIndex)">
          <td>{{ deposit.dcls_strt_day }}</td>
          <td>{{ deposit.kor_co_nm }}</td>
          <td>{{ deposit.fin_prdt_nm }}</td>
          <template v-for="(month, monthIndex) in months">
            <template v-if="shouldShowColumn(month)">
              <template v-for="(prefer, preferIndex) in preferred">
                <td class="rate-cell">
                  <template v-if="hasOption(deposit, month)">
                    {{ prefer ? getPreferredRate(deposit, month) : getInterestRate(deposit, month) }}%
                  </template>
                  <template v-else>
                    {{ sortDescending[month][prefer] ? '-' : '-' }}
                  </template>
                </td>
              </template>
            </template>
          </template>
        </tr>
      </tbody>
    </table>
  </div>
</template>


<script setup>
import { ref, onMounted, computed,watch } from 'vue';
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

// 필터링을 위한 상태
const selectedBanks = ref([]);
const selectedTerm = ref('');
const banks = ref([]);
const terms = months; // 예치 기간 필터링을 위한 데이터

// 필터링 적용
const filteredDeposits = computed(() => {
  return deposits.value.filter(deposit => {
    const bankMatch = selectedBanks.value.length === 0 || selectedBanks.value.includes(deposit.kor_co_nm);
    const termMatch = selectedTerm.value === '' || hasOption(deposit, selectedTerm.value);
    return bankMatch && termMatch;
  });
});

// 열 표시 조건
const shouldShowColumn = (month) => {
  return selectedTerm.value === '' || selectedTerm.value == month;
};

let lastSortMonth = null;
let lastSortPrefer = null;

onMounted(async () => {
  try {
    await counterStore.getSaving();
    if (counterStore.SavingInfos && counterStore.SavingInfos.length > 0) {
      deposits.value = counterStore.SavingInfos.map(deposit => ({
        ...deposit,
        options: deposit.saving_options ? Object.fromEntries(deposit.saving_options.map(option => [option.save_trm, option])) : {}
      }));
      banks.value = [...new Set(deposits.value.map(deposit => deposit.kor_co_nm))];
    } else {
      deposits.value = [];
    }
  } catch (error) {
    console.log(error);
  }
});

const goDetail = (id) => {
  router.push({ name: 'SavingDetail', params: { id: id } });
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

const applyFilters = () => {
  // 필터 적용 함수
  filteredDeposits.value = deposits.value.filter(deposit => {
    const bankMatch = selectedBanks.value.length === 0 || selectedBanks.value.includes(deposit.kor_co_nm);
    const termMatch = selectedTerm.value === '' || hasOption(deposit, selectedTerm.value);
    return bankMatch && termMatch;
  });
};

const highlightRow = (index) => {
  document.querySelectorAll('.container .table tbody tr')[index].classList.add('highlighted');
};

const unhighlightRow = (index) => {
  document.querySelectorAll('.container .table tbody tr')[index].classList.remove('highlighted');
};

const selectAllBanks = ref(false);
const selectAllBanksChanged = () => {
  if (selectAllBanks.value) {
    selectedBanks.value = banks.value.slice();
  } else {
    selectedBanks.value = [];
  }
};
watch([selectedBanks, selectedTerm], () => {
  applyFilters();
});


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

/* 필터 섹션 스타일 */
.filter-container {
  display: flex;
  justify-content: space-around;
  margin-bottom: 20px;
}

.filter-section {
  display: flex;
  flex-direction: column;
}

.filter-section label {
  margin-bottom: 5px;
}

.filter-section select {
  padding: 5px;
  border-radius: 4px;
  border: 1px solid #dee2e6;
}
.filter-container {
  display: flex;
  justify-content: space-around;
  margin-bottom: 20px;
}

.filter-section {
  position: relative;
}

.filter-section label {
  margin-bottom: 5px;
}

.dropdown-toggle {
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 5px 10px;
  cursor: pointer;
}

.dropdown-toggle:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(50, 115, 220, 0.25);
}

.dropdown-menu {
  display: none;
  position: absolute;
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  z-index: 1000;
}

.dropdown-menu.show {
  display: block;
}

.dropdown-menu li {
  list-style: none;
  margin-bottom: 5px;
}

.dropdown-menu label {
  margin-left: 5px;
}

.dropdown-menu input[type="checkbox"] {
  margin-right: 5px;
}
</style>
