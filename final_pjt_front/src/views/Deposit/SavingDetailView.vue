<template>
    <div class="container">
        <div class="header">
            <h2><strong>정기 예금 상세</strong></h2>
            <button class="join-button">가입하기</button>
        </div>
        <div class="info">
            <p>공시 제출일: {{ depositdata.dcls_strt_day }}</p>
            <p>은행: {{ depositdata.kor_co_nm }}</p>
            <p v-if="depositdata.max_limit >= 100000000">한도: {{ depositdata.max_limit / 100000000 }}억원</p>
            <p v-else-if="depositdata.max_limit > 10000">한도: {{ depositdata.max_limit / 10000 }}만원</p>
            <p v-else>한도: 없음</p>
            <p>가입 방법: {{ depositdata.join_way }}</p>
        </div>
        <div class="conditions">
            <p>우대 조건</p>
            <p>{{ depositdata.spcl_cnd }}</p>
            <p>{{ depositdata.etc_note }}</p>
        </div>
    </div>
</template>





<script setup>
import { ref, onMounted } from 'vue';
import {useCounterStore} from '@/stores/counter';
import { useRouter,useRoute } from 'vue-router';
const depositdata = ref([]);
const counterStore = useCounterStore();
const router = useRouter();
const route  = useRoute();
const how = ref('')
onMounted(async () => {
    try{
        await counterStore.getSavingDetail(route.params.id);
        depositdata.value = counterStore.SavingDetails
        how.value = depositdata.value.saving_options[0].rsrv_type_nm
    } catch (e) {
        console.log(e)
    }
})
</script>

<style scoped>
.container {
    max-width: 600px;
    margin: 30px auto;
    padding: 20px;
    background-color: #f7f7f7;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}

h2 {
    color: #1abc9c;
    text-align: center;
    margin: 0;
    flex-grow: 1; /* To make the title centered */
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
    margin-left: 20px;
}

.join-button:hover {
    background-color: #16a085;
}

.info p {
    margin: 10px 0;
    font-size: 16px;
    color: #333;
}

.info p strong {
    color: #000;
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
</style>
