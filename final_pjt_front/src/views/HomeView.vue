<template>
  <div class="container">
    <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="/som1.jpg" class="d-block mx-auto img-fluid" alt="사진1">
          <div class="carousel-caption d-none d-md-block">
            <h1>단복단복!</h1>
            <h1>입맛대로 이자 받아요</h1>
            <h5>부자되세용</h5>
            <p>계속 설명</p>
          </div>
        </div>
        <div class="carousel-item">
          <img src="/som2.jpg" class="d-block mx-auto img-fluid" alt="사진2">
          <div class="carousel-caption d-none d-md-block">
            <h1>만나서</h1>
            <h1>반갑습니다</h1>
            <h5>Slide 2</h5>
            <p>Description for slide 2.</p>
          </div>
        </div>
        <div class="carousel-item">
          <img src="/som3.jpg" class="d-block mx-auto img-fluid" alt="사진3">
          <div class="carousel-caption d-none d-md-block">
            <h1>나를 위한</h1>
            <h1>금융 상품 추천</h1>
            <h5>또봬요</h5>
            <p>Description for slide 3.</p>
          </div>
        </div>
      </div>
      <button class="carousel-control-prev custom-control" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next custom-control" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
    <div class="info-section">
      <div class="icons">
        <div class="icon">
          <img src="/PROFIN.png" alt="전체계좌조회">
          <p>전체계좌조회</p>
        </div>
        <div class="icon">
          <img src="/PROFIN.png" alt="즉시이체">
          <p>즉시이체</p>
        </div>
        <div class="icon">
          <img src="/PROFIN.png" alt="상품공시실">
          <p>상품공시실</p>
        </div>
        <div class="icon">
          <img src="/PROFIN.png" alt="영업점안내">
          <p>영업점안내</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter()
</script>

<style scoped>
.carousel-caption{
  position: absolute;
  top: 40%;
  transform: translate(-50%, -50%);
  text-align: center;
}
.carousel-item img {
  max-height: 500px;
  object-fit: cover;
}

.custom-control {
  top: 50%;
  transform: translateY(-50%);
}

.carousel-control-prev, .carousel-control-next {
  height: auto;
  width: 5%;
}

.carousel-inner {
  position: relative;
}

.carousel-inner img {
  width: 100%;
}

.carousel-control-prev {
  left: 10px;
}

.carousel-control-next {
  right: 10px;
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
