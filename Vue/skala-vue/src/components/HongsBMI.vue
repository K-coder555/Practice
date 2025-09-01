<template>
  <div class="m-3">
    <h3>홍길동의 BMI 계산기</h3>
    <div class="mb-2">
      <label for="heightInput" class="form-label">키 (cm)</label>
      <input v-model="height" id="heightInput" type="number" class="form-control">
    </div>
    <div class="mb-2">
      <label for="weightInput" class="form-label">체중 (kg)</label>
      <input v-model="weight" id="weightInput" type="number" class="form-control">
    </div>
    <div class="mt-3">
      <p>BMI 지수: {{ bmi.toFixed(2) }}</p>
      <p>판정: {{ bmiMessage }}</p>
    </div>
    <div>
      <h2>음식먹기</h2>
      <button @click="weight++">햄버거(+1kg)</button><button @click="weight+=2">피자(+2kg)</button>
    </div>
    <div>
      <h2>기술연습</h2>
      <button @click="weight--">걷기(-1kg)</button><button @click="weight-=2">달리기(-2kg)</button>
    </div>
    
      
  </div>
</template>
<script setup>
import { ref, computed, watch } from "vue";

const height = ref(170);
const weight = ref(60);

const bmi = computed(() => {
  if (height.value <= 0) return 0;
  return weight.value / ((height.value / 100) * (height.value / 100));
});

const bmiMessage = ref('');

// bmi 값이 변경될 때마다 감지하여 메시지를 업데이트합니다.
watch(bmi, (newBmiValue) => {
  if (newBmiValue < 18.5) {
    bmiMessage.value = "저체중";
  }
  else if (newBmiValue >= 18.5 && newBmiValue < 23) {
    bmiMessage.value = "정상";
  }
  else if (newBmiValue >= 23 && newBmiValue < 25) {
    bmiMessage.value = "과체중";
  }
  else {
    bmiMessage.value = "비만";
  }
}, { immediate: true }); // immediate: true 옵션으로 컴포넌트 로드 시 즉시 실행
</script>