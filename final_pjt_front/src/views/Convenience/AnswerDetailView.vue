<template>
    <div class='articles'>
      <div>
        <h3>{{ counterStore.title }}</h3>
        <div class="user-time-container">
          <p class="user">유저 : {{ counterStore.username.nickname }}</p>
          <p class="time">작성시간 : {{ counterStore.updated_time }}</p>
        </div>
        <br>
        <!-- 줄바꿈 처리된 콘텐츠를 v-html로 렌더링 -->
        <div v-html="formattedContent"></div>
        <br>
        <div class="buttons">
          <div class="back-button">
            <button @click="goCommunity">뒤로가기</button> 
          </div>
          <div class="update-button" v-if=" counterStore.username.username === crt_user">
            <button @click="updatePost">수정하기</button>
          </div>
          <div class="delete-button" v-if=" counterStore.username.username === crt_user">
            <button @click="deletePost">삭제하기</button> 
          </div>
        </div>
        <div class="comments">
          <h3>답변</h3>
          <form @submit.prevent="addComment" v-if="crt_user">
            <input type="text" v-model="newComment" placeholder="답변을 작성해주세요" />
            <div class="click-button">
              <button type="submit">등록</button>
            </div>
          </form>
          <div @click.prevent="router.push({name:'Login'})" v-else>
            <input type="text" placeholder="로그인 후 작성하실 수 있습니다." style="width: 100%;"/>
          </div>
          <ul>
            <li v-for="comment in comments" :key="comment.id">
              <p>{{ comment.user.nickname }} : {{ comment.content }}</p>
              <button @click="deleteComments(comment.id)" v-if="comment.user.username === crt_user">삭제</button>
            </li>
          </ul>
        </div>
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
  const crt_user = ref('')
  const goCommunity = function () {
    router.push({ name: 'Answer'})
  }
  
  const deletePost = async () => {
    try {
      await counterStore.deleteArticle('qna',route.params.id)
      alert('게시글이 삭제되었습니다.')
      router.push({ name: 'Answer'})
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
      counterStore.newComment('qna',route.params.id, newComment.value)
      await counterStore.viewComment('qna',route.params.id)
      router.go(0)
    } catch (error) {
      console.error('Failed to add comment:', error)
      alert('댓글 등록에 실패했습니다.')
    }
  }
  
  const deleteComments = async (parameter) => {
    try {
      await counterStore.deleteComment('qna',route.params.id, parameter)
      alert('댓글이 삭제되었습니다.')
      router.go(0)
    } catch (error) {
      console.error('Failed to delete post:', error)
      alert('댓글 삭제에 실패했습니다.')
    }
  }
  
  const formattedContent = computed(() => {
  return counterStore.content.replace(/\n/g, '<br>');
});


  onMounted(async () => {
      try {
        await counterStore.getArticleById('qna',route.params.id)  
        await counterStore.viewComment('qna',route.params.id)
        comments.value = counterStore.commentList
        crt_user.value =   sessionStorage.getItem('username')
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
  .articles {
    font-family: 'Arial', sans-serif;
    max-width: 800px; /* 전체 게시판 너비 조정 */
    margin: 0 auto; /* 가운데 정렬 */
    background: #fff; /* 배경색 추가 */
    padding: 20px; /* 패딩 추가 */
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* 그림자 효과 추가 */
    border-radius: 10px; /* 모서리 둥글게 */
  }
  
  h3 {
    color: #333;
    font-size: 20px;
    margin-top: 0;
    padding-bottom: 10px;
    border-bottom: 1px solid #eee;
  }
  
  p {
    color: #666;
    font-size: 16px;
    margin: 10px 0;
  }
  
  .buttons {
    margin-top: 20px;
    display: flex;
    justify-content: right;
  }
  
  .buttons button {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 3px 6px;
    cursor: pointer;
    border-radius: 5px;
    transition: background-color 0.3s ease;
    display: flex;
    margin-left: 10px;
  }
  
  .buttons button:hover {
    background-color: #0056b3;
  }
  
  .comments .click-button button {
    padding: 5px 10px;
    background-color: #ffffff; /* 버튼 배경색을 하얀색으로 설정 */
    color: #007bff; /* 버튼 텍스트 색상을 블루로 설정 */
    border: 1px solid #ccc; /* 경계선 추가 */
    cursor: pointer;
    border-radius: 5px;
    transition: all 0.3s ease; /* 부드러운 전환 효과 */
  }
  
  .comments .click-button button:hover {
    background-color: #007bff; /* 호버 상태에서의 배경색 변경 */
    color: white; 
    border-color: #007bff; /* 호버 상태에서의 경계선 색 변경 */
  }
  
  .buttons .delete-button button {
    background-color: #dc3545; /* 빨간색 */
  }
  
  .buttons .delete-button button:hover {
    background-color: #bd2f3d; /* 빨간색 */
  }
  
  
  .buttons .back-button button {
    background-color: #999999; 
  }
  
  .buttons .back-button button:hover {
    background-color: #6d6d6d; 
  }
  
  .user-time-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 10px 0;
  }
  
  .time, .user {
    flex: 1; /* 유저 이름과 작성시간을 같은 너비로 설정 */
    text-align: right; /* 작성시간을 오른쪽 정렬 */
  }
  
  .user {
    text-align: left; /* 유저 이름을 왼쪽 정렬 */
  }
  
  .comments {
    margin-top: 30px;
  }
  
  .comments h3 {
    margin-bottom: 10px;
  }
  
  .comments form {
    display: flex;
    align-items: center;
  }
  
  .comments input[type="text"] {
    flex: 1;
    padding: 8px;
    margin-right: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .comments button {
    padding: 8px 12px;
    background-color: #28a745;
    color: white;
    border: none;
    cursor: pointer;
    border-radius: 5px;
  }
  
  .comments ul {
    list-style: none;
    padding: 0;
  }
  
  .comments li {
    padding: 10px;
    background-color: #f8f9fa;
    border: 1px solid #ccc;
    margin-top: 8px;
    margin-bottom: 8px;
    border-radius: 5px;
    position: relative;
  }
  
  .comments li p {
    margin: 0;
    color: #333;
  }
  
  .comments li button {
    background-color: #b6b6b6;
    color: #fff;
    border: none;
    cursor: pointer;
    border-radius: 5px;
    padding: 4px 8px;
    position: absolute;
    right: 10px;
    top: 5px;
  }
  
  .comments li button:hover {
    background-color: #9b9b9b;
  }
  </style>
  
  