<template>
    <div>
        <h2>정기 예금 상세</h2>
        <p>공시 제출일 : {{ depositdata.dcls_strt_day }}  </p>
        <p>은행 : {{ depositdata.kor_co_nm }}</p>
        <p v-if="depositdata.max_limit >100000000">한도 : {{ depositdata.max_limit/100000000  }}억원</p>
        <p v-else-if="depositdata.max_limit >10000"> 한도 : {{ depositdata.max_limit/10000 }}만원</p>
        <p v-else> 한도 : 없음</p>
        <p>가입 방법 : {{ depositdata.join_way }}</p>
        <div>
            <p>우대 조건 : {{ depositdata.spcl_cnd }}</p>
            <p> {{ depositdata.etc_note }} </p>
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
onMounted(async () => {
    try{
        await counterStore.getDepositDetail(route.params.id);
        depositdata.value = counterStore.DepositDetails
    } catch (e) {
        console.log(e)
    }
})
</script>

<style scoped>

</style>