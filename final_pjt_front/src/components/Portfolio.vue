<template>
  <div class="main-container">
    <div class="button-container">
      <button @click="showModal('Normal', '<span>&lt;Normal버전&gt;</span> <strong>100 포인트</strong>가 차감됩니다<br>계속하시겠습니까?')" class="btn">Normal</button>
      <button @click="showModal('Premium', '<strong>1000 포인트</strong>가 차감됩니다 <br>계속하시겠습니까?')" class="btn">Premium</button>
    </div>
    <div class="container border">
      <RouterView />
    </div>
    <Modal :visible="isModalVisible" :message="modalMessage" @confirm="handleConfirm" @cancel="handleCancel" />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import Modal from '@/components/Modal.vue';

const isModalVisible = ref(false);
const modalMessage = ref('');
const targetRoute = ref(null);
const router = useRouter();

const showModal = (routeName, message) => {
  targetRoute.value = { name: routeName };
  modalMessage.value = message;
  isModalVisible.value = true;
};

const handleConfirm = () => {
  isModalVisible.value = false;
  if (targetRoute.value) {
    router.push(targetRoute.value);
    targetRoute.value = null;
  }
};

const handleCancel = () => {
  isModalVisible.value = false;
  targetRoute.value = null;
};
</script>

<style scoped>
.main-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.button-container {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.btn {
  padding: 10px 20px;
  background-color: white;
  color: #1abc9c;
  text-decoration: none;
  border: 2px solid #1abc9c;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s, color 0.3s;
}

.btn:hover {
  background-color: #1abc9c;
  color: white;
}

.container.border {
  width: 100%;
  max-width: 1500px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  background-color: #f9f9f9;
}
</style>
