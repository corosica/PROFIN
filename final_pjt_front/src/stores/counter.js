
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
export const useCounterStore = defineStore('counter', () => {
  const articleList = ref([])
  const title = ref('')
  const content = ref('')
  const username = ref('')
  const updated_time = ref('')

  
  const login = function () {
    axios({
      method : 'POST',
      url : 'http://127.0.0.1:8000/accounts/login/', //주소
      data : {
        username : 'testuser',
        password : 'ssafy11!'
      }
    }).then(function (response) {
      console.log(response.data)
      localStorage.setItem('token','Token '+response.data.key)
    }).catch(function (err) {
      console.log(err)
    })
  }

  const viewArticles = async function () {
    try {
      const response = await axios({
        method: 'GET',
        url: 'http://127.0.0.1:8000/api/v1/articles/',
      });
      articleList.value = response.data;
      console.log(articleList.value);
    } catch (err) {
      console.error('Failed to fetch articles:', err);
    }
  };

  const getArticleById = function (id) {
    axios(
      {
      method : 'GET',
      url : `http://127.0.0.1:8000/api/v1/articles/${id}/`,
    }
    )
    .then(function (response) {
      console.log(response.data)
      title.value = response.data.title
      content.value = response.data.content
      username.value = response.data.user
      updated_time.value = response.data.updated_at.split('T')[0]
    })
    .catch(function (err) {
      console.log(err)
    })
  }
   
    
  const createArticles = function(title,contents) {  
    axios({ 
      method : 'POST',
      url : 'http://127.0.0.1:8000/api/v1/articles/',
      headers : {
        Authorization : localStorage.getItem('token'),
      },
        data : {
        title : title,
        content : contents
      }
    })
  }

  const deleteArticle = function(id) {  
    axios({
      method: 'DELETE',
      url: `http://127.0.0.1:8000/api/v1/articles/${id}/`,
      headers: {
        Authorization: localStorage.getItem('token'),
      },
    })
    .then(function(response) {
      console.log('Article deleted:', response.data)
    })
    .catch(function(error) {
      console.log(error)
    })      
  }

  const updateArticle = function(id, title, content) {
    axios({
      method: 'PUT',
      url: `http://127.0.0.1:8000/api/v1/articles/${id}/`,
      headers: {
        Authorization: localStorage.getItem('token'),
      },
      data: {
        title: title,
        content: content,
      },
    })
   .then(function(response) {
   console.log('Article updated:', response.data)
   })
  .catch(function(error) {
    console.log(error)
    })
  }

  return { 
    login,
    createArticles,
    viewArticles,
    articleList,
    getArticleById,
    title,
    content,
    username,
    updated_time,
    deleteArticle,
    updateArticle,
  }
})
