<template>
    <div class="container text-center">
        <h1>금융 상품 조회</h1>
        <p>예적금 상품</p>
        <div class="d-flex row g-4">
            <div @click.prevent="goDetail(deposit.id)" v-for="deposit in deposits" :key="deposit.id" class="border col-3 p-3">
                <img :src="`/${deposit.kor_co_nm}.png`" alt="테스트" width="200px" height="150px">
                <p>
                    {{ deposit.fin_prdt_nm }}
                </p>
                <p>
                    {{ deposit.kor_co_nm }}
                </p>
                
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import {useCounterStore} from '@/stores/counter';
import { useRouter } from 'vue-router';
const deposits = ref([]);
const counterStore = useCounterStore();
const router = useRouter();
onMounted(async () => {
    try{
        await counterStore.getDeposit()
        deposits.value = counterStore.DepositInfos
    } catch (e) {
        console.log(e)
    }
})

const goDetail = (id) => {
    router.push({name: 'DepositDetail', params: {id: id}})
}
</script>

<style scoped>

</style>