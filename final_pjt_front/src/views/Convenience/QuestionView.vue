<template>
    <div class="container mt-4">
      <div class="faq-section">
        <h1 class="faq-title">FAQ</h1>
        <div v-for="(faq, index) in faqs" :key="index" class="faq-item">
          <div class="faq-question" @click="toggleFaq(index)">
            {{ faq.question }}
            <span class="faq-toggle-icon">{{ faq.open ? '-' : '+' }}</span>
          </div>
          <!-- Updated: Separate container for v-html to avoid overriding child elements -->
          <div v-if="faq.open" class="faq-answer">
            <div v-html="faq.answer"></div> <!-- Safe usage of v-html -->
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const faqs = ref([
    { 
        question: "팀장님 하루만 대여가능한가요?", 
        answer: "현재 문의가 많은 관계로 대기표를 뽑고 기다려주세요.", 
        open: false 
    },
    { 
        question: "포인트는 어떻게 모으나요?", 
        answer: "게시글 작성시 30 point, 댓글 작성시 5 point, 출석체크시 50 point를 지급해드립니다.", 
        open: false 
    },
    { 
        question: "저에게 맞는 상품 추천은 어떻게 받나요?", 
        answer: "로그인 후 <strong>회원정보</strong> > <strong>포트폴리오</strong>를 선택하면 상품을 추천받으실 수 있습니다.", 
        open: false 
    },
    { 
      question: "비밀번호를 변경하고 싶어요.", 
      answer: "로그인 후 <strong>회원정보 > 비밀번호 변경</strong>을 선택하여 비밀번호를 변경할 수 있습니다.", 
      open: false 
    },
    {
      question: "회원 탈퇴를 하고싶어요.", 
      answer: "탈퇴를 원하시는 <strong>아이디</strong>와 함께 <strong>문의하기</strong> 게시판에 요청해주세요.", 
      open: false 
    },
    {
      question: "개인 정보 처리 방침은 어떻게 되나요?", 
      answer: "2024년 5월 25일 이후로 모든 개인정보는 파기될 예정입니다.", 
      open: false 
    }
  ]);
  
  const toggleFaq = (index) => {
    faqs.value[index].open = !faqs.value[index].open;
  };
  </script>
  
  
  
  <style scoped>
  
  .container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .faq-section {
    background: #eff8f4;
    border-radius: 8px;
    padding: 20px;
  }
  
  .faq-title {
    text-align: center;
    color: #5c5c6d;
    margin-bottom: 20px;
  }
  
  .faq-item + .faq-item {
    margin-top: 10px;
  }
  
  .faq-question {
    padding: 10px;
    background: #d2eee3;
    border-radius: 6px;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: bold;
  }
  
  .faq-answer {
    margin-top: 5px;
    padding: 10px;
    background: #ffffff;
    border-radius: 6px;
  }
  
  .faq-toggle-icon {
    font-size: 20px;
  }
  </style>
  