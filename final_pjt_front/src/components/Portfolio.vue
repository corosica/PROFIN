<template>
  <div class="main-container">
    <div class="button-container">
      <button @click="navigate('Normal')" class="btn">Normal</button>
      <button @click="navigate('Premium')" class="btn">Premium</button>
    </div>
    <RouterView />
    <Modal :visible="isModalVisible" :message="modalMessage" @confirm="handleConfirm" @cancel="handleCancel" />
  </div>
</template>

<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import Modal from './Modal.vue'; // Modal이 로컬 컴포넌트라고 가정

export default {
  components: { Modal },
  setup() {
    const router = useRouter();
    const isModalVisible = ref(false);
    const modalMessage = ref('');

    const navigate = (routeName) => {
      router.push({ name: routeName });
    };

    const handleConfirm = () => {
      isModalVisible.value = false;
    };

    const handleCancel = () => {
      isModalVisible.value = false;
    };

    return {
      navigate,
      isModalVisible,
      modalMessage,
      handleConfirm,
      handleCancel,
    };
  },
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
  gap: 30px; /* 버튼 간의 간격을 넓힘 */
  margin-bottom: 20px;
  position: relative;
  right: 10%;
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
  border-radius: 10px;
  background-color: #ffffff;
}
</style>
