
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import axios from 'axios'
export const useCounterStore = defineStore('counter', () => {
  const articleList = ref([])
  const title = ref('')
  const content = ref('')
  const username = ref('')
  const updated_time = ref('')
  const commentList = ref([])
  const map_data = ref({})
  const router = useRouter()
  const login = function (username,password) {
    axios({
      method : 'POST',
      url : 'http://127.0.0.1:8000/accounts/login/', //주소
      data : {
        username : username,
        password : password
      }
    }).then(function (response) {
      console.log(response.data)
      localStorage.setItem('token','Token '+response.data.key)
      router.push({name:'Home'}).then(() => {
        // router.push가 완료된 후 새로고침을 수행
          router.go(0);
        });
    }).catch(function (err) {
      alert('아이디 비밀번호를 다시 확인해보세요')
      console.log(err)
    })
  }


  const signup = function (username,password1,password2,email) {
    axios({
      method:'POST',
      url : 'http://127.0.0.1:8000/accounts/signup/',
      data : {
        username : username,
        password1 : password1,
        password2 : password2,
        email : email
      }
    }).then(function (response) {
      login(username,password1)
      console.log(response.data)
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

  const newComment = function (id, comment) {
    axios({
      method: 'POST',
      url: `http://127.0.0.1:8000/api/v1/articles/${id}/comments/`, // URL 형식 확인
      headers: {
        Authorization: localStorage.getItem('token'),
      },
      data: {
        "content": comment
      },
    })
    .then(function (response) {
      console.log('Comment created:', response.data)
    })
    .catch(function (error) {
      console.log(error)
    })
  }

  const viewComment = async function (id) {
    try {
      const response = await axios({
        method: 'GET',
        url: `http://127.0.0.1:8000/api/v1/articles/${id}/comments/`,
      });
      commentList.value = response.data;
      console.log(commentList.value);
    } catch (err) {
      console.error('Failed to fetch articles:', err);
    }
  };

  const deleteComment = function (id, commentId) {  
    axios({
      method: 'DELETE',
      url: `http://127.0.0.1:8000/api/v1/articles/${id}/comments/${commentId}`,
      headers: {
        Authorization: localStorage.getItem('token'),
      },
    })
    .then(function(response) {
      console.log('Comment deleted:', response.data)
    })
    .catch(function(error) {
      console.log(error)
    })      
  }

  const read_map = async function (city, gu,bank) {  
    try {
      const response = await axios({
        method: 'POST',
        url: `http://127.0.0.1:8000/api/v1/outerapi/kakaomaps/`,
        data: {
          city: city,
          gu: gu,
          bank: bank,
        }
      });
      return response.data;
    } catch (error) {
      console.error('Failed to fetch map data:', error);
      throw error; // 에러를 던져 호출자가 처리하도록 합니다.
    }
  };

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
    newComment,
    viewComment,
    commentList,
    deleteComment,
    read_map,
    map_data,
    signup,
  }
})
