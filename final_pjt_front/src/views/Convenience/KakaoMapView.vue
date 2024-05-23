<template>
  <div class="map-container">
    <h2>카카오 맵 보기</h2>
    <form @submit.prevent="findmap" class="map-form">
      <div class="selectors">
        <select id="city" v-model="selectedCity">
          <option v-for="city in cities" :key="city.city" :value="city.city">{{ city.city }}</option>
        </select>
        <select id="district" v-model="selectedGu">
          <option v-for="district in filteredDistricts" :key="district" :value="district">{{ district }}</option>
        </select>
      </div>
      <div class="search">
        <input type="text" id="bank" placeholder="은행을 입력하세요">
        <div class="seacrh-btn">
          <input type="submit" value="찾기">
        </div>
      </div>
    </form>
    <div id="map"></div>
  </div>
</template>



<script setup>
import { ref, onMounted, computed } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { useRouter } from 'vue-router';

let map = null;
let markers = []; // 마커를 저장할 배열
const counterStore = useCounterStore();
const router = useRouter();

onMounted(() => {
  if (window.kakao && window.kakao.maps) {
    initMap();
  } else {
    const script = document.createElement('script');
    /* global kakao */
    const api_key = import.meta.env.VITE_KAKAO_JAVA_SCRIPT_KEY
    script.onload = () => kakao.maps.load(initMap);
    script.src = `//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${api_key}&libraries=services`;
    document.head.appendChild(script);
  }
});

const initMap = () => {
  const container = document.getElementById('map'); // 어디에 담을건지 고르는것(div등)
  const options = { //옵션
    center: new kakao.maps.LatLng(35.093655296844,128.85567741474),
    level: 7,
  };

  // 지도 객체를 등록합니다.
  // 지도 객체는 반응형 관리 대상이 아니므로 initMap에서 선언합니다.
  map = new kakao.maps.Map(container, options);

  // 초기 마커 관련
  var position = new kakao.maps.LatLng(35.093655296844, 128.85567741474);

  // 마커를 생성합니다
  var marker = new kakao.maps.Marker({
    position: position
  });

  // 마커를 지도에 표시합니다.
  marker.setMap(map);
  markers.push(marker);
  // 마커에 커서가 오버됐을 때 마커 위에 표시할 인포윈도우를 생성합니다
  var iwContent = '<div style="padding:5px;">SSAFY 부울경!</div>'; // 인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다

  // 인포윈도우를 생성합니다
  var infowindow = new kakao.maps.InfoWindow({
    content: iwContent
  });

  // 마커에 마우스오버 이벤트를 등록합니다
  kakao.maps.event.addListener(marker, 'mouseover', function() {
    // 마커에 마우스오버 이벤트가 발생하면 인포윈도우를 마커위에 표시합니다
    infowindow.open(map, marker);
  });

  // 마커에 마우스아웃 이벤트를 등록합니다
  kakao.maps.event.addListener(marker, 'mouseout', function() {
    // 마커에 마우스아웃 이벤트가 발생하면 인포윈도우를 제거합니다
    infowindow.close();
  });
};

// 지도 검색 API 요청
const findmap = async function(res) {
  try {
    clearMarkers();
    const map_data = await counterStore.read_map(selectedCity.value, selectedGu.value, res.target.bank.value);
    console.log(map_data);
    panTo(map_data.meta.x, map_data.meta.y); // 이동
    makeMarker(map_data.documents);
  } catch (error) {
    console.log(error);
  }
}

// 입력받은 좌표 정보를 받아오는것
const selectedCity = ref('');
const selectedGu = ref('');

const filteredDistricts = computed(() => { // 첫번째 선택항목 변경시 두번째 선택항목도 바뀌게 하는 코드
  const city = cities.value.find(city => city.city === selectedCity.value);
  return city ? city.gu : [];
});

const cities = ref([
  // 시군구 지역코드
  {
    "city": "서울특별시",
    "gu": ['용산구', '성동구', '성북구', '강북구', '도봉구', '노원구', '광진구', '동대문구', '구로구', '동작구', '중구', '중랑구', '관악구', '영등포구', '은평구', '서대문구', '마포구', '강남구', '양천구', '금천구', '강서구', '종로구', '서초구', '송파구', '강동구']
  },
  {
    "city": "부산광역시",
    "gu": ['강서구', '연제구', '수영구', '사상구', '기장군', '서구', '중구', '동래구', '남구', '북구', '해운대구', '사하구', '금정구', '동구', '영도구', '부산진구']
  },
  {
    "city": "제주특별자치도",
    "gu": ['제주시', '서귀포시']
  },
  {
    "city": "인천광역시",
    "gu": ['옹진군', '부평구', '계양구', '서구', '강화군', '중구', '남동구', '북구', '동구', '남구', '연수구', '미추홀구']
  },
  {
    "city": "울산광역시",
    "gu": ['울주군', '중구', '남구', '동구', '북구']
  },
  {
    "city": "세종특별자치시",
    "gu": ['세종시']
  },
  {
    "city": "대전광역시",
    "gu": ['서구', '유성구', '대덕구', '동구', '중구']
  },
  {
    "city": "대전광역시",
    "gu": ['중구', '동구', '수성구', '달성군', '서구', '남구', '북구', '달서구']
  },
  {
    "city": "광주광역시",
    "gu": ['동구', '서구', '북구', '남구', '광산구']
  }
]);

function panTo(center_x, center_y) {
  // 이동할 위도 경도 위치를 생성합니다
  var moveLatLon = new kakao.maps.LatLng(center_y, center_x);

  // 지도 중심을 부드럽게 이동시킵니다
  // 만약 이동할 거리가 지도 화면보다 크면 부드러운 효과 없이 이동합니다
  map.panTo(moveLatLon);
}

var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/places_category.png";

function makeMarker(data) {
  var imageSize = new kakao.maps.Size(27, 28);
  var imgOptions = {
    spriteSize: new kakao.maps.Size(72, 208),
    spriteOrigin: new kakao.maps.Point(46, 0),
    offset: new kakao.maps.Point(11, 28)
  };
  var infowindow = new kakao.maps.InfoWindow({
    zIndex: 1
  });
  var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize, imgOptions);
  for (const info of data) {
    var marker = new kakao.maps.Marker({
      map: map,
      position: new kakao.maps.LatLng(info.y, info.x),
      title: info.place_name,
      image: markerImage
    });
    markers.push(marker);
    (function(marker, title) {
      kakao.maps.event.addListener(marker, 'mouseover', function() {
        infowindow.setContent('<div style="padding:5px; max-width: 150px; word-wrap: break-word; white-space: normal; overflow: hidden;">' + title + '</div>')
        infowindow.open(map, marker);
      });

      kakao.maps.event.addListener(marker, 'mouseout', function() {
        infowindow.close();
      });
    })(marker, info.place_name);
  }
}

function clearMarkers() {
  markers.forEach(marker => marker.setMap(null));
  markers = [];
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');

* {
  font-family: 'Noto Sans KR', sans-serif; /* 전역 폰트 적용 */
}

.map-container {
  font-family: 'Arial', sans-serif;
  max-width: 800px;
  margin: 40px auto;
  background: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h2 {
  color: #4a4a4a;
  margin-bottom: 20px;
  text-align: center;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  width: 100%;
}

form .selectors {
  width: 100%;
  display: flex;
  justify-content: space-between;
}

select {
  width: 49%; /* 각 select는 가용 공간의 약 50%를 차지하도록 설정 */
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background: #f8f9fa;
}

.search {
  width: 50%; /* search 부분이 전체 가용 공간의 50%를 차지하도록 설정 */
  display: flex;
  align-items: center;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background: #f8f9fa;
}

input[type="text"], input[type="submit"] {
  padding: 8px;
  color: #ccc;
  border: none;
  flex: 1;
}

.search .seacrh-btn input[type="submit"] {
  padding: 8px 25px; /* 패딩 증가 */
  font-size: 16px; /* 폰트 크기 조정 */
  background-color: #0266d1; /* 배경색 */
  color: white; /* 글자색 */
  border: none; /* 테두리 없음 */
  cursor: pointer; /* 클릭 가능한 커서 스타일 */
  transition: background-color 0.3s ease; /* 배경색 변경 시 애니메이션 효과 */
  border-radius: 8px; /* 둥근 모서리 */
}

.search .seacrh-btn input[type="submit"]:hover {
  background-color: #03458b; /* 호버 시 배경색 변경 */
}

#map {
  width: 100%;
  height: 500px;
  margin-top: 20px;
  border-radius: 5px;
}
</style>
