<template>
    <div>
        <h1>기본 추천</h1>
        <button @click.prevent="recommend">추천 받기</button>
        <ul>
            <li v-for="recommend in recommendedList" :key="recommend.id">
                <p>
                    이름 : {{ recommend.name }}
                    
                    종류 : {{ recommend.type }}
                    <button @click.prevent="router.push({name:'DepositDetail',params:{id:recommend.id}})" v-if="(recommend.type=='예금')">
                        상품 보러가기
                    </button>
                    <button @click.prevent="router.push({name:'SavingDetail',params:{id:recommend.id}})" v-else>
                        상품 보러가기
                    </button>

                </p>

            </li>
        </ul>
    </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter()
const counterStore = useCounterStore()
const recommendedList = ref([])
const recommend = async function () {
    await counterStore.normalRecommend()
    recommendedList.value= counterStore.normalRecommendList
    console.log(recommendedList.value)
}
</script>

<style scoped>
    
</style>