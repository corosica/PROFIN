<template>
  <div>
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
          </div>
          <div class="carousel-item">
            <img src="/som2.jpg" class="d-block mx-auto img-fluid" alt="사진2">
          </div>
          <div class="carousel-item">
            <img src="/som3.jpg" class="d-block mx-auto img-fluid" alt="사진3">
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
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter()
</script>

<style scoped>
.carousel-item img {
  max-height: 500px; /* 원하는 이미지 최대 높이 설정 */
  object-fit: cover; /* 이미지를 잘라서 요소에 맞게 조정 */
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
</style>
