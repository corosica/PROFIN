<template>

    <div>
			<h1>게시글 목록</h1>
		</div>
		<ul>
			<li v-for="post in posts" :key="post.id" >
				<p>글 번호 : {{ post.id }}</p>
				<RouterLink :to="{name :'PostDetail', params:{id:post.id}}">
					<p>제목 : {{ post.title }} </p>
				</RouterLink>
			</li>
		</ul>
    <div>
        <RouterLink :to="{name : 'PostCreate'}">게시글 작성</RouterLink>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { onMounted } from 'vue';
  import { useCounterStore } from '@/stores/counter';
  const counterStore = useCounterStore()
  const posts = ref([]);
  onMounted(() => {
    counterStore.viewArticles()
    posts.value = counterStore.articleList
  })  
  // 게시물이 없는 경우를 테스트하려면 위의 배열을 빈 배열로 설정해보세요.
  // const posts = ref([]);
  </script>
  
  <style scoped>
  </style>
  