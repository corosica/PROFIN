
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
  const userInfos = ref({})
  const ExchangeInfos = ref({})
  const DepositInfos = ref({})
  const DepositDetails = ref({})
  const SavingDetails = ref({})
  const SavingInfos = ref({})
  const buyProductList = ref([])
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
      sessionStorage.setItem('token','Token '+response.data.key)
      sessionStorage.setItem('username',username)
      getUserInfo()
      router.push({name:'Home'}).then(() => {
        // router.push가 완료된 후 새로고침을 수행
          router.go(0);
        });
    }).catch(function (err) {
      alert('아이디 비밀번호를 다시 확인해보세요')
      console.log(err)
    })
  }


  const signup = function (username,password1,password2,email,nickname,age, gender, asset, goal, job) {
    axios({
      method:'POST',
      url : 'http://127.0.0.1:8000/accounts/signup/',
      data : {
        username : username,
        password1 : password1,
        password2 : password2,
        email : email,
        nickname : nickname,
        age : age,
        gender : gender,
        asset : asset,
        goal : goal,
        job : job,
      }
    }).then(function (response) {
      login(username,password1)
      console.log(response.data)
    }).catch(function (err) {
      console.log(err)
    })
  }
  const viewArticles = async function (item) {
    try {
      const response = await axios({
        method: 'GET',
        url: `http://127.0.0.1:8000/api/v1/articles/${item}/`,
      });
      articleList.value = response.data;
      console.log(articleList.value);
    } catch (err) {
      console.error('Failed to fetch articles:', err);
    }
  };

  const getArticleById = function (item,id) {
    axios(
      {
      method : 'GET',
      url : `http://127.0.0.1:8000/api/v1/articles/${item}/${id}/`,
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
   
    
  const createArticles = function(item,title,contents) {  
    axios({ 
      method : 'POST',
      url : `http://127.0.0.1:8000/api/v1/articles/${item}/`,
      headers : {
        Authorization : sessionStorage.getItem('token'),
      },
        data : {
        title : title,
        content : contents
      }
    })
  }

  const deleteArticle = function(item,id) {  
    axios({
      method: 'DELETE',
      url: `http://127.0.0.1:8000/api/v1/articles/${item}/${id}/`,
      headers: {
        Authorization: sessionStorage.getItem('token'),
      },
    })
    .then(function(response) {
      console.log('Article deleted:', response.data)
    })
    .catch(function(error) {
      console.log(error)
    })      
  }

  const updateArticle = function(item,id, title, content) {
    axios({
      method: 'PUT',
      url: `http://127.0.0.1:8000/api/v1/articles/${item}/${id}/`,
      headers: {
        Authorization: sessionStorage.getItem('token'),
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

  const newComment = function (item,id, comment) {
    axios({
      method: 'POST',
      url: `http://127.0.0.1:8000/api/v1/articles/${item}/${id}/comments/`, // URL 형식 확인
      headers: {
        Authorization: sessionStorage.getItem('token'),
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

  const viewComment = async function (item,id) {
    try {
      const response = await axios({
        method: 'GET',
        url: `http://127.0.0.1:8000/api/v1/articles/${item}/${id}/comments/`,
      });
      commentList.value = response.data;
      console.log(commentList.value);
    } catch (err) {
      console.error('Failed to fetch articles:', err);
    }
  };

  const deleteComment = function (item,id, commentId) {  
    axios({
      method: 'DELETE',
      url: `http://127.0.0.1:8000/api/v1/articles/${item}/${id}/comments/${commentId}`,
      headers: {
        Authorization: sessionStorage.getItem('token'),
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
  const getUserInfo = async function () {
      // 회원정보 조회
    try {

      const response = await axios({
        method:'GET',
        url : 'http://127.0.0.1:8000/accounts/user/',
        headers: {
          Authorization: sessionStorage.getItem('token'),
        },
      })
      userInfos.value = response.data; //userInfos => 데이터 받아온거 posts역할
      sessionStorage.setItem('user_id',userInfos.value.pk)
    } catch(err) {
      console.error('Failed to fetch userInfo:', err);

    }
  }

  const changeUserInfo = async function (nickname, email, age, gender, asset, goal, job) {
    // 회원정보 조회
  await axios({
      method:'PATCH',
      url : 'http://127.0.0.1:8000/accounts/user/',
      headers: {
        Authorization: sessionStorage.getItem('token'),
      },
      data: {
      nickname : nickname,
      email : email,
      age : age,
      gender : gender,
      asset : asset,
      goal : goal,
      job : job,
      }
    }).then((response) => {
    
      router.go(-1)
      userInfos.value = response.data; //userInfos => 데이터 받아온거 posts역할
    }). catch((err) => {
    console.error('Failed to fetch userInfo:', err);
  })
}
  const getExchange = async function () {
    try {
      const response = await axios({
        method:'GET',
        url : 'http://127.0.0.1:8000/api/v1/outerapi/exchange/',
      })
      ExchangeInfos.value = response.data;
  
    } catch (err) {
      console.error('Failed to fetch articles:', err);
      throw err
    }
  }

    const getDeposit = async function () {
      try {
        const response = await axios({
          method:'GET',
          url : 'http://127.0.0.1:8000/api/v1/outerapi/deposit/',
        })
        DepositInfos.value = response.data;
        console.log(DepositInfos.value)
      }
      catch (err) {
        console.error('Failed to fetch articles:', err);
        if(err.message == 'Request failed with status code 404')
        {
          await axios({
            method:'GET',
            url : 'http://127.0.0.1:8000/api/v1/outerapi/deposit/saving',
          })
          router.go(0)
        }
        throw err
      }
    }
    const getDepositDetail = async function (id) {
      try {
        const response = await axios({
          method:'GET',
          url : `http://127.0.0.1:8000/api/v1/outerapi/deposit/${id}`,
        })
        DepositDetails.value = response.data;
        console.log(DepositDetails.value)
      }
      catch (err) {
        console.error('Failed to fetch articles:', err);
        throw err
      }
    }
    const getSaving = async function () {
      try {
        const response = await axios({
          method:'GET',
          url : 'http://127.0.0.1:8000/api/v1/outerapi/saving/',
        })
        SavingInfos.value = response.data;
        console.log(SavingInfos.value)
      }
      catch (err) {
        console.error('Failed to fetch articles:', err);
        if(err.message == 'Request failed with status code 404')
        {
          await axios({
            method:'GET',
            url : 'http://127.0.0.1:8000/api/v1/outerapi/saving/saving',
          })
          router.go(0)
        }
        throw err
      }
    }
    const getSavingDetail = async function (id) {
      try {
        const response = await axios({
          method:'GET',
          url : `http://127.0.0.1:8000/api/v1/outerapi/saving/${id}`,
        })
        SavingDetails.value = response.data;
        console.log(SavingDetails.value)
      }
      catch (err) {
        console.error('Failed to fetch articles:', err);
        throw err
      }
    }

    const buyProduct = async function (method,product_pk,option_pk) {
      try {
        const response = await axios({
          method:'POST',
          url : `http://127.0.0.1:8000/api/v1/outerapi/${method}/${product_pk}/${option_pk}/`,
          data : {},
          headers: {
            Authorization: sessionStorage.getItem('token'),
          },
        })
        console.log(response.data)
      }
      catch (err) {
        console.error('Failed to fetch articles:', err);
        throw err
      }
    }

    const getProductsList = async function () {
      try {
        const response = await axios({
          method:'GET',
          url : 'http://127.0.0.1:8000/api/v1/outerapi/search_deposit/',
          headers: {
            Authorization: sessionStorage.getItem('token'),
          },
        })
        buyProductList.value = response.data;
        console.log(buyProductList.value)
      }
      catch (err) {
        console.error('Failed to fetch articles:', err);
        throw err
      }

    }
    const normalRecommendList = ref([])
    const normalRecommend = async function () {
      try {
        const response = await axios({
          method:'GET',
          url : 'http://127.0.0.1:8000/api/v1/outerapi/recommend/normal/',
          headers: {
            Authorization: sessionStorage.getItem('token'),
          },
        })
        normalRecommendList.value = response.data;
        console.log(normalRecommendList.value)
      }
      catch (err) {
        console.error('Failed to fetch articles:', err);
        throw err
      }
    }
    const premiumRecommendList = ref([])
    const premiumRecommend = async function () {
      try {
        const response = await axios({
          method:'GET',
          url : 'http://127.0.0.1:8000/api/v1/outerapi/recommend/premium/',
          headers: {
            Authorization: sessionStorage.getItem('token'),
          },
        })
        premiumRecommendList.value = response.data;
        console.log(premiumRecommendList.value)
      }
      catch (err) {
        console.error('Failed to fetch articles:', err);
        throw err
      }
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
    newComment,
    viewComment,
    commentList,
    deleteComment,
    read_map,
    map_data,
    signup,
    getUserInfo,
    userInfos,
    getExchange,
    ExchangeInfos,
    getDeposit,
    DepositInfos,
    getDepositDetail,
    DepositDetails,
    SavingDetails,
    SavingInfos,
    getSaving,
    getSavingDetail,
    changeUserInfo,
    buyProduct,
    buyProductList,
    getProductsList,
    normalRecommendList,
    normalRecommend,
    premiumRecommendList,
    premiumRecommend,
  }
})
