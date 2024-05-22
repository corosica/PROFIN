<template>
    <div>
        <p>담은상품</p>
        <p>가입한 순서대로 정렬됩니다.(최초가입 최상단)</p>
        <h3>예금</h3>
        <div v-for="deposit_item in deposit_buy_data" :key="deposit_item.id">
            <template v-for="item in deposit_data">
                <div v-if="item.id === deposit_item.product" :key="item.id">
                    <!-- CSS수정 하단부 -->
                    <span>
                        {{ item.kor_co_nm }} - 
                        <a @click.prevent="router.push({name:'DepositDetail',params:{id:item.id}})" href="">
                            {{ item.fin_prdt_nm }}
                        </a>
                    </span>
                    <hr>
                </div>
            </template>
        </div>
        <h3>적금</h3>
        <div v-for="saving_item in saving_buy_data" :key="saving_item.id">
            <template v-for="item in saving_data">
                <div v-if="item.id === saving_item.product" :key="item.id">
                    <span>
                        {{ item.kor_co_nm }} - 
                        <a @click.prevent="router.push({name:'SavingDetail',params:{id:item.id}})" href="">
                        {{ item.fin_prdt_nm }}
                        </a>
                    </span>
                    <hr>
                </div>
            </template>
        </div>

        <h3>이밑은 그래프자리</h3>
    </div>
</template>

<script setup>
    import { ref, onMounted } from 'vue';
    import { useRouter } from 'vue-router';
    import { useCounterStore } from '@/stores/counter';
    const deposit_buy_data = ref([]);
    const saving_buy_data = ref([]);
    const deposit_data = ref([]);
    const saving_data = ref([]);
    const router = useRouter();
    const counterStore = useCounterStore();
    
    onMounted(async () => {
      try {
        await counterStore.getProductsList();
        await counterStore.getSaving()
        await counterStore.getDeposit()
        deposit_data.value = counterStore.DepositInfos
        saving_data.value = counterStore.SavingInfos
        deposit_buy_data.value = counterStore.buyProductList['예금'];
        saving_buy_data.value = counterStore.buyProductList['적금'];
      } catch (error) {
        console.error('Failed to load user data:', error);
      }
    });
</script>

<style scoped>

</style>