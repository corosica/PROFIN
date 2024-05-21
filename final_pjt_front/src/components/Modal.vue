<template>
    <div class="modal-overlay" v-if="visible" @click="overlayClick">
      <div class="modal-content" @click.stop>
        <p v-html="message"></p>
        <div class="button-group">
          <button class="confirm-btn" @click="confirm">확인</button>
          <button class="cancel-btn" @click="cancel">취소</button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const props = defineProps({
    visible: Boolean,
    message: String,
  });
  
  const emit = defineEmits(['confirm', 'cancel']);
  
  const confirm = () => {
    emit('confirm');
  };
  
  const cancel = () => {
    emit('cancel');
  };
  
  const overlayClick = (event) => {
    if (event.target.classList.contains('modal-overlay')) {
      cancel();
    }
  };
  </script>
  
  <style scoped>
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .modal-content {
    background-color: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: center;
    max-width: 400px;
    width: 100%;
  }
  
  .button-group {
    display: flex;
    justify-content: space-around;
    margin-top: 20px;
  }
  
  button {
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s;
  }
  
  .confirm-btn {
    background-color: #1abc9c;
    color: white;
  }
  
  .confirm-btn:hover {
    background-color: #16a085;
  }
  
  .cancel-btn {
    background-color: #e74c3c;
    color: white;
  }
  
  .cancel-btn:hover {
    background-color: #c0392b;
  }
  </style>
  