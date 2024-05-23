<template>
  <div class="calendar-container">
    <div class="calendar">
      <div class="header">
        <span @click="prevMonth" class="nav-button">‹</span>
        <span class="month">{{ currentMonthName }}</span>
        <span @click="nextMonth" class="nav-button">›</span>
      </div>
      <div class="weekdays">
        <span v-for="day in weekdays" :key="day">{{ day }}</span>
      </div>
      <div class="days">
        <span 
          v-for="date in dates" 
          :key="date.key" 
          @click="selectDate(date.date)" 
          :class="{ 
            today: isToday(date.date), 
            selected: isSelected(date.date), 
            'other-month': date.isOtherMonth, 
            empty: date.isEmpty,
            weekend: isWeekend(date.date)
          }">
          {{ date.date && date.date.getDate() ? date.date.getDate() : '' }}
        </span>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue';

export default {
  props: {
    onDateClick: {
      type: Function,
      required: true
    }
  },
  setup(props) {
    const today = new Date();
    const selectedDate = ref(new Date(today.getFullYear(), today.getMonth(), today.getDate()));
    const currentYear = ref(today.getFullYear());
    const currentMonth = ref(today.getMonth());
    const weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];

    const currentMonthName = computed(() => {
      return new Date(currentYear.value, currentMonth.value).toLocaleString('default', { month: 'long', year: 'numeric' });
    });

    const dates = computed(() => {
      const start = new Date(currentYear.value, currentMonth.value, 1);
      const end = new Date(currentYear.value, currentMonth.value + 1, 0);

      const datesArray = [];

      // Add dates from the previous month
      for (let i = start.getDay(); i > 0; i--) {
        const prevDate = new Date(start);
        prevDate.setDate(start.getDate() - i);
        datesArray.push({ date: prevDate, isOtherMonth: true, key: `prev-${prevDate.getDate()}` });
      }

      // Add dates from the current month
      for (let i = 1; i <= end.getDate(); i++) {
        datesArray.push({ date: new Date(currentYear.value, currentMonth.value, i), isOtherMonth: false, key: `current-${i}` });
      }

      // Add empty dates to fill the last week if needed
      const lastDayOfWeek = end.getDay();
      if (lastDayOfWeek !== 6) { // 6 corresponds to Saturday
        for (let i = 1; i <= 6 - lastDayOfWeek; i++) {
          const nextDate = new Date(end);
          nextDate.setDate(end.getDate() + i);
          datesArray.push({ date: nextDate, isOtherMonth: true, key: `next-${nextDate.getDate()}` });
        }
      }

      return datesArray;
    });

    const isToday = (date) => {
      if (!date) return false;
      return date.getDate() === today.getDate() && date.getMonth() === today.getMonth() && date.getFullYear() === today.getFullYear();
    };

    const isSelected = (date) => {
      if (!date) return false;
      return date.getDate() === selectedDate.value.getDate() && date.getMonth() === selectedDate.value.getMonth() && date.getFullYear() === selectedDate.value.getFullYear();
    };

    const isWeekend = (date) => {
      if (!date) return false;
      return date.getDay() === 0 || date.getDay() === 6; // 0 is Sunday, 6 is Saturday
    };

    const selectDate = (date) => {
      if (!date) return;
      selectedDate.value = date;
      props.onDateClick(date);
    };

    const prevMonth = () => {
      if (currentMonth.value === 0) {
        currentMonth.value = 11;
        currentYear.value--;
      } else {
        currentMonth.value--;
      }
    };

    const nextMonth = () => {
      if (currentMonth.value === 11) {
        currentMonth.value = 0;
        currentYear.value++;
      } else {
        currentMonth.value++;
      }
    };

    return {
      currentYear,
      currentMonth,
      currentMonthName,
      weekdays,
      dates,
      isToday,
      isSelected,
      selectDate,
      prevMonth,
      nextMonth,
      isWeekend
    };
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700;900&display=swap');

* {
  font-family: 'Noto Sans KR', sans-serif; /* 전역 폰트 적용 */
}

.calendar-container {
  display: flex;
  justify-content: flex-start; /* 왼쪽 정렬 */
  padding-right: 15%;
  box-sizing: border-box;
}

.calendar {
  width: 100%;
  max-width: 700px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  margin: 10px 0 50px 0;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  background-color: #ffffff;
  color: #696969;
  font-weight: bold;
  font-size: 1.5rem;
}

.nav-button {
  cursor: pointer;
  user-select: none;
}

.weekdays {
  display: flex;
  background-color: #f0f0f0;
  padding: 10px 0;
  border-bottom: 1px solid #ddd;
}

.weekdays span {
  flex: 1;
  text-align: center;
  font-weight: bold;
  color: #777;
}

.days {
  display: flex;
  flex-wrap: wrap;
  padding: 10px;
  gap: 2px; /* 간격을 위해 gap 사용 */
}

.days span {
  flex: 1 0 calc(14.28% - 4px); /* 100% / 7 days - gap */
  text-align: center;
  padding: 30px 0;
  margin: 0;
  cursor: pointer;
  user-select: none;
  font-size: 1.2rem;
  border-radius: 50%; /* 원 모양을 위해 추가 */
  aspect-ratio: 1 / 1; /* 원 모양을 위해 추가 */
  transition: background-color 0.3s, color 0.3s;
}

.days span.today {
  background-color: #1abc9c;
  color: #fff;
  border-radius: 50%;
  font-weight: bold;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  position: relative;
  overflow: hidden;
}
.days span.today::after {
  color: #fff;
  font-size: 0.8rem;
  position: absolute;
  top: 5px;
  right: 5px;
}

.days span.selected {
  background-color: #007bff;
  color: #fff;
  border-radius: 50%;
  font-weight: bold;
}

.days span.other-month {
  color: #ccc;
}

.days span.empty {
  background-color: transparent;
  cursor: default;
}

.days span:hover {
  background-color: #f0f0f0;
}
</style>