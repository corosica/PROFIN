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
        answer: "대기표를 뽑고 기다려주세요.", 
        open: false 
    },
    { 
      question: "비밀번호를 변경하고 싶어요.", 
      answer: "로그인 후 <strong>회원정보 > 비밀번호 변경</strong>을 선택하여 비밀번호를 변경할 수 있습니다.", 
      open: false 
    },
    { 
      question: "비밀번호를 잊어버렸어요.", 
      answer: "로그인 화면에서 <strong>비밀번호 찾기</strong> 옵션을 사용하여 비밀번호를 재설정하세요.", 
      open: false 
    },
    {
      question: "회원 탈퇴를 하고싶어요.", 
      answer: "현재 기능상의 문제로 회원 탈퇴가 불가능합니다.", 
      open: false 
    },
    {
      question: "개인 정보 처리 방침은 어떻게 되나요?", 
      answer: "개인 정보 처리 방침은 사이트 하단 개인정보 처리방침에서 확인 가능해요.", 
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
  