<template>
    <div>
      <h3>게시글 수정</h3>
      <form @submit.prevent="updatePost">
        <label for="title">제목: </label>
        <input id="title" v-model="title" type="text" />
        <br>
        <label for="content">내용:</label>
        <textarea id="content" v-model="content"></textarea>
        <br>
        <input name="file" type="file">
        <br>
        <button type="submit">수정하기</button>
        I
        <button type="button" @click="cancel">취소</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { onMounted, ref } from 'vue'
  import { useRouter, useRoute } from 'vue-router'
  import { useCounterStore } from '@/stores/counter'
  
  const router = useRouter()
  const route = useRoute()
  const counterStore = useCounterStore()
  const title = ref('')
  const content = ref('')
  title.value = counterStore.title 
  content.value = counterStore.content

  
  const updatePost = async () => {
    try {
      await counterStore.updateArticle(route.params.id,title.value,content.value)
      alert('게시글이 수정되었습니다.')
      router.push({ name:'PostDetail', params: { id: route.params.id }})
    }  catch (error) {
      console.error('Failed to update post:', error)
      alert('게시글 수정에 실패했습니다.')
    }
  }
  const cancel = () => {
    router.push({ name:'PostDetail', params: { id: route.params.id }});
  };
  </script>
  