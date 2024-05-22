<template>
  <div class="container">
    <div class="real-container">
      <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-indicators">
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
          <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
        </div>
        <div class="carousel-inner">
          <div class="carousel-item active">
            <div class="carousel-content">
              <div class="text-section">
                <h1>나를 위한 금융상품 추천</h1>
              </div>
              <div class="image-section">
                <img src="/som2.jpg" alt="추천 이미지" class="banner-image" />
              </div>
            </div>
          </div>
          <div class="carousel-item">
            <div class="carousel-content">
              <div class="text-section">
                <h1>만나서</h1>
                <h1>반갑습니다</h1>
                <h5>Slide 2</h5>
                <p>Description for slide 2.</p>
              </div>
              <div class="image-section">
                <img src="/som2.jpg" alt="사진2" class="banner-image" />
              </div>
            </div>
          </div>
          <div class="carousel-item">
            <div class="carousel-content">
              <div class="text-section">
                <h1>나를 위한</h1>
                <h1>금융 상품 추천</h1>
                <h5>또봬요</h5>
                <p>Description for slide 3.</p>
              </div>
              <div class="image-section">
                <img src="/som3.jpg" alt="사진3" class="banner-image" />
              </div>
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
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter()
</script>

<style scoped>
.real-container {
  width: 100%;
}
.carousel-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #f0f8ff; /* 밝은 파란색 배경 */
  color: #000; /* 검정색 텍스트 */
  padding: 20px;
  height: 100%;
}
.text-section {
  max-width: 50%;
}
.text-section h1 {
  font-size: 2rem;
  margin-bottom: 10px;
}
.image-section {
  max-width: 50%;
}
.banner-image {
  width: 100%;
  height: auto;
}
.carousel-caption {
  position: absolute;
  top: 40%;
  transform: translate(-50%, -50%);
  text-align: center;
  width: 100%;
}
.carousel-item img {
  max-height: 500px;
  object-fit: cover;
  max-width: 1100px;
}
.custom-control {
  top: 50%;
  transform: translateY(-50%);
}
.carousel-control-prev, .carousel-control-next {
  height: auto;
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
