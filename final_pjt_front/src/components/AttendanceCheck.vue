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
        <span v-for="date in dates" :key="date.key" @click="selectDate(date.date)" :class="{ today: isToday(date.date), selected: isSelected(date.date), 'other-month': date.isOtherMonth, empty: date.isEmpty }">
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
      const end = new Date(currentYear.value, currentMonth.value+1, 0);

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
      nextMonth
    };
  }
};
</script>

<style scoped>
.calendar-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.calendar {
  width: 100%;
  max-width: 400px;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: #f5f5f5;
  border-bottom: 1px solid #ddd;
}

.nav-button {
  cursor: pointer;
  user-select: none;
}

.month {
  font-weight: bold;
}

.weekdays {
  display: flex;
  background-color: #f9f9f9;
  padding: 10px;
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

}

.days span {
  flex: 1 0 14.28%; /* 100% / 7 days */
  text-align: center;
  padding: 10px;
  margin: 0px;
  cursor: pointer;
  user-select: none;

}

.days span.today {
  background-color: #ffd700;
  border-radius: 50%;
}

.days span.selected {
  background-color: #007bff;
  color: #fff;
  border-radius: 50%;
}

.days span.other-month {
  color: #aaa;
}

.days span.empty {
  background-color: transparent;
  cursor: default;
}

.days span:hover {
  background-color: #f0f0f0;
}
</style>
