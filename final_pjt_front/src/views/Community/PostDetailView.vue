<template>
  <div>
      <h3>{{ counterStore.title }} </h3>
      <p>글 번호 : {{ route.params.id  }}</p>
      <p>유저 : {{ counterStore.username.nickname }}   업데이트 : {{ counterStore.updated_time }}  </p>
      <p>내용</p>
      <p>{{counterStore.content}}</p>
    <div class="buttons">
      <button @click="deletePost">삭제하기</button> |
      <button @click="goCommunity">뒤로가기</button> |
      <button @click="updatePost">수정하기</button>
    </div>
    <div class="comments">
      <h3>댓글</h3>
      <form @submit.prevent="addComment">
        <input type="text" v-model="newComment" placeholder="댓글을 입력하세요" />
        <button type="submit">등록</button>
      </form>
      <ul>
        <li v-for="comment in comments" :key="comment.id">
          <p> {{ comment.user.nickname }} : {{ comment.content }}</p> 
          <button @click="deleteComments(comment.id)">삭제</button>
        </li>
      </ul>
      
    </div>

  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted, computed  } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useCounterStore } from '@/stores/counter';

const router = useRouter();
const route = useRoute();
const counterStore = useCounterStore();

const comments = ref([])
const newComment = ref('')
const commentId = ref('')

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

const addComment = async () => {
  try {
    counterStore.newComment(route.params.id, newComment.value)
    await counterStore.viewComment(route.params.id)
    router.go(0)
  } catch (error) {
    console.error('Failed to add comment:', error)
    alert('댓글 등록에 실패했습니다.')
  }
}

const deleteComments = async (parameter) => {
  try {
    await counterStore.deleteComment(route.params.id, parameter)
    alert('댓글이 삭제되었습니다.')
    router.go(0)
  } catch (error) {
    console.error('Failed to delete post:', error)
    alert('댓글 삭제에 실패했습니다.')
  }
}



onMounted(async () => {
    try {
      await counterStore.getArticleById(route.params.id)  
      await counterStore.viewComment(route.params.id)
      comments.value = counterStore.commentList
    } catch (e) {
      console.error('failed to view articles',e)
    }
    finally {
      // loading.value = false;
      // console.log(counterStore.articleList)
    }
  })  

</script>

<style scoped>
/* 최소한의 스타일링만 추가 */
</style>