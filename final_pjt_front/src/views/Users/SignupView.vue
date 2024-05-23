<template>
  <div class="signup-container">
    <h1>회원가입</h1>
    <br>
    <form @submit.prevent="signup" class="signup-form">
      <div class="form-group">
        <label for="username">아이디: </label>
        <div class="d-flex row">

          <input type="text" id="username" v-model="username" required placeholder="필수" style="width: 80%; margin:auto">
          <button @click.prevent="check_user" class="check-button col-2">중복체크</button>
        </div>
        <p v-if="checked">아이디 사용이 가능합니다</p>
      </div>
      <div class="form-group">
        <label for="password">비밀번호: </label>
        <input type="password" id="password" v-model="password" required placeholder="필수">
      </div>
      <div class="form-group">
        <label for="confirmPassword">비밀번호 확인: </label>
        <input type="password" id="confirmPassword" v-model="confirmPassword" required placeholder="필수">
      </div>
      <div class="form-group">
        <label for="nickname">닉네임: </label>
        <input type="text" id="nickname" v-model="nickname">
      </div>
      <div class="form-group">
        <label for="email">이메일: </label>
        <input type="email" id="email" v-model="email" required placeholder="필수">
      </div>
      <div class="form-group">
        <label for="age">나이: </label>
        <input type="number" id="age" v-model="age" required placeholder="필수">
      </div>
      <div class="form-group">
          <label>성별: </label>
          <div class="gender-options no-wrap">
            <label class="gender-option">
              <input name="gender" value="남성" type="radio" v-model="gender">
              남성
            </label>
            <label class="gender-option">
              <input name="gender" value="여성" type="radio" v-model="gender">
              여성
            </label>
            <label class="gender-option">
              <input name="gender" value="비공개" type="radio" v-model="gender">
              비공개
            </label>
          </div>
        </div>
      <div class="form-group">
        <label for="asset">자산: </label>
        <input type="number" id="asset" v-model="asset" placeholder="만원 단위입니다.">
      </div>      
      <div class="form-group">
          <label for="goal">목표: </label>
          <select id="goal" v-model="goal" required>
            <option value="" disabled selected>목표를 선택하세요</option>
            <option value="무계획">무계획</option>
            <option value="안전형">안전형</option>
            <option value="수익형">수익형</option>
          </select>
        </div>
      <div class="form-group">
        <label for="job">직업: </label>
        <input type="text" id="job" v-model="job">
      </div>
      
      <br>
      <button type="submit" class="signup-button">회원가입</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useCounterStore } from '@/stores/counter';

const checked = ref(false);
const username = ref('');
const email = ref('');
const password = ref('');
const confirmPassword = ref('');
const nickname = ref('');
const age = ref('');
const gender = ref('male'); // 성별 선택을 위한 변수
const asset = ref('');
const goal = ref('');
const job = ref('');
const router = useRouter();
const ans = ref('');
const counterStore = useCounterStore();
const signup = () => {
  if (checked.value === false) {
    alert('아이디 중복체크를 해주세요.');
  }
  else if (!(username.value && password.value && confirmPassword.value && email.value && age.value)) {
    alert('필수 입력사항을 확인하세요.');
  }
  else if (password.value !== confirmPassword.value) {
    alert('비밀번호가 일치하지 않습니다.');
    return;
  }
  else {
    counterStore.signup(username.value, password.value, confirmPassword.value, email.value, nickname.value, age.value, gender.value, asset.value, goal.value, job.value);
  }
};

const check_user = async () => {
  await counterStore.check_user(username.value);
  ans.value = (counterStore.isUser);
  console.log(ans.value);
  if (ans.value == 'No'){
    checked.value = true;
    alert('아이디 사용이 가능합니다.');

  }
  else {
    checked.value = false;

    alert('이미 사용중인 아이디입니다.');
  }
};
</script>

<style scoped>
.signup-container {
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
  border: 1px solid #dcdcdc;
  border-radius: 8px;
  background-color: #f9f9f9;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.signup-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-group input,
.form-group select {
  width: 100%;
  padding: 8px;
  border: 1px solid #dcdcdc;
  border-radius: 4px;
  box-sizing: border-box;
}

.gender-options {
    display: flex;
    gap: 50px;
  }
  
.no-wrap {
  white-space: nowrap;
}

.signup-button {
  padding: 10px 15px;
  border: none;
  background-color: #1abc9c;
  color: #ffffff;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.check-button {
  padding: 10px 15px;
  border: none;
  color: black;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.signup-button:hover {
  background-color: #16a085;
}

.no-wrap {
  white-space: nowrap;
}

</style>
