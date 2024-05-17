<template>
  <div>
      <h3>{{ counterStore.title }} </h3>
      <p>글 번호 : {{ route.params.id  }}</p>
      <p>유저 : {{ counterStore.username}}   업데이트 : {{ counterStore.updated_time }}  </p>
      <p>내용</p>
      <p>{{counterStore.content}}</p>
      <button @click="deletePost">삭제하기</button> |
      <button @click="goCommunity">뒤로가기</button> |
      <button @click="updatePost">수정하기</button>
      
    <div class="comments">

    </div>

  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted,computed  } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useCounterStore } from '@/stores/counter';

const router = useRouter();
const route = useRoute();
const counterStore = useCounterStore();


const goCommunity = function () {
  router.push({ name: 'Community'})
}

const deletePost = async () => {
  try {
    await counterStore.deleteArticle(route.params.id)
    alert('게시글이 삭제되었습니다.')
    router.push({ name: 'Community'})
  } catch (error) {
    console.error('Failed to delete post:', error)
    alert('게시글 삭제에 실패했습니다.')
  }
}

const updatePost = function () {
  router.push({ name: 'PostUpdate', params: { id: route.params.id } })
}

onMounted(() => {
  counterStore.getArticleById(route.params.id)
  console.log(route.params.id)
// Community에 설정한 params:{id:post.id}}
})
</script>

<style scoped>
/* 최소한의 스타일링만 추가 */
</style>
