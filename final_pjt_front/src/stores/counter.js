import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
export const useCounterStore = defineStore('counter', () => {
  const token = ref(null)
  const articleList = ref([])
  const login = function () {
    axios({
      method : 'POST',
      url : 'http://127.0.0.1:8000/accounts/login/', //주소
      data : {
        username : 'testuser',
        password : 'ssafy11!'
      }
    }).then(function (response) {
      token.value = 'Token '+response.data.key
      console.log(token.value)
    }).catch(function (err) {
      console.log(err)
    })
  }
  const viewArticles = function () {
    axios({
      method : 'GET',
      url : 'http://127.0.0.1:8000/api/v1/articles/',
    })
    .then(function (response) {
      articleList.value = response.data
      console.log(articleList.value)
    }).catch(function (err) {
      console.log(err)
    })
  }
  const createArticles = function(title,contents) {  
    axios({ 
      method : 'POST',
      url : 'http://127.0.0.1:8000/api/v1/articles/',
      headers : {
        Authorization : token.value,
      },
        data : {
        title : title,
        content : contents
      }
    })
  }
  return { login,createArticles,viewArticles,token,articleList }
})
