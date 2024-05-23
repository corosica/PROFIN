<template>
  <div class="container">
    <div id="carouselExampleDark" class="carousel slide carousel-dark" data-bs-ride="carousel">
      <div>
        <button class="carousel-control-prev custom-control" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <div class="carousel-indicators">
          <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
          <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="1" aria-label="Slide 2"></button>
          <button type="button" data-bs-target="#carouselExampleDark" data-bs-slide-to="2" aria-label="Slide 3"></button>
        </div>
        <button class="carousel-control-next custom-control" type="button" data-bs-target="#carouselExampleDark" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active" @click="navigate('Portfolio')" title="상품 추천 페이지로 이동합니다">
          <img src="/상품추천.png" class="d-block w-100" alt="추천 이미지">
          <div class="carousel-caption left-top">
            <h1 class="bold-text">나를 위한</h1>
            <h1 class="bold-text">금융 상품 추천</h1>
            <div class="sub-text">
              <h5>서로 다른 성향과 목적</h5>
              <h5>나에게 맞는 상품이 궁금하다면?</h5>
            </div>
          </div>
        </div>
        <div class="carousel-item" @click="navigate('Deposit')" title="예적금 조회 페이지로 이동합니다">
          <img src="/돼지.png" class="d-block w-100" alt="핑크 돼지">
          <div class="carousel-caption left-top">
            <h1 class="bold-text">예금 적금</h1>
            <h1 class="bold-text">입맛대로 담기</h1>
            <div class="sub-text">
              <h5>다양한 상품들</h5>
              <h5>한 눈에 비교해보세요</h5>
            </div>
          </div>
        </div>
        <div class="carousel-item" @click="navigate('Portfolio')" title="PROFIN 소개 페이지로 이동합니다">
          <img src="/돼지.png" class="d-block w-100" alt="사진3">
          <div class="carousel-caption left-top">
            <h1 class="bold-text">만나서</h1>
            <h1 class="bold-text">반갑습니다</h1>
            <div class="sub-text">
              <h5>PROFIN에 대해</h5>
              <p>더 자세히 알고싶나요?</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="info-section">
      <div class="icons">
        <div class="icon">
          <img src="/PROFIN.png" @click="navigate('Exchange')" alt="환율 계산기" title="환율 계산기">
          <p>환율 계산기</p>
        </div>
        <div class="icon" @click="navigate('Kakaomap')" alt="은행찾기" title="은행찾기">
          <img src="/PROFIN.png" alt="은행찾기">
          <p>은행찾기</p>
        </div>
        <div class="icon">
          <img src="/PROFIN.png" @click="navigate('Community')" alt="커뮤니티" title="커뮤니티">
          <p>커뮤니티</p>
        </div>
        <div class="icon">
          <img src="/PROFIN.png" @click="navigate('Answer')" alt="문의하기" title="문의하기">
          <p>문의하기</p>
        </div>
      </div>
    </div>

    <div>
      <AttendanceCheck  @dateClick="handleDateClick"/>
      <button @click="checkAttendance">출석체크</button>
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import AttendanceCheck from '@/components/AttendanceCheck.vue';
import axios from 'axios';
const router = useRouter();
const message = ref('');
const today = new Date().toISOString().split('T')[0]

const navigate = (routeName) => {
  router.push({ name: routeName });
};


const checkAttendance = async () => {
  try {
        const response = await axios({
              method:'POST',
              url : 'http://127.0.0.1:8000/api/v1/outerapi/attendance/',
              headers: {
                Authorization: sessionStorage.getItem('token'),
              },
            })
        message.value = response.data.message
      } catch (error) {
        if (error.response) {
          message.value = error.response.data.message
        } else {
          message.value = 'An error occurred.'
        }
      } finally{
        alert(message.value)
      }
}
const handleDateClick = (date) => {
      if (date === today) {
        checkAttendance()
      }
    }
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');

* {
  font-family: 'Noto Sans KR', sans-serif; /* 전역 폰트 적용 */
}

.carousel-item {
  position: relative;
  cursor: pointer; /* 커서 모양 변경 */
}

.carousel-caption {
  color: #fff;
  border-radius: 10px;
  text-align: left;
  top: 50%;
  transform: translateY(-50%);
  position: absolute;
  width: auto;
  max-width: 50%;
}

.left-top {
  left: 15%;
  height: 80%;
  transform: translateY(-50%);
}

.bold-text {
  font-weight: 700; /* 폰트 굵게 설정 */
  font-size: 45px;
  margin: 10px 0;
}

.sub-text {
  font-weight: 400; /* 부제목 폰트 설정 */
  font-size: 18px;
  padding-top: 10px;
  margin: 10px 0;
}

.carousel-item img {
  width: 100%;
  height: 500px;
  object-fit: cover;
}

.custom-control {
  top: 50%;
  transform: translateY(-50%);
}

.carousel-control-prev,
.carousel-control-next {
  height: auto;
}

.carousel-inner {
  position: relative;
}

.info-section {
  text-align: center;
  margin-top: 20px;
}

.info-section h2 {
  font-size: 1.5rem;
  margin-bottom: 10px;
}

.info-section p {
  font-size: 1rem;
  color: #666;
}

.icons {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.icon {
  margin: 0 10px;
  text-align: center;
  cursor: pointer; /* 커서 모양 변경 */
}

.icon img {
  width: 50px;
  height: 50px;
}

.icon p {
  margin-top: 5px;
  font-size: 0.9rem;
}
</style>
