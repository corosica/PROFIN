<template>
    <div class="container">
      <p class="title">담은 상품</p>
      <p class="subtitle">가입한 순서대로 정렬됩니다.(최초가입 최상단)</p>
  
      <div class="content">
        <div class="column card-wrapper">
          <h3 class="section-title">예금</h3>
          <div class="card-container" v-for="deposit_item in deposit_buy_data" :key="deposit_item.id">
            <template v-for="item in deposit_data">
              <div v-if="item.id === deposit_item.product" :key="item.id" class="card">
                <span class="product-title">
                  {{ item.kor_co_nm }} -
                  <a @click.prevent="router.push({ name: 'DepositDetail', params: { id: item.id } })" href="" class="product-link">
                    {{ item.fin_prdt_nm }}
                  </a>
                </span>
                <p class="rate">
                  기본금리: <span class="rate-value">{{ deposit_item.intr_rate }}%</span>
                </p>
                <p class="rate">
                  우대금리: <span class="rate-value">{{ deposit_item.intr_rate2 }}%</span>
                </p>
              </div>
            </template>
          </div>
        </div>
  
        <div class="separator"></div>
  
        <div class="column card-wrapper">
          <h3 class="section-title">적금</h3>
          <div class="card-container" v-for="saving_item in saving_buy_data" :key="saving_item.id">
            <template v-for="item in saving_data">
              <div v-if="item.id === saving_item.product" :key="item.id" class="card">
                <span class="product-title">
                  {{ item.kor_co_nm }} -
                  <a @click.prevent="router.push({ name: 'SavingDetail', params: { id: item.id } })" href="" class="product-link">
                    {{ item.fin_prdt_nm }}
                  </a>
                </span>
                <p class="rate">
                  기본금리: <span class="rate-value">{{ saving_item.intr_rate }}%</span>
                </p>
                <p class="rate">
                  우대금리: <span class="rate-value">{{ saving_item.intr_rate2 }}%</span>
                </p>
              </div>
            </template>
          </div>
        </div>
      </div>
  
      <h3 class="section-title chart-title">가입한 상품 금리</h3>
      <div class="chart-container">
        <canvas id="interestRateChart"></canvas>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import { useCounterStore } from '@/stores/counter';
  import { Chart, registerables } from 'chart.js';
  
  Chart.register(...registerables);
  
  const deposit_buy_data = ref([]);
  const saving_buy_data = ref([]);
  const deposit_data = ref([]);
  const saving_data = ref([]);
  const router = useRouter();
  const counterStore = useCounterStore();
  
  onMounted(async () => {
    try {
      await counterStore.getProductsList();
      await counterStore.getSaving();
      await counterStore.getDeposit();
      deposit_data.value = counterStore.DepositInfos;
      saving_data.value = counterStore.SavingInfos;
      deposit_buy_data.value = counterStore.buyProductList['예금'];
      saving_buy_data.value = counterStore.buyProductList['적금'];
  
      // 차트 데이터 준비
      const labels = [...deposit_buy_data.value, ...saving_buy_data.value].map(item => {
        const product = [...deposit_data.value, ...saving_data.value].find(p => p.id === item.product);
        return product ? product.fin_prdt_nm : 'Unknown';
      });
  
      const basicRates = [...deposit_buy_data.value, ...saving_buy_data.value].map(item => item.intr_rate);
      const preferentialRates = [...deposit_buy_data.value, ...saving_buy_data.value].map(item => item.intr_rate2);
  
      // 차트 그리기
      const ctx = document.getElementById('interestRateChart').getContext('2d');
      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: labels,
          datasets: [
            {
              label: '기본 금리',
              data: basicRates,
              backgroundColor: 'rgba(54, 162, 235, 0.6)',
              borderColor: 'rgba(54, 162, 235, 1)',
              borderWidth: 1
            },
            {
              label: '우대 금리',
              data: preferentialRates,
              backgroundColor: 'rgba(75, 192, 192, 0.6)',
              borderColor: 'rgba(75, 192, 192, 1)',
              borderWidth: 1
            }
          ]
        },
        options: {
          responsive: true,
          scales: {
            x: {
              beginAtZero: true,
              title: {
                display: true,
                text: '가입한 상품'
              }
            },
            y: {
              beginAtZero: true,
              title: {
                display: true,
                text: '금리 (%)'
              }
            }
          }
        }
      });
    } catch (error) {
      console.error('Failed to load user data:', error);
    }
  });
  </script>
  
  <style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');
  
  * {
    font-family: 'Noto Sans KR', sans-serif; /* 전역 폰트 적용 */
  }
  
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .title {
    font-size: 24px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 10px;
  }
  
  .subtitle {
    font-size: 14px;
    text-align: center;
    color: #666;
    margin-bottom: 20px;
  }
  
  .content {
    display: flex;
    justify-content: space-between;
    gap: 20px;
  }
  
  .card-wrapper {
    flex: 1;
    background: #f8f9fa;
    border-radius: 8px;
    padding: 20px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  }
  
  .separator {
    width: 2px;
    background: #ffffff;
    margin: 0 10px;
  }
  
  .section-title {
    font-size: 20px;
    font-weight: bold;
    margin-top: 0;
    margin-bottom: 20px;
    text-align: center;
  }
  
  .chart-title {
    margin-top: 50px;
    margin-bottom: 20px;
  }
  
  .card-container {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  
  .card {
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    padding: 15px;
    transition: transform 0.3s;
  }
  
  .card:hover {
    transform: translateY(-5px);
  }
  
  .product-title {
    font-size: 16px;
    font-weight: bold;
    margin-bottom: 5px;
  }
  
  .product-link {
    color: #007bff;
    text-decoration: none;
  }
  
  .product-link:hover {
    text-decoration: underline;
  }
  
  .rate {
    font-size: 14px;
    color: #333;
  }
  
  .rate-value {
    font-weight: bold;
    color: #007bff;
  }
  
  .chart-container {
    max-width: 800px;
    margin: 40px auto;
  }
  </style>
  