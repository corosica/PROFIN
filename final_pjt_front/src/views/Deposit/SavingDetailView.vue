<template>
    <div class="container">
        <h2><strong>정기 적금 상세</strong></h2>
        <div class="info-header">
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
    <button class="back-button" @click="goBack">목록</button>
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

const goBack = () => {
    router.go(-1);
};
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
    position: relative;
}

h2 {
    color: #1abc9c;
    text-align: center;
    margin-bottom: 10px;
}

.info-header {
    position: relative;
    height: 40px; /* Adjust the height as needed */
}

.join-button {
    position: absolute;
    right: 0;
    top: 0;
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

.back-button {
    margin-top: 20px;
    padding: 10px 20px;
    background-color: #dfdfdf;
    color: #333;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    font-weight: bold;
    display: block;
    width: 100px;
    margin-left: auto;
    margin-right: auto;
}

.back-button:hover {
    background-color: #bbb;
}
</style>
