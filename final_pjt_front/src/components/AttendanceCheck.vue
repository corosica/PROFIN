<template>
    <div class="calendar-container">
      <div class="calendar">
        <div class="calendar-header">
          <button @click="prevMonth">&lt;</button>
          <span>{{ currentYear }}년 {{ currentMonth + 1 }}월</span>
          <button @click="nextMonth">&gt;</button>
        </div>
        <div class="calendar-body">
          <div class="day" v-for="(day, index) in days" :key="index">
            <div
              :class="['date', { checked: isChecked(day) }]"
              @click="toggleAttendance(day)"
            >
              {{ day.date }}
            </div>
          </div>
        </div>
      </div>
      <div v-if="dialog" class="dialog">
        <div class="dialog-content">
          <p>{{ dialogMessage }}</p>
          <button @click="dialog = false">확인</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        currentYear: new Date().getFullYear(),
        currentMonth: new Date().getMonth(),
        days: [],
        attendance: [],
        dialog: false,
        dialogMessage: '',
      };
    },
    mounted() {
      this.generateCalendar();
    },
    methods: {
      generateCalendar() {
        const daysInMonth = new Date(this.currentYear, this.currentMonth + 1, 0).getDate();
        this.days = [];
        for (let i = 1; i <= daysInMonth; i++) {
          this.days.push({ date: i, month: this.currentMonth, year: this.currentYear });
        }
      },
      prevMonth() {
        if (this.currentMonth === 0) {
          this.currentYear--;
          this.currentMonth = 11;
        } else {
          this.currentMonth--;
        }
        this.generateCalendar();
      },
      nextMonth() {
        if (this.currentMonth === 11) {
          this.currentYear++;
          this.currentMonth = 0;
        } else {
          this.currentMonth++;
        }
        this.generateCalendar();
      },
      isChecked(day) {
        return this.attendance.some(
          (d) => d.date === day.date && d.month === day.month && d.year === day.year
        );
      },
      toggleAttendance(day) {
        const today = new Date();
        const isToday =
          day.date === today.getDate() &&
          day.month === today.getMonth() &&
          day.year === today.getFullYear();
  
        if (this.isChecked(day)) {
          if (isToday) {
            this.dialogMessage = '오늘은 이미 출석 완료하였습니다.';
          } else {
            this.dialogMessage = `${day.year}년 ${day.month + 1}월 ${day.date}일에 이미 출석하였습니다.`;
          }
          this.dialog = true;
        } else {
          this.attendance.push(day);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .calendar-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
  }
  
  .calendar {
    border: 1px solid #ddd;
    padding: 20px;
    border-radius: 10px;
    width: 300px;
    text-align: center;
  }
  
  .calendar-header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 10px;
  }
  
  .calendar-body {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    gap: 5px;
  }
  
  .day {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .date {
    width: 40px;
    height: 40px;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 50%;
    cursor: pointer;
    user-select: none;
  }
  
  .date.checked {
    background-color: #42b983;
    color: white;
  }
  
  .dialog {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    background: rgba(0, 0, 0, 0.5);
  }
  
  .dialog-content {
    background: white;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
  }
  </style>
  