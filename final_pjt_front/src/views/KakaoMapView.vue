<template>
    <div>
        <h2>지도</h2>
        <form @submit.prevent="findmap">
            <select id="city" v-model="selectedCity">
                <option v-for="city in cities" :key="city.city" :value="city.city">{{ city.city }}</option>
            </select>
            <select id="district" v-model="selectedGu">
                <option v-for="district in filteredDistricts" :key="district" :value="district">{{ district }}</option>
            </select>
            <input type="text" name="bank" id="bank" placeholder="은행을 입력하세요">
            <input type="submit" value="Submit" />
        </form>
    </div>
</template>

<script setup>
import { ref,computed } from 'vue'
const findmap = function (res) {
    console.log(selectedCity.value, selectedGu.value, res.target.bank.value);
}
const selectedCity = ref('');
const selectedGu = ref('');

const filteredDistricts = computed(() => {
      const city = cities.value.find(city => city.city === selectedCity.value);
      return city ? city.gu : [];
    });
const cities = ref([{
    "city": "제주특별자치도",
    "gu": ['제주시','서귀포시']
  },
  {
    "city": "인천광역시",
    "gu": ['옹진군','부평구','계양구','서구','강화군','중구','남동구','북구','동구','남구','연수구','미추홀구']
  },
  {
    "city": "울산광역시",
    "gu": ['울주군','중구','남구','동구','북구']
  },
  {
    "city": "세종특별자치시",
    "gu": ['세종시']
  },
  {
    "city": "서울특별시",
    "gu": ['용산구','성동구','성북구','강북구','도봉구','노원구','광진구','동대문구','구로구','동작구','중구','중랑구','관악구','영등포구','은평구','서대문구','마포구','강남구','양천구','금천구','강서구','종로구','서초구','송파구','강동구']
  },
  {
    "city": "부산광역시",
    "gu": ['강서구','연제구','수영구','사상구','기장군','서구','중구','동래구','남구','북구','해운대구','사하구','금정구','동구','영도구','부산진구']
  },
  {
    "city": "대전광역시",
    "gu": ['서구','유성구','대덕구','동구','중구']
  },
  {
    "city": "대전광역시",
    "gu": ['중구','동구','수성구','달성군','서구','남구','북구','달서구']
  },
  {
    "city": "광주광역시",
    "gu": ['동구','서구','북구','남구','광산구']
  }])


</script>

<style scoped>

</style>