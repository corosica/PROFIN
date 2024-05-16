<template>
  <div>
    <h1>{{ post.title }}</h1>
    <p>{{ post.content }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useCounterStore } from '@/stores/counter';

const route = useRoute();
const counterStore = useCounterStore();
const post = ref({});

onMounted(() => {
  const postId = route.params.id;
  const article = counterStore.getArticleById(postId);

  if (article) {
    post.value = article;
  } else {
    // 필요한 경우, 게시글이 없는 경우의 처리를 추가합니다.
    console.error('게시글을 찾을 수 없습니다.');
  }
});
</script>

<style scoped>
/* 최소한의 스타일링만 추가 */
</style>
